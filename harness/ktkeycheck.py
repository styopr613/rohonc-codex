"""VALIDATE THE KEY. Does Kiraly and Tokai's dictionary land where it says?

Everything this project reads rests on their glossed codes. Nothing had ever
checked that our PARSE of their dictionary agrees with the manuscript, and
they gave us the instrument themselves: entries cite folio and line for their
examples, so the code an entry defines must stand at that folio, on that line.

BARS, DECLARED BEFORE THE FIRST RUN AND NOT MOVED SINCE:

  1. The landing rate must beat a shuffled control -- the same citations with
     the folio replaced by a random other cited folio -- by 5 sigma over 20
     shuffles. Below that our parse does not agree with the manuscript and
     nothing downstream is safe.
  2. The exact-line rate is reported WITHOUT a bar. A code can legitimately
     stand elsewhere on a cited folio. Diagnostic, not a gate.
  3. The residue -- headword citations that miss their folio -- is the
     deliverable. It is a list to read by hand, not a number to minimise.

TWO FAULTS OF THIS SCRIPT, FOUND AND FIXED, RECORDED BECAUSE THE FIRST
VERSION REPORTED THEM AS THE DICTIONARY'S:

  - An entry carries SEVERAL codes. Only 144 of the first 400 carry one.
    After "expr." or "var." comes a DIFFERENT code and the folios that follow
    belong to it. Attributing them all to the headword reported 45.3% of
    citations missing. Corrected, headwords miss 22.4%.
  - "see", "but see", "cp." and "cf." introduce a pointer to another entry,
    not an example. Those folios are not claims and are excluded.
  - Whole-token matching. The manuscript writes K&T's words with affixes
    attached; see inside() below. This one cost the most: it reported the
    dictionary missing 22.4% of its own headword citations when the true
    figure is 10.8%.

WHAT THE SPLIT BY ORIGIN MEANS, and why only HEAD is the key's own claim:

  HEAD       the dictionary headword. This is the key proper.
  VAR        a variant spelling the entry records for the headword.
  EXPR       an EXPRESSION: a phrase K&T write as one code but the
             manuscript writes as several tokens. A single-token lookup
             cannot find it, so its low rate is expected and is not a
             fault -- confirmed by checking that a token on the cited line
             shares a prefix with the expression code in 199 of 329 cases.
  UNCERTAIN  a code K&T themselves mark "?" or "??".
  OR / OTHER a further code offered in the entry without a marker.

Nothing here modifies the dictionary. data/rohonc/kt/ is read only.

    python3 ktkeycheck.py                the rates, the control, the residue
    python3 ktkeycheck.py --residue      every headword citation that misses
"""
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict

import corpus
import ktaffix as A
import ktcross as K

DICT = os.path.join(corpus.DATA, "rohonc", "kt", "dict_en.json")
NSHUF = 20
BAR = 5.0
POINTER = ("see", "but see", "cp.", "cf.")
ORIGIN = {"expr.": "EXPR", "var.": "VAR", "or": "OR", "?": "UNCERTAIN",
          "??": "UNCERTAIN"}
REF = re.compile(r"(\d{3}[rv])(\d{2})?|(?<![0-9rv])(\d{2})(?![0-9rv])")


def citations():
    """[(code, origin, gloss, folio, line|None)], attributed to the code that
    actually introduced each reference."""
    raw = json.load(open(DICT, encoding="utf-8"))
    merged = {}
    for e in raw:
        merged.setdefault(e["code"], []).extend(e["entry"])
    gloss = defaultdict(set)
    out = []
    for head, frags in merged.items():
        cur, mark, origin = head, None, "HEAD"
        for frag in frags:
            t = frag.get("text", "")
            st = frag.get("style")
            if st == "rohonc":
                if t.strip():
                    cur = t.strip()
                    origin = ORIGIN.get(mark, "OTHER") if mark else "HEAD"
                continue
            if st == "meta":
                mark = t.strip().lower()
                continue
            if st == "lemma":
                if t.strip():
                    gloss[cur].add(t.strip())
                continue
            if st is not None:
                continue
            if mark in POINTER:
                continue
            last = None
            for m in REF.finditer(t):
                if m.group(1):
                    last, ln = m.group(1), (int(m.group(2)) if m.group(2) else None)
                elif last:
                    ln = int(m.group(3))
                else:
                    continue
                out.append((cur, origin, last, ln))
    return [(c, o, "; ".join(sorted(gloss.get(c, ()))), f, l) for c, o, f, l in out]


