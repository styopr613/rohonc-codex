"""Is the Rohonc's repetition a real text reusing phrases, or bulk copying?

The cross-line result (ROHONC.md) shows the Rohonc's text is independent of the
page it is written on: passages recur at different distances from the margin.
That rules out tracing, and it rules out a process that composes line by line.
It does not rule out a person filling 448 pages by recycling earlier ones.

So: how much of the book is new?

A real text reuses material for reasons of content. A liturgical or devotional
book repeats set phrases constantly, and a gospel harmony repeats whole
passages, because the same episode appears in more than one gospel -- so long
verbatim parallels are expected and prove nothing on their own. What a real
text still does is carry a large majority of material that occurs once. A book
padded by recycling does not.

Measured as coverage: the share of tokens lying inside some sequence of length
k or more that occurs at least twice anywhere in the book.

Two controls, both needed.

The Rohonc uses only 987 distinct symbols across 60,000 tokens, so short
sequences repeat constantly by chance alone. The baseline shuffles the whole
token stream, preserving the vocabulary and every symbol's frequency exactly
and destroying only the order. That is the coverage this vocabulary produces
with no text behind it at all.

Coverage also grows with length, so comparisons between manuscripts are made on
prefixes truncated to a common token count, and the Rohonc's full-book figure
is reported separately against its own shuffle.

Repeats may not cross a gap left by an unreadable glyph, nor a break between
non-consecutive folios; a unique sentinel is inserted at each, so no repeat is
manufactured across missing text.

    python repeats.py
"""
import random
import sys
from collections import defaultdict

import corpus

SEED = 408
KS = (3, 5, 8, 12, 20, 30, 50)


def coverage(seq, k):
    """Share of positions inside a k-gram that occurs at least twice."""
    n = len(seq)
    if n < k:
        return 0.0
    seen = defaultdict(int)
    for i in range(n - k + 1):
        seen[tuple(seq[i:i + k])] += 1
    covered = bytearray(n)
    for i in range(n - k + 1):
        if seen[tuple(seq[i:i + k])] > 1:
            for j in range(i, i + k):
                covered[j] = 1
    return sum(covered) / n * 100


