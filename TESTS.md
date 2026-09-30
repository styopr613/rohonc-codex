# TESTS — whether this project's additions to the dictionary are true

Written 2026-09-21. Every bar below was declared in the test's own docstring
before it ran, and none was moved. Saved runs are in `work/rohonc/`.
Replay every saved result, twice under different Python hash seeds, from the
repository root with `python3 harness/reproduce_tests.py`. The checker first
verifies the exact source inputs and never contacts an outside model API.

The question: Király and Tokai published a dictionary of 841 signs. This
project added 919 readings on top (tiers A–D) and 847 bracketed
restorations (tier G), which are counted as readings nowhere. Are the
additions true?

Every earlier check was run by the process that made the readings. These
were designed to break that. Test 16 comes first: it checks the transcription
they are all read from.

## Test 16 — a second, independent transcription

`harness/ktopen.py` · `work/rohonc/ktopen.txt`

**This one comes first because it is not a test of the readings. It is a test
of the page they are read from.** Every other test in this document reads
Király and Tokai's transcription. If that transcription were wrong, nothing
below would notice: they would all be wrong together and agree with each other
about it.

There is one outside witness. An anonymous author published an open
transcription of the codex in 2014, glyph by glyph, in an alphabet of their
own, with no word division, four years before Király and Tokai published.
Different person, different alphabet, different page numbering, same book. No
dictionary and no reading are involved: if both are honestly recording the
same physical marks, some bijection carries one alphabet onto the other, and
it has to hold across the whole manuscript.

**The pages line up on their own, and say the book reads right to left.** The
open transcription numbers SPREADS of the library scan and labels each row L
or R. Matching row-length profiles alone — no glyphs, no readings — puts the
left page of spread k at folio k recto and the right page at folio k-1 verso.
That is the order a right-to-left book falls open in, neither transcription
states it, and it drops out of nothing but arithmetic on how many marks are in
each row. Király and Tokai's finding that the script runs right to left is
corroborated here by two transcriptions that never mention it.

    the open transcription covers       417 of 441 sides
    rows comparable glyph for glyph     1131 of 4372   25.9%
    glyphs compared                     17454

    GATE A, the two alphabets
      best map, as transcribed          91.1%
      the same rows, open row reversed  14.3%
      control, rows paired at random    12.9%   (sd 0.17, 20 shuffles)
                                        458.5 sigma
      BAR: observed >= 60%, control <= 30%, >= 5 sigma   PASS

    GATE B, the words this edition reads
      words compared                    7356
      identical in both transcriptions  83.8%
      BAR: >= 80%                       PASS

**Which rows are compared, and why only a quarter.** The rule is mechanical,
is in `aligned()` in the script, and is applied to every row in the book: a row
is comparable when the two transcriptions put it on the same side of the same
leaf, agree on how many rows that side has, and agree on how many marks are in
that row. Nothing is chosen by hand and nothing is dropped for scoring badly —
the criterion never looks at a glyph. The three quarters that fail it are where
the two split a line differently, or where one reads damage the other does not,
and a row that fails is counted in the denominator and never guessed at.

**What the 83.8% is a fraction of.** 7,356 words: every word lying wholly
inside a comparable row, cut at Király and Tokai's own word boundaries, since
the open transcription has none. A word counts as identical only if every one
of its glyphs maps through.

**A mistake worth recording, because it is the same one twice.** The first pass
at this found 2,114 rows and a flat contradiction with the provenance file's
4,250. The open transcription labels rows `L` and `R` for the two pages of a
spread, and the parser matched only `R` — half the book, thrown away silently,
and the comparison it produced was noise. This is the glyph-versus-word unit
error of the early Rohonc figures wearing different clothes: **confirm what one
row of a file IS before measuring anything with it.** Learned twice now.

**What was already seen when the bars were written**: an
exploratory pass had reported the 91.1% and the reversed 14.3%, so the headline
is not a prediction. The bars were declared for the part that had not been run
— the matched control, each open row paired with a random row of the same
length from elsewhere in the book, a map learned the same way, twenty times —
and it came in at 12.9%, which is what picking each symbol's commonest partner
gets you when the pairing means nothing.

Within what can be compared, the text this edition reads is not one person's
reading of the page.

## Test 1 — source agreement after excluding named evidence folios

`harness/ktheldout.py` · `work/rohonc/ktheldout.txt`

Every reading has a free-form evidence note. Folios named in that note are
excluded. On every other folio where the sign stands and a chapter and verse
is cited, the diagnostic asks whether a word of the gloss is in that passage.
Control: the same signs on the same folios with the glosses shuffled among
readings of the same tier, twenty times. Ceiling: K&T's own glosses measured
the same way — true words that still miss, because a folio cites one passage
and carries a dozen lines.

This was originally called held out. It is not. The method required every
proposed fill to be checked at every occurrence before admission, and tiers
A/B were selected for surviving those checks. Folios not named in the prose
therefore still influenced selection. The shuffle does not replay that
selection process, so its sigma is a descriptive comparison, not an
independent generalisation test.

    K&T's own words                          1717 / 6602     26.0%

    tier   signs  excluded   rate   shuffle   sigma   vs K&T
    A+B      100       367  24.8%     7.6%     9.4      95%    reported
    C+D       29       124  34.7%    12.1%     6.4     133%    reported

