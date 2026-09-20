"""One folio beside the source passage it is telling, so the gaps can be read.

A sign that occurs once cannot be checked at a second occurrence, and reading
it from its own line alone is weak. But the codex names its source for every
reading -- evangelist and chapter -- and the content is standard. So the page
is a puzzle with a known picture: find the passage in the reference corpus,
lay it beside the rendering, and the hole in the line is whatever the source
has in that slot. That is a reading against an outside text, not a guess.

    python ktpage.py 108r "salt of the earth"
    python ktpage.py 108r --find          # guess the passage from the page

Gaps are marked <<hex>> so they can be fed straight to ktcontext.py.
"""
import os
import re
import sys

import corpus
import ktcontext as X
import ktgap as G
import ktaffix as A

REF = os.path.join(corpus.DATA, "ref", "rohonc")
BOOKS = ["bible_kjv", "apocrypha_wake", "golden_legend",
         "plays_york", "plays_towneley", "plays_chester", "plays_ntown"]


def load_refs():
    out = {}
    for b in BOOKS:
        p = os.path.join(REF, b + ".txt")
        if os.path.exists(p):
            out[b] = open(p, encoding="utf-8", errors="replace").read()
    return out


def window(text, i, before=420, after=900):
    return " ".join(text[max(0, i - before):i + after].split())


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    folio = argv[0]
    gl, doc, seg, var, prop = G.build()
    page = next((p for p in doc if p.page == folio), None)
    if page is None:
        print(f"no folio {folio}")
        return 1

    print("=" * 78)
    print(f"FOLIO {folio}   as far as it reads")
    print("=" * 78)
    for i, ln in enumerate(page.lines, 1):
        toks = [t for run in ln for t in run]
        if not toks:
            continue
        cells = []
        for t in toks:
            if G.readable(t, gl, seg, var, prop):
                cells.append(G.word(t, gl, seg, var, prop))
            else:
                cells.append("<<" + X.hx(A.strip(t)[0]) + ">>")
        print(f"{i:2d}  " + " ".join(cells))

    phrase = " ".join(a for a in argv[1:] if not a.startswith("--"))
    if not phrase:
        return 0
    refs = load_refs()
    key = re.sub(r"[^a-z ]", "", phrase.lower())
    hits = 0
    print()
    print("=" * 78)
    print(f"SOURCE passages containing: {phrase}")
    print("=" * 78)
    for name, text in refs.items():
        low = text.lower()
        start = 0
        while True:
            j = low.find(key, start)
            if j < 0 or hits >= 4:
                break
            print(f"\n--- {name} ---")
            print(window(text, j))
            hits += 1
            start = j + len(key)
    if not hits:
        print("not found in the reference corpus")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
