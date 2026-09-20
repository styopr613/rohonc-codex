# METHOD — reading the Rohonc Codex, and the standing orders for whoever runs it next

This file is the method. Read all of it before touching anything. It was
written on 2026-09-20 after the method below carried the translation from
105 folios to 182 and produced 163 readings; every claim in it was paid for.

## Standing orders

1. **The target is lines fully read at 98%.** It is at 58.4% today. Nothing
   below stops until the user says stop. Do not end a turn to report a
   batch; report only when you are blocked on something only the user can
   decide. The user has said, more than once, that stopping between batches
   is the single worst thing about this work.
2. **Every turn does two things at once:** translate the next six folios in
   page order, and read the signs those pages make readable. Translating
   alone does not move the number; translating uses signs already known.
3. **Start every session with**

        python3 ktnext.py

   It prints the next six untranslated folios as far as they read, the gaps
   on them with occurrence counts, and the lines that cite a source. That
   is the batch. It reads which folios are done from the translation file
   itself, so it is never stale. (The hand-kept set it replaced was 44
   folios behind on the day this was written.)
4. **Finish every batch with** the three checkers green and a commit:

        python3 gate.py && python3 check_results.py && python3 check_rohonc.py
        git add -A && git commit -m "Translate 100r-102v: ... 182 -> 188 folios"

   Never commit on a MISMATCH. It happened once (an insertion anchor missed
   on a line break), and the fix commit had to name the mistake.

## What exists

- `harness/proposals.json` — **the output.** 163 readings: 28 tier A, 52 B,
  81 C, 2 D, plus two `_withdrawn_` entries kept on the record. Add to it.
  Never edit K&T's dictionary in `data/rohonc/kt/`.
- `work/rohonc/translation/rohonc_translation.md` — the translation, 182 of
  441 folios. Resume at **100r**. Format per line:

        **N**  English
        `gloss as rendered`
        > note naming the source verse, if any

- `work/rohonc/translation/rohonc_reading_plus.txt` — the book rendered with
  our readings applied (`+word` tiers A/B, `?word` tiers C/D, `[?]` unread).
  Regenerate with `python3 kttranslate.py` after any change to
  `proposals.json`. Its output is byte-reproducible; if two runs differ, a
  set is being iterated somewhere and that is a bug.
- `harness/ktnext.py` — the next batch, one command.
- `harness/ktpage.py FOLIO "phrase"` — a folio as far as it reads, gaps as
  `<<hex>>`, beside every reference passage containing the phrase.
- `harness/ktcontext.py HEX ...` — every occurrence of a sign, rendered. A
  `*` marks a translated folio.
- `harness/ktgap.py --page FOLIO` / `--wide HEX` — lines one word short.
- `harness/ktresidue.py` — unread words cut into readable pieces plus one
  unknown, ranked by how many words each unknown blocks. `--audit` ranks
  every existing reading by blast radius.

## The loop, per batch of six folios

1. `python3 ktnext.py`. Read the six folios as they stand.
2. **Identify the passage.** The codex opens most readings with a formula:
   *written by holy John, in the sixteenth chapter*. The content is
   standard: gospel pericopes, the Golden Legend, the apocrypha, Latin-church
   preaching. Nine of ten citations checked land on the right chapter of the
   right evangelist. So a page is a puzzle with a known picture. Find the
   picture first. `ktpage.py FOLIO "a phrase from the rendering"` searches
   the corpus; `--find` guesses.
3. **Translate the page whole,** not line by line. If a line makes no sense
   against the passage, the reading of something in it is wrong. The user's
   rule: *where it makes no sense it is either a flag and unique, or more
   likely wrong.* Wrong is the way to bet.
4. **Fill the gaps from the source.** The hole in the line is whatever the
   passage has in that slot. Then run `ktcontext.py HEX` and check the fill
   at every other occurrence before it goes in. A fill that fails one clear
   occurrence is not entered at a lower tier; it is not entered.
5. **Enter the reading** in `proposals.json` with gloss, tier, n, and
   evidence naming folio:line for each decisive occurrence.
6. Append the translations under a `## NNNr — title` heading (that heading
   is what marks a folio done; `ktcontext.py` reads the file, nothing is
   kept by hand), bump the folio count in `ROHONC.md` and
   `check_rohonc.py`, rerun `kttranslate.py`, checkers, commit. Go to 1.

## Tiers, exactly

- **A** — survives every occurrence, or proved by an identical formula
  (the same sentence elsewhere with a defined word in the slot) or by a
  numeral resolving against a number the story supplies.
- **B** — survives most occurrences; the rest are unclear, not contrary.
- **C** — read from one passage, or checked against an outside source, with
  nothing internal to test it against.