The figures also correct a parser that recognized `033v` but not compact
references such as `033v05`, and therefore treated many named evidence folios
as if they were excluded. With the citations parsed correctly, the A/B rate
remains close to K&T's, but neither the old nor corrected result says what
happens where nobody looked.

## Test 5 — external truth: sentences K&T translated whole

`harness/ktsentence.py` · `work/rohonc/ktsentence.txt`

K&T's dictionary quotes 172 example sentences from the codex with their own
English and a folio cite. Those sentences contain signs they never glossed
on their own, so their translation says what each such sign means there, in
their words, before this project existed. Every reading whose evidence so
much as mentions them is excluded as circular — 611 of them. Control:
glosses shuffled among the tested signs, twenty times. Ceiling: K&T's own
headwords standing in the same sentences.

    K&T's own words echoed in their sentences    223 / 419    53.2%

    tier   signs  pairs   rate   shuffle   sigma   vs K&T
    A+B       22     33  84.8%     5.9%    13.9    159%    PASS
    C+D        0      0     —        —       —       —     none left to test

The confirmed readings are echoed in their translations more often than
their own headwords are: ours are content words, theirs include prefixes
and particles a free translation swallows. The five misses — five, three,
pierce, redeem, ghost — are numerals and words a paraphrase drops. On the
readings of 28 September there is no C+D pair left to score: the two that
were scored, both hits with no sigma, are now read as Király and Tokai's own
words or fall out as circular, and the C+D bar has nothing to rule on.

Revised later the same day, after the outside review (Test 12 below). The
margin over K&T's own headwords is not a comfort. Under a strict rule it is
still 26 points, and two outside readers given only K&T's words and their
translations reach our gloss seven times in ten. This test shows the
readings agree with K&T's translations. It cannot show they were not taken
from them.

## Test 6 — word order after excluding named evidence folios

`harness/ktorder.py` · `work/rohonc/ktorder.txt`

Test 1 asks whether a word is in the passage; a right word on the wrong
sign passes that. This asks whether it lands in the right place: the
longest common subsequence of content words, in order, between each cited
folio and its passage — K&T alone, K&T plus our A/B readings, and K&T plus
the same glosses shuffled among the signs. A reading is used on a folio only
if that folio is not named in its evidence. As in Test 1, these folios were
checked while choosing readings, so this is selection-conditioned and is
reported as a diagnostic rather than an independent test.

    cited folios 299      K&T-only match total 1356

    A+B, evidence-excluded   670 signs   gain +25    shuffled -34.3 (sd 10.4)   5.7 sigma   reported

## Test 2 and 2b — part of speech from context: the instrument is no good

`harness/ktpos.py`, `harness/ktpos2.py` · `work/rohonc/ktpos.txt`, `ktpos2.txt`

Never looks at any passage. Trains a classifier on how K&T's own signs sit
among other signs and asks whether a sign glossed as a noun keeps noun
company. Stage 1 calibrates on K&T's words, which nobody doubts; only if it
passes are our readings scored.

    2   lexicon labels, all signs       n=505   68.3%   needed 70%          FAIL
    2b  hand labels, 5+ occurrences     n=197   85.3%   4.7 sigma, needed 5  FAIL

Both fail on K&T's own words. That is an instrument that cannot reach its
bar on the sample available, not a verdict on anything here. The readings
were never scored by it. Verdict: NO VERDICT, not FAIL -- a test that cannot
score the known-good entries cannot condemn anything.

## Test 3 — the blindfold, run clean

`harness/ktblind.py` · `work/rohonc/blindfold_1790006519.txt` and `_score.txt` · `notes/BLINDFOLD.md`

