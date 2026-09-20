"""Can the grammar be abstracted from the text, rather than waiting for K&T?

One rule already was. ktname.py and ktsegment.py recovered the construction
<modifier><name-sign> from the codex itself, confirmed it at 12.4 and 9.8
sigma against matched controls without using K&T's glosses to find it, and
that single rule took coverage from 58.4% to 77.6%. So grammar abstraction is
not speculative here. It has happened once and it paid.

The question is whether the rule that matters next is there to be found.
Coverage is no longer the bottleneck: 66.0% of the book is words that carry
several senses with no published rule for choosing. ktsense.py showed context
picks the right sense at 39.9% against 20% chance -- real signal at 22.8
sigma, but below its 40% bar, and the real task is harder than that gate
because a code's own senses are 2.5x closer to each other than random senses.

A better chooser is only worth building if the senses are contextually
determined AT ALL. If K&T list several senses because the code genuinely
means different things in different places, its occurrences should split into
distinguishable context groups. If they list several because they were unsure,
or because the codex is vague, no method will ever separate them and the 66%
needs their grammar paper, not ours.

That is a question about the text, and it is answerable now.

THE GATE, fixed before the run and not moved:

  For every code with at least 20 occurrences, build a context vector per
  occurrence from the readable words around it, split the occurrences in two
  by k-means, and measure how much of the variance the split explains. A code
  whose senses are contextually conditioned should split better than one with
  a single sense.

  The control is single-sense codes matched on frequency, which holds the
  book's topical structure and the sample size fixed and leaves only the
  polysemy.

  BAR: multi-sense codes must explain at least 1.15x the variance of matched
  single-sense codes, at 5 sigma or better. Below either, sense choice is not
  recoverable from context and this document says so.

    python ktgrammar.py
"""
import random
import sys
from collections import Counter, defaultdict

import ktdict
import ktsegment as S
import ktsense as Q
import rohonc_kt as KT

MIN_OCC = 20
CTX = 4
BAR_RATIO = 1.15
BAR_SIGMA = 5.0


def context_vectors(code, stream, owner, stems_for):
    out = []
    for i, t in enumerate(stream):
        if t != code:
            continue
        bag = Counter()
        for j in range(max(0, i - CTX), min(len(stream), i + CTX + 1)):
            if j == i or owner[j] != owner[i]:
                continue
            bag.update(stems_for(stream[j]))
        if bag:
            out.append(bag)
    return out


def variance_explained(vecs, rng, iters=12):
    """Share of total distance-from-centre explained by the best 2-way split."""
    if len(vecs) < 6:
        return None
    keys = sorted({k for v in vecs for k in v})
    if len(keys) < 3:
        return None
    mat = []
    for v in vecs:
        n = (sum(x * x for x in v.values())) ** 0.5 or 1.0
        mat.append([v.get(k, 0) / n for k in keys])
    d = len(keys)

    def centre(rows):
        m = len(rows)
        return [sum(r[i] for r in rows) / m for i in range(d)]

    def sqd(a, b):
        return sum((x - y) ** 2 for x, y in zip(a, b))

    g = centre(mat)
    total = sum(sqd(r, g) for r in mat)
    if total <= 0:
        return None
    best = 0.0
    for _ in range(iters):
        a, b = rng.sample(range(len(mat)), 2)
        ca, cb = mat[a][:], mat[b][:]
        for _ in range(12):
            A = [r for r in mat if sqd(r, ca) <= sqd(r, cb)]
            B = [r for r in mat if sqd(r, ca) > sqd(r, cb)]
            if not A or not B:
                break
            ca, cb = centre(A), centre(B)
        if not A or not B:
            continue
        within = sum(sqd(r, ca) for r in A) + sum(sqd(r, cb) for r in B)
        best = max(best, (total - within) / total)
    return best



