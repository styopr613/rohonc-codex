# Where this stopped — 2026-09-22

## TOMORROW: THE COVER BADGE (Cover Maker design 20260921-212932-2sdz)

The cover's "THE FIRST COMPLETE ENGLISH RENDERING" roundel was baked into the
art, not a badge. Done so far, all in Cover Maker's own data, nothing pushed to
Book Maker or the site yet:

- The roundel is cloned out of the raw art with paper from the same band
  (`gen/20260921-212932-2sdz.png`; backup `.png.pre-badge-20260922`). A faint
  disc ghost is visible where the patch is cleaner than the paper around it.
- A real Cover Maker badge is in the saved design (`.meta.json`; backup
  `.meta.json.pre-badge-20260922`): shape `label`, flat, red #b3261e, white ink,
  `badge_show` true (that flag gates drawing), placed by `badge_x` 0.30 /
  `badge_y` 0.085 where the roundel was, size 0.9, stretch 1.3. Text
  "FIRST EDITION EVER\nNEVER BEFORE READ" -- the label draws ONE line, so the
  second is dropped; use `badge_text2` or a seal/ribbon if both lines are wanted.
  Rendered front: `scratchpad/front_try2.jpg` -- red rounded label, clear of
  the title. The owner's words for it: first edition ever, never before read,
  never seen by human eyes; "I'm a popularizer not an academic". It dates
  itself 1593, so "four centuries", not six hundred years.

