"""A second pass over signs the owner sent back, steered by the note.

Two things went wrong on the first pass (harness/sign_review.json, "regen"):

  the WRONG SIGN was stacked      607, 933, b61, b7a: the search found
                                  look-alikes and the seed took the bigger
                                  cluster. Every copy is now identity-checked
                                  before it may join the stack
                                  (kttrace.deep_checked).
  a HOLLOW was filled             071, 670, b30, b60: a counter one or two
                                  scan pixels wide does not survive a median
                                  of misaligned copies. Their outline is
                                  fitted to our ink's box and, where it has
                                  no ink at all, ours is taken away. The
                                  rule from ktpen.py: their outline may only
                                  REMOVE ink from ours, never add any, and
                                  the carve is refused when it would take
                                  more than a third of the ink, because then
                                  the two are not the same sign.

    python3 ktregen.py            every sign marked regen in sign_review.json
    python3 ktregen.py --codes 670,b60
"""
import argparse
import json
import os
import sys
from collections import Counter

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as nd

import kttrace as T
import ktdeep
from ktcut import boxed, iou
from ktpen import fit_box

OUT = os.path.join(T.ROOT, "work", "rohonc", "deepGlyphs_regen.json")
SHEET = os.path.join(T.OUTDIR, "regen.png")
REVIEW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sign_review.json")


def carve(mask, ktkey, reach=1.5):
    """Take ink away where their outline, fitted to our box, has none within
    `reach` stroke widths. Returns the carved mask and the share removed."""
    ys, xs = np.nonzero(mask)
    box = (mask.shape, (ys.min(), xs.min(), ys.max() + 1, xs.max() + 1))
    k = fit_box(ktkey, box)
    wid = float(np.median(nd.distance_transform_edt(mask)[mask])) or 2.0
    near = nd.distance_transform_edt(~k) <= reach * wid
    out = mask & near
    removed = 1 - out.sum() / max(1, mask.sum())
    return out, removed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--codes")
    ap.add_argument("--no-carve", action="store_true")
    args = ap.parse_args()
    rev = json.load(open(REVIEW, encoding="utf-8"))
    codes = args.codes.split(",") if args.codes else sorted(rev["regen"])
    sg = json.load(open(T.SIGNS, encoding="utf-8"))["signs"]
    F = ktdeep.freq()
    hits = json.load(open(os.path.join(T.OUTDIR, "hits.json")))
    cache = {f: a for f, a in T.spreads()}
    allk = {code: boxed(T.key(g, 0.1, ss=1) > 0.5) for code, g in sg.items()}
    ktmask = {code: T.key(g, 0.1, ss=1) > 0.5 for code, g in sg.items()}
    done = json.load(open(OUT)) if os.path.exists(OUT) else {"upm": 1000, "signs": {}}
    rows = []
    for c in codes:
        hl = [tuple(h) for h in hits[c]]
        med, kept, tried = T.deep_checked(hl, cache, c, allk, boxed, iou, cap=max(2, F.get(c, 0)))
        if med is None:
            print(f"{c}: no copies pass the identity check", file=sys.stderr)
            continue
        mask, _ = T.centre_ink(med, T.otsu(med))
        if not mask.any():
            continue
        before = iou(boxed(mask), allk[c])
        removed, carved = 0.0, False
        if not args.no_carve:
            m2, removed = carve(mask, ktmask[c])
            if m2.any() and removed <= 0.34:
                mask, carved = m2, True
        own = iou(boxed(mask), allk[c])
        rival, rv = max(((o, iou(boxed(mask), k)) for o, k in allk.items() if o[:2] != c[:2]), key=lambda t: t[1])
        status = "OK" if kept >= 3 and rv <= own + 0.03 else ("LOOKS LIKE " + rival if rv > own + 0.03 else "FEW COPIES")
        d, shape = T.potrace_path(mask)
        path, b, w = T.to_units(d, shape, sg[c], hl[0][6] if hl else T.SCALES[1])
        done["signs"][c] = {"d": path, "w": w, "b": b, "status": status, "kept": kept, "checked_of": tried,
                            "in_book": F.get(c, 0), "own_iou": round(own, 2), "own_iou_before_carve": round(before, 2),
                            "carved": carved, "carve_removed": round(removed, 2), "rival": rival, "rival_iou": round(rv, 2),
                            "note": rev["regen"].get(c, {}).get("note", "")}
        rows.append((c, status, kept, tried, med, mask, allk[c], before, own, carved))
        print(f"{c}: {kept} checked copies of {tried}; own IoU {before:.2f} -> {own:.2f}{' (carved %.0f%%)' % (100 * removed) if carved else ''}; {status}")
    json.dump(done, open(OUT, "w"), indent=0)
    cell = 72
    img = Image.new("L", (cell * 3 + 190, cell * max(1, len(rows)) + 4), 255)
    dr = ImageDraw.Draw(img)
    for r, (c, st, k, t, med, mask, kb, b0, b1, cv) in enumerate(rows):
        y = r * cell + 2
        dr.text((2, y + 2), f"{c}  {st[:16]}", fill=0)
        dr.text((2, y + 16), f"{k} of {t} copies", fill=0)
        dr.text((2, y + 30), f"iou {b0:.2f}->{b1:.2f}{' carved' if cv else ''}", fill=0)
        for j, tile in enumerate([med, np.where(mask, 0, 255), np.where(kb, 0, 255)]):
            im = Image.fromarray(np.clip(np.asarray(tile, np.float32), 0, 255).astype(np.uint8))
            im.thumbnail((cell - 6, cell - 6))
            img.paste(im, (190 + j * cell, y + 3))
    img.save(SHEET)
    print(f"ktregen: {len(rows)} signs, {dict(Counter(r[1].split()[0] for r in rows))}; sheet {SHEET}")


if __name__ == "__main__":
    sys.exit(main())
