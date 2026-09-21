"""TEST 10: replay the search on a null book. Does the keep-rule find
readings, or does it manufacture them?

Grok's objection: every sigma published so far shuffles glosses AFTER the
readings were chosen. That does not model the search that chose them. The
remedy is to write the search down as an algorithm, run it on the real book
and on books where the tether between sign and passage has been cut, and
compare how many "consistent readings" come out of each.

The human search was not logged. Grok's mechanical proxy stands in for it,
written here before the run:

  THE KEEP-RULE
  For every sign K&T did not read that stands on >= 3 distinct folios which
  cite a passage: the free pool of a folio is the content stems of its
  cited passage (Douay and King James) minus every stem K&T's own glosses
  carry. The sign's candidates are the stems present in EVERY one of its
  folios' pools. Keep the sign if that set is non-empty; its reading is the
  rarest surviving stem, rarity counted over both Bibles.

  HELD-OUT SCORE
  For each such sign and each of its folios f: derive from the OTHER
  folios only. If a reading results, it is a trial; a hit if that stem is in
  f's pool. Control: the derived stems permuted among the trials, 20 times.

NULL BOOKS, each seeded, the same rule run on each:
  within-folio    sign tokens permuted within each folio. Grok's null (a).
                  Vacuous for a folio-level rule -- a sign's folio set does
                  not change -- and reported to show that it is.
  global          sign tokens permuted across the whole book, unigram
                  frequencies preserved, folio sets randomised.
  rotated         folio i receives the passage of cited folio i+17. Grok's
                  null (b), offset pre-registered.

BARS, declared before the run, not moved (Grok's, verbatim):
  FAIL if either the global or the rotated null yields at least half as
  many kept readings as the real book, or if readings extracted from either
  null still beat their own shuffled glosses by >= 5 sigma held-out.
  Either result voids the published sigmas.

    python3 ktnullreplay.py [--shuf N]
"""
import random
import sys
from collections import defaultdict

import ktcross as K
import ktleft as L
import kttestlib as TL

SEED = 20260921
OFFSET = 17
MIN_FOLIOS = 3


def derive(pools, folios, freq):
    cand = None
    for f in folios:
        cand = set(pools[f]) if cand is None else cand & pools[f]
        if not cand:
            return None
    return min(cand, key=lambda s: (freq.get(s, 0), s)) if cand else None


def replay(sign_folios, pools, freq, nshuf, rng):
    kept = {}
    trials = []
    for s, fols in sorted(sign_folios.items()):
        fols = sorted(f for f in fols if f in pools)
        if len(fols) < MIN_FOLIOS:
            continue
        d = derive(pools, fols, freq)
        if d:
            kept[s] = d
        for f in fols:
            d2 = derive(pools, [x for x in fols if x != f], freq)
            if d2:
                trials.append((s, f, d2))
    tested = sum(1 for s, fols in sign_folios.items()
                 if len([f for f in fols if f in pools]) >= MIN_FOLIOS)
    hit = sum(1 for s, f, d in trials if d in pools[f])
    n = len(trials)
    obs = hit / n if n else 0
    nulls = []
    stems = [d for _, _, d in trials]
    for _ in range(nshuf):
        p = stems[:]
        rng.shuffle(p)
        nulls.append(sum(1 for (s, f, _), d in zip(trials, p) if d in pools[f]) / n if n else 0)
    m, sd, sig = TL.sigma(obs, nulls)
    return tested, len(kept), n, obs, m, sd, sig


def main(argv):
    nshuf = int(argv[argv.index('--shuf') + 1]) if '--shuf' in argv else 20
    gl, doc, seg, var, prop, inv = K.build()
    vv, vd = L.verses(), L.verses_dr()
    refs = TL.cited(doc)
    pools = TL.free_pools(doc, gl, vv, vd, refs)
    freq = TL.corpus_freq(vv, vd)
    fs = TL.folio_signs(doc)
    unread = lambda s: s not in gl and s not in var

    def folio_sets(fs_):
        out = defaultdict(set)
        for f, signs in fs_.items():
            for s in signs:
                if unread(s):
                    out[s].add(f)
        return out

    rng = random.Random(SEED)
    books = {}
    books['real'] = (folio_sets(fs), pools)
    # within-folio permutation
    r1 = random.Random(SEED + 1)
    fs_w = {}
    for f, signs in fs.items():
        p = signs[:]
        r1.shuffle(p)
        fs_w[f] = p
    books['within-folio'] = (folio_sets(fs_w), pools)
    # global permutation
    r2 = random.Random(SEED + 2)
    order = sorted(fs)
    alltok = [s for f in order for s in fs[f]]
    r2.shuffle(alltok)
    fs_g, k = {}, 0
    for f in order:
        fs_g[f] = alltok[k:k + len(fs[f])]
        k += len(fs[f])
    books['global'] = (folio_sets(fs_g), pools)
    # rotated passages
    cited = sorted(pools)
    rot = {cited[i]: pools[cited[(i + OFFSET) % len(cited)]] for i in range(len(cited))}
    books['rotated'] = (folio_sets(fs), rot)

    print("TEST 10: THE KEEP-RULE REPLAYED ON NULL BOOKS")
    print(f"  cited folios {len(pools)}; K&T-unread sign types {sum(1 for s in folio_sets(fs))}; "
          f"rule needs >= {MIN_FOLIOS} cited folios; offset {OFFSET}; seed {SEED}\n")
    print(f"  {'book':14s}{'signs':>7s}{'kept':>7s}{'trials':>8s}{'held-out':>10s}"
          f"{'shuffle':>9s}{'sd':>6s}{'sigma':>7s}")
    res = {}
    for name, (sf, pl) in books.items():
        tested, kept, n, obs, m, sd, sig = replay(sf, pl, freq, nshuf, rng)
        res[name] = (kept, sig)
        print(f"  {name:14s}{tested:7d}{kept:7d}{n:8d}{obs*100:9.1f}%{m*100:8.1f}%"
              f"{sd*100:6.2f}{sig:7.1f}")
    real = res['real'][0]
    print()
    ok = True
    for name in ('global', 'rotated'):
        kept, sig = res[name]
        a = kept < 0.5 * real
        b = sig < 5
        print(f"  {name:9s} kept {kept} vs real {real}: {'under' if a else 'AT OR OVER'} half"
              f"   held-out {sig:.1f} sigma: {'under' if b else 'AT OR OVER'} 5")
        ok &= a and b
    print(f"  BAR: both nulls under half the real count and under 5 sigma  ->  "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
