# Voynich hypothesis-ranking harness — plan

Written 2026-09-19 by Fable after a prior-work search. For Opus to execute.
Folder: `/home/ubuntu/voynich/`. Nothing here touches any live site.

## 0. The one-paragraph answer to "hasn't someone done this?"

Mostly yes, in pieces, and one piece is very close. `SachekDenis/voynich-fingerprint`
(updated 2026-09-18) measures a 44-metric fingerprint on a held-out leaf split and
scores its own five-component generator, Timm & Schinner's self-citation generator,
a substitution-cipher control and 13 natural languages on that one scale. What it
does NOT score: a verbose cipher (Greshko's Naibbe, which has public code), a
table-and-grille (Rugg/Zandbergen), a scribal-abbreviation model (nobody has built
one), Llull-style combinatorics, or the real human gibberish samples from Gaskell &
Bowern. Its own LIMITATIONS.md asserts, without measuring, that a verbose cipher or
grille "would be statistically indistinguishable" from its generator. That assertion
is the gap. `antenore/voynich-toolkit` has Rugg, Naibbe and Llull generators but scores
them on a different, 16-property, non-held-out scale with no language control and no
self-citation baseline. So the two camps still argue past each other on different
rulers. The job is to put every process on the fingerprint's ruler, with the same
held-out protocol, and publish the table.

## 1. Prior work, what each one covers (verified 2026-09-19)

| work | metrics | generators / corpora scored | held-out | code | where on Rachel |
|---|---|---|---|---|---|
| SachekDenis/voynich-fingerprint (2026-09) | 44 (15 text + 29 structure) | own 5-component model, hand-executable manual, Timm & Schinner (best of 20 configs), substitution attack, 13 languages | yes, odd/even leaves + reversed | Python, MIT | `refs/voynich-fingerprint` |
| antenore/voynich-toolkit (2026-04) | 16 "confirmed properties" (z-tests) | Rugg grille (10/16), Naibbe (code, no result committed), Llull machine | no | Python, MIT | `refs/voynich-toolkit` |
| Timm & Schinner 2019/2020 (Cryptologia) | ~10 in paper | self-citation | no | Java jar | `refs/SelfCitationTextgenerator` |
| Greshko 2025, Naibbe cipher (Cryptologia) | ~8 in paper | verbose homophonic cipher over Latin/Italian; "Voynichesque" alphabet mapper | no | Python, modified MIT (cite) | `refs/naibbe-cipher` |
| Gaskell & Bowern 2022 | ~12 + ML classifier | 42 human gibberish samples vs VMS vs meaningful corpus | no | Python + R | `refs/voynich` |
| Lindemann & Bowern 2020 (+ hermesj extension) | h1/h2 entropy, bigram concentration | 316 comparison texts, some cipher variants | no | R | `refs/R_Voynich_Stats` |
| Parisel 2026, arXiv 2604.19762 | 4 "signatures" | slot-based generator, Cardan grille; 4 languages | no | none released | — |
| adequatelimited/voynich (voynich.win, 2026-09) | 5 baseline families | none (governance/grading scaffold, Python 3.14) | n/a | Apache | `refs/voynich-2` |
| vigibygg-cmyk/voynich-research | ~100 ad-hoc | none | no | Python | `refs/voynich-research` |
| Workwrite-Niidome (2026-04) | ad-hoc | claims a partial translation; not a harness | no | Python | `refs/voynich-manuscript-analysis` |
| Rugg 2004; Rugg & Taylor 2017; Zandbergen 2021 grille paper | — | hand method | — | none | (paper only) |

Nobody has: (a) a scribal-abbreviation generator, (b) Naibbe or a grille scored on a
44-metric held-out fingerprint, (c) a noise-floor row (the manuscript's own other half
scored as if it were a generator), (d) all of the above in one table.

## 2. Data — already on disk, no network needed

`/home/ubuntu/voynich/data/` holds the six voynich.nu IVTFF 2.0 files the fingerprint
repo expects (`IT2a-n.txt` Takahashi EVA is the primary; `GC2a-n`, `ZL3b-n`, `VT0e-n`,
`RF1b-e`, `FG2a-n`, `000_README.txt`). voynich.nu IS reachable from Rachel (checked).
Still to fetch, all from GitHub raw: the 11 Universal Dependencies treebanks listed in
`refs/voynich-fingerprint/data/README.md`, plus Dante (Gutenberg 1012) and Augustine's
Confessions (Latin Library). Gaskell's human gibberish and meaningful corpora are in
`refs/voynich/data/*.zip` (use Python `zipfile`, `unzip` is not installed).

## 3. Design

One ruler, one protocol, every process. Build it as a thin layer on top of the
fingerprint repo rather than rewriting its metrics: its `voynich_lib.py`,
`tier2_metrics.py` and `refstats.py` already compute the 44 numbers, and reusing
them means our table is directly comparable to the numbers that repo publishes.

```
/home/ubuntu/voynich/
  data/            IVTFF files (done) + ref/ corpora
  refs/            cloned prior work, read-only
  harness/
    profile.py     computes the metric vector for any "document" (list of pages ->
                   lines -> words) by calling fingerprint's functions; adds the
                   line-level properties fingerprint lacks (see 3.2)
    split.py       train = even leaves, test = odd leaves; reversed split too
    layout.py      the layout spec every generator receives (lines per page,
                   words per line, paragraph-final short lines) taken from the
                   TRAIN half only
    generators/    one file per process, one interface:
                   generate(seed, layout, budget) -> document
    tune.py        bounded tuning of each generator on TRAIN
    score.py       score every generator on TEST and reversed TEST
    report.py      the table + per-metric failure list -> RESULTS.md
  RESULTS.md       the deliverable
```

### 3.1 The generator roster

| id | process | source | work needed |
|---|---|---|---|
| `noise_floor` | the manuscript's own train half, scored as if generated | data | trivial; this is the row every other row is judged against |
| `selfcite` | Timm & Schinner self-citation | `refs/SelfCitationTextgenerator/executable/text-generator.jar` (Java 17 present) | wrap; fingerprint's `compare_generators.py` already does this, it expects the jar at `tools/scitext/executable/`, so symlink |
| `fivecomp` | fingerprint's five-component model | `refs/voynich-fingerprint/analysis/voynich_artgen.py` + `frozen/FROZEN_CONFIG.json` | wrap |
| `manual` | fingerprint's hand-executable manual | `analysis/scribe_method.py` | wrap |
| `grille` | Rugg table-and-grille (corpus-built table, Stolfi prefix/core/suffix) | `refs/voynich-toolkit/src/voynich_toolkit/rugg_test.py` | port the table builder + grille walker; give it our layout |
| `llull` | Llull combinatoric disks | `refs/voynich-toolkit/.../lull_machine_test.py` | port |
| `naibbe` | verbose homophonic cipher over Latin and Italian | `refs/naibbe-cipher/naibbe_v2.py` (+ `voynichesque.py`) | wrap; plaintext = Augustine + Dante from data/ref |
| `subst` | simple substitution over Latin into an invented 22-glyph alphabet | write (~40 lines) | control; should lose badly on h2 |
| `abbrev` | Latin scribal-abbreviation model: apply Cappelli-style contraction + suspension + common-sign rules to Latin, then map to an invented alphabet with positional variants | write (new, ~300 lines) | the one process nobody has modelled; see 3.3 |
| `natlang` | plain Latin / Italian / Hebrew in an invented alphabet, laid out on VMS layout | write (~40 lines) | control |
| `gibberish` | Gaskell & Bowern's 42 human gibberish samples, EVA-mapped | `refs/voynich/data/gibberish_transcriptions.zip` | real samples, no tuning; short, so flag which metrics are undefined at that length |

Each generator produces a document at the same token count as the TEST half, on the
TRAIN-derived layout, from a fixed seed. Any generator with free parameters gets the
same tuning budget (say 200 evaluations of the 15 text metrics on TRAIN, random
search, seeded). Tuning never sees TEST. Timm & Schinner get their best-of-20 switch
sweep as the fingerprint repo already does.

### 3.2 The profile

Start from the fingerprint's 44 metrics unchanged, so the numbers cross-check against
its `frozen/FROZEN_RESULTS.json`. Add, as a second block, the line-level properties the
toolkit found that the fingerprint does not measure: line self-containment (no word
repeat across a line boundary), `m` as line-final marker, simple-gallows-at-paragraph-start,
paragraph vocabulary coherence, word-by-section mutual information (Montemurro), Currier
A/B vocabulary split. That gives every item in the user's original list: entropy,
word-length distribution, glyph position effects, adjacent repetition, vocabulary
self-similarity, Currier A/B, section drift.

Score = mean absolute percentage error per metric, reported per block (text /
structure / line-level) and overall, exactly as the fingerprint repo reports, plus the
per-metric worst offenders for each generator.

### 3.3 The abbreviation generator (new work)

Model, not a decipherment: take Latin plaintext, apply (1) suspension of common
endings (-us, -um, -orum, -ibus, -tur...), (2) contraction of nomina sacra and
frequent words, (3) the common signs (per/pro/prae, con-, -rum, macron for nasals),
(4) then a one-to-one map of the resulting letters+signs onto an invented alphabet,
with positional allographs (word-initial vs word-final forms) because that is a real
scribal habit and it is the mechanism most likely to depress conditional entropy.
Parameters: abbreviation rate per rule, number of positional variants. Predict
before running: it should improve h2 and word-length shape over `natlang` but keep
Brevity law near a language's value; whether that prediction holds is the finding.

### 3.4 Fairness and leak rules

- Layout (line lengths, paragraph shapes) comes from TRAIN only, and is given to every
  generator identically. State this in RESULTS.md so nobody mistakes layout metrics
  for evidence.
- Every generator seeded; `score.py --verify` reruns and diffs, must be 0.00% drift.
- Reversed split (train on odd, test on even) always reported next to the main one.
- The `noise_floor` row defines "as good as it gets". Any generator within the noise
  floor on a metric is "matched", not "better".
- No generator may read `IT2a-n.txt` TEST leaves. Grep for it in a gate script.

## 4. Steps for Opus, with gates

1. **Environment.** `python3 -m venv /home/ubuntu/voynich/.venv`; install numpy,
   scipy, pandas, Pillow, click. Fetch the 13 reference corpora per
   `refs/voynich-fingerprint/data/README.md` into `data/ref/`. Symlink
   `refs/voynich-fingerprint/tools/scitext -> ../../SelfCitationTextgenerator`.
   Gate: `python analysis/freeze_and_verify.py --verify` inside the fingerprint repo
   (with `data/` pointed at ours) reports 0.00% drift. If it does not, stop and report;
   our whole table depends on reproducing their numbers first.
2. **Profile + noise floor.** `harness/profile.py`, `split.py`, `layout.py`. Gate:
   profile of the full manuscript equals the fingerprint's published vector to 4 places;
   `noise_floor` row produced.
3. **Wrap the four existing generators** (`selfcite`, `fivecomp`, `manual`, `naibbe`)
   and the two controls (`subst`, `natlang`). Gate: table with 7 rows renders; `subst`
   and `natlang` sit far from the manuscript on h2 (sanity).
4. **Port `grille` and `llull`** from the toolkit onto our layout. Gate: `grille`
   reproduces the toolkit's own headline (Zipf and slot grammar pass, vocabulary size
   and line-level fail) before tuning.
