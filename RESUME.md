# Where this stopped — 2026-09-23

## NOTES, SOURCES, KINDLE — 2026-09-23

The owner asked how sure the readings on the Lucifer pages are, and then for
precedents. What was done, all committed through ktcommit.sh and pushed:

- **Five endnotes added or corrected** in `work/rohonc/translation/notes.md`
  (54 now): the mother born at 004r:11 (K&T's own example for both signs); the
  cup on 004r (their sign, "cup or jar", four times there and three elsewhere;
  nearest precedents the Romanian carol of Judas plundering paradise and the
  Slavonic Michael-and-Satanael tale; the Grail-from-Lucifer's-crown story is
  1832, not medieval); the Elijah frame (no longer "no source found": Slavonic
  Enoch, the Apocalypse of Elijah, and Kalmany's Szeged folk tellings); the
  Marian test behind 002r (Scotus, Suarez 1590s; Agreda 1670 too late); Seth's
  branch at 006r (K&T themselves unsure between branch, seed, fruit and oil;
  Golden Legend and the Erdy codex promise the healing; nothing performs it).
- **One reading corrected in Book One.** 006r said Adam was healed by "the
  seed and the anointing light". K&T's apparatus lists those signs as a
  variant of their expression "immediately", four times on the folio. It now
  reads "when Seth brought the branch, at once Adam's eyes were opened". The
  note says the earlier printing was wrong.
- **DATA_PROVENANCE.md section 6**: the ten texts the notes read online but
  did not fetch, each with what it supplied, where, and its copyright position.
  The duplicated section number is fixed (the Hungarian dictionary is 7).
  `ktsite.py notes_sources()` renders it on the sources page; the site copy
  key is `sources_notes_lead`. Kalmany and Balint are in the citations owed,
  with a sixth gloss in `ktsite_copy.json` (glosses pair by POSITION; the
  first rebuild paired the new citation with the page-scans gloss).
- **The Kindle edition is live, $0.99, https://www.amazon.com/dp/B0HKQCWV2S**
  and is linked from the front page, the read page, the reader's toolbar
  (`/var/www/oona13/read/rohonc.php`, `kindle` key; backup `.pre-kindle-20260923`)
  and the README's first line. Plain text "Read on Kindle", no logo.

- **Download bug fixed (site).** Pressing Download EPUB killed every other button:
  fam.js set its `navigating` flag and waited for a page that never came. Watchdog
  added in `oona13/public/fam/fam.js` (backup `.pre-dlwatchdog-20260923`), the
  site's EPUB anchors carry `download`, include bumped to `fam.js?v=20260923`,
  Cloudflare purged. Gate `harness/ktdownloadgate.js` (needs live site + Playwright
  from character-playground/node_modules): FAILED before, PASSES after, also with
  `STRIP=1`. Written up in `oona13/OONA13.md`.

**Open:** the Kindle file on Amazon is the 03:40 build of 2026-09-23 and is
now BEHIND the shelf by five notes and the 006r correction. Re-upload from
the shelf when the notes settle. The paperback and Zenodo items below still
stand.

# Where this stopped — 2026-09-22

## HANDOFF, evening 2026-09-22 — Cover Maker, picked up by Opus

The book, site, repo and DOI are all published and consistent (see below). The
evening went on the COVER, in `/opt/covers-app`. State:

**Done and live**
- The ebook cover was CROPPED: `compose_wrap.py` scaled the front to cover
  1600x2560 and cut 3.1% off each side, taking the woodcut's right border and
  the end of "STEPHEN TAYLOR". Fixed with `ebook_from_front()` (scale to FIT,
  pad top/bottom in paper colour sampled from the front's edges). The rebuilt
  file is `data/users/u1/out/20260921-212932-2sdz/the-rohonc-codex-ebook-cover-1600x2560.jpg`
  and was emailed to the owner. The wrap (553pp) was never wrong.
- Server: `web/galleryapi.py` `_keep_geometry()` — a save can no longer null
  trim/paper/printer/pages. Both write paths use it.
- Client: `static/studio.js` restoreState() now applies the cover's own saved
  design OVER the localStorage blob (`covers_form_v1`), only where the design
  holds a value. Backups: `.pre-designwins-20260922` (original),
  `.broke-preview-20260922` (the over-broad first fix that blanked the form),
  `.fixed-20260922` (current).
- Design `20260921-212932-2sdz`: pages 553, trim 6x9, cream, badge off,
  tagline removed, new back blurb ("branch from the tree of mercy").
- Stale wraps (591pp, 633pp) deleted from the out folder; only 553pp remains.
- Kindle price decided: $0.99. No paperback yet.

**Open — do these next**
1. `scripts/shellgate.js` has a new `[preview]` check that is VACUOUS: it
   passed against the broken script too, because it CLICKS the cover and a
   click applies the saved design regardless. The failure was at page LOAD.
   Rewrite it to seed the stale blob, have the cover already selected at load
   (find how `pick()` / the gallery auto-selects — grep `pick(` call sites),
   reload, NOT click, then assert the stage draws and the form carries the
   design, not the blob. Prove it with the mutation: swap in
   `studio.js.broke-preview-20260922`, restart, expect `[preview] FAIL`,
   restore `.fixed-20260922`, restart. Do not ship a gate that stays green
   through the bug it was written for.
2. `[v1-layout]` FAILS: 4 of 402 elements moved. The gate now prints their ids
   (patch added this evening). Find whether the applyConfig-at-load change
   moved them before touching the baseline; never rebaseline blind.
3. Offered, not decided: texture the ebook cover's 80px padding bands with
   cloned paper grain instead of a flat fill.

Owner's note on tone: the previous session kept insisting the cover was right
while he held a cut-off file, and told him to hard-reload when localStorage
restore made that useless. LOOK AT THE EXACT FILE HE DOWNLOADED FIRST.


## THE SYNC MESS, FIXED — 2026-09-22

**One command now pushes everything: `harness/ktpush.sh`.** It regenerates what
the readings produce, runs every gate, then builds the shelf book, its EPUB,
the web reader's copy, the print PDF and the public site, in dependency order,
nothing piped. `--check` stops before pushing. The gate list is
`harness/gates.txt` and `ktcommit.sh` reads the same file, so the two cannot
drift. All six gates pass and everything above was pushed from one run.

**Edits made in Book Maker are no longer destroyed.** `ktbook.py --shelf`
writes `.kt_stamp.json` beside `book.json` recording what it left. If the shelf
no longer matches, the build stops, names the edited chapters and exits 3.
`--overwrite-shelf-edits` discards them deliberately. Tested both ways on a
copy of the shelf, never the real one.

**The draft is archived.** `retelling.md` stopped being Book One when Codex
rewrote it, and two checkers went on reading it for a day: ktretellcheck
measured its 1,142 quotations and reported the strictest-looking pass in the
project while the printed book was checked by nothing, and ktnotecheck proved
all 50 endnote anchors stood in it, which is true and beside the point, since
not one of them is in the printed text and ktbook has always placed those notes
by folio. Both now read `reading.md`. ktnotecheck checks what actually decides
placement: the folio on the note's source line, against the folios Book One
cites. ktbook no longer falls back to the draft -- a missing Book One is a
failure, not something to substitute for. See `archive/drafts-20260922/`.

**195 backup files archived** to `archive/backups-20260922/`, 179 with their
git history. Nothing reads them. The rule is in `archive/README.md`: back up
before editing, then move it there once committed, because a tree with 179 dead
files in it is a tree where nobody can see which file is live.

**Defects the repointed gate found in the printed book, all fixed:**

- Three part headings sat below paragraphs belonging to the next part. The
  opening of the Cross story was printed inside the Preaching chapter.
- `PARTS` said IX began at 215r and X at 221r while the prose divided at 215v
  and 223v, so three paragraphs of Acts were printed under The Last Things.
  PARTS and the declared ranges in reading.md now match the book.
- The front matter stated "97.9% of them are the gloss's own". The rewrite made
  it 71.1/9.2/19.7. `front_matter()` now calls `ktverify.accounting()`.

**Two things I got wrong and corrected**, both worth keeping: 31 quotations
were reported as broken in the printed book when they were in the archived
draft; and 11 folios were reported as never cited, which was a citation parser
that read only the endpoints of "(055r-056v)". All 441 are cited.
`ktbook.cited_folios()` is now the one reader for that.

**Still open, and the author's call:** the printed Book One carries no
guillemet quotations at all, so the quotation check weighs nothing. It says so
out loud every run rather than passing in silence. Whether Book One should
quote the manuscript is an editorial decision.

## VERIFICATION BEFORE PUBLISHING — 2026-09-22

The owner asked whether the signs or the sources could be wrong, and whether we
could verify as much as possible first. What was done:

**THE BIG ONE: the transcription now has an outside witness (Test 16,
`harness/ktopen.py`).** Every other test reads Kiraly and Tokai's own
transcription, so none of them could see an error in it. The 2014 anonymous
open transcription (`data/rohonc/latest.txt`) is the only independent one that
exists: different person, its own glyph alphabet, no word separation, spread
numbering, published years before K&T. Parse it as `<spread>: <L|R><row>:` --
BOTH sides, 4,188 rows, not the 2,114 you get if you only match `R`. Row-length
profiles alone then say the left page of spread k is folio k recto and the
right page folio k-1 verso, which is how a RIGHT-TO-LEFT book falls open and is
stated by neither transcription. On the quarter of rows where both agree on the
shape (1,131 rows, 17,454 glyphs), one alphabet maps onto the other 91.1% of
the time; the same rows with the open row reversed give 14.3%, and the declared
control -- each open row paired with a random K&T row of the same length,
a map learned the same way, 20 times -- gives 12.9%, so 458.5 sigma. 83.8% of
the words this edition reads are identical in both. Both bars declared before
the control ran; the 91.1% had been seen exploratorily first and the test says
so. The other three quarters of rows are where the two split lines or read
damage differently: counted, never guessed at.

**Every deterministic test rerun and diffed** (14 programs). EIGHT did not match
their saved runs: Tests 1, 2, 2b, 5, 6, 7, 8, 9. Cause: proposals.json last
changed 09-21 17:10 (the variant-loader fix, 234 spellings newly seen) and
those runs were written 16:01-16:52. Seeds are pinned, so it was the input, not
randomness. Regenerated on the final readings; the old files are kept as
`*_v2_prevariantfix.txt`. Test 7's ten-shuffle control was itself unstable (sd
0.67 then 0.36); NSHUF raised to 100, declared in the docstring first, bar
unchanged: 10.3 sigma, PASS, and all three runs kept. TESTS.md has a section on
it before the Summary.

**New gate `harness/check_tests.py`**, in ktcommit.sh: every `NN sigma` / `NN%`
on an indented line of a test section, and on its Summary row, must appear
verbatim in that test's cited run file. 125 figures checked, bar zero. It
caught Test 12's re-glosser 84% for the file's 83.9%.

**Also checked:** the rendering reads K&T's own transcription (`rohonc_kt.py`),
not the open one; Book Two carries every main-block row of all 441 folios;
about 350 signs of K&T's `picture`, `header` and `block` rows are NOT rendered
and that is an honest gap to name. All 297 citing folios resolve to verses; 144
have retrieved sources only; none has nothing.

**Not rerun, on purpose:** the extension-attempt gates and null control that
ROHONC.md reports (`ktsegment`, `ktname`, `ktalign_gate*`, `ktextend_gates`,
`null_control`, `ktproof`, `ktsense*`, all 09-20). They are records of attempts
made on the readings of their day, and the document says so.

**Still not possible from here:** anything K&T's transcription itself gets
wrong in the same way the open one does, and a reading of the manuscript by
someone who does not depend on this project.

## THE COVER — DONE 2026-09-22 (Cover Maker design 20260921-212932-2sdz)

The baked "THE FIRST COMPLETE ENGLISH RENDERING" roundel is cloned out of the
raw art with paper from the same rows, tone-matched to the annulus round the
hole (`gen/20260921-212932-2sdz.png`; the untouched art is
`.png.pre-badge-20260922`). A red seal was tried in its place and taken off; a
line in the lower cream space was tried and taken off (that region is restored
from the backup, y 3990-4380). What the owner wanted, and what stands: "FIRST
TIME IN PRINT" SET INTO THE ART inside the woodcut's own empty box at its foot
-- the band between the two tower bases, x 720-2960, y 3488-3695 of the
3371x5056 art -- in the title bar's weight of lettering: Cinzel Black (the
variable Cinzel.ttf carries Regular/Bold/Black), fitted to 90% of the box's
width (size 152, cap 107px in a 207px box), ink (20,7,8) measured from the
cut. No badge keys remain in the design. Why not a native slot: every
front-text slot and the `text` badge draw a knock-out halo and load the
Regular weight; the cover's own lettering is heavy and halo-free.

Carried through: the composed front is the shelf book's `cover.jpg` (backup
`cover.jpg.pre-seal-20260922` is the roundel version), the EPUB carries the
same bytes, the reader's copy is republished, the 6x9 wrap renders with the
line on the front only, and `work/rohonc/book3d.png` is regenerated with the
studio's `book3d.snapshot` (rx -14, ry -34) and copied to the site by ktsite.
The KDP wrap is downloaded from the studio as before.

