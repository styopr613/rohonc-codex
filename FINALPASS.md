# THE FINAL PASS — check the vocabulary before checking the guesses

Written 2026-09-21, after the first clean run of the blindfold test.

## Why this order, and it is not a preference

The book is rendered from the vocabulary. Every bracketed guess was made by
a reader looking at a line, and that line was printed using the readings
already entered. If a reading in the line is wrong, the guess beside it was
made against a corrupted sentence. So the vocabulary is checked first, and
the guesses are checked afterwards, against the corrected text.

Measured 2026-09-21 over all 4,372 lines, by the worst other reading
standing in a guess's own line:

    guesses in the book (occurrences)                975
      read against clean context only                493   50.6%
      standing beside ANOTHER guess                  373   38.3%
      standing beside a tier C reading                63    6.5%
      standing beside a tier D reading                46    4.7%

Half the guesses were made in a line where everything else is K&T's own
dictionary or a tier A/B reading. Those are as good as a guess gets here.
The other half were made in a line that already contained something
uncertain, and 373 of them were made next to another guess. A guess read
off a guess is the failure mode this pass exists to catch.

## What the blindfold test says the guesses are worth

Run 2026-09-21 by a session that had not read the dictionary. Seed
1789991853. Strict score 7 of 25, 28.0%, which falls in the declared 15-30%
band. The consequence for that band was declared before any run and has
already been applied: passage-read tier C became tier D.

The run also split the failure cleanly, and this is the useful part:

    true word was in the candidate list the tool built    7 of 9 right
    true word was not in the list                         2 of 16 right

The reader is not the weak part of the judgment step. The list is.

## What is wrong with the list, measured

`ktrecall.py`, written 2026-09-21, masks every one of K&T's entries one at a
time and asks where the true word was. Leave-one-out over 616 entries that
stand on a cited folio:

    true gloss in the list the pipeline builds today      32.5%
    tether-cut control                                    11.1%   7.9 sigma
    mean list length                                      96 words

    why the other 67.5% miss, first reason that explains it:
      TAKEN    21.3%   in the cited verses, but filtered out because
                       another sign already carries that English stem
      NARROW    8.0%   within three verses of the cite, not in it
      CHAPTER   6.7%   elsewhere in a cited chapter
      BIBLE    26.6%   somewhere in the KJV or Douay, not in these chapters
      OUTSIDE   5.0%   in neither Bible: apocrypha, sermon, function word

TAKEN is a bug, not a limit. K&T have many signs for one English word, so
striking a word out because some other sign already means it withholds the
right answer one time in five. That filter has to become a warning rather
than a deletion.

BIBLE at 26.6% is the honest ceiling on any Bible-pool method: the word is
in scripture but not in the chapters this folio cites. NARROW and CHAPTER,
together 14.7%, are reachable by widening the cite.

The bar for any change to the list builder was declared in `ktrecall.py`
before the fix was attempted, and it stands: raise the 32.5% by at least ten
points, with a mean list no more than twice as long, beating the tether-cut
control by 5 sigma over 20 shuffles. Presence bought with a longer list is
not an improvement. The reader pays for every extra word.

## The passes, in order

**1. Vocabulary.** 947 readings, tiers A to D, plus K&T's 841 entries which
are not ours to change.

   a. Every reading at every occurrence. `ktcontext.py HEX`. This is the
      project's one gate that has always worked. A reading that fails a
      clear occurrence comes out; it is not demoted.
   b. Blast radius before anything else. `ktresidue.py --audit`. A wrong
      piece under three glyphs feeds dozens of compound words, and two of
      those (`540` as *shall*, `570` as *ark*) have already had to be
      withdrawn. Read the words a piece feeds, not its own occurrences.
   c. The 211 tier C and 82 tier D readings. These were read from one
      passage with nothing internal to test them. They are where the
      vocabulary is thinnest and where a correction moves the most text.
   d. Wrong sense of a right entry. `ktsensefit.py` found 1,628 words
      printing a sense K&T publish but the folio's passage does not use,
      and corrected 755 on 222 folios. The rest are still standing.
      This outnumbered the dark words five to one and it will again.

