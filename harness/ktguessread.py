"""One guess, everything a person needs to judge it, printed once.

Gloss, why it was entered, every occurrence as the book prints it, and the
text of the passage the folio's note cites -- because the way to replace a
wrong guess is to read the source and find the word that belongs in the slot.

    python3 ktguessread.py HEX [HEX ...]        [--full] [--occ N]
"""
import json
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R
import kttranslate as T


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    vv, vd = L.verses(), L.verses_dr()
    maxocc = int(argv[argv.index('--occ') + 1]) if '--occ' in argv else 6
    full = '--full' in argv
    skip = set()
    for i, a in enumerate(argv):
        if a in ('--occ',):
            skip.add(i + 1)
    want = [a for i, a in enumerate(argv)
            if not a.startswith('--') and i not in skip]

    refs_by_page = {}
    for pg in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pg))
        if r:
            refs_by_page[pg] = r

    occ = defaultdict(list)
    for pg in doc:
        for i, ln in enumerate(pg.lines, 1):
            toks = [x for run in ln for x in run]
            hs = {K.hx(A.strip(t)[0]) for t in toks}
            for h in hs & set(want):
                occ[h].append((pg.page, i, toks))

    for h in want:
        v = p.get(h)
        if not isinstance(v, dict):
            print(f"=== {h}  ABSENT FROM proposals.json\n")
            continue
        st = R.stems(v.get('gloss', ''))
        print(f"=== {h}  tier {v['tier']}  \"{v.get('gloss','')}\"  "
              f"n={v.get('n')}  occurrences={len(occ[h])}")
        print(f"    why: {v.get('evidence','')[:400]}")
        pages = []
        for pgn, i, toks in occ[h][:maxocc]:
            r = ' '.join(T.render_token(t, gl, seg, False, var, prop)
                         for t in toks)
            refs = refs_by_page.get(pgn, [])
            tag = ''
            if refs:
                s = set()
                for k, txt in L.passage(vv, refs) + L.passage(vd, refs):
                    s |= R.stems(txt)
                tag = (' [IN]' if st & s else ' [not in]') + ' ' + \
                      ','.join(f"{x[0]} {x[1]}:{x[2]}" for x in refs[:3])
            print(f"    {pgn}:{i:<3}{tag}")
            print(f"      {r if full else r[:190]}")
            if pgn not in pages:
                pages.append(pgn)
        if len(occ[h]) > maxocc:
            print(f"    ... {len(occ[h]) - maxocc} more")
        if full:
            for pgn in pages[:3]:
                refs = refs_by_page.get(pgn)
                if not refs:
                    continue
                print(f"    --- {pgn} cites "
                      f"{','.join(f'{x[0]} {x[1]}:{x[2]}' for x in refs)}")
                for k, txt in L.passage(vd, refs)[:14]:
                    print(f"      {k}  {txt[:170]}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
