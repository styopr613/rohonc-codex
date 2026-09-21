"""Unread signs that differ from a sign K&T read by ONE glyph.

The transcription is a string of three-digit glyph codes. A scribe copying a
long compilation spells the same word more than one way, and K&T's own
dictionary records that with its "var." entries. What is left unread in this
book is full of words that are some read word with a single glyph swapped,
added or dropped -- 520151520390 and 520151520391 are the same word, and only
one of them was in the dictionary.

This compares every unread sign against every read one at the level of whole
glyphs, and reports the pairs one glyph apart. A hit is a candidate variant,
not a reading: one glyph is also the difference between many genuinely
different words, so the occurrence has to agree before anything is written
down.

    python ktnear.py             every unread sign one glyph from a read one
    python ktnear.py --min N     only signs of N glyphs or more (default 3;
                                 at two glyphs almost everything is one away
                                 from something)
"""
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import kttranslate as T


def glyphs(h):
    return tuple(h[i:i + 3] for i in range(0, len(h), 3))


def one_away(a, b):
    """True if b is a with exactly one glyph substituted, inserted or dropped."""
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    if abs(len(a) - len(b)) != 1:
        return False
    long, short = (a, b) if len(a) > len(b) else (b, a)
    i = 0
    while i < len(short) and short[i] == long[i]:
        i += 1
    return short[i:] == long[i + 1:]


def main(argv):
    ming = 3
    if "--min" in argv:
        ming = int(argv[argv.index("--min") + 1])
    gl, doc, seg, var, prop, inv = K.build()
    read = {}
    for c, senses in gl.items():
        read[K.hx(c)] = "; ".join(sorted({s.strip() for s in senses}))[:70]
    for c, (g, tier) in prop.items():
        read.setdefault(K.hx(c), g.replace("_", " ") + f" [this project, {tier}]")
    by_len = defaultdict(list)
    for h, g in read.items():
        by_len[len(glyphs(h))].append((glyphs(h), h, g))

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
        gh = glyphs(h)
        if len(gh) < ming:
            continue
        near = []
        for L in (len(gh) - 1, len(gh), len(gh) + 1):
            for gb, hb, g in by_len.get(L, ()):
                if one_away(gh, gb):
                    near.append((hb, g))
        if near:
            rows.append((len(where[h]), h, near))
    rows.sort(key=lambda r: -r[0])
    print(f"{len(rows)} unread signs of {ming}+ glyphs are one glyph from a read sign\n")
    for n, h, near in rows:
        print(f"=== {h}   x{n}")
        for hb, g in near[:3]:
            print(f"    vs {hb}  = {g}")
        for pg, i, s in where[h][:3]:
            print(f"    {pg}:{i:<3d} {s[:150]}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
