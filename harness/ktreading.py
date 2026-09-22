"""The reading edition: what the manuscript means, in English.

    python3 ktreading.py sample 052v 148v     a few folios, printed
    python3 ktreading.py run                  the whole book
    python3 ktreading.py account              the word accounting, per folio

WHAT THIS IS, AND WHAT IT IS NOT. Every other layer of this edition is made
from the manuscript alone. This one is not, and that is the point of it: it is
shown the passages the folio is working from, and it uses them to resolve what
the codex's own broken, elliptical lines are reaching for. That is what a
reading edition of a damaged text does, and it is how the manuscript was meant
to be read: its compiler and his readers knew these stories.

So the honest description, which the book prints on its own first page: this is
an interpretation. Book Two is the evidence and does not move.

THE INPUTS, per folio:
  1. the line-by-line English made by hand against the sources, with the gloss
     under each line (rohonc_translation.md)
  2. the folio's cited chapter and verse, from the Douay the compiler had
  3. the passages retrieved from the medieval corpus -- the Life of Adam and
     Eve, the Golden Legend, the apocryphal gospels, Barlaam, the missal, the
     Holy Week office, the four cycles of mystery plays, Josephus (ktsource.py)
  4. the project's own note on the folio, where it has one

THE ACCOUNTING, declared here before the first run. Every content word of the
reading is put in one of three classes and the counts are published per folio:

    FROM THE MANUSCRIPT   the word is in that folio's own gloss
    FROM THE SOURCE       not in the gloss, but in a passage shown with it
    FROM NEITHER          in neither

The bar is on the third class only, and it is ZERO outside a list of ordinary
English function and connective words: a word from neither the manuscript nor
the source it was given is invention, and the paragraph is written again with
those words quoted back at it. The second class is NOT barred -- it is the
whole method -- but it is counted and printed, folio by folio, so a reader can
see exactly how much of any page came from the source rather than the codex.
"""
import argparse
import json
import os
import re
import sys
import time
import concurrent.futures as cf

import corpus
import ktbook
import ktenglish as KE
import ktor
import ktsource as S

OUT = os.path.join(corpus.ROOT, "work", "rohonc", "translation", "reading.md")
ACC = os.path.join(corpus.ROOT, "work", "rohonc", "reading_account.json")
MODEL = "deepseek/deepseek-v4-pro-0813"
EXTRA = {"reasoning": {"enabled": False}}
PER_CALL = 4
BAR = 0          # words from neither the manuscript nor its sources

