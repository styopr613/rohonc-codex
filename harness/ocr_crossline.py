"""The cross-line test run on images, with no transcription step at all.

Clustering the scanned tokens into types failed honestly: at this resolution a
token is sixteen pixels tall, handwriting moves a stroke further than that
between two writings of the same word, and no merge threshold produced a
vocabulary anything like either human transcription's without visibly merging
words that differ. Forcing a hard label on every token invents information the
pixels do not carry.

So the labels are dropped. The test never needed them. It asks whether a
sequence straddling a line break is one the manuscript also writes inside a
line -- and "the same sequence" can be decided by image similarity directly.

For each token, its neighbourhood is every token whose raster lies within a
distance. A straddling pair (A, B) counts as occurring inside a line if some
adjacent within-line pair (A', B') has A' in the neighbourhood of A and B' in
the neighbourhood of B. Chance is the same measurement after shuffling which
line follows which inside a page, which leaves every line intact and destroys
only the pairing.

The neighbourhood radius is swept. Both the observed and the chance figure use
the same radius at every point, so the comparison is fair wherever it is read:
a radius too tight makes everything unmatched, too loose makes everything
matched, and neither can manufacture a gap between them.

    python ocr_crossline.py
"""
import random
from collections import defaultdict

import numpy as np

import ocr_tokens as O

SEED = 408
SHUFFLES = 10
RADII = (0.05, 0.10, 0.15, 0.20, 0.30, 0.40)


def neighbours(V, ink, ars, radius, band=0.18):
    """For each token, the set of tokens within `radius`, blocked by shape."""
    n = len(V)
    A = np.log(np.asarray(ars, dtype=np.float32) + 1e-6)
    out = [set() for _ in range(n)]
    order = np.argsort(A)
    lo = 0
    while lo < n:
        hi = lo
        while hi < n and A[order[hi]] - A[order[lo]] <= band:
            hi += 1
        idx = order[lo:hi]
        if len(idx) > 1:
            B = V[idx]
            d = ink[idx][:, None] + ink[idx][None, :] - 2.0 * (B @ B.T)
            rel = d / np.maximum(np.maximum(ink[idx][:, None],
                                            ink[idx][None, :]), 1.0)
            ii, jj = np.where(rel < radius)
            for a, b in zip(idx[ii], idx[jj]):
                out[int(a)].add(int(b))
        lo = hi if hi > lo else lo + 1
    for i in range(n):
        out[i].add(i)
    return out


def line_index(pages):
    """Flat token ids, and the per-page list of lines as id lists."""
    ids, doc, k = [], [], 0
    for page, rows in pages:
        lines = []
        for row in rows:
            lines.append(list(range(k, k + len(row))))
            k += len(row)
            ids.extend([None] * 0)
        doc.append(lines)
    return doc, k


def within_pairs(doc, order=None):
    out = []
    for gi, lines in enumerate(doc):
        idx = order[gi] if order else list(range(len(lines)))
        for li in idx:
            ln = lines[li]
            out.extend(zip(ln, ln[1:]))
    return out


def straddling(doc, order=None):
    out = []
    for gi, lines in enumerate(doc):
        idx = order[gi] if order else list(range(len(lines)))
        for a, b in zip(idx, idx[1:]):
            x, y = lines[a], lines[b]
            if x and y:
                out.append((x[-1], y[0]))
    return out


def rate(pairs, index, N):
    """Share of pairs that also occur, up to image similarity, inside a line."""
    if not pairs:
        return 0.0
    hit = 0
    for a, b in pairs:
        nb = N[b]
        for a2 in N[a]:
            s = index.get(a2)
            if s and not s.isdisjoint(nb):
                hit += 1
                break
    return hit / len(pairs) * 100


def main():
    rng = random.Random(SEED)
    for ratio in (0.18, 0.25, 0.32):
        pages = O.extract(ratio)
        vecs, ars = [], []
        for _, rows in pages:
            for row in rows:
                for v, ar in row:
                    vecs.append(v)
                    ars.append(ar)
        V = np.asarray(vecs, dtype=np.float32)
        ink = V.sum(axis=1)
        doc, n = line_index(pages)
        wp = within_pairs(doc)
        index = defaultdict(set)
        for a, b in wp:
            index[a].add(b)
        sp = straddling(doc)
        print(f"\n=== blank-width ratio {ratio}: {n} tokens, "
              f"{sum(len(l) for l in doc)} lines, "
              f"{len(wp)} within-line pairs, {len(sp)} straddling ===")
        print(f"{'radius':>7s} {'straddling':>11s} {'chance':>9s} {'sd':>6s} "
              f"{'sigma':>7s} {'headroom':>9s}")
        for r in RADII:
            N = neighbours(V, ink, ars, r)
            obs = rate(sp, index, N)
            nulls = []
            for _ in range(SHUFFLES):
                order = []
                for lines in doc:
                    o = list(range(len(lines)))
                    rng.shuffle(o)
                    order.append(o)
                nulls.append(rate(straddling(doc, order), index, N))
            m = sum(nulls) / len(nulls)
            sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
            sig = (obs - m) / sd if sd else 0.0
            head = (obs - m) / (100.0 - m) * 100 if m < 100 else float("nan")
            print(f"{r:7.2f} {obs:10.2f}% {m:8.2f}% {sd:6.2f} {sig:7.1f} {head:8.1f}%")


if __name__ == "__main__":
    main()
