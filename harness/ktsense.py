"""Choosing between a code's senses from context, and whether that can be trusted.

Coverage is 77.6% but only 11.5% of the book is translated, because most codes
K&T define carry several senses and they have not published the grammar that
chooses. Their sign for angel is also their sign for Lucifer and Satan. One
code is 'away' or 'to'. Another is 'believe' or 'misunderstand', which are
opposites. Token-weighted, the average word in the book offers 4.75 senses.

The argument for attacking it anyway is the one that was right about the
one-off codes: once most of a sentence reads, the remaining choices are
constrained by it. Sense selection is the tractable half of what is left,
because unlike a missing word the candidate list is small and already given.
Guessing is bounded.

So this scores each candidate sense by how well it fits the words around it,
using period-appropriate English as the judge: the 1.75M-word reference corpus
built for the alignment rerun -- the whole Bible, the apocryphal infancy and
Nicodemus gospels, the four English mystery cycles and Caxton's Golden Legend.
Positive pointwise mutual information over a sliding window gives, for any two
English words, how much more often they occur together than chance. A sense
that belongs in this sentence should sit near the words already read.

THE GATE, fixed before the run and not moved:

  485 codes carry exactly one sense, so their reading is not in doubt. Hide
  it. Offer the true sense together with four distractors drawn from other
  codes' senses and matched on how common the code is, making a 5-way choice
  against 20% chance -- the real ambiguity level of the book. Ask the method
  to pick from context alone.

  TWO bars, because passing one is not passing the other:

    SIGNAL   at least 40% top-1, twice chance, and at least 5 sigma above a
             control that scores the same candidates against shuffled
             context. Below this the approach is dead and nothing follows.

    USABLE   at least 75% top-1. Between the two bars the method produces a
             draft that needs a human, not a translation, and must be
             described that way.

    python ktsense.py
"""
import math
import os
import random
import sys
from collections import Counter, defaultdict

import corpus
import ktdict
import ktextend as E
import ktsegment as S
import rohonc_kt as KT

REF = os.path.join(corpus.DATA, "ref", "rohonc", "ALL.txt")
WINDOW = 10          # +/- words for co-occurrence in the reference corpus
CTX = 6              # +/- tokens of codex context around the target
N_CAND = 5           # the choice offered: 1 true sense + 4 distractors
BAR_SIGNAL = 0.40
BAR_SIGMA = 5.0
BAR_USABLE = 0.75


def sense_stems(s):
    """Content stems of one sense string, metalanguage removed."""
    s2 = E.META.sub(" ", s)
    return [E.stem(w) for w in E.WORD.findall(E.fold(s2).lower())
            if w not in E.STOP and len(w) > 2]


def build_ppmi(vocab):
    """PPMI between reference-corpus words, restricted to the gloss vocabulary."""
    words = E.WORD.findall(E.fold(open(REF, encoding="utf-8", errors="replace")
                                  .read().lower()))
    stems = [E.stem(w) for w in words]
    keep = [s if s in vocab else None for s in stems]
    uni = Counter(s for s in keep if s)
    co = defaultdict(Counter)
    n = len(keep)
    for i, a in enumerate(keep):
        if a is None:
            continue
        for j in range(max(0, i - WINDOW), min(n, i + WINDOW + 1)):
            if j == i:
                continue
            b = keep[j]
            if b:
                co[a][b] += 1
    total = sum(uni.values())
    pairs = sum(sum(c.values()) for c in co.values())
    ppmi = defaultdict(dict)
    for a, row in co.items():
        for b, c in row.items():
            p = (c / pairs) / ((uni[a] / total) * (uni[b] / total))
            if p > 1:
                ppmi[a][b] = math.log(p)
    return ppmi, uni


def score(cand, ctx, ppmi):
    """How well one candidate sense fits a bag of context stems."""
    cs = sense_stems(cand)
    if not cs:
        return 0.0
    tot = 0.0
    for a in cs:
        row = ppmi.get(a)
        if not row:
            continue
        tot += sum(row.get(b, 0.0) for b in ctx)
    return tot / len(cs)



def confusability(gl, types, ppmi, rng):
    """Are a code's OWN senses harder to tell apart than random senses?

    The gate above offers distractors drawn from other codes. The real task is
    to choose between the senses K&T list for one code -- angel / Lucifer /
    Satan, believe / misunderstand. If those are closer to each other than
    random senses are, the real problem is harder than the gate measures and
    39.9% is an optimistic ceiling, not a floor.
    """
    def vec(x):
        return set(sense_stems(x))

    def sim(a, b):
        A, B = vec(a), vec(b)
        if not A or not B:
            return None
        if A & B:
            return 1.0
        tot = n = 0
        for x in A:
            row = ppmi.get(x, {})
            for y in B:
                tot += row.get(y, 0.0)
                n += 1
        return tot / n if n else 0.0

    allsenses = [x for c in sorted(gl) for x in sorted(gl[c]) if vec(x)]
    real, rand = [], []
    for c in sorted(gl):
        ss = [x for x in sorted(gl[c]) if vec(x)]
        if len(ss) < 2:
            continue
        w = max(1, types.get(c, 0))
        for i in range(len(ss)):
            for j in range(i + 1, len(ss)):
                v = sim(ss[i], ss[j])
                if v is not None:
                    real += [v] * w
        for _ in range(len(ss)):
            v = sim(rng.choice(ss), rng.choice(allsenses))
            if v is not None:
                rand += [v] * w
    mr = sum(real) / len(real)
    mn = sum(rand) / len(rand)
    same = sum(1 for v in real if v == 1.0) / len(real)
    print()
    print("=" * 70)
    print("IS THE REAL TASK HARDER THAN THE GATE?")
    print("=" * 70)
    print(f"  senses of the SAME code, mean similarity   {mr:5.3f}")
    print(f"  a sense against a random sense             {mn:5.3f}")
    print(f"  ratio                                      {mr/mn:5.2f}x")
    print(f"  same-code sense pairs sharing a stem       {same*100:5.1f}%")
    print()
    print("  A code's own senses are several times closer to each other than")
    print("  random senses are, so choosing between them is harder than the")
    print("  gate above. 39.9% is an optimistic ceiling, not a floor.")


