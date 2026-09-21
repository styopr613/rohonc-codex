"""What is already known about the pieces of a code.

A Rohonc code is often a phrase written without a space, and the costliest
mistake this project recorded was guessing at a whole token whose halves were
both already in the dictionary. Before guessing, look here. Prints every way
the hex splits on glyph boundaries into pieces that are themselves known,
and what each piece says, from K&T's dictionary first and ours second.

A piece COMBINES with its neighbours. It does not hand down its meaning to
the whole. Read the output as ingredients, never as an answer.

    python3 ktparts.py HEX [HEX ...]
"""
import json
import sys

import ktcross as K


def known(h, gl, prop, raw):
    out = []
    if h in gl:
        out.append('KT: ' + '; '.join(gl[h])[:90])
    v = prop.get(h)
    if isinstance(v, dict) and v.get('gloss'):
        out.append(f"{v['tier']}: {v['gloss']}")
    return ' | '.join(out)


def splits(h, ok, lo=3):
    """Every split of h into >=2 pieces, each a known code."""
    if not h:
        yield []
        return
    for i in range(lo, len(h) + 1, 3):
        pre = h[:i]
        if pre in ok:
            for rest in splits(h[i:], ok, lo):
                yield [pre] + rest


def uses(h, gl, p, doc):
    """Every token type in the book that contains h on glyph boundaries."""
    import ktaffix as A
    from collections import Counter
    c = Counter()
    for pg in doc:
        for ln in pg.lines:
            for run in ln:
                for t in run:
                    c[K.hx(A.strip(t)[0])] += 1
    out = []
    for t, n in c.items():
        j = t.find(h)
        while j != -1:
            if j % 3 == 0 and (j + len(h)) % 3 == 0:
                out.append((n, t, known(t, gl, p, None)))
                break
            j = t.find(h, j + 1)
    out.sort(reverse=True)
    return out


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    if '--uses' in argv:
        for h in [a for a in argv if not a.startswith('--')]:
            u = uses(h, gl, p, doc)
            print(f"=== {h} appears inside {len(u)} token types")
            for n, t, k in u[:30]:
                print(f"    {n:>5}x  {t:<26}{k[:86]}")
            print()
        return 0
    ok = set(gl) | {k for k, v in p.items()
                    if isinstance(v, dict) and v.get('gloss')
                    and v.get('tier') != 'G'}
    for h in [a for a in argv if not a.startswith('--')]:
        print(f"=== {h}")
        for i in range(3, len(h), 3):
            a, b = h[:i], h[i:]
            ka, kb = known(a, gl, p, None), known(b, gl, p, None)
            if ka or kb:
                print(f"    {a:<12} {ka[:80]:<82}")
                print(f"    {b:<12} {kb[:80]}")
                print()
        best = [s for s in splits(h, ok) if len(s) > 1]
        for s in best[:6]:
            print('    FULL  ' + '  +  '.join(
                f"{x}({known(x, gl, p, None)[:44]})" for x in s))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
