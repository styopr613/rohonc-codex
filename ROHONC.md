# The Rohonc Codex, on the same ruler

A second manuscript, run through the test that decided the Voynich question.
Written 2026-09-20. The Voynich work is in [`RESULTS.md`](RESULTS.md) and its
plain-English summary in [`CONCLUSION.md`](CONCLUSION.md).

## Why bother

Every claim in `RESULTS.md` rests on one measurement: the dependence between
one token and the next dies at the right margin in the Voynich, where a real
language keeps most of it. That measurement had never been run on anything but
the manuscript it was designed for and a handful of prose controls laid out in
Voynich-shaped paragraphs. A test that has only ever been pointed at one book
is not a test yet. It needs a second manuscript that ought to come out the
other way.

The Rohonc Codex is the right second manuscript. It is a real 448-page codex in
an unknown script, uncracked since 1839, with the same reputation for possibly
being meaningless. If our test can separate it from the Voynich, the test
works. If it cannot, `RESULTS.md` is weaker than it claims.

## What had to be got first

There is no public machine-readable transcription of the Rohonc. Király and
Tokai built one covering all 448 pages for their 2018 decipherment paper and
never released it; the journal lists no supplementary data. The scans at the
Hungarian Academy of Sciences are staff-only at full resolution and marked not
for redistribution at low resolution.

The one open transcription was at `quint.us/Roho/`. That domain now serves a
browser game. The file survives in the Internet Archive and is what this work
uses:

    data/rohonc/latest.txt     revision 2.5, 2014-09-18, 217 KB
    https://web.archive.org/web/20180421091607id_/http://quint.us/Roho/latest.txt

It is an incomplete, partly machine-generated transcription by an anonymous
author. 214 pages, 4,250 lines, 60,407 readable glyph tokens over 987 distinct
symbols, with 6.5% of tokens marked unreadable and dropped. Every figure below
inherits that provenance and should be read as provisional. Nothing here is a
claim about the Rohonc Codex that would survive the release of a scholarly
transcription unchanged.

## One glyph is one token

The Rohonc script has no word separators, so the harness's character-level
metrics — entropy, word length, spelling similarity — do not apply at all and
are not reported. What does apply is the line-break test, which needs only a
token stream and the line breaks.

Király and Tokai argue each Rohonc symbol codes a whole word rather than a
letter. On that reading one glyph plays the part one space-delimited word plays
in the Voynich, and the two manuscripts can be compared directly.

## The orientation problem, and how it was settled

The codex is written right to left. The recovered transcription does not
document whether it stores each line in reading order or in visual order, and
the entire measurement turns on it: mutual information is symmetric, so the
within-line figure is the same either way, but the across-break pair is
(end of this line, start of the next) and reversing the storage swaps them.

The two orientations give completely different answers — 16.9 sigma one way and
2.2 sigma the other — so this could not be left open.

External clues point both ways. The delimiter symbol that Király and Tokai
report separates sentences sits at the stored end of the line in 252 of its 269
appearances, which suits stored = reading order. The physical-damage marker
sits at the stored start more often than the stored end, 126 to 77, which suits
the opposite.

**A first attempt failed and was discarded.** `roho_orient.py` reasoned that an
incomplete bottom-of-page line has a genuine beginning and a spurious end, so
whichever stored end better fits the pool of normal line openings is the real
beginning. It returned a verdict — and its own control returned *negative* lift
on complete lines, where both ends are genuine and both should have scored
clearly positive. The pools carry no information, the measurement had no power,
and the verdict was noise on 32 lines. It is kept in the repository, with its
failure recorded, because a discarded test is part of the evidence.

**What settled it** was the property the Rohonc actually has in abundance, and
the one Ottó Gyürk used in 1970: long verbatim repeats. Inside a line, the two
orientations are mirror images and carry no information about direction. At a
line boundary they are not: reading order joins the tail of one line to the
head of the next, the reversed reading joins head to tail, and those are
different sequences. So ask which orientation makes a straddling sequence look
like ordinary text — one the codex also writes inside a line.

| 4-gram straddling a line break | found inside lines | chance | sigma |
|---|---|---|---|
| stored order as-is | 36.39% | 19.87% | **36.2** |
| reversed | 19.68% | 20.15% | −0.9 |

Reversed sits exactly on chance. The file stores reading order. Everything
below uses it as-is.

## The result

Percentage of token n-grams straddling a line break that the same manuscript
also writes strictly inside a line. Chance shuffles which line follows which
within a page, leaving every line intact and destroying only the pairing.

`lift` is the ratio to chance and is the **wrong** way to compare these texts:
the Rohonc's chance level is already 76.65% at n=2, so its ratio cannot exceed
1.30 however continuous the text is, while a text with a 6% chance level has
room for 17x. `headroom` is the share of the distance from chance to 100% that
the text actually covers, and is comparable across manuscripts with very
different repeat rates.

### One token from each side of the break

