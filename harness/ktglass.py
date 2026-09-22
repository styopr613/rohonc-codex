#!/usr/bin/env python3
"""Generate the magnifying glass that sits over the sign strip, with Seedream
on DeepInfra, and cut it into an asset the page can use.

The lens must end up EMPTY -- a transparent hole -- because the page shows the
magnified sign through it. So the prompt asks for a bare rim on a flat white
field, seen straight on, and the cutter below floods white to transparent from
the corners and from the middle of the lens. Whatever circle that leaves is
measured, not assumed: the page's clip circle is written from the measurement.

    python3 ktglass.py --gen            # four candidates, ~5 cents each
    python3 ktglass.py --cut FILE       # cut one to work/rohonc/glass.png
"""
import argparse, base64, json, os, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "work", "rohonc", "glass")
KEY = open("/opt/secrets/deepinfra_api_key").read().strip()
URL = "https://api.deepinfra.com/v1/inference/ByteDance/Seedream-5.0-Pro"

COMMON = ("Seen perfectly straight on, face on, not at an angle. The lens is EMPTY: "
          "there is no glass in it, no reflection, no tint, no shine on the lens, "
          "you see the plain white background through the ring. "
          "Isolated on a pure flat pure white background, no shadow, no gradient, "
          "no table, no hand, nothing else in the frame. The whole object fits "
          "inside the frame with a margin. Sharp, clean edges.")

PROMPTS = {
    "brass": "An antique brass magnifying glass. A thick round brass rim and a short "
             "turned brass handle leaving the rim at the lower right at 45 degrees. "
             "Warm polished brass, aged, fine engraved detail on the rim. " + COMMON,
    "scholar": "A 17th century scholar's magnifying glass with a dark stained wood "
               "handle and an aged bronze rim, the handle at the lower right at 45 "
               "degrees, short. Museum object photograph. " + COMMON,
    "ink": "A magnifying glass drawn as a 16th century woodcut in sepia brown ink on "
           "white, cross-hatched engraving lines, a plain round rim and a short "
           "handle at the lower right at 45 degrees. " + COMMON,
    "gilt": "A magnifying glass with a slender gilt gold rim and a slim dark handle at "
            "the lower right at 45 degrees, elegant, minimal, antiquarian. " + COMMON,
}


def gen(names, size="1024x1024"):
    os.makedirs(DIR, exist_ok=True)
    for name in names:
        body = json.dumps({"prompt": PROMPTS[name], "size": size,
                           "output_format": "png"}).encode()
        req = urllib.request.Request(URL, body, {
            "Authorization": "bearer " + KEY, "Content-Type": "application/json"})
        d = json.load(urllib.request.urlopen(req, timeout=300))
        imgs = d.get("images") or d.get("output") or []
        if not imgs:
            print(name, "no image; keys:", list(d)); continue
        raw = imgs[0]
        if raw.startswith("data:"):
            raw = raw.split(",", 1)[1]
            blob = base64.b64decode(raw)
        elif raw.startswith("http"):
            blob = urllib.request.urlopen(raw, timeout=300).read()
        else:
            blob = base64.b64decode(raw)
        p = os.path.join(DIR, name + ".png")
        open(p, "wb").write(blob)
        print("wrote", p, len(blob), "bytes")




# ---- cutting -----------------------------------------------------------------------
# Run this part with /usr/bin/python3: it needs numpy and PIL, and nothing else.

def _flood(mask, seeds):
    """Scanline flood fill over a boolean array. Rows are cut with numpy rather
    than walked pixel by pixel, which is the difference between a second and a
    minute on a 1024-square image."""
    import numpy as np
    h, w = mask.shape
    out = np.zeros_like(mask)
    stack = [(int(x), int(y)) for x, y in seeds]
    while stack:
        x, y = stack.pop()
        if not mask[y, x] or out[y, x]:
            continue
        free = mask[y] & ~out[y]
        blocked = np.flatnonzero(~free)
        lo = blocked[blocked < x]
        hi = blocked[blocked > x]
        x1 = int(lo[-1]) + 1 if lo.size else 0
        x2 = int(hi[0]) - 1 if hi.size else w - 1
        out[y, x1:x2 + 1] = True
        for ny in (y - 1, y + 1):
            if 0 <= ny < h:
                run = mask[ny, x1:x2 + 1] & ~out[ny, x1:x2 + 1]
                idx = np.flatnonzero(run)
                if idx.size:
                    starts = idx[np.concatenate(([True], np.diff(idx) > 1))]
                    for s in starts:
                        stack.append((x1 + int(s), ny))
    return out


