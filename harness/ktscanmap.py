"""Which scanned opening is which folio, decided by counting lines.

The page images are the one piece of evidence in this project that played no
part in producing any reading. The codex is illustrated, and a picture on the
folio is an independent witness to what the text there says -- but only if we
know which image is which folio, and nothing in the scan says so.

The transcription knows how many lines each folio has. So does the image, if
the line finder works at 100 ppi. Line counts are a fingerprint: a run of
folios with 13, 9, 12, 14, 11 lines will match at one offset and nowhere else.

THE BAR, fixed before the run and not moved:

  The offset is accepted only if it matches the transcription's line count
  to within one line on at least 70% of pages, AND beats the second-best
  offset by at least 15 points. Below either, the mapping is not established
  and the illustrations stay unusable. A mapping that is nearly right is
  worse than none, because it would attach the wrong picture to the text.

    python3 ktscanmap.py            [--offset N] [--show FOLIO]
"""
import glob
import os
import sys

import numpy as np
from PIL import Image

import ktcross as K
import roho_ocr as O


def scan_line_counts():
    """[(spread index, verso lines, recto lines)] for every image."""
    fs = sorted(glob.glob(os.path.join(O.SCAN, "nat*.png")))
    out = []
    for i, f in enumerate(fs):
        a = np.array(Image.open(f).convert("L"))
        row = []
        for p in O.split_spread(a):
            sub = O.crop_page(p)
            row.append(0 if sub is None else len(O.lines_of(sub)))
        out.append((i, row[0], row[1]))
    return out


def doc_line_counts():
    """[(folio, lines)] in PHYSICAL folio order, not K&T's reading order.

    This mattered. K&T publish the codex in the order they think it should be
    read -- their pagelist starts 004v, 004r, 002r -- while the scan is in the
    order the book is bound. Matching one against the other scored 41.7% and
    failed this file's own bar. Sorting the folios by their labels first is
    what the scan can be compared to.
    """
    gl, doc, seg, var, prop, inv = K.build()
    n = {}
    for pg in doc:
        n[pg.page] = n.get(pg.page, 0) + len(pg.lines)

    def key(f):
        return (int(f[:3]), 0 if f[3] == 'r' else 1)

    return [(f, n[f]) for f in sorted(n, key=key)]


def main(argv):
    sc = scan_line_counts()
    flat = []
    for i, v, r in sc:
        flat.append((f"spread{i:03d}v", v))
        flat.append((f"spread{i:03d}r", r))
    dc = doc_line_counts()
    print(f"scan pages {len(flat)}   transcription folios {len(dc)}")

    best = []
    for off in range(-6, 12):
        ok = tot = 0
        for j, (folio, n) in enumerate(dc):
            k = j + off
            if 0 <= k < len(flat):
                tot += 1
                if abs(flat[k][1] - n) <= 1:
                    ok += 1
        if tot > 100:
            best.append((ok / tot, off, ok, tot))
    best.sort(reverse=True)
    for pct, off, ok, tot in best[:5]:
        print(f"  offset {off:+3d}   {pct*100:5.1f}%   {ok}/{tot}")
    if len(best) < 2:
        print("NOT ESTABLISHED: too few offsets tested")
        return 1
    top, second = best[0], best[1]
    gap = (top[0] - second[0]) * 100
    good = top[0] >= 0.70 and gap >= 15
    print(f"  best {top[0]*100:.1f}% at offset {top[1]:+d}, "
          f"second best {second[0]*100:.1f}%, gap {gap:.1f} points")
    print(f"  BAR: >=70% and >=15 points clear  ->  "
          f"{'ESTABLISHED' if good else 'NOT ESTABLISHED'}")
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
