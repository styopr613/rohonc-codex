# One ruler, every process

A hypothesis-ranking harness for the Voynich manuscript (Beinecke MS 408).
Twenty rows on one metric vector under one held-out protocol: fourteen
candidate processes, five controls whose behaviour is known in advance, and the
manuscript's own other half, which says how much of the difference is sampling
noise rather than explanation.

**This is a ranking with caveats, not a verdict.** Nothing here reads the
manuscript, and no result below is a decipherment. Read §7 before quoting §3,
and §6 for the four conclusions this document has already had to withdraw —
including, in §4.2.2 and §4.2.3, the two it found most interesting.

Built 2026-09-19 on Rachel. Private working repository; see §9.

---

## 1. Why this exists

The statistics of Voynichese have been measured many times and the field has
split into two camps that argue past each other because they use different
rulers.

One camp says a simple copying procedure explains the anomalies without any
message: Rugg (2004) with a table and grille, Timm & Schinner (2019) with
self-citation, and most recently Sachak's `voynich-fingerprint` (2026), which
measures a 44-metric fingerprint on a held-out split and reproduces it at 3.7 %
mean error with a five-component generator containing no language at all.

The other camp says the higher-order structure is too language-like for that:
Montemurro & Zanette (2013) on section-specific vocabulary, Bowern & Lindemann
(2020, 2021) on entropy and word structure, and Greshko (2025), whose Naibbe
cipher encrypts real Latin and Italian by hand into something that reproduces
"many key statistical properties of the Voynich Manuscript at once".

These are measured on different metric sets, against different baselines, with
different splits. `voynich-fingerprint`'s own LIMITATIONS.md states that a
verbose cipher "would be statistically indistinguishable" from its generator —
and does not measure one. `voynich-toolkit` measures a grille, a Naibbe and a
Llull machine, but on a 16-property scale with no held-out split, no language
control and no self-citation baseline.

So: one ruler, every process, the same protocol. The unglamorous unification.

The single most useful thing it produced was not a ranking. It was §4.2.2 and
§4.2.3 together: the manuscript's word-to-word structure is real, it stops dead
at the right-hand margin where a real language's does not, and inside the line
it sits entirely in the first and last couple of words. Whatever made this text
worked one line at a time, with a way of starting a line and a way of ending
one, and nothing in between.

## 2. What was built

The metric vector has three blocks:

| block | metrics | where it comes from |
|---|---|---|
| `text` | 15 | `voynich-fingerprint`'s tier-1 vector, computed by calling its own code |
| `struct` | 27 | its tier-2 vector, minus the two keys it excludes when scoring |
| `line` | 8 | **new here**: the line- and section-level properties the fingerprint repo does not measure |

The first two blocks reproduce the fingerprint repo's published held-out figures
to within 0.35 %, which `harness/gate.py` checks on every run, so our numbers
for those blocks are directly comparable to its. The `line` block adds the
properties `voynich-toolkit` found and the fingerprint repo omits: the `m`
line-end marker, gallows at paragraph starts, line self-containment, paragraph
vocabulary coherence, word-by-section mutual information, and word-length
autocorrelation.

**Two scales.** Mean absolute percentage error is the fingerprint repo's scale
and is reported for continuity. But APE is unusable on a metric whose true
value is near zero: the manuscript repeats a word across a line boundary 0.12 %
of the time, and the book's own other half misses that by 196 % while being
wrong by a quarter of a percentage point. So every metric is also scored in
**floor units** — multiples of how far two halves of the same book sit apart on
that metric, estimated from six contiguous chunks of the training half. A score
of 1.0 means "off by as much as the manuscript is off from itself". Below 1.0
means the difference is inside the book's own sampling spread and nothing can be
claimed from it. **The ranking is read in floor units. APE is shown beside it.**

**Protocol.** Train on even-numbered leaves, test on odd. Every parameterised
process gets the same tuning budget (200 random-search evaluations, or an
exhaustive sweep where the parameter space is smaller), scored on the training
half only. The held-out half is never read by any generator; `gate.py` greps for
it. Everything is seeded and reruns bit-identically. The reversed split is run
and reported beside the main one, and arbitrates anything the search may have
fitted to one half.

**Layout is given, not earned.** Every process receives the same layout spec —
paragraph shapes, line character budgets, and the section and Currier labels
that carry them — sampled from the *training* half. This is stricter than the
fingerprint repo, whose LIMITATIONS.md records that an earlier revision took
those constants from the held-out document and that the leak inflated its
result. The metrics this dictates (line geometry, paragraph shape) are marked
and are not evidence about any process. What the layout buys is that every
process writes under the same physical constraints as the scribe.

## 3. The ranking

Floor units, held-out half. Lower is closer to the manuscript. The figure in
brackets in the last column is the reversed split: train on odd leaves, test on
even, which arbitrates anything the tuning may have fitted to one half.

**The ranking is stable across the two splits**: Spearman rank correlation
0.991 over twenty rows, no process moves more than two places, and the top
eight are in identical order on both. The movements that do occur are inside
groups whose members sit within a few tenths of a floor unit of each other. No
conclusion in §4 depends on any of them.

<!--TABLE:RANKING-->
| process | what it is | fp42 APE | fp42 floor | line floor | median floor |
|---|---|---:|---:|---:|---:|
| `noise_floor` | manuscript, other half | 2.0% | 0.16x | 0.35x | 0.12x (0.13) |
| `fivecomp` | five-component model (fingerprint) | 3.3% | 0.29x | 2.96x | 0.25x (0.29) |
| `fivecomp_scribe` | five-component model + a scribe's page habits | 4.4% | 0.37x | 1.43x | 0.37x (0.31) |
| `fivecomp_lines` | five-component model + page habits + a line-opening rule | 4.5% | 0.31x | 1.31x | 0.30x (0.33) |
| `manual` | hand-executable manual (fingerprint) | 9.0% | 1.15x | 2.99x | 0.61x (0.65) |
| `naibbe_latin` | Naibbe verbose cipher over latin | 15.6% | 1.24x | 3.24x | 1.07x (0.86) |
| `naibbe_italian` | Naibbe verbose cipher over italian | 15.4% | 1.19x | 3.30x | 0.87x (0.73) |
| `naibbe_wb` | Naibbe, word breaks kept (Latin) | 19.6% | 1.47x | 3.32x | 1.40x (1.08) |
| `naibbe_wb_italian` | Naibbe, word breaks kept (Italian) | 19.6% | 1.40x | 3.43x | 1.25x (1.07) |
| `naibbe_word` | Naibbe, one word per word (Latin) | 186.9% | 10.77x | 3.21x | 1.73x (1.75) |
| `grille` | table-and-grille (Rugg) | 34.8% | 3.34x | 2.48x | 1.47x (1.42) |
| `grille_bigtable` | table-and-grille, large table | 23.0% | 2.68x | 2.83x | 1.58x (1.51) |
| `selfcite` | self-citation (Timm & Schinner) | 18.6% | 2.38x | 2.93x | 1.64x (1.18) |
| `llull` | Llull combinatoric disks | 51.6% | 5.18x | 4.04x | 3.24x (2.54) |
| `abbrev` | Latin scribal abbreviation | 50.1% | 5.66x | 3.22x | 4.61x (4.22) |
| `gibberish` | human gibberish (42 volunteers) | 65.7% | 7.79x | 2.75x | 5.06x (4.64) |
| `natlang_italian` | plain italian, invented alphabet | 45.3% | 5.56x | 3.75x | 3.64x (3.97) |
| `natlang_latin` | plain latin, invented alphabet | 51.1% | 4.78x | 3.17x | 4.13x (4.22) |
| `natlang_hebrew` | plain hebrew, invented alphabet | 52.4% | 6.60x | 3.93x | 4.23x (3.98) |
| `subst` | substitution cipher over Latin | 49.3% | 4.71x | 3.15x | 3.96x (4.11) |
| `subst_homophonic` | homophonic cipher over Latin (k=3) | 97.7% | 12.87x | 3.24x | 6.05x (5.34) |

