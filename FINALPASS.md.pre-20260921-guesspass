# THE FINAL PASS — check the vocabulary before checking the guesses

Written 2026-09-21, after the first clean run of the blindfold test.

## Why this order, and it is not a preference

The book is rendered from the vocabulary. Every bracketed guess was made by
a reader looking at a line, and that line was printed using the readings
already entered. If a reading in the line is wrong, the guess beside it was
made against a corrupted sentence. So the vocabulary is checked first, and
the guesses are checked afterwards, against the corrected text.

Measured 2026-09-21 over all 4,372 lines, by the worst other reading
standing in a guess's own line:

    guesses in the book (occurrences)                975
      read against clean context only                493   50.6%
      standing beside ANOTHER guess                  373   38.3%
      standing beside a tier C reading                63    6.5%
      standing beside a tier D reading                46    4.7%

Half the guesses were made in a line where everything else is K&T's own
dictionary or a tier A/B reading. Those are as good as a guess gets here.
The other half were made in a line that already contained something
uncertain, and 373 of them were made next to another guess. A guess read
off a guess is the failure mode this pass exists to catch.

## What the blindfold test says the guesses are worth

Run 2026-09-21 by a session that had not read the dictionary. Seed
1789991853. Strict score 7 of 25, 28.0%, which falls in the declared 15-30%
band. The consequence for that band was declared before any run and has
already been applied: passage-read tier C became tier D.

The run also split the failure cleanly, and this is the useful part:

    true word was in the candidate list the tool built    7 of 9 right
    true word was not in the list                         2 of 16 right

The reader is not the weak part of the judgment step. The list is.

## What is wrong with the list, measured

`ktrecall.py`, written 2026-09-21, masks every one of K&T's entries one at a
time and asks where the true word was. Leave-one-out over 616 entries that
stand on a cited folio:

    true gloss in the list the pipeline builds today      32.5%
    tether-cut control                                    11.1%   7.9 sigma
    mean list length                                      96 words

    why the other 67.5% miss, first reason that explains it:
      TAKEN    21.3%   in the cited verses, but filtered out because
                       another sign already carries that English stem
      NARROW    8.0%   within three verses of the cite, not in it
      CHAPTER   6.7%   elsewhere in a cited chapter
      BIBLE    26.6%   somewhere in the KJV or Douay, not in these chapters
      OUTSIDE   5.0%   in neither Bible: apocrypha, sermon, function word

TAKEN is a bug, not a limit. K&T have many signs for one English word, so
striking a word out because some other sign already means it withholds the
right answer one time in five. That filter has to become a warning rather
than a deletion.

BIBLE at 26.6% is the honest ceiling on any Bible-pool method: the word is
in scripture but not in the chapters this folio cites. NARROW and CHAPTER,
together 14.7%, are reachable by widening the cite.

The bar for any change to the list builder was declared in `ktrecall.py`
before the fix was attempted, and it stands: raise the 32.5% by at least ten
points, with a mean list no more than twice as long, beating the tether-cut
control by 5 sigma over 20 shuffles. Presence bought with a longer list is
not an improvement. The reader pays for every extra word.

## The passes, in order

**1. Vocabulary.** 947 readings, tiers A to D, plus K&T's 841 entries which
are not ours to change.

   a. Every reading at every occurrence. `ktcontext.py HEX`. This is the
      project's one gate that has always worked. A reading that fails a
      clear occurrence comes out; it is not demoted.
   b. Blast radius before anything else. `ktresidue.py --audit`. A wrong
      piece under three glyphs feeds dozens of compound words, and two of
      those (`540` as *shall*, `570` as *ark*) have already had to be
      withdrawn. Read the words a piece feeds, not its own occurrences.
   c. The 211 tier C and 82 tier D readings. These were read from one
      passage with nothing internal to test them. They are where the
      vocabulary is thinnest and where a correction moves the most text.
   d. Wrong sense of a right entry. `ktsensefit.py` found 1,628 words
      printing a sense K&T publish but the folio's passage does not use,
      and corrected 755 on 222 folios. The rest are still standing.
      This outnumbered the dark words five to one and it will again.

**2. Then the guesses.** 839 signs, 975 occurrences, rendered `[word]`.

   a. Start with the 373 that stand beside another guess. Wrong context.
   b. Then the 109 beside a tier C or D reading, after pass 1 has settled
      those.
   c. The 493 read against clean context are the last and the least
      likely to move.
   d. The mechanical sweep that needs no source text: a restoration that
      repeats a content word already standing within three places of it in
      the line is telling you the slot is taken. Run once already, 46 hits
      on 43 signs, 40 corrected. Rerun it after any vocabulary change,
      because the words standing in the line will have changed.

