#!/usr/bin/env python3
"""ktatlas.py -- the atlas: maps and timelines of where the Rohonc Codex came
out of, drawn from atlas.json.

    python3 ktatlas.py              # writes work/rohonc/atlas/*.svg, *.png, atlas.json
    python3 ktatlas.py --check      # re-renders to a scratch dir and fails if the
                                    # saved plates differ (ktatlascheck.py runs this)

Five plates, each an SVG with a viewBox only, so the site scales it to the
column, and a PNG proof at 1600 wide for image search and for looking at:

    hungary-1593      the kingdom in three parts at the proposed date read in the codex
    tongues           the languages and faiths around Rohonc, the presses, the scripts
    sources-map       where the books the codex is compiled from were written,
                      and where the witnesses this edition read it against come from
    sources-timeline  when those texts were written, ending at the proposed date 1593
    codex-timeline    the codex's own history, 1530s to now, with the attempts to read it

Idiom: the Plaintext Classics infographic plates (parchment, EB Garamond, sea /
terra / gold / ink), through ktmapgen.py. Nothing on a plate is typed twice:
every place, date and claim is in atlas.json with the line where it was read,
and ktatlascheck.py refuses an entry without one. The region rings and language
areas are hand-placed approximations and every plate that uses them says so.

Type is never smaller than 12 units on a 1000-wide plate, and labels carry the
fact, because the same PNGs can be printed at column width where nothing can be
tapped. On the site each event is a <g class="ev"> carrying data-label,
data-date and data-desc for the page's popup.
"""
import html
import json
import math
import os
import shutil
import sys
import tempfile

import corpus
import ktmapgen as M
from ktmapgen import INK, SOFT, GOLD, TERRA, SEA, PARCH, FONT, esc

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "atlas.json")
OUT = os.path.join(corpus.ROOT, "work", "rohonc", "atlas")
SIGNS = os.path.join(corpus.ROOT, "work", "rohonc", "signs.json")
BAND1, BAND2, HILITE = "#ece1c9", "#f1ead9", "#e7dcc0"
CREDIT_GEO = "Coastlines, rivers, lakes: Natural Earth (public domain). Borders and areas approximate, drawn by hand."
FAITH = {"Catholic": GOLD, "Lutheran": SEA, "Calvinist": INK, "Unitarian": "#6b8e8a",
         "Orthodox": "#9a7ba8", "Islam": TERRA}
HU_BBOX = (11.8, 44.2, 26.6, 49.8)


def data():
    return json.load(open(DATA, encoding="utf-8"))


def ll(d, name):
    return tuple(d["places"][name]["ll"])


def ev_open(label, date, desc):
    return (f'<g class="ev" tabindex="0" data-label="{esc(label)}" data-date="{esc(date)}" '
            f'data-desc="{esc(desc)}">')


# ---------------------------------------------------------------- glyphs
def glyph_row(sg, items, x, y, h, color=INK, gap=14, size=13):
    """The codex's own signs, right to left, each with its gloss beneath.
    Returns the fragment and its total width."""
    parts, cx = [], x
    for it in items:
        code = it["code"]
        gl = [sg["signs"].get(code[i:i + 3]) for i in range(0, len(code), 3)]
        gl = [g for g in gl if g]
        if not gl:
            continue
        total = sum(g["w"] for g in gl)
        y0 = min(g["b"][1] for g in gl)
        y1 = max(g["b"][3] for g in gl)
        pad = 40
        s = h / (y1 - y0 + 2 * pad)
        w = total * s
        inner, px = [], total
        for g in gl:
            px -= g["w"]
            inner.append(f'<path d="{g["d"]}" transform="translate({px} 0)"/>')
        # font units are y-up; flip, then place the baseline so the sign fills h
        parts.append(f'<g transform="translate({cx:.1f} {y + h:.1f}) scale({s:.4f} {-s:.4f}) '
                     f'translate(0 {-(y0 - pad)})" fill="{color}">{"".join(inner)}</g>')
        parts.append(f'<text x="{cx + w / 2:.1f}" y="{y + h + size + 4:.1f}" font-size="{size}" '
                     f'font-style="italic" fill="{SOFT}" text-anchor="middle">{esc(it["gloss"])}</text>')
        cx += w + gap
    return "".join(parts), cx - x - gap


