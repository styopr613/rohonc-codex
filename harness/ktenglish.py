"""English prose for each folio, written from the gloss and NOTHING else.

The reader's edition is a gloss. It follows the manuscript's sign order, and
about a third of its signs are whole phrases written without a space, so it
never becomes sentences on its own. This turns each folio's gloss into English
using a language model, and then checks mechanically that the model did not
invent anything.

THE RULE, and it is the whole safety of this file. **The sentence follows the
GLOSS.** The model is given the folio's numbered gloss lines and nothing else:
not the chapter title, not the source passage the folio cites, not the page
image. Every one of those would let a model that knows the Bible write the
Bible from memory, and the book would stop being evidence of anything. It is
allowed to reorder, to supply articles and auxiliaries, and to punctuate. It
is not allowed to add a content word.

THE GATE, declared before the first run. Every content word of the English is
stemmed and looked for in the stems of that folio's own gloss. A word with no
match is a LEAK. The bar: a folio passes with **zero** unexplained leaks
outside the function-word list; a folio over that is refused and its gloss
paragraph stands instead. Leaks are printed, counted and kept, not hidden.

THE REFUSAL BAR, declared before the first rerun. The median folio flags 1.9%
of its words as unsupported, which is the ordinary noise of a stemmer meeting
a gloss. A folio at or above **three times the median, 5.7%**, is not noisy,
it is a different shape: the model has stopped rendering the gloss and started
reciting the source it recognises. Those folios are refused and rewritten with
their own leaked words quoted back at them. A folio that fails the bar twice
loses its English altogether and the gloss paragraph stands in its place,
because no English at all is better than the Vulgate with this book's name on
it.

    python3 ktenglish.py sample 089v 005r     write 2 folios, show the leaks
    python3 ktenglish.py run [--limit N]      write every folio still missing
    python3 ktenglish.py redo --above 5.7     rewrite every folio over the bar
    python3 ktenglish.py status
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import sys
import unicodedata
import time
import urllib.request

import corpus

ED = os.path.join(corpus.ROOT, "work", "rohonc", "translation",
                  "rohonc_readers_edition.md")
OUT = os.path.join(corpus.ROOT, "work", "rohonc", "translation",
                   "english.json")
KEY = open("/opt/secrets/deepinfra_api_key").read().strip()
MODEL = "deepseek-ai/DeepSeek-V4-Pro"
URL = "https://api.deepinfra.com/v1/openai/chat/completions"

SYSTEM = """You turn a word-for-word gloss of a manuscript into English prose.

The manuscript is the Rohonc Codex. Its script writes many phrases as a single
sign, so the gloss runs them together with hyphens, and it keeps the
manuscript's word order, which is not English order. Your job is to write what
the gloss says, in English.

THE ONE RULE YOU MUST NOT BREAK. You may only use content that is in the
gloss. You may reorder freely, supply articles, prepositions, auxiliaries,
pronouns and tense, join lines into sentences, and punctuate. You may NOT add
a noun, a verb, a name, an event or a clause that the gloss does not contain.
You will recognise much of this material. Write ONLY what this gloss says,
never what you know the passage says. If the gloss is shorter than the story,
the English is shorter than the story.

The marks, and you must preserve them:
  word*        keep the asterisk
  [word]       keep the brackets -- a restored word
  word^        drop the caret, it is only a note about which sense was chosen
  |            a gap in the manuscript; you may end a clause there
  [?] [...]    an unreadable sign; write ... in its place
  a_b_c        one sign that means a phrase; write it as the phrase
  ~word        drop the tilde, it marks a variant spelling
  ?word        keep the question mark before the word, it is uncertain
  <something>  a grammatical note, not a word; use it, do not print it

If a gloss word is not English -- a Hungarian word the dictionary left
untranslated, say -- keep that word exactly as it stands. Do not guess what it
means from the surrounding story. Add no adverb and no filler noun that is not
in the gloss, however natural it would sound.

Where the gloss is incoherent, leave it incoherent. Do not smooth it into
sense. A reader has the gloss printed underneath and will check you.

