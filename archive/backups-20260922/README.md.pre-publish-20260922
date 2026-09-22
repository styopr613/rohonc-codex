# Voynich hypothesis-ranking harness

One metric vector, one held-out protocol, fourteen candidate processes and five
controls for the Voynich manuscript's text, and a row that says how much of the
difference is sampling noise.

**Start with [`RESULTS.md`](RESULTS.md).** It is the deliverable: the ranking,
what each process fails on, the corrections made along the way, and what none of
it can decide.

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

Private working repository. Publish only if the table turns out to be worth it.
