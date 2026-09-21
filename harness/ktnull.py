"""THE NULL CONTROL: does this pipeline produce readings from noise?

Every gate in this file is declared here, with its bar, BEFORE the run. A
near miss is a miss. If any of these fails, the corresponding part of the
method manufactures readings and the percentage it produced is worthless.

The three mechanisms that produced the 891 readings are tested separately,
because they could fail separately.

--------------------------------------------------------------------------
GATE 1. Do structurally related signs share a meaning?

  ktinside.py, ktcover.py and ktnear.py all rest on one assumption: that when
  an unread sign sits inside a sign K&T read, contains one whole, or is one
  glyph from one, it MEANS something close to it. That assumption has never
  been measured. Measure it on their own dictionary, where the answer is
  known.

    For every sign K&T read that has a structural neighbour in their
    dictionary (inside / holds / one glyph away), hide its gloss, predict
    the neighbour's gloss, and score a hit if any content stem of the
    prediction is a content stem of the truth.

  CONTROL: the same structure, with the glosses PERMUTED among their signs.
  The hex strings do not move, so every structural relation is identical;
  only which word sits on which sign changes. 20 permutations.

  BAR: the observed hit rate must beat the control mean by 5 sigma.
       Anything less and the structural tools are matching noise.

--------------------------------------------------------------------------
GATE 2. Are the cited passages the right passages?

  A third of this project's readings were got by matching a line against the
  chapter and verse the folio cites. If those citations are wrong, the pools
  are noise and so is everything drawn from them.

    For every folio that cites a chapter and verse, take every token on it
    whose sign K&T read, and ask whether a content stem of their gloss is
    present in that folio's OWN cited verses.

  CONTROL: score the same tokens against a DIFFERENT cited folio's verses,
  drawn at random. 20 shuffles. This holds the codex, the dictionary and the
  corpus fixed and destroys only the folio-to-passage assignment.

  BAR: observed must beat the control mean by 5 sigma.

--------------------------------------------------------------------------
GATE 3. Does the rendering read like language, or like a word list?

  The strongest thing said about this work is that whole folios come out
  coherent. That is an impression. Turn it into a number.

    Take every adjacent pair of content words in the rendering of the whole
    book. Ask how often that pair, as stems, occurs within four words of
    each other somewhere in the Douay-Rheims or the King James.

  CONTROL: permute the glosses among the signs and render again. Two forms,
  both declared:
    (a) a free permutation;
    (b) a STRATIFIED permutation, in which a sign may only take the gloss of
        another sign in the same frequency decile. This is the harder
        control, because it stops a common sign being handed a rare word,
        and it is the one the bar is set against.

  BAR: observed must beat the STRATIFIED control mean by 5 sigma.

--------------------------------------------------------------------------
  python ktnull.py            all three gates
  python ktnull.py --gate 2   one of them
  python ktnull.py --shuf N   how many permutations (default 20)
"""
import random
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktnear as N

SEED = 20260921
BAR = 5.0


def stems(text):
    out = set()
    g = re.sub(r"[<\[(][^>\])]*[>\])]", " ", text).translate(K.ACCENT)
    for w in re.findall(r"[a-zA-Z]+", g):
        if w.lower() in K.STOP or len(w) < 3:
            continue
        out.add(K.stem(w))
    return out


def beat(obs, ctrl):
    """How many controls the observation beats. Descriptive, not a bar.

    Added after the first run, and it changes no gate: sigma is a poor
    statistic when the control distribution is heavy-tailed, which it is
    here, because a permutation's score is dominated by where the handful
    of very common signs land. A gate that failed on sigma still failed.
    """
    return sum(1 for c in ctrl if obs > c), len(ctrl)


def sigma(obs, ctrl):
    m = sum(ctrl) / len(ctrl)
    if len(ctrl) < 2:
        return 0.0, m
    v = sum((c - m) ** 2 for c in ctrl) / (len(ctrl) - 1)
    sd = v ** 0.5
    return ((obs - m) / sd if sd else float("inf")), m


