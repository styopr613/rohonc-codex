# THE DARK WORDS — the last 3.6% of the Rohonc Codex

A self-contained job for a fresh session. Read this file, then start. You do
not need to know anything else about the project to do it, but `METHOD.md`
and `BLINDFOLD.md` are next door if you want the background.

## What the job is

The Rohonc Codex is 29,997 words. 93.1% are read, 3.2% are read from one
passage, and **1,087 words are dark**: 930 signs the rendering cannot read,
813 of them occurring exactly once in the whole book. This job is to make
ONE written decision per sign — a reading, a guess, or "leave it dark" — and
get every decision into the deposit through the tools below.

The work is judgment, sign by sign. Nothing here can be automated further;
the dossier already puts every signal on one screen. What the previous
session could not do was sit and read 930 dossiers. That is the job.

## What a guess is worth (measured, do not re-measure)

    python3 ktguess.py --test --rare 400        (saved: work/rohonc/ktguess_rare.txt)
      passage pool holds the true word           7.8% of rare words
      top candidate correct, over all trials     2.0%
      top candidate correct, when present       25.8%

So a guess made from the passage alone is right about one time in four
WHEN the answer is in the passage, and the answer is usually not. That is
why a guess is tier G, is shown in brackets in the reader's edition, and is
never counted as read. Guess anyway where the slot demands a word; the
reader's edition front matter already explains what a bracket is worth.

## The tools (run from `harness/`)

    python3 ktdark.py dossier          the dossier for every unread sign, queue order
    python3 ktdark.py dossier 40       the next 40
    python3 ktdark.py apply FILE.json  write decisions into proposals.json (dated backup)
    ./ktcommit.sh "message"            the ONLY way to commit: regenerates the saved
                                       run, runs three checkers, refuses on failure
    python3 ktqueue.py pass HEX why    park a sign you have decided to leave dark,
                                       WITH the reason; it drops out of the dossier
    python3 ktlook.py HEX              Király & Tokai's own entry for a code and its glyphs
    python3 ktlook.py --cite 100r10    their entries that cite a line
    python3 ktreader.py                regenerate the reader's edition after applying

A full dossier is saved at `work/rohonc/dark_dossier.txt` (6,642 lines, 943
signs, made before batch 1). Regenerate it when you start; 13 signs are gone.

## How to read one dossier entry

    === 520ab8   x2   2 glyphs   completes 2 line(s)
      near  520 = away; to                      one glyph from a read sign
      cover away; to + ?ab8   (50%)             greedy cover by read signs
      063v:8   ... go holy-Thomas <<___>>       the line, hole marked
      181r:6   exist go holy-Thomas <<___>> one Saturday evening
      src   063v: John 20:24–25                 the passage the folio's note cites
      pool  063v: didymus, print, twelve        free words of that passage, rarest first

`in` = the sign sits inside a read sign; `holds` = a read sign sits inside
it. `[A]`/`[B]`/`[C]` after a gloss marks this project's own readings; the
rest are Király & Tokai's. A free word is one no sign already carries; if the
word you want is NOT in the pool, some other sign already means it, and your
guess would make two signs for one word. Prefer free words.

## The decision rule

Write ONE of three things per sign.

**Tier C** — a real reading. Requires BOTH: a structural anchor (`in`,
`holds`, `near` on a sign whose meaning fits, or the same word in the cited
passage at two or more occurrences) AND a fit at every occurrence you can
check. Say which occurrence does not fit, if one does not. Examples from
batch 1: `796143` = is_dead (one glyph from K&T 'dead', both lines are
"Abraham ... [x]", John 8:52 "Abraham is dead"); `520670502520060` = loose
(Matthew 16:19, both slots).

**Tier G** — a guess. The slot demands a word, the passage or the story
supplies one, nothing structural confirms it. Write the evidence and end it
with the word GUESS. Examples: `52070b` = cherubim (Eden both times, Gen 3:24
cited, 'cherubims' the free word); `606520` = arise (line-initial before
"take the child and his mother", Matthew 2:13/2:20).

**Dark** — `ktqueue.py pass HEX "reason"`. Use it when the slot is open:
a single glyph in three unrelated contexts, a name-shaped sign with no name
in the passage, a damaged line. Leaving a sign dark is a decision too and
it must be written down, or the next session re-reads the dossier.

Rules that are not negotiable:

- **A story that fits is not evidence.** If you can tell a story for two
  different words, it is G or dark, never C.
- **A near miss is a miss.** One occurrence that does not fit is written
  into the evidence, not explained away.
- **If the stem is already carried by another sign, do not guess it** unless
  you can say why the book would write one word two ways here (it does:
  055r:10, 144v). Say so in the evidence.
- Single glyphs are usually particles. Do not guess a noun for a one-glyph
  sign unless the slot is unmistakable.
- Do not read K&T's dictionary files in `data/rohonc/kt/` directly and never
  edit them. `ktlook.py` is the window.
- Numerals: `060` = one, `060060` = two, ... Before guessing a number, check
  how K&T write it (`ktlook.py`). Two open numeral cases are noted below.

## The batch loop

1. `python3 ktdark.py dossier 40 > /tmp/d.txt` and read it.
2. Write `work/rohonc/dark_batch_NN.json` — `{"hex": ["gloss", "C|G", "evidence"], ...}`,
   NN counting up from 02. Never reuse a filename. Underscores join a
   multi-word gloss (`is_dead`, `the_way`).
3. `python3 ktdark.py apply work/rohonc/dark_batch_NN.json`
4. For each sign you leave dark: `python3 ktqueue.py pass HEX "why"`.
5. `python3 ktreader.py > /dev/null` then `./ktcommit.sh "Dark words, batch NN: ..."`.
   The message lists what was read (C), what was guessed (G), and how many
   were parked. If a checker fails, fix the cause; do not skip the checker.
6. Repeat. Many batches per turn. Do not stop to report between batches.

Do not add a "translation" of a folio; the translation is complete. Do not
touch `ROHONC.md`, `CONCLUSION.md` or `METHOD.md` except to correct a figure
`ktbump.py` does not carry. The reader's edition regenerates itself.

## Open cases already looked at, not decided

- `0600600600601f7060060060060` after "holy Matthew" at 087v:2 and 202v:8
  (202v cites Matthew 22). Looks like a chapter number: four + `1f7` + four.
  Find how K&T write 8 or 22 before deciding. `1f7` has no K&T entry.
- `433` in "nine [x] chapter" at 205v:5 (Luke 19 cited) and "14-one [x]
  chapter" at 210r:3 (Matthew 12). If it were "-teen"/"ten", 9+10 = 19 fits
  the first and not the second. Check what "14" actually is at 210r.
- `343`, `7c2`, `813`, `984`: multi-occurrence single glyphs, no consistent
  slot. Probably particles. Park them with that reason unless you see more.
- `5405200602b1` x3 on 144v–145v (the woman and the image, three visits,
  "grab bread and [x]"). No source; the story is in the folio notes.

## When you are done

Report: how many C, how many G, how many parked; the new figures from the
last `ktcommit.sh` line; and the five decisions you are least sure of, by
hex. The user reads plain English, short sentences, no tables.
