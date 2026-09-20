"""A verbose cipher with the randomness taken out.

§4.2.1 found that Greshko's Naibbe cipher reaches the manuscript's conditional
entropy and then produces almost no dependence between neighbouring words, and
that the cause is the homophony: each plaintext letter is encoded through one
of six tables chosen by drawing a playing card, and choosing at random is what
destroys local structure. A word-boundary-preserving variant changed nothing,
because the boundaries were never the problem.

That leaves the obvious untested version, and it is the older form of the idea
(Pelling's verbose cipher, 2006): keep the one-to-many encoding, which is what
lowers the entropy, and drop the homophony, which is what destroys the
structure. Each plaintext letter becomes the *same* group of glyphs every time.

This is built as the minimal change to Greshko's own cipher -- his tables, his
chunking, his glyph assignments -- with the card draw removed so that table
`alpha` is always used. One variable moves, so whatever changes is the
homophony's doing and nothing else.

Two readings of "keep the word boundaries" are offered, as in naibbe_wb, and
both plaintexts, because Italian starts with far more cross-word dependence
than Latin and is the plaintext a cipher would need in order to reach the
manuscript's within-line figure at all.

What to watch, in order:
  h2                 must stay near the manuscript's 1.84, or verbose encoding
                     is not doing its job
  within-line MI     the test the homophonic version fails at 0.005 against
                     the manuscript's 0.179
  across-break MI    the manuscript's is zero. A cipher of flowing prose should
                     carry the plaintext's across a line break, which would be
                     a new failure rather than a fix
  TTR                deterministic encoding means one plaintext word always
                     becomes the same ciphertext word, so vocabulary richness
                     is inherited from the plaintext
"""
import os
import random

import corpus
import layout
from . import register
from .naibbe import _in_repo, _load
from .naibbe_wb import clean_keep_spaces, respace_words
from .natlang import REF


def encipher(path, seed, joined, max_lines=4000):
    """Greshko's encoder with the card draw disabled."""
    nb = _load()
    rng = random.Random(seed)
    random.seed(seed)
    out = []
    orig_respace, orig_deck = nb.respace_plaintext, nb.create_card_deck
    with _in_repo():
        try:
            # one table, always: the cipher stops being homophonic
            nb.create_card_deck = lambda use_78=False: ["alpha"] * 64
            with open(path, encoding="utf-8", errors="replace") as fh:
                for i, line in enumerate(fh):
                    if i >= max_lines:
                        break
                    cleaned = clean_keep_spaces(line)
                    if not cleaned:
                        continue
                    chunks, owner = respace_words(cleaned, rng)
                    if not chunks:
                        continue
                    nb.respace_plaintext = lambda t, f=None, _c=chunks: list(_c)
                    toks = nb.encrypt_naibbe(cleaned, nb.naibbe_tables,
                                             nb.placeholder_to_glyph, use_78=False)
                    if not joined:
                        out.extend(toks)
                        continue
                    cur, last = [], None
                    for t, w in zip(toks, owner):
                        if last is not None and w != last and cur:
                            out.append("".join(cur))
                            cur = []
                        cur.append(t)
                        last = w
                    if cur:
                        out.append("".join(cur))
        finally:
            nb.respace_plaintext, nb.create_card_deck = orig_respace, orig_deck
    return out


def _make(name, lang, fname, joined, label, note):
    @register(name, kind="stream", label=label, note=note)
    def generate(spec, train, seed=0, _f=fname, _l=lang, _j=joined):
        ws = encipher(os.path.join(REF, _f), seed + 3, _j)
        doc, exhausted = layout.lay_out(ws, spec)
        return doc, {"shortfall": exhausted, "plaintext": _l,
                     "variant": "joined" if _j else "boundary-aligned",
                     "cite": "after Pelling (2006) and Greshko (2025); homophony removed"}
    return generate


_make("verbose_det", "latin", "confessions_lat.txt", False,
      "verbose cipher, no homophony (Latin)",
      "NEW: one-to-many but deterministic -- the untested form of the idea")
_make("verbose_det_italian", "italian", "dante_it.txt", False,
      "verbose cipher, no homophony (Italian)",
      "NEW: the plaintext with enough cross-word dependence to reach the target")