def sense_kinds(gl, types):
    """WHY the gate failed: most multi-sense entries are not ambiguous at all.

    Looking at the codes that split best -- Creator/create/creation/creature,
    book/scripture/write, debt/debtor/indebted, place/put, fire/flame,
    Word/gospel -- almost none of them are a word with several meanings. They
    are ONE meaning rendered in whatever English part of speech the sentence
    needed. There is nothing for context to separate, which is exactly why a
    context model cannot separate it.

    That matters for the headline number. A word whose senses are all one
    concept IS understood; what is unknown is only which English form to write.
    Counting it as untranslated overstates the problem.

    The split below uses shared word stems, which needs no threshold and so
    invents no rule. It is a LOWER bound on the one-concept group: fire/flame
    and Word/gospel are one concept and share no stem, so they are counted on
    the wrong side here.
    """
    import ktextend as E

    def stems(x):
        return {E.stem(w) for w in E.WORD.findall(E.fold(E.META.sub(" ", x)).lower())
                if w not in E.STOP and len(w) > 2}

    one = distinct = mixed = 0
    one_t = distinct_t = mixed_t = 0
    ex_one, ex_dist = [], []
    for c in sorted(gl):
        ss = [x for x in sorted(gl[c]) if stems(x)]
        if len(ss) < 2:
            continue
        n = types.get(c, 0)
        pairs = [(i, j) for i in range(len(ss)) for j in range(i + 1, len(ss))]
        share = [bool(stems(ss[i]) & stems(ss[j])) for i, j in pairs]
        if all(share):
            one += 1
            one_t += n
            if n >= 20 and len(ex_one) < 6:
                ex_one.append((n, ", ".join(ss)[:56]))
        elif not any(share):
            distinct += 1
            distinct_t += n
            if n >= 20 and len(ex_dist) < 6:
                ex_dist.append((n, ", ".join(ss)[:56]))
        else:
            mixed += 1
            mixed_t += n
    tot = one_t + distinct_t + mixed_t
    print()
    print("=" * 70)
    print("WHY: MOST MULTI-SENSE ENTRIES ARE NOT AMBIGUOUS")
    print("=" * 70)
    print(f"  every sense shares a stem  {one:4d} codes  {one_t:6d} tokens  "
          f"{one_t/tot*100:5.1f}%")
    print(f"  some do                    {mixed:4d} codes  {mixed_t:6d} tokens  "
          f"{mixed_t/tot*100:5.1f}%")
    print(f"  none do                    {distinct:4d} codes  {distinct_t:6d} tokens  "
          f"{distinct_t/tot*100:5.1f}%")
    print()
    print("  one concept, several English forms:")
    for n, t in ex_one:
        print(f"    {n:4d}  {t}")
    print("  no shared stem (a lower bound counts these as ambiguous,")
    print("  though fire/flame and Word/gospel are plainly one concept):")
    for n, t in ex_dist:
        print(f"    {n:4d}  {t}")


def main():
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
        out = []
        if t in gl:
            for s in sorted(gl[t]):
                out += Q.sense_stems(s)
        elif t in seg:
            for p in seg[t]:
                for s in sorted(gl[p]):
                    out += Q.sense_stems(s)
        return out

    stream, owner = [], []
    for p in doc:
        for line in p.lines:
            for x in line:
                for t in (x if isinstance(x, list) else [x]):
                    stream.append(t)
                    owner.append(p.page)

    rng = random.Random(408)
    multi, single = [], []
    for c in sorted(gl):
        n = types.get(c, 0)
        if n < MIN_OCC:
            continue
        real = [s for s in sorted(gl[c]) if Q.sense_stems(s)]
        v = variance_explained(context_vectors(c, stream, owner, stems_for), rng)
        if v is None:
            continue
        (multi if len(real) > 1 else single).append((c, n, len(real), v))

    print("=" * 70)
    print("ARE A CODE'S SENSES SEPARATED BY CONTEXT?")
    print("=" * 70)
    print(f"codes with {MIN_OCC}+ occurrences:  "
          f"{len(multi)} multi-sense, {len(single)} single-sense")
    if not multi or not single:
        print("  not enough of one kind to compare")
        return 1

    obs_m = sum(v for _, _, _, v in multi) / len(multi)

    # frequency-matched control: for each multi-sense code draw a single-sense
    # code of comparable frequency, many times
    nulls = []
    for _ in range(300):
        picks = []
        for _, n, _, _ in multi:
            near = [x for x in single if abs(x[1] - n) <= max(5, n * 0.5)] or single
            picks.append(rng.choice(near)[3])
        nulls.append(sum(picks) / len(picks))
    m = sum(nulls) / len(nulls)
    sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
    sig = (obs_m - m) / sd if sd else 0.0
    ratio = obs_m / m if m else 0.0

    print(f"  variance explained, multi-sense codes      {obs_m*100:5.1f}%")
    print(f"  variance explained, matched single-sense   {m*100:5.1f}%  (sd {sd*100:.2f})")
    print(f"  ratio {ratio:.2f}x     sigma {sig:.1f}")
    ok = ratio >= BAR_RATIO and sig >= BAR_SIGMA
    print()
    print(f"  BAR: ratio >= {BAR_RATIO}x and sigma >= {BAR_SIGMA}  ->  "
          f"{'PASS' if ok else 'FAIL'}")
    print()
    if ok:
        print("  A code with several senses splits its occurrences more cleanly")
        print("  than a code with one. The senses are conditioned by context, so")
        print("  a better chooser is worth building and the 66% is reachable.")
    else:
        print("  Codes with several senses split no better than codes with one.")
        print("  On this evidence the senses are not separated by context, and")
        print("  no amount of context modelling will choose between them.")

    sense_kinds(gl, types)

    print("\n  most contextually split multi-sense codes:")
    for c, n, k, v in sorted(multi, key=lambda x: -x[3])[:12]:
        print(f"    {n:4d} occ  {k} senses  {v*100:4.1f}%  "
              f"{', '.join(sorted(gl[c]))[:52]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
