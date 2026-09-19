"""Control: a letter-level substitution cipher over Latin.

The classical hypothesis, and the one the fingerprint repo's substitution
attack already rules out. It is kept in the table because a ranking needs a row
whose failure is understood in advance: a one-to-one substitution cannot change
conditional entropy at all, so this row must land where plain Latin lands. If
it ever does not, the harness is broken.

Homophonic variants are offered too: each plaintext letter gets k ciphertext
symbols chosen at random per occurrence, which is the standard fifteenth-century
answer to frequency analysis. Homophony *raises* entropy, so this row is also
the demonstration that the manuscript's anomaly cannot be a homophonic cipher.
"""
import random

import layout
from . import register
from .natlang import plaintext, relabel


def homophonic(words, k, seed=1):
    from .alphabet import pool as glyph_pool
    rng = random.Random(seed)
    alpha = sorted({c for w in words for c in w})
    g = glyph_pool(rng, len(alpha) * k)
    table, i = {}, 0
    for c in alpha:
        table[c] = g[i:i + k]
        i += k
    return ["".join(rng.choice(table[c]) for c in w) for w in words]


@register("subst", kind="stream", label="substitution cipher over Latin",
          note="control: one-to-one, cannot move conditional entropy")
def generate(spec, train, seed=0):
    ws = relabel(plaintext("latin"), seed=seed + 7)
    doc, exhausted = layout.lay_out(ws, spec)
    return doc, {"shortfall": exhausted, "plaintext": "latin"}


@register("subst_homophonic", kind="stream",
          label="homophonic cipher over Latin (k=3)",
          note="control: homophony raises entropy, it cannot lower it")
def generate_hom(spec, train, seed=0):
    ws = homophonic(plaintext("latin"), k=3, seed=seed + 7)
    doc, exhausted = layout.lay_out(ws, spec)
    return doc, {"shortfall": exhausted, "plaintext": "latin", "homophones": 3}