**2. Then the guesses.** 839 signs, 975 occurrences, rendered `[word]`.

   a. Start with the 373 that stand beside another guess. Wrong context.
   b. Then the 109 beside a tier C or D reading, after pass 1 has settled
      those.
   c. The 493 read against clean context are the last and the least
      likely to move.
   d. The mechanical sweep that needs no source text: a restoration that
      repeats a content word already standing within three places of it in
      the line is telling you the slot is taken. Run once already, 46 hits
      on 43 signs, 40 corrected. Rerun it after any vocabulary change,
      because the words standing in the line will have changed.

**3. Then rebuild**, and only then. `kttranslate.py`, `ktreader.py`,
`ktbook.py`, and the retelling gate.

## The rules that do not move for this pass

- A guess stays a guess and stays in the book. Every one of them is marked.
  Removing a guess to protect a percentage is not a correction; the
  brackets are the honesty, not the emptiness. The measured worth of a
  bracket is written in the reader's edition front matter and it stays
  accurate.
- Coverage falling is a valid result. It happened when *shall* and *ark*
  came out, 59.5% to 57.9%, and the book got truer.
- Do not widen a gate to make a pass succeed.
- Do not retype a figure. Every number above is either printed by a script
  named beside it or saved in `work/rohonc/`.

## Open, and not part of this pass

The blindfold result is not yet written into `ROHONC.md` or
`CONCLUSION.md`, and `check_rohonc.py` has no assertion for it. The old
invalid 48% run is still the one those documents describe.

One leak found in the test itself and not yet fixed: the blind sample
prints restored `°`-marked and `?`-marked words in the lines around a
masked sign, and on 006r that handed the answer *Paradise* to the reader
for free. `ktblind.py` should strip this project's own guesses from a
masked sign's context, or the test measures the project against itself.
Without that one hit the clean score is 6 of 24, 25%, which does not change
the band.

## THE KEY, VALIDATED — 2026-09-21

Backup first: `/home/ubuntu/backups/voynich.pre-finalpass-20260921-1258.tar.gz`,
116M, gzip verified, carrying the repository with its history, K&T's 455
dictionary files, the 229 scans and all of `work/`. `data/ref` and `refs/`
are excluded: both are gitignored third-party corpora and re-fetchable.
K&T's dictionary is NOT in git, so that tarball is the only copy of it
outside `data/rohonc/kt/`.

Then the validation. `ktkeycheck.py`, bars declared in its docstring before
the first run and not moved since. K&T cite folio and line for every example
in every entry, so the code an entry defines must stand at that folio, on
that line. Saved run: `work/rohonc/keycheck.txt`.

    headword citations                     2,045
      stands on the cited folio             89.2%
      control, folio shuffled                1.9%
      415 sigma, bar 5                       PASS
      on the EXACT cited line, of those      97.5%

**The key holds.** Nine times in ten K&T's own citation lands, and when it
lands it lands on the exact line they name 97.5% of the time. Against a
shuffled control of 1.9%. Our parse of their dictionary agrees with the
manuscript, and that is the foundation everything else stands on.

The other origins are reported separately and only HEAD is the key's own
claim: VAR 79.5%, UNCERTAIN (their own "?" and "??") 59.1%, EXPR 23.7%.
EXPR is low by construction, not by fault — an expression is a phrase the
book writes as several tokens.

### Three faults in the checker, all mine, all found before reporting

This script reported the dictionary as broken three times before it was
right, and each number went into the docstring as a correction rather than
being quietly replaced.

1. **One entry, several codes.** Only 144 of the first 400 entries carry a
   single code. After `expr.` or `var.` comes a different code and the
   folios following belong to it. Attributing them all to the headword
   reported 45.3% of citations missing.
2. **Cross-references are not examples.** `see`, `but see`, `cp.` and `cf.`
   point at another entry. Those folios are not claims that the code stands
   there.
3. **Whole-token matching, which cost the most.** The manuscript writes
   K&T's words with affixes attached and the renderer has always known it.
   Matching whole tokens reported 22.4% of headwords missing; matching
   whole-glyph constituents reports 10.8%.

