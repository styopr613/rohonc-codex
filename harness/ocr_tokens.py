"""Turn the segmented scan into a token stream by clustering look-alike images.

Nothing here reads anything. Two ink shapes get the same label if they look the
same, which is all the cross-line test needs: it asks whether sequences recur,
never what they say. The output is a third transcription of the Rohonc Codex,
independent of both human ones, whose errors are machine errors and therefore
uncorrelated with theirs.

Each token image is trimmed to its ink, scaled to a fixed raster and compared
with every other token of similar shape. Tokens closer than a threshold are
merged by union-find into a type. Both free parameters -- the blank width that
ends a token, and the merge distance -- are swept rather than chosen, because
neither has a value the page picks out. A conclusion that holds across both
sweeps does not rest on either.

The two failure modes pull opposite ways and both corrupt exactly the statistic
this is for. Merging too eagerly makes distinct words identical and inflates
repeats; merging too little splits one word into several types and destroys
them. The sweep is what shows which side the answer is sitting on.

    python ocr_tokens.py --ratio 0.25 --merge 0.10
"""
import argparse
import glob
import os
import pickle

import numpy as np
from PIL import Image, ImageFilter

import corpus
import roho_ocr as R

WORK = os.path.join(corpus.ROOT, "work", "rohonc")
RH, RW = 16, 32          # the raster every token is compared on
BLUR = 1.2               # stroke-jitter tolerance, in raster pixels


def raster(w, ink=120):
    """Token image as a fixed binary raster, plus its true aspect ratio."""
    b = (w < ink)
    rows = np.where(b.any(axis=1))[0]
    cols = np.where(b.any(axis=0))[0]
    if not len(rows) or not len(cols):
        return None, None
    t = w[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1]
    ar = t.shape[1] / t.shape[0]
    im = Image.fromarray(t).resize((RW, RH), Image.LANCZOS)
    b = (np.array(im) < ink).astype(np.float32)
    # A pen stroke lands a pixel or two off between two writings of the same
    # word, and on a 16-row raster that is most of a stroke. Blurring before
    # comparison makes the match tolerant of that jitter; without it nothing
    # merges at any sane threshold (type/token stayed at 0.998).
    b = np.array(Image.fromarray((b * 255).astype(np.uint8))
                 .filter(ImageFilter.GaussianBlur(BLUR)), dtype=np.float32) / 255.0
    return b.ravel(), ar


def extract(ratio, limit=None):
    """[(page id, [[raster, ...] per line])] over the whole scan."""
    fs = sorted(glob.glob(os.path.join(R.SCAN, "nat*.png")))
    if limit:
        fs = fs[:limit]
    out = []
    for si, f in enumerate(fs):
        for side, lines in R.read_spread(f, ratio=ratio):
            page = f"{si:03d}{side[0]}"
            rows = []
            for ws in lines:
                row = []
                for w in ws:
                    v, ar = raster(w)
                    if v is not None and v.sum() >= 6:
                        row.append((v, ar))
                if row:
                    rows.append(row)
            if rows:
                out.append((page, rows))
    return out


class Union:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


def cluster(vecs, ars, merge=0.10, band=0.18):
    """Merge tokens whose rasters differ by less than `merge` of their ink.

    Comparisons are blocked by aspect ratio: two tokens whose widths differ by
    more than `band` in log ratio are never the same word, and skipping them
    keeps this within one pass of matrix arithmetic per block.
    """
    n = len(vecs)
    V = np.asarray(vecs, dtype=np.float32)
    A = np.log(np.asarray(ars, dtype=np.float32) + 1e-6)
    ink = V.sum(axis=1)
    u = Union(n)
    order = np.argsort(A)
    lo = 0
    while lo < n:
        hi = lo
        while hi < n and A[order[hi]] - A[order[lo]] <= band:
            hi += 1
        idx = order[lo:hi]
        if len(idx) > 1:
            B = V[idx]
            # Hamming on a binary raster: |a| + |b| - 2 a.b
            d = ink[idx][:, None] + ink[idx][None, :] - 2.0 * (B @ B.T)
            scale = np.maximum(ink[idx][:, None], ink[idx][None, :])
            rel = d / np.maximum(scale, 1.0)
            ii, jj = np.where(np.triu(rel < merge, 1))
            for a, b in zip(idx[ii], idx[jj]):
                u.union(int(a), int(b))
        lo = hi if hi > lo else lo + 1
    return np.array([u.find(i) for i in range(n)])


def build(ratio, merge, limit=None):
    pages = extract(ratio, limit)
    vecs, ars, where = [], [], []
    for pi, (page, rows) in enumerate(pages):
        for li, row in enumerate(rows):
            for v, ar in row:
                vecs.append(v)
                ars.append(ar)
                where.append((pi, li))
    if not vecs:
        return [], {}
    lab = cluster(vecs, ars, merge)
    remap, nxt = {}, 0
    ids = []
    for x in lab:
        if x not in remap:
            remap[x] = nxt
            nxt += 1
        ids.append(f"t{remap[x]}")
    doc, k = [], 0
    for page, rows in pages:
        lines = []
        for row in rows:
            lines.append([[ids[k + i] for i in range(len(row))]])
            k += len(row)
        doc.append((page, lines))
    stats = {"tokens": len(ids), "types": nxt, "pages": len(pages),
             "lines": sum(len(r) for _, r in pages)}
    return doc, stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ratio", type=float, default=0.25)
    ap.add_argument("--merge", type=float, default=0.10)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--save", default=None)
    a = ap.parse_args()
    doc, st = build(a.ratio, a.merge, a.limit)
    print(f"ratio {a.ratio}  merge {a.merge}  -> {st}")
    if st:
        print(f"  TTR {st['types']/st['tokens']:.4f}, "
              f"{st['tokens']/max(1,st['lines']):.2f} tokens/line")
    if a.save:
        os.makedirs(WORK, exist_ok=True)
        with open(os.path.join(WORK, a.save), "wb") as fh:
            pickle.dump(doc, fh)
        print("  saved", a.save)


if __name__ == "__main__":
    main()
