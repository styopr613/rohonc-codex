"""Guesses whose code splits cleanly into codes that are already read.

The costliest mistake this project recorded was guessing at a whole token
whose halves were both already in the dictionary. This asks that question of
every bracketed guess at once. A split is reported only when EVERY piece is
read -- by K&T, by a variant, or by a reading entered here that is not itself
a guess.

A code COMBINES with its pieces. It does not inherit their meaning. The
output is ingredients, and the check is whether the guess is consistent with
what the pieces say, not whether it equals them.

    python3 ktgsplit.py            [--tier G]
"""
import json
import sys
from collections import Counter

import ktaffix as A
import ktcross as K


def splits(h, ok, memo=None):
    if memo is None:
        memo = {}
    if h in memo:
        return memo[h]
    if not h:
        return [[]]
    out = []
    for i in range(3, len(h) + 1, 3):
        if h[:i] in ok:
            for rest in splits(h[i:], ok, memo):
                out.append([h[:i]] + rest)
    memo[h] = out
    return out


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    tier = argv[argv.index('--tier') + 1] if '--tier' in argv else 'G'

    def un(x):
        return "".join(chr(0xE000 + int(x[i:i + 3], 16))
                       for i in range(0, len(x), 3))

    def sense(x):
        s = un(x)
        if s in gl:
            return "; ".join(sorted(gl[s]))[:40]
        if s in var:
            t = var[s]
            return "~" + "; ".join(sorted(gl.get(t, {"?"})))[:38]
        v = p.get(x)
        if isinstance(v, dict) and v.get('gloss') and v.get('tier') != 'G':
            return f"{v['tier']}:{v['gloss']}"
        return None

    cnt = Counter()
    for pg in doc:
        for ln in pg.lines:
            for run in ln:
                for t in run:
                    cnt[K.hx(A.strip(t)[0])] += 1

    known = set()
    for x in list(gl) + list(var):
        known.add(K.hx(x))
    for k, v in p.items():
        if (not k.startswith('_') and isinstance(v, dict)
                and v.get('gloss') and v.get('tier') != 'G'):
            known.add(k)

    n = 0
    for h in sorted(k for k, v in p.items()
                    if not k.startswith('_') and isinstance(v, dict)
                    and v.get('tier') == tier):
        if len(h) < 6:
            continue
        ss = [s for s in splits(h, known) if len(s) > 1]
        if not ss:
            continue
        n += 1
        ss.sort(key=len)
        print(f"=== {h}  \"{p[h].get('gloss','')}\"  n={cnt.get(h,0)}")
        for s in ss[:3]:
            print("    " + "  +  ".join(f"{x}({sense(x)})" for x in s))
    print(f"-- {n} guesses split entirely into read codes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
