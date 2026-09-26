"""A folio, token by token, with the hex, the reading and where it came from.

The rendered page tells you what the book says. This tells you which sign
said it, so a guess can be checked against its neighbours and against the
passage the note cites.

    python3 ktline.py 072v            [--line 5] [--src]
"""
import json
import sys

import ktaffix as A
import ktcross as K
import ktleft as L
import kttranslate as T


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    want = [a for a in argv if not a.startswith('--')]
    only = int(argv[argv.index('--line') + 1]) if '--line' in argv else None
    for pgn in want:
        pages = [x for x in doc if x.page == pgn]
        if not pages:
            print(f"{pgn}: no such folio")
            continue
        refs = L.refs_in(K.note_for(pgn))
        print(f"=== {pgn}   cites "
              + (','.join(f"{x[0]} {x[1]}:{x[2]}" for x in refs) or "nothing"))
        if '--src' in argv and refs:
            vd = L.verses_dr()
            for k, txt in L.passage(vd, refs)[:20]:
                print(f"    {k}  {txt[:165]}")
        for pg in pages:
            for i, ln in enumerate(pg.lines, 1):
                if only and i != only:
                    continue
                toks = [x for run in ln for x in run]
                phr = [j in T.phrase_slots(run) for run in ln for j in range(len(run))]
                wrd = [T.phrase_slots(run).get(j) for run in ln for j in range(len(run))]
                print(f"  --- line {i}")
                for t, inp, pw in zip(toks, phr, wrd):
                    s, mark = A.strip(t)
                    h = K.hx(s)
                    r = pw if inp else T.render_token(t, gl, seg, False, var, prop)
                    v = p.get(h)
                    if inp:
                        src = 'expr'
                    elif s in gl:
                        src = 'KT'
                    elif isinstance(v, dict) and v.get('gloss'):
                        src = v.get('tier', '?')
                    elif s in seg:
                        src = 'seg'
                    elif s in var:
                        src = 'var'
                    else:
                        src = '--'
                    print(f"      {h:<26}{src:<5}{r[:60]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
