"""Guesses that share a stem with another reading but say something else.

A code COMBINES with what it contains. It does not inherit the meaning, but
it does not usually contradict it either: if 0607a3670ae0 is 'is baptized'
then 0607a3 is not 'condemned'. This lists every pair where one reading's
code sits inside another's on glyph boundaries and the two glosses share no
content word, so a person can look.

Pairs where the shorter piece is a very common structural code are dropped:
520 is K&T's verbal prefix and opens a third of the book, and a pair built
on it says nothing. The cut is: the inner code must occur in fewer than 40
token types.

    python3 ktgroot.py
"""
import json
import sys
from collections import Counter

import ktaffix as A
import ktcross as K
import ktrederive as R

MAXSPREAD = 40


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    ours = {k: v for k, v in p.items() if not k.startswith('_')
            and isinstance(v, dict) and v.get('gloss')
            and v.get('tier') in ('A', 'B', 'C', 'D', 'G')}

    types = Counter()
    for pg in doc:
        for ln in pg.lines:
            for run in ln:
                for t in run:
                    types[K.hx(A.strip(t)[0])] += 1
    spread = Counter()
    for t in types:
        for h in ours:
            if len(h) >= len(t):
                continue
            j = t.find(h)
            while j != -1:
                if j % 3 == 0 and (j + len(h)) % 3 == 0:
                    spread[h] += 1
                    break
                j = t.find(h, j + 1)

    rows = []
    keys = sorted(ours)
    for a in keys:
        if spread[a] >= MAXSPREAD:
            continue
        sa = R.stems(ours[a]['gloss'])
        if not sa:
            continue
        for b in keys:
            if len(b) <= len(a):
                continue
            j = b.find(a)
            inside = False
            while j != -1:
                if j % 3 == 0 and (j + len(a)) % 3 == 0:
                    inside = True
                    break
                j = b.find(a, j + 1)
            if not inside:
                continue
            sb = R.stems(ours[b]['gloss'])
            if sb and not (sa & sb):
                rows.append((a, ours[a], b, ours[b]))
    for a, va, b, vb in rows:
        print(f"{a:<26}{va['tier']} {va['gloss'][:28]:<30}"
              f"inside {b:<28}{vb['tier']} {vb['gloss'][:28]}")
    print(f"-- {len(rows)} pairs")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