Fault 3 nearly became a false discovery. The residue looked like a
systematic prefix nobody had handled — `630` *on/at/to* 74 times, `871`
*holy* 31 times, `521` the case markers 13 times, sitting on words K&T had
already read (wedding, James, Caiaphas, candlestick). `871` is the very
prefix DARK.md records as a six-year miss, which made it more believable,
not less. Measured against our own definition of "readable" it looked like
977 unread tokens on 884 lines.

Put to the actual renderer, it was nothing: of 1,372 tokens carrying those
three prefixes over a readable word, the renderer already reads 1,337.
Thirty-five are genuinely unread, on 34 lines. The rule that caught it is
METHOD.md's: if a tool disagrees with the page, fix the tool before reading
anything off it.

### What is left to read by hand

    220 headword citations on 117 codes still miss their folio.

That is the list the vocabulary pass starts from, and it is small enough to
read one by one. Each is our parse, a spelling the transcription writes
differently, or a slip of theirs — and the first two kinds are readings we
do not currently have.

---

## The guess pass, 2026-09-21

Every one of the 848 bracketed guesses read by hand, one at a time, in order
of how many times the sign occurs. What follows is what the pass produced.

### First, the cheap whole-corpus checks, run before any reading

Four questions asked of all 848 at once, because the lesson of the last pass
was that the cheap check belongs first, not last.

    ktcited.py     does K&T's dictionary cite the line this guess sits on,
                   and does that entry print the guess's own glyphs?
                   426 sit on a cited line; 26 of those also print the glyphs.
    ktprinted.py   does K&T print this exact code anywhere at all, even
                   citing a different folio?                           17
    ktsubst.py     is this code a spelling K&T license by a substitution
                   RULE rather than by a list?                         52
    ktgsplit.py    does the code split entirely into codes already read?  0

The last is zero and that is a good sign: anything that splits cleanly is
already read by the segmenter, so no guess was standing where composition
could have answered it.

### What K&T's own apparatus settled

Nineteen guesses were answered out of their dictionary, plus one more found
through the same entry. Wrong and now right:

    6305201d9  'wrote'        -> on the tree     |
    0d2233     'the world'    -> tree            | one entry, the Holy Rood
    2da520     'withdrawn'    -> tree            |
    153, 345   'walked','saw' -> high            | their 'the high heavens'
    060a75     'one day at'   -> morning         | their morning-evening-noon
    5e4        'equal'        -> finger
    ae1b13     'again'        -> doomsday
    a10001005270001a10060  "my Father's house" -> him   | their 'I in him'
    5409c81f6  'grapes'       -> do not pick
    520ac3ae01f2 'sat at meat'-> company         | their 'table company'
    520524950  'outer darkness' -> darkness
    5209aa520060 'shepherd'   -> will            | their 'good will'
    5fc670ae0  'sinners'      -> then
    6709c7670  'root'         -> outgrow
    520060540152[45]40231 'and keep' -> not commit
    588        'hid'          -> up
    520b42 + a51  'shall perish' + 'but' -> two halves of their one word 'but'

Right all along, and promoted out of the brackets because the reading turns
out to be theirs and not ours: 481 'stood', a10354 'lifted up', 520060007
'part', 520151670 'dragon', 520252520670 'profit'.

The rule used throughout: an unqualified K&T reading promotes to tier A; a
reading they mark ? or ?? stays bracketed, because their doubt is doubt.

### The substitution rules, and the five readings they overturned

Some K&T entries do not list variant spellings one by one. They state a rule:
the entry for PRAY opens "var. 670 ~ 520, 540; ae0 ~ 060, ø". Our loader could
only read listed codes, so every spelling covered by a rule and by no list
went unread. `ktvariant.by_rule()` now expands them: 44 types, 238 tokens, all
of it theirs. Book coverage 77.6% -> 79.5%; lines fully read from their
dictionary alone 23.8% -> 25.4%.

Five readings entered here were words those rules already cover, and all five
were wrong. They are withdrawn and the lines now read from the dictionary:

    520ae0850270ae0     34x  'afterward'       -> their DO
    670b06              17x  'coming'          -> their BE BORN
    681ae0520250         7x  'inscription'     -> their EMPEROR
    520ae0520ae0a101f6   7x  'shall be called' -> their BODY
    5400609a2670a41      1x  'barley loaves'   -> their LITTLE