## PUBLISHED — 2026-09-22

**The repository is live and public: https://github.com/styopr613/rohonc-codex**
(the owner's account, the former `fluent613`, renamed. A copy went up under the
secondary account `SUP613` first and has been deleted; there is one place.)

What is in it: `harness/`, `work/rohonc/`, the root documents, `archive/`, and
`book/` with the EPUB and the cover. What is NOT: `data/` is gitignored, so
Kiraly and Tokai's dictionary and the manuscript scans are not published. A scan
of every tracked file found no credential, no personal email and no server
address; the two programs that need keys read them from `/opt/secrets` at run
time.

**oona13.com/rohonc/ is public again.** The magic-link `forward_auth` block is
out of the Caddyfile with its `no-store` header, and the bare-path redirect is
`permanent` again as it was before the gate. The gated config is kept at
`/etc/caddy/Caddyfile.pre-rohonc-live-20260922`. Caddy needs RESTART, not
reload, on this box. Signed out, the index, the tests page, the reader and the
EPUB all answer 200.

**Every "will be posted to GitHub" is now the real address** -- in the book's
front matter, the site introduction, the data page, the dictionary page and the
programs page. That promise had been unredeemable since it was written.

### Still to do

1. **Zenodo.** The DOI comes from Zenodo watching the repository, and enabling
   that needs the owner's own login: sign in at zenodo.org with GitHub, switch
   `rohonc-codex` on under Settings -> GitHub, and only THEN cut a release --
   Zenodo archives releases made after the switch, not before.
2. **The paperback.** KDP upload; the 6x9 print PDF is on the shelf at
   `/opt/publish-app/data/u1/books/20260921-052535-r0hc/print.pdf`, 553 pages,
   and is deliberately NOT served from the site. Skip KDP Select: digital
   exclusivity would disqualify the free EPUB. When it is live, put its link in
   the README's first line.
3. **The cover claim.** "FIRST TIME IN PRINT" is gone; the woodcut's foot now
   reads THE COMPLETE MANUSCRIPT IN ENGLISH. Jason Edward Lee's "The Rohonc
   Codex: A Working Solution" (Lulu, 2019, 620pp) is a prior printed English
   claim, unreviewed anywhere and absent from Wikipedia's list of attempts, and
   a 2011 joke edition exists whose text is The Wind in the Willows.

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

Run `cd harness && ./ktpush.sh --check` after any change to the readings. (`whatbroke.py` did this job until 2026-09-22; it counted quotations, and the printed Book One has none. See `archive/tools-20260922/`.)
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

    cd harness && ./ktpush.sh --check

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