# ---------------------------------------------------------------- plate 1
def plate_hungary(d):
    m = M.MapPlate(HU_BBOX, W=1000, H=780, pad_top=92, name="hu",
                   title="Hungary in 1593, on the proposed reading",
                   subtitle="A kingdom in three parts, and the town the book is named for in its Habsburg west. Borders approximate.")
    m.draw_land(tol=0.015)
    m.draw_lakes()
    m.draw_rivers(names=("Danube", "Tisza", "Tisa", "Drava"), width=1.8)
    for r in d["regions_1593"]:
        m.region(r["ring"], r["fill"], r["name"], at=r["at"], opacity=0.42, size=19,
                 lines=[r["sub"]] if r["sub"] else [])
    P = lambda n: ll(d, n)
    m.city(*P("Vienna"), "Vienna", note="the Habsburg court", anchor="end", dx=-11)
    m.city(*P("Pozsony"), "Pozsony", note="seat of Royal Hungary", dx=11, dy=-6)
    m.city(*P("Graz"), "Graz", dx=11, dy=8)
    m.city(*P("Gyor"), "Gyor", dx=10, dy=-8)
    m.city(*P("Buda"), "Buda", note="Ottoman since 1541", dx=12)
    m.city(*P("Esztergom"), "Esztergom", dx=11, dy=-8)
    m.city(*P("Eger"), "Eger", note="falls 1596", dx=11)
    m.city(*P("Kanizsa"), "Kanizsa", note="falls 1600", dx=-11, anchor="end")
    m.city(*P("Szeged"), "Szeged", dx=11)
    m.city(*P("Temesvar"), "Temesvar", dx=11)
    m.city(*P("Belgrade"), "Belgrade", dx=11)
    m.city(*P("Gyulafehervar"), "Gyulafehervar", note="the prince's seat", dx=11)
    m.city(*P("Kassa"), "Kassa", dx=11)
    m.city(*P("Zagreb"), "Zagreb", dx=-11, anchor="end")
    m.city(*P("Sisak"), "Sisak", note="battle, June 1593", dx=11, dy=10)
    m.city(*P("Venice"), "Venice", note="the paper, 1530s", dx=11, dy=-4)
    m.star(*P("Rohonc"), "ROHONC", note=["Batthyany estate", "the codex's home until 1838"], dx=-18, dy=-34, anchor="end")
    # the river names, set along the water
    m.label(18.85, 46.2, "Danube", italic=True, size=15, color="#5f8791", anchor="middle")
    m.label(20.75, 47.15, "Tisza", italic=True, size=15, color="#5f8791", anchor="middle")
    m.label(17.5, 45.75, "Drava", italic=True, size=14, color="#5f8791", anchor="middle")
    m.label(17.75, 46.75, "Balaton", italic=True, size=13, color="#5f8791", anchor="middle")
    m.label(13.0, 44.4, "Adriatic Sea", italic=True, size=17, color=SEA, anchor="middle")
    m.raw(ev_open("The proposed reading: 1593", "1593", "On Király and Tokai's reading, one of the codex's last leaves counts one thousand five hundred and sixty years from the Ascension, giving 1593. That summer the Long Turkish War began between the Habsburgs and the Ottomans, and it ran until 1606. Rohonc lay about a hundred kilometres from the frontier at Kanizsa."))
    m.callout(630, 100, 350, "1593", [
        "On Király and Tokai's reading, a last leaf",
        "counts 1,560 years from the Ascension: 1593.",
        "That summer the Long Turkish War began",
        "(1593-1606). Rohonc lay about a hundred",
        "kilometres from the frontier at Kanizsa."], size=15.5)
    m.raw("</g>")
    m.compass(x=950, y=690)
    m.key([(r["name"].title(), r["fill"]) for r in d["regions_1593"]], x=30, y=745, size=14, swatch="box")
    return m.render(credit=CREDIT_GEO)


