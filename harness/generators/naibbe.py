"""Greshko's Naibbe cipher (Cryptologia 2025): a verbose homophonic
substitution cipher, executable by hand with fifteenth-century materials.

Plaintext is cut into one- and two-letter units by a die roll, each unit is
encoded through one of six tables chosen by drawing a playing card, and the
ciphertext word is the concatenation of the encoded units. Because one
plaintext letter becomes several ciphertext glyphs, conditional entropy falls
without any information being lost: the ciphertext is still decipherable.

This is the strongest form of the cipher hypothesis currently on the table, and
it is the row the fingerprint repo asserts would be "statistically
indistinguishable" from its own generator without having measured it.

Run from the author's own code. The plaintexts are the same Augustine and Dante
files the natural-language control uses, so the only difference between those
rows and this one is the process.
"""
import contextlib
import os
import random
import sys

import corpus
import layout
from . import register
from .natlang import REF

NAIBBE = os.path.join(corpus.ROOT, "refs", "naibbe-cipher")


@contextlib.contextmanager
def _in_repo():
    old = os.getcwd()
    os.chdir(NAIBBE)
    if NAIBBE not in sys.path:
        sys.path.insert(0, NAIBBE)
    try:
        yield
    finally:
        os.chdir(old)


def _load():
    with _in_repo():
        import naibbe_v2
        return naibbe_v2


def encipher(path, seed, max_lines=4000):
    """Encrypt a plaintext file, return the ciphertext word stream."""
    nb = _load()
    random.seed(seed)
    out = []
    with _in_repo():
        with open(path, encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh):
                if i >= max_lines:
                    break
                cleaned = nb.clean_line(line)
                if not cleaned:
                    continue
                out.extend(nb.encrypt_naibbe(cleaned, nb.naibbe_tables,
                                             nb.placeholder_to_glyph,
                                             use_78=nb.USE_78_CARD_DECK))
    return out


def _make(lang, fname):
    @register(f"naibbe_{lang}", kind="stream",
              label=f"Naibbe verbose cipher over {lang}",
              note="Greshko 2025, his own code; same plaintext as the control row")
    def generate(spec, train, seed=0, _f=fname, _l=lang):
        ws = encipher(os.path.join(REF, _f), seed + 3)
        doc, exhausted = layout.lay_out(ws, spec)
        return doc, {"shortfall": exhausted, "plaintext": _l,
                     "cite": "Greshko, M.A. (2025), Cryptologia, doi:10.1080/01611194.2025.2566408"}
    return generate


for _l, _f in (("latin", "confessions_lat.txt"), ("italian", "dante_it.txt")):
    _make(_l, _f)
