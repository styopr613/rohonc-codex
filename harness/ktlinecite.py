"""Find the lines where Király and Tokai's dictionary names a word for a sign.

A PROPOSER, NOT A RULE (2026-09-28, the same day). Run over the whole book as
a rule, this printed the wrong sense in enough places that every candidate was
then decided by hand instead; the decisions are glossfix.json, applied by
ktglossfix.py, and that is what the reader's edition and the site print.
Nothing imports word_for() now. It is kept so the next dictionary change can
be proofed the same way: run it, compare with glossfix.json, decide by hand.
The rules below describe how it proposes, and the account of what went wrong
with each is kept.

WHY. On 2026-09-28 the gloss was proofed against the dictionary before a
reader pass, because the gloss is the evidence a reader pass checks Book One
against. Their entries cite folio and line: "{ab1} (2) Thursday 190r08",
"{b52} ... house 043v06". 2,496 times a spelling they cite stands whole on the
line they cite. 519 times the reader's edition printed something else. The
causes were four, all mechanical:

  1. Two entries share one spelling (520b7a "believe" and "clothes"; ab1
     "wound" and "Thursday"). The renderer merges them and prints the first,
     so the prodigal son's robe read "believe" and Maundy Thursday "wound".
  2. One variant spelling is claimed by two entries (b52: "until" and
     "house"). The variant map keeps one.
  3. This project's own readings outranked theirs on a spelling they had
     already read: "answered*" / "hast thou done*" for their "naked",
     "cherub*" for "Eve", "rejoiced" for "sheep", "emperor" for "cock".
  4. Spellings their entries list at the head, beside the headword, never
     reached the dictionary, so the renderer cut them into pieces:
     "exist-chapter" for "temple", "one-heavenly-year" for "friend".

THE RULES, DECLARED BEFORE THE FIRST RUN.

  A. LINE RULE. A citation counts when (i) the spelling is one sign, no space
     (runs of signs are ktexpr.json's job); (ii) it has folio AND line;
     (iii) it is not after "see", "but see", "cp." or "cf." (a pointer, not a
     reading); (iv) the spelling stands whole on that line, raw or with its
     affixes stripped. There, their word is printed, whatever this project
     would have printed: its own reading at any tier, a cut, a variant, the
     sense-fit pick, or another sense of the same entry.
  B. WHICH WORD. The citation's own English, where plain English stands
     between the spelling and the reference ("{461ab1} Holy Thursday, ...
     028v04"); otherwise the lemma group the reference falls under -- the
     last group before it, or the first group when the reference comes
     before any lemma -- and the first lemma of that group.
  C. NO OVERRIDE when the word is a grammatical label ("<marker of
     subject>"), or when two entries cite the same spelling at the same line
     with different words (their homograph is unresolved there, so the line
     prints as before and is listed by --conflicts).
  D. SPELLING RULE -- WITHDRAWN after its first run, 2026-09-28. As
     declared: a spelling their entries list under exactly ONE word, not
     itself a headword, is that word wherever it stands. Run, it changed
     2,219 tokens and was wrong in bulk: a spelling an entry lists is often a
     compound built on the headword, so "Lord-Jézus" became "Lord" 534 times,
     "virgin-Mary" "virgin" 62 times, "this-Lord" "this" 133 times. Only the
     line rule is kept; a spelling is read as their word where they cite it,
     not beyond.
  E. Their set phrases (ktexpr.json) still come first: they are also theirs,
     and longer.
  F. NO OVERRIDE where the gloss as it stands already carries their word as
     one of its parts ("Lord-Jézus" for "Lord", "~exist" for "exist",
     "believe*" for "believe"). The line says what they say already, and the
     longer rendering keeps what the sign is built from. Added with D's
     withdrawal, before the second run. Widened before the third: no
     override where the gloss already prints ANY sense of the citing entry
     (their "tie (up) / bind" cited under "bind" leaves "tie up" alone).
     This rule changes nothing that is wrong; it stops churn.
     WIDENING WITHDRAWN 2026-09-28, on the owner's word-by-word read: where
     they name a sense for a line ("faithful" 002r04, "immediately" and
     "bright" 006r01-10), the general sense of the same entry is not "their
     word already", it is the wrong sense. F compares the cited word only.

  AMENDMENTS ON THE WORD-BY-WORD READ, 2026-09-28, each from a case:
  I. A spelling given as an example ("<e. g.> {644} 017v12") illustrates
     the lemma BEFORE it (017v12 "get conceived", not the next "create";
     058v01 "church father", not the next "scribe").
  J. A "?" or "??" written before a lemma marks that sense uncertain for
     every reference under it (222v05 "?? week"), so rule H applies.
  K. An expression's English may stand past a marker in the next piece of
     the entry ("{a10670371b47} 183v02 <?> against each other").
  L. Which lemma a spelling written after a lemma belongs to: if a new sense
     letter ("c)", "II.") or a "[var." bracket stands between, the lemma that
     follows ("c) [<var.> {990990990} 034r07] be afraid"); otherwise the
     lemma before ("than ... <similarly> {991ae0} 032v02"). Rule B' had
     sent every such spelling forward.

  AMENDMENTS BEFORE THE THIRD RUN, after reading every change the second
  made (595 tokens, 316 kinds):
  B'. In their entries a spelling written after the last lemma belongs to
     the lemma that FOLLOWS it: "c) [<var.> {990990990} 034r07] be afraid".
     The second run gave it the lemma before ("shall"). A reference written
     straight after a lemma still belongs to that lemma.
  G. A spelling they mark negated ("<neg.> {5b1ae0} 109r08" under "exist")
     is skipped: printing the headword drops the "not".
  H. A citation they mark "?" or "??" replaces only a reading of this
     project's (tiers A-D, a bracket, a dark word), never a reading of
     theirs.
  "öl" is Hungarian in their English column (for "bosom") and is skipped.

  AMENDMENTS BEFORE THE FOURTH RUN, after reading the third's 319 changes:
  B''. English standing straight after a spelling is that spelling's word
     even with a marker between it and the reference ("{6a6270} Creator Lord
     <e. g.> 029r02"). An expression's English may stand AFTER its
     references ("<expr.> {7e1acd} 076r01, ... 127v08 apostolic letter");
     an expression with no English of its own is skipped, never given the
     entry's next lemma. The third run printed "disciple" for their
     "apostolic letter". A spelling listed after a comma in the same run
     shares the English of the one before it.
  F''. Rule F compares words cut to five letters, so "the Baptist" already
     says their "baptize" (their "{8714a84b1520060131} ... Saint John the
     Baptist") and "righteously" their "righteous".

Only the writers of published files use this (ktreader.py, ktsite.py), as
with ktexpr.json. Every test and gate renders sign by sign, so no figure
computed from signs moves.

    python3 ktlinecite.py                 summary
    python3 ktlinecite.py --list          every line override
    python3 ktlinecite.py --spelling      every spelling-rule word
    python3 ktlinecite.py --conflicts     lines left alone under rule C
"""
import json
import re
import sys
from collections import defaultdict

