# Superseded drafts

## retelling.md

The first Book One. Codex rewrote Book One on 2026-09-22 and the book has
printed `work/rohonc/translation/reading.md` ever since; this file stopped
being the deliverable that day and nothing has printed it since.

It stayed in the working tree, and two checkers went on reading it. That cost
a day. `ktretellcheck.py` measured its 1,142 guillemet quotations and reported
the strictest-looking pass in the project while the printed book was checked by
nothing; `ktnotecheck.py` proved all 50 endnote anchors stood in it, which was
true and beside the point, because not one of those anchors is in the printed
text and `ktbook.annotate()` has always placed those notes by folio instead.
Both now read the file the book prints. `ktbook.build()` no longer falls back
to this file either: a missing Book One is a failure, not something to
substitute a draft for.

Kept because the quotations record how the readings stood before the hardening
sweeps of 21-22 September, when `eternal*` became `heaven*`, `anointed*` became
`~place`, and the guess `[cherubim]` gave way to `can_be` on Kiraly and Tokai's
own published translation of that sentence.