| | straddling | chance | sigma | lift | headroom |
|---|---|---|---|---|---|
| **Rohonc Codex** (glyphs) | 84.37% | 76.65% | 15.4 | 1.10x | **33.0%** |
| Italian prose (words) | 25.24% | 9.64% | 26.1 | 2.62x | 17.3% |
| Hebrew prose (words) | 21.43% | 6.75% | 23.8 | 3.18x | 15.7% |
| Latin prose (words) | 12.41% | 5.71% | 13.7 | 2.17x | 7.1% |
| five-component model | 12.01% | 8.37% | 7.8 | 1.43x | 4.0% |
| **Voynich EVA** (words) | 6.46% | 5.87% | 2.0 | 1.10x | **0.6%** |
| **Voynich v101** (words) | 6.38% | 5.84% | 1.7 | 1.09x | **0.6%** |
| self-citation (Timm) | 14.16% | 13.79% | 0.8 | 1.03x | 0.4% |
| line-reset scribe | 8.54% | 8.65% | −0.2 | 0.99x | −0.1% |

### Three tokens from each side

| | straddling | chance | sigma | lift |
|---|---|---|---|---|
| **Rohonc Codex** | 15.81% | 4.99% | **32.2** | 3.17x |
| Hebrew prose | 0.56% | 0.09% | 9.3 | 6.60x |
| Latin prose | 0.27% | 0.06% | 3.7 | 4.83x |
| Italian prose | 0.13% | 0.03% | 2.9 | 3.95x |
| **Voynich EVA** | 0.00% | 0.00% | — | — |
| **Voynich v101** | 0.00% | 0.00% | — | — |
| five-component model | 0.00% | 0.00% | — | — |
| self-citation, line-reset | 0.00% | 0.00% | — | — |

Not one six-glyph sequence that straddles a Voynich line break occurs inside a
Voynich line. In the Rohonc, one in six does.

## What this means

**The test works.** Pointed at a second manuscript in an unknown script, with a
different transcription, a different symbol inventory, a different reading
direction and a different unit of writing, it separates the two cleanly and in
the direction it should. The Rohonc sits above every natural-language control;
the Voynich sits at the bottom with the meaning-free generators. That is the
positive control `RESULTS.md` never had, and it strengthens every claim there.

**Why the Rohonc scores above prose.** Almost certainly because it is far more
repetitive than the prose controls — a devotional text full of formulae, per
Király and Tokai's reading of it as a Catholic gospel harmony. The headroom
normalisation controls for the repeat rate through the chance baseline, but not
perfectly. The honest claim is that the Rohonc is comfortably in the same
region as real language and the Voynich is nowhere near it, not that the Rohonc
is *more* linguistic than Italian.

**The mechanism is worth stating plainly.** The Rohonc repeats long passages,
and it repeats them at different positions relative to the line breaks. Text
that is split across a break in one place sits whole inside a line somewhere
else. That is a direct demonstration that the text exists independently of the
lines it is written on — which is exactly what one expects of a real text laid
out by a scribe, and exactly what the Voynich never once does.

## How much of the book is new

The cross-line result shows the Rohonc's text is independent of the page it is
written on. That rules out tracing and rules out line-by-line composition. It
does not rule out a person filling 448 pages by recycling earlier ones, and a
forger doing that would pass the test cleanly. So the next question is how much
of the book occurs only once.

Share of tokens inside a sequence of length k or more that occurs at least
twice anywhere in the book. The shuffle preserves the vocabulary exactly and
destroys only the order, which matters here because 987 symbols over 60,000
tokens make short repeats inevitable by chance. All texts truncated to 33,641
tokens so the lengths match.

| k = | 3 | 5 | 8 | 12 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|---|
| **Rohonc Codex** | 85.3 | 58.1 | 23.9 | 10.1 | 3.2 | 0.8 | 0.0 |
| *shuffled* | 59.7 | 1.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hebrew prose | 35.4 | 5.0 | 0.8 | 0.2 | 0.2 | 0.0 | 0.0 |
| Italian prose | 17.7 | 0.7 | 0.1 | 0.1 | 0.0 | 0.0 | 0.0 |
| Latin prose | 8.5 | 1.6 | 1.0 | 0.6 | 0.6 | 0.6 | 0.0 |
| Voynich (words) | 2.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

The shuffle explains the k=3 column and nothing beyond it: at k=5 the vocabulary
alone produces 1.4% and the codex produces 58.1%. From k=5 onward this is all
real structure.

### Nothing page-sized was duplicated

| longest sequence occurring twice | tokens |
|---|---|
| Rohonc, sentinels at every gap (lower bound) | 44 |
| Rohonc, gaps ignored entirely (upper bound) | 44 |
| Latin prose | 31 |
| Hebrew prose | 27 |
| Italian prose | 14 |
| Voynich (words) | 4 |

A Rohonc folio averages 282 tokens and a line averages 14, so the longest
verbatim repeat in the entire codex is about three lines. Coverage at k=60, 100
and 150 is exactly zero. Both bounds agree, so the dropped unreadable glyphs
are not what is truncating it.

**That rules out bulk copying.** A person padding 448 pages by recycling
earlier ones leaves repeats at the scale of the unit being recycled — a
paragraph, a page, a folio. Nothing in this codex repeats beyond three lines.

