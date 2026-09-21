# Where this stopped — 2026-09-21

## BOOK ONE IS FINISHED

All ten parts are written, `ktretellcheck.py` passes at its bar of zero, and
the retelling draws on **441 of 441 folios** — every leaf of the manuscript is
cited somewhere in the front of the book. Ten chapters, 19,988 words; the
whole volume is 88 chapters and 105,349 words.

Run `cd harness && python3 whatbroke.py` after any change to the readings.
`fix.md` at the repo root is the standing instruction for what to do with what
it reports. The one thing no checker can do for you is its section 3, and that
now has exactly one entry: **Enoch**, bracketed in all three places it stands
in the manuscript and read in none.

**Build straight to the shelf, always, without asking:**

    python3 ktbook.py --shelf /opt/publish-app/data/u1/books/20260921-052535-r0hc

That is the owner's private Book Maker shelf and it is where the book belongs
the moment it builds. It is not publishing; `/var/www/oona13/library/` is the
public Free Library and that one does need asking. Back up the old
`book.json` first and never reuse a backup name.

Open item: `ktcommit.sh` still does not regenerate the reader's edition — see
the traps section of `fix.md`.

What follows is the record of how it got here.


The manuscript is finished: 441 of 441 folios. `ktnext.py` prints "0 to go".
What is unfinished is **Book One, the retelling**, and this session got most
of the way through it. The user stopped the run here and said the work may
need to be redone, so read the next section before building on any of it.

## State of the retelling

`work/rohonc/translation/retelling.md`. Eight of ten parts are written and
`ktretellcheck.py` passes at its declared bar of zero.

    I    The Fall of Lucifer          004v-006v   written, re-marked
    II   Flood to the House of David  008r-015v   written
    III  Joachim and Anne             016r-022r   written
    IV   The Twelve Signs             022v-028v   written
    V    The Passion                  029r-052v   written this session
    VI   Burial to Ascension          053r-009v   written this session
    VII  The Preaching                064r-182v   THREE of five stretches
    VIII Finding of the Cross         183r-214v   NOT WRITTEN
    IX   Acts of the Apostles         215r-220v   NOT WRITTEN
    X    The Last Things              221r-224v   written, re-marked

Part VII is one `##` block with `####` sub-headings inside it, because
`ktbook.retelling()` looks each part up by its exact name in `ktbook.PARTS`.
Its stretches, this edition's divisions and not the book's:

    written:  The last discourse, the Ascension, and Pentecost   064r-082v
              The Trinity, Augustine, and the rich man           083v-099v
              Elijah, Jerusalem, and the parables of what
                was lost                                         100r-121r
    missing:  Genesis retold, Hezekiah, the Unmerciful Servant,
                and the Virgin cycle                             121v-147v
              Barlaam, the healings, the stewards and
                the lepers                                       148r-182v

## When the readings have been hardened

    cd harness && python3 whatbroke.py

One command: what broke, what is exposed, what is load-bearing, what is left.
`fix.md` at the repo root explains each section and what to do about it. The
short answer is that Book One quotes Kiraly and Tokai seven eighths of the
time, so hardening our own readings cannot move most of it: 13.1% of
quotations are exposed, the bar for patching rather than rewriting was a
fifth, and it was declared before the count was run.

## THE NEXT THING TO DO

Write the missing two stretches of Part VII, then Parts VIII and IX, then
rebuild the book with `ktbook.py`. The loop that worked, three times:

    cd harness
    python3 ktquote.py part VIII                 # English + gloss, whole part
    python3 ktquote.py show 148v 149r 149v       # the folios you mean to quote
    ...write the prose, quoting the GLOSS, in «guillemets»...
    python3 ktretellcheck.py                     # bar is 0

`ktquote.py` is new this session and is the clerk for this job: `show`,
`part`, `check ... -- phrase`, `find word`. Quote the gloss, never the
DeepSeek English — the English is allowed a leak budget and the gloss is not,
which is exactly why the gate reads the gloss.

Set pieces still to write, named by the outside reader: **Barlaam's man in the
pit** with the two mice and the lance (148v, 149r, 149v); **the prodigal told
a second time** (150r, 150v); **the captive and the king** (154v-158v);
**Chosroes on his gold tower and barefoot Heraclius** (183r, 183v, 185r,
186r); **Stephen's stoning with Saul holding the coats** (218r, 218v, 216v,
219r).

## What this session changed, and the one thing that might need redoing

1. **`ktbook.folios()` was dropping 527 gloss lines, 12.1% of the
   manuscript.** Its pattern for a numbered line was `^\s{2,}\d+\s`; the
   reader's edition right-aligns numbers in a width-3 field, so line 9 is
   `  9  word` and line 10 is ` 10  word` with one space. Every line numbered
   ten or higher fell out of Book Two and out of the retelling gate that reads
   it. `ktenglish` had the right pattern all along. Both now use one, and they
   agree on all 441 folios. Backup: `ktbook.py.pre-linefix-20260921`.

   **This is the change to check first if anything here is redone.** Fifteen
   of the retelling's 28 standing failures were caused by it, not by bad
   prose, and Book Two's line-by-line text was missing an eighth of the book
   in every build before today.

2. **`ktcommit.sh` now runs `ktretellcheck.py`** alongside the other three.
   Backup: `ktcommit.sh.pre-retellgate-20260921`.

3. **Parts I and X now quote in guillemets, not italics**, which is what puts
   them under the gate at all: they declared 0 quotations before and 110 now.
   Every quotation in the file — 717 of them — is checked word by word
   against the gloss of a folio the part cites.

4. **A claim in Part X was wrong and is corrected in place.** It said 222v is
   the only leaf where the sign glossed *the name of the author* stands. It
   stands on three: 137v, 138r and 222v. On the first two he writes himself
   into a prayer to the Virgin; 222v is the only page where he records what he
   did rather than what he asks for. The correction says it was wrong rather
   than quietly amending it.

## Rules that cost something to learn, for this job specifically

- **Quote the gloss, not the English.** Roughly twenty quotations in Parts
  II-IV were lifted from the model's English and had to be rewritten:
  «grabbed every creature» became «grab each, every create», «from dying»
  became «from die», «the beginning of the suffering» became «this is begin
  suffering».
- **The stemmer will not unify a doubled consonant** — grab/grabbed,
  sin/sinned, begin/beginning all read as different words. That is the safe
  direction to fail in and it was NOT widened. Write the gloss's own form.
- **A digit anywhere in the prose must be declared** in `ktretellcheck`'s
  `ARITHMETIC` or written as a chapter-and-verse reference, which the gate
  strips. "Genesis 9" failed; "Genesis 9:21" passes and is truer.
- **Do not number sub-headings.** `#### 1. The last discourse` is a NUMBER
  FAIL. Spell it or drop it.
- **A folio outside the part's span needs `cf.`** — `cf. 159r`, and it must be
  written that way in the sentence, not in a footnote.
- **Never quote the word "guillemets" in guillemets.** The gate cannot tell an
  editorial mention from a claim, and it is right not to try.
