"""Evidence for a batch of flagged readings, compact enough to read many.

For each sign: the gloss, then every occurrence rendered as the book prints
it, with the cited passage's verdict on the reading's own word. Nothing is
decided here and nothing is scored. It prints what a person needs to see.

    python3 ktevid.py HEX HEX ...
    python3 ktevid.py --flag DUP --top 20
"""
import json
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R
import kttranslate as T

MAXOCC = 7


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    vv, vd = L.verses(), L.verses_dr()
    pool = {}
    for pg in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pg))
        if r:
            s = set()
            for k, txt in L.passage(vv, r) + L.passage(vd, r):
                s |= R.stems(txt)
            pool[pg] = (s, r)

    want = [a for a in argv if not a.startswith('--')]
    if '--flag' in argv:
        import ktharden
        sys.argv = ['x', '--flag', argv[argv.index('--flag') + 1]]
        return ktharden.main(sys.argv[1:])

    for h in want:
        v = p.get(h)
        if not v:
            print(f"=== {h}  ABSENT"); continue
        st = R.stems(v.get('gloss', ''))
        print(f"=== {h}  tier {v['tier']}  \"{v['gloss']}\"  n={v.get('n')}")
        ev = v.get('evidence', '')
        print(f"    why: {ev[:150]}")
        n = 0
        for pg in doc:
            if n >= MAXOCC:
                break
            for i, ln in enumerate(pg.lines, 1):
                toks = [x for run in ln for x in run]
                if not any(K.hx(A.strip(t)[0]) == h for t in toks):
                    continue
                r = ' '.join(T.render_token(t, gl, seg, False, var, prop)
                             for t in toks)
                tag = ''
                if pg.page in pool:
                    s, refs = pool[pg.page]
                    tag = ' [IN PASSAGE]' if st & s else ' [NOT in passage]'
                    tag += ' ' + ','.join(f"{x[0]} {x[1]}:{x[2]}" for x in refs[:2])
                print(f"    {pg.page}:{i:<3}{tag}")
                print(f"      {r[:155]}")
                n += 1
                if n >= MAXOCC:
                    break
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