Twenty other readings entered here independently agreed with the rule-covered
spelling. That is the more useful half of the result: where the dictionary and
this project met on the same word, they agreed twenty times out of twenty-five.

The same rules corrected two readings of ours that were not withdrawn but
wrong in a different way: 00b670ae0520ae0 and 00b520ae0520ae0, twenty
occurrences between them, had been read 'as' and are K&T's PRAY -- and they
cite three of those very lines themselves, under their sense '? read', for
Luke 10:26, "how readest thou?".

### A gate that was moving

BAR A and BAR B in `ktvariant.py` were computed over Python sets, so the
random stand-ins were drawn in a different order on every run. Bar B moved
between 53.1% and 61.2% on the same data, which crosses its own bar: it was
reporting FAIL by luck. The case lists are now sorted and the numbers
reproduce exactly. The verdict does not change -- A 56.5% vs 39.4%, 1.8 sigma;
B 57.1% vs 33.9%, 4.8 sigma, both fail -- and ROHONC.md says in place that the
figures it used to print were one draw from a number that would not hold
still.

### Read one at a time: what the hand pass changed

Beyond the dictionary work, the reading of all 848 in their own lines changed
these, each for a reason written into its own entry:

    3a1     'into heaven' -> one another   (in two of three places the word
                                            before it is K&T's 'among')
    216     'he ascended' -> among         (the creed its evidence cited is
                                            on lines 4-5 of that folio, and
                                            this sign is on line 1)
    b52011  'healeth'     -> until         (194v runs from the creation of
                                            the world until the birth)
    0607a3  'condemned'   -> baptized      (the sign one line above is this
                                            one plus K&T's 'be')
    270990  'whatsoever'  -> must          (K&T's 'whatever' is already on
                                            the line, three words later)
    5202e5  'a physician' -> answered      (to agree with the same sign under
                                            a second verbal prefix)
    060060443670 'the kingdom' -> heaven
    681ae0540ae0 'and'    -> emperor       (Chosroes' son, and 681-ae0-540 is
                                            the front of K&T's emperor)
    8e4  'render to Caesar' -> render      (their emperor already on the line)
    4a79b84b0 'sent saying' -> sent        (say already on both sides)
    52084e 'and ever'     -> and           (103v:9 is 'for ever AND for ever')

One more withdrawn: a904f00300a2ae0, whose evidence had said WITHDRAWN for a
day while the entry stayed live and kept printing 'a numeral' on the page --
and none of its glyphs is one of this book's number signs.

### What was read and left standing, with the doubt written down

Fourteen guesses read at one occurrence and not at another. Rather than patch
them, each entry now says which line fails and what that line actually wants:
010, 454022, 5200948f0094, 520990ae0, 520950969, 556, 5208a8, 64f, 73a, 805,
1f2, 5f0, 817, 8c15246909a2. Two numerals, 0600601f7060060460ae1 and 121121,
are recorded as unsupported by this book's own tally rule rather than guessed
again. And two claims inside the evidence itself were found false and
corrected: 5208a8's said K&T gloss the phrase at that line, and 537961's said
the sign holds a piece of K&T's 'die'. Neither was true.

### Where it stands

    readings (tiers A-D)      926      A 491   B 179   C 201   D 55
    bracketed guesses         847
    withdrawn                  14
    lines fully read         81.4%     98.8% including the guesses
    book coverage from K&T alone      79.5%

New standing tools, all of which run on demand and decide nothing:
`ktcited.py`, `ktprinted.py`, `ktsubst.py`, `ktgsplit.py`, `ktgroot.py`,
`ktguesspass.py`, `ktguessread.py`, `ktgbatch.py`, `ktline.py`, `ktparts.py`,
`ktraw.py`, `ktset.py`, `ktwithdraw.py`, and `ktharden.py --guesses`.

---

## Tests of whether the additions are true, 2026-09-21

Everything before this section was run by the process that made the
readings. These are the checks designed to break that.

### Test 1 — do the readings track their source where nobody looked?

`ktheldout.py`. Every reading names in its evidence the folio it was read
from. That folio is excluded. On every OTHER folio where the sign stands and
a passage is cited, the test asks whether a content word of the gloss is in
that passage. Control: the same signs on the same folios with the glosses
shuffled among readings of the same tier, 20 times. Ceiling: K&T's own 841
glosses measured the same way — true words that still miss, because a folio
cites one passage and carries a dozen lines. Bars declared before the run.

    K&T ceiling                    1704 / 6565      26.0%

    tier   signs  held-out   rate   shuffle   sigma   vs ceiling
    A+B      310       634   25.7%     6.0%    17.5      99%     PASS
    C+D       37       155   26.5%     9.3%     6.2     102%     PASS
    G          0         -      -        -       -        -      unreachable

The tier A/B readings land in the cited passage, on folios that played no
part in choosing them, at the same rate as the dictionary they extend. The
guesses cannot be tested this way at all: 742 of 848 occur once, and the
106 that occur more often name every occurrence in their evidence, so
nothing is held out. Saved run: `work/rohonc/ktheldout.txt`.

### Test 2 — does each sign behave like the part of speech its gloss says?

`ktpos.py`. Never looks at any passage. Trains a naive-Bayes classifier on
how K&T's own signs sit among other signs — the token before, the token
after, whether the sign takes their genitive prefix b60 or verbal prefix 520
or their subject marker 910 — with each sign labelled noun or verb from its
English gloss by a lexicon built out of the two Bibles. Bar 1, calibration:
leave-one-out on K&T's signs must reach 70% and 5 sigma above the majority
class, or the instrument cannot see parts of speech and stage 2 is not a
result.

    stage 1  K&T's signs   n=505   68.3%   majority 56.0%   5.6 sigma   FAIL

A near miss is a miss. The instrument is not sharp enough, so the stage 2
numbers (A+B 63.2% agreement against 51.7% shuffled, 7.6 sigma; C+D 1.3
sigma; G 2.2 sigma) are printed in the saved run and are NOT a result. The
direction is the expected one; the bar was not met and is not moved. Saved
run: `work/rohonc/ktpos.txt`.

### Test 3 — the blindfold, leak fixed, ready to hand over

`ktrederive.dump` used to render the context around a masked sign with this
project's own readings in it, marked ? and °. Fixed: the blind file now
shows K&T's dictionary only. A fresh sample is drawn with seed 1790006519 at
`work/rohonc/blindfold_1790006519.txt`. It must be read by a session or a
person who has not read the dictionary; the brief is `BLINDFOLD.md`. It
measures the accuracy of the procedure that produces guesses, on 25 words
whose answers K&T published, and its consequences are declared in
`ktrederive.py`.

### Test 4 — the illustrations, blocked

`ktscanmap.py`. The page images are the only evidence that played no part in
any reading, and the codex draws its scenes. The mapping from image to folio
failed its declared bar three ways (43.8% by line counts, correlation +0.20
by word counts) because line counts barely vary and the scan is 100 ppi.
Until the images can be tied to folios another way, the pictures cannot be
used.

### What no test reaches

The 742 guesses that occur once. Only Test 3 says anything about them, and
what it says is a hit rate for the procedure, not a verdict on any one.

### Test 2b — same question, hand labels, population fixed in advance

`ktpos2.py`, with labels in `ktpos_labels.json` written by hand before the
run. Population: signs with five or more occurrences. Bars declared: 70% and
5 sigma over the majority class on K&T's own signs; then A+B 5 sigma over a
label shuffle.

    stage 1  K&T's signs   n=197   85.3%   majority 70.1%   4.7 sigma   FAIL

Hand labels took the instrument from 68.3% to 85.3%, which confirms the label
noise was real. It fails anyway, on the sigma clause: with 197 signs and a
70% majority, five sigma needs 86.4%. A near miss is a miss and the bar is
not moved. Stage 2 is not a result, and would have failed on its own: A+B
76.8% against 60.7% shuffled on 56 signs, 3.1 sigma. The population that
can be labelled cleanly is too small for this test to reach five sigma
either way. Saved run: `work/rohonc/ktpos2.txt`.

### Tests 2 and 2b: the test is no good, not the readings

To say it plainly: both versions of the part-of-speech test failed their
own calibration on Király and Tokai's words, which nobody doubts. That is
an instrument that cannot reach its bar on the sample available, not a
verdict on anything in this project. The readings were never scored by it.

### Test 5 — external truth: sentences K&T translated whole

`ktsentence.py`. K&T's dictionary quotes 172 example sentences with their
own English and a folio cite. Those sentences contain signs they never
glossed on their own, and their translation says what each means, in their
words, before this project existed. Every reading whose evidence so much as
mentions K&T is excluded as circular (583 of them), which is why the sample
is small. Control: glosses shuffled among the tested signs, 20 times.
Ceiling: K&T's own headwords in the same sentences, measured the same way.

    K&T's own words in their sentences        223/419      53.2%

    tier   signs  pairs   rate   shuffle   sigma   vs K&T
    A+B       26     38  81.6%     7.9%     8.6    153%    PASS
    C+D        2      2  100%        -       -       -     two pairs: no test
    G          0      -

Our confirmed readings are echoed in their translations more often than
their own headwords are -- because ours are content words and many of
theirs are prefixes and particles a free translation swallows. The seven
misses are law, five, ghost, pierce, redeem, three, mount: numerals and
words a paraphrase drops. The C+D line is two pairs, both hits, and cannot
carry a sigma; the bar reads FAIL because two pairs cannot meet it, which
is the test's size, not the readings. Saved run: `work/rohonc/ktsentence.txt`.

### Test 6 — word order on held-out folios

`ktorder.py`. Test 1 asks whether a gloss is in the passage; a right word on
the wrong sign passes that. This asks whether the word lands in the right
PLACE: the longest common subsequence of content stems between each cited
folio rendered in order and its passage in order, with K&T alone, with our
A/B readings added, and with the same readings' glosses shuffled among the
signs. A reading is applied to a folio only if that folio is not named in
its evidence.

    cited folios 297     K&T-only match total 1340

    A+B, held out     670 signs   gain +73    shuffled +14.6 (sd 8.5)   6.9 sigma   PASS
    G, not held out   847 signs   gain +151   shuffled +11.2           descriptive only

The guesses' figure is not a test -- a guess was made looking at its line
and its passage, so its position was fitted -- and is printed only so the
number exists. Saved run: `work/rohonc/ktorder.txt`.

### Where the additions stand after the tests

    Test 1  source presence, held-out folios        A+B 17.5 sigma, 99% of K&T    PASS
    Test 5  K&T's own sentence translations         A+B  8.6 sigma, 153% of K&T   PASS
    Test 6  word order, held-out folios             A+B  6.9 sigma                PASS
    Test 2  part of speech                          instrument failed calibration
    Test 3  blindfold                               drawn, needs a blind reader
    Test 4  illustrations                           blocked on the image mapping

Three independent tests, three passes, for the 670 tier A/B readings. Tier
C/D is too thin for two of them and passes the third. The 848 guesses are
reached by none of them and will not be until Test 3 is run.

### The blindfold, run clean, 2026-09-21

A fresh session that had never seen this project read 25 hidden K&T
entries from the pipeline's evidence and committed before reveal. Strict
score 4 of 24, 16.7% (seed 1790006519). Same band as the invalid run's
clean subset, same consequence, reaffirmed: passage-read tier C is tier D;
072 moved. Full record in TESTS.md.

Applying it turned up a second fault in the variant loader: it read only
the first three fragments after K&T's 'var.' mark. declared_full() now
walks the whole bracket -- 234 types and 778 tokens of theirs reached by
the two loader fixes together -- and six more readings of ours fell to
words they had listed all along: 531ae0 'therefore' is their copula (54
occurrences), 540ae0850270ae0 'afterward' their DO, and aca, 7c1910,
a22a10, 630340ae0 their you, if, over-against and immediately. 5202da2da
'tree' was already right and is now theirs. 520b7b 'believe' is recorded
as a live disagreement -- they list it under 'ask (for)' with a note to
compare 'believe' -- and drops from A to B. Coverage from their dictionary
alone: 77.6% -> 81.3%.