# ---------------------------------------------------------------- plate 2
def plate_tongues(d, sg):
    t = d["tongues"]
    m = M.MapPlate(HU_BBOX, W=1000, H=800, pad_top=92, name="tg",
                   title="The tongues and faiths around Rohonc, c. 1600",
                   subtitle="Seven mapped vernaculars, six confessions, three regional scripts, and one book in a script of its own. Areas indicative, not surveyed.")
    m.draw_land(tol=0.015)
    m.draw_lakes()
    m.draw_rivers(names=("Danube", "Tisza", "Tisa", "Drava"), width=1.6)
    for a in t["areas"]:
        m.region(a["ring"], a["fill"], a["name"], at=a["at"], opacity=0.30, size=20, spacing=3.5,
                 color="#3a3f4a")
    for mk in t["marks"]:
        lon, lat = ll(d, mk["place"])
        c = FAITH[mk["faith"]]
        m.city(lon, lat, mk["label"], note=mk.get("note"), color=c, r=6, size=17,
               **({"anchor": "end", "dx": -11} if mk["place"] in ("Graz", "Zagreb", "Vienna") else {}))
    # the presses within reach of Rohonc: a small open book
    for pr in t["presses"]:
        x, y = m.project(*ll(d, pr["place"]))
        m.raw(f'<path d="M{x - 7:.1f},{y - 4:.1f} h6 v9 h-6z M{x + 1:.1f},{y - 4:.1f} h6 v9 h-6z" fill="{PARCH}" stroke="{INK}" stroke-width="1.3"/>')
        if pr["place"] == "Varasd":
            m.text_xy(x + 11, y + 4, pr["label"], size=13, color=INK, weight=600)
    m.raw(ev_open("Presses within reach", "1582-1604",
                  "Johannes Manlius, a printer, worked from 1582 on the estates of western Hungary: Varasd in 1587, Monyorokerek on the Erdody estate, Nemetlovo in 1592, where he printed Kozarvari's historical epic, Sarvar in 1602, where he printed Magyari's anti-Catholic book, and Keresztur, where he died about 1604. Nemetlovo is a dozen kilometres from Rohonc. Each little book on the map is one of his stations."))
    m.callout(30, 100, 340, "PRESSES WITHIN REACH", [
        "Manlius's travelling press, from 1582:",
        "Varasd 1587, Monyorokerek, Nemetlovo 1592",
        "(a dozen kilometres from Rohonc), Sarvar",
        "1602, Keresztur, where he died c. 1604."], size=14.5)
    m.raw("</g>")
    m.star(*ll(d, "Rohonc"), "ROHONC", dx=-18, dy=-12, anchor="end", size=22, r=12)
    m.label(13.0, 44.4, "Adriatic Sea", italic=True, size=17, color=SEA, anchor="middle")
    # inset: the codex's own script
    bx, by, bw = 596, 98, 380
    m.raw(f'<rect x="{bx}" y="{by}" width="{bw}" height="150" rx="6" fill="{PARCH}" stroke="{TERRA}" stroke-width="1.5" opacity="0.97"/>')
    m.text_xy(bx + 14, by + 24, "THE CODEX'S OWN SCRIPT", size=13.5, color=TERRA, weight=700, spacing=1.6)
    m.text_xy(bx + 14, by + 44, "Several hundred signs; code units mostly stand for words; right to left.", size=13, color=INK)
    frag, w = glyph_row(sg, t["glyphs"], bx + 18, by + 54, 40, gap=22, size=12.5)
    m.raw(frag)
    m.text_xy(bx + bw - 12, by + 140, "signs after Király and Tokai's font; glosses theirs", size=10.5, color=SOFT, italic=True, anchor="end")
    # callout: a Catholic book in a Protestant country
    m.raw(ev_open("A Catholic book in a Protestant country", "c. 1600",
                  "Around 1600 some 85 to 90 per cent of the kingdom's people were Protestant, more than half of them Calvinist. The codex is a Catholic reader: the Douay Bible's saints, the Roman Missal's feasts, the Golden Legend. Whoever wrote it belonged to a minority in the country around it."))
    m.callout(30, 628, 400, "A CATHOLIC BOOK IN A PROTESTANT COUNTRY", [
        "Around 1600 some 85-90% of the kingdom's people",
        "were Protestant, over half Calvinist. The codex",
        "is a Catholic reader: missal, Legend, Vulgate."], size=15)
    m.raw("</g>")
    # key: the confessions, then the scripts
    m.key([(f, c) for f, c in FAITH.items()], x=30, y=748, size=13.5, swatch="line")
    m.text_xy(30, 771, "Scripts represented here: Latin letters across the seven mapped vernaculars; Cyrillic for Serbian, Romanian and Church Slavonic; "
                       "Arabic letters for Ottoman Turkish; and the codex's own signs, in one book.", size=12, color=SOFT)
    return m.render(credit=CREDIT_GEO)