def gate1(gl, nshuf):
    hexes = {K.hx(c): "; ".join(s) for c, s in gl.items()}
    hs = list(hexes)
    gset = {h: N.glyphs(h) for h in hs}
    # structural neighbour: inside / holds / one glyph away
    nb = {}
    by_len = defaultdict(list)
    for h in hs:
        by_len[len(gset[h])].append(h)
    for h in hs:
        best = None
        for hb in hs:
            if hb == h:
                continue
            if (len(h) >= 6 and h in hb) or (len(hb) >= 6 and hb in h):
                best = hb
                break
        if best is None and len(gset[h]) >= 3:
            for L2 in (len(gset[h]) - 1, len(gset[h]), len(gset[h]) + 1):
                for hb in by_len.get(L2, ()):
                    if hb != h and N.one_away(gset[h], gset[hb]):
                        best = hb
                        break
                if best:
                    break
        if best:
            nb[h] = best

    def rate(table):
        hit = tot = 0
        for h, hb in nb.items():
            t, p = stems(table[h]), stems(table[hb])
            if not t or not p:
                continue
            tot += 1
            hit += bool(t & p)
        return hit / tot, tot

    obs, tot = rate(hexes)
    rng = random.Random(SEED)
    ctrl = []
    vals = list(hexes.values())
    for _ in range(nshuf):
        sh = vals[:]
        rng.shuffle(sh)
        ctrl.append(rate(dict(zip(hs, sh)))[0])
    s, m = sigma(obs, ctrl)
    b, n = beat(obs, ctrl)
    print("GATE 1  do structurally related signs share a meaning?")
    print(f"  pairs tested (sign, its structural neighbour)   {tot}")
    print(f"  observed: neighbour's gloss shares a stem       {obs*100:.1f}%")
    print(f"  control (glosses permuted, structure kept)      {m*100:.1f}%")
    print(f"  observed beats {b} of {n} controls")
    print(f"  {s:.1f} sigma against a bar of {BAR}   -> {'PASS' if s >= BAR else 'FAIL'}")
    return s >= BAR


def gate2(gl, doc, nshuf):
    vv, vd = L.verses(), L.verses_dr()
    pools, toks = {}, {}
    for p in doc:
        r = L.refs_in(K.note_for(p.page))
        if not r:
            continue
        idx = {}
        both, dro, kjo, syn = L.pools_for(vv, vd, r, idx, 0)
        pool = set(both) | set(dro) | set(kjo)
        if not pool:
            continue
        st = []
        for t in p.tokens:
            b = A.strip(t)[0]
            if b in gl:
                s = stems("; ".join(gl[b]))
                if s:
                    st.append(s)
        if st:
            pools[p.page], toks[p.page] = pool, st
    pages = sorted(pools)

    def rate(assign):
        hit = tot = 0
        for pg in pages:
            pool = pools[assign[pg]]
            for s in toks[pg]:
                tot += 1
                hit += bool(s & pool)
        return hit / tot, tot

    obs, tot = rate({p: p for p in pages})
    rng = random.Random(SEED)
    ctrl = []
    for _ in range(nshuf):
        sh = pages[:]
        rng.shuffle(sh)
        ctrl.append(rate(dict(zip(pages, sh)))[0])
    s, m = sigma(obs, ctrl)
    b, n = beat(obs, ctrl)
    print("GATE 2  are the cited passages the right passages?")
    print(f"  folios citing a chapter and verse               {len(pages)}")
    print(f"  tokens scored                                   {tot}")
    print(f"  observed: gloss present in its OWN passage      {obs*100:.1f}%")
    print(f"  control (folio-to-passage shuffled)             {m*100:.1f}%")
    print(f"  observed beats {b} of {n} controls")
    print(f"  {s:.1f} sigma against a bar of {BAR}   -> {'PASS' if s >= BAR else 'FAIL'}")
    return s >= BAR