def longest_repeat(seq, cap=4000):
    """Length of the longest sequence occurring at least twice."""
    lo, hi = 1, min(cap, len(seq) // 2)
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        seen = set()
        hit = False
        for i in range(len(seq) - mid + 1):
            g = tuple(seq[i:i + mid])
            if g in seen:
                hit = True
                break
            seen.add(g)
        if hit:
            best, lo = mid, mid + 1
        else:
            hi = mid - 1
    return best


def multiplicity(seq, k):
    """How many distinct k-grams repeat, and the most repeats any one gets."""
    seen = defaultdict(int)
    for i in range(len(seq) - k + 1):
        seen[tuple(seq[i:i + k])] += 1
    rep = [c for c in seen.values() if c > 1]
    return len(rep), (max(rep) if rep else 0)


def rohonc_stream():
    """Reading-order token stream with sentinels at every discontinuity."""
    import rohonc
    doc = rohonc.load()
    out = []
    mark = 0
    prev_page = None
    for p in doc:
        try:
            pn = int(p.page)
        except (TypeError, ValueError):
            pn = None
        if prev_page is not None and (pn is None or pn != prev_page + 1):
            mark += 1
            out.append(f"\x00gap{mark}")
        prev_page = pn
        for runs in p.lines:
            for ri, run in enumerate(runs):
                if ri:                       # an unreadable glyph sat here
                    mark += 1
                    out.append(f"\x00gap{mark}")
                out.extend(run)
    return out


def report(label, seq, rng, ks=KS, shuffles=3):
    row = [coverage(seq, k) for k in ks]
    nulls = [[] for _ in ks]
    for _ in range(shuffles):
        sh = seq[:]
        rng.shuffle(sh)
        for i, k in enumerate(ks):
            nulls[i].append(coverage(sh, k))
    base = [sum(x) / len(x) for x in nulls]
    print(f"{label:24s}" + "".join(f"{v:8.1f}" for v in row))
    print(f"{'  (shuffled)':24s}" + "".join(f"{v:8.1f}" for v in base))
    return row, base


# --------------------------------------------------------------------------
# where the repeats sit
# --------------------------------------------------------------------------
def distances(seq, k):
    """Gaps, in tokens, between consecutive occurrences of each repeated k-gram."""
    pos = defaultdict(list)
    for i in range(len(seq) - k + 1):
        pos[tuple(seq[i:i + k])].append(i)
    out = []
    for p in pos.values():
        if len(p) > 1:
            out.extend(b - a for a, b in zip(p, p[1:]))
    return sorted(out)


def where(label, seq, ks=(8, 12, 20)):
    n = len(seq)
    for k in ks:
        d = distances(seq, k)
        if not d:
            print(f"  {label:20s} k={k:<3d} no repeats")
            continue
        med = d[len(d) // 2]
        near = sum(1 for x in d if x <= 300) / len(d) * 100      # same folio
        far = sum(1 for x in d if x > 3000) / len(d) * 100       # >10 folios off
        print(f"  {label:20s} k={k:<3d} {len(d):6d} gaps   median {med:6d}   "
              f"same folio {near:5.1f}%   far apart {far:5.1f}%   "
              f"longest gap {d[-1]}  (book is {n})")


def main():
    rng = random.Random(SEED)
    roh = rohonc_stream()
    ev = corpus.words(corpus.load())
    from generators.natlang import plaintext

    langs = []
    for lg in ("italian", "latin", "hebrew"):
        try:
            langs.append((lg, plaintext(lg, limit=200000)))
        except Exception as e:
            print(f"  ({lg} unavailable: {e})", file=sys.stderr)

    n = min([len(roh), len(ev)] + [len(w) for _, w in langs])
    print("=" * 86)
    print("HOW MUCH OF THE BOOK IS NEW?")
    print("=" * 86)
    print("Share of tokens (%) inside a sequence of length k or more that occurs")
    print("at least twice. `shuffled` preserves the vocabulary and destroys the")
    print(f"order. All texts truncated to {n} tokens so the lengths match.\n")
    print(f"{'k =':24s}" + "".join(f"{k:8d}" for k in KS))
    print("-" * 86)
    report("Rohonc Codex", roh[:n], rng)
    report("Voynich (words)", ev[:n], rng)
    for lg, w in langs:
        report(f"{lg} prose (words)", w[:n], rng)

    print("\n" + "=" * 86)
    print("THE ROHONC AT FULL LENGTH, AGAINST ITS OWN SHUFFLE")
    print("=" * 86)
    print(f"{len(roh)} tokens\n")
    print(f"{'k =':24s}" + "".join(f"{k:8d}" for k in KS))
    print("-" * 86)
    report("Rohonc Codex", roh, rng)

    print("\nlongest sequence occurring at least twice, in tokens:")
    for lab, s in (("Rohonc Codex", roh), ("Voynich (words)", ev)) + \
                  tuple((f"{lg} prose", w[:len(roh)]) for lg, w in langs):
        print(f"  {lab:24s} {longest_repeat(s):6d}")

    print("\nrepeated sequences at k=20, and the most repeats any one of them gets:")
    for lab, s in (("Rohonc Codex", roh), ("Voynich (words)", ev)) + \
                  tuple((f"{lg} prose", w[:len(roh)]) for lg, w in langs):
        d, mx = multiplicity(s, 20)
        print(f"  {lab:24s} {d:6d} distinct   max {mx}")

    print("\nlongest repeat, bounded both ways:")
    import rohonc as _rh
    flat = [t for pg in _rh.load() for t in pg.tokens]
    print(f"  sentinels at every gap (lower bound)  {longest_repeat(roh):6d} tokens")
    print(f"  gaps ignored entirely  (upper bound)  {longest_repeat(flat):6d} tokens")
    nl = sum(len(pg.lines) for pg in _rh.load())
    print(f"  a folio averages {len(flat)//len(_rh.load())} tokens, a line {len(flat)//nl}")
    for k in (60, 100, 150):
        print(f"  coverage at k={k:<4d} {coverage(flat, k):.2f}%")

    print("\ndistance between repeated sequences (a folio is about 282 tokens):")
    where("Rohonc Codex", roh)
    for lg, w in langs:
        where(f"{lg} prose", w[:len(roh)])

    print("\n  A real text carries a large majority of material that occurs once,")
    print("  however many set phrases it reuses. Coverage near the shuffled")
    print("  baseline means the repetition is only what the vocabulary forces;")
    print("  coverage far above it at large k means whole passages recur.")


if __name__ == "__main__":
    main()