5. **Build `abbrev`.** Write the prediction in RESULTS.md before the first run.
6. **`gibberish` row** from Gaskell's samples, with the undefined-metric flags.
7. **Tuning pass** with the fixed budget, then final `score.py` on TEST and reversed.
8. **RESULTS.md**: the table; for each generator the five worst metrics with the
   actual vs generated value; one plain paragraph per generator saying where it fails
   and what that failure means; the caveat section (below) verbatim.
9. **Gates file** `harness/gate.py`: determinism, leak grep, both splits present,
   noise-floor row present, every generator row present. Run after every change.

Effort: about six to eight Opus sessions. Cost: none beyond compute; no model calls.

## 5. Caveats that go in RESULTS.md unchanged

- A ranking, not a verdict. If a procedural generator wins, that is evidence the text
  is consistent with procedural generation, not proof it carries no message.
- The fingerprint repo's own limitation still applies: a verbose cipher or nomenclator
  produces statistics of the *encoding*, so a cipher that matches the fingerprint has
  shown viability, not content.
- Everything here is text-internal. Paleography, codicology, botany and the
  radiocarbon date constrain hypotheses from outside and are not modelled.
- EVA is a transliteration choice; the fingerprint repo checks h2 across five alphabets,
  and we inherit that check only for the metrics it covers.
- Human gibberish samples are short; metrics that need thousands of tokens are marked
  undefined for that row, not zero.

## 6. Licences and credit

fingerprint: MIT. toolkit: MIT. Timm: MIT. Naibbe: modified MIT, must cite Greshko 2025.
Gaskell & Bowern: modified MIT, must cite. Voynich.nu transliterations: CC0 per the
host's statement (adequatelimited/voynich checked this). Cite all of them in RESULTS.md.
**Decision 2026-09-19: private for now.** Pulling from GitHub (the cloned refs, UD
corpora, anything else needed) is fine. No remote, no PR, no fork of our own code yet.
A local `git init` inside `/home/ubuntu/voynich/harness` is fine for history. Keep the
citation list in RESULTS.md current so publishing is a copy, not a rewrite. If the table
turns up something interesting, we publish our code; the honest framing then is "an
extension of voynich-fingerprint's protocol to the hypothesis classes it did not score".
