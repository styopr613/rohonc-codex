"""Human gibberish: Gaskell & Bowern's 42 volunteers (2022).

Not a model of anything. Forty-two people were asked to write meaningless text
that looked like writing, and they did, by hand, at length. Gaskell and Bowern
found that what they produced is significantly non-random and shares many of
Voynichese's peculiarities, which is the strongest existing argument that the
manuscript's low-level structure does not need a mechanism at all -- only a
person improvising.

It belongs in this table precisely because it is the one row not produced by a
procedure anybody designed. Its limitation is size: the samples total a few
thousand words, far short of the manuscript's, so vocabulary-growth metrics
(TTR, hapax share, type counts, Zipf slope) are measured on a much smaller
sample than every other row and are not comparable. `notes["undefined"]` lists
them and the write-up marks them rather than scoring them.

Relabelled onto the shared one-character glyph inventory like the other
invented alphabets, so no metric is reading the volunteers' Latin spelling.
"""
import os
import random
import re
import zipfile

import corpus
import layout
from . import register
from .alphabet import pool as glyph_pool

ZIP = os.path.join(corpus.ROOT, "refs", "voynich", "data",
                   "gibberish_transcriptions.zip")

# metrics a few thousand tokens cannot support at the manuscript's scale
UNDEFINED = ["TTR", "hapax %", "H(word)", "top-10 word share %",
             "hapax share of types %", "zipf slope (top500)",
             "distinct (first,last) pairs"]


def samples():
    """Every volunteer's text as a word stream, concatenated."""
    out = []
    with zipfile.ZipFile(ZIP) as z:
        for name in sorted(z.namelist()):
            if not name.lower().endswith(".txt"):
                continue
            txt = z.read(name).decode("utf-8", "replace").lower()
            for w in re.findall(r"[^\W\d_]+", txt, re.UNICODE):
                out.append(w)
    return out


@register("gibberish", kind="stream", label="human gibberish (42 volunteers)",
          note="real people improvising; small sample, some metrics undefined")
def generate(spec, train, seed=0):
    ws = samples()
    rng = random.Random(seed + 17)
    alpha = sorted({c for w in ws for c in w})
    g = glyph_pool(rng, len(alpha))
    m = {c: g[i] for i, c in enumerate(alpha)}
    ws = ["".join(m[c] for c in w) for w in ws]
    doc, exhausted = layout.lay_out(ws, spec, cycle=False)
    return doc, {"shortfall": exhausted, "source_tokens": len(ws),
                 "undefined": UNDEFINED,
                 "cite": "Gaskell & Bowern (2022), CEUR-WS Vol-3313"}
