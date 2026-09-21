"""THE ODD WORD OUT: a reading whose own line agrees with the source, but it
does not.

ktharden.py's SOURCE flag asks whether a reading's English word is in the
passage its folio cites. That is too blunt on its own, and 83 readings raise
it while most are correct: the book retells in its own vocabulary, so a word
can be the book's and not the passage's.

This asks the sharper question, and it is the one that actually found the
shepherd. On 064r the line read 'one who home good [sons], in turn two farm
hand' -- and fold, sheep, hireling and shepherd are all in John 10, which the
folio cites, while 'sons' is not. The LINE was anchored in its source and the
reading was the single word floating free of it.

So for every occurrence on a folio with a citation we can look up, count:

    anchor  other content words on that line whose stem IS in the passage
    hit     whether the reading's own stem is in the passage

A reading with a high mean anchor and no hits anywhere is standing, over and
over, in lines the source explains -- and is itself the one word the source
does not. That is the shape worth reading by hand.

NO BAR, and it is not a gate. Declared before the run so the ranking cannot
be fitted afterwards: the list is ordered by mean anchor among readings that
never hit, restricted to signs with at least two cited occurrences, because
one line proves nothing and this project has been burned by exactly that.

Known and expected false positives, all of them legitimate evidence that
will rank high here: a reading taken from K&T's own citation list; a formula
the book repeats in its own words (the creed, the closing doxology, the
Marian prayers); a folio whose citation names one verse of a story the page
tells at length.

    python3 ktoddone.py            ranked
    python3 ktoddone.py --sign HEX show every line, with what anchored it
"""
import json
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R
import kttranslate as T

MINCITED = 2


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    ours = {k: v for k, v in p.items()
            if not k.startswith('_') and isinstance(v, dict)
            and v.get('tier') in ('A', 'B', 'C', 'D')}
    vv, vd = L.verses(), L.verses_dr()
    pool = {}
    for pg in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pg))
        if r:
            s = set()
            for k, txt in L.passage(vv, r) + L.passage(vd, r):
                s |= R.stems(txt)
            pool[pg] = (s, r)

    rows = defaultdict(list)
    for pg in doc:
        if pg.page not in pool:
            continue
        s, refs = pool[pg.page]
        for i, ln in enumerate(pg.lines, 1):
            toks = [x for run in ln for x in run]
            rend = [T.render_token(t, gl, seg, False, var, prop) for t in toks]
            hexes = [K.hx(A.strip(t)[0]) for t in toks]
            for j, h in enumerate(hexes):
                if h not in ours:
                    continue
                mine = R.stems(ours[h].get('gloss', ''))
                if not mine:
                    continue
                anchor = set()
                for k2, r2 in enumerate(rend):
                    if k2 == j:
                        continue
                    anchor |= (R.stems(r2) & s)
                rows[h].append((pg.page, i, len(anchor), bool(mine & s),
                                sorted(anchor)[:6], ' '.join(rend)[:120]))

    if '--sign' in argv:
        h = argv[argv.index('--sign') + 1]
        v = ours.get(h, {})
        print(f"=== {h}  tier {v.get('tier')}  '{v.get('gloss')}'\n")
        for page, i, a, hit, anch, line in rows.get(h, []):
            print(f"  {page}:{i:<3} anchor {a:<3} {'HIT' if hit else '   '}  "
                  f"{','.join(anch)}")
            print(f"      {line}")
        return 0

    scored = []
    for h, occ in rows.items():
        if len(occ) < MINCITED or any(o[3] for o in occ):
            continue
        scored.append((sum(o[2] for o in occ) / len(occ), len(occ), h))
    print("THE ODD WORD OUT: never in its own source, in lines the source "
          "explains\n")
    print(f"  {len(scored)} readings stand on {MINCITED}+ cited lines and "
          f"never once appear in the passage.\n")
    print(f"  {'sign':22s} {'t':2s} {'n':>3s} {'lines':>5s} {'anchor':>7s}  gloss")
    for mean, n, h in sorted(scored, reverse=True)[:30]:
        v = ours[h]
        print(f"  {h:22s} {v['tier']:2s} {str(v.get('n')):>3s} {n:5d} "
              f"{mean:7.1f}  {v['gloss'][:28]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