SYSTEM = """You are making a reading edition of the Rohonc Codex, a sixteenth-century
manuscript, in English, for people who want to know what it says.

For each folio you are given, in this order:
  THE MANUSCRIPT   its text, line by line: an English rendering of each line with the
                   word-for-word gloss beneath it. This is what the page actually says.
                   It is elliptical: this script writes phrases as single signs, drops
                   verbs and articles, and repeats formulas. Gaps are marked.
  THE SOURCE       the passages the folio is working from -- the verses it cites, and
                   the medieval texts this manuscript compiles: the Life of Adam and
                   Eve, the Golden Legend, the apocryphal gospels, Barlaam, the missal,
                   the mystery plays. The compiler knew these stories and wrote for
                   readers who knew them too.

Write what the folio says, in clear English prose, using the source to resolve what
the manuscript's broken lines are reaching for. It must READ: a person who knows none
of this should be able to follow it straight through. A page of half-sentences broken
by dots has failed, and so has a page that tells a story the manuscript does not.

THE RULES:
- The manuscript leads. The source only ever tells you what a phrase in the manuscript
  MEANS. It never adds an episode, a person, a speech or a detail the manuscript does
  not have. If the source has a scene and the manuscript does not, it is not in your
  English.
- Where a line is broken, CLOSE THE GAP if the source and the surrounding lines make
  the sense plain, and keep the sentence running. That is what the source is for: the
  compiler's readers knew these stories and filled the same gaps as they read. Write
  ... only where neither the manuscript nor the source gives you anything at all.
- Do not pad a bare line into a scene. Completing a sentence is not the same as adding
  an episode.
- Where the manuscript departs from the source -- a different name, a different number,
  an episode the source does not have -- FOLLOW THE MANUSCRIPT. Those departures are
  the most interesting thing in the book and must survive.
- Keep restored words in [brackets].
- THE NUMERALS ADD, and a "ten" written after a group multiplies that group by ten.
  six-six is twelve. ten-ten-ten-ten is forty. two-two-ten is forty. six-two is eight.
  ten-ten-two-nine is thirty-one. Work the number out and write it in words; never
  copy a numeral string ("sixth-two") into the English, and never shorten a count:
  "six-hundred and six-thousand and six-ten and six" is six hundred, and six thousand,
  and sixty, and six, and all four parts stay.
- Resolve the formulas the same way every time: the angel who hides himself is Lucifer;
  "in turn" introduces the next item; "somebody" is a man; "then-exist" is "there was".
- THE HOUSE VOICE, the same one used for every other edition on this imprint: plain
  words a twelve-year-old reads easily. Prefer the common word over the literary one
  wherever the common word is equally faithful. Do not sanitise: where the manuscript
  is harsh or strange, the English is too.
- The sources you are shown are in seventeenth-century Bible English. DO NOT COPY THEIR
  CADENCE. Nothing archaic: no thee, thou, thy, thine, ye; no -eth or -est endings
  (needeth, doth, hath, saith, goest); no "unto", "whither", "behold", "verily", "lo".
  Say "you", "has", "says", "to", "where", "look". No inverted word order: "wholly
  clean", not "clean wholly"; "he does not need", not "he needeth not".
- Stay in the manuscript's time and place. No modern slang, nothing that postdates the
  sixteenth century.
- Punctuate for sense. A question mark only where the line is actually a question.
  "Master, do not wash my feet" is a refusal, not a question.
- No commentary, no notes, no quotation of the gloss, no editorial voice. Just the text.
- Paragraph naturally. End each paragraph with the folios it renders in brackets, like
  (052v) or (029r-030v).

NEVER DESCRIBE THE MATERIAL. You are not writing about this manuscript, you are writing
it out. Do not summarise what a folio contains, do not say what a source says, do not
compare them, and never use the words "manuscript", "folio", "source", "passage",
"text", "account" or "describes". Begin with the first thing that happens on the page
and carry straight on.

TWO WORKED EXAMPLES, which are the standard. The first is an easy page.

    gloss: Lord-Jézus give_up_the_ghost +cross / earth quake rock stone [?] sun and
    moon this eclipse / one soldier on-Jerusalem blind / exist Longinus and pierce spear

    And then the Lord Jesus gave up his spirit on the cross. The earth shook, the
    rocks and the stones split, the sun and the moon went dark, and all creation
    mourned when Christ the Lord was crucified. And a soldier came from Jerusalem,
    a blind man, and that soldier was Longinus, and he ran his spear into the side
    of the Lord Jesus Christ. (052v)

The second is a hard page: formulaic, half of it broken, and the source is what
tells you what it is saying. Note that it is written as sentences even so, that the
source (the angels commanded to bow to Adam, and one refusing) resolves line 7, and
that nothing is invented to fill the holes.

    gloss: Lord-<divine> mother be_born and hide_oneself-angel to-Lord to-Lord /
    hide_oneself-angel this on throne [?] Lord-<divine> <of>-Lord [?] / exist earth
    [?] from-father God [?] Michael / angel believe servant stand_up up and then-exist
    stand_up / heavenly say from-father-<divine> [?] go to-hide_oneself-angel and /
    hide_oneself-angel bow_down on throne <of>-Lord and then-exist inside [?] /
    bow_down and from angel each,_every to-which hide_oneself-angel bow_down /
    and then-exist [?] from-father God [?] and shout

    The mother of the Lord God was born; and Lucifer spoke to the Lord, to the Lord;
    Lucifer set himself upon the throne, equal to the Lord God. There was the earth;
    and then God the Father eternal, and Michael. The angels, faithful servants, rose
    up; and when they had risen the heavenly ones spoke. God the Father eternal went
    to Lucifer, and Lucifer bowed down before the throne of the Lord; and within, they
    bowed down, every one of the angels, to him whom Lucifer would not bow to. And
    then God the Father eternal saw it, and cried out. (002r)

Return only the prose."""


def blocks():
    """Each folio: its hand-made English and gloss, line by line."""
    out = {}
    txt = open(S.TRANS, encoding="utf-8").read()
    for m in re.finditer(r"^## (\d{3}[rv])([^\n]*)\n(.*?)(?=^## |\Z)", txt, re.M | re.S):
        pg, title, body = m.groups()
        lines = []
        cur = None
        for l in body.splitlines():
            if l.startswith("**"):
                cur = re.sub(r"^\*\*(\d+)\*\*\s+", r"\1  ", l).strip()
            elif l.strip().startswith("`") and cur:
                lines.append(cur + "\n       gloss: " + l.strip().strip("`"))
                cur = None
        if cur:
            lines.append(cur)
        out[pg] = {"title": title.strip(" —"), "lines": lines}
    return out


