# Pre-registered prediction: the scribal-abbreviation process

Written 2026-09-19, before `harness/generators/abbrev.py` was written and before
any run of it. Recorded separately so the ordering is auditable rather than
asserted. Whatever the run shows, this file is not edited afterwards.

## The process

Latin plaintext (Augustine, *Confessiones*, the same file the `natlang_latin`
and `naibbe_latin` rows use), then:

1. **Suspension** of frequent inflectional endings: `-us -um -orum -arum -ibus
   -tur -que -bus -ur`. The scribe writes the stem and a mark.
2. **Contraction** of very frequent words and nomina sacra: `dominus deus
   noster est enim autem` and the like, written as first and last letter with a
   bar.
3. **Common signs**: `per pro prae con- -rum` and the nasal macron, each a
   single stroke standing for two or three letters.
4. A one-to-one map of the resulting letters-and-signs onto an invented
   alphabet, with **positional allographs**: a letter takes a different glyph
   word-initially, word-finally and in the middle. This is an ordinary scribal
   habit, and it is the step most likely to depress conditional entropy,
   because it makes the identity of a glyph partly predictable from where it
   sits.

## What is being tested

Lindemann and Bowern (2020) list scribal abbreviation among the candidate
explanations for Voynichese's conditional entropy and do not model it. Nobody
has built it. The question is narrow: **can ordinary medieval abbreviation
practice, applied to real Latin, move the statistics from where plain Latin
sits to where the manuscript sits?**

## The prediction

1. `abbrev` will beat `natlang_latin` and `subst` on h2 (conditional character
   entropy) and on the word-length distribution. Suspension shortens words and
   the positional allographs make the next glyph more predictable, so both must
   move in the manuscript's direction.
2. It will **not** reach the manuscript. Specifically h2 will land between
   Latin's 3.19 and the manuscript's 1.84, and closer to Latin than to the
   manuscript — I expect roughly 2.6 to 2.9.
3. The **Brevity law** will stay near a natural language's value (around −0.9)
   rather than the manuscript's −0.39, because abbreviation shortens frequent
   words *more*, which strengthens the brevity relation rather than abolishing
   it. This is the prediction I am least sure of and the most diagnostic: if
   abbreviation flattened Brevity, the abbreviation hypothesis would gain a lot.
4. It will fail the whole `line` block as badly as every other process that does
   not model the line, because nothing in abbreviation practice puts a gallows
   at a paragraph start or an `m` at a line end.
5. Overall it will finish behind `naibbe` and ahead of `natlang_latin` on floor
   units.

## What each outcome would mean

- If (1) and (2) hold: abbreviation is a real contributor to the entropy
  anomaly but not a sufficient explanation, which is the useful negative result
  the field currently lacks.
- If `abbrev` reached the manuscript's h2 while staying decipherable, that
  would be a substantially stronger claim than anything in this harness and
  would need checking against a second plaintext and a second abbreviation
  table before being believed.
- If it does not beat plain Latin at all, the implementation is wrong, not the
  hypothesis: suspension and allographs cannot fail to move conditional
  entropy. Debug before reporting.