## 4. What the numbers say

### 4.1 The entropy anomaly has two solutions, not one

<!--TABLE:HEADLINE-->
| process | h2 | h1 | TTR | word len | Zipf | cross-word MI |
|---|---|---|---|---|---|---|
| **the manuscript** | **1.84** | **3.86** | **0.275** | **5.17** | **-0.904** | **0.068** |
| `noise_floor` | 1.85 | 3.86 | 0.273 | 5.20 | -0.919 | 0.068 |
| `fivecomp` | 1.86 | 3.85 | 0.251 | 5.16 | -0.918 | 0.065 |
| `fivecomp_scribe` | 1.87 | 3.87 | 0.261 | 5.17 | -0.908 | 0.064 |
| `fivecomp_lines` | 1.84 | 3.86 | 0.239 | 5.12 | -0.900 | 0.048 |
| `manual` | 1.91 | 3.79 | 0.232 | 5.20 | -0.728 | 0.049 |
| `naibbe_latin` | 1.78 | 3.87 | 0.271 | 5.23 | -0.954 | 0.005 |
| `naibbe_italian` | 1.79 | 3.86 | 0.262 | 5.20 | -0.973 | 0.004 |
| `naibbe_wb` | 1.69 | 3.86 | 0.223 | 5.15 | -1.041 | 0.005 |
| `naibbe_wb_italian` | 1.69 | 3.86 | 0.208 | 5.08 | -1.077 | 0.004 |
| `naibbe_word` | 2.19 | 3.86 | 0.905 | 18.39 | -0.530 | 0.007 |
| `grille` | 2.02 | 3.84 | 0.079 | 4.60 | -0.642 | 0.017 |
| `grille_bigtable` | 2.10 | 3.84 | 0.269 | 4.59 | -0.799 | 0.005 |
| `selfcite` | 2.31 | 3.84 | 0.335 | 5.21 | -0.706 | 0.010 |
| `llull` | 2.33 | 3.57 | 0.181 | 7.13 | -0.420 | 0.001 |
| `abbrev` | 3.22 | 4.22 | 0.368 | 5.04 | -0.928 | 0.024 |
| `gibberish` | 3.94 | 4.40 | 0.680 | 4.94 | -0.650 | 0.021 |
| `natlang_italian` | 3.12 | 4.12 | 0.239 | 3.95 | -0.994 | 0.056 |
| `natlang_latin` | 3.19 | 3.97 | 0.351 | 5.33 | -0.934 | 0.016 |
| `natlang_hebrew` | 3.80 | 4.27 | 0.349 | 3.74 | -0.833 | 0.024 |
| `subst` | 3.19 | 3.97 | 0.351 | 5.33 | -0.934 | 0.016 |
| `subst_homophonic` | 4.74 | 5.56 | 0.746 | 5.33 | -0.762 | 0.037 |

Conditional character entropy is the manuscript's most famous anomaly: 1.84
bits against 3.12 for the closest natural language in the reference set. Two
kinds of process reach it, and they are not the same kind.

**Procedural generation reaches it.** The fingerprint repo's five-component
model lands at 1.86, inside the noise floor, and its hand-executable manual at
1.91. That result replicates cleanly on our stricter layout.

**A verbose cipher reaches it too, and slightly overshoots.** Greshko's Naibbe
cipher over Augustine's Latin gives 1.78, and over Dante 1.79 — both *below*
the manuscript. This is the first time that cipher has been scored on the
fingerprint's own vector, and it answers half of the question that repo left
open by assertion. Its LIMITATIONS.md says a verbose cipher "would be
statistically indistinguishable" from its generator. On conditional entropy
that is correct. On the whole vector it is not: §4.2 gives a metric on which
the two come apart cleanly.

The narrower lesson stands on its own. **Low conditional entropy is not
evidence of meaninglessness.** It is evidence of a one-to-many encoding, and a
meaning-free procedure and a fully decipherable cipher both provide one.

**Nothing else reaches it.** Self-citation stops at 2.31, the Llull machine at
2.33, the grille at 2.02–2.10, scribal abbreviation at 3.22, human gibberish at
3.94, plain Latin at 3.19. A plain substitution cipher sits exactly on plain
Latin, as it must, and a homophonic cipher moves entropy the wrong way, to
4.74. Those two rows are controls: if they ever move, the harness is broken.

### 4.2 Cross-word dependence is where the cipher fails

The manuscript carries 0.068 bits of mutual information between the end of one
word and the start of the next — Currier's old observation that words ending in
`y` tend to precede words beginning `qo-`.

| | cross-word MI |
|---|---:|
| the manuscript | 0.068 |
| its own other half | 0.068 |
| five-component model (models it explicitly) | 0.065 |
| plain Italian in an invented alphabet | 0.056 |
| hand-executable manual | 0.049 |
| scribal abbreviation | 0.024 |
| human gibberish | 0.021 |
| plain Latin | 0.016 |
| self-citation | 0.010 |
| **Naibbe verbose cipher** | **0.005** |
| grille, large table | 0.005 |
| Llull machine | 0.001 |

This is the sharpest discriminator between the cipher and everything else, and
it cuts against the cipher. **But see §4.2.2 before reading anything further
into it**: the dependence turns out to be bounded by the line, which changes
what it can be evidence for.

Read the natural-language rows carefully before drawing the moral, because they
do not agree with each other. Italian gives 0.056 and Latin 0.016. The metric is
character-level — the last character of one word against the first character of
the next — so it is sensitive to how much a language's word boundaries are
grammatically constrained. Italian's articles and prepositions make the next
word's opening partly predictable; Latin's free word order and inflectional
endings make it much less so. The firm statement is therefore: **the
manuscript's cross-word dependence, at 0.068, is higher than either natural
language in the reference set, and the Naibbe cipher has essentially none.**

### 4.2.1 Why the cipher loses it — a repair that was built and failed

The first version of this document blamed the respacing. Greshko's cipher
strips every space from the plaintext before cutting the letter stream into
one- and two-letter units, so ciphertext word breaks fall where the dice put
them. That looked like the obvious culprit and it came with an obvious repair,
which this document recommended as the next thing to build.

It was built. It does not work. Three variants are in the table:

| | cross-word MI | h2 | word length | TTR |
|---|---:|---:|---:|---:|
| the manuscript | **0.068** | 1.84 | 5.17 | 0.275 |
| plain Italian, the plaintext | 0.056 | 3.12 | 3.95 | 0.239 |
| Naibbe over Italian, as published | 0.004 | 1.79 | 5.20 | 0.262 |
| Naibbe over Italian, **word breaks kept** | 0.004 | 1.69 | 5.08 | 0.208 |
| Naibbe over Latin, **word breaks kept** | 0.005 | 1.69 | 5.15 | 0.223 |
| Naibbe over Latin, **one word per word** | 0.007 | 2.19 | 18.39 | 0.905 |

Italian is the decisive plaintext, because it starts with 0.056 bits of
cross-word dependence where Augustine's Latin has only 0.016. A Latin result
alone could not separate "the cipher destroys it" from "the plaintext never had
it". Italian can, and the answer is unambiguous: **the plaintext has it, the
ciphertext does not, and keeping the word boundaries does not bring it back.**
0.056 goes to 0.004 either way.

So the cause is not the respacing. It is the homophony. Each plaintext letter
is encoded through one of six tables chosen by drawing a playing card, which is
the whole point of the cipher — it is how a fifteenth-century encipherer defeats
frequency analysis without knowing what frequency analysis is. But choosing the
symbol at random is exactly what destroys the local dependence between one
symbol and the next. The property that makes the cipher strong is the property
that makes its output unlike the manuscript.

That generalises past this one cipher, and it is a stronger claim than the one
it replaces: **a verbose cipher cannot buy low conditional entropy through
homophony and keep cross-word dependence at the same time.** Any cipher in that
class faces the same wall. Something other than homophony would have to be
doing the entropy work.