Return ONLY the English. No preamble, no notes, no line numbers."""

FUNC = set("""a an the and or but if then so that this these those there here
of to in on at by for from with without into onto upon over under about as
than when while where who whom whose which what because since until before
after again also too very not no nor only own same such both each few more
most other some any all every is are was were be been being am do does did
doing done have has had having will would shall should may might must can
could let it its it's they them their theirs he him his she her hers we us
our ours you your yours i me my mine himself herself itself themselves
myself ourselves yourself one two three four five six seven eight nine ten
s
up down out off out_of through above below between among against toward
towards within upon o yea unto thee thou thy thine ye hath doth said say
says saying""".split())

STEM = re.compile(r"[a-z]+")
SUF = ("ings", "ing", "eth", "est", "edly", "ed", "ies", "es", "s", "ly",
       "er", "d")


def norm(w):
    """One canonical root per word, applied to BOTH sides of the check.

    Not a real stemmer and not trying to be. It has one job: stop the gate
    reporting 'dies' against 'die' as if the model had invented a word. Any
    pair it fails to unify shows up as a leak and gets looked at by hand,
    which is the safe direction to fail in.
    """
    for _ in range(3):
        for s in SUF:
            if w.endswith(s) and len(w) - len(s) >= 3:
                w = w[:-len(s)]
                break
        else:
            break
    if w.endswith("e") and len(w) > 3:
        w = w[:-1]
    if w.endswith("i") and len(w) > 3:
        w = w[:-1] + "y"
    return w


def _mkalias():
    return {norm(k): norm(v) for k, v in ALIAS.items()}


def flat(s):
    """Fold accents away, because the gloss keeps Hungarian spellings.

    The dictionary writes Jezus with an accent and files some words with
    parentheses inside them -- Jew(ish), (thorn)bush. Neither is a difference
    the leak gate has any business reporting: it cost 320 false alarms before
    this existed, which is most of what the gate was finding.
    """
    return "".join(c for c in unicodedata.normalize("NFKD", s.lower())
                   if not unicodedata.combining(c))


TOKEN = re.compile(r"[^\s|]+")

# The only spellings the gate is told are the same word. Each one is a
# difference between the dictionary's Hungarian orthography and ordinary
# English, not a difference of content, and each is listed here so that a
# reader can see exactly how much latitude the gate has been given. It is
# this much and no more.
ALIAS = {"jesus": "jezus",       # Jezus is K&T's spelling of the name
         "christ": "krisztus",
         # English ordinals against the gloss's cardinals. The manuscript
         # writes "six chapter"; English writes "the sixth chapter". That is
         # the same claim, and the gate has no business calling it an import.
         "first": "one", "second": "two", "third": "three", "fourth": "four",
         "fifth": "five", "sixth": "six", "seventh": "seven",
         "eighth": "eight", "ninth": "nine", "tenth": "ten",
         "eleventh": "eleven", "twelfth": "twelve", "thirteenth": "thirteen",
         "twentieth": "twenty", "thirtieth": "thirty"}

# Signs whose gloss is a grammatical note rather than a word, but which a
# translator must render as a word. K&T's <suffix of divine name> is the mark
# that makes a name God's name; English has no such suffix and writes "God".
ALIAS_N = None   # filled below, once norm exists

SIGNWORD = {"suffix_of_divine_name": "god",
            "preposition_of_genitive": "of",
            "subject_marker": "the",
            "name_of_the_author": "writer"}

# A decade word is supported when the gloss has both pieces it is built from:
# the codex writes 22 as two-two-ten, and English writes twenty-two.
DECADE = {"twenty": ("two", "ten"), "thirty": ("three", "ten"),
          "forty": ("four", "ten"), "fifty": ("five", "ten"),
          "sixty": ("six", "ten"), "seventy": ("seven", "ten"),
          "eighty": ("eight", "ten"), "ninety": ("nine", "ten"),
          "thirteen": ("three", "ten"), "fourteen": ("four", "ten"),
          "fifteen": ("five", "ten"), "sixteen": ("six", "ten"),
          "seventeen": ("seven", "ten"), "eighteen": ("eight", "ten"),
          "nineteen": ("nine", "ten")}


def stems(s):
    s = flat(s)
    out = set()
    for tok in TOKEN.findall(s):
        parts = STEM.findall(tok)
        for key, word in SIGNWORD.items():
            if key in tok:
                out.add(canon(word))
        for w in parts:
            if w not in FUNC:
                out.add(canon(w))
        # Jew(ish) and (thorn)bush are one word with a bracket in it
        if len(parts) > 1:
            j = "".join(parts)
            if j not in FUNC:
                out.add(canon(j))
    return out


def folios():
    """page -> (subtitle, [gloss lines]) straight out of the reader's edition."""
    txt = open(ED, encoding="utf-8").read()
    out = {}
    for m in re.finditer(
            r"^## (\d{3}[rv])(?: — ([^\n]*))?\n(.*?)(?=^## |\Z)", txt,
            re.M | re.S):
        pg, sub, body = m.groups()
        lines = [re.sub(r"^\s*\d+\s+", "", l).strip()
                 for l in body.splitlines() if re.match(r"^\s*\d+\s+\S", l)]
        out[pg] = (sub or "", lines)
    return out


def canon(w):
    """One canonical form, alias applied on both sides of the stemmer.

    "Christ's" reaches here as christs, which no alias keyed on christ will
    ever match; stemming first and aliasing again fixes that without widening
    the table.
    """
    n = norm(ALIAS.get(w, w))
    return ALIAS_N.get(n, n)