**3. Then rebuild**, and only then. `kttranslate.py`, `ktreader.py`,
`ktbook.py`, and the retelling gate.

## The rules that do not move for this pass

- A guess stays a guess and stays in the book. Every one of them is marked.
  Removing a guess to protect a percentage is not a correction; the
  brackets are the honesty, not the emptiness. The measured worth of a
  bracket is written in the reader's edition front matter and it stays
  accurate.
- Coverage falling is a valid result. It happened when *shall* and *ark*
  came out, 59.5% to 57.9%, and the book got truer.
- Do not widen a gate to make a pass succeed.
- Do not retype a figure. Every number above is either printed by a script
  named beside it or saved in `work/rohonc/`.

## Open, and not part of this pass

The blindfold result is not yet written into `ROHONC.md` or
`CONCLUSION.md`, and `check_rohonc.py` has no assertion for it. The old
invalid 48% run is still the one those documents describe.

One leak found in the test itself and not yet fixed: the blind sample
prints restored `°`-marked and `?`-marked words in the lines around a
masked sign, and on 006r that handed the answer *Paradise* to the reader
for free. `ktblind.py` should strip this project's own guesses from a
masked sign's context, or the test measures the project against itself.
Without that one hit the clean score is 6 of 24, 25%, which does not change
the band.

## THE KEY, VALIDATED — 2026-09-21

Backup first: `/home/ubuntu/backups/voynich.pre-finalpass-20260921-1258.tar.gz`,
116M, gzip verified, carrying the repository with its history, K&T's 455
dictionary files, the 229 scans and all of `work/`. `data/ref` and `refs/`
are excluded: both are gitignored third-party corpora and re-fetchable.
K&T's dictionary is NOT in git, so that tarball is the only copy of it
outside `data/rohonc/kt/`.

Then the validation. `ktkeycheck.py`, bars declared in its docstring before
the first run and not moved since. K&T cite folio and line for every example
in every entry, so the code an entry defines must stand at that folio, on
that line. Saved run: `work/rohonc/keycheck.txt`.

    headword citations                     2,045
      stands on the cited folio             89.2%
      control, folio shuffled                1.9%
      415 sigma, bar 5                       PASS
      on the EXACT cited line, of those      97.5%

**The key holds.** Nine times in ten K&T's own citation lands, and when it
lands it lands on the exact line they name 97.5% of the time. Against a
shuffled control of 1.9%. Our parse of their dictionary agrees with the
manuscript, and that is the foundation everything else stands on.

The other origins are reported separately and only HEAD is the key's own
claim: VAR 79.5%, UNCERTAIN (their own "?" and "??") 59.1%, EXPR 23.7%.
EXPR is low by construction, not by fault — an expression is a phrase the
book writes as several tokens.

### Three faults in the checker, all mine, all found before reporting

This script reported the dictionary as broken three times before it was
right, and each number went into the docstring as a correction rather than
being quietly replaced.

1. **One entry, several codes.** Only 144 of the first 400 entries carry a
   single code. After `expr.` or `var.` comes a different code and the
   folios following belong to it. Attributing them all to the headword
   reported 45.3% of citations missing.
2. **Cross-references are not examples.** `see`, `but see`, `cp.` and `cf.`
   point at another entry. Those folios are not claims that the code stands
   there.
3. **Whole-token matching, which cost the most.** The manuscript writes
   K&T's words with affixes attached and the renderer has always known it.
   Matching whole tokens reported 22.4% of headwords missing; matching
   whole-glyph constituents reports 10.8%.

Fault 3 nearly became a false discovery. The residue looked like a
systematic prefix nobody had handled — `630` *on/at/to* 74 times, `871`
*holy* 31 times, `521` the case markers 13 times, sitting on words K&T had
already read (wedding, James, Caiaphas, candlestick). `871` is the very
prefix DARK.md records as a six-year miss, which made it more believable,
not less. Measured against our own definition of "readable" it looked like
977 unread tokens on 884 lines.

Put to the actual renderer, it was nothing: of 1,372 tokens carrying those
three prefixes over a readable word, the renderer already reads 1,337.
Thirty-five are genuinely unread, on 34 lines. The rule that caught it is
METHOD.md's: if a tool disagrees with the page, fix the tool before reading
anything off it.

### What is left to read by hand

    220 headword citations on 117 codes still miss their folio.

That is the list the vocabulary pass starts from, and it is small enough to
read one by one. Each is our parse, a spelling the transcription writes
differently, or a slip of theirs — and the first two kinds are readings we
do not currently have.