# ---------------------------------------------------------------- plate 3
# label placement is cartography, so it lives here and not in the data:
# (dx, dy, anchor) per place, defaults to the right of the point
LABEL_AT = {
    "Jerusalem": (-12, -46, "end"), "Alexandria": (12, -14, "start"), "Antioch": (12, -6, "start"),
    "Rome": (12, 14, "start"), "Carthage": (12, 16, "start"), "Hippo": (-12, 16, "end"),
    "Athos": (12, 14, "start"), "Tarnovo": (12, 18, "start"), "Kiev": (12, 4, "start"),
    "Montier": (-12, -4, "end"), "Genoa": (-12, 8, "end"), "Wartburg": (-12, 4, "end"),
    "Florence": (12, 12, "start"), "Trent": (-12, -4, "end"), "Wittenberg": (12, 2, "start"),
    "Douai": (-12, 2, "end"), "London": (-12, -8, "end"), "York": (-12, -6, "end"),
    "Lyon": (-12, 12, "end"), "Agreda": (12, 4, "start"), "Bucharest": (12, 12, "start"),
    "Lund": (12, 2, "start"), "Debrecen": (12, -8, "start"), "Obuda": (12, -8, "start"), "Lovold": (-10, 30, "end"),
    "Marosvasarhely": (12, 16, "start"), "Szeged": (12, 16, "start"), "Budapest": (12, 4, "start"),
}