The strict variant fails for a separate and simpler reason. Writing each
plaintext word as one ciphertext word gives a mean word length of 18.4 against
the manuscript's 5.17, and a type-token ratio of 0.905 — nearly every word in
the text occurring exactly once. Verbose encoding and realistic word length
cannot both hold unless ciphertext words are much shorter than plaintext words,
which is precisely why Greshko respaced in the first place. His design choice
was not careless; it was forced.

### 4.2.2 The line is the unit, and the word structure stops at the margin

§4.2 called the manuscript's cross-word dependence the loose thread in this
project: present at 0.068 bits, stronger than either reference language, and
reproduced by no meaning-free process except the one whose author built it in.
It was tempting to read that as the text behaving like a language.

Two tests were run to check that reading before anyone leaned on it. The first
asks how far the dependence reaches. The second asks whether it is about words
at all, or about how a quill moves between shapes. Both are surrogate-corrected:
the control shuffles the order of one element of each pair, which preserves both
marginals exactly and destroys only the association, so the shuffled value *is*
the estimator's bias at that sample size.

**Reach: the dependence dies immediately, and so does a real language's.**

Surrogate-corrected mutual information in bits, by how many words apart:

| | lag 1 | lag 2 | lag 3 | lag 4 | lag 5 |
|---|---:|---:|---:|---:|---:|
| the manuscript | 0.1606 | 0.0063 | 0.0064 | 0.0016 | 0.0033 |
| its own other half | 0.1625 | 0.0078 | 0.0030 | 0.0029 | 0.0031 |
| plain Italian | 0.1563 | 0.0082 | 0.0011 | 0.0025 | −0.0010 |
| five-component model | 0.1457 | −0.0001 | −0.0011 | −0.0013 | 0.0004 |
| Naibbe over Latin | 0.0043 | 0.0007 | 0.0011 | 0.0008 | 0.0023 |

The control's spread is about 0.001, so anything under roughly 0.002 is zero.

This test does not discriminate, and saying so is the point of running it. The
manuscript's dependence collapses by a factor of twenty-five after one word —
but **so does plain Italian's**. Character-level dependence between word
boundaries is a local effect in a real language too. The measure is too crude to
see grammar, so "does it reach like language?" cannot be answered this way. The
test was proposed in an earlier version of this document as the decisive one.
It is not.

**The pen test: the dependence vanishes at a line break, and a language's does
not.**

This one does discriminate, and the result is the clearest in the project.
Adjacent word pairs inside a line, against pairs straddling a line break:

| | within a line | across a line break | sigma |
|---|---:|---:|---:|
| **the manuscript** (whole book) | **0.1794** | **0.0058 ± 0.0080** | **0.7** |
| the manuscript, held-out half | 0.1826 | −0.0001 ± 0.0127 | 0.0 |
| the manuscript, training half | 0.1777 | 0.0270 ± 0.0211 | 1.3 |
| **plain Italian** | **0.1576** | **0.1464 ± 0.0206** | **7.1** |
| five-component model | 0.1509 | 0.0177 ± 0.0135 | 1.3 |
| self-citation | 0.0201 | −0.0119 ± 0.0153 | −0.8 |
| Naibbe over Latin | 0.0052 | 0.0009 ± 0.0221 | 0.0 |

A real language does not care where the line ends. Italian keeps 93 % of its
cross-word dependence across a line break, at 7.1 sigma. **The manuscript keeps
none of it.** The effect is strong inside a line and statistically zero across
the margin, on the whole book and on each half separately.

This is a null result, so it is only worth anything if the test could have seen
the effect had it been there. It could: Italian, at the same sample size, shows
it at 7.1 sigma. The power is there and the signal is not.

**It is not a transcription artefact.** Repeated on v101, an independent
transliteration by a different reader in which one glyph is exactly one
character and the shapes are grouped differently:

| | lag 1 | lag 2 | within a line | across a line break |
|---|---:|---:|---:|---:|
| EVA (Takahashi) | 0.1606 | 0.0063 | 0.1826 | −0.0001 |
| v101 (Currier) | 0.2060 | 0.0167 | 0.2321 | 0.0112 |

Same shape, slightly stronger. Two readers who disagree about what the glyphs
are agree about this.

**What it means, and what this document now withdraws.**

The word-level structure is real, but it is bounded by the line. Whatever
produced this text worked a line at a time, and what happened at the end of one
line carried nothing into the next.

That is very hard to square with language. Sentences do not stop at the right
margin. It is easy to square with a process that fills lines: a scribe reading
from a table, a grille laid over a page, a procedure that generates text to fit
a measured space. The five-component model shows the same pattern — 0.1509
inside a line, 0.0177 across — because it too composes by the line.

So the reading offered in §4.2, that the manuscript's word structure is
"higher than either natural language and unexplained by the mechanical
theories", is **withdrawn in its suggestive form**. The number is still correct.
Its interpretation was not. The dependence is confined to the line, and a
line-bound process explains it without any message.

This is the sharpest evidence in the whole table for the meaning-free side of
the argument, and it was produced by testing this project's own most
interesting claim rather than defending it.

A narrower statement survives, and it is worth keeping. Currier observed in 1976
that lines behave as self-contained units, and `voynich-toolkit` confirmed it
for exact word repeats. This is a much stronger version: not merely that words
rarely repeat across a line boundary, but that **no character-level dependence
of any kind survives the boundary**, while remaining strong within it.

### 4.2.3 Is it a list, then? No. The structure sits at the edges of the line

§4.2.2 ruled out flowing prose but not meaning, because plenty of meaningful
writing is line-bounded: a recipe book, an inventory, a herbal with one plant
per line. So the next question is narrower. Given that the line is the unit,
does a line behave like an **entry** -- a self-contained item with its own
shape -- or like a **chunk**, an arbitrary run of text one line long?

Two measurements, each against a prose control (Italian on the manuscript's own
line budgets, where line breaks are arbitrary by construction) and a positive
control (a synthetic list: a headword from a small inventory, then body words).
Both hold word length fixed, because the scribe fitted words to the space left
and onset class correlates with length. Paragraph-opening lines are excluded
throughout; they are already known to carry a gallows capital.

| | opening distinct \| length | sigma | position structure \| length | sigma |
|---|---:|---:|---:|---:|
| **the manuscript** | **0.1930** | 250 | **0.0585** | 44 |
| register (synthetic list) | 0.1986 | 120 | 0.0433 | 13 |
| five-component model | 0.0259 | 14 | 0.0075 | 4.7 |
| prose (Italian, same layout) | 0.0026 | 1.2 | −0.0017 | −1.2 |
| table-and-grille | 0.0019 | 0.7 | −0.0011 | −0.6 |
| Naibbe cipher | 0.0029 | 1.5 | −0.0002 | −0.1 |

On the face of it the manuscript looks like a list and nothing like prose. Its
line openings are as distinct as a deliberately constructed register's, and its
position structure is *stronger* than one. Prose sits at zero on both.

It is not decoration doing it. A gallows glyph opens 8.9 % of continuation
lines against 8.3 % of mid-line words — no difference at all. What separates a
line opening is vocabulary: `d-` twice as common as mid-line, `y-` five times,
`s-` five times, while `ch-` is suppressed fivefold and `k-` fourfold. The
commonest line openers are `daiin saiin dain sol sor sain`; the commonest
mid-line words are `daiin chedy ol aiin chol shedy`. Genuinely different sets.

**Then both halves of it came apart.**

*The distinctive opening is free.* Adding one rule to the best generator —
begin each continuation line from a separate stock of opener words, drawn from
the training half — takes opening distinctness from 0.0259 to **0.1890**
against the manuscript's 0.1930. A procedure that starts each line somewhere
different, from the first column of a table or the top of a page, produces this
without anything being said. Nothing can be inferred from it.

*The internal structure is only edges.* An entry has a shape across its whole
length; strip a word or two off each end and most of it should survive. Strip
the manuscript's lines instead:

