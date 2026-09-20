"""A third Rohonc transcription, made here from the scans.

Two transcriptions of this codex already exist: the anonymous open one of 2014
recovered from the Internet Archive, and Kiraly & Tokai's, served for
verification at rechnitzer-kodex.hu. Both were made by people, years apart, by
different methods. This makes a third by machine, from the page images, so that
the cross-line result can be checked against three sources whose errors have
nothing in common. Agreement across all three would mean the finding is not an
artefact of any one transcriber's decisions.

**The unit is a run of ink between blanks, and the blank width is a free
parameter.** Within a word the glyphs touch, so glyph segmentation would mean
guessing boundaries that presuppose a reading. Word segmentation looked easy on
a sample line, whose blank runs measured 1,1,2,2,3,4,5 pixels inside words and
7,10,12,12,15,24 between them. That was misleading. Pooled over 14,301 blank
runs from sixty spreads and scaled by line height, the distribution is not
bimodal at all -- it decays smoothly from zero to about 1.2 line heights with
no gap anywhere, so there is no threshold the page itself picks out, and Otsu's
method on it returns the meaningless 0.89 of the far tail.

That ambiguity is handled by not resolving it. The token stream is built at
several thresholds across the plausible range, and the cross-line test is run
at each. A finding that holds across the range does not depend on a choice
nobody can justify; one that moves with the threshold was never real. Kiraly &
Tokai's transcription is word-separated, so the threshold that reproduces their
token density is reported too, as a point of comparison rather than a target.

Nothing here attempts to read anything. Two word images get the same label if
they look the same. That is all the cross-line test needs, because it asks only
whether sequences recur, never what they say.

Source: real-ms.mtak.hu/80, the low-resolution scan, free for academic use and
not redistributed. 227 spreads at about 880x545, so a page is roughly 400x480
and a line of text about 16 to 18 pixels tall.
"""
import os

import numpy as np
from PIL import Image

import corpus

SCAN = os.path.join(corpus.DATA, "rohonc", "scan")

# blank width as a multiple of line height; swept, never fitted
SWEEP = (0.12, 0.18, 0.25, 0.32, 0.40, 0.50, 0.65)
SWEEP_DEFAULT = 0.32


def split_spread(a):
    """A scanned opening into its two pages, cut at the gutter."""
    col = a.mean(axis=0)
    mid = a.shape[1] // 2
    lo, hi = max(0, mid - 70), min(a.shape[1], mid + 70)
    seam = lo + int(np.argmin(col[lo:hi]))
    return a[:, :seam], a[:, seam:]


def page_box(p, bright=110, frac=0.30):
    """Bounding box of the lit page against the dark scanning surround."""
    b = p > bright
    rows, cols = b.sum(axis=1), b.sum(axis=0)
    r = np.where(rows > p.shape[1] * frac)[0]
    c = np.where(cols > p.shape[0] * frac)[0]
    if len(r) < 20 or len(c) < 20:
        return None
    return r[0], r[-1], c[0], c[-1]


def crop_page(p, inset=0.04):
    box = page_box(p)
    if box is None:
        return None
    r0, r1, c0, c1 = box
    dy, dx = int((r1 - r0) * inset), int((c1 - c0) * inset)
    sub = p[r0 + dy:r1 - dy, c0 + dx:c1 - dx]
    return sub if sub.shape[0] > 60 and sub.shape[1] > 60 else None


def lines_of(sub, ink=120, frac=0.10, minh=6):
    """Text lines, by horizontal ink projection."""
    prof = (sub < ink).sum(axis=1)
    if prof.max() < 3:
        return []
    thr = max(2, prof.max() * frac)
    out, inl, st = [], False, 0
    for i, v in enumerate(prof):
        if v > thr and not inl:
            inl, st = True, i
        elif v <= thr and inl:
            inl = False
            if i - st >= minh:
                out.append((st, i))
    if inl and len(prof) - st >= minh:
        out.append((st, len(prof)))
    return out


def word_gap(runs, lineh=17, ratio=None):
    """Blank width, in pixels, at or above which a blank ends a token.

    Expressed as a multiple of line height so it travels across a book whose
    line height drifts. There is no principled value: see the module docstring.
    Callers sweep `ratio`; the default is the midpoint of the swept range.

    Two earlier versions were wrong and are recorded because both produced
    plausible-looking output. The first took the widest jump in the sorted run
    widths, which lands on the extreme tail and merged most words (3.9 tokens
    per line against Kiraly & Tokai's 7.0). The second ran Otsu's method per
    line, which is unstable on the ten or so runs a line provides and only
    reached 4.7. The distribution is unimodal, so neither method had anything
    to find.
    """
    return max(3, int(round(lineh * (SWEEP_DEFAULT if ratio is None else ratio))))


def words_of(band, ink=120, ratio=None):
    """Word images in one line band, right to left (reading order)."""
    col = (band < ink).sum(axis=0)
    runs, inG, st = [], False, 0
    for i, v in enumerate(col):
        if v == 0 and not inG:
            inG, st = True, i
        elif v != 0 and inG:
            inG = False
            runs.append((st, i))
    if inG:
        runs.append((st, len(col)))
    cut = word_gap(None, band.shape[0], ratio)
    # split the line at every blank run at least `cut` wide
    bounds, prev = [], 0
    for a, b in runs:
        if b - a >= cut:
            if a > prev:
                bounds.append((prev, a))
            prev = b
    if prev < len(col):
        bounds.append((prev, len(col)))
    out = []
    for a, b in bounds:
        if b - a < 3:
            continue
        w = band[:, a:b]
        if (w < ink).sum() < 6:
            continue
        out.append(w)
    return out[::-1]          # the codex reads right to left


def normalise(w, h=24, maxw=96, ink=120):
    """A word image as a fixed-size binary array, trimmed and height-scaled."""
    b = (w < ink)
    rows, cols = np.where(b.any(axis=1))[0], np.where(b.any(axis=0))[0]
    if not len(rows) or not len(cols):
        return None
    t = w[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1]
    sc = h / t.shape[0]
    nw = max(3, min(maxw, int(round(t.shape[1] * sc))))
    im = Image.fromarray(t).resize((nw, h), Image.LANCZOS)
    a = (np.array(im) < ink).astype(np.uint8)
    out = np.zeros((h, maxw), dtype=np.uint8)
    out[:, :nw] = a
    return out, nw


def read_spread(path, ratio=None):
    """[(page side, [[word image, ...] per line])] for one scanned opening."""
    a = np.array(Image.open(path).convert("L"))
    out = []
    for side, p in zip(("verso", "recto"), split_spread(a)):
        sub = crop_page(p)
        if sub is None:
            out.append((side, []))
            continue
        out.append((side, [words_of(sub[max(0, s - 2):e + 2], ratio=ratio)
                           for s, e in lines_of(sub)]))
    return out


if __name__ == "__main__":
    import glob
    fs = sorted(glob.glob(os.path.join(SCAN, "nat*.png")))
    print(f"{len(fs)} spreads")
    nl = nw = npg = 0
    for f in fs[:20]:
        for side, lines in read_spread(f):
            if lines:
                npg += 1
            nl += len(lines)
            nw += sum(len(x) for x in lines)
    print(f"first 20 spreads: {npg} pages, {nl} lines, {nw} words")
    print(f"  {nl/max(1,npg):.1f} lines/page, {nw/max(1,nl):.1f} words/line")