- **D** — a sign that occurs ONCE, read from the single line it stands in
  with no source to check. It is a reading of the line, not of the sign.
  Keep it countable apart. Never let D or C inflate what has been checked.

A single clear contradicting occurrence drops the tier. Do not argue it away.

## What burned us, so you do not do it again

- **Blast radius.** A short piece enters the cut of every word containing
  it. `540` read as *shall* had 4 tokens of its own and fed 55 words, 99
  tokens, and produced *shall-slide* seven times and *shall-day-today's*
  for the daily bread. `570` as *ark* had 1 own token and fed 6 words,
  giving *to-not-chapter-ark* inside Abraham and Isaac. Both withdrawn;
  coverage fell 59.5% to 57.9% and that was the honest number. Run
  `ktresidue.py --audit` before entering any piece under three glyphs, and
  read the words it will feed, not just its own occurrences.
- **A reading inferred from a doubled sign, never checked at occurrences,**
  is a guess with a tier it did not earn. That is what *shall* was.
- **Theology is a check.** *Abraham signified this Jesus crucified* was
  wrong; the user caught it. Abraham is the Father, Isaac is Christ, and
  the codex said so on the next folio: *as Abraham gave his son, so God the
  Father gave his.* A name written twice is name + pronoun (K&T's rule), and
  that is what the line had.
- **Wrong readings that only source reading caught:** the `00b` family is
  *as* not *apart* (it carries the *as* in *forgive us our debts as we
  forgive*); `520b78` is *mount* not *the Mount of Olives* (Matthew 5:14
  needs *hill*); `5ee060` is *seven* not *the last* (K&T gloss `5ee` as
  *six*; folio 065r then says *Matthew chapter seven* over Matthew 7, and
  Luke 10's seventy and Luke 11's seven spirits follow).
- **Identical numbers hide churn.** The sense gate read 39.9% before and
  after a real change; the per-case diff showed 1,668 changed answers and an
  RNG confound. Never write "no effect" from a headline figure. Diff per
  case, pin every random draw across arms.
- **Set iteration made the page non-reproducible**: 224 lines differed
  between runs. Every loop that feeds the inventory iterates `sorted()`.
- **Tools drifting off one inventory.** `ktgap.py` and `ktcontext.py` were
  both behind the renderer. If a tool disagrees with the page, fix the
  tool before reading anything off it.
- **Statistical gates on this problem are done.** Eighteen were run; the
  last, `ktproof.py`, failed at 1.04x and the diagnostic showed the
  instrument cannot find a passage it is handed. The gate that works is
  step 4 above: does the reading hold at every occurrence.

## What validates, and what does not

- The **citation test** validates. The codex names evangelist and chapter;
  if the page then tells that chapter, the readings that made the page
  legible are right together. Nine of ten so far. Keep the list in
  `ROHONC.md` current and keep the miss (090v cites John 2 over John 3) on
  it.
- A **whole page reading as its source** validates the page.
- A **count of +words** validates nothing. Nor does coverage rising.
  Coverage fell when two wrong readings came out, and the book got truer.

## Coverage arithmetic, so no one promises what the numbers forbid

A line is 6.9 words, so fully-read lines are about (1-p)^6.9 for unread
word share p. Today p = 8.6%, lines 58.4%. Reading every one of the ~890
blocking pieces leaves p near 1.6% and lines near 90%. Reaching 98% needs p
near 0.3%, about ninety unread words in the whole book, and roughly seven
hundred signs occur exactly once. So the last stretch is source reading,
page by page, at tier C and D, and the figure for what has been CHECKED will
stay well below the figure for what has been READ. Report both, always.

## The book, as far as the pages say

A book of readings. Formulaic openings and closings, sources cited by
chapter, whole pericopes repeated verbatim (a Pauline passage at 068r and
again at 070v-071r; John 16 at 068v and 080r). Contents so far: the Life of
Adam and Eve, the Rood legend, Joachim and Anne, the Nativity, a Passion
from Matthew and John, the Improperia, Longinus, the harrowing of hell,
Emmaus with Cleopas named, Thomas, the Good Shepherd, the Lord's Prayer,
Dives and Lazarus, Nicodemus, the Great Supper, the Bread of Life, Augustine
and the child on the seashore, purgatory named at 088r:10, and the whole
company of heaven as one compound sign at 097. A logographic script is
language-independent; that is a use, not a disguise. Say "probably".

## After every change

    cd /home/ubuntu/voynich/harness
    python3 gate.py && python3 check_results.py && python3 check_rohonc.py

## Ground rules

Plain English to the user, short sentences, no tables in chat. No
subagents. Never `rm` a glob; backups `.pre`/`.post`, never reuse a name.
Credit Király & Tokai for the dictionary, transcription and grammar; the
readings in `proposals.json` and the translation are ours and say so. Fetch
at 1.5s intervals. Private for now.
