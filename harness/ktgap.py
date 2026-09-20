"""Lines that are one word short, so the missing word can be read from the line.

A sign that occurs once cannot be checked against a second occurrence. That
is the only thing it cannot have. It can still be READ, the way any missing
word in a sentence is read, as soon as everything around it is readable --
and 1,534 lines of the codex are currently exactly one word short.

This lists them and prints the gap in its line. Pages already translated come
first, because there the story is known and the guess is strongest.

    python ktgap.py              # count, and the signs involved
    python ktgap.py --done       # only lines on translated folios
    python ktgap.py --page 053r  # one folio
"""
import sys
from collections import Counter

import ktcontext as X
import ktcoverage as C
import kttranslate as T
import ktvariant as V


def build():
    gl, doc, seg = C.build()
    var = {v: h for v, (h, _) in V.readings()[6].items()}
    prop = T.load_proposals()
    return gl, doc, seg, var, prop


def readable(t, gl, seg, var, prop):
    return t in gl or t in seg or t in var or t in prop


def word(t, gl, seg, var, prop):
    if t in prop:
        return "+" + prop[t].replace(" ", "_")
    return X.word(t, gl, seg, var)


def gaps(doc, gl, seg, var, prop, pages=None):
    out = []
    for p in doc:
        if pages and p.page not in pages:
            continue
        for i, ln in enumerate(p.lines, 1):
            toks = [t for run in ln for t in run]
            if not toks:
                continue
            un = [t for t in toks if not readable(t, gl, seg, var, prop)]
            if len(un) != 1:
                continue
            s = " ".join("<<" + X.hx(t) + ">>" if t == un[0]
                         else word(t, gl, seg, var, prop) for t in toks)
            out.append((p.page, i, un[0], s))
    return out


def main(argv):
    gl, doc, seg, var, prop = build()
    types = Counter(t for p in doc for t in p.tokens)
    if "--page" in argv:
        pg = {argv[argv.index("--page") + 1]}
        for page, i, t, s in gaps(doc, gl, seg, var, prop, pg):
            print(f"  {page}:{i:<3d} n={types[t]:<3d} {s}")
        return
    pages = X.DONE if "--done" in argv else None
    g = gaps(doc, gl, seg, var, prop, pages)
    sigs = Counter(t for _, _, t, _ in g)
    print(f"lines one word short: {len(g)}")
    print(f"  distinct signs {len(sigs)}, carrying {sum(types[t] for t in sigs)} tokens")
    print(f"  of those signs, occur once in the whole book: "
          f"{sum(1 for t in sigs if types[t] == 1)}")
    print()
    for page, i, t, s in g[:60]:
        print(f"  {page}:{i:<3d} n={types[t]:<3d} {s[:150]}")
    if len(g) > 60:
        print(f"  ... {len(g)-60} more")


if __name__ == "__main__":
    main(sys.argv[1:])
