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
import ktaffix as A
import ktvariant as V


def build():
    """The same inventory kttranslate.py renders with, extended segmentation
    included. Building it from ktcoverage alone left this tool one step
    behind the page: it listed lines as one word short that the extended
    cut had already closed."""
    gl, doc, seg, var = X.load()      # extended segmentation, proposals loaded
    return gl, doc, seg, var, T.load_proposals()


def readable(t, gl, seg, var, prop):
    t = A.strip(t)[0]
    return t in gl or t in seg or t in var or t in prop


def word(t, gl, seg, var, prop):
    b, mark = A.strip(t)
    if b in prop:
        return ("+" if prop[b][1] in ("A","B") else "?") + prop[b][0].replace(" ", "_") + mark
    return X.word(t, gl, seg, var)


def wide(doc, gl, seg, var, prop, pages=None, start=0, count=40):
    """Gap lines with the line before and after, so the sentence can be read.

    A gap in isolation is usually unreadable; the same gap inside its
    paragraph usually is not. This prints the neighbours.
    """
    out = []
    for p in doc:
        if pages and p.page not in pages:
            continue
        lines = [[t for run in ln for t in run] for ln in p.lines]
        for i, toks in enumerate(lines):
            if not toks:
                continue
            un = [t for t in toks if not readable(t, gl, seg, var, prop)]
            if len(un) != 1:
                continue
            def render(ts, mark=None):
                return " ".join("<<" + X.hx(t) + ">>" if (mark is not None and t is mark)
                                else word(t, gl, seg, var, prop) for t in ts)
            before = render(lines[i - 1]) if i > 0 and lines[i - 1] else ""
            after = render(lines[i + 1]) if i + 1 < len(lines) and lines[i + 1] else ""
            out.append((p.page, i + 1, un[0], before, render(toks, un[0]), after))
    return out[start:start + count]


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
    if "--wide" in argv:
        gl, doc, seg, var, prop = build()
        k = argv.index("--wide")
        start = int(argv[k + 1]) if len(argv) > k + 1 and argv[k + 1].isdigit() else 0
        cnt = int(argv[k + 2]) if len(argv) > k + 2 and argv[k + 2].isdigit() else 30
        pages = {argv[argv.index("--page") + 1]} if "--page" in argv else None
        for pg, i, t, b, m, a in wide(doc, gl, seg, var, prop, pages, start, cnt):
            print(f"\n{pg}:{i}")
            if b:
                print(f"   -  {b[:150]}")
            print(f"   >  {m[:150]}")
            if a:
                print(f"   +  {a[:150]}")
        return 0

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
