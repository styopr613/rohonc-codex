"""Scoring in floor units.

Mean absolute percentage error is the fingerprint repo's scale and this harness
keeps it, so our numbers stay comparable to its published ones. But APE is
unusable on a metric whose true value is near zero: the manuscript repeats a
word across a line boundary 0.12 % of the time, and the book's own other half
misses that by 196 % while being off by 0.24 percentage points. A ranking built
on that number is measuring the estimator, not the process.

So every metric is also scored in units of how far two halves of the same book
sit apart on it. The scale is estimated by cutting the TRAIN half into k
contiguous chunks the size of the held-out half's paragraphs, measuring each
against the held-out half, and taking the mean absolute deviation per metric.

A score of 1.0 means "off by as much as the manuscript is off from itself".
Below 1.0 means the difference is inside the book's own sampling spread and
nothing can be claimed from it. This is the scale the write-up ranks on; APE is
reported beside it for continuity with the literature.
"""
import os

import corpus
import profile as prof

FLOOR_CHUNKS = 6
TINY = 1e-12


def chunks(train, k=FLOOR_CHUNKS):
    """k contiguous paragraph blocks of TRAIN, each of similar size."""
    total = sum(len(p.words) for p in train)
    per = total / k
    out, cur, got = [], [], 0
    for p in train:
        cur.append(p)
        got += len(p.words)
        if got >= per and len(out) < k - 1:
            out.append(cur)
            cur, got = [], 0
    if cur:
        out.append(cur)
    return [c for c in out if c]


def scale(train, ref, k=FLOOR_CHUNKS):
    """Per-metric mean absolute deviation between a chunk of TRAIN and the
    held-out half. This is the natural unit of each metric."""
    devs = {b: {m: [] for m in ref[b]} for b in prof.BLOCKS}
    for c in chunks(train, k):
        p = prof.profile(c)
        for b in prof.BLOCKS:
            for m in ref[b]:
                devs[b][m].append(abs(p[b][m] - ref[b][m]))
    return {b: {m: max(sum(v) / len(v), TINY) for m, v in devs[b].items()}
            for b in prof.BLOCKS}


def score(gen, ref, sc):
    """Absolute deviation from the manuscript, in floor units."""
    out = {}
    for b in prof.BLOCKS:
        out[b] = {m: abs(gen[b][m] - ref[b][m]) / sc[b][m] for m in ref[b]}
    # length distribution: total variation, scaled the same way
    g, r = gen["_lendist"], ref["_lendist"]
    gt, rt = sum(g.values()), sum(r.values())
    tv = 0.5 * sum(abs(g[k] / gt - r[k] / rt) for k in set(g) | set(r))
    out["text"]["len dist TV"] = tv / sc["text"]["len dist TV"]
    return out


def lendist_scale(train, ref, k=FLOOR_CHUNKS):
    """The TV metric has no single-document value, so its floor is measured
    directly as the mean TV between a TRAIN chunk and the held-out half."""
    r = ref["_lendist"]
    rt = sum(r.values())
    vals = []
    for c in chunks(train, k):
        g = prof.profile(c)["_lendist"]
        gt = sum(g.values())
        vals.append(0.5 * sum(abs(g[x] / gt - r[x] / rt) for x in set(g) | set(r)))
    return max(sum(vals) / len(vals), TINY)


def build(train, ref, k=FLOOR_CHUNKS):
    sc = scale(train, ref, k)
    sc["text"]["len dist TV"] = lendist_scale(train, ref, k)
    return sc


def means(fs):
    per = {b: sum(fs[b].values()) / len(fs[b]) for b in prof.BLOCKS}
    allv = [v for b in prof.BLOCKS for v in fs[b].values()]
    per["overall"] = sum(allv) / len(allv)
    per["fingerprint44"] = (sum(fs["text"].values()) + sum(fs["struct"].values())) / (
        len(fs["text"]) + len(fs["struct"]))
    return per


def medians(fs):
    """Median floor units per block. The mean is dragged by one bad metric;
    the median says where the typical metric sits."""
    import statistics
    per = {b: statistics.median(fs[b].values()) for b in prof.BLOCKS}
    allv = [v for b in prof.BLOCKS for v in fs[b].values()]
    per["overall"] = statistics.median(allv)
    return per