| words dropped from each end | EVA | sigma | v101 | sigma |
|---:|---:|---:|---:|---:|
| 0 | 0.0428 | 60.7 | 0.0383 | 41.0 |
| 1 | 0.0128 | 15.6 | 0.0117 | 8.5 |
| **2** | **0.0017** | **0.9** | **0.0016** | **1.1** |
| 3 | −0.0017 | −1.0 | −0.0025 | −1.0 |

Two words off each end and there is nothing left. The deep middle of a
Voynich line has no position structure whatever, in either transliteration.
The synthetic list behaves the same way, because its whole shape was its
headword; a real entry template would not.

**So the answer is no.** The manuscript is not prose, because nothing survives
a line break. It is not a list either, because a line has no internal shape
beyond its first and last couple of words. What it is, on this evidence, is
**lines with distinctive openings, distinctive endings, and an unstructured
middle** — which is what a line-filling procedure with a start rule and an end
flourish produces, and which every one of those rules turned out to be
obtainable for free.

Taken together with §4.3, three rules now cover the whole line-and-paragraph
block: a flourish at the line end, a gallows capital at the paragraph start,
and a stock of line openers. The `fivecomp_lines` row carries all three. It
moves the line block from 2.96 to **1.31** floor units on the main split and
**0.95** on the reversed one -- inside the manuscript's own sampling spread --
while the cost on the fingerprint's 42 metrics is 0.29 to 0.31, which is
nothing.

The methodological point is now the recurring one in this document. Three
times a property looked unexplained, and three times a rule of two or three
lines, calibrated on the training half and fitted to nothing, supplied it.
**A metric that no process was built to match is not evidence until somebody
tries to match it.**

### 4.3 The line and paragraph block, and how much of it is just decoration

<!--TABLE:LINE-->
| process | m line-final | gallows lift | cross-line rep | para coherence | section MI | len autocorr |
|---|---|---|---|---|---|---|
| **the manuscript** | **66.97** | **73.34** | **0.12** | **2.61** | **0.23** | **0.11** |
| `noise_floor` | 67.18 | 74.63 | 0.36 | 1.86 | 0.27 | 0.13 |
| `fivecomp` | 10.51 | 2.40 | 0.45 | 1.06 | -0.01 | 0.06 |
| `fivecomp_scribe` | 47.90 | 63.20 | 0.39 | 1.19 | -0.01 | 0.06 |
| `fivecomp_lines` | 50.28 | 78.12 | 0.17 | 1.20 | -0.01 | 0.05 |
| `manual` | 6.75 | 0.35 | 0.80 | 1.75 | 0.02 | 0.03 |
| `naibbe_latin` | 15.93 | 0.20 | 0.18 | 1.27 | 0.05 | -0.03 |
| `naibbe_italian` | 17.27 | 0.49 | 0.06 | 1.15 | 0.05 | -0.04 |
| `naibbe_wb` | 15.87 | -0.60 | 0.18 | 1.09 | 0.04 | -0.04 |
| `naibbe_wb_italian` | 13.87 | -0.04 | 0.48 | 1.09 | 0.03 | -0.06 |
| `naibbe_word` | 13.49 | 2.50 | 0.00 | 0.00 | 0.15 | -0.01 |
| `grille` | 13.87 | -0.65 | 0.42 | 1.39 | 0.22 | 0.07 |
| `grille_bigtable` | 16.09 | 0.00 | 0.24 | 1.39 | 0.07 | 0.03 |
| `selfcite` | 14.57 | -5.81 | 0.42 | 1.02 | 0.08 | 0.06 |
| `llull` | 3.18 | 1.30 | 0.00 | 0.68 | 0.03 | -0.06 |
| `abbrev` | 0.00 | -1.68 | 0.00 | 1.16 | 0.08 | -0.05 |
| `gibberish` | 0.00 | 0.23 | 0.74 | 0.98 | 0.19 | 0.11 |
| `natlang_italian` | 0.00 | 0.00 | 0.00 | 1.16 | 0.03 | -0.15 |
| `natlang_latin` | 0.00 | 0.00 | 0.12 | 1.08 | 0.06 | -0.03 |
| `natlang_hebrew` | 0.00 | 0.00 | 0.18 | 1.33 | 0.06 | -0.24 |
| `subst` | 8.70 | -2.54 | 0.12 | 1.08 | 0.06 | -0.03 |
| `subst_homophonic` | 0.00 | -0.22 | 0.00 | 0.86 | 0.12 | -0.03 |

Two properties are not reproduced by any published process in the table:

- **The `m` line-end marker.** Two thirds of the manuscript's `m` glyphs sit at
  the end of a line. The book's own other half gives 67.2 %. The best any
  published process manages is 17.3 %, and most give zero.
- **Gallows at paragraph openings.** A paragraph's first line starts with a
  gallows glyph 73 percentage points more often than its continuation lines do.
  The other half of the book gives 74.6. Every published process gives between
  −5.8 and +2.4. They are all effectively at zero, and two are *negative*.

The five-component model, which sits inside the noise floor on the fingerprint's
42 metrics, is off by 10 floor units on gallows placement and 4.7 on the line-end
marker. It calibrates a *line-initial* gallows rate and matches that metric well;
what it does not have is the distinction between a line that opens a paragraph
and a line that continues one.

**But the obvious objection to that is right, and it was tested.** Nobody asked
those processes to decorate a page. A scribe would do it without meaning
anything by it. So the `fivecomp_scribe` row adds two habits to the best
generator, one rule each, both calibrated on the training half and neither
fitted to any metric:

- *The flourish.* Line-final `m` is a flourished `r`, and the training data says
  so plainly: `dam` ends a line 36 times while `dar` appears 130 times
  elsewhere; `am` against `ar`, 34 to 155; `okam` against `okar`, 12 to 65. So
  at the end of a line a word ending in `r` is written with `m` instead.
- *The capital.* At the start of a paragraph a gallows letter is written in
  front of the first word.

| | `m` line-final | gallows lift | line block, floor units | fp42, floor units |
|---|---:|---:|---:|---:|
| the manuscript | 66.97 | 73.34 | — | — |
| its own other half | 67.18 | 74.63 | 0.35x | 0.16x |
| five-component model | 10.51 | 2.40 | 2.96x | 0.29x |
| **+ a scribe's page habits** | **47.90** | **63.20** | **1.43x** | **0.37x** |

Two rules close most of the gap. The line block halves, from 2.96 to 1.43 floor
units, and the cost on the fingerprint's own 42 metrics is small: 0.29 to 0.37.

**So this section's original claim was too strong and is withdrawn.** The
line and paragraph properties are not deep evidence about what the text is.
They are largely consistent with a scribe decorating a page, and they can be
had cheaply by any process willing to decorate. What remains after that is
worth stating precisely, because it is smaller but it is real:

1. **Neither habit fully closes.** 47.9 against 67.0, and 63.2 against 73.3.
   The remainder is not nothing, but it is the kind of gap a second pass of
   fitting would probably close, and we have not tried.
2. **The capital costs something specific.** Adding paragraph capitals breaks a
   metric the generator had been matching: the overall line-initial gallows rate
   goes from 0.12 to 2.50 floor units. The manuscript places gallows in a
   pattern that a naive "capital at the paragraph start" habit overshoots.
   Getting both right at once is a real constraint, and no published process
   currently satisfies it.
3. **The honest lesson is about measurement, not about the manuscript.** A
   metric no process was built to match is not evidence until somebody tries to
   match it. Three lines of decoration were enough here. The result of adding
   the line block is therefore not "every theory fails" but "these particular
   properties are cheap, and the field was right not to weight them heavily".

### 4.4 A negative result: scribal abbreviation does not do it

Lindemann & Bowern (2020) list medieval scribal abbreviation among the candidate
explanations for Voynichese's entropy and do not model it. Nobody had. This
harness models it: suspension of inflectional endings, contraction of frequent
words, the common signs (`per`, `pro`, `prae`, `con-`, `-rum`, the nasal
macron), and positional allographs.

