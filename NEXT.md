# NEXT — Rohonc translation (handoff, 2026-09-20 night)

## The job

**Translate the book.** Line by line, into English sentences. The user has
asked for this repeatedly and does not want more measurement, more gates or
more proposals first. Start translating in the first turn of the next
session. Do not ask whether to begin.

## What exists

- `work/rohonc/translation/rohonc_reading.txt` — the whole book, 441 pages,
  4,372 lines, every word glossed in K&T's page order. First sense only.
- `work/rohonc/translation/rohonc_reading_full.txt` — same, every sense,
  glyph codes for unread words. **Translate from this one.**
- Marks: `word/word` several senses, theirs first; `word-word` a composed
  code; `~word` a declared variant; `[?xxx]` unread; `|` a gap.
- Coverage 78.8%. 11.3% single-sense, 47% several senses, 19.2% composed,
  1.2% declared variants, 21.2% unread. 975 lines fully glossed.
- Context cannot choose senses (ktsense 39.9%, ktgrammar 0.97x). A reader
  has to. That reader is the model, and its blind record is 1–2 of 6.

## How to do it

1. Write to `work/rohonc/translation/rohonc_translation.md`. One section per
   folio, in K&T's page order. For each line: the gloss line, then the
   English below it. Keep the two together so anyone can check.
2. **Start with folio 137v** — the page K&T published a reading for — then
   the opening folios 004v, 004r, 002r, and onward in page order.
3. Choose one sense per word. Supply articles, tense, word order. Mark every
   real guess with `(?)`. Render an unread word as `[…]` and, where context
   makes it obvious, a guess in brackets: `[the serpent?]`.
4. When an unread code gets the same guess in three or more places, note it
   in a table at the top: code, guess, folios. That is the K&T method and
   it is how the dictionary grows. Do not add it to the dictionary; list it.
5. Batch by ~20 folios per turn. Commit after each batch. Keep the report
   to the user short: which folios, what they seem to be about, what was
   guessed.
6. Do not run any new gate before translating. If a gate is wanted later
   for the new-word guesses, it is: does the guess hold at every occurrence.

## Ground rules still in force

- No subagents. Plain English to the user. Never `rm` a glob. Backups
  `.pre`/`.post`. Fetch at 1.5 s if fetching.
- Credit K&T for the dictionary and the grammar. Private for now.
- `harness/check_rohonc.py`, `gate.py`, `check_results.py` must stay green
  after any edit to the documents.

## First pass at 137v, from the full gloss (not yet written to the file)

    1  Hail, Virgin, through holy Mary, mother of God [?] [?]
    2  Queen Mary, [?] lady [?] [?] | you
    3  Mary, the one and only virgin maiden; you, Mary, conceived Jesus without [sin?]
    4  Born of Mary [?], and from the Lord the Redeemer, in the Lord | this [author]
    5  We do not doubt, [author], we [?] | this [author]
    6  We pray you, Mary, [?] | of [author]
    7  We, when it is [?], the soul is forgiven | of [author]
    8  We are, chapter, amen. This prayer must be.
    9  [?] have mercy, Hail Mary, [?] have mercy [?] | Lord

K&T's published reading of line 3 is "sin, without, Jesus, conceive,
you-Mary" — matches. The right-margin column (`| this-author`, `| of-author`)
is a colophon: the author's name sign repeated down the side.
