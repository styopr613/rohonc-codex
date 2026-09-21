"""Every bracketed guess, compactly, in one pass, for reading by hand.

One block per guess: the gloss, how many times it occurs, every occurrence
as the book prints it, and which verses the folio's note cites. Enough to
judge most of them without opening anything else; ktguessread.py --full
prints the passage text when a block is not enough.

    python3 ktgbatch.py [--from N] [--n N] [--class SOURCED|ABSENT|...]
"""
import json
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R
import kttranslate as T

MAXOCC = 5


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    start = int(argv[argv.index('--from') + 1]) if '--from' in argv else 0
    n = int(argv[argv.index('--n') + 1]) if '--n' in argv else 25
    vv, vd = L.verses(), L.verses_dr()

    refs = {}
    pool = {}
    for pgn in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pgn))
        if r:
            refs[pgn] = r
            s = set()
            for k, txt in L.passage(vv, r) + L.passage(vd, r):
                s |= R.stems(txt)
            pool[pgn] = s

    guesses = {k for k, v in p.items() if not k.startswith('_')
               and isinstance(v, dict) and v.get('tier') == 'G'}
    occ = defaultdict(list)
    for pg in doc:
        for i, ln in enumerate(pg.lines, 1):
            toks = [x for run in ln for x in run]
            hs = {K.hx(A.strip(t)[0]) for t in toks}
            hit = hs & guesses
            if not hit:
                continue
            rend = ' '.join(T.render_token(t, gl, seg, False, var, prop)
                            for t in toks)
            for h in hit:
                occ[h].append((pg.page, i, rend))

    order = sorted(guesses, key=lambda h: (-len(occ[h]), h))
    for h in order[start:start + n]:
        v = p[h]
        st = R.stems(v.get('gloss', ''))
        print(f"=== {h}  \"{v.get('gloss','')}\"  occ={len(occ[h])}")
        ev = ' '.join(v.get('evidence', '').split())
        if ev.startswith('MOVED FROM TIER D'):
            ev = 'was tier D: ' + ev.split('Prior tier D evidence:')[-1]
        print(f"  why: {ev[:230]}")
        for pgn, i, rend in occ[h][:MAXOCC]:
            r = refs.get(pgn, [])
            tag = ''
            if r:
                tag = ('IN ' if st & pool[pgn] else '   ') + \
                      ','.join(f"{x[0]} {x[1]}:{x[2]}" for x in r[:2])
            print(f"  {pgn}:{i:<3} {tag}")
            print(f"     {rend[:175]}")
        if len(occ[h]) > MAXOCC:
            print(f"     ... {len(occ[h]) - MAXOCC} more")
        print()
    print(f"-- guesses {start}..{start+n} of {len(order)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