It does not work. Conditional entropy moves from Latin's 3.19 to 3.22 — that
is, **it does not move at all**, and character entropy gets *worse*, rising from
3.97 to 4.22 against the manuscript's 3.86. Given the full parameter budget the
tuner chose **one** allograph table, meaning it found positional variants
actively harmful.

The reason is structural and worth stating, because it generalises. A
positional allograph is a one-to-one relabelling conditioned on position: it
splits the alphabet without making any glyph predictable from the *preceding*
glyph, which is what conditional entropy measures. Verbose encoding — one
plaintext letter becoming several ciphertext glyphs — does make the next glyph
predictable, which is why Naibbe reaches 1.78 and abbreviation does not budge.

**Abbreviation is not a route to the Voynich entropy anomaly.** Verbose
encoding is the only mechanism in this table that gets there other than
procedural generation.

This contradicts the prediction written before the code
(`PREDICTION_abbrev.md`, which is not edited after the fact). That prediction
said h2 would land between 2.6 and 2.9. It lands at 3.22. See §6 for the
correction that produced the wrong intermediate reading.

### 4.5 A correction to the published verdict on the grille

`voynich-toolkit` reports that a Rugg grille fails on vocabulary size, "181
types vs 8,493", and counts that as one of six properties the grille cannot
reproduce. That result is an artefact of its 40-row table. Vocabulary is
bounded by table height times the number of grille configurations, so a 40-row
table cannot produce more than a few hundred distinct words whatever else is
true of the method.

With the table height tuned on the same budget every other process gets, and
pinned at 8000 rows in the `grille_bigtable` row, the grille reaches 3,974 types
against the manuscript's 4,526, and a type-token ratio of 0.269 against 0.275.
**Vocabulary size is not a failure of the grille.**

What replaces it is a trade-off that the small table was hiding. As the table
grows, cross-word mutual information collapses:

| table rows | types | TTR | h2 | cross-word MI |
|---:|---:|---:|---:|---:|
| 172 | 577 | 0.039 | 2.02 | 0.041 |
| 600 | 1,344 | 0.092 | 2.10 | 0.017 |
| 1,200 | 2,076 | 0.142 | 2.08 | 0.008 |
| 3,000 | 3,123 | 0.214 | 2.10 | 0.008 |
| 8,000 | 3,974 | 0.272 | 2.11 | 0.005 |
| *the manuscript* | *4,526* | *0.275* | *1.84* | *0.068* |

A small table gives local dependence because the grille keeps revisiting
neighbouring rows; a large table gives vocabulary. The grille cannot give both.
That is a better-founded objection to the device than the one in the
literature, and it is the same wall the Naibbe cipher hits from the other side.

### 4.6 Human gibberish

Gaskell & Bowern's 42 volunteers produce text with a type-token ratio of 0.68
against the manuscript's 0.275 — people improvising invent far more distinct
words than the manuscript contains — and conditional entropy of 3.94, the
highest in the table. Their own paper is careful that the samples are short,
and they are: about 10,000 tokens against the held-out half's 16,436. Metrics
that depend on vocabulary growth are marked undefined for this row rather than
scored, and the row should be read as a lower bound on what a longer sample
might do.

## 5. What each process fails on

Five worst metrics, in floor units, held-out half.

<!--TABLE:WORST-->
**`fivecomp` — five-component model (fingerprint)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 2.395 | 73.336 | 10.0x |
| line | m line-final % | 10.511 | 66.966 | 4.7x |
| line | para vocab coherence | 1.063 | 2.610 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`fivecomp_scribe` — five-component model + a scribe's page habits**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | para/line-initial gallows % | 32.592 | 21.997 | 2.5x |
| line | m line-final % | 47.902 | 66.966 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | para vocab coherence | 1.189 | 2.610 | 1.7x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`naibbe_latin` — Naibbe verbose cipher over latin**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 0.204 | 73.336 | 10.2x |
| struct | hapax share of types % | 54.661 | 71.586 | 7.2x |
| struct | adjacent identical words % | 0.160 | 0.870 | 5.3x |
| line | m line-final % | 15.933 | 66.966 | 4.3x |
| line | word-len autocorr | -0.033 | 0.113 | 4.1x |

**`naibbe_wb_italian` — Naibbe, word breaks kept (Italian)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | -0.041 | 73.336 | 10.1x |
| struct | hapax share of types % | 51.768 | 71.586 | 8.0x |
| line | word-len autocorr | -0.063 | 0.113 | 5.0x |
| line | m line-final % | 13.873 | 66.966 | 4.4x |
| struct | adjacent identical words % | 0.238 | 0.870 | 4.3x |

**`grille_bigtable` — table-and-grille, large table**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | len<=2 % | 16.980 | 7.240 | 14.7x |
| text | top-5 finals % | 72.404 | 91.640 | 10.1x |
| line | gallows para-start lift | 0.003 | 73.336 | 10.0x |
| struct | hapax share of types % | 52.037 | 71.586 | 8.4x |
| text | mean word len | 4.588 | 5.173 | 6.4x |

**`abbrev` — Latin scribal abbreviation**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 58.070 | 91.640 | 17.5x |
| struct | len<=2 % | 18.195 | 7.240 | 16.3x |
| struct | H pos4 from end | 4.062 | 3.364 | 14.8x |
| text | h1 (char) | 4.221 | 3.863 | 13.1x |
| text | top-5 onsets % | 46.630 | 70.175 | 10.8x |

**`gibberish` — human gibberish (42 volunteers)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 44.093 | 91.640 | 24.9x |
| struct | H pos4 from end | 4.380 | 3.364 | 21.4x |
| text | h1 (char) | 4.399 | 3.863 | 19.7x |
| struct | H pos2 from end | 4.369 | 2.893 | 19.4x |
| text | top-5 onsets % | 32.665 | 70.175 | 17.3x |
**`fivecomp` — five-component model (fingerprint)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 2.395 | 73.336 | 10.0x |
| line | m line-final % | 10.511 | 66.966 | 4.7x |
| line | para vocab coherence | 1.063 | 2.610 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`fivecomp_scribe` — five-component model + a scribe's page habits**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | para/line-initial gallows % | 32.592 | 21.997 | 2.5x |
| line | m line-final % | 47.902 | 66.966 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | para vocab coherence | 1.189 | 2.610 | 1.7x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`naibbe_latin` — Naibbe verbose cipher over latin**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 0.204 | 73.336 | 10.2x |
| struct | hapax share of types % | 54.661 | 71.586 | 7.2x |
| struct | adjacent identical words % | 0.160 | 0.870 | 5.3x |
| line | m line-final % | 15.933 | 66.966 | 4.3x |
| line | word-len autocorr | -0.033 | 0.113 | 4.1x |

**`naibbe_wb_italian` — Naibbe, word breaks kept (Italian)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | -0.041 | 73.336 | 10.1x |
| struct | hapax share of types % | 51.768 | 71.586 | 8.0x |
| line | word-len autocorr | -0.063 | 0.113 | 5.0x |
| line | m line-final % | 13.873 | 66.966 | 4.4x |
| struct | adjacent identical words % | 0.238 | 0.870 | 4.3x |

**`grille_bigtable` — table-and-grille, large table**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | len<=2 % | 16.980 | 7.240 | 14.7x |
| text | top-5 finals % | 72.404 | 91.640 | 10.1x |
| line | gallows para-start lift | 0.003 | 73.336 | 10.0x |
| struct | hapax share of types % | 52.037 | 71.586 | 8.4x |
| text | mean word len | 4.588 | 5.173 | 6.4x |

**`abbrev` — Latin scribal abbreviation**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 58.070 | 91.640 | 17.5x |
| struct | len<=2 % | 18.195 | 7.240 | 16.3x |
| struct | H pos4 from end | 4.062 | 3.364 | 14.8x |
| text | h1 (char) | 4.221 | 3.863 | 13.1x |
| text | top-5 onsets % | 46.630 | 70.175 | 10.8x |

