"""Triage of every bracketed guess, so the hand pass runs in a sensible order.

This decides NOTHING. It sorts. For each tier G sign it reports how many
times the sign occurs, how many of those occurrences sit on a folio whose
note cites a chapter and verse, and at how many of THOSE the guess's own
word is a content word of the cited passage.

    SOURCED   every cited occurrence has the guess's word in the passage,
              and there is at least one cited occurrence. Read these first:
              a guess that keeps landing in its own source is a reading
              waiting to be promoted, or an error hiding in plain sight.
    SPLIT     some cited occurrences have it, some do not.
    ABSENT    the sign sits on cited folios and the guess's word is in none
              of them. These are where a wrong guess lives.
    NOCITE    no folio carrying this sign cites anything. The source cannot
              speak; only the surrounding reading can.
    FUNCTION  the guess is a function word -- "but", "so", "not", "as" --
              which stems to nothing, so the passage test can never report
              it present. Added after the first run put 196 signs in ABSENT
              and a good share of them were function words that the test was
              structurally incapable of finding. A test that cannot fail in
              one direction must not be allowed to convict in the other.

The word test is stem overlap against the Vulgate-Douay and the King James
of every verse the folio notes cite, the same pool ktevid.py prints. It is
weak evidence on its own -- a passage has a few hundred stems and a gloss
has one or two -- which is exactly why this file only orders the queue and
never writes to proposals.json.
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
    pool = {}
    for pg in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pg))
        if r:
            s = set()
            for k, txt in L.passage(vv, r) + L.passage(vd, r):
                s |= R.stems(txt)
            pool[pg] = (s, r)

    guesses = {k: v for k, v in p.items() if not k.startswith('_')
               and isinstance(v, dict) and v.get('tier') == 'G'}

    occ = defaultdict(list)          # hex -> [(page, lineno)]
    for pg in doc:
        for i, ln in enumerate(pg.lines, 1):
            for run in ln:
                for t in run:
                    h = K.hx(A.strip(t)[0])
                    if h in guesses:
                        occ[h].append((pg.page, i))

    rows = []
    for h, v in guesses.items():
        st = R.stems(v.get('gloss', ''))
        cited = [(pgn, i) for pgn, i in occ[h] if pgn in pool]
        hit = sum(1 for pgn, i in cited if st & pool[pgn][0])
        if not st:
            cls = 'FUNCTION'
        elif not cited:
            cls = 'NOCITE'
        elif hit == len(cited):
            cls = 'SOURCED'
        elif hit:
            cls = 'SPLIT'
        else:
            cls = 'ABSENT'
        rows.append((cls, h, v.get('gloss', ''), len(occ[h]), len(cited), hit))

    only = argv[argv.index('--class') + 1] if '--class' in argv else None
    order = {'SOURCED': 0, 'SPLIT': 1, 'ABSENT': 2, 'NOCITE': 3,
             'FUNCTION': 4}
    rows.sort(key=lambda r: (order[r[0]], -r[3], r[1]))
    counts = defaultdict(int)
    for r in rows:
        counts[r[0]] += 1
    if '--summary' in argv:
        print(f"{len(rows)} guesses")
        for c in ('SOURCED', 'SPLIT', 'ABSENT', 'NOCITE', 'FUNCTION'):
            print(f"  {c:<8}{counts[c]:>5}")
        zero = sum(1 for r in rows if r[3] == 0)
        print(f"  (occurring zero times as a whole token: {zero})")
        return 0
    for cls, h, g, n, nc, hit in rows:
        if only and cls != only:
            continue
        print(f"{cls:<8}{h:<24}{g[:34]:<36}n={n:<4}cited={nc:<4}in={hit}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
