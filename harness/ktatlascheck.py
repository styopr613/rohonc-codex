#!/usr/bin/env python3
"""ktatlascheck.py -- the gate on the atlas (ktatlas.py, atlas.json).

    python3 ktatlascheck.py

What it refuses, declared before it ran:

  1. An event, text, region or area in atlas.json with no `source` line, a
     missing field, an unknown place, a lane or kind outside the two allowed,
     or a glyph code that is not in signs.json.
  2. A year on the codex timeline that the book does not also state: 1593,
     1838, 2014 and 2018 must appear in the book's introduction as written in
     ktbook.py. If the book's date moves and the plate's does not, this fails.
  3. A stale plate: `ktatlas.py --check` re-renders every plate from the data
     and fails if a saved SVG differs or a PNG is missing. A gate that reads a
     generated file must regenerate it, or it agrees with itself.
  4. A saved SVG that does not parse as XML, or that carries a duplicate id
     (five plates sit inline on one page).
  5. A site copy key the Atlas page needs that is not in ktsite_copy.json.
  6. A regression to the factual errors corrected in the 2026-09-23 audit:
     pages called folios, glossed dictionary codes called signs, the Missal and
     Martyrology given one date, or disputed origins plotted as certain.
"""
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

import corpus

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(corpus.ROOT, "work", "rohonc", "atlas")
FAITHS = {"Catholic", "Lutheran", "Calvinist", "Unitarian", "Orthodox", "Islam"}
BOOK_YEARS = {"1593": r"which is 1593", "1838": r"in 1838", "2014": r"published in 2014",
              "2018": r"In 2018"}


def main():
    fails = []
    d = json.load(open(os.path.join(HERE, "atlas.json"), encoding="utf-8"))
    sp = os.path.join(corpus.ROOT, "work", "rohonc", "signs.json")
    if not os.path.exists(sp):
        # A local working file made from Király and Tokai's font; see .gitignore.
        print("signs.json is missing: run ktsigns.py first (it reads their font from data/)")
        return 1
    sg = json.load(open(sp, encoding="utf-8"))["signs"]
    places = d["places"]
    for i, e in enumerate(d["events"]):
        for k in ("year", "date", "lane", "label", "desc", "source"):
            if not e.get(k):
                fails.append(f"event {i} ({e.get('label', '?')}): no {k}")
        if e.get("lane") not in ("book", "read"):
            fails.append(f"event {e.get('label')}: lane {e.get('lane')!r}")
    for t in d["texts"]:
        for k in ("name", "place", "year", "date", "kind", "line", "source", "short"):
            if k not in t or t[k] in (None, ""):
                if not (k == "line" and t.get("kind") == "read"):
                    fails.append(f"text {t.get('name', '?')}: no {k}")
        if t.get("place") not in places:
            fails.append(f"text {t.get('name')}: unknown place {t.get('place')!r}")
        if t.get("kind") not in ("had", "read"):
            fails.append(f"text {t.get('name')}: kind {t.get('kind')!r}")
    for r in d["regions_1593"]:
        if len(r.get("ring", [])) < 3 or not r.get("source") or not r.get("at"):
            fails.append(f"region {r.get('name')}: ring, source or label point missing")
    tg = d["tongues"]
    for a in tg["areas"]:
        if len(a.get("ring", [])) < 3 or not a.get("at"):
            fails.append(f"area {a.get('name')}: ring or label point missing")
    for k in ("areas_source", "marks_source", "presses_source", "glyphs_source"):
        if not tg.get(k):
            fails.append(f"tongues: no {k}")
    for m in tg["marks"]:
        if m["place"] not in places:
            fails.append(f"mark {m['label']}: unknown place")
        if m["faith"] not in FAITHS:
            fails.append(f"mark {m['label']}: faith {m['faith']!r}")
    for p in tg["presses"]:
        if p["place"] not in places:
            fails.append(f"press {p['label']}: unknown place")
    for g in tg["glyphs"]:
        code = g["code"]
        if any(code[i:i + 3] not in sg for i in range(0, len(code), 3)):
            fails.append(f"glyph {g['gloss']}: code {code} not in signs.json")

    # 2. the years the book states
    src = open(os.path.join(HERE, "ktbook.py"), encoding="utf-8").read()
    years = {str(e["year"]) for e in d["events"]}
    for y, pat in BOOK_YEARS.items():
        if y not in years:
            fails.append(f"codex timeline has no event in {y}")
        if not re.search(pat, src):
            fails.append(f"the book no longer says {pat!r}; the plate says {y}")

    # 3. fresh plates
    r = subprocess.run([sys.executable, os.path.join(HERE, "ktatlas.py"), "--check"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        fails.append("ktatlas --check: " + (r.stdout.strip().splitlines() or ["?"])[-1])
        fails += ["  " + ln for ln in r.stdout.splitlines() if ln.startswith("FAIL")]

    # 4. well-formed, unique ids
    seen = {}
    for fn in sorted(os.listdir(OUT)) if os.path.isdir(OUT) else []:
        if not fn.endswith(".svg"):
            continue
        try:
            root = ET.parse(os.path.join(OUT, fn)).getroot()
        except ET.ParseError as ex:
            fails.append(f"{fn}: not well-formed XML: {ex}")
            continue
        for el in root.iter():
            i = el.get("id")
            if i:
                if i in seen:
                    fails.append(f"duplicate id {i!r} in {fn} and {seen[i]}")
                seen[i] = fn

    # 5. site copy
    cp = json.load(open(os.path.join(HERE, "ktsite_copy.json"), encoding="utf-8"))
    for k in ("atlas_lead", "card_atlas"):
        if not cp.get(k):
            fails.append(f"ktsite_copy.json: no {k}")

    # 6. factual regressions found in the source audit
    events = " ".join(e["label"] + " " + e["desc"] for e in d["events"])
    for bad in ("441 folios", "841 signs read", "Rohonc becomes Rechnitz"):
        if bad in events:
            fails.append(f"factual regression in events: {bad!r}")
    if "proposed" not in next(e for e in d["events"] if e["year"] == 1593)["label"].lower():
        fails.append("the 1593 event is no longer identified as a proposed reading")

    texts = {t["name"]: t for t in d["texts"]}
    expected = {"The Roman Missal": 1570, "The Roman Martyrology": 1584}
    for name, year in expected.items():
        if name not in texts or texts[name].get("year") != year:
            fails.append(f"{name}: expected a separate {year} entry")
    if texts.get("The Debreceni codex", {}).get("place") != "Obuda":
        fails.append("The Debreceni codex must be located at its place of production, Obuda")
    for name in ("The Gospels and Acts", "The Life of Adam and Eve",
                 "The Protevangelium of James", "The Apocalypse of Elijah",
                 "The Reversio sanctae crucis",
                 "The York, Chester, Towneley and N-Town plays"):
        if texts.get(name, {}).get("map", True):
            fails.append(f"{name}: disputed or multiple origins must not be plotted as one certain place")

    for f in fails:
        print("FAIL", f)
    n_svg = len([f for f in os.listdir(OUT) if f.endswith(".svg")]) if os.path.isdir(OUT) else 0
    print(f"ktatlascheck: {len(d['events'])} events, {len(d['texts'])} texts, "
          f"{n_svg} plates, {len(fails)} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