import ktdict

POINTER = ("see", "but see", "cp.", "cf.")
REF = re.compile(r"(\d{3}[rv])(\d{2})(?:[–-](\d{2}))?|(?<=, )(\d{2})(?![0-9rv])")


def hx(s):
    return "".join("%03x" % (ord(c) - 0xE000) for c in s if ord(c) >= 0xE000)


# Rule B takes the English that stands between a spelling and its reference.
# Five such strings are pieces of an example sentence, not the sign's meaning,
# and are skipped by name, decided by hand (2026-09-28).
NOT_A_SENSE = {"+ suffix", "~ with you", "how? … so", "fire up and sadden",
               "at  9 o'clock", "öl",
               # added before the fourth run, same test: an example's words
               "as …  so  also", "to the disciples", "act of", "~ among you"}


def _frags(e):
    """The entry as a list of (kind, text): code, meta, lemma, text."""
    out = []
    for f in e["entry"]:
        s, t = f.get("style"), f.get("text", "")
        if s == "rohonc":
            out.append(("code", t.strip()))
        elif s == "meta":
            out.append(("meta", t.strip().lower()))
        elif s == "lemma":
            if t.strip():
                out.append(("lemma", t.strip()))
        elif s == "section":
            out.append(("sect", t.strip()))
        elif s is None:
            out.append(("text", t))
    return out


def _groups(fr):
    """Index of each lemma -> the first lemma of its group. A group is lemmas
    with nothing but commas, slashes, spaces or <or> between them."""
    first, cur, gap = {}, None, True
    for i, (k, t) in enumerate(fr):
        if k == "lemma":
            if gap or cur is None:
                cur = t
            first[i] = cur
            gap = False
        elif k == "meta" and t == "or":
            continue
        elif k == "text" and re.fullmatch(r"[\s,/]*", t):
            continue
        else:
            gap = True
    return first


