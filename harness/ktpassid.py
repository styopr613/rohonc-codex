"""TEST 11: can the folio-to-passage map be recovered from K&T's words alone?

Grok's objection to Tests 1, 6 and 9: the passage each folio is said to
retell was identified while translating with the full reading, ours
included. If the map cannot be recovered WITHOUT our readings, those three
tests have no target independent of the readings they test.

So: render every cited folio with Király and Tokai's dictionary only --
their 841 glosses and their listed variant spellings, nothing of ours, no
segmentation -- take the bag of content stems that gives, and score it
against EVERY chapter of the Douay Bible (1334 of them) by tf-idf cosine.
Where does the chapter the note names come out in the ranking?

  rank      best rank among the cited chapters, 1 = top of 1334
  top-1     the cited chapter is the best-scoring chapter of the whole Bible
  top 5%    rank <= 67

DECOYS, per folio, both fixed before scoring:
  frequency-matched   the chapter, not cited, whose profile over the 50
                      commonest stems of the Bible is closest (cosine) to
                      the cited chapter's. Genre and length twin.
  other genre         a chunk of the Golden Legend of the cited chapter's
                      length in stems, drawn once with a fixed seed.
Sign test: the cited chapter must outscore the decoy on more folios than a
fair coin would give, binomial p < 0.01.

SHUFFLE: K&T's glosses permuted among their signs once, seed fixed, the
same ranking run again. What the map looks like from the wrong words.

BARS, declared before the run, not moved (Grok's, verbatim):
  FAIL if the median rank of the cited chapter is worse than the top 5% of
  candidates (rank > 67 of 1334), or if the cited chapter does not beat the
  frequency-matched decoy at p < 0.01.
  Top-1 accuracy is reported beside the rank; a sigma with single-digit
  accuracy would be a fail regardless.

    python3 ktpassid.py
"""
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R
import kttestlib as TL

SEED = 20260921
LEGEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data",
                      "ref", "rohonc", "golden_legend.txt")


def binom_p(k, n):
    """one-sided P(X >= k) for a fair coin"""
    return sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n


def cosine(a, b):
    num = sum(v * b.get(k, 0) for k, v in a.items())
    da = math.sqrt(sum(v * v for v in a.values()))
    db = math.sqrt(sum(v * v for v in b.values()))
    return num / (da * db) if da and db else 0.0


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    refs = TL.cited(doc)
    vd = L.verses_dr()
    # ---- candidates: every Douay chapter as a stem Counter
    chap = defaultdict(Counter)
    for (b, c, v), txt in vd.items():
        chap[(b, c)].update(R.stems(txt))
    keys = sorted(chap)
    N = len(keys)
    df = Counter()
    for k in keys:
        df.update(set(chap[k]))
    idf = {s: math.log(N / d) for s, d in df.items()}
    cvec = {k: {s: n * idf[s] for s, n in chap[k].items()} for k in keys}
    top50 = [s for s, _ in sum((chap[k] for k in keys), Counter()).most_common(50)]

    # ---- K&T-only stem bag per folio
    def bag(gloss_of):
        out = {}
        for pg in doc:
            if pg.page not in refs:
                continue
            c = Counter()
            for t in pg.tokens:
                s = A.strip(t)[0]
                s = var.get(s, s)
                if s in gloss_of:
                    c.update(gloss_of[s])
            out[pg.page] = c
        return out

    kt_st = {s: set().union(*(R.stems(x) for x in g)) for s, g in gl.items()}
    kt_st = {s: st for s, st in kt_st.items() if st}

    # ---- decoys, fixed before any score is computed
    rng = random.Random(SEED)
    prof = {k: {s: chap[k][s] for s in top50} for k in keys}
    import ktorder as O
    leg = O.ordered_stems(open(LEGEND, encoding="utf-8", errors="ignore").read())
    decoy_f, decoy_g = {}, {}
    for pg, r in refs.items():
        cited_ch = sorted({(b, c) for b, c, _, _ in r if (b, c) in chap})
        if not cited_ch:
            continue
        main_ch = cited_ch[0]
        best = max((k for k in keys if k not in cited_ch),
                   key=lambda k: (cosine(prof[main_ch], prof[k]), k))
        decoy_f[pg] = best
        n = sum(chap[main_ch].values())
        start = rng.randrange(0, max(1, len(leg) - n))
        c = Counter(leg[start:start + n])
        decoy_g[pg] = {s: v * idf.get(s, math.log(N)) for s, v in c.items()}

    def run(gloss_of, label):
        bags = bag(gloss_of)
        ranks, top1, beat_f, beat_g, n, book1 = [], 0, 0, 0, 0, 0
        for pg in sorted(decoy_f):
            b = bags.get(pg)
            if not b:
                continue
            fv = {s: c * idf.get(s, 0) for s, c in b.items() if s in idf}
            if not fv:
                continue
            cited_ch = {(bk, c) for bk, c, _, _ in refs[pg] if (bk, c) in chap}
            scores = {k: cosine(fv, cvec[k]) for k in keys}
            order = sorted(keys, key=lambda k: -scores[k])
            rk = min(order.index(k) for k in cited_ch) + 1
            ranks.append(rk)
            top1 += rk == 1
            book1 += order[0][0] in {bk for bk, _ in cited_ch}
            best_cited = max(scores[k] for k in cited_ch)
            beat_f += best_cited > scores[decoy_f[pg]]
            beat_g += best_cited > cosine(fv, decoy_g[pg])
            n += 1
        ranks.sort()
        med = ranks[len(ranks) // 2]
        pf, pgg = binom_p(beat_f, n), binom_p(beat_g, n)
        print(f"  {label}")
        print(f"    folios scored                     {n}")
        print(f"    cited chapter is top-1            {top1:4d}   {top1/n*100:5.1f}%")
        print(f"    top-1 chapter is in a cited book  {book1:4d}   {book1/n*100:5.1f}%   (reported, no bar)")
        print(f"    cited chapter in top 5% (<=67)    {sum(1 for r in ranks if r <= 67):4d}   "
              f"{sum(1 for r in ranks if r <= 67)/n*100:5.1f}%")
        print(f"    median rank of cited chapter      {med:4d}   of {N}")
        print(f"    beats frequency-matched decoy     {beat_f:4d}/{n}   p = {pf:.2e}")
        print(f"    beats other-genre decoy           {beat_g:4d}/{n}   p = {pgg:.2e}")
        return med, top1 / n, pf

    print("TEST 11: PASSAGE IDENTIFICATION FROM K&T'S WORDS ALONE")
    print(f"  candidates: {N} Douay chapters; folios with a cited chapter {len(decoy_f)}")
    print(f"  K&T signs with a content stem {len(kt_st)}; our readings not consulted\n")
    med, t1, pf = run(kt_st, "K&T's glosses, as published")
    print()
    signs = sorted(kt_st)
    perm = signs[:]
    random.Random(SEED + 1).shuffle(perm)
    shuf = {a: kt_st[b] for a, b in zip(signs, perm)}
    run(shuf, "K&T's glosses shuffled among their signs (seed fixed)")
    print()
    ok = med <= 67 and pf < 0.01
    print(f"  BAR: median rank <= 67 of {N} and p < 0.01 against the frequency-matched "
          f"decoy  ->  {'PASS' if ok else 'FAIL'}")
    print(f"  absolute top-1 accuracy {t1*100:.1f}%")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
