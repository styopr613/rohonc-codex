"""Naibbe with the plaintext's word boundaries kept.

§4.2 of RESULTS.md found that Greshko's cipher reproduces the manuscript's
conditional entropy and then fails completely on cross-word dependence, and
that it fails there by construction: `respace_plaintext` strips every space
before cutting the letter stream into one- and two-letter units, so ciphertext
word breaks fall where the dice put them rather than where the Latin's words
ended.

That is an objection with a repair in it, so here is the repair. The cutting
still happens, and the encoding tables are Greshko's, untouched. The only
change is that a unit may not straddle a space in the plaintext.

Two variants, because "keep the word boundaries" has two readings:

  `naibbe_wb`     the cut points are a superset of the plaintext's word breaks.
                  Every ciphertext word still encodes one or two letters, so
                  word length is unchanged, but a plaintext word break is now
                  always also a ciphertext word break.
  `naibbe_word`   one ciphertext word per plaintext word: the units of a word
                  are written joined. This is the strict reading, and the
                  obvious risk is that a five-letter Latin word becomes three
                  glyph groups written together and the result is far too long.

Both are run rather than one, because which of them is "the" repair is exactly
what is in question.
"""
import os
import random
import unicodedata

import corpus
import layout
from . import register
from .naibbe import _in_repo, _load
from .natlang import REF


# Greshko's clean_line keeps only alphabetic characters, which deletes every
# space before the respacing step ever runs. Word boundaries are therefore
# already gone by the time his cipher cuts the stream. This is the same
# normalisation with the spaces kept.
_REPL = {"ae": "ae", "\u00e6": "ae", "\u00c6": "ae", "\u0153": "oe", "\u0152": "oe",
         "\u00f0": "d", "\u00d0": "d", "\u00fe": "th", "\u00de": "th",
         "\u0142": "l", "\u0141": "l", "\u00df": "ss", "\u00f8": "o", "\u00d8": "o"}


def clean_keep_spaces(text):
    n = unicodedata.normalize("NFD", text)
    n = "".join(c for c in n if unicodedata.category(c) != "Mn")
    n = "".join(_REPL.get(c, c) for c in n)
    n = "".join(c if (c.isalpha() or c.isspace()) else " " for c in n).upper()
    n = n.replace("W", "UU").replace("J", "I").replace("K", "C")
    return " ".join(n.lower().split())


def respace_words(text, rng, respacing=17):
    """Greshko's respacing, stopped at every space.

    His rule: at each position, take one letter with probability
    respacing/36, otherwise take two. Applied inside a word and never across
    the gap between two words; a one-letter tail is taken as a unigram.
    """
    chunks, owner = [], []
    for wi, word in enumerate(text.lower().split()):
        i = 0
        while i < len(word):
            if i == len(word) - 1 or rng.random() < (respacing / 36):
                chunks.append(word[i])
                i += 1
            else:
                chunks.append(word[i:i + 2])
                i += 2
            owner.append(wi)
    return chunks, owner


def encipher(path, seed, joined, max_lines=4000):
    nb = _load()
    rng = random.Random(seed)
    random.seed(seed)
    out = []
    orig = nb.respace_plaintext
    with _in_repo():
        try:
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
                    # hand Greshko's encoder our word-respecting units
                    nb.respace_plaintext = lambda t, f=None, _c=chunks: list(_c)
                    toks = nb.encrypt_naibbe(cleaned, nb.naibbe_tables,
                                             nb.placeholder_to_glyph,
                                             use_78=nb.USE_78_CARD_DECK)
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
            nb.respace_plaintext = orig
    return out


def _make(name, lang, fname, joined, label, note):
    @register(name, kind="stream", label=label, note=note)
    def generate(spec, train, seed=0, _f=fname, _l=lang, _j=joined):
        ws = encipher(os.path.join(REF, _f), seed + 3, _j)
        doc, exhausted = layout.lay_out(ws, spec)
        return doc, {"shortfall": exhausted, "plaintext": _l,
                     "variant": "joined" if _j else "boundary-aligned",
                     "cite": "after Greshko (2025); modified here"}
    return generate


_make("naibbe_wb", "latin", "confessions_lat.txt", False,
      "Naibbe, word breaks kept (Latin)",
      "NEW: cut points never straddle a plaintext space")
_make("naibbe_word", "latin", "confessions_lat.txt", True,
      "Naibbe, one word per word (Latin)",
      "NEW: strict reading, a plaintext word is written as one ciphertext word")
# Italian is the decisive plaintext for the cross-word question: Dante starts at
# 0.056 bits of cross-word dependence where Augustine's Latin has only 0.016, so
# a Latin result alone cannot separate "the cipher destroys it" from "the
# plaintext never had it".
_make("naibbe_wb_italian", "italian", "dante_it.txt", False,
      "Naibbe, word breaks kept (Italian)",
      "NEW: the decisive row -- a plaintext that HAS cross-word dependence")
