# METHOD — reading the Rohonc Codex, and the standing orders for whoever runs it next

This file is the method. Read all of it before touching anything. It was
written on 2026-09-20 after the method below carried the translation from
105 folios to 182 and produced 163 readings, and then run three more times
exactly as written, as a test, which took it to 200 folios and 203
readings. Every claim in it was paid for. The three test batches are the
last three "Translate" commits; read their diffs to see what a batch is.

## Standing orders

1. **The target is 90%, and the ceiling moves as readings land.** Lines fully
   read stand at 74.8% tonight, up from 62.4% this morning. Two earlier versions
   of this order were wrong and both were mine. The first said 98%, with no
   arithmetic behind it. The second said 82% and showed its working, and the
   working assumed that a sign occurring once in the book can never be read.
   That assumption was false: Kiraly and Tokai's own entries name hundreds of
   such signs, with folio and line, and reading them costs no guess.

   Measured on 2026-09-20 after that supply was worked out: 1,468 words have
   no reading, 1,181 distinct signs, 989 of them occurring exactly once. Read
   every one of the 192 signs that occur twice or more and lines fully read
   reach **90.3%**. Recompute that number after every batch rather than
   quoting this one; it rose from 82.0% to 90.3% in a single day because the
   hapax pile itself shrank.

   Nothing below stops until the user says stop. Do not end a turn to report
   a batch; report only when you are blocked on something only the user can
   decide. The user has said, more than once, that stopping between batches
   is the single worst thing about this work.

   Where the remaining work is, measured the same day:

        859 lines carry exactly one unread word. Each is one reading away
            from being a fully read line. `ktgrind.py` ranks them and
            attaches every constraint that bears on the hole.
        989 signs occur exactly once and are not named anywhere in K&T's
            apparatus. These are the real wall. A reading of one cannot be
            checked against a second occurrence and cannot rise above C.
          6 signs are still named in K&T's entries and unread. That seam,
            which was 370 signs and 577 words this morning, is worked out.
            `ktsupply.py` reports what is left of it in one command.
        155 passages are written twice, but ktdouble.py matches on token
            types, so a sign occurring once can never fall inside a match.
            A gapped alignment of the two copies would reach at most 278
            of the hapaxes and is the largest unbuilt idea on the list.

   **The fast loop for those 859 lines, built 2026-09-20 evening, is
   `ktleft.py`.** It turns the crosser-off round. Where the translation names
   the passage a folio retells, the words of that passage (King James, verse-
   numbered, `data/ref/rohonc/bible_kjv_verses.txt`) minus every word a sign
   already carries are the pool the folio's holes can still be. Four modes:

        python3 ktleft.py --wide 1 --cross   # signs on 2+ cited folios whose
                                             # passages SHARE a free word.
                                             # Start here: the intersection
                                             # does K&T's carry-it-everywhere
                                             # test before you guess.
        python3 ktleft.py --wide 1 --holes   # one-hole lines on cited folios,
                                             # smallest pool first
        python3 ktleft.py --wide 2 128v 129r # one folio: pool beside holes
        python3 ktleft.py                    # the whole pool, ranked: what
                                             # the book still has no sign for

   Its first run gave eight readings in an hour (hateth, became, dust,
   gate/open, gates, chapter, exceed, garment; 74.4% to 74.8%). Rules that
   came out of that run:

   - The pool is candidates, not readings. Carry the word to every line the
     sign stands on (`ktgrind.py HEX`) and check `ktcross.py --taken WORD`
     before entering. Two occurrences in the same retold sentence (the
     doubled Life of Adam on 007r/125r) is one passage, tier C.
   - A word the pool calls free may be a synonym of one that is taken: it
     lists tell, meat, flesh, arise, sepulchre, depart because K&T glossed
     say, food, body, rise, grave, go away. Check the concept, not the word.
   - **Pool from the Douay-Rheims, not the King James.** The book is a
     Catholic compilation and its author had the Vulgate; an English
     candidate list built off a Protestant translation manufactures
     near-misses. Measured 2026-09-20 over 181 cited folios: the King James
     pool holds 1,960 words, 652 of them — **a third** — are wording the
     Douay does not use. Two readings already entered were among them and
     both were corrected: *exceed* at Matthew 5:20 is the King James word
     where the Vulgate has *abundaverit*, Douay *abound*; *dust* at Genesis
     2:7 is the King James word where the Vulgate has *de limo terrae*,
     Douay *slime*, and dust properly belongs to Genesis 3:19, a different
     Latin word. The clinching case is Mark 16:14, where the King James says
     the eleven sat *at meat* and Douay says *at table* — and this project
     had already read a sign as *at table* from K&T's own citations while the
     King James pool was still offering *meat* as a candidate.
     ktleft.py now prints three classes and the order is the order of trust:

         both  : free in both translations, the safest candidates
         douay : Douay only, the author's own tradition
         KJV   : King James only, weakest, usually a translator's word

     Douay also carries the deuterocanon, so Tobias, Judith, Wisdom,
     Ecclesiasticus, Baruch and Machabees can be cited in a note and looked
     up; the King James file here cannot. Not handled: Douay follows the
     Septuagint psalm numbering and runs one behind from Psalm 10 to 146, so
     treat any psalm pool as King James only.
   - A sign inside K&T's own spellings is read from them: their four gate
     and open spellings all end in ab0, so ab0 is gate/open. Their 670 is
     chapter, so 432670 after a numeral is chapter.
   - An empty intersection is a result: the sign is not a content word of
     the passage. Do not force one.
   - ktcross's stemmer was not idempotent until this evening (priests
     stemmed to priest, priest to pri) and reported kissed and priests as
     free while kiss and priest were taken. Fixed to a fixed point; if the
     free list ever offers a word whose base form is taken, that is the bug
     to look for. The same fault came back in a second form on 2026-09-20:
     the stemmer had no nominalising rules, so *judgment*, *appearance* and
     *righteousness* reported free while *judge*, *appear* and *righteous*
     were all taken, and a reading was nearly made on one of them. Endings
     like -ment, -ance, -ness and -tion are stripped first now, longest
     first, and the handful the rules cannot reach (salvation, forgiveness,
     belief, wisdom, truth, life, death, creature) are aliased by hand, each
     one checked against the dictionary before it went in.
   - **The King James book names do not survive a regex.** The first version
     of ktleft named each book by pattern-matching the Gutenberg heading,
     which merged 1 and 2 Kings, merged the gospel of John with the three
     epistles of John, lost Samuel altogether and filed Revelation under
     "Divine". A note reading "Kings 19:6" then fetched 2 Kings 19, Rabshakeh
     and the king of Assyria, for a page about Elijah and the cake baken on
     the coals -- and the shared-word intersection duly offered *rabshakeh*
     as a candidate for two folios that never mention him. Books are assigned
     by canonical position now, advancing at each "1:1", and a bare name
     means the first book of that name. The check is cheap: 66 books and
     31,102 verses, which is the King James exactly.
   - **A verse does not start at the start of a line.** The same first
     version only recognised "N:M" at the beginning of a line, and the King
     James wraps, so every verse swallowed the opening of the next one and
     every pool carried a neighbouring verse's words. Genesis 2:7 came back
     with *planted* and *eastward* in it, which are 2:8. Split on the marker
     wherever it falls.

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