Still to do: adjust in the studio if wanted; then Book Maker re-import of the
composed front (`_render_cover_wrap(uid, gid, dst, mode="front", dpi=300,
maxpx=2560)` from `/opt/publish-app/web/bookapi.py`, the same call
`/api/covers/use` makes, writing the shelf's `cover.jpg`); rebuild the book
(`ktbook.py --shelf ...`, which also publishes the reader's EPUB); the KDP wrap
is built in the studio; the site's `img/book3d.png` was made by hand and still
shows the old roundel.

## THE NEXT THING TO DO: THE GITHUB REPOSITORY

Every page that used to link a data file or a program now says "will be
posted to GitHub", and nothing is served from /rohonc/data or /rohonc/code any
more (the one exception is `data/dictionary.json`, which the dictionary page's
search loads; it is not linked). When the repository exists:

1. What goes up: `harness/`, `work/rohonc/` (the saved runs, proposals.json,
   english.json, the readers' edition, notes.md, reading.md, the outside
   readers' replies), the documents at the root. What does NOT: `data/rohonc/kt/`
   (Kiraly and Tokai's dictionary and transcription), `data/rohonc/latest.txt`
   and `scan/`, and `data/ref/` — see DATA_PROVENANCE.md for why each.
2. Replace the "posted to GitHub" sentences with the address. They live in
   `harness/ktsite_copy.json` (`data_lead`) and in `harness/ktsite.py`:
   `page_data`, `page_code`, the dictionary page's file sentence, and the
   crosswalk note. Grep for `GitHub`. The brief in `ktsitecopy.py` says the
   same, so a regeneration keeps it.
3. The site is still behind the gate (see 2026-09-21 below). Same steps to
   open it.

## WHAT CHANGED 2026-09-22

**Book One was rewritten**, all ten parts, by Codex working from
`CODEX_REWRITE.md`: semicolons 3.84 -> 0.05 per 100 words, 37,186 -> 26,979
words. `ktverify.py` on the new text: 71.1% of content words in the gloss,
9.2% in the source shown, 19.7% in neither — and that "neither" is mostly
`saint` for the gloss's `holy`, `person` for `somebody`, and the editor's
own words (`attributed`, `unclear`). The front matter's 97.9% figure was from
the old text and is now stated against the gloss, which is what it counts.
`ktverify.py risk` is the tool; the gloss is the referent, and the gloss is
itself a translation of the signs.

**224v got its seal back**: "within the seal [of this book]" — the gloss has
`seal` read at line 5 and the rewrite had dropped it. The one editorial cut
found by hand that was an accident, not a decision.

**The book links**: notes are gen's own footnotes (real EPUB3 noterefs; they
pop up in the house reader and in Apple Books/Kobo, with a Notes page at the
back), and every paragraph's gloss citation links to its folio in Book Two,
whose heading links back — 940 cross-file links, none unresolved. The shared
reader needed a fix for that: epub.js drops the fragment on a cross-file link
under the paginated continuous manager, so `reader.php` 1.9.14 resolves such
links itself (section.document -> element -> CFI). Notes-page return links
were broken the same way and are fixed by it.

**Front matter and the site intro redone**: how it came to the Academy (1838,
Batthyany's library from Rohonc/Rechnitz), how it dates itself (1,560 years
from the Ascension at 223v = 1593), that it was made with AI under an editor
and which model did what, and the two parts. Tagline: "Using AI to extend and
test the Kiraly and Tokai dictionary."

**The tests page**: the summary in TESTS.md is a pipe-separated table now,
rendered as four columns with one verdict per row — PASS, FAIL, NO VERDICT
(instrument failed on K&T's own words, or has no power), IN BAND (Test 3), and
two rows "reported, not a verdict". Test 7 stays FAIL on the declared bar;
Test 13 stays FAIL with "the rivals exist; the method did not choose them"
on the line; Test 12b is the re-glossers, their own row. The reviewers are
named as Gemini 2.5 Pro and Grok 4.7 in the sentence itself, everywhere.

**The orders are published**: `METHOD.md` whole and unedited at
`/rohonc/orders.html`, local paths redacted by a counted mark. Nothing on the
site is "sent on request" any more. `page_method` and `page_read` were each
defined twice in ktsite.py; the second definition won both times.

**The programs page** is a crosswalk, test -> program -> saved run, read out
of TESTS.md at build (`test_rows()`); no hand-kept list. **Notes**: the
Elijah-frame note (anchored on the retelling's own phrase, placed at 004v by
its source line) and the Carmel note corrected (189r, 195r; John preaches
there at 116v).

**The front page**: the sign strip no longer scrolls itself; drag, throw,
arrows, keys; a photographed brass glass (Seedream, `ktglass.py`, measured
hole) with a click and a flick per sign; 36px signs, 1.8x, 150px lens on a
wide sheet, smaller on a phone. The flash between pages was fam.js's arrival
veil, dark over a cream sheet; first render now waits for fam.js
(`rel=expect`) and the veil is dropped on arrival without a fade.

## TRAPS THAT COST TIME TODAY

- `python3 build.py | tail -1 && commit` commits on tail's exit status. Two
  commits went in with a crashed build. `set -o pipefail`, and verify the
  output before the commit — the same trap ktcommit.sh was written to close.
- A patch that slices "from def X to the next def" takes the module-level
  constant that sits between them with it (ORDERS_REDACT went that way).
- Writing a file and THEN parsing it leaves a broken file on disk. Parse
  first.
- An inline `style=` beats every media query; the glass sizes had to move
  into the stylesheet before a phone could override them.
- "It works" measured inside a paginated iframe is not "it is on screen":
  the iframe is wider than the window. Measure against `window`.
- `ktcommit.sh` runs `git add -A`, so while another agent (Codex) has the
  tree, every commit sweeps its half-written work in under your message.

What follows is the record as it stood the day before.

# Where this stopped — 2026-09-21 (earlier)

## THE PUBLIC SITE IS OFF THE AIR UNTIL THE BOOK IS DONE

oona13.com/rohonc/ is behind the magic-link gate as of 2026-09-21. Signed in,
it works exactly as before. Signed out, every path under /rohonc goes to the
oona13 home page — not to the sign-in page, because a login screen on a path
meant to be dark still tells a stranger something is there. Nothing was
deleted; all 13 pages and 4.2M of data are on disk at /var/www/oona13/rohonc.

Every redirect in that block is **302, not 301**, on purpose: this is going
back up, and a permanent redirect is cached by browsers and by Google and is
painful to undo. The bare-path redirect used to be `permanent` and was changed.

**To go live, when the book is done:** in the `@o13rohonc` block of
/etc/caddy/Caddyfile delete the `forward_auth` block and the `no-store`
header, put `redir @rhbare /rohonc/ permanent` back, then
`sudo caddy validate --config /etc/caddy/Caddyfile` and
`sudo systemctl restart caddy` — **restart, not reload**, because the admin
endpoint is off. The public version of the block is kept whole at
/etc/caddy/Caddyfile.pre-rohonc-offline-20260921.

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