def folio_prompt(pg, bl, src):
    d = src.get(pg, {})
    p = [f"FOLIO {pg}" + (f" — {bl[pg]['title']}" if bl[pg]["title"] else ""), "",
         "THE MANUSCRIPT"]
    p += bl[pg]["lines"]
    p.append("")
    p.append("THE SOURCE")
    if d.get("note"):
        p.append("  note on this folio: " + d["note"])
    for c in d.get("cited", [])[:14]:
        p.append(f"  {c['ref']}  {c['text']}")
    for r in d.get("retrieved", [])[:3]:
        p.append(f"  from the {r['source']}: {r['text']}")
    if not d.get("cited") and not d.get("retrieved"):
        p.append("  (nothing found; go on the manuscript alone)")
    return "\n".join(p)


FUNC = KE.FUNC | set("""said says go goes went come comes came take takes took give gives
gave make makes made see sees saw know knows knew tell tells told ask asks asked
answer answers answered speak speaks spoke stand stands stood sit sits sat put puts
turn turns turned begin begins began call calls called bring brings brought leave
leaves left hear hears heard find finds found let lets man men thing things word
words place places time times day days great good own upon into unto again still
now then there here where when while because since after before against toward""".split())


CITE_RE = re.compile(r"\(\d{3}[rv](?:\s*[-\u2013,]\s*\d{3}[rv])*\)")


# The stemmer chops suffixes and cannot touch an irregular verb, so "came"
# stemmed to "cam" and was reported as a word the manuscript does not have
# while its own gloss said "come". A few dozen pairs were doing most of the
# reported imports. This unifies them on BOTH sides, which is the only safe
# way to mend a stemmer: it can no longer flag a form of a word that is there,
# and it still flags a word that is not.
IRREG = {"came": "come", "gave": "give", "spoke": "speak", "spoken": "speak",
         "rose": "rise", "risen": "rise", "arose": "rise", "told": "tell",
         "went": "go", "gone": "go", "goes": "go", "going": "go",
         "saw": "see", "seen": "see", "made": "make", "taken": "take",
         "took": "take", "written": "write", "wrote": "write", "ate": "eat",
         "eaten": "eat", "struck": "strike", "knew": "know", "known": "know",
         "understood": "understand", "began": "begin", "begun": "begin",
         "brought": "bring", "bore": "bear", "born": "bear", "fell": "fall",
         "fallen": "fall", "heard": "hear", "held": "hold", "kept": "keep",
         "left": "leave", "laid": "lay", "led": "lead", "lost": "lose",
         "paid": "pay", "ran": "run", "sat": "sit", "sent": "send",
         "shut": "shut", "sought": "seek", "sold": "sell", "stood": "stand",
         "thought": "think", "threw": "throw", "thrown": "throw",
         "wept": "weep", "won": "win", "found": "find", "fled": "flee",
         "forgiven": "forgive", "forgave": "forgive", "bound": "bind",
         "children": "child", "feet": "foot", "men": "man", "teeth": "tooth"}
IRREG_N = {KE.norm(k): KE.norm(v) for k, v in IRREG.items()}


def canon(w):
    return IRREG_N.get(w, w)


def account(text, gloss_words, source_words):
    """Three classes of content word. See the docstring.

    The folio citation is stripped first: "(069v)" stems to "v" and "069v" and
    those were being reported as imported vocabulary, which buried the real
    ones. Stems of two letters or fewer go the same way."""
    text = CITE_RE.sub(" ", text)
    gloss_words = {canon(w) for w in gloss_words}
    source_words = {canon(w) for w in source_words}
    ms, src, neither = set(), set(), set()
    for w0 in KE.stems(text):
        if len(w0) <= 2 or w0 in FUNC:
            continue
        w = canon(w0)
        if w in FUNC:
            continue
        if w in gloss_words:
            ms.add(w)
        elif w in source_words:
            src.add(w)
        else:
            neither.add(w0)
    return ms, src, neither


def words_of(pg, bl, src):
    g = set()
    for l in bl[pg]["lines"]:
        g |= KE.stems(l)
    s = set()
    d = src.get(pg, {})
    for c in d.get("cited", []):
        s |= KE.stems(c["text"])
    for r in d.get("retrieved", []):
        s |= KE.stems(r["text"])
    if d.get("note"):
        s |= KE.stems(d["note"])
    return g, s


