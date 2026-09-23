"""A Latin scribal-abbreviation process. New work; nobody has modelled this.

Lindemann & Bowern (2020) name scribal abbreviation as a candidate explanation
for Voynichese's conditional entropy and do not model it. The question this row
answers is narrow: can ordinary medieval abbreviation practice, applied to real
Latin, move the statistics from where Latin sits to where the manuscript sits?

Four stages, in the order a scribe would apply them:

  1. suspension  -- frequent inflectional endings become a mark
  2. contraction -- very frequent words become first + last letter and a bar
  3. common signs -- per / pro / prae / con- / -rum / the nasal macron
  4. relabelling with positional allographs -- a letter takes a different glyph
     word-initially, word-finally and medially, which is an ordinary scribal
     habit and the stage most likely to depress conditional entropy

The prediction for this row was written before the code and is in
notes/PREDICTION_abbrev.md. It is not edited afterwards.

This is a model of a *process*, not a decipherment: the output is not claimed
to be what is in the manuscript, only to be what medieval abbreviation practice
does to the statistics of a real language.
"""
import random

import layout
from . import register
from .natlang import plaintext

# stage 1: inflectional endings a scribe suspends, longest first
SUSPENSIONS = [("orum", "\x01"), ("arum", "\x02"), ("ibus", "\x03"),
               ("que", "\x04"), ("tur", "\x05"), ("bus", "\x06"),
               ("us", "\x07"), ("um", "\x08"), ("ur", "\x09")]

# stage 2: very frequent words written as a contraction
CONTRACTIONS = {
    "dominus": "d\x0as", "domine": "d\x0ae", "domini": "d\x0ai", "dominum": "d\x0am",
    "deus": "d\x0bs", "deum": "d\x0bm", "dei": "d\x0bi", "deo": "d\x0bo",
    "noster": "n\x0cr", "nostri": "n\x0ci", "nostrum": "n\x0cm",
    "est": "\x0d", "enim": "\x0e", "autem": "\x0f", "quia": "q\x10",
    "quod": "q\x11", "qui": "q\x12", "quae": "q\x13", "non": "\x14",
    "sunt": "s\x15", "esse": "\x16", "etiam": "\x17", "sicut": "\x18",
}

# stage 3: common signs, each one stroke for two or three letters
SIGNS = [("prae", "\x19"), ("per", "\x1a"), ("pro", "\x1b"),
         ("con", "\x1c"), ("rum", "\x1d")]

NASAL = "\x1e"    # macron standing for a nasal before a consonant

DEFAULTS = {"p_suspend": 0.85, "p_contract": 0.9, "p_sign": 0.8,
            "p_nasal": 0.7, "allographs": 3}


def abbreviate(words, cfg, rng):
    out = []
    for w in words:
        if w in CONTRACTIONS and rng.random() < cfg["p_contract"]:
            out.append(CONTRACTIONS[w])
            continue
        for src, dst in SIGNS:
            if src in w and rng.random() < cfg["p_sign"]:
                w = w.replace(src, dst, 1)
                break
        if cfg["p_nasal"]:
            i = 1
            while i < len(w) - 1:
                if w[i] in "mn" and w[i + 1] not in "aeiou" and rng.random() < cfg["p_nasal"]:
                    w = w[:i] + NASAL + w[i + 1:]
                i += 1
        for end, mark in SUSPENSIONS:
            if w.endswith(end) and len(w) > len(end) and rng.random() < cfg["p_suspend"]:
                w = w[:-len(end)] + mark
                break
        out.append(w)
    return out


def relabel_positional(words, n_allo, seed=1):
    """One-to-one relabelling with positional allographs.

    Information-preserving and length-preserving: a reader who knows which
    position they are in can invert it, and one glyph is always one character.
    Initial, final and medial forms of the same letter are different glyphs,
    which is what a fifteenth-century hand actually does.
    """
    from .alphabet import pool as glyph_pool
    rng = random.Random(seed)
    alpha = sorted({c for w in words for c in w})
    n_allo = max(1, n_allo)
    g = glyph_pool(rng, len(alpha) * n_allo)
    tables, i = [], 0
    for _ in range(n_allo):
        t = {}
        for c in alpha:
            t[c] = g[i]
            i += 1
        tables.append(t)
    def form(w):
        if not w:
            return w
        out = []
        for j, c in enumerate(w):
            if len(tables) == 1:
                t = tables[0]
            elif j == 0:
                t = tables[0]
            elif j == len(w) - 1:
                t = tables[min(1, len(tables) - 1)]
            else:
                t = tables[min(2, len(tables) - 1)]
            out.append(t[c])
        return "".join(out)
    return [form(w) for w in words]


@register("abbrev", kind="stream", label="Latin scribal abbreviation",
          note="NEW: suspension + contraction + signs + positional allographs")
def generate(spec, train, seed=0, cfg=None):
    cfg = {**DEFAULTS, **(cfg or {})}
    rng = random.Random(seed + 13)
    ws = abbreviate(plaintext("latin"), cfg, rng)
    ws = relabel_positional(ws, cfg["allographs"], seed=seed + 2)
    doc, exhausted = layout.lay_out(ws, spec)
    # The bare filename, not the path. It is written into work/results_*.json,
    # and those files are the archived runs: a cosmetic change here would make a
    # regenerated table differ from the published one for no reason. The file
    # moved to notes/ on 2026-09-23; this names it, it does not locate it.
    return doc, {"shortfall": exhausted, "plaintext": "latin", "cfg": cfg,
                 "prediction": "PREDICTION_abbrev.md"}