def plate_sources_map(d):
    m = M.MapPlate((-6.5, 29.4, 40.5, 56.8), W=1000, H=780, pad_top=92, name="src",
                   title="Where the stories came from",
                   subtitle="Securely locatable books used by the codex and this edition; disputed origins are left unpinned.")
    m.draw_land(tol=0.03)
    by_place = {}
    for t in d["texts"]:
        if t.get("map", True):
            by_place.setdefault(t["place"], []).append(t)
    roh = ll(d, "Rohonc")
    bow = -1
    for pl, ts in by_place.items():
        if any(t["kind"] == "had" for t in ts) and pl not in ("Debrecen", "Lovold", "Marosvasarhely", "Budapest"):
            bow = -bow
            dist = math.hypot(ll(d, pl)[0] - roh[0], ll(d, pl)[1] - roh[1])
            m.arrow(ll(d, pl), roh, GOLD, 1.6, bow=bow * min(70, 18 + dist * 3), opacity=0.55)
    for pl, ts in by_place.items():
        lon, lat = ll(d, pl)
        x, y = m.project(lon, lat)
        kinds = {t["kind"] for t in ts}
        col = GOLD if kinds == {"had"} else SEA if kinds == {"read"} else INK
        dx, dy, anc = LABEL_AT.get(pl, (12, 4, "start"))
        label = ts[0]["place_label"] if "place_label" in ts[0] else PLACE_NAMES.get(pl, pl)
        desc = " ".join(f"{t['name']} ({t['date']}): {t['line']}." for t in ts)
        m.raw(ev_open(label, ", ".join(sorted({t["date"] for t in ts})), desc))
        m.raw(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{col}" stroke="{PARCH}" stroke-width="1.6"/>')
        m.text_xy(x + dx, y + dy, label, size=16, color=col, weight=700, anchor=anc)
        lines = [f"{t['short']}, {t['date']}" for t in ts]
        for i, ln in enumerate(lines[:3]):
            m.text_xy(x + dx, y + dy + 14 + i * 13, ln, size=12, color=INK, italic=True, anchor=anc)
        m.raw("</g>")
    m.star(*roh, "ROHONC", dx=-16, dy=-14, anchor="end", size=22, r=12)
    m.label(17.5, 34.2, "Mediterranean Sea", italic=True, size=18, color=SEA, anchor="middle")
    m.label(-4.5, 47.0, "Atlantic", italic=True, size=15, color=SEA, anchor="middle")
    m.key([("what the compiler had, written before 1593", GOLD),
           ("what this edition read it against", SEA),
           ("both", INK)], x=700, y=118, size=14, vertical=True)
    return m.render(credit="Coastlines: Natural Earth (public domain). Pins mark documented or commonly proposed places of composition; works without a defensible single place are not plotted.")


PLACE_NAMES = {"Montier": "Montier-en-Der", "Athos": "Mount Athos", "Tarnovo": "Bulgaria", "Kiev": "the Slavonic world",
               "Lovold": "Lovold", "Marosvasarhely": "Marosvasarhely", "Wartburg": "the Wartburg", "Agreda": "Agreda",
               "Douai": "Douai and Rheims", "London": "London", "Budapest": "Budapest", "Obuda": "Obuda"}


# ---------------------------------------------------------------- timelines
def _levels(items, x_of, width_of, gap=10):
    """Greedy stacking: each item gets the lowest level where its label does
    not overlap the previous label on that level."""
    right = []
    out = []
    for it in sorted(items, key=x_of):
        x0 = x_of(it) - width_of(it) / 2
        x1 = x_of(it) + width_of(it) / 2
        lvl = 0
        while lvl < len(right) and right[lvl] + gap > x0:
            lvl += 1
        if lvl == len(right):
            right.append(x1)
        else:
            right[lvl] = x1
        out.append((it, lvl))
    return out


def _tw(s, size):
    return len(s) * size * 0.48


def _star(cx, cy, r, fill):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append(f"{cx + rr * math.cos(ang):.1f},{cy + rr * math.sin(ang):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{PARCH}" stroke-width="1.4"/>'


def _label(p, x, y, text, size, fill, weight=None, anchor="middle"):
    """Text with a parchment halo behind it, so a stalk crossing a label
    cannot strike through the words."""
    w = _tw(text, size) + 8
    x0 = x - w / 2 if anchor == "middle" else x if anchor == "start" else x - w
    p.append(f'<rect x="{x0:.0f}" y="{y - size * 0.85:.0f}" width="{w:.0f}" height="{size * 1.15:.0f}" fill="{PARCH}" opacity="0.85"/>')
    wt = f' font-weight="{weight}"' if weight else ""
    p.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}"{wt} fill="{fill}">{esc(text)}</text>')


def _stalks(p, items, x_of, ax, up, size=15, first=56, step=44, label=lambda t: t["label"],
            date=lambda t: t["date"], color=lambda t: GOLD, star=lambda t: False,
            popup=lambda t: ("", "", "")):
    """Events on one side of an axis, stacked so labels do not collide.
    Items are drawn in two passes: stalks and markers first, then every label,
    so no stalk is ever drawn over a word."""
    placed = _levels(items, lambda t: x_of(t), lambda t: _tw(label(t), size) + 10)
    for t, lvl in placed:
        x = x_of(t)
        c = color(t)
        ly = (ax - first - lvl * step) if up else (ax + first + 14 + lvl * step)
        p.append(f'<line x1="{x:.0f}" y1="{ax + (-8 if up else 8)}" x2="{x:.0f}" y2="{ly + (12 if up else -28):.0f}" stroke="{c}" stroke-width="1.1"/>')
        p.append(_star(x, ax, 11, c) if star(t) else f'<circle cx="{x:.0f}" cy="{ax}" r="5" fill="{c}" stroke="{PARCH}" stroke-width="1.4"/>')
    for t, lvl in placed:
        x = x_of(t)
        c = color(t)
        ly = (ax - first - lvl * step) if up else (ax + first + 14 + lvl * step)
        lab, dt, desc = popup(t)
        p.append(ev_open(lab, dt, desc))
        _label(p, x, ly, label(t), size, TERRA if star(t) and t.get("kind") == "codex" else INK, weight=600)
        _label(p, x, ly + (-16 if up else 14), date(t), 12.5, c)
        p.append("</g>")


def plate_sources_timeline(d):
    """One axis in two stretches: AD 1 to 1250 compressed on the left, 1250 to
    1620 opened out on the right, with a marked break between them, because
    two thirds of the texts fall in the last four centuries."""
    W, H = 1000, 720
    AX = 400
    XA0, XA1 = 60, 500       # segment A: 0 - 1250
    XB0, XB1 = 540, 950      # segment B: 1250 - 1620
    def xs(y):
        if y <= 1250:
            return XA0 + y / 1250 * (XA1 - XA0)
        return XB0 + (y - 1250) / (1620 - 1250) * (XB1 - XB0)
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" class="worldtl" {FONT} role="img" aria-label="When the codex\'s sources were written">',
         f'<rect width="{W}" height="{H}" fill="{PARCH}"/>',
         f'<text x="30" y="46" font-size="30" font-weight="600" fill="{INK}">When the stories were written</text>',
         f'<text x="30" y="76" font-size="17" font-style="italic" fill="{SOFT}">Sixteen centuries of texts, and the proposed date read in the codex. The scale opens out after 1250, where most of them fall.</text>']
    bands = [(0, 500, "SCRIPTURE, FATHERS", BAND1), (500, 1250, "THE LEGENDS GROW", BAND2), (1250, 1620, "LEGENDARIES, CODICES, PRINT", BAND1)]
    for a, b, lab, fill in bands:
        p.append(f'<rect x="{xs(a):.0f}" y="100" width="{xs(b) - xs(a):.0f}" height="{H - 150}" fill="{fill}"/>')
        p.append(f'<text x="{(xs(a) + xs(b)) / 2:.0f}" y="122" text-anchor="middle" font-size="12.5" letter-spacing="1.8" fill="{SOFT}">{lab}</text>')
    p.append(f'<line x1="{XA0}" y1="{AX}" x2="{XA1}" y2="{AX}" stroke="{SEA}" stroke-width="2"/>')
    p.append(f'<line x1="{XB0}" y1="{AX}" x2="{XB1}" y2="{AX}" stroke="{SEA}" stroke-width="2"/>')
    p.append(f'<line x1="{XA1}" y1="{AX}" x2="{XB0}" y2="{AX}" stroke="{SOFT}" stroke-width="1.4" stroke-dasharray="2 6"/>')
    for bx in (XA1, XB0):
        p.append(f'<path d="M{bx - 5},{AX - 7} l6,14 M{bx + 1},{AX - 7} l6,14" stroke="{SOFT}" stroke-width="1.2" fill="none"/>')
    p.append(f'<text x="{(XA1 + XB0) / 2:.0f}" y="{AX - 14}" text-anchor="middle" font-size="10.5" letter-spacing="1" fill="{TERRA}">SCALE CHANGES</text>')
    for yr in list(range(0, 1251, 250)) + list(range(1300, 1601, 50)):
        p.append(f'<line x1="{xs(yr):.0f}" y1="{AX - 5}" x2="{xs(yr):.0f}" y2="{AX + 5}" stroke="{SEA}" stroke-width="1.2"/>')
        if yr % 250 == 0 or yr % 100 == 0:
            p.append(f'<text x="{xs(yr):.0f}" y="{AX + 22}" text-anchor="middle" font-size="12.5" fill="{SOFT}">{yr if yr else "AD 1"}</text>')
    texts = sorted([t for t in d["texts"] if t["year"] <= 1600], key=lambda t: t["year"])
    codex = {"short": "THE CODEX", "date": "proposed: 1593", "year": 1593, "kind": "codex", "name": "The codex", "line": "", "desc": "On Király and Tokai's reading, one of the codex's last leaves gives 1593. Everything on this plate that is gold was in its compiler's reach in Latin or in Hungarian by then."}
    above = [t for i, t in enumerate(texts) if i % 2 == 0]
    below = [t for i, t in enumerate(texts) if i % 2 == 1] + [codex]
    col = lambda t: TERRA if t["kind"] == "codex" else GOLD if t["kind"] == "had" else SEA
    pop = lambda t: (t["name"], t["date"], (t["desc"] + " " if t["desc"] else "") + (t["line"].capitalize() + "." if t["line"] else ""))
    kw = dict(size=15, first=54, step=42, label=lambda t: t["short"], color=col,
              star=lambda t: t["kind"] == "codex", popup=pop)
    _stalks(p, above, lambda t: xs(t["year"]), AX, True, **kw)
    _stalks(p, below, lambda t: xs(t["year"]), AX, False, **kw)
    ky = H - 22
    p.append(f'<circle cx="40" cy="{ky}" r="5" fill="{GOLD}"/><text x="52" y="{ky + 5}" font-size="14" fill="{SOFT}">what the compiler had</text>')
    p.append(f'<circle cx="250" cy="{ky}" r="5" fill="{SEA}"/><text x="262" y="{ky + 5}" font-size="14" fill="{SOFT}">what this edition read it against</text>')
    p.append(f'{_star(520, ky, 9, TERRA)}<text x="536" y="{ky + 5}" font-size="14" fill="{SOFT}">the codex, proposed date 1593</text>')
    p.append('</svg>')
    return "\n".join(p)