def build():
    """line: {(folio, line, spelling): (word, [every lemma of the entry], uncertain)}
    spelling: always empty now (rule D withdrawn), kept for the --spelling view;
    conflicts: {(folio, line, spelling): {words}}"""
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    cite = defaultdict(dict)         # (f, l, code) -> {word: (lemmas, uncertain)}
    for n, e in enumerate(raw):
        fr = _frags(e)
        grp = _groups(fr)
        lem_at = sorted(grp)
        lemmas = tuple(t for k, t in fr if k == "lemma")
        cur, multi, mark = hx(e["code"]), False, None
        code_at, recent, code_eng, list_eng, lem_unc = -1, [], None, None, set()
        example = False
        for i, (k, t) in enumerate(fr):
            if k == "code":
                if t:
                    cur, multi, code_at, code_eng = hx(t), len(t.split()) > 1, i, None
                    # rule I: the marker straight before the spelling says
                    # whether it is an example
                    pm = [x for x in fr[max(0, i - 3):i] if x[0] != "text" or x[1].strip()]
                    example = bool(pm) and pm[-1][0] == "meta" and pm[-1][1].startswith("e. g.")
                    # English standing straight after the spelling, before any
                    # reference, is the spelling's own ("{6a6270} Creator Lord
                    # <e. g.> 029r02"), even with a marker in between
                    nxt = fr[i + 1] if i + 1 < len(fr) else None
                    if nxt and nxt[0] == "text":
                        head = REF.split(nxt[1])[0] if REF.search(nxt[1]) else nxt[1]
                        head = re.sub(r"[†\[\]();]|\b\d+×", " ", head).split(",")[0].strip(" –-")
                        if re.search(r"[A-Za-z]{3}", head):
                            code_eng = head
                    # a spelling listed after a comma in the same run shares the
                    # English of the one before it ("{6a6270} Creator Lord ...
                    # 029r02, {6a6520270} 087r05, {2706a6} 137v04")
                    if (code_eng is None and list_eng and i > 0 and fr[i - 1][0] == "text"
                            and fr[i - 1][1].rstrip().endswith(",")):
                        code_eng = list_eng
                    list_eng = code_eng
                continue
            if k == "meta":
                mark = t
                recent.append(t)
                continue
            if k == "lemma":
                if any(m in ("?", "??") for m in recent):
                    lem_unc.add(i)
                recent, list_eng = [], None
                continue
            if mark in POINTER or multi:
                continue
            # rule G: a negated form ("<neg.> {5b1ae0} 109r08" under "exist")
            # is not the headword; printing the headword drops the "not".
            if any(m.startswith("neg") for m in recent):
                continue
            uncertain = any(m in ("?", "??") for m in recent)
            expr = any(m.startswith("expr") for m in recent[-3:]) and code_at > max(
                [j for j, (kk, _) in enumerate(fr[:i]) if kk == "lemma"] or [-1])
            # an expression's English may stand after its references
            # ("<expr.> {7e1acd} 076r01, ... 127v08 apostolic letter")
            tail = None
            if expr and not code_eng:
                refs = list(REF.finditer(t))
                if refs:
                    tl = t[refs[-1].end():].split(";")[0]
                    tl = re.sub(r"[†\[\]();]|\b\d+×", " ", tl).split(",")[0].strip(" –-")
                    if re.search(r"[A-Za-z]{3}", tl):
                        tail = tl
                    elif not t[refs[-1].end():].strip(" ,"):
                        # "... 183v02 <?> against each other": past markers
                        for kk, tt in fr[i + 1:]:
                            if kk == "meta":
                                if tt in ("?", "??"):
                                    uncertain = True
                                continue
                            if kk == "text":
                                tl = re.sub(r"[†\[\]();]|\b\d+×", " ", tt.split(";")[0]).split(",")[0].strip(" –-")
                                if re.search(r"[A-Za-z]{3}", tl) and not REF.search(tt.split(";")[0]):
                                    tail = tl
                            break
            last, pos, prev = None, 0, None
            for m in REF.finditer(t):
                pre = t[pos:m.start()]
                first = pos == 0
                pos = m.end()
                if m.group(1):
                    last = m.group(1)
                    ls = [int(m.group(2))]
                    if m.group(3):
                        ls = list(range(int(m.group(2)), int(m.group(3)) + 1))
                elif last:
                    ls = [int(m.group(4))]
                else:
                    continue
                # rule B: plain English right before the reference, in the
                # same fragment, after the spelling. A later reference in the
                # same list carries the word of the one before it; a later
                # reference with new English in front of it is another
                # sense, not attributable here, and is skipped.
                eng = re.sub(r"[†\[\]();]|\b\d+×", " ", pre)
                eng = eng.split(",")[0].strip(" –-")
                has = re.search(r"[A-Za-z]{3}", eng)
                if not first and prev is not None:
                    if has:
                        prev = None
                        continue
                    word = prev
                elif has and first and fr[i - 1][0] == "code":
                    word = eng.strip()
                elif has:
                    continue
                elif code_eng:
                    word = code_eng
                elif tail:
                    word = tail
                elif expr and not any(j > i for j in lem_at if j > code_at
                                      and not [x for x in fr[code_at + 1:j] if x[0] == "code"]):
                    # an expression with neither English nor a lemma of its
                    # own straight after it
                    continue
                else:
                    # rule B, amended before the third run: a spelling written
                    # after the last lemma belongs to the lemma that FOLLOWS it
                    # ("c) [<var.> {990990990} 034r07] be afraid"); a reference
                    # written straight after a lemma belongs to that lemma.
                    before = [j for j in lem_at if j < i]
                    after = [j for j in lem_at if j > i]
                    # rule L: between the last lemma and the spelling, a new
                    # sense letter ("c)", "II.") or a "[var." bracket means
                    # the spelling belongs to the lemma that FOLLOWS; with
                    # neither, it is an example of the lemma before it.
                    between = fr[before[-1] + 1:code_at] if before else []
                    newsense = any(kk == "sect" for kk, _ in between) or any(
                        kk == "text" and "[" in tt for kk, tt in between)
                    if before and (example or code_at < before[-1] or not newsense):
                        # an example ("<e. g.> {644} 017v12") illustrates the
                        # lemma before it
                        j = before[-1]
                    elif after:
                        j = after[0]
                    elif before:
                        j = before[-1]
                    else:
                        continue
                    word = grp[j]
                    if j in lem_unc:
                        uncertain = True
                prev = word
                if not word or word.startswith("<") or word in NOT_A_SENSE:
                    continue
                for l in ls:
                    cite[(last, l, cur)][word] = (lemmas, uncertain)
    line, conflicts = {}, {}
    for key, ws in cite.items():
        if len(ws) == 1:
            w, (lem, unc) = next(iter(ws.items()))
            line[key] = (w, lem, unc)
        else:
            conflicts[key] = set(ws)
    return line, {}, conflicts


