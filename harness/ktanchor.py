"""Working backwards from the parts that are certainly right.

Some of the translation is bound to be correct. The question is which parts,
decided by something other than my say-so, and what they can then be used to
prove.

The most certain evidence in the book needs no dictionary at all: the codex
repeats itself. Where two passages run identically for several codes, break
for exactly one code, and then run identically again, the two odd codes stand
in the same slot of the same sentence. That is a substitution frame, and it is
the oldest lever in cryptanalysis -- known plaintext either side of an unknown.

    ... A B C  [X]  D E F ...
    ... A B C  [Y]  D E F ...

X and Y are used the same way. If X is defined and Y is not, Y inherits X's
reading on positional evidence alone, with no alignment to an outside text and
no appeal to what the passage seems to mean.

THE GATE, fixed before the run and not moved.

  Take the frames where BOTH codes are defined by Kiraly & Tokai -- the
  answer is known there. Ask whether the two glosses share a content stem.

  The control keeps one member of each pair and replaces the other with a
  random defined code of comparable frequency, so gloss vocabulary, pair
  count and the stemmer are all fixed and only substitutability is destroyed.

  BAR: at least 40% of known frames share a stem, at least twice the control,
  and at least 5 sigma above it.

  Below any of the three, a substitution frame does not predict meaning, the
  undefined halves are not read, and this is reported as the fifteenth
  failure.

Context radius is fixed at 3 codes either side -- six identical codes around
the break -- and declared here before the run. Radius 2 and 4 are printed
alongside as supporting detail only; the verdict is radius 3.

    python ktanchor.py
"""
import random
import sys
from collections import Counter, defaultdict

import ktdict
import ktextend as E
import ktsegment as S
import rohonc_kt as KT

RADIUS = 3
BAR_HIT = 0.40
BAR_RATIO = 2.0
BAR_SIGMA = 5.0


def runs(doc):
    """Every unbroken run of codes: a gap or a folio break ends a run."""
    out = []
    for p in doc:
        for line in p.lines:
            for run in line:
                if run:
                    out.append((p.page, run))
    return out


def frames(seq_list, radius):
    """{(a, b): [(page, left context)]} for codes substitutable in identical context.

    A frame is two positions in the book with the same `radius` codes before
    and the same `radius` codes after, and different codes between. Indexed
    by the shared context so the two sides never have to be compared
    pairwise.
    """
    index = defaultdict(list)
    for page, seq in seq_list:
        for i in range(radius, len(seq) - radius):
            key = (tuple(seq[i - radius:i]), tuple(seq[i + 1:i + 1 + radius]))
            index[key].append((seq[i], page))
    out = defaultdict(list)
    for key, hits in index.items():
        kinds = {c for c, _ in hits}
        if len(kinds) < 2:
            continue
        for a in sorted(kinds):
            for b in sorted(kinds):
                if a < b:
                    out[(a, b)].append((key, [pg for c, pg in hits]))
    return out


def stems(glosses):
    out = set()
    for s in glosses:
        s2 = E.META.sub(" ", s)
        out |= {E.stem(w) for w in E.WORD.findall(E.fold(s2).lower())
                if w not in E.STOP and len(w) > 2}
    return out


def gate(fr, gl, types, rng, trials=200):
    known = [(a, b) for (a, b) in fr if a in gl and b in gl
             and stems(gl[a]) and stems(gl[b])]
    if not known:
        return 0, 0.0, 0.0, 0.0, 0.0, 0.0, []
    hit = 0
    rows = []
    for a, b in known:
        sa, sb = stems(gl[a]), stems(gl[b])
        ok = bool(sa & sb)
        hit += ok
        rows.append((ok, len(fr[(a, b)]), a, b))
    obs = hit / len(known)

    pool = [c for c in gl if stems(gl[c])]
    bykey = defaultdict(list)
    for c in pool:
        bykey[min(types.get(c, 0), 50)].append(c)

    def match(c):
        n = min(types.get(c, 0), 50)
        for w in range(0, 51):
            cand = [x for k in range(max(0, n - w), min(50, n + w) + 1)
                    for x in bykey.get(k, []) if x != c]
            if len(cand) >= 5:
                return cand
        return pool

    nulls = []
    for _ in range(trials):
        k = 0
        for a, b in known:
            if rng.random() < 0.5:
                sa, sb = stems(gl[a]), stems(gl[rng.choice(match(b))])
            else:
                sa, sb = stems(gl[rng.choice(match(a))]), stems(gl[b])
            k += bool(sa & sb)
        nulls.append(k / len(known))
    m = sum(nulls) / len(nulls)
    sd = (sum((v - m) ** 2 for v in nulls) / max(1, len(nulls) - 1)) ** 0.5
    sig = (obs - m) / sd if sd else 0.0
    ratio = obs / m if m else float("inf")
    return len(known), obs, m, sd, sig, ratio, rows