def plate_codex_timeline(d):
    W, H = 1000, 1040
    XL, XR = 70, 960
    ML, MR = 1520, 2032
    ZL, ZR = 1962, 2030
    xm = lambda y: XL + (y - ML) / (MR - ML) * (XR - XL)
    xz = lambda y: XL + (y - ZL) / (ZR - ZL) * (XR - XL)
    Y_MAC, Y_ZOOM = 300, 720
    BAND_T, FUNNEL_B = 100, 560
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" class="worldtl" {FONT} role="img" aria-label="The codex from the 1530s to now">',
         f'<rect width="{W}" height="{H}" fill="{PARCH}"/>',
         f'<text x="30" y="46" font-size="30" font-weight="600" fill="{INK}">The codex, from the paper to the present</text>',
         f'<text x="30" y="76" font-size="17" font-style="italic" fill="{SOFT}">Five centuries above, the last sixty years below. Above each line, the book; below it, the people who tried to read it.</text>']
    p.append(f'<rect x="{xm(ZL):.0f}" y="{BAND_T}" width="{xm(ZR) - xm(ZL):.0f}" height="{FUNNEL_B - BAND_T}" fill="{HILITE}"/>')
    p.append(f'<path d="M{xm(ZL):.0f},{FUNNEL_B} L{XL},{Y_ZOOM - 110} L{XR},{Y_ZOOM - 110} L{xm(ZR):.0f},{FUNNEL_B} Z" fill="{HILITE}" opacity="0.7"/>')
    p.append(f'<rect x="{XL}" y="{Y_ZOOM - 110}" width="{XR - XL}" height="{H - (Y_ZOOM - 110) - 44}" fill="{HILITE}"/>')
    p.append(f'<line x1="{XL}" y1="{Y_MAC}" x2="{XR}" y2="{Y_MAC}" stroke="{SEA}" stroke-width="2"/>')
    for yr in range(1550, 2031, 50):
        p.append(f'<line x1="{xm(yr):.0f}" y1="{Y_MAC - 5}" x2="{xm(yr):.0f}" y2="{Y_MAC + 5}" stroke="{SEA}" stroke-width="1.2"/>')
        if yr % 100 == 0:
            p.append(f'<text x="{xm(yr):.0f}" y="{Y_MAC + 24}" text-anchor="middle" font-size="13" fill="{SOFT}">{yr}</text>')
    p.append(f'<text x="{XL}" y="{Y_MAC - 150}" font-size="12.5" letter-spacing="1.8" fill="{SOFT}">THE BOOK</text>')
    p.append(f'<text x="{XL}" y="{Y_MAC + 175}" font-size="12.5" letter-spacing="1.8" fill="{SOFT}">THE READERS</text>')
    evs = d["events"]
    col = lambda e: GOLD if e["lane"] == "book" else SEA
    pop = lambda e: (e["label"], e["date"], e["desc"])
    kw = dict(size=15, color=col, star=lambda e: e.get("star", False), popup=pop)
    macro = [e for e in evs if e["year"] < ZL]
    _stalks(p, [e for e in macro if e["lane"] == "book"], lambda e: xm(e["year"]), Y_MAC, True, first=56, step=44, **kw)
    _stalks(p, [e for e in macro if e["lane"] == "read"], lambda e: xm(e["year"]), Y_MAC, False, first=56, step=44, **kw)
    p.append(f'<line x1="{XL}" y1="{Y_ZOOM}" x2="{XR}" y2="{Y_ZOOM}" stroke="{SEA}" stroke-width="2"/>')
    for yr in range(1970, 2031, 10):
        p.append(f'<line x1="{xz(yr):.0f}" y1="{Y_ZOOM - 5}" x2="{xz(yr):.0f}" y2="{Y_ZOOM + 5}" stroke="{SEA}" stroke-width="1.2"/>')
        p.append(f'<text x="{xz(yr):.0f}" y="{Y_ZOOM + 24}" text-anchor="middle" font-size="13" fill="{SOFT}">{yr}</text>')
    zoom = [e for e in evs if e["year"] >= ZL]
    _stalks(p, [e for e in zoom if e["lane"] == "book"], lambda e: xz(e["year"]), Y_ZOOM, True, first=50, step=40, **kw)
    _stalks(p, [e for e in zoom if e["lane"] == "read"], lambda e: xz(e["year"]), Y_ZOOM, False, first=50, step=40, **kw)
    p.append(f'<text x="{XR}" y="{Y_ZOOM - 92}" text-anchor="end" font-size="12.5" letter-spacing="1.8" fill="{SOFT}">1962-2030, ENLARGED</text>')
    ky = H - 18
    p.append(f'<circle cx="40" cy="{ky}" r="5" fill="{GOLD}"/><text x="52" y="{ky + 5}" font-size="14" fill="{SOFT}">the book itself</text>')
    p.append(f'<circle cx="200" cy="{ky}" r="5" fill="{SEA}"/><text x="212" y="{ky + 5}" font-size="14" fill="{SOFT}">attempts to read it</text>')
    p.append(f'{_star(392, ky, 9, INK)}<text x="408" y="{ky + 5}" font-size="14" fill="{SOFT}">the turns the story hangs on</text>')
    p.append('</svg>')
    return "\n".join(p)