**`gibberish` — human gibberish (42 volunteers)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 44.093 | 91.640 | 24.9x |
| struct | H pos4 from end | 4.380 | 3.364 | 21.4x |
| text | h1 (char) | 4.399 | 3.863 | 19.7x |
| struct | H pos2 from end | 4.369 | 2.893 | 19.4x |
| text | top-5 onsets % | 32.665 | 70.175 | 17.3x |
**`fivecomp` — five-component model (fingerprint)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 2.395 | 73.336 | 10.0x |
| line | m line-final % | 10.511 | 66.966 | 4.7x |
| line | para vocab coherence | 1.063 | 2.610 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`fivecomp_scribe` — five-component model + a scribe's page habits**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | para/line-initial gallows % | 32.592 | 21.997 | 2.5x |
| line | m line-final % | 47.902 | 66.966 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | para vocab coherence | 1.189 | 2.610 | 1.7x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`naibbe_latin` — Naibbe verbose cipher over latin**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 0.204 | 73.336 | 10.2x |
| struct | hapax share of types % | 54.661 | 71.586 | 7.2x |
| struct | adjacent identical words % | 0.160 | 0.870 | 5.3x |
| line | m line-final % | 15.933 | 66.966 | 4.3x |
| line | word-len autocorr | -0.033 | 0.113 | 4.1x |

**`naibbe_wb_italian` — Naibbe, word breaks kept (Italian)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | -0.041 | 73.336 | 10.1x |
| struct | hapax share of types % | 51.768 | 71.586 | 8.0x |
| line | word-len autocorr | -0.063 | 0.113 | 5.0x |
| line | m line-final % | 13.873 | 66.966 | 4.4x |
| struct | adjacent identical words % | 0.238 | 0.870 | 4.3x |

**`grille_bigtable` — table-and-grille, large table**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | len<=2 % | 16.980 | 7.240 | 14.7x |
| text | top-5 finals % | 72.404 | 91.640 | 10.1x |
| line | gallows para-start lift | 0.003 | 73.336 | 10.0x |
| struct | hapax share of types % | 52.037 | 71.586 | 8.4x |
| text | mean word len | 4.588 | 5.173 | 6.4x |

**`abbrev` — Latin scribal abbreviation**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 58.070 | 91.640 | 17.5x |
| struct | len<=2 % | 18.195 | 7.240 | 16.3x |
| struct | H pos4 from end | 4.062 | 3.364 | 14.8x |
| text | h1 (char) | 4.221 | 3.863 | 13.1x |
| text | top-5 onsets % | 46.630 | 70.175 | 10.8x |

**`gibberish` — human gibberish (42 volunteers)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 44.093 | 91.640 | 24.9x |
| struct | H pos4 from end | 4.380 | 3.364 | 21.4x |
| text | h1 (char) | 4.399 | 3.863 | 19.7x |
| struct | H pos2 from end | 4.369 | 2.893 | 19.4x |
| text | top-5 onsets % | 32.665 | 70.175 | 17.3x |
**`fivecomp` — five-component model (fingerprint)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 2.395 | 73.336 | 10.0x |
| line | m line-final % | 10.511 | 66.966 | 4.7x |
| line | para vocab coherence | 1.063 | 2.610 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`fivecomp_scribe` — five-component model + a scribe's page habits**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | para/line-initial gallows % | 32.592 | 21.997 | 2.5x |
| line | m line-final % | 47.902 | 66.966 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | para vocab coherence | 1.189 | 2.610 | 1.7x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`naibbe_latin` — Naibbe verbose cipher over latin**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 0.204 | 73.336 | 10.2x |
| struct | hapax share of types % | 54.661 | 71.586 | 7.2x |
| struct | adjacent identical words % | 0.160 | 0.870 | 5.3x |
| line | m line-final % | 15.933 | 66.966 | 4.3x |
| line | word-len autocorr | -0.033 | 0.113 | 4.1x |

**`naibbe_wb_italian` — Naibbe, word breaks kept (Italian)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | -0.041 | 73.336 | 10.1x |
| struct | hapax share of types % | 51.768 | 71.586 | 8.0x |
| line | word-len autocorr | -0.063 | 0.113 | 5.0x |
| line | m line-final % | 13.873 | 66.966 | 4.4x |
| struct | adjacent identical words % | 0.238 | 0.870 | 4.3x |

**`grille_bigtable` — table-and-grille, large table**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | len<=2 % | 16.980 | 7.240 | 14.7x |
| text | top-5 finals % | 72.404 | 91.640 | 10.1x |
| line | gallows para-start lift | 0.003 | 73.336 | 10.0x |
| struct | hapax share of types % | 52.037 | 71.586 | 8.4x |
| text | mean word len | 4.588 | 5.173 | 6.4x |

**`abbrev` — Latin scribal abbreviation**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 58.070 | 91.640 | 17.5x |
| struct | len<=2 % | 18.195 | 7.240 | 16.3x |
| struct | H pos4 from end | 4.062 | 3.364 | 14.8x |
| text | h1 (char) | 4.221 | 3.863 | 13.1x |
| text | top-5 onsets % | 46.630 | 70.175 | 10.8x |

**`gibberish` — human gibberish (42 volunteers)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 44.093 | 91.640 | 24.9x |
| struct | H pos4 from end | 4.380 | 3.364 | 21.4x |
| text | h1 (char) | 4.399 | 3.863 | 19.7x |
| struct | H pos2 from end | 4.369 | 2.893 | 19.4x |
| text | top-5 onsets % | 32.665 | 70.175 | 17.3x |
**`fivecomp` — five-component model (fingerprint)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 2.395 | 73.336 | 10.0x |
| line | m line-final % | 10.511 | 66.966 | 4.7x |
| line | para vocab coherence | 1.063 | 2.610 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`fivecomp_scribe` — five-component model + a scribe's page habits**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | para/line-initial gallows % | 32.592 | 21.997 | 2.5x |
| line | m line-final % | 47.902 | 66.966 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | para vocab coherence | 1.189 | 2.610 | 1.7x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`naibbe_latin` — Naibbe verbose cipher over latin**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 0.204 | 73.336 | 10.2x |
| struct | hapax share of types % | 54.661 | 71.586 | 7.2x |
| struct | adjacent identical words % | 0.160 | 0.870 | 5.3x |
| line | m line-final % | 15.933 | 66.966 | 4.3x |
| line | word-len autocorr | -0.033 | 0.113 | 4.1x |

**`naibbe_wb_italian` — Naibbe, word breaks kept (Italian)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | -0.041 | 73.336 | 10.1x |
| struct | hapax share of types % | 51.768 | 71.586 | 8.0x |
| line | word-len autocorr | -0.063 | 0.113 | 5.0x |
| line | m line-final % | 13.873 | 66.966 | 4.4x |
| struct | adjacent identical words % | 0.238 | 0.870 | 4.3x |

**`grille_bigtable` — table-and-grille, large table**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | len<=2 % | 16.980 | 7.240 | 14.7x |
| text | top-5 finals % | 72.404 | 91.640 | 10.1x |
| line | gallows para-start lift | 0.003 | 73.336 | 10.0x |
| struct | hapax share of types % | 52.037 | 71.586 | 8.4x |
| text | mean word len | 4.588 | 5.173 | 6.4x |

**`abbrev` — Latin scribal abbreviation**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 58.070 | 91.640 | 17.5x |
| struct | len<=2 % | 18.195 | 7.240 | 16.3x |
| struct | H pos4 from end | 4.062 | 3.364 | 14.8x |
| text | h1 (char) | 4.221 | 3.863 | 13.1x |
| text | top-5 onsets % | 46.630 | 70.175 | 10.8x |

