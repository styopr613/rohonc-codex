"""Unread signs that are PART of a sign K&T already read.

Where this came from: 'towel' and 'cling' were both got by noticing, by eye,
that an unread sign was sitting inside a compound K&T had already glossed --
520af0a105204e4 'wipe with kerchief' contains a105204e4, and their 'cling'
entry contains 060041. Both readings are tier B, because K&T's own dictionary
supplies the evidence and nothing in this project has to be assumed.

That was luck. This does it for every unread sign at once: take the hex of
each sign the rendering cannot read, and look for it inside the hex of every
sign that IS read. A hit means K&T glossed a longer word that contains this
one, and the gloss of the longer word names the field the shorter one is in.

WHAT A HIT IS AND IS NOT. It is not a reading. A sign inside a compound may
be the head of it, a modifier, an affix, or an accident of the writing -- the
transcription is a string of glyph codes and short strings collide. What the
hit gives is a strong, independent starting point, and the occurrences
printed beside it are what decides. Only the ones where the parent gloss and
every occurrence agree get written down.

    python ktinside.py            every unread sign found inside a read one
    python ktinside.py --min N    only signs of N hex digits or more
                                  (short ones collide by chance; 6 is sane)
"""
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import kttranslate as T


def main(argv):
    minlen = 6
    if "--min" in argv:
        minlen = int(argv[argv.index("--min") + 1])
    gl, doc, seg, var, prop, inv = K.build()

    # every sign that HAS a reading, with the words it was read as
    read = {}
    for c, senses in gl.items():
        read[K.hx(c)] = "; ".join(sorted({s.strip() for s in senses}))[:120]
    for c, (g, tier) in prop.items():
        read.setdefault(K.hx(c), g.replace("_", " ") + f" [this project, {tier}]")

    where = defaultdict(list)
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            miss = {A.strip(t)[0] for t in tk if A.strip(t)[0] not in inv}
            for b in miss:
                s = " ".join("<<___>>" if A.strip(t)[0] == b
                             else T.render_token(t, gl, seg, False, var, prop)
                             for t in tk)
                where[K.hx(b)].append((p.page, i, s))

    hits = []
    for h in where:
        if len(h) < minlen:
            continue
        parents = [(ph, g) for ph, g in read.items() if h in ph and ph != h]
        if parents:
            hits.append((len(where[h]), h, parents))
    hits.sort(key=lambda r: -r[0])

    print(f"{len(hits)} unread signs of {minlen}+ hex digits sit inside a read sign\n")
    for n, h, parents in hits:
        print(f"=== {h}   x{n}")
        for ph, g in parents[:4]:
            pos = "head" if ph.startswith(h) else ("tail" if ph.endswith(h) else "inside")
            print(f"    in {ph}  ({pos})  = {g}")
        for pg, i, s in where[h][:4]:
            print(f"    {pg}:{i:<3d} {s[:150]}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
