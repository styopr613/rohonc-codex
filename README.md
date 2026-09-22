# The Rohonc Codex, read

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22902166.svg)](https://doi.org/10.5281/zenodo.22902166)

The Rohonc Codex is a paper book of the sixteenth century, 224 leaves, held at
the Library of the Hungarian Academy of Sciences in Budapest, written in a
script that occurs in no other document. In 2018 Levente Zoltán Király and
Gábor Tokai published the dictionary and grammar that opened it. This
repository is an attempt to read the rest of it, and everything needed to
check that attempt.

**It has not been peer reviewed. It is published so that it can be attacked.**

* **[`TESTS.md`](TESTS.md)** — every test, its bar declared before the run, and
  the ones that failed. Start here if you want to know whether to believe any
  of it.
* **[`CONCLUSION.md`](CONCLUSION.md)** — the plain-English account, including
  what is still guessed at.
* **[`ROHONC.md`](ROHONC.md)** — the long technical record.
* **[`METHOD.md`](METHOD.md)** — the rules the work was done under, written
  before the results.
* **[`book/`](book)** — the edition itself as an EPUB, free.

## What it claims, and what it does not

Every word of the reading carries its evidence. A plain word is read. A word
marked `*` is read from one passage with nothing in the book able to refuse it.
A word in `[brackets]` is a restoration, a guess, and is counted as a reading
nowhere. `[...]` is a word nobody can read.

Of the manuscript's 29,997 words this edition has a reading for 94.1%. Of its
4,372 lines, 81.5% have every word read; 98.9% are complete once the bracketed
guesses are counted. The gap between those two numbers is how much is being
guessed at, and it is meant to be visible.

The one check that is not internal: everything here reads Király and Tokai's
transcription, so no test of this project's could catch an error in it. An
anonymous transcription published in 2014 — a different person, a different
glyph alphabet, no word division, four years earlier — agrees with it on 91.1%
of the glyphs that can be compared, against 12.9% for the same rows paired at
random.

**Király and Tokai's dictionary is their published work and is not in this
repository.** Neither are the manuscript scans. `DATA_PROVENANCE.md` says where
everything came from and what may be done with it.

## Licence

Three parts, three licences, set out in full in [`LICENSE`](LICENSE).

| what | licence | what you may do |
|---|---|---|
| the programs, `harness/` | MIT | anything, including sell what you build |
| the data and saved runs | CC BY 4.0 | build on it, with credit |
| the translation and the prose | CC BY-NC-ND 4.0 | read, quote, teach, check, republish whole non-commercially, with credit |

**The commercial rights to the English text are reserved.** A paperback of it is
sold, and the text is the thing being sold. Everything you need in order to
*check* the work — the data and the programs — is under the permissive licences,
which is the point: the restriction is on reselling the translation, not on
attacking it.

Király and Tokai's dictionary, grammar and transcription are their published
work, are not redistributed here, and no licence over them is claimed or
implied. The manuscript images belong to the Library of the Hungarian Academy of
Sciences; the manuscript itself is out of copyright. `DATA_PROVENANCE.md` states
the position on every file.

## Citing this

Cite the concept DOI, which always resolves to the latest version:

> Taylor, Stephen. *The Rohonc Codex, read: an attempt, and everything needed to
> check it.* https://doi.org/10.5281/zenodo.22902166

The archived snapshot of this release is 10.5281/zenodo.22902167. The work it
builds on is Király, L. Z. and Tokai, G. (2018), "Cracking the code of the
Rohonc Codex", *Cryptologia* 42(4):285-315, doi:10.1080/01611194.2018.1449147.

## The Voynich harness

This began as something else: a hypothesis-ranking harness for the Voynich
manuscript, which is still here and still stands on its own. One metric vector,
one held-out protocol, fourteen candidate processes and five controls, and a
row that says how much of the difference is sampling noise.
**[`RESULTS.md`](RESULTS.md)** is that deliverable. The Rohonc work started as
its positive control: a book whose script was genuinely solved, to check that
the instruments could tell a solved book from an unsolved one.

## What is here

| path | what it is |
|---|---|
| `CONCLUSION.md` | the plain-English conclusion, one page, no numbers |
| `ROHONC.md` | the same line-break test run on the Rohonc Codex, as a positive control |
| `DATA_PROVENANCE.md` | where the Rohonc data came from and what may be done with it |
| `RESULTS.md` | the write-up. Tables generated from the data, prose figures checked against it |
| `VOYNICH_PLAN.md` | the plan, including the prior-work survey that decided the scope |
| `PREDICTION_abbrev.md` | prediction for the abbreviation model, written before the code. Not edited afterwards |
| `harness/` | the code |
| `harness/ktsite.py` | builds the public page, oona13.com/rohonc/, from the files above: the introduction, the reading, the dictionary, the tests as a verdict table, the method, and the standing orders published whole. The data and the programs are not served from it — they go to GitHub — except `dictionary.json`, which the dictionary page's search loads. Nothing of Király and Tokai's is copied there |
| `data/` | six IVTFF transcriptions from voynich.nu, plus reference corpora. Not redistributed |
| `refs/` | ten cloned prior-work repositories, read-only |
| `work/` | results JSON, tuned configurations, logs |

## The code

| module | what it does |
|---|---|
| `corpus.py` | loads the transcription into paragraphs with section / Currier / hand metadata. Reproduces voynich-fingerprint's split exactly |
| `profile.py` | the ruler: 15 text + 27 structural metrics from the fingerprint repo's own code, plus 8 new line- and section-level ones |
| `floor.py` | the second scale: every metric in units of how far two halves of the same book sit apart |
| `layout.py` | the layout spec every process is handed, sampled from the training half only |
| `generators/` | one file per process, all behind `generate(spec, train, seed) -> (doc, notes)` |
| `tune.py` | equal search budget for every parameterised process, scored on the training half |
| `score.py` | runs everything, writes `work/results_<split>.json` |
| `report.py` | renders the tables |
| `build_results.py` | fills the table placeholders in `RESULTS.md` from the data |
| `rohonc.py`, `rohonc_kt.py` | the two Rohonc transcriptions as token streams (2014 glyph-level; Király–Tokai word-level) |
| `roho_orient.py`, `roho_orient2.py` | storage orientation of the 2014 file — the first failed its own control and is kept |
| `crossline.py`, `linebreak.py`, `repeats.py` | the line-break test in three forms, and how much of a book is new |
| `ktdict.py`, `ktvalidate.py`, `ktlocalise.py` | Király–Tokai's dictionary: coverage, gospel-specificity, page localisation |
| `ktextend.py`, `ktalign.py` | three attempts to extend the dictionary; all fail their held-out gates |
| `roho_ocr.py`, `ocr_tokens.py`, `ocr_crossline.py` | a third transcription from the scans; fails for resolution |
| `check_rohonc.py` | every figure in `ROHONC.md` against the saved runs in `work/rohonc/` |
| `check_results.py` | verifies every figure quoted in the prose against the data |
| `gate.py` | the checks that must pass after any change |

## Running it

```sh
.venv/bin/python harness/tune.py --budget 200      # training half only
.venv/bin/python harness/score.py                  # main split
.venv/bin/python harness/score.py --reverse        # reversed split
.venv/bin/python harness/build_results.py          # refresh the tables
.venv/bin/python harness/check_results.py          # verify the prose
.venv/bin/python harness/gate.py                   # all gates
```

Run `gate.py` after every change. It is not a correctness proof; it only rules
out the specific mistakes that would silently invalidate the table — a generator
reading the held-out half, a split that drifted from the reference
implementation, a missing noise-floor row, a non-deterministic rerun.

## The one-line summary

The manuscript's word-to-word structure stops dead at the right-hand margin,
where a real language's does not. Whatever made this text worked one line at a
time. On the letter statistics everyone argues about, a meaning-free generator
and a verbose cipher over real Latin both already match it.

## Credit

Every generator ranked here is somebody else's work, most of it run from their
own code: Sachak's `voynich-fingerprint`, Timm & Schinner's self-citation jar,
Greshko's Naibbe cipher, Gaskell & Bowern's gibberish samples, and the grille
and Llull implementations in Antenore's `voynich-toolkit`. Full attribution and
licences are in `RESULTS.md` §9. Transliterations are Zandbergen's, CC0.