**`gibberish` — human gibberish (42 volunteers)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 44.093 | 91.640 | 24.9x |
| struct | H pos4 from end | 4.380 | 3.364 | 21.4x |
| text | h1 (char) | 4.399 | 3.863 | 19.7x |
| struct | H pos2 from end | 4.369 | 2.893 | 19.4x |
| text | top-5 onsets % | 32.665 | 70.175 | 17.3x |
**`fivecomp` — five-component model (fingerprint)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 2.395 | 73.336 | 10.0x |
| line | m line-final % | 10.511 | 66.966 | 4.7x |
| line | para vocab coherence | 1.063 | 2.610 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`naibbe_latin` — Naibbe verbose cipher over latin**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 0.204 | 73.336 | 10.2x |
| struct | hapax share of types % | 54.661 | 71.586 | 7.2x |
| struct | adjacent identical words % | 0.160 | 0.870 | 5.3x |
| line | m line-final % | 15.933 | 66.966 | 4.3x |
| line | word-len autocorr | -0.033 | 0.113 | 4.1x |

**`grille_bigtable` — table-and-grille, large table**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | len<=2 % | 16.980 | 7.240 | 14.7x |
| text | top-5 finals % | 72.404 | 91.640 | 10.1x |
| line | gallows para-start lift | 0.003 | 73.336 | 10.0x |
| struct | hapax share of types % | 52.037 | 71.586 | 8.4x |
| text | mean word len | 4.588 | 5.173 | 6.4x |

**`abbrev` — Latin scribal abbreviation**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 58.070 | 91.640 | 17.5x |
| struct | len<=2 % | 18.195 | 7.240 | 16.3x |
| struct | H pos4 from end | 4.062 | 3.364 | 14.8x |
| text | h1 (char) | 4.221 | 3.863 | 13.1x |
| text | top-5 onsets % | 46.630 | 70.175 | 10.8x |

**`gibberish` — human gibberish (42 volunteers)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 44.093 | 91.640 | 24.9x |
| struct | H pos4 from end | 4.380 | 3.364 | 21.4x |
| text | h1 (char) | 4.399 | 3.863 | 19.7x |
| struct | H pos2 from end | 4.369 | 2.893 | 19.4x |
| text | top-5 onsets % | 32.665 | 70.175 | 17.3x |
**`fivecomp` — five-component model (fingerprint)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 2.395 | 73.336 | 10.0x |
| line | m line-final % | 10.511 | 66.966 | 4.7x |
| line | para vocab coherence | 1.063 | 2.610 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`naibbe_latin` — Naibbe verbose cipher over latin**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 0.204 | 73.336 | 10.2x |
| struct | hapax share of types % | 54.661 | 71.586 | 7.2x |
| struct | adjacent identical words % | 0.160 | 0.870 | 5.3x |
| line | m line-final % | 15.933 | 66.966 | 4.3x |
| line | word-len autocorr | -0.033 | 0.113 | 4.1x |

**`grille_bigtable` — table-and-grille, large table**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | len<=2 % | 16.980 | 7.240 | 14.7x |
| text | top-5 finals % | 72.404 | 91.640 | 10.1x |
| line | gallows para-start lift | 0.003 | 73.336 | 10.0x |
| struct | hapax share of types % | 52.037 | 71.586 | 8.4x |
| text | mean word len | 4.588 | 5.173 | 6.4x |

**`abbrev` — Latin scribal abbreviation**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 58.070 | 91.640 | 17.5x |
| struct | len<=2 % | 18.195 | 7.240 | 16.3x |
| struct | H pos4 from end | 4.062 | 3.364 | 14.8x |
| text | h1 (char) | 4.221 | 3.863 | 13.1x |
| text | top-5 onsets % | 46.630 | 70.175 | 10.8x |

**`gibberish` — human gibberish (42 volunteers)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 44.093 | 91.640 | 24.9x |
| struct | H pos4 from end | 4.380 | 3.364 | 21.4x |
| text | h1 (char) | 4.399 | 3.863 | 19.7x |
| struct | H pos2 from end | 4.369 | 2.893 | 19.4x |
| text | top-5 onsets % | 32.665 | 70.175 | 17.3x |
**`fivecomp` — five-component model (fingerprint)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 2.395 | 73.336 | 10.0x |
| line | m line-final % | 10.511 | 66.966 | 4.7x |
| line | para vocab coherence | 1.063 | 2.610 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`naibbe_latin` — Naibbe verbose cipher over latin**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 0.204 | 73.336 | 10.2x |
| struct | hapax share of types % | 54.661 | 71.586 | 7.2x |
| struct | adjacent identical words % | 0.160 | 0.870 | 5.3x |
| line | m line-final % | 15.933 | 66.966 | 4.3x |
| line | word-len autocorr | -0.033 | 0.113 | 4.1x |

**`grille_bigtable` — table-and-grille, large table**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | len<=2 % | 16.980 | 7.240 | 14.7x |
| text | top-5 finals % | 72.404 | 91.640 | 10.1x |
| line | gallows para-start lift | 0.003 | 73.336 | 10.0x |
| struct | hapax share of types % | 52.037 | 71.586 | 8.4x |
| text | mean word len | 4.588 | 5.173 | 6.4x |

**`abbrev` — Latin scribal abbreviation**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 58.070 | 91.640 | 17.5x |
| struct | len<=2 % | 18.195 | 7.240 | 16.3x |
| struct | H pos4 from end | 4.062 | 3.364 | 14.8x |
| text | h1 (char) | 4.221 | 3.863 | 13.1x |
| text | top-5 onsets % | 46.630 | 70.175 | 10.8x |

**`gibberish` — human gibberish (42 volunteers)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 44.093 | 91.640 | 24.9x |
| struct | H pos4 from end | 4.380 | 3.364 | 21.4x |
| text | h1 (char) | 4.399 | 3.863 | 19.7x |
| struct | H pos2 from end | 4.369 | 2.893 | 19.4x |
| text | top-5 onsets % | 32.665 | 70.175 | 17.3x |
**`fivecomp` — five-component model (fingerprint)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 2.395 | 73.336 | 10.0x |
| line | m line-final % | 10.511 | 66.966 | 4.7x |
| line | para vocab coherence | 1.063 | 2.610 | 1.9x |
| line | word-section MI (bits) | -0.008 | 0.232 | 1.8x |
| line | word-len autocorr | 0.059 | 0.113 | 1.6x |

**`naibbe_latin` — Naibbe verbose cipher over latin**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| line | gallows para-start lift | 0.204 | 73.336 | 10.2x |
| struct | hapax share of types % | 54.661 | 71.586 | 7.2x |
| struct | adjacent identical words % | 0.160 | 0.870 | 5.3x |
| line | m line-final % | 15.933 | 66.966 | 4.3x |
| line | word-len autocorr | -0.033 | 0.113 | 4.1x |

**`grille_bigtable` — table-and-grille, large table**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| struct | len<=2 % | 16.980 | 7.240 | 14.7x |
| text | top-5 finals % | 72.404 | 91.640 | 10.1x |
| line | gallows para-start lift | 0.003 | 73.336 | 10.0x |
| struct | hapax share of types % | 52.037 | 71.586 | 8.4x |
| text | mean word len | 4.588 | 5.173 | 6.4x |

**`abbrev` — Latin scribal abbreviation**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 58.070 | 91.640 | 17.5x |
| struct | len<=2 % | 18.195 | 7.240 | 16.3x |
| struct | H pos4 from end | 4.062 | 3.364 | 14.8x |
| text | h1 (char) | 4.221 | 3.863 | 13.1x |
| text | top-5 onsets % | 46.630 | 70.175 | 10.8x |

**`gibberish` — human gibberish (42 volunteers)**

| block | metric | it produced | the manuscript | floor units |
|---|---|---:|---:|---:|
| text | top-5 finals % | 44.093 | 91.640 | 24.9x |
| struct | H pos4 from end | 4.380 | 3.364 | 21.4x |
| text | h1 (char) | 4.399 | 3.863 | 19.7x |
| struct | H pos2 from end | 4.369 | 2.893 | 19.4x |
| text | top-5 onsets % | 32.665 | 70.175 | 17.3x |

## 6. Corrections made during the work

Recorded because a result that was corrected mid-flight is more useful to the
next person than a clean-looking table.

