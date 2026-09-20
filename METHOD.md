# METHOD — reading the unread Rohonc signs, Király & Tokai's way

This is the one method in seventeen that has produced words. It is not
statistical. It is the method K&T built their dictionary with: guess a sign
from one passage where the story is known, then carry the guess to every
other place the sign occurs and keep it only if it survives all of them.

Everything below is for whoever executes it next. Read it all before
starting.

## What exists

- `harness/proposals.json` — the readings made so far, with tier, count and
  evidence. **This is the output.** Add to it. Never edit K&T's dictionary.
- `harness/ktcontext.py` — the tool. No arguments: lists the 163 unread
  signs with 3+ occurrences that sit in a translated passage, commonest
  first. With hex codes as arguments: prints every occurrence of those
  signs, rendered, with `<<...>>` around the target. A `*` marks a line on a
  translated folio.
- `harness/kttranslate.py` — renders the book three ways. The third file,
  `work/rohonc/translation/rohonc_reading_plus.txt`, applies tiers A and B
  from `proposals.json`, marked `+word` so nothing of ours can be mistaken
  for theirs. Rerun it after every change to `proposals.json`.
- `work/rohonc/translation/rohonc_translation.md` — the translation so far,
  61 folios. Resume at 036r in page order. `harness/page.sh 036r 036v ...`
  prints a page's full gloss.

## The loop, per sign

1. `python3 harness/ktcontext.py` — pick the next sign from the top of the
   list that is not yet in `proposals.json`.
2. `python3 harness/ktcontext.py <hex>` — read EVERY occurrence. Not the
   first ten. Note: the tool renders with the shortest K&T sense, so *Satan*
   is their angel/Satan/Lucifer sign, *they* is Jews, *learn* is apostle,
   *peace* is commandment, *day* is year, *book* is write, *table* is
   throne, *boy* is son, *girl* is virgin, *rich* is holy.
3. Guess from the occurrences on translated pages, where the story is
   known. Then check the guess against every untranslated occurrence.
4. Assign a tier:
   - **A** — fits every occurrence, or is proved by an identical formula
     (the same sentence elsewhere with a K&T-defined word in that slot) or
     by a numeral that resolves against a known number.
   - **B** — fits most occurrences; the rest are unclear rather than
     contradicting.
   - **C** — a guess. Rendered nowhere; kept so it is not re-guessed.
   A single contradicting occurrence that is clear drops the tier. Do not
   argue it away.
5. Write the entry: gloss, tier, n, and evidence that names folio:line for
   each decisive occurrence, so anyone can check it with step 2.
6. After each batch of five or so: rerun `kttranslate.py`, reread a
   translated page in `rohonc_reading_plus.txt`, and make sure the new
   words read as sentences. If a `+word` makes a line worse, the reading is
   wrong.

## What to look for, because it is what has worked

- **Formula slots.** The book repeats formulas verbatim (the salvation
  formula, the prophecy, the Nativity). An unread sign in a slot that a
  K&T-defined word fills in another copy of the same formula IS that word.
  That is how *be saved* and *believe* were read. Tier A.
- **Numerals.** Strokes: one stroke `060` is one, two is K&T's *two*,
  three is three, five is five. Digits add; a `ten` after a group
  multiplies it. Ordinals are the list marker or `812` in front of a
  numeral. Any sign made of these resolves; check it against a number the
  story supplies (days, apostles, denarii, chapter numbers).
- **Composition.** A long sign that contains a shorter K&T sign or a read
  sign as a prefix or suffix. `630461796` contains `630461`, which is the
  cross; `569910` is *this* + the subject marker. Check the parts.
- **Named episodes.** A sign that occurs in the arrest, the denial, the
  crucifixion, and nowhere else, means what those scenes need. `rise`,
  `crucified`, `Nazareth`, `answered` came this way.