It also sits awkwardly with Király and Tokai's report of a verbatim parallel
running from 133v07 to 134r02 and again at 101r04–09, which is some seven
lines. Either their transcription differs from this one, or that parallel is
not strictly verbatim. Their reading of it does not depend on the difference,
but it is a discrepancy and worth recording.

### The repeats are local as well as long-range

Distance in tokens between consecutive occurrences of a repeated sequence.
"same folio" means within 282 tokens; "far apart" means more than ten folios.

| k=20 | repeats | median gap | same folio | far apart |
|---|---|---|---|---|
| **Rohonc Codex** | 173 | 269 | 60.1% | 24.3% |
| Latin prose | 108 | 5,430 | 0.0% | 88.9% |
| Hebrew prose | 14 | 6,848 | 0.0% | 100.0% |
| Italian prose | 0 | — | — | — |

The prose controls repeat long sequences only at long range — Augustine quoting
the same psalm a hundred pages later. The Rohonc does that too, with single
phrases recurring across 58,000 tokens, nearly the length of the book. But most
of its long repeats are *local*: a twenty-symbol sequence recurring a few lines
away on the same folio.

### What this settles and what it does not

**Settled:** the book was not padded by copying pages. The repeat length caps
out at three lines, everywhere, by both bounds.

**Consistent with, but not proved:** a formulaic devotional text. Heavy local
repetition of long phrases is what a litany, a responsory or a calendar looks
like, and Király and Tokai read the codex as a gospel harmony with a calendar
section. The long-range recurrence of the same phrases fits a genuine formula
rather than a local tic.

**The missing control, stated plainly.** The Rohonc is far more repetitive than
any text compared against it here at every k from 5 upward. But the comparisons
are Dante, Augustine and a Hebrew narrative — literary and narrative works,
none of them the genre the codex is claimed to be. Litanies, psalters and books
of hours are extremely repetitive by design. Without one of those in the
reference set, this document cannot say whether the Rohonc's repetition rate is
abnormal *for what it claims to be*. That is the obvious next control and it
has not been done.

## Where the two measures disagree

The token-to-token mutual-information version of the test (`linebreak.py`) is
less clean and should be read with more caution than the n-gram version:

| | within line | matched | across break | sigma | keeps |
|---|---|---|---|---|---|
| Rohonc Codex | 1.4222 | 1.0495 | 0.2391 | 16.9 | 22.8% |
| Italian prose | 0.3538 | 0.1137 | 0.0659 | 8.1 | 57.9% |
| self-citation (Timm) | 0.1755 | 0.0675 | 0.0252 | 3.9 | 37.4% |
| Latin prose | 0.1391 | 0.0344 | 0.0117 | 2.1 | 34.0% |
| five-component model | 0.0877 | 0.0167 | 0.0040 | 1.3 | 24.0% |
| Voynich EVA | 0.1754 | 0.0455 | 0.0087 | 1.9 | 19.2% |

`matched` is the within-line figure recomputed on a random subsample the same
size as the across-break set, so the two rest on equal evidence. Every figure
is surrogate-corrected.

On significance the two measures agree: the Rohonc's across-break dependence is
overwhelming at 16.9 sigma and the Voynich's is marginal at 1.9. But on the
proportion retained they do not. By this measure the Rohonc keeps 22.8% and the
Voynich 19.2% — nearly the same — and the five-component model keeps more than
the Voynich does.

Both measures are reported because they disagree. The n-gram version is
preferred here for a stated reason rather than a convenient one: adjacent-token
mutual information across a 987-type inventory at n=4,036 is severely
undersampled, and the fact that the within-line estimate falls from 1.42 to
1.05 simply by subsampling shows how sample-size-dependent the ratio is. The
n-gram test counts whole sequences and needs no entropy estimate.

## Reproducing

    cd harness
    python rohonc.py          # corpus statistics
    python roho_orient2.py    # the orientation decision
    python crossline.py       # the main result
    python linebreak.py       # the mutual-information version
    python roho_orient.py     # the failed first attempt, kept

Saved outputs are in `work/rohonc/`. The gate (`python gate.py`) covers the
Voynich harness and is unaffected by any of this; it still passes.

## What this does not decide

Nothing here says what the Rohonc means, and nothing here endorses Király and
Tokai's decipherment. The test says the text runs across the margin the way a
real text does. It does not say what text.

It also does not close the Voynich question. It removes one specific doubt —
that our line-break measurement might find "the line is the unit" in any
manuscript you point it at — and that doubt is now answered. The limits listed
in `CONCLUSION.md` are untouched.

## Credit

The transcription is the work of an anonymous author who published it openly
and whose site is gone; it is used here because it was released freely and is
credited as fully as it can be. Ottó Gyürk (1970) first analysed line breaks in
the codex's repeated sequences, which is the idea the orientation test and the
main result both rest on. Levente Zoltán Király and Gábor Tokai, *Cracking the
code of the Rohonc Codex*, Cryptologia 42:4 (2018), 285–315, is the source for
the reading direction, the symbol-as-word interpretation and the delimiter.
Benedek Láng, *The Rohonc Code: Tracing a Historical Riddle* (Penn State Press,
2021), is the standing survey.
