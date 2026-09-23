#!/usr/bin/env python3
"""ktmapgen.py -- the map engine behind the atlas plates (ktatlas.py).

Ported from the Plaintext Classics map engine (/opt/plaintextclassics/mapgen.py,
this project's own code, 2026-06), with three things added for a landlocked
subject: rivers, lakes, and shaded regions with a label. Real coastlines,
rivers and lakes from Natural Earth (public domain), simplified in pure
Python (Douglas-Peucker, no GIS dependencies), projected to an SVG in the
house idiom: parchment, EB Garamond, sea / terra / gold / ink.

    m = MapPlate((12, 44, 27, 50), title="...", subtitle="...")
    m.draw_land(); m.draw_rivers(); m.draw_lakes()
    m.region([(lon, lat), ...], fill, "ROYAL HUNGARY", at=(lon, lat))
    m.star(16.44, 47.31, "ROHONC"); m.city(19.04, 47.50, "Buda")
    open("out.svg", "w").write(m.render())

The plate carries a viewBox only, no width or height, so the page's CSS
scales it to the column. Type sizes are given in viewBox units; ktatlas.py
draws at 1000 wide with nothing under 20 units, because these plates are
printed at column width in a 6x9 book as well as shown on the site.

Data: data/geo/ (gitignored), see DATA_PROVENANCE.md section 8.
"""
import html
import json
import math
import os

import corpus

INK, SOFT, GOLD, TERRA, SEA = "#1b212e", "#4a5468", "#a8842f", "#b9543b", "#103b44"
PARCH = "#f6f1e7"
SEAFILL, LAND, COAST, WAVE = "#cdd9d6", "#e7d6ad", "#c2a86f", "#bccfcb"
RIVER, LAKE = "#8fb0b8", "#b9cfd2"
FONT = 'font-family="EB Garamond, Georgia, serif"'
GEO = os.path.join(corpus.ROOT, "data", "geo")
LAND_GEOJSON = os.path.join(GEO, "ne_50m_land.geojson")
RIVERS_GEOJSON = os.path.join(GEO, "ne_50m_rivers_lake_centerlines.geojson")
LAKES_GEOJSON = os.path.join(GEO, "ne_50m_lakes.geojson")


def esc(s):
    return html.escape(str(s or ""), quote=True)


# ---- Douglas-Peucker line simplification (planar, fine at this scale) ----
def _perp(p, a, b):
    ax, ay = a
    bx, by = b
    px, py = p
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def simplify(pts, tol):
    if len(pts) <= 2:
        return pts
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        i, j = stack.pop()
        dmax, idx = 0.0, -1
        for k in range(i + 1, j):
            d = _perp(pts[k], pts[i], pts[j])
            if d > dmax:
                dmax, idx = d, k
        if dmax > tol and idx != -1:
            keep[idx] = True
            stack.append((i, idx))
            stack.append((idx, j))
    return [p for p, kp in zip(pts, keep) if kp]


