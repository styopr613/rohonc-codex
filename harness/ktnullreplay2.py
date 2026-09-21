"""TEST 10b: the keep-rule replayed on null books, at chapter scale.

Test 10 ran Grok's mechanical keep-rule at the scale the notes cite, which
is mostly a single verse (median free pool: 7 stems). At that scale the
rule kept 10 readings of 316 candidates on the real book and 8 on each null
book. Ten against eight cannot tell a search from a decipherment either
way; that instrument has no power on the count criterion, and Test 10 is
recorded as the FAIL its bar makes it. This is the same rule with a pool
wide enough to give the count a chance to move, declared before it runs:

  THE KEEP-RULE, CHAPTER SCALE
  For every sign K&T did not read that stands on folios citing >= 3
  DISTINCT chapters: the pool of a chapter is its content stems (Douay and
  King James, whole chapter) minus every stem K&T's own glosses carry. The
  sign's candidates are the stems present in every one of its chapters'
  pools. Keep if non-empty; reading = the rarest survivor, rarity over both
  Bibles. Distinct chapters, so that a sign standing on ten folios of Mark
  16 counts Mark 16 once.

  HELD-OUT SCORE
  For each such sign and each of its chapters c: derive from the other
  chapters. If a reading results, it is a trial; a hit if the stem is in
  c's pool. Control: derived stems permuted among the trials, 20 times.

NULL BOOKS, seeded:
  global     sign tokens permuted across the whole book, unigram
             frequencies preserved.
  rotated    cited folio i receives the chapters of cited folio i+17.

BARS, the same as Test 10, declared before the run, not moved:
  FAIL if either null yields at least half as many kept readings as the
  real book, or if readings from either null beat their own shuffled
  glosses by >= 5 sigma held-out.

    python3 ktnullreplay2.py [--shuf N]
"""
import random
import sys
from collections import Counter, defaultdict

import ktcross as K
import ktleft as L
import ktrederive as R
import kttestlib as TL

SEED = 20260921
OFFSET = 17
MIN_CH = 3


def derive(pools, chs, freq):
    cand = None
    for c in chs:
        cand = set(pools[c]) if cand is None else cand & pools[c]
        if not cand:
            return None
    return min(cand, key=lambda s: (freq.get(s, 0), s))


def replay(sign_chs, pools, freq, nshuf, rng):
    kept, trials, tested = {}, [], 0
    for s, chs in sorted(sign_chs.items()):
        chs = sorted(c for c in chs if c in pools)
        if len(chs) < MIN_CH:
            continue
        tested += 1
        d = derive(pools, chs, freq)
        if d:
            kept[s] = d
        for c in chs:
            d2 = derive(pools, [x for x in chs if x != c], freq)
            if d2:
                trials.append((s, c, d2))
    n = len(trials)
    hit = sum(1 for s, c, d in trials if d in pools[c])
    obs = hit / n if n else 0
    stems = [d for _, _, d in trials]
    nulls = []
    for _ in range(nshuf):
        p = stems[:]
        rng.shuffle(p)
        nulls.append(sum(1 for (s, c, _), d in zip(trials, p) if d in pools[c]) / n if n else 0)
    m, sd, sig = TL.sigma(obs, nulls)
    return tested, kept, n, obs, m, sd, sig


def main(argv):
    nshuf = int(argv[argv.index('--shuf') + 1]) if '--shuf' in argv else 20
    gl, doc, seg, var, prop, inv = K.build()
    vv, vd = L.verses(), L.verses_dr()
    refs = TL.cited(doc)
    taken = TL.kt_taken(gl)
    freq = TL.corpus_freq(vv, vd)
    chap = defaultdict(set)
    for t in (vv, vd):
        for (b, c, v), txt in t.items():
            chap[(b, c)] |= TL.content(txt)
    pools = {k: s - taken for k, s in chap.items()}
    folio_ch = {f: sorted({(b, c) for b, c, _, _ in r if (b, c) in pools}) for f, r in refs.items()}
    folio_ch = {f: v for f, v in folio_ch.items() if v}
    fs = TL.folio_signs(doc)
    unread = lambda s: s not in gl and s not in var

    def sign_chapters(fs_, fch):
        out = defaultdict(set)
        for f, signs in fs_.items():
            if f not in fch:
                continue
            for s in signs:
                if unread(s):
                    out[s].update(fch[f])
        return out

    books = {}
    books['real'] = sign_chapters(fs, folio_ch)
    r2 = random.Random(SEED + 2)
    order = sorted(fs)
    alltok = [s for f in order for s in fs[f]]
    r2.shuffle(alltok)
    fs_g, k = {}, 0
    for f in order:
        fs_g[f] = alltok[k:k + len(fs[f])]
        k += len(fs[f])
    books['global'] = sign_chapters(fs_g, folio_ch)
    cited = sorted(folio_ch)
    rot = {cited[i]: folio_ch[cited[(i + OFFSET) % len(cited)]] for i in range(len(cited))}
    books['rotated'] = sign_chapters(fs, rot)

    print("TEST 10b: THE KEEP-RULE REPLAYED ON NULL BOOKS, CHAPTER SCALE")
    print(f"  cited folios {len(folio_ch)}; distinct chapters {len({c for v in folio_ch.values() for c in v})}; "
          f"rule needs >= {MIN_CH} distinct chapters; median chapter pool "
          f"{sorted(len(pools[c]) for v in folio_ch.values() for c in v)[len([c for v in folio_ch.values() for c in v])//2]} free stems; "
          f"offset {OFFSET}; seed {SEED}\n")
    print(f"  {'book':10s}{'signs':>7s}{'kept':>7s}{'trials':>8s}{'held-out':>10s}"
          f"{'shuffle':>9s}{'sd':>6s}{'sigma':>7s}")
    rng = random.Random(SEED)
    res = {}
    for name, sc in books.items():
        tested, kept, n, obs, m, sd, sig = replay(sc, pools, freq, nshuf, rng)
        res[name] = (len(kept), sig, kept)
        print(f"  {name:10s}{tested:7d}{len(kept):7d}{n:8d}{obs*100:9.1f}%{m*100:8.1f}%"
              f"{sd*100:6.2f}{sig:7.1f}")
    real = res['real'][0]
    print()
    # what the rule kept on the real book, against what this project read
    import json
    p = json.load(open('proposals.json', encoding='utf-8'))
    un = lambda h: "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))
    ours = {un(h): (v['tier'], v['gloss']) for h, v in p.items()
            if isinstance(v, dict) and v.get('tier') in 'ABCD'}
    agree = tot = 0
    for s, d in sorted(res['real'][2].items()):
        if s in ours:
            tot += 1
            agree += d in R.stems(ours[s][1].replace('_', ' '))
    print(f"  real-book readings the rule kept that this project also read: {tot} of {real}; "
          f"same stem {agree}  (reported, no bar)")
    print()
    ok = True
    for name in ('global', 'rotated'):
        kept, sig, _ = res[name]
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