Twenty-five of K&T's own entries hidden. A fresh session that had never
seen this project, the dictionary, or the conversation that built it read
them from the evidence the pipeline gives — the rendered lines, the folio's
chapter and verse, the passage's free words, the structural neighbours —
committed all 25 before anything was revealed, and did not score itself.
The context showed K&T's dictionary only; the leak that used to let this
project's own readings into it had been fixed that morning. Seed
1790006519.

    committed 24, blank 1
    strict hits (a content stem shared with K&T's gloss)   4 of 24   16.7%

    hits: sin, eye, fish, James
    near-misses by my own judgment, not counted: rod for their stick,
    husbandmen for their vineyard worker, sorrow for their painful,
    witness for their Stephen — about 7 of 24, 29%, on the lenient count

The declared bands, written before any run, put 15–30% at "the judgment
step adds little; passage-read tier C readings become tier D". That
consequence had already been applied once, on the 23.1% estimate from the
invalid run; the clean run lands in the same band and reaffirms it. The one
passage-read tier C reading entered since, 072, is now tier D.

What the number means: this is the accuracy of the procedure that produces
a bracketed guess from a single line and its passage, measured on words
whose answers are known — about one in six strict, one in three lenient.
It is the number to hold against every `°` on the page.

What the blind reader reported as giveaways, for tightening the test: a
structural neighbour glossed as a compound containing the hidden sign
('ill; sinful' for a sign containing sin) hands over the morpheme; the
masked hex codes of signs outside the sample still show and can be
triangulated; and the free-word list, cut at forty words alphabetically,
leaks by what it omits. None of these changed the strict score much — the
four hits were fish, James, sin and eye, three of them handed over by the
rendered neighbours — but they are on the record.

## Test 4 — the illustrations: blocked

`harness/ktscanmap.py`

The page images are the only evidence that played no part in any reading,
and the codex draws its scenes. Tying image to folio failed its declared
bar three ways (43.8% by line counts, correlation +0.20 by word counts):
line counts barely vary and the scan is 100 ppi. Until the images can be
mapped another way, the pictures cannot be used.

## Test 7 — take K&T's words away

`harness/ktrecover.py` · `work/rohonc/ktrecover.txt`

Two questions. First: hide every one of K&T's 841 glosses and render the
book from this project's readings alone. Does it still read?

    words read           3487 / 29997    11.6%
    lines touched        2425 /  4372    55.5%
    lines fully read        2 /  4372     0.0%

No. Our readings are an extension of their dictionary and read nothing
without it. That is what they were built to be, so the 11.9% is a fact
about the design and not a verdict. The verdict below is on the recovery
bar, which was declared at 5 sigma and reached 4.4: FAIL, and it stays FAIL.

Second: can ours give K&T's words back? Hide one of their signs, render its
line with our readings only, align the line to the cited passage in order,
and take as candidates the passage words that fall between the nearest
matched word before the hidden sign and the nearest after. Then reveal
their gloss. Control: our glosses shuffled among the signs. Ceiling: the
same method with the whole dictionary as anchors.

    617 K&T signs, 1395 occurrences, capped at three per sign

    anchors        presence   top-1   no anchor
    ours A+B          2.6%     0.4%      89.2%
    ours A-D          3.8%     0.5%      84.5%
    K&T + ours       10.8%     1.8%      39.7%
    shuffled          0.7%     0.1%   (sd 0.29, 100 shuffles)

    ours A-D vs shuffled   10.8 sigma   needed 5   PASS

The bar is met, and the history of this line has to be told, because the
verdict on it changed. The first run, on the readings as they stood before
the variant-loader fix of 21 September, gave 4.4 sigma against ten shuffles:
FAIL, and it was reported as one. Rerun on the final readings with the same
ten shuffles it gave 8.4. The presence figure had barely moved, 3.7% to
3.6%; what moved was the standard deviation of ten shuffles, 0.67 to 0.36.
Ten was too few to hold a control still, so the shuffle count was raised to
a hundred, declared in the script before it ran, with the bar left at 5. The
hundred-shuffle control gave 10.3 sigma, 10.9 on the readings of 28
September, and 10.8 on those of 29 September. All three runs are kept
(`ktrecover_v2_prevariantfix.txt`, `ktrecover_v3_tenshuffles.txt`,
`ktrecover.txt`). What the table also says: with our readings alone, nine
lines in ten have nothing that matches the passage, so there is nothing to
bracket the slot, and even with the whole dictionary as anchors the method
finds the word only one time in nine. The instrument is weak; ours alone
reach about a third of what the whole dictionary reaches by it, and beat a
shuffle of themselves by ten sigma.

## Test 8 — from a random 30% of the words, can the rest be got back?

`harness/ktbootstrap.py` · `work/rohonc/ktbootstrap.txt`

A random 30% of every readable sign, K&T's and ours together, kept; the
other 70% hidden. Two stages, both bars declared first.

    readable signs 1574   seed 472   hidden 862 on cited folios
    the seed covers 18.8% of the tokens on those folios

Stage 1, which passage is this folio: render each cited folio with the seed
words only and pick, from the 288 passages any folio note cites, the one
that contains most of what is rendered.

    seed words          6.0% of folios right
    seed shuffled       0.4%  (chance 0.3%)      37.6 sigma     PASS

Stage 2, fill the holes: bracket each hidden sign's slot in the passage
between the nearest seed word before and after it, fill the narrowest
windows first with the rarest candidate, make the fills anchors, go round
again.

    true passages        filled 27.3%   recovered  1.0%
    predicted passages   filled 51.2%   recovered  0.6%
    seed shuffled                       recovered  0.1%   15.3 sigma   PASS

Both bars pass and the absolute numbers are small. The seed carries real
signal — a shuffled seed identifies nothing and recovers nothing — but the
machine that does the filling is the weak part, as it was in Test 7: it
knows only "between these two words", and with the seed covering one token
in five, most lines give it nothing to stand between. The step that actually
grew the reading was a person reading the line against the passage, and no
machine here stands in for that person. What this test shows is that the
seed points the right way; how far it can be grown is Test 3's question.

## Test 9 — the hidden 70% validated against the random 30% seed

`harness/ktseedcheck.py` · `work/rohonc/ktseedcheck.txt`

The owner's correction to Test 8: we already hold readings for the hidden
70%; the seed should validate them. Keep a random 30% of every readable
sign, K&T's and ours together. For each hidden sign, on its lines, bracket
its slot in the cited passage between the nearest seed word before it and
the nearest after, and ask whether the gloss we already hold fits that
window. The seed never saw the hidden gloss and the hidden gloss never used
the seed. Five random splits so every sign is hidden in some; the hidden
glosses shuffled among the hidden signs as control, five times per split.
K&T's own hidden signs, scored against the same seed, are the ceiling.

    source    bracketed   fit    shuffle   sigma
    K&T's         1270   18.9%     3.3%    18.3
    ours A+B       620   23.5%     4.2%     8.9    PASS   125% of K&T's rate
    ours C+D       275   21.8%     3.9%     6.0

This is the two codes proving each other. A random third of the dictionary
— theirs and ours mixed — places the other two thirds, theirs and ours
alike, five to six times better than chance, and our readings fit the
slots the seed brackets at least as well as theirs do. Occurrences where the
line held no seed word at all are set aside, not counted either way.

## The outside review — 2026-09-21

Two models were asked, with the tests above in front of them, what a
sceptic would still demand (`work/rohonc/outside/gemini_tests.md`,
`grok_tests.md`). Both said the same thing: the passage each folio retells
was identified while translating with the full reading, so Tests 1, 6 and
9 score against a target we made; Test 5 is the only external anchor, and
beating K&T's own headwords on their own sentences is a warning, not a
comfort. Grok wrote ten tests with bars; the four that need no new data
were built and run that day, each bar copied verbatim into the script's
docstring before it ran. Two more instruments were declared along the way
when the first had no power. None of the bars was moved. The first run of
Tests 10, 10b and 13 had inflected auxiliaries (hath, goeth, wilt) in
every pool through a gap in the stop list; those runs are kept as
`*_v1_stopleak.txt` and the figures below are from the corrected rerun.

## Test 11 — can the passage map be recovered from K&T's words alone?

`harness/ktpassid.py` · `work/rohonc/ktpassid.txt`

Grok's second test, run first because the others hang on it. Every cited
folio is rendered with K&T's 841 glosses and listed variants only, nothing
of ours, and the bag of stems is scored by tf-idf cosine against every
chapter of the Douay Bible. Decoys fixed before scoring: for each folio,
the chapter not cited whose profile on the fifty commonest stems is closest
to the cited one, and a chunk of the Golden Legend of the same length.
Control: K&T's glosses shuffled among their signs once.

    candidates                              1334 chapters
    folios with a cited chapter              300

                                        K&T as published    shuffled
    cited chapter is top-1 of 1334          38   12.7%        4    1.3%
    cited chapter in the top 5%            213   71.0%       35   11.7%
    median rank of the cited chapter        25               415
    beats the frequency-matched decoy      243/300           167/300
                                          p = 8e-29          p = 0.03
    beats the other-genre decoy            285/300           187/300

    BAR: median rank in the top 5% and p < 0.01 against the matched decoy   PASS

The map stands without our readings: from K&T's words alone the cited
chapter is the single best of 1334 one folio in eight and in the top 67 for
seven folios in ten, against one in eighty and one in nine from the
same words on the wrong signs. Tests 1, 6 and 9 have a target that does
not depend on the readings they test.

## Test 10, 10b, 10c — the search replayed on null books

`harness/ktnullreplay.py`, `ktnullreplay2.py`, `ktnullreplay3.py` ·
`work/rohonc/ktnullreplay.txt`, `ktnullreplay2.txt`, `ktnullreplay3.txt`

Grok's first test. Shuffling glosses after the readings were chosen does
not model the search that chose them. Write the keep-rule as an algorithm,
run it on the real book and on two null books — tokens permuted across the
whole book, and every cited folio handed the passage of the folio
seventeen places on — and see whether the nulls yield readings too. Fail if
a null keeps half as many as the real book, or if a null's readings beat
their own shuffle by 5 sigma held-out.

The search was human and unlogged, so Grok's mechanical proxy stood in:
keep a sign if some free stem is in the cited passage at every one of its
occurrences. It was run at three scales.

    scale                          real kept   global   rotated   held-out sigma, real / nulls
    10   the verse the note cites      7          1        4        9.3 / -0.9, -0.6     FAIL
    10b  the whole cited chapter     217        345      296       -2.1 / -2.3, -3.9      FAIL
    10c  the line and the verse
         its K&T words point to        2          0        0        8.7 /  0.0, -0.4      PASS

At verse scale the rule keeps 7 signs of 317; at chapter scale it keeps
everything on every book and never once picks the stem this project
picked (0 of 73 shared signs); at line scale, the closest to what the loop
actually did, it keeps 2. Seven against four and two against nought cannot
tell a search from a decipherment either way. What the held-out column does
say is consistent: on the real book the rule's readings land where they
were not derived from, 8 to 9 sigma over shuffle, and on the null books they do
not. The count criterion has no power at any scale, because "in the
passage at every occurrence" is not the rule that produced the 670
readings — a word is checked for sense at every occurrence, not for
presence in a verse. The test that would settle Grok's point is the human
loop run on a rotated book by a reader who does not know it is rotated.
That has not been done.

## Test 12 and 12b — Test 5 rescored under a strict rule, then two outside re-glossers

`harness/ktstrict.py` · `work/rohonc/ktstrict.txt`,
`ktstrict_reglosser_gemini.txt`, `ktstrict_reglosser_grok.txt`,
`work/rohonc/outside/reglosser_*.json`

Grok's fourth test. First sense only, every content word of it present in
K&T's English as the lemma itself — irregular forms mapped, one regular
inflection allowed, no synonyms, no stemmer. K&T's own headwords scored the
same way, restricted like ours to first senses with a content word.

    K&T's own headwords, strict             167 / 329    50.8%

    tier   signs  pairs  strict   shuffle   sigma   loose (Test 5's rule)
    A+B       22     33   78.8%     4.8%    13.4    84.8%

    strict >= 40%                                  ok
    >= 3 sigma                                     ok
    ours minus K&T's headwords  +28.0 points       FAIL   (bar: at most +10)

    matched on gloss length and sign frequency: K&T 54.2%, ours +24.6 points

Then the independent re-glosser. The 38 sentences were sent to two outside
models with each sentence in K&T's words only, the sign in question
blanked, and K&T's English — our glosses not in the file — and each was
asked what the blank must mean. Their answers are scored against that sheet
of 38, kept as `work/rohonc/outside/reglosser_key.json`, not against the
pairs today's readings give (the strict table above now has 33).

    reader             agree with ours   undetermined   agree among the determined
    Gemini 2.5 Pro        26 / 38  68.4%      7             83.9%
    Grok 4.7              27 / 38  71.1%      3             77.1%

    BAR: agreement >= 30%   PASS

Leakage check, same signs on cited folios that are neither in their
evidence nor the folio of a K&T sentence, Test 1's measure:

    7 signs   52 occurrences   17.3%   shuffle 14.0%   0.5 sigma   no verdict

Read together: the glosses are the words K&T's translations imply, an
outside reader recovers them from the sentence seven times in ten, and on
other folios they cannot be told from shuffled glosses. Test 5 is
consistent with the readings being true and equally consistent with their
having been read off the sentences. It stays in the table as agreement
with K&T, not as independent confirmation.

## Test 13 — the underdetermination census

`harness/ktcensus.py` · `work/rohonc/ktcensus.txt`

Grok's sixth test. For every tier A/B reading whose sign stands on folios
citing three or more distinct chapters: list every free stem present in
all of those chapters. A rival is one that is not a form of the chosen
gloss. Fail if more than 40% of the signs have a rival that also satisfies
the keep-rule.

    A/B signs counted                     95
    chosen gloss in every chapter          0     0.0%
    a rival in every chapter              62    65.3%     FAIL   (bar: 40%)
    a matched-frequency random stem
      in every chapter                           0.3%

    at the verse the note cites (reported): 71 signs, chosen survives 1, rivals 3

The bar fails as declared. In plain terms: the 95 are this project's tier
A/B readings whose signs stand on folios citing three or more chapters; the
rule asks whether some other word appears in every one of those chapters;
for 62 of the 95 a common verb does. The 65.3% measures how often a common
verb turns up in three chapters, not how often a reading is arbitrary. The
rivals exist; the method did not choose them -- not one of the 95 glosses is
the product of that rule -- so the FAIL is a measure of the rival space and
not of what the method did, and it stands as declared. What the count shows
is that the rule being censused is not the rule that made the readings: not one of the 95 glosses
is present in every chapter its sign's folios cite, so the rivals — answer,
tell, ruler, cast, enter, depart — are words that satisfy a rule the
readings themselves do not. The rivals are the commonest free verbs of the
corpus; a random stem as rare as the chosen gloss survives every chapter
three times in a thousand. The census does not reach the question of
whether a second word fits each reading's own lines. That needs a
line-level count, which is the Mad-Libs companion Grok also asked for:
82 of the 670 A/B signs are the only K&T-unread sign on some line of their
evidence folio, 12.2%; the rest were read in company. The earlier 50 (7.5%)
was another consequence of the compact-reference parser bug corrected in
Tests 1 and 6.

## Test 14 — the blind rotated run, with an outside reader

`harness/ktblindfill.py` · `work/rohonc/ktblindfill.txt` ·
`work/rohonc/outside/blindfill/` (every prompt and reply, raw)

The test every reviewer asked for and Test 10 could not deliver by
machine: run the gap-filling loop on pages that have been handed the wrong
passage. Forty cited folios drawn by seed. Twenty got their own passage,
twenty got the passage of the cited folio seventeen places on, never one
sharing a chapter. Each page rendered in K&T's words only, gaps numbered,
nothing of ours. The reader, DeepSeek V4 Pro through OpenRouter at
temperature zero, was told nothing about arms and asked two things: does
this page retell this passage, and for each gap, one word if the passage
and the words around it determine it, else none. Two real-arm pages got
no answer, one after the model spent its whole thinking budget and one
when the key's monthly cap was reached; both are named in the run and
not scored.

    arm       pages   gaps   says it matches   fills   fills per page
    REAL        18     362        13                69        3.8
    ROTATED     20     374         0                 0        0.0

    MANUFACTURE  rotated fills must be under half of real   0% of real     PASS
    DETECTION    real must beat rotated, Fisher p < 0.01     p = 1.6e-06    PASS

Handed the wrong passage the reader filled nothing and said so every time.
Handed the right one it filled and said the page retold it on thirteen of
eighteen. The loop, run by a reader who does not know which is which, does
not produce readings from a passage that is not the page's. This is the
answer to Grok's first objection, on the actual procedure rather than a
proxy.

What the fills say about our readings is less than it looks. Of the 69
gaps the reader filled, 12 carry a tier A or B reading of ours, and the
reader agreed with 2 — shepherd and bread — which is the blindfold band,
one in six. Most of the rest are gaps we read as K&T's function words
written together (a genitive marker with "Lord", a conjunction with an
auxiliary) where the reader put the next content word of the verse. On
200v it filled all twenty-five gaps straight down the parable of the
vineyard, and where that runs into a reading of ours that K&T's own system
fixes, three tally strokes for "three", it is the reader that is wrong.
The reader's fills are a second single-line guess, not a standard, and the
agreement figure is reported as that.

## Test 15 — passage identification by an outside reader

`harness/ktpassid2.py` · `work/rohonc/ktpassid2.txt` ·
`work/rohonc/outside/passid/` (every prompt and reply, raw)

Gemini's first ask: someone independent identifies what each folio
retells, from the dictionary alone. The first twenty folios of Test 14's
sample, in K&T's words only, gaps as numbered blanks, and the reader asked
which chapter of the Bible the page retells. Control: the same twenty
pages with K&T's glosses shuffled among their signs. Halved from forty
before the run for cost. The reader was changed before any scoring:
Test 14's model took six minutes and twenty cents a page here and reached
four of forty before the key's cap; those replies are set aside unused
and the reader is DeepSeek V3.2 with thinking off, which is a weaker
reader and so a harder test.

    condition    chapter named is a cited chapter    book is a cited book
    real                  9 / 20   45%                   13 / 20   65%
    shuffled              0 / 20    0%                    3 / 20   15%

    discordant folios: real-only 9, shuffled-only 0, sign test p = 0.002
    Test 11's bag of stems over all 298 folios: top-1 12.4%
    cost $0.007

    BAR: p < 0.01 and real chapter hits >= 25%    PASS

From K&T's words alone a reader who knows the Bible names the cited
chapter on nine pages of twenty and the cited book on thirteen; from the
same words on the wrong signs, never the chapter. Of the misses, four
name the parallel telling of the same event, John 18 for Matthew 27,
Mark 5 for Matthew 9, Acts 7 for Acts 6, and are counted as misses.

## Test 17 — does Test 15's reader already know the answer?

`harness/ktmemory.py` · `work/rohonc/ktmemory.txt` ·
`work/rohonc/outside/memory/` (every prompt and reply, raw)

Added 2026-09-29. Test 15's shuffle rules out a reader who finds the Bible
in anything. It does not rule out memory. Király and Tokai published which
passage many folios retell, and a model trained on that could recognise a
page and recall the chapter; a remembered page is recognised only in its
real order, so memory would also beat the shuffle. This asks the same
model, same settings, the same twenty folios by number only, no page shown,
which chapter each retells. Control: each answer scored against the other
folios' cited chapters over 10,000 derangements.

    answered (not null)          1 / 20
    recall chapter hits          0 / 20
    of Test 15's 9 hits, recalled by number  0

    BAR: hits >= 3 and p < 0.01              NO MEMORY SHOWN

    Test 15 rescored on the 20 folios not recalled:
    real 9/20 45.0%   shuffled 0/20   Test 15's bar   PASS

The model declined nineteen folios and gave 1 Corinthians 13 for the
twentieth, which is wrong. It does not know which chapter goes with which
folio, so Test 15's nine were not recalled by label, and Test 15 stands
unchanged. What this cannot show is that the model knows nothing of K&T:
it could fail to recall by number and still recognise a page's wording.
Recall by label is the cheap and likely route, and it is closed. Cost
$0.0013.

## Test 18 — two blind models: read from some folios, judged on another chapter

`harness/kttwomodel.py` · `work/rohonc/kttwomodel.txt` ·
`work/rohonc/outside/twomodel/` (design, every prompt and reply, raw)

Every reading was checked at every place its sign stands before it was
kept, so no line is held out for the project's own readings. This asks what
can be asked instead. A reader model sees a sign on up to three folios, in
K&T's words only, and gives one gloss. A second model, from another
company, sees one line of a folio the reader never saw, citing a chapter
none of the reader's folios cite, and picks which of three glosses fills the
blank: the reader's gloss for that sign or the reader's glosses for two
other signs. Neither model sees this project's glosses or knows where a
candidate came from. K&T's own words go through the same steps as known
answers, matched to ours on how many folios they stand on. Design and bars
declared in the program before any call.

    reader DeepSeek V3.2, judge Gemini 2.5 Flash, both thinking off

    arm              judged   picked   chance      p     agree with the arm's word
    K&T known words      71    46.5%    33.3%  0.015           14.1%
    project A/B          63    36.5%    33.3%   0.34           12.7%

    CALIBRATION  K&T's words must transfer at p < 0.01     FAILED
    TRANSFER     ours, the same rule                       NO VERDICT
    AGREEMENT    ours at least half of K&T's rate          NO VERDICT

K&T's known words lean toward transferring and miss the declared bar, so
the instrument is not shown to have the power to judge ours, and by the
rule declared first nothing is concluded about them. Reported as it stands:
reading blind from a few folios, the reader lands on the project's word
about as often as on K&T's, 12.7% against 14.1%. Cost $0.04.

## Every run regenerated — 2026-09-22

Before publication every deterministic test was rerun from scratch and
diffed against its saved run. Eight did not match. The reason was one
commit: the readings last changed at 17:10 on 21 September, when the variant
loader was found to read only the first three spellings after a `var.` mark
and was fixed, and 234 spellings it had never seen came through; the runs
for Tests 1, 2, 2b, 5, 6, 7, 8 and 9 had been written between 16:01 and
16:52 that day, against the readings as they stood before. Nothing checked
the figures in this document against the runs, so the site and the book
quoted the old ones. `harness/check_tests.py` now does that check on every
commit.

All eight were regenerated on the final readings with the same seeds and the
same bars. The earlier files are kept beside them as `*_v2_prevariantfix.txt`.
What moved:

    test   figure                         before      after
    1      A+B sigma                        17.5       16.4
    1      C+D signs / sigma              37 / 6.2   32 / 5.6
    5      readings excluded as circular      583        581
    6      A+B gain / sigma               +73 / 6.9  +68 / 7.1
    7      read from this project alone    11.9%      11.6%
    7      recovery sigma, ten shuffles      4.4        8.4
    7      recovery sigma, hundred shuffles    —       10.3
    8      passage sigma (absolute)     33.9 (8.4%) 37.6 (6.1%)
    8      recovery sigma (absolute)     8.5 (0.9%) 15.3 (1.0%)
    9      A+B sigma / of K&T's rate    11.3 / 130%  6.9 / 115%
    2, 2b  stage 1 on K&T's own words     unchanged  unchanged
    10, 10b, 10c, 11, 12, 13              unchanged  unchanged

No verdict changed except Test 7's, and that one changed because its
control was too small to hold still, not because the readings did; the
section above tells it in full. The extension-attempt gates and the null
control that ROHONC.md reports (`ktsegment`, `ktname`, `ktalign_gate`,
`null_control`, `ktproof`) are records of attempts made on the readings of
their day and are not rerun; they date from 20 September and the document
says so where it quotes them.

## Every run regenerated again — 2026-09-28

The replay (`harness/reproduce_tests.py`) found 15 of the 20 saved runs no
longer reproduced. The cause was the same as on 22 September, over a longer
stretch: readings changed on 25 September (two readings corrected, commit
8ca1a99) and again on 28 September, when every line Király and Tokai's
dictionary cites was decided by hand and 50 of this project's readings were
replaced by theirs, and the saved runs were not rewritten. `check_tests.py`
did not notice, because it checks that each figure here stands in its saved
run, not that the run still comes out of the program. The replay was made a
gate on every build that day. On 29 September it was moved to release time:
it runs before every release, and a failing run is rerun and carried here
before the tag. Between releases a saved run can lag the readings; in a
published version it cannot.

All fifteen were rerun on the readings as they stand, with the same seeds
and the same bars. The earlier files are kept in the session's backups, and
the diff of every one was read before this was written. What moved:

    test   figure                         before      after
    1      A+B sigma / of K&T's rate      16.4 / 99%  15.4 / 100%
    5      readings excluded as circular      581        610
    5      A+B pairs / sigma               38 / 8.6   35 / 14.0
    5      C+D pairs                            2          0
    6      A+B sigma                          8.2        8.3
    7      recovery sigma, hundred shuffles  10.3       10.9
    9      A+B sigma / of K&T's rate    6.9 / 115%  8.9 / 125%
    10     rotated null kept / held out    6 / 1.9    4 / -0.6
    11     cited chapter top-1              12.4%      12.7%
    12     strict A+B / sigma          73.7% / 8.4  77.1% / 12.3
    12     over K&T's own headwords     +22.9 points +26.4 points
    13     rival in every chapter      61/94 64.9%  62/95 65.3%

No verdict changed. Test 5's C+D row no longer has a verdict to give,
because nothing is left in it. Test 12b could not be rerun on today's
readings at all: the outside readers answered a numbered sheet of 38 items,
and the scorer numbered today's pairs instead, so after the first changed
reading every answer was scored against the wrong sign. The sheet as sent is
now kept (`reglosser_key.json`) and the answers are scored against it; the
published 68.4% and 71.1% reproduce exactly. Tests 2, 3, 14, 15 and 16 did
not move.

## Six runs rerun — 2026-09-29

The numeral three with the year-or-day sign had printed "three days" on all
eighteen of its lines; it now prints "three", with "days" kept by hand on the
seven lines that mean days. That moved six saved runs a little. Each was
rerun on the readings as they stand, with the same seeds and the same bars,
and the diff of every one was read before this was written. What moved:

    test   figure                         before        after
    1      A+B held-out rate / of K&T's    25.9% / 100%  25.5% / 98%
    5      readings excluded as circular      610           611
    5      A+B pairs / sigma / of K&T     35 / 14.0 / 161%  33 / 13.9 / 159%
    6      A+B gain over the shuffle          +58           +56
    7      recovery sigma, hundred shuffles  10.9          10.8
    8      predicted passages filled         51.5%         51.2%
    12     strict A+B / sigma             77.1% / 12.3  78.8% / 13.4
    12     over K&T's own headwords       +26.4 points  +28.0 points
    12     leakage check                  1.5 sigma     0.7 sigma

No verdict changed. Test 12 still fails its leakage clause, by more. From
this date the replay runs before every release rather than on every commit
(see above).

## Folio-reference correction — 2026-09-29

The evidence parser in Tests 1, 6 and 13 required a word boundary after the
folio side. It therefore missed the corpus's usual compact citations, such as
`033v05`, and subdivision citations such as `013vc1:03`. The parser is now
shared, tested against every form in the evidence, and optionally checked
against the manuscript's folio set. The same correction was applied to Test
12's leakage diagnostic and the historical `ktproof` program.

    test   figure                              before          after
    1      A+B signs / occurrences          311 / 632       100 / 367
    1      A+B rate / shuffle / sigma   25.5 / 5.5 / 15.4  24.8 / 7.6 / 9.4
    6      A+B gain / sigma                    +56 / 8.3       +25 / 5.7
    12     leakage signs / occurrences / sigma 10 / 56 / 0.7    7 / 52 / 0.5
    13     Mad-Libs companion                  50 / 7.5%       82 / 12.2%

The old numerical bars would still be crossed, but Tests 1 and 6 are no
longer given PASS verdicts. Checking every occurrence was part of the
admission rule, so excluding only the folios written in an evidence note did
not create an independent holdout. Their corrected figures remain as
selection-conditioned diagnostics.

## Summary

    The transcription every other test reads, checked against an independent one:
    Test 16 | a second, independent transcription | 91.1% of glyphs agree where both can be compared, against a 12.9% control, 458.5 sigma; 83.8% of the words identical | PASS

    The readings:
    Test 1  | source presence, evidence-excluded folios | A+B 9.4 sigma; 95% of K&T's own rate, after correcting compact folio references; selection-conditioned | reported, not a verdict
    Test 5  | K&T's own sentence translations | A+B 13.9 sigma; 159% of K&T | PASS
    Test 6  | word order, evidence-excluded folios | A+B 5.7 sigma after correcting compact folio references; selection-conditioned | reported, not a verdict
    Test 2  | part of speech from context | the instrument fails on K&T's own words (68.3% against a needed 70%; 4.7 sigma against a needed 5); the readings were never scored | NO VERDICT
    Test 3  | the blindfold, run clean | 4 of 24 strict, 16.7%; the declared band for that result was 15-30%, and its declared consequence, tier C passage readings become tier D, was applied | IN BAND
    Test 7  | K&T's words removed | reads 11.6% from this project's readings alone, by design: the readings extend the dictionary. Recovery of a hidden K&T word: 10.8 sigma against a declared 5, on a hundred-shuffle control; the ten-shuffle runs gave 4.4 before the variant fix and 8.4 after, and all three are kept | PASS
    Test 8  | bootstrap from a random 30% | passage 37.6 sigma (6.0% absolute); recovery 15.3 sigma (1.0% absolute) | PASS
    Test 9  | hidden 70% validated by the 30% | A+B 8.9 sigma; 125% of K&T's own rate | PASS

    After the outside review by Gemini 2.5 Pro and Grok 4.7, same day:
    Test 11 | passage map from K&T's words alone | median rank 25 of 1,334; top-1 12.7%; p 8e-29 | PASS
    Test 10 | the search replayed on null books | 7 / 217 / 2 signs kept at three scales; the count rule has no power at any, so it cannot tell a search from a decipherment | NO VERDICT
    Test 10, held out | the same runs, scored where the readings were not derived | real book 8 sigma over shuffle; null books none | reported, not a verdict
    Test 12 | Test 5 rescored under the strict rule | 78.8%, 13.4 sigma; but +28.0 points over K&T's own headwords trips the declared leakage clause | FAIL on that clause
    Test 12b | two independent re-glossers, Gemini 2.5 Pro and Grok 4.7 | given K&T's words only and the sign blanked, they recover this project's gloss 68.4% and 71.1% of the time | PASS
    Test 13 | the underdetermination census | 62 of 95 A/B readings have a common verb present in every chapter their folios cite, against a bar of 40% | FAIL
    Test 13, the same rule | applied to the chosen glosses | 0 of the 95 pass it. The rivals exist; the method did not choose them. The FAIL measures the rival space, not what the method did | reported, not a verdict
    Test 14 | the blind rotated run, outside reader | rotated book 0 fills, 0 matches; real book 3.8 fills a page, 13 of 18 | PASS
    Test 15 | passage identification, outside reader | chapter level 9 of 20 against 0 of 20 shuffled; p 0.002 | PASS
    Test 17 | memory check on Test 15's reader | asked by folio number with no page shown, it names 0 of 20 cited chapters and declines 19; Test 15's nine were not recalled by label | NO MEMORY SHOWN
    Test 18 | two blind models, reader and judge | K&T's known words transfer to another chapter 46.5% against 33.3% chance, p 0.015, short of the declared 0.01; the reader lands on the project's word 12.7% of the time and on K&T's 14.1% | NO VERDICT

    PASS and FAIL are verdicts on the readings against a bar declared before the run.
    NO VERDICT means the instrument failed its own check on Király and Tokai's words,
    or has no power to tell a search from a decipherment; it says nothing about the
    readings either way, and it is kept on the page because it was specified.
    IN BAND is a test with declared bands rather than a bar: the result fell in the
    band it was predicted to, and the consequence declared for that band was applied.

Where that leaves the 670 tier A/B readings. The passage map survives
without them (Test 11), so the tests still have a target. Test 9 retains its
PASS, while Tests 1 and 6 are selection-conditioned diagnostics rather than
independent confirmation. Test 5 likewise measures agreement with K&T's
translations, which were available while the readings were made. The loop
run blind on rotated pages (Test 14) produced nothing when handed the wrong
passage. The guesses are measured by Test 3: one in six strict, one in
three lenient.

Also on record, from earlier the same day: K&T's own citations land on the
folio they name 89.2% of the time and the exact line 97.5% of those, against
1.9% by chance (`ktkeycheck.py`); and across all 926 readings there are zero
conflicts with their dictionary (`ktagree.py`).
