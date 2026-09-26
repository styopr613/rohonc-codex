"""Book One beside its gloss, for a reader pass; and exact edits applied back.

A reader pass reads every Book One paragraph against the gloss of the folios
it cites and corrects what the signs do not support. This builds the sheet to
read from, and applies the corrections as exact, unique replacements, so no
edit can land in the wrong paragraph.

    python3 ktreview.py build OUT.txt       # paragraph, then each folio's gloss
    python3 ktreview.py apply EDITS.json    # [[old, new], ...] into reading.md

`apply` matches across line breaks (any run of whitespace in OLD matches any
run in the file) and refuses the whole batch if any OLD is missing or occurs
more than once. Back the file up first (.pre suffix); nothing here does it.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = os.path.join(ROOT, "work", "rohonc", "translation")
ED = os.path.join(TR, "rohonc_readers_edition.md")
B1 = os.path.join(TR, "reading.md")


def build(out):
    txt = open(ED, encoding="utf-8").read()
    gl, title = {}, {}
    for m in re.finditer(r"^## (\d{3}[rv])(?: — ([^\n]*))?\n(.*?)(?=^## |\Z)", txt, re.M | re.S):
        pg, t, body = m.groups()
        title[pg] = t or ""
        gl[pg] = [l.strip() for l in body.splitlines() if re.match(r"^\s*\d+\s+\S", l)]
    order = list(gl)
    rows, n = [], 0
    for para in re.split(r"\n\s*\n", open(B1, encoding="utf-8").read()):
        para = re.sub(r"\s+", " ", para).strip()
        if para.startswith("#"):
            rows.append("\n" + para + "\n")
            continue
        m = re.search(r"\(([^)]*\d{3}[rv][^)]*)\)\s*$", para)
        if not m:
            continue
        fols = []
        for bit in re.split(r"\s*,\s*", m.group(1)):
            e = re.findall(r"\d{3}[rv]", bit)
            if len(e) == 2:
                i, j = order.index(e[0]), order.index(e[1])
                fols += order[i:j + 1]
            else:
                fols += e
        n += 1
        rows.append(f"\n=== P{n} {m.group(1)}\nB1: {para}")
        for f in fols:
            rows.append(f"  -- {f} {title.get(f, '')}")
            rows += ["    " + l for l in gl.get(f, [])]
    open(out, "w", encoding="utf-8").write("\n".join(rows))
    print(f"{n} paragraphs -> {out}")


def apply(path):
    s = open(B1, encoding="utf-8").read()
    edits = json.load(open(path, encoding="utf-8"))
    for a, b in edits:
        pat = r"\s+".join(re.escape(w) for w in a.split())
        k = len(re.findall(pat, s))
        if k != 1:
            sys.exit(f"refused, nothing written: {k} matches for {a!r}")
        s = re.sub(pat, lambda _m: b, s)
    open(B1, "w", encoding="utf-8").write(s)
    print(f"{len(edits)} edits applied to reading.md")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("build", "apply"):
        sys.exit(__doc__)
    (build if sys.argv[1] == "build" else apply)(sys.argv[2])