def _grow(mask, n=2):
    import numpy as np
    m = mask.copy()
    for _ in range(n):
        g = m.copy()
        g[1:, :] |= m[:-1, :]; g[:-1, :] |= m[1:, :]
        g[:, 1:] |= m[:, :-1]; g[:, :-1] |= m[:, 1:]
        m = g
    return m


def cut(src, tol=30, soft=(8, 30)):
    """Key the flat background and the empty lens to transparency, then MEASURE
    the lens rather than assume it. The page's clip circle is written from these
    numbers, so a different picture with a different rim needs no CSS edited."""
    import numpy as np
    from PIL import Image
    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    h, w, _ = a.shape
    edge = np.concatenate([a[:6].reshape(-1, 3), a[-6:].reshape(-1, 3),
                           a[:, :6].reshape(-1, 3), a[:, -6:].reshape(-1, 3)])
    bg = np.median(edge, axis=0)
    dist = np.abs(a - bg).max(axis=2)
    near = dist <= tol

    outside = _flood(near, [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)])
    rest = near & ~outside
    # every enclosed background-coloured region; the biggest is the lens
    holes, seen = [], np.zeros_like(near)
    ys, xs = np.nonzero(rest)
    for y, x in zip(ys, xs):
        if seen[y, x]:
            continue
        c = _flood(rest & ~seen, [(x, y)])
        seen |= c
        holes.append(c)
    if not holes:
        raise SystemExit("no enclosed hole found: is the lens filled in?")
    lens = max(holes, key=lambda c: int(c.sum()))
    ly, lx = np.nonzero(lens)
    x0, x1, y0, y1 = int(lx.min()), int(lx.max()), int(ly.min()), int(ly.max())
    area = int(lens.sum())
    r_box = ((x1 - x0 + 1) + (y1 - y0 + 1)) / 4.0
    r_area = (area / 3.141592653589793) ** 0.5
    round_err = abs(r_box - r_area) / r_box

    # The hole is a circle, so clear the WHOLE circle, not only the pixels that
    # happened to match the background. The brass candidate kept a faint painted
    # glass tint inside its rim, and it showed as a grey smudge over the sign.
    yy, xx = np.ogrid[:h, :w]
    cxm, cym = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    inside = (xx - cxm) ** 2 + (yy - cym) ** 2 <= (r_box - 1.5) ** 2

    keyed = outside | lens | inside
    band = _grow(keyed, 2) & ~keyed
    lo, hi = soft
    sa = np.clip((dist.astype(float) - lo) / float(hi - lo), 0, 1)
    alpha = np.where(keyed, 0.0, np.where(band, sa, 1.0)) * 255.0

    rgba = np.dstack([np.asarray(im).astype(np.uint8), alpha.astype(np.uint8)])
    out = Image.fromarray(rgba, "RGBA")
    bb = out.getbbox()
    out = out.crop(bb)
    geom = {"src": os.path.basename(src), "w": out.width, "h": out.height,
            "cx": (x0 + x1) / 2.0 - bb[0], "cy": (y0 + y1) / 2.0 - bb[1],
            "r": r_box, "r_from_area": round(r_area, 2),
            "roundness_error": round(round_err, 4)}
    return out, geom


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", nargs="*", default=None,
                    help="generate candidates (needs the DeepInfra key); no names means all four")
    ap.add_argument("--size", default="1024x1024")
    ap.add_argument("--cut", default=None, help="cut one candidate to work/rohonc/glass.png")
    ap.add_argument("--name", default="glass", help="basename to write under work/rohonc/")
    a = ap.parse_args()
    if a.gen is not None:
        gen(a.gen or sorted(PROMPTS), a.size)
    if a.cut:
        img, geom = cut(a.cut)
        base = os.path.join(ROOT, "work", "rohonc", a.name)
        img.save(base + ".png")
        json.dump(geom, open(base + ".json", "w"), indent=1)
        print(json.dumps(geom, indent=1))