_CACHE = {}


def tables():
    if not _CACHE:
        _CACHE["t"] = build()
    return _CACHE["t"]


def _parts(printed):
    """The words of a printed gloss, each cut to five letters, so a
    different ending of the same word ('Baptist', 'baptize') is the same."""
    return {x.lower()[:5] for x in re.split(r"[-_\s/]+", re.sub(r"[*^~+?°.\[\]]", "", printed)) if x}


OURS_KIND = ("prop", "guess", "none", "cut", "cut1")   # cuts are ours too


def word_for(page, lineno, raw_hex, base_hex, printed=None, own=None, kind=None):
    """Their word for this token at this line, or None (rules A, C, F, G, H).

    `printed` is what the edition would print without this rule, `kind` how
    it got there (kttranslate.kind), `own` renders a sense into this edition's
    words for the comparison."""
    line, _, _ = tables()
    for h in (raw_hex, base_hex):
        hit = line.get((page, lineno, h))
        if not hit:
            continue
        w, lemmas, unc = hit
        # rule H: their "?" or "??" replaces a reading of ours, never one of theirs
        if unc and kind not in OURS_KIND:
            return None
        if printed is not None:
            have = _parts(printed)
            for L in (w,):
                try:
                    mine = own(L) if own else L
                except SystemExit:
                    mine = L
                if _parts(mine) and _parts(mine) <= have:
                    return None
        return w
    return None


def main(argv):
    line, spelling, conflicts = tables()
    if "--list" in argv:
        for (f, l, c), (w, _, unc) in sorted(line.items()):
            print(f"{f}{l:02d}  {c:16} {w}{'  (?)' if unc else ''}")
    elif "--spelling" in argv:
        for c, w in sorted(spelling.items(), key=lambda x: x[1]):
            print(f"{c:24} {w}")
    elif "--conflicts" in argv:
        for (f, l, c), ws in sorted(conflicts.items()):
            print(f"{f}{l:02d}  {c:16} {' | '.join(sorted(ws))}")
    else:
        print(f"line citations {len(line)}, spelling words {len(spelling)}, "
              f"conflicts left alone {len(conflicts)}")


if __name__ == "__main__":
    main(sys.argv[1:])