def do_chunk(pages, bl, src):
    body = "\n\n".join(folio_prompt(pg, bl, src) for pg in pages)
    gw, sw = set(), set()
    for pg in pages:
        a, b = words_of(pg, bl, src)
        gw |= a; sw |= b
    caught = ()
    for attempt in (1, 2):
        ask = body
        if caught:
            ask += ("\n\nYOUR LAST ATTEMPT USED THESE WORDS, AND THEY ARE IN NEITHER THE "
                    "MANUSCRIPT NOR THE SOURCE YOU WERE GIVEN:\n  " + ", ".join(caught) +
                    "\n\nThose are inventions. Write it again without them.")
        # ktor.ask sends ONE user message and has no system slot, so the
        # instructions have to travel with the body or the model just
        # echoes the folio back.
        text, usage = ktor.ask(MODEL, SYSTEM + "\n\n" + ask,
                               temperature=0.3, extra=EXTRA)
        ms, sr, no = account(text, gw, sw)
        # every folio in the chunk must be accounted for: a two-folio sample
        # came back with one folio silently dropped, which loses a page of the
        # book without saying so
        missing = [pg for pg in pages if pg not in text]
        if missing and attempt == 1:
            caught = ()
            ask2 = body + ("\n\nYOUR LAST ATTEMPT LEFT OUT " + ", ".join(missing) +
                           ". Write every folio you were given, each with its own "
                           "paragraph and its own citation.")
            text, usage = ktor.ask(MODEL, SYSTEM + "\n\n" + ask2,
                                   temperature=0.3, extra=EXTRA)
            ms, sr, no = account(text, gw, sw)
            missing = [pg for pg in pages if pg not in text]
        if len(no) <= BAR or attempt == 2:
            return text, {"pages": pages, "manuscript": len(ms), "source": len(sr),
                          "neither": sorted(no), "attempts": attempt,
                          "missing": missing,
                          "cost": float((usage or {}).get("cost") or 0)}
        caught = sorted(no)[:26]


def run(only=None):
    bl = blocks()
    src = json.load(open(S.OUT, encoding="utf-8")) if os.path.isfile(S.OUT) else {}
    fol = [pg for pg, _, _, _ in ktbook.folios()]
    pages = only or fol
    groups = [pages[i:i + PER_CALL] for i in range(0, len(pages), PER_CALL)]
    got, log = {}, []
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(do_chunk, g, bl, src): tuple(g) for g in groups}
        done = 0
        for f in cf.as_completed(futs):
            key = futs[f]
            try:
                text, acc = f.result()
            except Exception as e:
                print("  failed", key[0], str(e)[:90], file=sys.stderr); continue
            got[key] = text
            log.append(acc)
            done += 1
            if done % 10 == 0:
                cost = sum(x["cost"] for x in log)
                print(f"  {done}/{len(groups)}  ${cost:.2f}", file=sys.stderr, flush=True)
    if only:
        for g in groups:
            print(got.get(tuple(g), ""), "\n")
        return
    parts = ktbook.PARTS
    idx = {pg: i for i, pg in enumerate(fol)}
    bounds = sorted((idx.get(pg, 0), name) for pg, name, _ in parts)
    md = ["# The Rohonc Codex", "",
          "A reading edition: what the manuscript says, in English, read against the "
          "books it is compiled from. Book Two prints every folio's own text, line for "
          "line, and is the evidence.", ""]
    for bi, (start, name) in enumerate(bounds):
        end = bounds[bi + 1][0] if bi + 1 < len(bounds) else len(fol)
        md += [f"## {name}", "", f"### folios {fol[start]}–{fol[end - 1]}", ""]
        for g in groups:
            if idx.get(g[0], -1) >= start and idx.get(g[0], -1) < end:
                t = got.get(tuple(g))
                if t:
                    md.append(t.strip() + "\n")
    open(OUT, "w", encoding="utf-8").write("\n".join(md))
    json.dump(log, open(ACC, "w"), indent=1)
    tot_m = sum(x["manuscript"] for x in log)
    tot_s = sum(x["source"] for x in log)
    bad = sum(len(x["neither"]) for x in log)
    cost = sum(x["cost"] for x in log)
    print(f"wrote {OUT}\n  words from the manuscript {tot_m}, from the source {tot_s}, "
          f"from neither {bad}   ${cost:.2f}")


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["sample", "run", "account"])
    ap.add_argument("folios", nargs="*")
    a = ap.parse_args(argv)
    if a.cmd == "account":
        log = json.load(open(ACC))
        for x in sorted(log, key=lambda y: -len(y["neither"]))[:20]:
            print(x["pages"], "ms", x["manuscript"], "src", x["source"],
                  "neither", x["neither"][:8])
        return 0
    run(only=a.folios or None)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
