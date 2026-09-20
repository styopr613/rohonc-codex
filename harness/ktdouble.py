"""Passages the book writes twice, found by shared runs of word types.

The creation narrative is written once at 002v-003v and again at 121v-123r,
sentence for sentence. Kiraly and Tokai's dictionary shows it, because entry
after entry cites the two copies together, but nothing in this project looked
for it. A repeat is worth a great deal: the copies are rarely equally
readable, so the better-read one reads the gaps of the other, and a sign in
the matching slot of a parallel sentence is read the way a formula slot is.

The method is the plainest one that works. Take every window of N consecutive
tokens in the book, keyed by the token types alone, and report the windows
that occur in two places far apart. Then merge overlapping hits into runs and
print the longest runs, longest first.

    python3 ktdouble.py              # the repeated passages, longest first
    python3 ktdouble.py --n 5        # a shorter window, more and noisier hits
    python3 ktdouble.py --show 002v  # print both copies of every run on a page

Windows inside one page, or within twenty lines of each other, are skipped:
the book repeats formulas locally all the time and those are not passages.
"""
import sys
from collections import defaultdict

import ktaffix as A
import ktcontext as X


def stream(doc):
    """[(page, line, token)] in book order."""
    out = []
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            for run in ln:
                for t in run:
                    out.append((p.page, i, A.strip(t)[0]))
    return out


def runs(seq, n):
    """Merge windows of length n that repeat, into (a, b, length) matches."""
    seen = defaultdict(list)
    for i in range(len(seq) - n + 1):
        key = tuple(t for _, _, t in seq[i:i + n])
        seen[key].append(i)
    pairs = set()
    for key, idx in seen.items():
        if len(idx) < 2 or len(idx) > 8:
            continue
        for a in range(len(idx)):
            for b in range(a + 1, len(idx)):
                i, j = idx[a], idx[b]
                if j - i < 60:
                    continue
                pairs.add((i, j))
    # merge diagonally adjacent windows into runs
    best = {}
    for i, j in sorted(pairs):
        d = j - i
        if (i - 1, j - 1) in pairs:
            continue
        L = n
        while (i + L - n + 1, j + L - n + 1) in pairs:
            L += 1
        key = (i, d)
        best[key] = L
    return [(i, i + d, L) for (i, d), L in best.items()]


def main(argv):
    n = 8
    show = None
    if "--n" in argv:
        n = int(argv[argv.index("--n") + 1])
    if "--show" in argv:
        show = argv[argv.index("--show") + 1]
    gl, doc, seg, var = X.load()
    seq = stream(doc)
    found = runs(seq, n)
    found.sort(key=lambda r: -r[2])
    print(f"{len(seq)} tokens, window {n}: {len(found)} repeated runs "
          f"(separated by 60+ tokens)")
    print()
    shown = 0
    for i, j, L in found:
        pa, la, _ = seq[i]
        pb, lb, _ = seq[j]
        if show and show not in (pa, pb):
            continue
        print(f"{L:3d} tokens   {pa}:{la:<3d} = {pb}:{lb:<3d}")
        if show:
            for k, (p0, l0) in ((i, (pa, la)), (j, (pb, lb))):
                words = " ".join(X.word(t, gl, seg, var)
                                 for _, _, t in seq[k:k + L])
                print(f"    {p0}:{l0:<3d} {words[:300]}")
            print()
        shown += 1
        if shown >= (40 if not show else 20):
            break
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
