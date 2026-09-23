"""TEST 1 OF WHETHER OUR ADDITIONS ARE TRUE: do they track their source on
folios that played no part in making them?

Every reading entered here names, in its evidence, the folio or folios it was
read from. Those folios are its training data. The sign usually stands on
other folios too, and many of those cite a chapter and verse. A TRUE reading
should keep landing in the passage its folio cites even where nobody looked;
a reading invented to fit one line has no reason to.

  hit    the sign stands on a HELD-OUT folio (not named in its evidence),
         that folio cites a passage, and a content stem of the gloss is in
         that passage (Douay and King James, every cited verse)
  rate   hits / held-out cited occurrences, per tier

CONTROL, matched: the same signs on the same folios, but each reading's
gloss replaced by the gloss of a randomly chosen OTHER reading of the same
tier. 20 shuffles, mean and sd. A gloss drawn from the same vocabulary, put
on the wrong sign, should land in the passage only by chance.

CEILING: K&T's own 841 glosses, measured the same way over every cited
occurrence. Their words are true by the only standard available, and a folio
cites one passage while carrying a dozen lines, so even true words miss. This
is the number a true reading can be expected to reach.

BARS, declared before the run, not moved:

  A+B   must beat the shuffle by >= 5 sigma, and reach >= 70% of the K&T
        ceiling. Below the first, the method is broken. Below the second,
        the tier A/B readings are weaker than the dictionary they extend.
  C+D   must beat the shuffle by >= 3 sigma.
  G     reported. >= 3 sigma means the guesses carry information beyond
        the line they were read from; < 2 sigma means they do not.

What this cannot test: 742 of the 848 guesses occur once. They have no
held-out folio. Nothing here reaches them.

    python3 ktheldout.py    [--shuf N]
"""
import json
import random
import re
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R

NSHUF = 20
FOLIO = re.compile(r"\b(\d{3}[rv])\b")


def main(argv):
    nshuf = int(argv[argv.index('--shuf') + 1]) if '--shuf' in argv else NSHUF
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    vv, vd = L.verses(), L.verses_dr()
    pool = {}
    for pgn in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pgn))
        if r:
            s = set()
            for k, txt in L.passage(vv, r) + L.passage(vd, r):
                s |= R.stems(txt)
            pool[pgn] = s

    folios = defaultdict(set)          # hex -> folios it stands on
    for pg in doc:
        for ln in pg.lines:
            for run in ln:
                for t in run:
                    folios[K.hx(A.strip(t)[0])].add(pg.page)

    def hx(s):
        return "".join(f"{ord(c) - 0xE000:03x}" for c in s)

    # ---- our readings: (hex, stems, held-out cited folios)
    ours = defaultdict(list)
    for h, v in p.items():
        if h.startswith('_') or not isinstance(v, dict):
            continue
        tier = v.get('tier')
        if tier not in ('A', 'B', 'C', 'D', 'G'):
            continue
        st = R.stems(v.get('gloss', ''))
        if not st:
            continue
        seen = set(FOLIO.findall(v.get('evidence', '')))
        held = [f for f in folios.get(h, ()) if f not in seen and f in pool]
        if held:
            ours[tier].append((h, st, held))

    # ---- K&T ceiling: every cited occurrence of every glossed headword
    kt = []
    for s, g in gl.items():
        st = set()
        for x in g:
            st |= R.stems(x)
        if not st:
            continue
        cited = [f for f in folios.get(hx(s), ()) if f in pool]
        if cited:
            kt.append((hx(s), st, cited))

    def rate(rows):
        hit = tot = 0
        for h, st, held in rows:
            for f in held:
                tot += 1
                hit += bool(st & pool[f])
        return hit, tot

    def shuffled(rows, rng):
        glosses = [st for _, st, _ in rows]
        rng.shuffle(glosses)
        return rate([(h, g, held) for (h, _, held), g in zip(rows, glosses)])

    khit, ktot = rate(kt)
    ceiling = khit / ktot if ktot else 0
    print("TEST 1: SOURCE TRACKING ON HELD-OUT FOLIOS")
    print(f"  K&T ceiling   {khit}/{ktot} cited occurrences   "
          f"{ceiling*100:.1f}%   ({len(kt)} signs)")
    print()
    print(f"  {'tier':6s}{'signs':>6s}{'held-out':>10s}{'hit':>7s}"
          f"{'rate':>8s}{'shuffle':>9s}{'sd':>6s}{'sigma':>7s}"
          f"{'vs ceiling':>12s}")
    results = {}
    rng = random.Random(R.SEED)
    for group, tiers in (('A+B', 'AB'), ('C+D', 'CD'), ('G', 'G')):
        rows = [r for t in tiers for r in ours[t]]
        if not rows:
            continue
        hit, tot = rate(rows)
        nulls = []
        for _ in range(nshuf):
            h2, t2 = shuffled(rows, rng)
            nulls.append(h2 / t2 if t2 else 0)
        m = sum(nulls) / len(nulls)
        sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** .5
        obs = hit / tot if tot else 0
        sig = (obs - m) / sd if sd else 0
        results[group] = (obs, sig, len(rows), tot)
        print(f"  {group:6s}{len(rows):6d}{tot:10d}{hit:7d}{obs*100:7.1f}%"
              f"{m*100:8.1f}%{sd*100:6.2f}{sig:7.1f}"
              f"{obs/ceiling*100 if ceiling else 0:11.0f}%")
    print()
    ok = True
    if 'A+B' in results:
        obs, sig, n, tot = results['A+B']
        a = sig >= 5 and obs >= 0.7 * ceiling
        print(f"  BAR A+B: >= 5 sigma and >= 70% of ceiling  ->  "
              f"{'PASS' if a else 'FAIL'}")
        ok &= a
    if 'C+D' in results:
        c = results['C+D'][1] >= 3
        print(f"  BAR C+D: >= 3 sigma  ->  {'PASS' if c else 'FAIL'}")
        ok &= c
    if 'G' in results:
        s = results['G'][1]
        verdict = ('carry information' if s >= 3 else
                   'do not carry information' if s < 2 else 'unclear')
        print(f"  G: {s:.1f} sigma -> the guesses with a held-out folio "
              f"{verdict}")
    print(f"  not reachable: guesses with no held-out cited folio "
          f"{sum(1 for h,v in p.items() if isinstance(v,dict) and v.get('tier')=='G') - len(ours['G'])}")
    return 0 if ok else 1


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main(sys.argv[1:]))