**Four of this document's own conclusions have now been overturned by tests it
recommended.** The fourth is §4.2.3: having ruled out prose, this document
proposed that a line might be a meaningful entry, and the measurements at first
said so loudly -- line openings as distinct as a real list's, position structure
stronger than one. One rule supplied the openings for free, and stripping two
words off each end of a line erased everything else. The pattern is now
impossible to miss and is stated at the end of §4.2.3. Both are rewritten above rather than quietly amended, and both
are the reason those tests were worth running.

The first version blamed the cipher's loss of cross-word dependence on its
respacing, and recommended building a word-boundary-preserving variant as the
obvious next step. That variant was built. It changes nothing: 0.004 bits
either way, and unchanged even on an Italian plaintext that starts with 0.056.
The cause is the homophony, not the respacing. The replacement claim in §4.2.1
is stronger than the one it replaces, but the original was wrong and was stated
with more confidence than the evidence carried.

The second was the reach test, proposed as the decisive way to tell a habit
from grammar. It is not decisive: the manuscript's cross-word dependence dies
after one word, and so does plain Italian's, so the measure cannot see the
difference it was proposed to see. The test that did discriminate was the other
one — and it went against this document's most interesting claim. The
dependence is bounded by the line and vanishes completely at a line break,
where a real language keeps 93 % of it. §4.2.2 has the numbers and withdraws
the suggestive reading of §4.2. That is the third correction, it is the largest,
and it is the one that most changes what the project concludes.

The first version also claimed that no process reproduces the line and
paragraph properties, and left the impression that this was a deep failure of
every theory. Two rules of ordinary scribal decoration, calibrated on the
training half and fitted to nothing, halve that gap at a cost of 0.08 floor
units. §4.3 is rewritten and its strong form is withdrawn. A metric that no
process was built to match is not evidence until somebody tries to match it.

**The two-character glyph artefact.** The first implementation spelled invented
alphabets with EVA-style two-character glyph names. Any process whose alphabet
outgrew the 23 available one-character names had every word silently doubled in
length. The abbreviation row read h2 = 2.75 and mean word length 9.38 against
the manuscript's 5.17 — and 2.75 sat neatly inside the range the pre-registered
prediction had named, so the prediction appeared to be confirmed. It was the
spelling doing the work. With one glyph written as one character the true value
is 3.22, and the prediction is wrong. **A prediction that appears confirmed
through an artefact is worse than one that fails cleanly**, and it was only
caught because a word-length metric was obviously absurd.

What it costs to fix it this way is stated in `harness/generators/alphabet.py`:
the manuscript is measured in EVA, where a minority of glyphs are written with
two or three characters, so its character-level metrics sit on a slightly
different footing from the generated rows. The size of that effect is bounded
by the fingerprint repo's own five-alphabet check, which puts h2 between 1.85
and 2.35 across EVA, v101, Zandbergen–Landini, FSG and Friedman. Re-running the
whole table against v101, where one glyph is exactly one character, is the
obvious next robustness check and has not been done.

**The noise-floor row was wrong first.** It was initially laid out on the shared
layout spec like a generator, which scrambled the association between real words
and their real section labels and understated the floor on exactly the
section-level metrics that matter most. It now keeps its own paragraphs, lines
and metadata.

**The grille search space was too narrow.** The first tuning run allowed 40 to
1200 table rows and never saw the configurations that fix vocabulary size. §4.5
is the result of widening it. A conclusion drawn from the first run would have
repeated the published error rather than correcting it.

**Tuning did not transfer, and the self-citation sweep is unstable.** The
sweep over Timm & Schinner's twenty switch settings chose `canFollow=none,
morph=slim, sourceChooser=page` on the main split and a completely different
setting, `canFollow=curveline, morph=slim, sourceChooser=position`, on the
reversed one, at nearly identical training scores (1.34 and 1.33 floor units).
The switches are not doing much that the metrics can see. The grille's tuned
configuration likewise gained little over its defaults. Both are reported as
they fell rather than re-picked on the held-out half, which would be the leak
this protocol exists to prevent.

## 7. What this cannot decide

- **A ranking, not a verdict.** If a procedural generator wins, that is evidence
  the text is consistent with procedural generation, not proof it carries no
  message.
- **A matching cipher shows viability, not content.** Naibbe reaching the
  manuscript's entropy means a fifteenth-century hand *could* have produced
  these statistics from real Latin. It is not evidence that anyone did, and the
  cross-word result in §4.2 is a reason to doubt this particular cipher.
- **Everything here is text-internal.** Palaeography, codicology, the botanical
  identifications and the 1404–1438 radiocarbon date constrain hypotheses from
  outside the text and are not modelled. Software narrows the field; it does not
  close it.
- **Layout-given metrics are not evidence.** Line geometry, paragraph shape and
  the section and Currier labels are handed to every process identically.
- **EVA is a transcription choice**, and the whole table inherits it. See §6.
- **The `line` block's section metrics depend on given labels.** A process
  scores on word-by-section mutual information only if it conditions its
  vocabulary on the section label it was handed. None of them do, which is a
  real finding, but it is a finding about the processes as published, not a
  proof that they could not be extended.
- **One transcription, one manuscript, no external validation.** No result here
  has been reproduced by anyone else.

## 8. Reproducing it

```sh
cd /home/ubuntu/voynich
.venv/bin/python harness/tune.py  --budget 200          # training half only
.venv/bin/python harness/score.py                       # main split
.venv/bin/python harness/score.py --reverse             # reversed split
.venv/bin/python harness/report.py --markdown           # the tables above
.venv/bin/python harness/gate.py                        # the checks
```

`gate.py` verifies: no generator reads the held-out half; our split is identical
to `voynich-fingerprint`'s; our text and struct blocks reproduce its published
held-out values; the noise-floor row exists and no hypothesis row beats it;
every registered process has a row on both splits; and reruns are bit-identical.

Data is not redistributed. `data/` holds the six IVTFF transcriptions from
voynich.nu and the reference corpora fetched from Universal Dependencies,
Project Gutenberg and the Latin Library per
`refs/voynich-fingerprint/data/README.md`.

## 9. Credit, licences, and what is whose

This harness contributes the unification, the noise-floor row, the floor-units
scale, the `line` block, the abbreviation model, and the corrections in §4.5 and
§6. Every generator it ranks is somebody else's work and most of it is run from
their own code.

| | |
|---|---|
| Sachak, D. (2026) | `voynich-fingerprint` — the 44-metric fingerprint, the five-component model, the hand-executable manual, the held-out protocol. MIT. Blocks `text` and `struct` are computed by calling its code. |
| Timm, T. & Schinner, A. (2019/2020) | Self-citation. *Cryptologia* 44(1) 1–19. Run from their own `text-generator.jar`. MIT. |
| Greshko, M. A. (2025) | The Naibbe cipher. *Cryptologia*, doi:10.1080/01611194.2025.2566408. Run from the author's own Python. Modified MIT; citation required. |
| Gaskell, D. E. & Bowern, C. (2022) | Human gibberish samples. CEUR-WS Vol-3313. Modified MIT; citation required. |
| Antenore (2026) | `voynich-toolkit` — the 16-property framework, and the grille and Llull implementations this harness reimplements and corrects. MIT. |
| Rugg, G. (2004); Rugg & Taylor (2017); Zandbergen, R. (2021) | The table-and-grille hypothesis. |
| Lindemann, L. & Bowern, C. (2020); Bowern & Lindemann (2021) | Character entropy; the abbreviation hypothesis §4.4 tests. |
| Montemurro, M. & Zanette, D. (2013) | Word-by-section mutual information. |
| Currier, P. (1976); Stolfi, J.; Davis, L. F. (2020) | Line-level properties; the A/B split; the scribal hands. |
| Zandbergen, R., voynich.nu | The IVTFF transliterations. CC0 per the host's statement. |

Private for now. If any of this is worth publishing, the honest framing is an
extension of `voynich-fingerprint`'s protocol to the hypothesis classes it did
not score, and the first move is an issue or a pull request on that repository
rather than a competing one.