def index(doc):
    """folio -> {line: [hex]}, folio -> [hex], raw and affix-stripped."""
    byline = defaultdict(lambda: defaultdict(list))
    bypage = defaultdict(list)
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            for t in [x for run in ln for x in run]:
                for h in {K.hx(t), K.hx(A.strip(t)[0])}:
                    byline[p.page][i].append(h)
                    bypage[p.page].append(h)
    return byline, bypage


def inside(code, hexes):
    """Does `code` stand as a whole-glyph CONSTITUENT of any of these tokens?

    Testing whole-token equality was the third fault of this script and it
    cost the most. The manuscript writes K&T's words with prefixes and
    suffixes attached -- 630 'on/at/to', 871 'holy', 521 the case markers --
    and the renderer has always known that. Matching whole tokens reported
    those as the dictionary missing its own citations, 22.4% of headwords.
    Matching constituents reports 10.8%, and the renderer's own view of the
    same tokens agrees: of 1,372 tokens carrying those three prefixes over a
    readable word, it reads 1,337.

    A glyph is three hex characters, so a constituent must start and end on a
    multiple of three. Without that, 060 would match inside 1f4060 and inside
    a06012 and the test would pass on coincidence.
    """
    for x in hexes:
        j = x.find(code)
        while j != -1:
            if j % 3 == 0 and (j + len(code)) % 3 == 0:
                return True
            j = x.find(code, j + 1)
    return False


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    byline, bypage = index(doc)
    pages = set(bypage)
    cites = citations()

    rows = []
    for code, origin, g, folio, line in cites:
        h = K.hx(code)
        if folio not in pages:
            rows.append((h, origin, g, folio, line, "NOFOLIO"))
        elif not inside(h, bypage[folio]):
            rows.append((h, origin, g, folio, line, "MISS"))
        elif line is None:
            rows.append((h, origin, g, folio, line, "FOLIO(noline)"))
        elif inside(h, byline[folio].get(line, [])):
            rows.append((h, origin, g, folio, line, "EXACT"))
        else:
            rows.append((h, origin, g, folio, line, "FOLIO"))

    print("VALIDATING THE KEY: K&T's own citations, against the manuscript")
    print(f"  {len({r[0] for r in rows})} distinct codes, {len(rows)} citations\n")

    scored = [r for r in rows if r[5] != "NOFOLIO"]
    citedpages = sorted({r[3] for r in scored})
    print(f"  {'origin':10s} {'cites':>6s} {'lands':>6s} {'rate':>7s} "
          f"{'exact line':>11s}")
    for o in ("HEAD", "VAR", "EXPR", "UNCERTAIN", "OR", "OTHER"):
        rs = [r for r in scored if r[1] == o]
        if not rs:
            continue
        land = [r for r in rs if r[5] != "MISS"]
        ex = [r for r in land if r[5] == "EXACT"]
        withline = [r for r in land if r[5] in ("EXACT", "FOLIO")]
        print(f"  {o:10s} {len(rs):6d} {len(land):6d} "
              f"{len(land)/len(rs)*100:6.1f}% "
              f"{len(ex)/max(1,len(withline))*100:10.1f}%")

    head = [r for r in scored if r[1] == "HEAD"]
    obs = sum(1 for r in head if r[5] != "MISS") / len(head)
    ctrl = []
    for j in range(NSHUF):
        rng = random.Random(1000 + j)
        ctrl.append(sum(1 for r in head
                        if inside(r[0], bypage[rng.choice(citedpages)]))
                    / len(head))
    m = sum(ctrl) / len(ctrl)
    sd = (sum((c - m) ** 2 for c in ctrl) / (len(ctrl) - 1)) ** 0.5
    sig = (obs - m) / sd if sd else float("inf")
    print(f"\n  HEADWORDS, which are the key's own claim:")
    print(f"    stands on the cited folio       {obs*100:.1f}%")
    print(f"    control, folio shuffled         {m*100:.1f}%")
    print(f"    {sig:.1f} sigma against a bar of {BAR}  -> "
          f"{'PASS' if sig >= BAR else 'FAIL'}")

    res = [r for r in head if r[5] == "MISS"]
    print(f"\n  RESIDUE: {len(res)} headword citations on "
          f"{len({r[0] for r in res})} codes miss their folio.")
    print(f"  These are the ones to read by hand. Each is our parse, a "
          f"spelling\n  the transcription writes differently, or their slip.")
    if "--residue" in argv:
        print()
        for h, o, g, f, l, k in sorted(res, key=lambda r: (r[0], r[3])):
            print(f"    {h:22s} {f}:{str(l or '--'):>2s}  {g[:44]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