class MapPlate:
    def __init__(self, bbox, W=1000, H=760, margin=0, pad_top=0, title="", subtitle="", name="p"):
        # `name` keys every id in the SVG, so several plates can sit inline on one page
        self.name = name
        self.lon0, self.lat0, self.lon1, self.lat1 = bbox
        self.W, self.H, self.title, self.subtitle = W, H, title, subtitle
        latm = math.radians((self.lat0 + self.lat1) / 2)
        self.k = math.cos(latm)                    # lon compression at this latitude
        geoW = (self.lon1 - self.lon0) * self.k
        geoH = (self.lat1 - self.lat0)
        availW, availH = W - 2 * margin, H - 2 * margin - pad_top
        self.scale = min(availW / geoW, availH / geoH)
        self.ox = (W - geoW * self.scale) / 2
        self.oy = margin + pad_top + (availH - geoH * self.scale) / 2
        self._base, self._mid, self._top = [], [], []
        self._uid = 0

    def project(self, lon, lat):
        return (self.ox + (lon - self.lon0) * self.k * self.scale,
                self.oy + (self.lat1 - lat) * self.scale)

    def _inview(self, lons, lats, pad):
        bb = (self.lon0 - pad, self.lat0 - pad, self.lon1 + pad, self.lat1 + pad)
        return not (max(lons) < bb[0] or min(lons) > bb[2] or max(lats) < bb[1] or min(lats) > bb[3])

    def _path(self, ring, tol, close):
        s = simplify([(p[0], p[1]) for p in ring], tol)
        if len(s) < (3 if close else 2):
            return ""
        d = "M" + " L".join(f"{self.project(lo, la)[0]:.1f},{self.project(lo, la)[1]:.1f}" for lo, la in s)
        return d + ("Z" if close else "")

    # ---------- base: sea + real simplified land ----------
    def draw_land(self, tol=0.02, pad=0.6, waves=True):
        gj = json.load(open(LAND_GEOJSON))
        subpaths = []
        for feat in gj["features"]:
            g = feat["geometry"]
            polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
            for poly in polys:
                if not poly:
                    continue
                ring = poly[0]
                if not self._inview([p[0] for p in ring], [p[1] for p in ring], pad):
                    continue
                d = self._path(ring, tol, True)
                if d:
                    subpaths.append(d)
        self._base.append(f'<rect width="{self.W}" height="{self.H}" fill="{SEAFILL}"/>')
        if waves:
            for yy in range(int(self.oy) + 40, self.H, 48):
                self._base.append(f'<path d="M30,{yy} q34,-7 68,0 t68,0 t68,0 t68,0 t68,0 t68,0 t68,0 t68,0 t68,0 t68,0 t68,0 t68,0 t68,0 t68,0" fill="none" stroke="{WAVE}" stroke-width="1.1" opacity="0.5"/>')
        self._base.append(f'<g clip-path="url(#frame-{self.name})"><path d="{" ".join(subpaths)}" fill="{LAND}" stroke="{COAST}" stroke-width="1.3" stroke-linejoin="round"/></g>')

    def draw_rivers(self, tol=0.01, pad=0.3, max_rank=9, width=1.6, names=()):
        """Natural Earth river centrelines. `names` restricts to those rivers
        (by their `name_en` or `name` field); empty draws them all."""
        gj = json.load(open(RIVERS_GEOJSON))
        out = []
        for feat in gj["features"]:
            pr = feat.get("properties", {})
            nm = pr.get("name_en") or pr.get("name") or ""
            if names and nm not in names:
                continue
            if pr.get("scalerank", 0) and pr["scalerank"] > max_rank:
                continue
            g = feat["geometry"]
            lines = [g["coordinates"]] if g["type"] == "LineString" else g["coordinates"]
            for ln in lines:
                if not self._inview([p[0] for p in ln], [p[1] for p in ln], pad):
                    continue
                d = self._path(ln, tol, False)
                if d:
                    out.append(d)
        if out:
            self._base.append(f'<g clip-path="url(#frame-{self.name})"><path d="{" ".join(out)}" fill="none" stroke="{RIVER}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/></g>')

    def draw_lakes(self, tol=0.01, pad=0.3, min_area=None):
        gj = json.load(open(LAKES_GEOJSON))
        out = []
        for feat in gj["features"]:
            g = feat["geometry"]
            polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
            for poly in polys:
                if not poly:
                    continue
                ring = poly[0]
                if not self._inview([p[0] for p in ring], [p[1] for p in ring], pad):
                    continue
                d = self._path(ring, tol, True)
                if d:
                    out.append(d)
        if out:
            self._base.append(f'<g clip-path="url(#frame-{self.name})"><path d="{" ".join(out)}" fill="{LAKE}" stroke="{RIVER}" stroke-width="1"/></g>')

    # ---------- regions ----------
    def region(self, ring, fill, label="", at=None, opacity=0.55, hatch=False, stroke=None,
               size=18, color=None, spacing=2.5, lines=()):
        """A shaded area drawn from a hand-placed ring of lon/lat points, smoothed
        into a closed curve. It is APPROXIMATE by construction and the plate
        must say so. `lines` are extra label lines under the label."""
        pts = [self.project(lo, la) for lo, la in ring]
        d = _smooth_closed(pts)
        self._uid += 1
        fill_ref = fill
        if hatch:
            hid = f"hatch-{self.name}-{self._uid}"
            self._base.append(
                f'<defs><pattern id="{hid}" patternUnits="userSpaceOnUse" width="9" height="9" patternTransform="rotate(45)">'
                f'<line x1="0" y1="0" x2="0" y2="9" stroke="{fill}" stroke-width="2.2" opacity="{opacity}"/></pattern></defs>')
            fill_ref = f"url(#{hid})"
            opacity = 1
        st = f' stroke="{stroke}" stroke-width="1.4" stroke-dasharray="6 5"' if stroke else ' stroke="none"'
        self._mid.append(f'<g clip-path="url(#frame-{self.name})"><path d="{d}" fill="{fill_ref}" opacity="{opacity}"{st}/></g>')
        if label and at:
            x, y = self.project(*at)
            self._top.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="600" letter-spacing="{spacing}" fill="{color or INK}" text-anchor="middle">{esc(label)}</text>')
            for i, ln in enumerate(lines):
                self._top.append(f'<text x="{x:.1f}" y="{y + (i + 1) * (size * 0.95):.1f}" font-size="{size * 0.72:.1f}" font-style="italic" fill="{color or INK}" text-anchor="middle">{esc(ln)}</text>')

    # ---------- annotations ----------
    def label(self, lon, lat, text, size=18, color=None, italic=False, anchor="start", spacing=0, weight=None, dx=0, dy=0, opacity=1.0):
        x, y = self.project(lon, lat)
        self.text_xy(x + dx, y + dy, text, size, color, italic, anchor, spacing, weight, opacity)

    def text_xy(self, x, y, text, size=18, color=None, italic=False, anchor="start", spacing=0, weight=None, opacity=1.0):
        st = ' font-style="italic"' if italic else ''
        wt = f' font-weight="{weight}"' if weight else ''
        ls = f' letter-spacing="{spacing}"' if spacing else ''
        op = f' opacity="{opacity}"' if opacity != 1.0 else ''
        self._top.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color or SOFT}" text-anchor="{anchor}"{st}{wt}{ls}{op}>{esc(text)}</text>')

    def city(self, lon, lat, name, dx=11, dy=6, anchor="start", size=19, color=None, r=5, note=None):
        x, y = self.project(lon, lat)
        c = color or INK
        self._top.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}" stroke="{PARCH}" stroke-width="1.4"/>')
        self._top.append(f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-size="{size}" fill="{c}" text-anchor="{anchor}">{esc(name)}</text>')
        if note:
            self._top.append(f'<text x="{x + dx:.1f}" y="{y + dy + size * 0.85:.1f}" font-size="{size * 0.75:.1f}" font-style="italic" fill="{SOFT}" text-anchor="{anchor}">{esc(note)}</text>')

    def star(self, lon, lat, name, dx=16, dy=8, anchor="start", size=24, r=13, color=TERRA, note=None):
        x, y = self.project(lon, lat)
        pts = []
        for i in range(10):
            rr = r if i % 2 == 0 else r * 0.42
            a = -math.pi / 2 + i * math.pi / 5
            pts.append(f"{x + rr * math.cos(a):.1f},{y + rr * math.sin(a):.1f}")
        self._top.append(f'<polygon points="{" ".join(pts)}" fill="{color}" stroke="{PARCH}" stroke-width="1.6"/>')
        self._top.append(f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-size="{size}" font-weight="700" fill="{color}" text-anchor="{anchor}">{esc(name)}</text>')
        for i, ln in enumerate([note] if isinstance(note, str) else (note or [])):
            self._top.append(f'<text x="{x + dx:.1f}" y="{y + dy + size * 0.8 * (i + 1):.1f}" font-size="{size * 0.7:.1f}" font-style="italic" fill="{SOFT}" text-anchor="{anchor}">{esc(ln)}</text>')

    def arrow(self, a, b, color, width, bow=0.0, dashed=False, head=True, layer="mid", opacity=1.0):
        """Curved arrow between two lon/lat points; bow = perpendicular px offset of the control point."""
        ax, ay = self.project(*a)
        bx, by = self.project(*b)
        mx, my = (ax + bx) / 2, (ay + by) / 2
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        cx, cy = mx + nx * bow, my + ny * bow
        dash = ' stroke-dasharray="3 8"' if dashed else ''
        seg = self._mid if layer == "mid" else self._top
        seg.append(f'<path d="M{ax:.1f},{ay:.1f} Q{cx:.1f},{cy:.1f} {bx:.1f},{by:.1f}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{dash} opacity="{opacity}"/>')
        if head:
            tx, ty = bx - cx, by - cy
            tl = math.hypot(tx, ty) or 1
            ux, uy = tx / tl, ty / tl
            px, py = -uy, ux
            s = width * 1.9 + 5
            p1 = (bx, by)
            p2 = (bx - ux * s + px * s * 0.6, by - uy * s + py * s * 0.6)
            p3 = (bx - ux * s - px * s * 0.6, by - uy * s - py * s * 0.6)
            seg.append(f'<path d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{p3[0]:.1f},{p3[1]:.1f} Z" fill="{color}" opacity="{opacity}"/>')
        return (cx, cy)

    def callout(self, x, y, w, title, lines, to=None, size=17, color=TERRA):
        lh = size * 1.25
        h = size * 2.2 + len(lines) * lh + size * 0.6
        self._top.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="8" fill="{PARCH}" stroke="{color}" stroke-width="1.6" opacity="0.96"/>')
        self._top.append(f'<text x="{x + 16}" y="{y + size * 1.45:.0f}" font-size="{size * 0.9:.1f}" font-weight="700" letter-spacing="1.6" fill="{color}">{esc(title)}</text>')
        for i, ln in enumerate(lines):
            self._top.append(f'<text x="{x + 16}" y="{y + size * 2.2 + (i + 0.85) * lh:.0f}" font-size="{size}" fill="{INK}">{esc(ln)}</text>')
        if to:
            tx, ty = self.project(*to)
            sx = x + w if tx > x + w else x if tx < x else tx
            sy = y + h if ty > y + h else y if ty < y else ty
            self._top.append(f'<line x1="{sx:.0f}" y1="{sy:.0f}" x2="{tx:.0f}" y2="{ty:.0f}" stroke="{color}" stroke-width="1.3" stroke-dasharray="3 4"/>')
        return h

    def compass(self, x=None, y=None, r=24):
        x = x if x is not None else self.W - 60
        y = y if y is not None else self.oy + 70
        self._top.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{PARCH}" stroke="{SOFT}" stroke-width="1.3"/>')
        self._top.append(f'<path d="M{x},{y - r * 0.8:.0f} l5,{r * 0.8:.0f} l-5,6 l-5,-6 z" fill="{TERRA}"/>')
        self._top.append(f'<path d="M{x},{y + r * 0.8:.0f} l5,-{r * 0.8:.0f} l-5,-6 l-5,6 z" fill="{SOFT}"/>')
        self._top.append(f'<text x="{x}" y="{y - r - 6}" font-size="13" font-weight="700" fill="{SOFT}" text-anchor="middle">N</text>')

    def key(self, items, x=30, y=None, size=16, swatch="line", vertical=False):
        """A legend. swatch = line | box | hatchbox; vertical stacks the rows."""
        y = y if y is not None else self.H - 22
        cx = x
        for lab, col in items:
            if vertical and cx != x:
                cx = x
                y += size * 1.5
            if swatch == "box":
                self._top.append(f'<rect x="{cx}" y="{y - 9}" width="22" height="16" fill="{col}" opacity="0.7"/>')
            elif swatch == "hatchbox":
                self._top.append(f'<rect x="{cx}" y="{y - 9}" width="22" height="16" fill="none" stroke="{col}" stroke-width="1.4" stroke-dasharray="4 3"/>')
            else:
                self._top.append(f'<line x1="{cx}" y1="{y}" x2="{cx + 26}" y2="{y}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
            self._top.append(f'<text x="{cx + 32}" y="{y + 5}" font-size="{size}" fill="{SOFT}">{esc(lab)}</text>')
            cx += 46 + len(lab) * size * 0.5
        return cx if not vertical else y

    def raw(self, svg_fragment, layer="top"):
        {"top": self._top, "mid": self._mid, "base": self._base}[layer].append(svg_fragment)

    def render(self, credit=""):
        p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" class="mapplate" {FONT} role="img" aria-label="{esc(self.title)}">']
        p.append(f'<defs><clipPath id="frame-{self.name}"><rect width="{self.W}" height="{self.H}"/></clipPath></defs>')
        p += self._base + self._mid
        if self.title:
            p.append(f'<rect x="0" y="0" width="{self.W}" height="{int(self.oy)}" fill="{PARCH}"/>')
            p.append(f'<text x="30" y="46" font-size="30" font-weight="600" fill="{INK}">{esc(self.title)}</text>')
        if self.subtitle:
            p.append(f'<text x="30" y="76" font-size="17" font-style="italic" fill="{SOFT}">{esc(self.subtitle)}</text>')
        p += self._top
        if credit:
            p.append(f'<text x="{self.W - 14}" y="{self.H - 10}" font-size="11.5" fill="{SOFT}" text-anchor="end" opacity="0.85">{esc(credit)}</text>')
        p.append('</svg>')
        return "\n".join(p)


def _smooth_closed(pts):
    """A closed Catmull-Rom curve through the points, as an SVG path."""
    n = len(pts)
    if n < 3:
        return ""
    out = [f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"]
    for i in range(n):
        p0 = pts[(i - 1) % n]
        p1 = pts[i]
        p2 = pts[(i + 1) % n]
        p3 = pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        out.append(f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}")
    return " ".join(out) + "Z"
