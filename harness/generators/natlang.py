"""Control: a plain natural language written in an invented alphabet.

No cipher, no abbreviation, no procedure. The plaintext's own letters are
relabelled one-to-one onto invented glyphs, which changes nothing measurable
except the names of the symbols. If the manuscript were an ordinary language in
an unfamiliar script, this is what its statistics would look like.

Three languages are offered because the manuscript has been claimed for all
three families: Latin (inflected, the Voynich's own milieu), Italian (Dante,
the closest natural language to the manuscript on conditional entropy) and
Hebrew (the Hauer & Kondrak language-ID result, and an abjad, which is the
standard explanation offered for a low-entropy script).
"""
import os

import corpus
import layout
from . import register

REF = os.path.join(corpus.ROOT, "data", "ref")


def _words_from_conllu(path, limit):
    import re
    W = re.compile(r"[^\W\d_]+")
    out = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if not line or line.startswith("#"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue
            form = parts[1].lower()
            if form and form != "_" and W.fullmatch(form):
                out.append(form)
                if len(out) >= limit:
                    return out
    return out


def _words_from_text(path, limit):
    import re
    W = re.compile(r"[^\W\d_]+")
    out = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            for w in W.findall(line):
                out.append(w.lower())
                if len(out) >= limit:
                    return out
    return out


def plaintext(lang, limit=60000):
    """Word stream of a reference language."""
    if lang == "latin":
        return _words_from_text(os.path.join(REF, "confessions_lat.txt"), limit)
    if lang == "italian":
        return _words_from_text(os.path.join(REF, "dante_it.txt"), limit)
    return _words_from_conllu(os.path.join(REF, f"{lang}.conllu"), limit)


def relabel(words, seed=1):
    """One-to-one map of the plaintext alphabet onto invented glyph names.

    Deterministic, information-preserving, and length-preserving: one glyph is
    one character, so relabelling cannot move any length metric. See
    alphabet.py for why that matters and what it costs.
    """
    import random
    from .alphabet import pool as glyph_pool
    alpha = sorted({c for w in words for c in w})
    rng = random.Random(seed)
    g = glyph_pool(rng, len(alpha))
    mapping = {c: g[i] for i, c in enumerate(alpha)}
    return ["".join(mapping[c] for c in w) for w in words]


def _make(lang):
    @register(f"natlang_{lang}", kind="stream",
              label=f"plain {lang}, invented alphabet",
              note="control: an ordinary language in an unfamiliar script")
    def generate(spec, train, seed=0, _lang=lang):
        ws = relabel(plaintext(_lang), seed=seed + 1)
        doc, exhausted = layout.lay_out(ws, spec)
        return doc, {"shortfall": exhausted, "plaintext": _lang}
    return generate


for _l in ("latin", "italian", "hebrew"):
    _make(_l)
