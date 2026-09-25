"""Hand-drawn signs: pen strokes drawn over the scribe's ink, rendered and traced.

hand_signs.json holds the strokes (see its _how). This renders them with a
pen -- 'round' or a broad 'nib' held at 30 degrees -- at 4x, traces the result
with potrace, and writes fill outlines in the same units the site uses
(upm 1000, y up), so the site can draw them exactly as it drew the old ones.
"""
import json
import math
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

import kttrace as T

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "hand_signs.json")
SS = 4                      # render at 4x the 300px drawing frame
UNIT = 700 / 300            # 300px frame -> 700 font units tall


def densify(sp, step=1.0):
    out = []
    for (x0, y0), (x1, y1) in zip(sp, sp[1:]):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
        out += [(x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n) for k in range(n)]
    return out + [sp[-1]]


def render(spec, style, W=460, H=300):
    im = Image.new("L", (W * SS, H * SS), 0)
    d = ImageDraw.Draw(im)
    pen = spec["pen"] * SS
    if style == "nib":
        a = math.radians(30)
        hw, hh = pen * 0.62, pen * 0.22          # broad edge, thin edge
        nib = [(hw * math.cos(t) * math.cos(a) - hh * math.sin(t) * math.sin(a),
                hw * math.cos(t) * math.sin(a) + hh * math.sin(t) * math.cos(a))
               for t in np.linspace(0, 2 * math.pi, 24, endpoint=False)]
    for st in spec["strokes"]:
        closed = st[0].strip().endswith("Z")
        for sp in T._subpaths(st[0].replace("Z", "")):
            if closed:
                sp = sp + [sp[0]]
            for x, y in densify([(x * SS, y * SS) for x, y in sp], 1.5):
                if style == "nib":
                    d.polygon([(x + px, y + py) for px, py in nib], fill=255)
                else:
                    r = pen / 2
                    d.ellipse([x - r, y - r, x + r, y + r], fill=255)
    for x, y, r in spec.get("dots", []):
        R = r * SS * 0.62
        d.ellipse([x * SS - R, y * SS - R, x * SS + R, y * SS + R], fill=255)
    return np.array(im) > 127


def outline(mask):
    """Filled outline in site units: x from 0, baseline at the frame's y=240."""
    ys, xs = np.nonzero(mask)
    x0 = xs.min()
    d, shape = T.potrace_path(mask[:, x0 - 2 * SS:])
    Hm = shape[0]
    s = UNIT / SS
    import re
    toks = re.findall(r"[mlcMLCzZ]|-?\d+(?:\.\d+)?", d)
    out, x, y, i, cmd, start = [], 0.0, 0.0, 0, None, (0.0, 0.0)
    base = (Hm - 240 * SS)                      # potrace y is up from the bottom
    P = lambda px, py: f"{round(px * s + 30)} {round((py - base) * s)}"
    while i < len(toks):
        t = toks[i]
        if t in "mlcMLCzZ":
            cmd = t
            i += 1
            if t in "zZ":
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
        else:
            v = list(map(float, toks[i:i + 6]))
            pts = [(x + v[0], y + v[1]), (x + v[2], y + v[3]), (x + v[4], y + v[5])] if cmd == "c" else \
                  [(v[0], v[1]), (v[2], v[3]), (v[4], v[5])]
            out.append("C" + " ".join(P(*p) for p in pts))
            x, y = pts[2]
            i += 6
    path = "".join(out)
    nums = [float(n) for n in re.findall(r"-?\d+", path)]
    b = [int(min(nums[0::2])), int(min(nums[1::2])), int(max(nums[0::2])), int(max(nums[1::2]))]
    return {"d": path, "b": b, "w": b[2] + 40}


def main():
    spec = json.load(open(SRC))
    spec.pop("_how", None)
    out = {}
    for style in ("round", "nib"):
        out[style] = {c: outline(render(v, style)) for c, v in spec.items()}
    p = os.path.join(T.ROOT, "work", "rohonc", "handSigns.json")
    json.dump({"upm": 1000, **out}, open(p, "w"))
    print(f"ktdraw: {len(spec)} signs in 2 pen styles -> {p}")


if __name__ == "__main__":
    sys.exit(main())
