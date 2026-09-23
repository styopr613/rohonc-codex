# The Rohonc Codex, read

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22902166.svg)](https://doi.org/10.5281/zenodo.22902166)

The Rohonc Codex is a paper book of the sixteenth century, 224 leaves, held at
the Library of the Hungarian Academy of Sciences in Budapest, written in a
script that occurs in no other document. In 2018 Levente Zoltán Király and
Gábor Tokai published the dictionary and grammar that opened it. This
repository is an attempt to read the rest of it, and everything needed to
check that attempt.

**It has not been peer reviewed. It is published so that it can be examined.**

## Start here

* **[`TESTS.md`](TESTS.md)** — every test, its bar declared before the run, and
  the ones that failed. Start here if you want to know whether to believe any
  of it.
* **[`CONCLUSION.md`](CONCLUSION.md)** — the plain-English account, including
  what is still guessed at.
* **[`ROHONC.md`](ROHONC.md)** — the long technical record.
* **[`METHOD.md`](METHOD.md)** — the rules the work was done under, written
  before the results.
* **[`DATA_PROVENANCE.md`](DATA_PROVENANCE.md)** — every source, the terms it
  carries, and what may be done with it.

## What it claims, and what it does not

Every word of the reading carries its evidence. A plain word is read. A word
marked `*` is read from one passage with nothing in the book able to refuse it.
A word in `[brackets]` is a restoration, a guess, and is counted as a reading
nowhere. `[...]` is a word nobody can read.

Of the manuscript's 29,997 words this edition has a reading for 94.1%. Of its
4,372 lines, 81.5% have every word read; 98.9% are complete once the bracketed
guesses are counted. The gap between those two numbers is how much is being
guessed at, and it is meant to be visible.

We found one external test to validate the signal. Everything here reads Király and Tokai's
transcription, so no test of this project's could catch an error in it. An
anonymous transcription published in 2014 — a different person, a different
glyph alphabet, no word division, four years earlier — agrees with it on 91.1%
of the glyphs that can be compared, against 12.9% for the same rows paired at
random.

**Király and Tokai's dictionary is their published work and is not in this
repository.** Neither are the manuscript scans. `DATA_PROVENANCE.md` says where
everything came from and what may be done with it.

## Reproducing the tests

After placing the source inputs named in [`DATA_PROVENANCE.md`](DATA_PROVENANCE.md),
run this from the repository root:

```sh
python3 harness/reproduce_tests.py
```

The checker verifies the exact source-file hashes, runs every published saved
result under two Python hash seeds, and requires byte-for-byte agreement with
the archived output. Tests 3, 12b, 14, and 15 score their committed blind or
outside-reader replies without contacting a model API. Test 4 is explicitly
blocked and has no result to reproduce.

## What is in this repository

| path | what it is |
|---|---|
| the five documents above | the account, the record, the tests, the rules and the provenance |
| [`book/`](book) | the edition itself as an EPUB, free, with its cover |
| [`harness/`](harness) | the programs: the reading, the tests, the checkers, and the builder for the public site. [`harness/README.md`](harness/README.md) describes them |
| `work/rohonc/` | the saved run behind every published figure, one file per test, each stating its bar at the top |
| [`notes/`](notes) | the working documents the stages were done from, published as they were written |
| [`archive/`](archive) | files no longer part of the edition, kept because the record of how a reading changed is itself evidence |
| [`RESULTS.md`](RESULTS.md) | the Voynich harness this project began as. See the last section |

Three things are named in the documents and are deliberately not here. `data/`
holds the sources — Király and Tokai's dictionary and transcription, the
manuscript scans, the reference corpora — which are other people's and are not
redistributed. `refs/` holds ten cloned prior-work repositories, read-only.
`DATA_PROVENANCE.md` gives the address and the terms for every one of them.

And the public site's artwork is not here: the five atlas plates, the book
rendered in 3D, the textures behind the page. They are pictures of a website,
not evidence for a reading, and this repository is the second kind of thing.
The atlas plates redraw from `harness/atlas.json` through `harness/ktatlas.py`,
both tracked, along with `harness/ktatlascheck.py`, which refuses any fact on a
plate that does not name its source.

## Reading it

The whole edition is free to read at https://oona13.com/rohonc/ and as an EPUB
in [`book/`](book). A paperback and a Kindle edition
(https://www.amazon.com/dp/B0HKQCWV2S) are sold. What that does and does not
restrict is the next section.

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
examining it.

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

## Credit

The dictionary, the grammar and the transcription this edition stands on are
**Levente Zoltán Király's and Gábor Tokai's**, and the reading would not exist
without them. What is theirs and what was added here is separated in writing in
[`ROHONC.md`](ROHONC.md), under "what is new here and what is not". The
manuscript scans are the Library of the Hungarian Academy of Sciences'. Every
other source, down to the individual public-domain text a folio was read
against, is named in [`DATA_PROVENANCE.md`](DATA_PROVENANCE.md), along with one
courtesy failure of ours recorded so it is not repeated.

## Where this came from: the Voynich harness

This project began as something else, and that work is still here and still
stands on its own: a hypothesis-ranking harness for the Voynich manuscript. One
metric vector, one held-out protocol, fourteen candidate processes and five
controls, and a row that says how much of the difference is sampling noise.
**[`RESULTS.md`](RESULTS.md)** is that deliverable; the plan and the prior-work
survey behind it are in [`notes/VOYNICH_PLAN.md`](notes/VOYNICH_PLAN.md).

Its finding, in one line: the manuscript's word-to-word structure stops dead at
the right-hand margin, where a real language's does not, so whatever made this
text worked one line at a time — and on the letter statistics everyone argues
about, a meaning-free generator and a verbose cipher over real Latin both
already match it. Five of the project's own conclusions were overturned by its
own follow-up tests; all five are recorded in `RESULTS.md` §6 and none was
quietly amended.

The Rohonc work started as this harness's positive control: a book whose script
was genuinely solved, to check that the instruments could tell a solved book
from an unsolved one. It then became the larger piece of work, which is why it
is what this repository is named for.

Every Voynich process ranked here is somebody else's work, most of it run from
their own code: Sachak's `voynich-fingerprint`, Timm & Schinner's self-citation
jar, Greshko's Naibbe cipher, Gaskell & Bowern's gibberish samples, and the
grille and Llull implementations in Antenore's `voynich-toolkit`. Full
attribution and licences are in `RESULTS.md` §9. Transliterations are
Zandbergen's, CC0. How to run the harness is in
[`harness/README.md`](harness/README.md).
