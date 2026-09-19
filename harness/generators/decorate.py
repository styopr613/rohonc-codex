"""A scribe's page habits, bolted onto the best-scoring generator.

§4.3 of RESULTS.md found that no process reproduces two properties of the page:
a letter that sits at the end of a line two thirds of the time, and a big
looping gallows glyph opening a paragraph's first line. A fair objection is
that nobody asked them to, and that a scribe would produce both for free
without any of it meaning anything. This row tests that objection directly.

Two habits, one rule each, both calibrated on the training half only:

  **the flourish.** Line-final `m` is almost certainly a flourished `r`, and
  the training data says so plainly: `dam` ends a line 36 times while `dar`
  appears 130 times elsewhere, `am`/`ar` 34 against 155, `okam`/`okar` 12
  against 65. So: at the end of a line, a word ending in `r` is written with
  `m` instead, at the rate the training half shows.

  **the capital.** A paragraph's first line opens with a gallows glyph. So: at
  the start of a paragraph, a gallows letter is written in front of the first
  word, at the training half's rate, drawn from the training half's own
  distribution of which gallows opens a paragraph.

Neither habit is fitted to any metric. Both are one line of scribal practice
that a person decorating a page would do without thinking. If they close the
gap for free, §4.3 dissolves and should be withdrawn. If they close it at a
cost elsewhere, §4.3 is real and we learn what the cost is.
"""
import random
from collections import Counter

import corpus
from . import register
from .fivecomp import generate as fivecomp_generate

GALLOWS = ("cth", "ckh", "cph", "cfh", "t", "k", "p", "f")


def habits(train):
    """Both rates and the gallows distribution, measured on TRAIN."""
    lines = [l for p in train.__iter__() for l in p.lines if l]
    lastw = [l[-1] for l in lines]
    n_m = sum(1 for w in lastw if w.endswith("m"))
    n_r = sum(1 for w in lastw if w.endswith("r"))
    flourish = n_m / (n_m + n_r) if (n_m + n_r) else 0.0
    firsts = [p.lines[0][0] for p in train if p.lines and p.lines[0]]
    cap = sum(1 for w in firsts if any(w.startswith(g) for g in GALLOWS)) / len(firsts)
    letters = Counter()
    for w in firsts:
        for g in GALLOWS:
            if w.startswith(g):
                letters[g[0] if len(g) == 1 else g] += 1
                break
    return {"flourish": flourish, "capital": cap, "letters": letters}


def apply(doc, h, rng):
    out = []
    keys = list(h["letters"]) or ["p"]
    wts = [h["letters"][k] for k in keys] or [1]
    for i, p in enumerate(doc):
        lines = [list(l) for l in p.lines]
        for ln in lines:
            if ln and ln[-1].endswith("r") and rng.random() < h["flourish"]:
                ln[-1] = ln[-1][:-1] + "m"
        if lines and lines[0] and rng.random() < h["capital"]:
            w = lines[0][0]
            if not any(w.startswith(g) for g in GALLOWS):
                lines[0][0] = rng.choices(keys, weights=wts)[0] + w
        out.append(corpus.Para(folio=p.folio, lines=lines, section=p.section,
                               lang=p.lang, hand=p.hand))
    return out


@register("fivecomp_scribe", kind="self",
          label="five-component model + a scribe's page habits",
          note="TEST: does ordinary page decoration close the line/paragraph gap for free?")
def generate(spec, train, seed=0, cfg=None):
    doc, notes = fivecomp_generate(spec, train, seed=seed)
    h = habits(train)
    doc = apply(doc, h, random.Random(seed + 31))
    notes = dict(notes)
    notes["habits"] = {"flourish": round(h["flourish"], 4),
                       "capital": round(h["capital"], 4)}
    return doc, notes
