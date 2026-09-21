"""Unread signs that are ALMOST entirely made of signs already read.

ktsegment splits a sign only when EVERY part of it is known, so a word that
is two read signs plus three unexplained hex digits falls through and is
reported as a hole. That is the commonest shape left in the book: the codex
writes phrases without a space, and the compiler's spelling wanders by a
glyph or two, so one element of a long compound fails to match.

This covers each unread sign with the longest read signs it can, left to
right, and reports how much of it is accounted for and what the gaps are.
A sign whose known parts are 'Lord' and 'crucify' with four digits left
over is not a mystery word; it is a phrase with a spelling this project has
not seen, and the line usually settles it.

    python ktcover.py            every unread sign, best-covered first
    python ktcover.py --min F    only those at least F covered (0.6 default)
"""
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import kttranslate as T


def cover(h, read, lens):
    """Greedy longest-match left to right. (pieces, covered_digits)."""
    out, i, cov = [], 0, 0
    while i < len(h):
        for L in lens:
            if L <= len(h) - i and h[i:i + L] in read:
                out.append((h[i:i + L], read[h[i:i + L]]))
                cov += L
                i += L
                break
        else:
            if out and out[-1][1] is None:
                out[-1] = (out[-1][0] + h[i], None)
            else:
                out.append((h[i], None))
            i += 1
    return out, cov


def main(argv):
    floor = 0.6
    if "--min" in argv:
        floor = float(argv[argv.index("--min") + 1])
    gl, doc, seg, var, prop, inv = K.build()
    read = {}
    for c, senses in gl.items():
        read[K.hx(c)] = "; ".join(sorted({s.strip() for s in senses}))[:44]
    for c, (g, tier) in prop.items():
        read.setdefault(K.hx(c), g.replace("_", " "))
    lens = sorted({len(k) for k in read}, reverse=True)

    where = defaultdict(list)
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            for b in {A.strip(t)[0] for t in tk if A.strip(t)[0] not in inv}:
                s = " ".join("<<[x]>>" if A.strip(t)[0] == b
                             else T.render_token(t, gl, seg, False, var, prop)
                             for t in tk)
                where[K.hx(b)].append((p.page, i, s))

    rows = []
    for h in where:
        pieces, cov = cover(h, read, lens)
        if len(h) and cov / len(h) >= floor and any(g for _, g in pieces):
            rows.append((cov / len(h), len(where[h]), h, pieces))
    rows.sort(key=lambda r: (-r[1], -r[0]))
    print(f"{len(rows)} unread signs are at least {floor:.0%} made of signs already read\n")
    for frac, n, h, pieces in rows:
        print(f"=== {h}   x{n}   {frac:.0%} accounted for")
        print("    " + "  +  ".join(f"{p}={g}" if g else f"{p}=???" for p, g in pieces))
        for pg, i, s in where[h][:3]:
            print(f"    {pg}:{i:<3d} {s[:150]}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
