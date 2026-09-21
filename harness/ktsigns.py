"""ktsigns.py -- draw every sign of the script as an SVG path.

    /opt/publish-app/venv/bin/python ktsigns.py          # writes work/rohonc/signs.json

The site could not show the signs. It asked the reader to install Kiraly and
Tokai's font, which nobody will do. This reads that font once, locally, and
writes the OUTLINE of each sign as an SVG path, so the pages can draw the
signs themselves with nothing to install and nothing of theirs served.

What this is, stated plainly, because it matters: the shapes are the
sixteenth-century scribe's and are out of copyright. The font that carries
them is Kiraly and Tokai's own drawing of those shapes, made for
rechnitzer-kodex.hu. Paths written here are taken from it. They are credited
to them wherever they are shown, the font file itself is never served, and
DATA_PROVENANCE.md records the position. If they ask for them to come down,
they come down.
"""
import json
import os
import re
import sys

from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen

import corpus

FONT = os.path.join(corpus.ROOT, "data", "rohonc", "kt", "fonts", "RohoncCodex.woff")
OUT = os.path.join(corpus.ROOT, "work", "rohonc", "signs.json")
PUA_LO, PUA_HI = 0xE000, 0xEBFF   # the range the site's own stylesheet declares
_ROUND = re.compile(r"-?\d+\.\d+")


def main():
    if not os.path.isfile(FONT):
        raise SystemExit("ktsigns: no font at " + FONT)
    f = TTFont(FONT)
    upm = f["head"].unitsPerEm
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    hmtx = f["hmtx"]
    signs = {}
    for cp, name in sorted(cmap.items()):
        if not (PUA_LO <= cp <= PUA_HI):
            continue
        pen = SVGPathPen(gs)
        gs[name].draw(pen)
        d = pen.getCommands()
        if not d:
            continue                      # a blank glyph draws nothing
        # Full float precision triples the file for no visible gain: at 1000
        # units to the em, a whole unit is a thousandth of the drawn sign.
        d = _ROUND.sub(lambda m: str(round(float(m.group(0)))), d)
        bp = BoundsPen(gs)
        gs[name].draw(bp)
        if not bp.bounds:
            continue
        x0, y0, x1, y1 = (round(v) for v in bp.bounds)
        signs["%03x" % (cp - PUA_LO)] = {"d": d, "w": hmtx[name][0],
                                         "b": [x0, y0, x1, y1]}
    meta = {"upm": upm, "n": len(signs),
            "credit": ("Sign outlines from the Rohonc Codex font of Levente Zoltan "
                       "Kiraly and Gabor Tokai, rechnitzer-kodex.hu."),
            "signs": signs}
    json.dump(meta, open(OUT, "w"), separators=(",", ":"))
    print("wrote %s: %d signs, %d em, %d KB"
          % (OUT, len(signs), upm, os.path.getsize(OUT) // 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
