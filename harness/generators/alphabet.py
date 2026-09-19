"""One glyph, one character.

A relabelling must not change how long a word is. The first version of this
harness spelled invented glyphs with EVA-style two-character names, which
doubled the word length of any process whose alphabet outgrew the 23 available
one-character names -- an artefact of the spelling, not of the process. Every
invented alphabet now draws from a single-character inventory large enough for
any of them, so word length always means "number of glyphs".

What this costs, stated plainly: the manuscript is measured in EVA, where a
minority of glyphs (ch, sh, cth, ckh, cph, cfh) are written with two or three
characters, so its character-level metrics are on a slightly different footing
from the generated rows. The size of that effect is already known and is small:
voynich-fingerprint's alphabet_robustness.py puts h2 between 1.85 and 2.35
across five independent transliterations, including v101, where one glyph is
exactly one character and the alphabet has 166 symbols. A one-character
encoding is inside that band.
"""

# Letters from eight well-separated scripts: all single characters, all
# word-characters, none of them EVA, so an invented alphabet can never be
# confused with the manuscript's own transliteration in an output file. Large
# enough for the widest alphabet any process here needs (abbreviation with
# three positional allographs, 165 glyphs).
INVENTORY = "".join(chr(c) for a, b in (
    (0x0061, 0x007a), (0x03b1, 0x03c9), (0x0430, 0x044f), (0x0561, 0x0586),
    (0x10d0, 0x10fa), (0x05d0, 0x05ea), (0x2c81, 0x2cb1), (0x0531, 0x0556),
) for c in range(a, b + 1) if chr(c).isalpha())


def pool(rng, n):
    """n distinct single-character glyph names, shuffled."""
    if n > len(INVENTORY):
        raise ValueError(f"need {n} glyphs, inventory has {len(INVENTORY)}")
    p = list(INVENTORY)
    rng.shuffle(p)
    return p[:n]