# ---------------------------------------------------------------- build
PLATES = [
    ("hungary-1593", "Hungary in 1593", "The kingdom in three parts at the date proposed by Király and Tokai, with Rohonc in its Habsburg west."),
    ("tongues", "Tongues and faiths", "Seven mapped vernaculars, six confessions and three regional scripts around one town, and a book in a script of its own."),
    ("sources-map", "Where the stories came from", "The securely locatable books used by the codex and this edition, flowing to Rohonc."),
    ("sources-timeline", "When the stories were written", "Sixteen centuries of texts, ending at the proposed date read in the codex."),
    ("codex-timeline", "The codex, from the paper to the present", "The book above the line and the people who tried to read it below, with the last sixty years enlarged."),
]


def render_all(d, sg):
    return {
        "hungary-1593": plate_hungary(d),
        "tongues": plate_tongues(d, sg),
        "sources-map": plate_sources_map(d),
        "sources-timeline": plate_sources_timeline(d),
        "codex-timeline": plate_codex_timeline(d),
    }


def write(outdir, svgs, png=True):
    os.makedirs(outdir, exist_ok=True)
    for name, svg in svgs.items():
        open(os.path.join(outdir, name + ".svg"), "w", encoding="utf-8").write(svg)
        if png:
            import cairosvg
            cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=os.path.join(outdir, name + ".png"),
                             output_width=1600, background_color=PARCH)
    man = [{"name": n, "title": t, "caption": c} for n, t, c in PLATES]
    json.dump(man, open(os.path.join(outdir, "atlas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def main(argv):
    d = data()
    sg = json.load(open(SIGNS, encoding="utf-8"))
    svgs = render_all(d, sg)
    if "--check" in argv:
        bad = []
        for name, svg in svgs.items():
            f = os.path.join(OUT, name + ".svg")
            if not os.path.isfile(f):
                bad.append(f"{name}: not built")
            elif open(f, encoding="utf-8").read() != svg:
                bad.append(f"{name}: saved plate differs from a fresh render")
            if not os.path.isfile(os.path.join(OUT, name + ".png")):
                bad.append(f"{name}: no PNG")
        for b in bad:
            print("FAIL", b)
        print(f"ktatlas --check: {len(svgs)} plates, {len(bad)} stale")
        return 1 if bad else 0
    write(OUT, svgs)
    print(f"wrote {len(svgs)} plates to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
