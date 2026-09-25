"""Deep traces: a sign stacked from dozens of its own copies in the scan.

kttrace.py stacks at most five copies of a WORD. A common sign occurs hundreds
of times, and every copy sits at a different sub-pixel offset, so stacking
dozens of them recovers shape no 13-pixel copy has, and the strokes of
neighbouring signs, which change from copy to copy, vote themselves out.

  1. Find the sign's copies (kttrace.search, cached in trace/hits.json).
  2. kttrace.deep: seed from the best copies that agree with each other, then
     keep every copy that agrees with the seed, never more copies than the
     transcription says the book has of that sign, and take the median.
  3. Identity check: the result is compared with every one of Király and
     Tokai's signs, boxed. If it looks more like another sign than its own,
     it is marked LOOKS LIKE and not used.
  4. Trace it (Otsu threshold on the median, potrace).

Their outlines are the search key and the identity check. Nothing of them is
in the output.

    python3 ktdeep.py --codes 910,4b0       these signs
    python3 ktdeep.py --site                every sign the site draws
"""
import argparse
import glob
import json
import os
import sys
from collections import Counter

import numpy as np
from PIL import Image, ImageDraw

import kttrace as T
from ktcut import boxed, iou

OUT = os.path.join(T.ROOT, "work", "rohonc", "deepGlyphs.json")
SHEET = os.path.join(T.OUTDIR, "deep.png")
PAGES = os.path.join(T.ROOT, "data", "rohonc", "kt", "pages")


def freq():
    cnt = Counter()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "text" and isinstance(v, str):
                    for ch in v:
                        if 0xE000 <= ord(ch) < 0xF900:
                            cnt["%03x" % (ord(ch) - 0xE000)] += 1
                else:
                    walk(v)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    for f in glob.glob(os.path.join(PAGES, "*.json")):
        walk(json.load(open(f, encoding="utf-8")))
    return cnt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--codes")
    ap.add_argument("--site", action="store_true")
    ap.add_argument("--checked", action="store_true", help="stack only copies that look like their own sign")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    sg = json.load(open(T.SIGNS, encoding="utf-8"))["signs"]
    if args.codes:
        codes = args.codes.split(",")
    else:
        words = open(os.path.join(T.ROOT, "work", "rohonc", "sitecodes.txt")).read().split()
        codes = sorted({w[i:i + 3] for w in words if len(w) % 3 == 0 for i in range(0, len(w), 3)} & set(sg))
    F = freq()
    hp = os.path.join(T.OUTDIR, "hits.json")
    hits = json.load(open(hp)) if os.path.exists(hp) else {}
    need = [c for c in codes if c not in hits]
    if need:
        print(f"searching {len(need)} signs", file=sys.stderr)
        hits.update(T.search(need, sg))
        json.dump(hits, open(hp, "w"))
    cache = {f: a for f, a in T.spreads()}
    allk = {code: boxed(T.key(g, 0.1, ss=1) > 0.5) for code, g in sg.items()}
    out = args.out or OUT
    done = json.load(open(out)) if os.path.exists(out) else {"upm": 1000, "signs": {}}
    rows = []
    for c in codes:
        hl = [tuple(h) for h in hits[c]]
        if args.checked:
            med, kept, tried = T.deep_checked(hl, cache, c, allk, boxed, iou, cap=max(2, F.get(c, 0)))
        else:
            med, kept, tried = T.deep(hl, cache, cap=max(2, F.get(c, 0)))
        if med is None:
            continue
        mask, cut = T.centre_ink(med, T.otsu(med))
        if not mask.any():
            continue
        mb = boxed(mask)
        own = iou(mb, allk[c])
        rival, rv = max(((o, iou(mb, k)) for o, k in allk.items() if o != c), key=lambda t: t[1])
        status = "OK" if kept >= 3 and rv <= own + 0.03 else ("LOOKS LIKE " + rival if rv > own + 0.03 else "FEW COPIES")
        d, shape = T.potrace_path(mask)
        path, b, w = T.to_units(d, shape, sg[c], hl[0][6] if hl else T.SCALES[1])
        done["signs"][c] = {"d": path, "w": w, "b": b, "status": status, "kept": kept,
                            "in_book": F.get(c, 0), "own_iou": round(own, 2),
                            "rival": rival, "rival_iou": round(rv, 2)}
        rows.append((c, status, kept, F.get(c, 0), med, mask, allk[c]))
    json.dump(done, open(out, "w"), indent=0)
    cell = 72
    img = Image.new("L", (cell * 3 + 170, cell * len(rows) + 4), 255)
    dr = ImageDraw.Draw(img)
    for r, (c, st, k, fb, med, mask, kb) in enumerate(rows):
        y = r * cell + 2
        dr.text((2, y + 2), c, fill=0)
        dr.text((2, y + 16), st[:20], fill=0)
        dr.text((2, y + 30), f"{k} copies / {fb} in book", fill=0)
        for j, t in enumerate([med, np.where(mask, 0, 255), np.where(kb, 0, 255)]):
            im = Image.fromarray(np.clip(np.asarray(t, np.float32), 0, 255).astype(np.uint8))
            im.thumbnail((cell - 6, cell - 6))
            img.paste(im, (170 + j * cell, y + 3))
    img.save(SHEET)
    n = Counter(r[1].split()[0] for r in rows)
    print(f"ktdeep: {len(rows)} signs, {dict(n)}; sheet {SHEET}")


if __name__ == "__main__":
    sys.exit(main())