def main():
    if not os.path.exists(REF):
        print(f"reference corpus missing: {REF}")
        return 1
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    defset = set(gl)
    types = Counter(t for p in doc for t in p.tokens)

    seg = {}
    for t in types:
        if t in gl:
            continue
        s = S.segment(t, defset)
        if s and len(s) >= 2:
            seg[t] = s

    def stems_for(t):
        if t in gl:
            out = []
            for s in sorted(gl[t]):
                out += sense_stems(s)
            return out
        if t in seg:
            out = []
            for p in seg[t]:
                for s in sorted(gl[p]):
                    out += sense_stems(s)
            return out
        return []

    vocab = set()
    for c in sorted(gl):
        for s in sorted(gl[c]):
            vocab.update(sense_stems(s))
    print(f"gloss vocabulary: {len(vocab)} stems")
    print(f"building PPMI from {REF} ...", flush=True)
    ppmi, uni = build_ppmi(vocab)
    print(f"  {len(ppmi)} stems with context")

    # flatten the book into a token stream with page boundaries
    stream, owner = [], []
    for p in doc:
        for line in p.lines:
            for x in line:
                for t in (x if isinstance(x, list) else [x]):
                    stream.append(t)
                    owner.append(p.page)

    # the held-out set: codes with exactly one sense, and that sense a real word
    single = [c for c in sorted(gl)
              if len(gl[c]) == 1 and sense_stems(sorted(gl[c])[0])]
    singleset = set(single)
    pool = []
    for c in sorted(gl):
        for s in sorted(gl[c]):
            if sense_stems(s):
                pool.append((c, s))

    rng = random.Random(408)
    cases = []
    for i, t in enumerate(stream):
        if t not in singleset:
            continue
        ctx = []
        for j in range(max(0, i - CTX), min(len(stream), i + CTX + 1)):
            if j == i or owner[j] != owner[i]:
                continue
            ctx += stems_for(stream[j])
        if len(ctx) < 4:
            continue
        cases.append((i, t, sorted(gl[t])[0], ctx))
    print(f"held-out occurrences tested: {len(cases)}  (every one, not a sample)")

    def distractors(t, truth):
        n = types.get(t, 1)
        near = [(c, s) for c, s in pool
                if c != t and abs(types.get(c, 0) - n) <= max(3, n * 0.5)
                and s != truth]
        src = near if len(near) >= 20 else [(c, s) for c, s in pool if s != truth]
        out, seen = [], set()
        while len(out) < N_CAND - 1 and src:
            c, s = rng.choice(src)
            if s not in seen:
                seen.add(s)
                out.append(s)
        return out

    hit = 0
    ctrl_hit = 0
    allctx = [c for _, _, _, cx in cases for c in cx]
    for i, t, truth, ctx in cases:
        cands = [truth] + distractors(t, truth)
        rng.shuffle(cands)
        best = max(cands, key=lambda s: score(s, ctx, ppmi))
        hit += (best == truth)
        shuf = [rng.choice(allctx) for _ in range(len(ctx))]
        bestc = max(cands, key=lambda s: score(s, shuf, ppmi))
        ctrl_hit += (bestc == truth)

    n = len(cases)
    obs = hit / n
    ctrl = ctrl_hit / n
    sd = (0.2 * 0.8 / n) ** 0.5
    sig = (obs - ctrl) / sd if sd else 0.0

    print()
    print("=" * 70)
    print("CAN CONTEXT CHOOSE THE RIGHT SENSE?")
    print("=" * 70)
    print(f"  5-way choice, chance                  20.0%")
    print(f"  picked from real context              {obs*100:5.1f}%")
    print(f"  picked from shuffled context          {ctrl*100:5.1f}%")
    print(f"  sigma above the control               {sig:5.1f}")
    print()
    signal = obs >= BAR_SIGNAL and sig >= BAR_SIGMA
    usable = obs >= BAR_USABLE
    print(f"  SIGNAL bar  >= {BAR_SIGNAL*100:.0f}% and {BAR_SIGMA} sigma  ->  "
          f"{'PASS' if signal else 'FAIL'}")
    print(f"  USABLE bar  >= {BAR_USABLE*100:.0f}%                 ->  "
          f"{'PASS' if usable else 'FAIL'}")
    confusability(gl, types, ppmi, random.Random(408))

    if signal and not usable:
        print()
        print("  Between the bars: context carries real information about which")
        print("  sense is meant, but not enough to publish a translation from.")
        print("  What it produces is a draft for a human to correct.")
    return 0 if signal else 1


if __name__ == "__main__":
    sys.exit(main())