def main():
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    types = Counter(t for p in doc for t in p.tokens)
    defset = set(gl)
    seg = {}
    for t in types:
        if t not in gl:
            s = S.segment(t, defset)
            if s and len(s) >= 2:
                seg[t] = s
    seq_list = runs(doc)
    rng = random.Random(408)

    print("=" * 76)
    print("SUBSTITUTION FRAMES: WORKING BACKWARDS FROM WHAT THE BOOK REPEATS")
    print("=" * 76)
    print(f"runs of consecutive codes {len(seq_list)}, "
          f"codes {sum(len(s) for _, s in seq_list)}")
    print()
    print(f"{'radius':>7s} {'frames':>8s} {'both defined':>13s} {'one undefined':>14s}")
    store = {}
    for r in (2, 3, 4):
        fr = frames(seq_list, r)
        both = sum(1 for a, b in fr if a in gl and b in gl)
        one = sum(1 for a, b in fr if (a in gl) != (b in gl))
        print(f"{r:7d} {len(fr):8d} {both:13d} {one:14d}")
        store[r] = fr

    fr = store[RADIUS]
    n, obs, m, sd, sig, ratio, rows = gate(fr, gl, types, rng)
    print()
    print(f"THE GATE -- radius {RADIUS}, declared before the run")
    print(f"  frames where both codes are defined      {n}")
    print(f"  the two glosses share a content stem     {obs*100:5.1f}%")
    print(f"  same test, one member randomised         {m*100:5.1f}%  (sd {sd*100:.2f})")
    print(f"  ratio {ratio:.2f}x     sigma {sig:.1f}")
    ok = obs >= BAR_HIT and ratio >= BAR_RATIO and sig >= BAR_SIGMA
    print()
    print(f"  BAR: hit >= {BAR_HIT*100:.0f}%, ratio >= {BAR_RATIO}x, "
          f"sigma >= {BAR_SIGMA}  ->  {'PASS' if ok else 'FAIL'}")

    print()
    print("  known frames, most attested first:")
    for hit, k, a, b in sorted(rows, key=lambda x: -x[1])[:18]:
        ga = S.best_sense(gl[a])[:22]
        gb = S.best_sense(gl[b])[:22]
        print(f"   {'ok ' if hit else '   '} {k:3d}x  {S.hx(a):16s} {ga:24s}"
              f"  ~  {S.hx(b):16s} {gb}")

    print()
    print("=" * 76)
    print("WHAT THAT READS" if ok else "WHAT IT WOULD HAVE READ (gate failed, nothing is claimed)")
    print("=" * 76)
    prop = defaultdict(Counter)
    for (a, b), hits in fr.items():
        for kn, un in ((a, b), (b, a)):
            if kn in gl and un not in gl and un not in seg:
                prop[un][kn] += len(hits)
    tok = sum(types[u] for u in prop)
    total = sum(types.values())
    print(f"  undefined, unsegmentable codes given a reading   {len(prop):5d}")
    print(f"  tokens they carry                               {tok:5d}  "
          f"({tok/total*100:.1f}% of the book)")
    print()
    print(f"  {'n':>5s}  {'code':18s}  reads as")
    for u in sorted(prop, key=lambda x: -types[x])[:25]:
        kn, k = prop[u].most_common(1)[0]
        print(f"  {types[u]:5d}  {S.hx(u):18s}  {S.best_sense(gl[kn])[:40]}"
              f"   ({k} frame{'s' if k > 1 else ''})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
