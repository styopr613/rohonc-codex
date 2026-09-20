# NEXT — Rohonc translation (updated 2026-09-20)

## Where it stands

**59 of 441 folios are translated**, in
`work/rohonc/translation/rohonc_translation.md` — 674 lines of the codex,
English first with the gloss underneath so every choice can be checked.

Done, in Kiraly & Tokai's page order:

    004v 004r 002r 002v 003r 003v 001r 001v   the Life of Adam and Eve
    007r 007v 006r 006v 008r 008v 005r 005v   Eden to Abraham
    015r 015v 016r 016v 017r 017v 018r 018v   David, Joachim and Anne, the Annunciation
    019r 019v 020r 020v 021r 021v             the Nativity and the flight into Egypt
    022r 022v 023r 023v 024r 024v 025r 025v   Egypt, the numbered signs, Tabor, the baptism
    026r 026v 027r 027v 028r 028v 029r 029v   the confessions and the Last Supper
    030r 030v 031r 031v 032r 032v             the washing, the Eucharist, the betrayal
    033r 033v 034r 034v 035r 035v             Gethsemane and the arrest
    137v                                      the Marian prayer K&T published

## Resume at 036r

Next in page order: **036r 036v 037r 038r 038v 039r 039v 040r 040v 041r ...**
(there is no 037v in the transcription). The Passion is in progress and runs
on from the arrest. Keep going in page order to the end.

## How

1. `harness/page.sh 036r 036v 037r ...` prints the full-sense gloss for those
   folios. `work/rohonc/translation/rohonc_reading.txt` is the one-sense
   version and is easier to read; use the full one when a sense choice
   matters.
2. Append to `rohonc_translation.md` in the established format: `**n**` then
   the English, then the gloss in a code span on the next line. Keep the
   quoted-note blocks where a line matches a named chapter and verse.
3. Six to eight folios per batch, then commit. Do not stop to run gates.
4. `harness/check_rohonc.py` has a check on the folio count in the
   translation file — update the number when you extend it, or it fails.

## What has been found so far

The book is the **Life of Adam and Eve** (the apocryphal one, not Genesis),
then the Legend of the Rood, Noah, Abraham, the Protevangelium's Joachim and
Anne, the Nativity, and from 029r a Passion the codex says it takes from
Saint Matthew and Saint John. The frame is an angel revealing it all to
**Elijah the prophet**.

Numerals: parts add, and a `ten` after a group multiplies by ten. Confirmed
four times against a number the source supplies (forty days and forty nights,
forty days of rain, the eighth day, the twelve apostles).

Grammar: the list marker in front of a numeral makes an ordinal, which is how
the book numbers the signs of Christ first to eleventh.

Unread words guessed from context are tabled at the top of the translation
file. `EAE0` (217 occurrences) is almost certainly **day**.

## Ground rules still in force

- No subagents. Plain English to the user. Never `rm` a glob. Backups
  `.pre`/`.post`. Fetch at 1.5 s if fetching.
- Credit K&T for the dictionary and the grammar. The translation is ours;
  the glosses are theirs. Private for now.
- `harness/check_rohonc.py`, `gate.py`, `check_results.py` must stay green
  after any edit to the documents.
