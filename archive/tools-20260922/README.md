# Retired tools

## whatbroke.py

"The one command to run when the readings have been hardened." Its first line
was its premise: *Book One quotes the gloss.* Four sections, all of them
counting guillemet quotations -- what broke, what is exposed to a bracketed
guess, what is load-bearing, what is left.

The premise stopped being true when Codex rewrote Book One. The printed text
carries no guillemets at all, so every section of this measured the draft in
`archive/drafts-20260922/`, and the quotation check it ran on top of
`ktretellcheck.py` was removed on 2026-09-22 for the same reason. It imported
`ktretellcheck.QUOTE`, which no longer exists.

**What does its job now.** `harness/ktpush.sh` regenerates everything the
readings produce and runs every gate before anything is published, which is the
drift this tool was written to catch. `ktverify.py risk` is the accounting of
Book One against the gloss -- the share of content words that are the
manuscript's own -- and `front_matter()` prints that accounting from
`ktverify.accounting()`, so it cannot go stale in the book. Section 4's
question, which folios Book One has not drawn on, is `ktbook.cited_folios()`;
all 441 are cited.

Kept because its section 3 named a real blind spot that still exists: a
quotation is checked, the editorial sentence around it is not.