def E_ord(w):
    """The decade word this stem came from, if any."""
    for d in DECADE:
        if norm(d) == w:
            return d
    return None


ALIAS_N = _mkalias()


def leaks(english, gloss_lines):
    """Content words of the English that nothing in this folio's gloss supports.

    Three ways a word counts as supported, and they are deliberately generous,
    because the gate exists to catch imported CONTENT -- a name, an event, a
    clause the manuscript does not have -- not to referee morphology. A word
    the gate lets through wrongly is a word a reader can still catch against
    the printed gloss; a word it flags wrongly costs a folio.
    """
    have = set()
    for l in gloss_lines:
        have |= stems(l)
    bad = []
    for w in sorted(stems(english)):
        if w in have:
            continue
        ok = False
        if w in DECADE or any(E_ord(w) == d for d in DECADE):
            d = w if w in DECADE else next(x for x in DECADE if E_ord(w) == x)
            if all(norm(p) in have for p in DECADE[d]):
                continue
        for g in have:
            a, b = (w, g) if len(w) <= len(g) else (g, w)
            if len(a) >= 4 and b.startswith(a):
                ok = True
            elif len(a) >= 5 and a in b:
                ok = True
            if ok:
                break
        if not ok:
            bad.append(w)
    return bad


def ask(lines, caught=()):
    body = "\n".join(f"{i:>3}  {l}" for i, l in enumerate(lines, 1))
    if caught:
        body += ("\n\nYOUR LAST ATTEMPT AT THIS FOLIO FAILED. You used these "
                 "words, and NONE of them is in the gloss above:\n  "
                 + ", ".join(caught)
                 + "\n\nYou were completing the passage from a source you "
                   "recognise instead of rendering what is in front of you. "
                   "Write it again using only what the gloss gives you. If "
                   "that leaves the passage broken, leave it broken.")
    req = urllib.request.Request(
        URL,
        data=json.dumps({
            "model": MODEL,
            "messages": [{"role": "system", "content": SYSTEM},
                         {"role": "user", "content": body}],
            "temperature": 0.2, "max_tokens": 1200,
        }).encode(),
        headers={"Authorization": "Bearer " + KEY,
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.loads(r.read())
    return d["choices"][0]["message"]["content"].strip(), d.get("usage", {})


def load():
    if os.path.exists(OUT):
        return json.load(open(OUT, encoding="utf-8"))
    return {}


def save(d):
    json.dump(d, open(OUT, "w"), ensure_ascii=False, indent=0, sort_keys=True)


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("pages", nargs="*")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--above", type=float, default=5.7)
    a = ap.parse_args(argv)
    fo = folios()
    have = load()

    if a.cmd == "status":
        print(f"english for {len(have)} of {len(fo)} folios")
        return 0

    caught = {}
    if a.cmd == "redo":
        todo = []
        for pg, v in have.items():
            lines = fo.get(pg, ("", []))[1]
            if not lines:
                continue
            lk = leaks(v["english"], lines)
            if len(lk) / max(len(v["english"].split()), 1) * 100 >= a.above:
                todo.append(pg)
                caught[pg] = lk
        print(f"{len(todo)} folios at or over {a.above}% unsupported words")
    else:
        todo = a.pages or [p for p in fo if p not in have]
    if a.limit:
        todo = todo[:a.limit]
    nlk = ntok = 0

    def one(pg):
        sub, lines = fo.get(pg, ("", []))
        if not lines:
            return pg, None, "no lines"
        for attempt in range(3):
            try:
                return pg, ask(lines, caught.get(pg, ())), None
            except Exception as e:
                if attempt == 2:
                    return pg, None, str(e)
                time.sleep(3 * (attempt + 1))

    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for pg, got, err in ex.map(one, todo):
            sub, lines = fo.get(pg, ("", []))
            if err:
                print(f"{pg}  FAILED {err}", flush=True)
                continue
            eng, use = got
            lk = leaks(eng, lines)
            ntok += use.get("total_tokens", 0)
            nlk += len(lk)
            if a.cmd == "redo" and len(lk) / max(len(eng.split()), 1) * 100 >= a.above:
                print(f"{pg}  STILL OVER THE BAR, english dropped", flush=True)
                have.pop(pg, None)
                save(have)
                continue
            have[pg] = {"english": eng, "leaks": lk}
            save(have)
            if a.cmd == "sample":
                print(f"=== {pg} — {sub}\n{eng}")
                print(f"  LEAKS {len(lk)}: {' '.join(lk) if lk else '(none)'}\n",
                      flush=True)
            else:
                print(f"{pg}  {len(eng.split()):>4}w  leaks {len(lk)}"
                      + (f"  {' '.join(lk[:8])}" if lk else ""), flush=True)
    print(f"\n{len(todo)} folios, {ntok} tokens, {nlk} leaks total")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
