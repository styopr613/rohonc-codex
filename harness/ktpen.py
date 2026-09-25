"""The second pass: redraw a traced sign as an even pen stroke.

The first pass (kttrace.py, ktcut.py) gives the scribe's ink stacked from
several copies, but a 13-pixel original enlarged eight times comes out lumpy:
uneven edges, blobs where strokes meet, a neighbour's tail. This redraws it.

  1. Thin the traced ink to its centreline (Zhang-Suen).
  2. Prune spurs: centreline branches shorter than about two stroke widths.
  3. Compare with Király and Tokai's outline of the same sign, scaled to the
     same box, and REMOVE centreline far from any of their ink. That catches
     a neighbour's stroke or a smudge the first pass kept.
  4. Redraw the centreline with a round pen as wide as the scribe's median
     stroke, smooth it, and trace it.

THE RULE: their outline may only take ink away from ours, never add any.
Every line kept is on the scribe's centreline, drawn from the scan. Their
outline is a check, not a source. Shapes will look alike because both are
drawings of the same sixteenth-century signs; the lines here are not theirs.
"""
import numpy as np
from PIL import Image
from scipy import ndimage as nd


def thin(m):
    """Zhang-Suen thinning of a boolean mask."""
    m = np.pad(m.astype(np.uint8), 1)
    while True:
        changed = False
        for step in (0, 1):
            P = [np.roll(np.roll(m, dy, 0), dx, 1) for dy, dx in
                 ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1))]
            # P2..P9 clockwise from north: north is row-1, i.e. roll +1
            p2, p3, p4, p5, p6, p7, p8, p9 = P
            B = sum(P)
            seq = [p2, p3, p4, p5, p6, p7, p8, p9, p2]
            A = sum(((seq[i] == 0) & (seq[i + 1] == 1)).astype(np.uint8) for i in range(8))
            if step == 0:
                c = (p2 * p4 * p6 == 0) & (p4 * p6 * p8 == 0)
            else:
                c = (p2 * p4 * p8 == 0) & (p2 * p6 * p8 == 0)
            kill = (m == 1) & (B >= 2) & (B <= 6) & (A == 1) & c
            if kill.any():
                m[kill] = 0
                changed = True
        if not changed:
            break
    return m[1:-1, 1:-1].astype(bool)


def _nbrs(sk):
    k = np.ones((3, 3), int)
    k[1, 1] = 0
    return nd.convolve(sk.astype(int), k, mode="constant") * sk


def prune(sk, length):
    """Remove end branches shorter than `length` pixels, repeatedly."""
    sk = sk.copy()
    for _ in range(3):
        n = _nbrs(sk)
        ends = list(zip(*np.nonzero((n == 1))))
        removed = False
        for y, x in ends:
            path, cy, cx, prev = [(y, x)], y, x, None
            while len(path) <= length:
                nb = [(cy + dy, cx + dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1)
                      if (dy or dx) and 0 <= cy + dy < sk.shape[0] and 0 <= cx + dx < sk.shape[1]
                      and sk[cy + dy, cx + dx] and (cy + dy, cx + dx) not in path]
                if len(nb) != 1:
                    break
                cy, cx = nb[0]
                if n[cy, cx] > 2:
                    break
                path.append((cy, cx))
            if len(path) <= length and n[cy, cx] > 2:
                for p in path[:-1] if len(path) > 1 else path:
                    sk[p] = False
                removed = True
        if not removed:
            break
    return sk


def fit_box(src, shape_box):
    """Scale mask `src` into the bounding box (y0, x0, y1, x1) on a canvas of `shape`."""
    (H, W), (y0, x0, y1, x1) = shape_box
    ys, xs = np.nonzero(src)
    out = np.zeros((H, W), bool)
    if len(ys) == 0 or y1 <= y0 or x1 <= x0:
        return out
    crop = src[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    im = Image.fromarray(crop.astype(np.uint8) * 255).resize((x1 - x0, y1 - y0), Image.BILINEAR)
    out[y0:y1, x0:x1] = np.array(im) > 127
    return out


def pen(mask, kt=None, reach=2.5):
    """Redraw `mask` as an even pen stroke. `kt`, if given, is their outline
    rasterised at any size; it is fitted to our ink's box and used only to
    remove centreline further than `reach` stroke widths from their ink."""
    if not mask.any():
        return mask
    dist = nd.distance_transform_edt(mask)
    sk = thin(mask)
    wid = float(np.median(dist[sk])) if sk.any() else 2.0
    sk = prune(sk, int(4 * wid))
    if kt is not None and kt.any():
        ys, xs = np.nonzero(mask)
        box = (mask.shape, (ys.min(), xs.min(), ys.max() + 1, xs.max() + 1))
        k = fit_box(kt, box)
        far = nd.distance_transform_edt(~k) > reach * wid
        sk = sk & ~far                           # subtract only
    r = max(1.5, wid * 0.95)
    stroke = nd.distance_transform_edt(~sk) <= r
    soft = nd.gaussian_filter(stroke.astype(float), r * 0.35)
    return (soft > 0.5) & (nd.binary_dilation(mask, iterations=int(r)))   # never outside the scribe's ink
