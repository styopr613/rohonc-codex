"""Our own outlines of the signs, traced from the manuscript's ink.

The site drew its signs from outlines taken out of Király and Tokai's font.
Those outlines are their drawing. This makes a set that is not: every curve
here comes from the scribe's ink in the scan.

HOW. For each sign code:

  1. Find it. Their outline is rasterised at the scan's scale and used ONLY as
     a search key: normalised cross-correlation over every spread, three sizes,
     and the best non-overlapping hits are kept. Nothing of the key is kept.
  2. Stack it. The best instances are cut from the scan, enlarged eight times
     and aligned to each other on their own ink, and their median is taken.
     Several instances of the scribe's hand agree where one alone is noisy.
  3. Trace it. The median is thresholded and traced by potrace. Only ink that
     is connected to the sign's centre is kept, so a neighbour touching it
     drops out; where the neighbour is joined to it, the cut is marked.
  4. Show it. A contact sheet puts the key, the instances and the trace side
     by side, so every sign is accepted by eye and not by score.

THE BAR. The first bar was set on the key: best hit at least 0.55 and 3 hits
at least 0.45. It FAILED on its first run (the site's 55 words, 2026-09-24): it
passed words whose instances were plainly different writing -- one stack mixed
"10:0" with "IIII" -- because a short key scores well against look-alikes. It
is recorded here and replaced, not quietly moved.

The bar now is agreement in the manuscript itself: a trace is ACCEPTED only
when at least 3 instances, the best one included, agree with the best one at
a correlation of 0.60 or more on their own ink, after alignment. Only the
agreeing instances are stacked. Anything else is UNSURE and is not used by the
site. A score is still not a check; the sheet is.

The 0.60 in that rule was set without measuring and also let mixed stacks
through. Measured on 13 of the site's words, 6 good by eye and 7 mixed, good
instance pairs agree at 0.69-0.88 and mixed ones at 0.52-0.66, with one pair
at 0.86 in a stack whose other pair is 0.64. The line is now 0.70. It was
picked on those same words, so it is a working setting, not a tested one:
the sheet stays the gate.

Source: the low-resolution scan (DATA_PROVENANCE.md section 3), analysed
locally. The scan is not redistributed; the traces are new drawings of
sixteenth-century shapes.

    python3 kttrace.py --codes 060,131,...     trace these signs
    python3 kttrace.py --site                  the signs the site draws
    python3 kttrace.py --all                   every sign in signs.json
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw

import corpus

ROOT = corpus.ROOT
SCAN = os.path.join(ROOT, "data", "rohonc", "scan")
SIGNS = os.path.join(ROOT, "work", "rohonc", "signs.json")
OUTDIR = os.path.join(ROOT, "work", "rohonc", "trace")
OUT = os.path.join(ROOT, "work", "rohonc", "ourSigns.json")

SCALES = (0.018, 0.021, 0.024)     # scan px per font unit; median glyph 600u ~ 13px
TOPK = 8                            # instances stacked
UP = 8                              # enlargement before tracing
ACCEPT_BEST, ACCEPT_N, ACCEPT_NS = 0.55, 3, 0.45


# ---- their outline, rasterised as a search key -------------------------------

def _subpaths(d):
    toks = re.findall(r"[MCLHVZ]|-?\d+(?:\.\d+)?", d)
    subs, cur, x, y, i, cmd = [], [], 0.0, 0.0, 0, None
    while i < len(toks):
        t = toks[i]
        if t.isalpha():
            cmd = t
            i += 1
            if cmd == "Z":
                if cur:
                    subs.append(cur)
                cur = []
            continue
        if cmd == "M":
            if cur:
                subs.append(cur)
            x, y = float(toks[i]), float(toks[i + 1])
            cur = [(x, y)]
            i += 2
            cmd = "L"
        elif cmd == "L":
            x, y = float(toks[i]), float(toks[i + 1])
            cur.append((x, y))
            i += 2
        elif cmd == "H":
            x = float(toks[i])
            cur.append((x, y))
            i += 1
        elif cmd == "V":
            y = float(toks[i])
            cur.append((x, y))
            i += 1
        elif cmd == "C":
            x1, y1, x2, y2, x3, y3 = map(float, toks[i:i + 6])
            for k in range(1, 13):
                u = k / 12
                cur.append(((1 - u) ** 3 * x + 3 * (1 - u) ** 2 * u * x1 + 3 * (1 - u) * u * u * x2 + u ** 3 * x3,
                            (1 - u) ** 3 * y + 3 * (1 - u) ** 2 * u * y1 + 3 * (1 - u) * u * u * y2 + u ** 3 * y3))
            x, y = x3, y3
            i += 6
        else:
            i += 1
    if cur:
        subs.append(cur)
    return subs


def compose(code, sg):
    """A word's key: its signs laid RIGHT TO LEFT, as the site lays them.
    A word is far more distinctive than one sign: a lone stroke matches any
    look-alike on the page, a run of three matches only itself."""
    gl = [sg[code[i:i + 3]] for i in range(0, len(code), 3) if code[i:i + 3] in sg]
    x, subs = sum(g["w"] for g in gl), []
    for g in gl:
        x -= g["w"]
        subs += [[(px + x, py) for px, py in sp] for sp in _subpaths(g["d"])]
    xs = [p[0] for sp in subs for p in sp]
    ys = [p[1] for sp in subs for p in sp]
    return {"subs": subs, "b": [min(xs), min(ys), max(xs), max(ys)]}


def key(g, s, ss=4):
    """Their outline at s px/unit, even-odd filled, 0..1, with a 2px margin."""
    x0, y0, x1, y1 = g["b"]
    W = max(3, int(np.ceil((x1 - x0) * s)) + 4)
    H = max(3, int(np.ceil((y1 - y0) * s)) + 4)
    acc = np.zeros((H * ss, W * ss), bool)
    for sp in (g["subs"] if "subs" in g else _subpaths(g["d"])):
        m = Image.new("1", (W * ss, H * ss), 0)
        pts = [((px - x0) * s * ss + 2 * ss, (y1 - py) * s * ss + 2 * ss) for px, py in sp]
        if len(pts) > 2:
            ImageDraw.Draw(m).polygon(pts, fill=1)
        acc ^= np.array(m, bool)
    return acc.reshape(H, ss, W, ss).mean(axis=(1, 3))


# ---- the scan -----------------------------------------------------------------

def spreads():
    fs = sorted(glob.glob(os.path.join(SCAN, "nat-*.png")))
    out = []
    for f in fs:
        a = np.array(Image.open(f).convert("L")).astype(np.float32)
        out.append((os.path.basename(f), a))
    return out


def inkmap(a):
    return np.clip((185.0 - a) / 110.0, 0, 1).astype(np.float32)


def boxsum(a, h, w):
    c = np.pad(a, ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    return c[h:, w:] - c[:-h, w:] - c[h:, :-w] + c[:-h, :-w]


def search(codes, sg):
    """Best hits for each code across every spread: {code: [(score, file, y, x, h, w, s)]}"""
    sp = spreads()
    Hs = max(a.shape[0] for _, a in sp)
    Ws = max(a.shape[1] for _, a in sp)
    keys = {}
    for c in codes:
        for s in SCALES:
            k = key(sg[c], s)
            if k.sum() < 4:
                continue
            kz = k - k.mean()
            n = np.sqrt((kz ** 2).sum())
            if n == 0:
                continue
            keys[(c, s)] = (kz / n, k.shape)
    FH, FW = Hs + 64, Ws + 96
    kf = {ck: np.fft.rfft2(np.flipud(np.fliplr(kz)), (FH, FW)).astype(np.complex64)
          for ck, (kz, _) in keys.items()}
    hits = {c: [] for c in codes}
    for fi, (fname, a) in enumerate(sp):
        I = inkmap(a)
        If = np.fft.rfft2(I, (FH, FW)).astype(np.complex64)
        for (c, s), (kz, (h, w)) in keys.items():
            full = np.fft.irfft2(If * kf[(c, s)], (FH, FW))
            num = full[h - 1:I.shape[0], w - 1:I.shape[1]]
            S1 = boxsum(I, h, w)
            S2 = boxsum(I * I, h, w)
            hw = h * w
            var = S2 - S1 * S1 / hw
            ncc = num / np.sqrt(np.maximum(var, 1e-6))
            # Only a window that looks like writing can match: some ink but not
            # a slab of it, and real contrast. Flat margins and the black border
            # around the book otherwise divide by nearly nothing and win.
            m = S1 / hw
            ncc[(m < 0.06) | (m > 0.6) | (var < 0.04 * hw)] = 0
            for _ in range(4):
                y, x = np.unravel_index(np.argmax(ncc), ncc.shape)
                v = float(ncc[y, x])
                if v < 0.35:
                    break
                hits[c].append((v, fname, int(y), int(x), h, w, s))
                ncc[max(0, y - h // 2):y + h // 2 + 1, max(0, x - w // 2):x + w // 2 + 1] = 0
        if fi % 20 == 0:
            print(f"  searched {fi + 1}/{len(sp)} spreads", file=sys.stderr)
    for c in codes:
        hits[c].sort(reverse=True)
    return hits


# ---- stack and trace ------------------------------------------------------------

def dedupe(hl):
    """One place on one page is one copy. The search runs at three sizes and
    the same word can win at two of them a pixel apart; counted twice, it
    agreed with itself (285 on nat-119, found 2026-09-24)."""
    out = []
    for h in sorted(hl, reverse=True):
        v, f, y, x, hh, ww, s = h
        if any(f == o[1] and abs(y - o[2]) < max(hh, o[4]) / 2 and abs(x - o[3]) < max(ww, o[5]) / 2 for o in out):
            continue
        out.append(h)
    return out


def crops(hitlist, cache):
    out = []
    for v, fname, y, x, h, w, s in hitlist:
        a = cache[fname]
        m = 3
        y0, x0 = max(0, y - m), max(0, x - m)
        c = a[y0:y + h + m, x0:x + w + m]
        if c.shape[0] < h or c.shape[1] < w:
            continue
        big = Image.fromarray(c.astype(np.uint8)).resize((c.shape[1] * UP, c.shape[0] * UP), Image.BICUBIC)
        out.append((v, np.array(big).astype(np.float32)))
    return out


def align(ref, im, r=2 * UP):
    """Shift im to best match ref on ink, within +-r px."""
    A, B = 255 - ref, 255 - im
    H = min(A.shape[0], B.shape[0])
    W = min(A.shape[1], B.shape[1])
    A, B = A[:H, :W], B[:H, :W]
    best, bd = -1e18, (0, 0)
    for dy in range(-r, r + 1, 2):
        for dx in range(-r, r + 1, 2):
            v = (A * np.roll(np.roll(B, dy, 0), dx, 1)).sum()
            if v > best:
                best, bd = v, (dy, dx)
    return np.roll(np.roll(im[:H, :W], bd[0], 0), bd[1], 1)


AGREE, AGREE_N = 0.70, 3


def agreeing(cs):
    """The instances that agree with the best one on their own ink, aligned."""
    ref = cs[0][1]
    out = [(1.0, ref)]
    for v, im in cs[1:]:
        a = align(ref, im)
        H = min(ref.shape[0], a.shape[0])
        W = min(ref.shape[1], a.shape[1])
        A = (255 - ref[:H, :W]).ravel()
        B = (255 - a[:H, :W]).ravel()
        A, B = A - A.mean(), B - B.mean()
        r = float((A * B).sum() / np.sqrt((A * A).sum() * (B * B).sum() + 1e-9))
        if r >= AGREE:
            out.append((r, a))
    return out


def stack(cs):
    al = [im for _, im in cs]
    H = min(a.shape[0] for a in al)
    W = min(a.shape[1] for a in al)
    return np.median(np.stack([a[:H, :W] for a in al]), axis=0)


def centre_ink(med, thr=105):
    from scipy import ndimage as nd
    ink = med < thr
    lab, n = nd.label(ink)
    if n == 0:
        return ink, False
    H, W = ink.shape
    cy, cx = H / 2, W / 2
    keep = np.zeros(n + 1, bool)
    sizes = nd.sum(ink, lab, range(n + 1))
    coms = nd.center_of_mass(ink, lab, range(1, n + 1))
    for i, (yy, xx) in enumerate(coms, 1):
        inside = (0.12 * H < yy < 0.88 * H) and (0.10 * W < xx < 0.90 * W)
        if inside and sizes[i] > 0.01 * sizes[1:].sum():
            keep[i] = True
    out = keep[lab]
    touches = bool(out[:, :2].any() or out[:, -2:].any())
    return out, touches


def potrace_path(mask):
    """Trace a boolean mask; return an SVG path in mask pixels, y down."""
    with tempfile.TemporaryDirectory() as td:
        pb = os.path.join(td, "m.pbm")
        Image.fromarray((~mask).astype(np.uint8) * 255).convert("1").save(pb)
        sv = os.path.join(td, "m.svg")
        subprocess.run(["potrace", "-s", "--flat", "-a", "1.1", "-O", "0.4", "-t", "40",
                        "-u", "1", pb, "-o", sv], check=True)
        t = open(sv).read()
    ds = re.findall(r'<path d="([^"]+)"', t)
    return " ".join(ds), mask.shape


def to_units(d, shape, g, sc):
    """potrace's -u 1 path (y up from the bottom, relative commands) -> absolute units, upm 1000.

    The crop is the search window plus 3px, and the window was the key plus 2px,
    so the ink is placed in the same frame the key was found in: signs of one
    word then sit on one line when they are drawn side by side."""
    H, W = shape
    s = 1.0 / (sc * UP)                 # font units per enlarged pixel
    ox = g["b"][0] - 5 / sc             # unit x of the crop's left edge
    oy = g["b"][1] - 5 / sc             # unit y of the crop's bottom edge
    toks = re.findall(r"[mlcMLCzZ]|-?\d+(?:\.\d+)?", d)
    out, x, y, i, cmd, start = [], 0.0, 0.0, 0, None, (0.0, 0.0)
    def P(px, py):
        return f"{round(ox + px * s)} {round(oy + py * s)}"
    while i < len(toks):
        t = toks[i]
        if t in "mlcMLCzZ" and not t.lstrip("-").replace(".", "").isdigit():
            cmd = t
            i += 1
            if cmd in "zZ":
                out.append("Z")
                x, y = start
            continue
        if cmd in "mM":
            dx, dy = float(toks[i]), float(toks[i + 1])
            x, y = (x + dx, y + dy) if cmd == "m" else (dx, dy)
            start = (x, y)
            out.append("M" + P(x, y))
            i += 2
            cmd = "l" if cmd == "m" else "L"
        elif cmd in "lL":
            dx, dy = float(toks[i]), float(toks[i + 1])
            x, y = (x + dx, y + dy) if cmd == "l" else (dx, dy)
            out.append("L" + P(x, y))
            i += 2
        elif cmd in "cC":
            v = list(map(float, toks[i:i + 6]))
            if cmd == "c":
                pts = [(x + v[0], y + v[1]), (x + v[2], y + v[3]), (x + v[4], y + v[5])]
            else:
                pts = [(v[0], v[1]), (v[2], v[3]), (v[4], v[5])]
            out.append("C" + " ".join(P(*p) for p in pts))
            x, y = pts[2]
            i += 6
        else:
            i += 1
    path = "".join(out)
    nums = [float(n) for n in re.findall(r"-?\d+", path)]
    xs, ys = nums[0::2], nums[1::2]
    b = [int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys))] if xs else [0, 0, 0, 0]
    return path, b, b[2] + 30


def sheet(rows, path):
    """Contact sheet: key | top instances | stacked median | trace."""
    cell = 64
    img = Image.new("L", (cell * 9 + 80, cell * len(rows) + 4), 255)
    dr = ImageDraw.Draw(img)
    for r, (code, k, insts, med, mask, status, best) in enumerate(rows):
        y = r * cell + 2
        dr.text((2, y + 2), code, fill=0)
        dr.text((2, y + 16), status[:6], fill=0)
        dr.text((2, y + 30), f"agree {best}", fill=0)
        tiles = [255 - (k * 255)] + [im for _, im in insts[:5]] + [med, np.where(mask, 0, 255)]
        for j, t in enumerate(tiles):
            t = np.asarray(t, np.float32)
            im = Image.fromarray(np.clip(t, 0, 255).astype(np.uint8))
            im.thumbnail((cell - 4, cell - 4))
            img.paste(im, (80 + j * cell + 2, y + 2))
    img.save(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--codes")
    ap.add_argument("--site", action="store_true")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--words", action="store_true", help="trace the site's whole words, not single signs")
    ap.add_argument("--sitecodes", default=os.path.join(ROOT, "work", "rohonc", "sitecodes.txt"))
    args = ap.parse_args()
    sg = json.load(open(SIGNS, encoding="utf-8"))["signs"]
    if args.codes:
        codes = args.codes.split(",")
    elif args.words:
        codes = sorted(w for w in set(open(args.sitecodes).read().split())
                       if len(w) % 3 == 0 and all(w[i:i + 3] in sg for i in range(0, len(w), 3)))
        base, sg = sg, dict(sg)
        for w in codes:
            sg[w] = compose(w, base)
    elif args.site:
        words = open(args.sitecodes).read().split()
        codes = sorted({w[i:i + 3] for w in words for i in range(0, len(w), 3)} & set(sg))
    elif args.all:
        codes = sorted(sg)
    else:
        ap.error("say which signs")
    os.makedirs(OUTDIR, exist_ok=True)
    print(f"tracing {len(codes)} signs", file=sys.stderr)
    hp = os.path.join(OUTDIR, "hits.json")
    old = json.load(open(hp)) if os.path.exists(hp) else {}
    need = [c for c in codes if c not in old]
    if need:
        old.update(search(need, sg))
        json.dump(old, open(hp, "w"))
    hits = {c: dedupe([tuple(h) for h in old[c]]) for c in codes}
    cache = {f: a for f, a in spreads()}
    done = json.load(open(OUT)) if os.path.exists(OUT) else {"upm": 1000, "signs": {}}
    rows = []
    for c in codes:
        hl = hits[c][:TOPK]
        if hl:                           # stack only instances found at the best hit's size
            hl = [h for h in hl if h[6] == hl[0][6]]
        best = hl[0][0] if hl else 0.0
        n_ok = sum(1 for h in hl if h[0] >= ACCEPT_NS)
        cs = crops(hl, cache)
        if not cs:
            rows.append((c, key(sg[c], SCALES[1]), [], np.full((8, 8), 255.0), np.zeros((8, 8), bool), "NONE", 0.0))
            continue
        ag = agreeing(cs)
        med = stack(ag[:5])
        mask, cut = centre_ink(med)
        n_ok = len(ag)
        status = "ACCEPTED" if n_ok >= AGREE_N else "UNSURE"
        cs = ag
        if mask.any():
            d, shape = potrace_path(mask)
            path, b, w = to_units(d, shape, sg[c], hl[0][6])
            done["signs"][c] = {"d": path, "w": w, "b": b, "status": status, "cut": cut,
                                "best": round(best, 3), "n": n_ok,
                                "from": [f"{h[1]}@{h[2]},{h[3]}" for h in hl[:5]]}
        rows.append((c, key(sg[c], hl[0][6]), cs, med, mask, status, n_ok))
    json.dump(done, open(OUT, "w"), indent=0)
    for i in range(0, len(rows), 30):
        sheet(rows[i:i + 30], os.path.join(OUTDIR, f"sheet-{i // 30:03d}.png"))
    acc = sum(1 for r in rows if r[5] == "ACCEPTED")
    print(f"kttrace: {len(rows)} signs, {acc} accepted, {len(rows) - acc} unsure; sheets in {OUTDIR}")


if __name__ == "__main__":
    sys.exit(main())


# ---- deep stacking: many copies of one sign ------------------------------------

DEEP_N, DEEP_ROUNDS = 60, 3


def _r(a, b):
    A = (255 - a).ravel() - (255 - a).mean()
    B = (255 - b).ravel() - (255 - b).mean()
    return float((A * B).sum() / np.sqrt((A * A).sum() * (B * B).sum() + 1e-9))


def deep(hitlist, cache, n=DEEP_N, anchor=0.72, cap=None):
    """Stack up to n copies of one sign.

    The first run of this let the median wander: each round compared copies
    with the previous round's median, so a common look-alike pulled it over
    (4b0 became a plain H, a79 became o:o, 6a6 became O; 2026-09-24). Now a
    copy is judged against the SEED -- the median of the best copies that
    agree with each other, which is what kttrace already confirmed -- in every
    round, and only aligned to the current median. The seed never moves.
    A sign can never have more agreeing copies than the book has of it: with
    `cap`, only the `cap` copies that agree best are kept (a79 occurs 27 times
    and 49 copies "agreed", so 22 at least were another sign).
    Returns (median, copies kept, copies tried)."""
    hl = dedupe(hitlist)
    if not hl:
        return None, 0, 0
    s0 = hl[0][6]
    hl = [h for h in hl if h[6] == s0][:n]
    cp = crops(hl, cache)
    if not cp:
        return None, 0, 0
    H = min(c.shape[0] for _, c in cp)
    W = min(c.shape[1] for _, c in cp)
    cp = [(v, c[:H, :W]) for v, c in cp]
    seed = stack(agreeing(cp[:TOPK])[:5])[:H, :W]
    Hs, Ws = seed.shape
    ref, keep = seed, [seed]
    for _ in range(DEEP_ROUNDS):
        kept = []
        for _, c in cp:
            a = align(ref, c)[:Hs, :Ws]
            r = _r(seed, a)
            if r >= anchor:
                kept.append((r, a))
        kept = [a for _, a in sorted(kept, key=lambda t: -t[0])[:cap]]
        if len(kept) < 2:
            break
        keep = kept
        ref = np.median(np.stack(keep), axis=0)
    return ref, len(keep), len(cp)


def copy_is(code, img, allk, boxed, iou, margin=0.02):
    """Does this one copy look like `code` more than like any other sign?
    Variants of a sign in their font share the first two hex digits
    (ae0/ae1, 7e6/7e7) and count as the same sign here."""
    thr = otsu(img)
    ink, _ = centre_ink(img, thr)
    if not ink.any():
        return False
    b = boxed(ink)
    own = max(iou(b, k) for o, k in allk.items() if o[:2] == code[:2])
    rival = max(iou(b, k) for o, k in allk.items() if o[:2] != code[:2])
    return own >= rival - margin


def deep_checked(hitlist, cache, code, allk, boxed, iou, n=DEEP_N, cap=None):
    """deep(), but every copy must first pass copy_is(): the stack is made
    only of copies that look like their own sign. The owner's eye on the
    picker found signs where two of three copies were right and one was a
    look-alike; this does that check on every copy (2026-09-24)."""
    hl = dedupe(hitlist)
    if not hl:
        return None, 0, 0
    s0 = hl[0][6]
    hl = [h for h in hl if h[6] == s0][:n * 2]
    good = []
    for h in hl:
        cp = crops([h], cache)
        if cp and copy_is(code, cp[0][1], allk, boxed, iou):
            good.append(h)
        if len(good) >= n:
            break
    med, kept, tried = deep(good, cache, n=n, cap=cap)
    return med, kept, len(hl)


def otsu(a):
    h, _ = np.histogram(a, 256, (0, 256))
    p = h / max(1, h.sum())
    best, t = -1, 128
    for k in range(1, 255):
        w0 = p[:k].sum()
        w1 = 1 - w0
        if w0 == 0 or w1 == 0:
            continue
        m0 = (np.arange(k) * p[:k]).sum() / w0
        m1 = (np.arange(k, 256) * p[k:]).sum() / w1
        v = w0 * w1 * (m0 - m1) ** 2
        if v > best:
            best, t = v, k
    return t