def gate3(gl, doc, prop, nshuf):
    # the vocabulary the rendering can actually produce
    table = {}
    for c, senses in gl.items():
        v = sorted(stems("; ".join(senses)))
        if v:
            table[c] = v
    for c, (g, t) in prop.items():
        v = sorted(stems(g.replace("_", " ")))
        if v and c not in table:
            table[c] = v
    vocab = {x for v in table.values() for x in v}

    # corpus adjacency, restricted to that vocabulary so the set stays small
    near = set()
    for path in (L.KJV, L.DR):
        text = open(path, encoding="utf-8", errors="ignore").read().lower()
        for line in text.split("\n"):
            ws = [K.stem(w) for w in re.findall(r"[a-z]+", line)]
            ws = [w for w in ws if w in vocab]
            for i, a in enumerate(ws):
                for b in ws[i + 1:i + 5]:
                    near.add((a, b) if a < b else (b, a))

    # sequences of SIGNS, so a permuted table really changes the rendering
    seqs = []
    for p in doc:
        for ln in p.lines:
            seq = [A.strip(t)[0] for run in ln for t in run
                   if A.strip(t)[0] in table]
            if len(seq) >= 2:
                seqs.append(seq)

    def rate(tab):
        hit = tot = 0
        for seq in seqs:
            for i in range(len(seq) - 1):
                tot += 1
                a, b = tab[seq[i]], tab[seq[i + 1]]
                for x in a:
                    if any(((x, y) if x < y else (y, x)) in near for y in b):
                        hit += 1
                        break
        return hit / tot, tot

    keys = list(table)
    freq = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    obs, tot = rate(table)

    free_c, strat_c = [], []
    order = sorted(keys, key=lambda k: (-freq[k], K.hx(k)))
    d = max(1, len(order) // 10)
    for j in range(nshuf):
        rng2 = random.Random(SEED + 1000 + j)
        vals = [table[k] for k in keys]
        rng2.shuffle(vals)
        free_c.append(rate(dict(zip(keys, vals)))[0])
        out = {}
        for i in range(0, len(order), d):
            blk = order[i:i + d]
            v = [table[k] for k in blk]
            rng2.shuffle(v)
            out.update(dict(zip(blk, v)))
        strat_c.append(rate(out)[0])
    s, m = sigma(obs, strat_c)
    sf, mf = sigma(obs, free_c)
    print("GATE 3  does the rendering read like language?")
    print(f"  adjacent content-word pairs in the book         {tot}")
    print(f"  corpus pairs indexed (within four words)        {len(near)}")
    print("  observed: the pair stands within four words of")
    print(f"    each other somewhere in Douay or King James   {obs*100:.1f}%")
    print(f"  control, free permutation of the glosses        {mf*100:.1f}%  ({sf:.1f} sigma)")
    bf, nf = beat(obs, free_c)
    bs, ns = beat(obs, strat_c)
    print(f"  control, STRATIFIED by sign frequency           {m*100:.1f}%  ({s:.1f} sigma)")
    print(f"  observed beats {bf} of {nf} free controls, {bs} of {ns} stratified")
    print(f"  {s:.1f} sigma against a bar of {BAR}   -> {'PASS' if s >= BAR else 'FAIL'}")
    return s >= BAR


def main(argv):
    nshuf = 20
    if "--shuf" in argv:
        nshuf = int(argv[argv.index("--shuf") + 1])
    want = argv[argv.index("--gate") + 1] if "--gate" in argv else "123"
    gl, doc, seg, var, prop, inv = K.build()
    print(f"NULL CONTROL, bars declared in the docstring before the run. "
          f"{nshuf} permutations, seed {SEED}.\n")
    ok = []
    if "1" in want:
        ok.append(gate1(gl, nshuf)); print()
    if "2" in want:
        ok.append(gate2(gl, doc, nshuf)); print()
    if "3" in want:
        ok.append(gate3(gl, doc, prop, nshuf)); print()
    print("ALL DECLARED GATES PASS" if all(ok) else "A GATE FAILED -- see above")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