- **Grammar particles.** Single glyphs with hundreds of occurrences that
  K&T left undefined are grammatical. `910` is a subject marker. Say what
  a particle does, not what it means.

## What not to do

- Do not loosen a tier to make a number bigger. The count of `+word` in the
  book is not the goal; a page that reads is.
- Do not run a statistical gate on this. Seventeen have been run; the
  method that works is the one above. If a gate is wanted later it is:
  does the guess hold at every occurrence, and that is step 3.
- Do not touch `data/rohonc/kt/`. K&T's dictionary and transcription are
  theirs and are not edited.
- Do not spend more than a few minutes on a sign whose occurrences are all
  on untranslated pages. Translate the pages first; the sign gets easier.
- Signs that occur once are done last, from the fully-read lines around
  them, and stay tier C.

## Would finding the real source text help? Measured: barely

The obvious idea is to find the book the codex paraphrases and use it as
known plaintext. It was tested rather than assumed, by measuring recovery of
a hidden word on lines where the source passage is demonstrably present in
the corpus:

    the two near-verbatim parables, 135r and 119r    18.4%   5.2x control
    the gospel-close Passion folios, 029v-035v        7.6%   1.8x
    the Improperia and Longinus                       7.4%   2.1x
    the apocryphal opening, 004v-003v                 8.8%   1.8x

18.4% is the ceiling, and it is measured on the two pages where the source is
sitting right there and the wording is almost verbatim. Even with the correct
passage in hand, four hidden words in five are not recovered. The codex
paraphrases in a language that is not English, and Kiraly and Tokai's glosses
are English renderings, so stem matching loses most of it no matter how good
the source is.

So source research is not a way to read words in bulk. What it IS good for is
making a human guess better and faster: knowing exactly what a passage says
narrows what an unread sign in it can mean. Use it that way, as a reading aid
for a specific hard page, not as a substitute for the loop.

The content points at a late-medieval devotional compilation: the Life of
Adam and Eve, the Legend of the Rood, the Protevangelium, a Passion from
Matthew and John, the Improperia, and Longinus from the Golden Legend. The
closest known families are the Hungarian codices of the 1500s (Erdy,
Ersekujvari, Winkler, Nador, Debreceni, Weszpremi), Pseudo-Bonaventure's
Meditationes Vitae Christi, Ludolph of Saxony's Vita Christi, and the Bible
historiale tradition. Any of those would be a reading aid. None of them will
be a key.

## Order of work

1. The 163 multi-occurrence signs on translated pages, commonest first.
   Twenty are done. The next are `285`, `084`, `6a6`, `520ae0850270ae0`,
   then down the list.
2. Translate in page order from 036r, appending to the translation file in
   the established format. Every batch of six to eight folios, commit, then
   go back to step 1, because new pages make new signs readable.
3. `harness/ktverse.py` ranks lines by how well they match the reference
   corpus; its top lines point at pages worth translating out of order
   (it found the Unmerciful Servant and the Lost Sheep). Use it when page
   order gets slow.

**Where this ends.** Unread is 17.3% of the book. About 7% of the book is
signs that occur once, which need their surrounding line fully read first and
stay tier C. The other ~10% occurs three or more times and is reachable by
the loop, but only once the folio it sits on has been translated -- 163 such
signs are reachable today and the rest unlock as translation proceeds. So the
two halves of the work feed each other, and the realistic floor for unread
text is the hapax share, around 7%.

## After every change

    cd harness && python3 gate.py && python3 check_results.py && python3 check_rohonc.py

All three must say green. `check_rohonc.py` checks the folio count in the
translation file and the proposals block in `kttranslate.txt`; update those
checks when you extend either.

## Ground rules

Plain English to the user, short sentences, no tables in chat. No
subagents. Never `rm` a glob; backups `.pre`/`.post`. Credit K&T for the
dictionary, transcription and grammar; the readings in `proposals.json`
and the translation are ours and say so. Private for now.
