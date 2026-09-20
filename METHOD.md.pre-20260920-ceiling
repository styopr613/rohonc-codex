# METHOD — reading the Rohonc Codex, and the standing orders for whoever runs it next

This file is the method. Read all of it before touching anything. It was
written on 2026-09-20 after the method below carried the translation from
105 folios to 182 and produced 163 readings, and then run three more times
exactly as written, as a test, which took it to 200 folios and 203
readings. Every claim in it was paid for. The three test batches are the
last three "Translate" commits; read their diffs to see what a batch is.

## Standing orders

1. **The target is lines fully read at 98%.** It is at 59.1% today. Nothing
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
4. **Finish every batch with one command,** which carries the live figures
   into the documents, runs the three checkers on their real exit status,
   and commits only if all pass:

        ./ktcommit.sh "Translate 108r-110v: what the pages are. 200 -> 206 folios; 59.3% lines"

   Do not commit any other way. Three commits went in with a failing
   checker because `python3 check_rohonc.py | tail -1 && git commit` reports
   tail's exit status, not the checker's. Each needed a fix commit that
   named the mistake.

## What exists

- `harness/proposals.json` — **the output.** 203 readings: 54 tier A, 60 B,
  85 C, 4 D, plus two `_withdrawn_` entries kept on the record. Add to it.
  Never edit K&T's dictionary in `data/rohonc/kt/`.
- `work/rohonc/translation/rohonc_translation.md` — the translation, 200 of
  441 folios. `ktnext.py` says where to resume. Format per line:

        **N**  English
        `gloss as rendered`
        > note naming the source verse, if any

- `work/rohonc/translation/rohonc_reading_plus.txt` — the book rendered with
  our readings applied (`+word` tiers A/B, `?word` tiers C/D, `[?]` unread).
  Regenerate with `python3 kttranslate.py` after any change to
  `proposals.json`. Its output is byte-reproducible; if two runs differ, a
  set is being iterated somewhere and that is a bug.
- `harness/ktnext.py` — the next batch, one command: the next six
  untranslated folios rendered as the page renders them, the gaps with
  occurrence counts, the lines that cite a source.
- `harness/ktlook.py HEX ...` — K&T's own entry for a code and for every
  defined piece inside it. **`ktlook.py --cite 100r10 ...`** prints every
  entry of theirs that cites those lines. This is the single most
  productive check found in the three test batches; see step 3 below.
- `harness/ktbump.py` — carries the live figures (folios, signs, tier A,
  lines read) into `ROHONC.md` and `check_rohonc.py` from the saved run.
  `ktcommit.sh` runs it; you never retype a figure.
- `harness/ktcommit.sh "message"` — the only way to commit.
- `harness/ktpage.py FOLIO "phrase"` — a folio as far as it reads, gaps as
  `<<hex>>`, beside every reference passage containing the phrase.
- `harness/ktcontext.py HEX ...` — every occurrence of a sign, rendered. A
  `*` marks a translated folio.
- `harness/ktgap.py --page FOLIO` / `--wide HEX` — lines one word short.
- `harness/ktresidue.py` — unread words cut into readable pieces plus one
  unknown, ranked by how many words each unknown blocks.
- `harness/ktdouble.py` — **the passages the book writes twice.** It finds
  every run of eight or more consecutive word types that occurs in two
  places sixty tokens apart, merges them and prints the longest first.
  There are 155 such runs. The creation narrative runs twice (002v-003v and
  121v-123r), the Adam and Eve narrative twice (007r and 125r onward), John
  16 twice (068v and 080r), the Bread of Life twice (030v and 095r), and
  the Mark 16:16 creed four times. Use it before translating any folio:
  `ktdouble.py --show 125r` prints both copies of every run on that page
  side by side. The two copies are never equally readable, so the better
  one reads the other's gaps, and a sign standing in the matching slot of a
  parallel sentence is proved the way a formula slot is proved. That is
  tier A evidence, not a guess. `--audit` ranks
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
3. **Ask their apparatus before guessing.** Run
   `ktlook.py --cite` on every line that has a gap. Király & Tokai cite
   folio:line in every entry, for examples and for each variant spelling,
   and a gap on a line they cite is usually a word they already read under
   a spelling the transcription writes differently (one glyph swapped: 520
   for 670, 540 for 569, 690 for 5d1). In three batches this gave brother,
   Saint Augustine, sword, lame, resurrect, go not away, Adam, bosom, rent,
   stayed, shed his blood, found, bound up, the Samaritan: fourteen tier A
   readings, each checked at every occurrence by their own citation list.
   When their citation names a line and the only unread word on that line
   is yours, that word is theirs. Enter it tier A and say so. When TWO
   words on the line are unread and one citation covers them, you cannot
   tell which they meant: leave both and say so on the page. That happened
   twice, at 112v:1 and 114v:3.
   Then run `ktdouble.py --show FOLIO`. If the page is a second copy of a
   page elsewhere, read them together.
4. **Translate the page whole,** not line by line. If a line makes no sense
   against the passage, the reading of something in it is wrong. The user's
   rule: *where it makes no sense it is either a flag and unique, or more
   likely wrong.* Wrong is the way to bet.
5. **Fill the gaps from the source.** The hole in the line is whatever the
   passage has in that slot. Then run `ktcontext.py HEX` and check the fill
   at every other occurrence before it goes in. A fill that fails one clear
   occurrence is not entered at a lower tier; it is not entered.
6. **Enter the reading** in `proposals.json` with gloss, tier, n, and
   evidence naming folio:line for each decisive occurrence.
7. Append the translations under a `## NNNr — title` heading (that heading
   is what marks a folio done; `ktcontext.py` reads the file, nothing is
   kept by hand). Regenerate the saved run, then commit:

        python3 kttranslate.py > ../work/rohonc/kttranslate.txt
        ./ktcommit.sh "Translate ...: ... N -> M folios; P% lines"

   Go to 1.

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
- **A name read from one page can be the wrong prophet.** *Enoch* stood for
  a day; the sign is K&T's Elijah with one glyph swapped, and the Horeb
  page (133r) said so. When a name sign is yours, look for their spelling
  of the same name and compare glyph by glyph before anything else.
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
- **Numerals cut at the wrong stroke.** The renderer read five strokes +
  thousand as *three* + *two thousand*, because *two thousand* was a known
  word. Every stroke-numeral compound is now entered whole by K&T's rule
  (strokes, then a ten/hundred/thousand sign that multiplies them). If a
  new one appears, enter the whole word, never the piece.
- **A hand-kept list of done folios drifted 44 folios behind the file.**
  `ktcontext.DONE` now reads the translation's headings, and the checker
  tests that they agree. Never keep state by hand that a file already holds.
- **A commit chain that pipes the checker masks its exit status.** Use
  `ktcommit.sh`. And a `re.sub` replacement string turns `\n` into a real
  newline; `ktbump.py` uses a function replacement for that reason.
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
