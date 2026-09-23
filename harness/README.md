# The programs

Python 3.10.12 with numpy 2.2.6 and the standard library. Everything runs from
the **repository root**, as `python3 harness/<program>.py`. Every test program
names its test number and states its bar in its first lines, before any result
exists.

## The Rohonc reading

To reproduce the published results:

```sh
python3 harness/reproduce_tests.py
```

It verifies the exact hashes of the source inputs, runs every published saved
result twice under different Python hash seeds, and requires byte-for-byte
agreement with the archived run in `work/rohonc/`. The blind and outside-reader
tests score their committed replies without making any network request. Test 4
is explicitly blocked and has no result to reproduce. The three inputs it needs
are not in this repository; [`../DATA_PROVENANCE.md`](../DATA_PROVENANCE.md)
says where each came from.

**Which program made which number** is not kept in a list here, because a
hand-kept list drifts. [`../TESTS.md`](../TESTS.md) names the program and the
saved run for every test, and the public site's table of programs is generated
from that document at build time.

## The gates

`gates.txt` is the one list of checks, read by both `ktcommit.sh` and
`ktpush.sh`. Two scripts with two hand-kept lists was the drift this project
kept paying for. Add a gate to that file and both run it.

```sh
python3 harness/gate.py             # the Voynich harness gates
python3 harness/check_results.py    # every figure in RESULTS.md prose
python3 harness/check_rohonc.py     # every figure in ROHONC.md prose
python3 harness/check_tests.py      # every figure TESTS.md prints for a test
python3 harness/ktretellcheck.py    # every word Book One quotes, against the gloss
python3 harness/ktnotecheck.py      # the endnotes
python3 harness/ktatlascheck.py     # the atlas plates and their sources
```

Green is not correctness. Each gate rules out one specific way a number could
be silently wrong; none of them can tell you a reading is right.

## The Voynich harness

```sh
.venv/bin/python harness/tune.py --budget 200      # training half only
.venv/bin/python harness/score.py                  # main split
.venv/bin/python harness/score.py --reverse        # reversed split
.venv/bin/python harness/build_results.py          # refresh the tables
.venv/bin/python harness/check_results.py          # verify the prose
.venv/bin/python harness/gate.py                   # all gates
```

`gate.py` is not a correctness proof. It only rules out the specific mistakes
that would silently invalidate the table — a generator reading the held-out
half, a split that drifted from the reference implementation, a missing
noise-floor row, a non-deterministic rerun.

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
| `check_results.py` | verifies every figure quoted in the prose against the data |
| `gate.py` | the checks that must pass after any change |

## The Rohonc modules

The reading and its tests are the bulk of this directory. The ones that carry
the argument:

| module | what it does |
|---|---|
| `rohonc.py`, `rohonc_kt.py` | the two Rohonc transcriptions as token streams (2014 glyph-level; Király–Tokai word-level) |
| `roho_orient.py`, `roho_orient2.py` | storage orientation of the 2014 file — the first failed its own control and is kept |
| `crossline.py`, `linebreak.py`, `repeats.py` | the line-break test in three forms, and how much of a book is new |
| `ktdict.py`, `ktvalidate.py`, `ktlocalise.py` | Király–Tokai's dictionary: coverage, gospel-specificity, page localisation |
| `ktextend.py`, `ktalign.py` | three attempts to extend the dictionary; all fail their held-out gates |
| `roho_ocr.py`, `ocr_tokens.py`, `ocr_crossline.py` | a third transcription from the scans; fails for resolution |
| `kttranslate.py` | renders a folio from the dictionary, marking every word by how far it reads |
| `ktsite.py` | builds the public page, oona13.com/rohonc/, from the documents at the repository root. The data and the programs are not served from it — they go to GitHub — except `dictionary.json`, which the dictionary page's search loads. Nothing of Király and Tokai's is copied there |
| `ktbook.py` | the printed and EPUB edition |
| `ktcommit.sh`, `ktpush.sh` | the only sanctioned way to commit: they run `gates.txt` first |
