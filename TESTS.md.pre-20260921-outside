# TESTS — whether this project's additions to the dictionary are true

Written 2026-09-21. Every bar below was declared in the test's own docstring
before it ran, and none was moved. Saved runs are in `work/rohonc/`.

The question: Király and Tokai published a dictionary of 841 signs. This
project added 926 readings on top (tiers A–D) and 848 bracketed guesses
(tier G). Are the additions true?

Every earlier check was run by the process that made the readings. These
six were designed to break that.

## Test 1 — do the readings track their source where nobody looked?

`harness/ktheldout.py` · `work/rohonc/ktheldout.txt`

Every reading names the folio it was read from. That folio is excluded. On
every other folio where the sign stands and a chapter and verse is cited,
the test asks whether a word of the gloss is in that passage. Control: the
same signs on the same folios with the glosses shuffled among readings of
the same tier, twenty times. Ceiling: K&T's own glosses measured the same
way — true words that still miss, because a folio cites one passage and
carries a dozen lines.

    K&T's own words                          1704 / 6565     26.0%

    tier   signs  held-out   rate   shuffle   sigma   vs K&T
    A+B      310       634  25.7%     6.0%    17.5      99%    PASS
    C+D       37       155  26.5%     9.3%     6.2     102%    PASS

On folios that played no part in choosing them, the readings land in the
cited passage at the same rate as the dictionary they extend, and four
times the rate of a shuffled gloss.

## Test 5 — external truth: sentences K&T translated whole

`harness/ktsentence.py` · `work/rohonc/ktsentence.txt`

K&T's dictionary quotes 172 example sentences from the codex with their own
English and a folio cite. Those sentences contain signs they never glossed
on their own, so their translation says what each such sign means there, in
their words, before this project existed. Every reading whose evidence so
much as mentions them is excluded as circular — 583 of them. Control:
glosses shuffled among the tested signs, twenty times. Ceiling: K&T's own
headwords standing in the same sentences.

    K&T's own words echoed in their sentences    223 / 419    53.2%

    tier   signs  pairs   rate   shuffle   sigma   vs K&T
    A+B       26     38  81.6%     7.9%     8.6    153%    PASS
    C+D        2      2  100%        —       —       —     two pairs, no sigma

The confirmed readings are echoed in their translations more often than
their own headwords are: ours are content words, theirs include prefixes
and particles a free translation swallows. The seven misses — law, five,
three, mount, pierce, redeem, ghost — are numerals and words a paraphrase
drops.

## Test 6 — word order on held-out folios

`harness/ktorder.py` · `work/rohonc/ktorder.txt`

Test 1 asks whether a word is in the passage; a right word on the wrong
sign passes that. This asks whether it lands in the right place: the
longest common subsequence of content words, in order, between each cited
folio and its passage — K&T alone, K&T plus our A/B readings, and K&T plus
the same glosses shuffled among the signs. A reading is used on a folio
only if that folio is not named in its evidence.

    cited folios 297      K&T-only match total 1340

    A+B, held out    670 signs   gain +73    shuffled +14.6 (sd 8.5)   6.9 sigma   PASS

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
were never scored by it.

## Test 3 — the blindfold, run clean

`harness/ktblind.py` · `work/rohonc/blindfold_1790006519.txt` and `_score.txt` · `BLINDFOLD.md`

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

    words read           3579 / 29997    11.9%
    lines touched        2466 /  4372    56.4%
    lines fully read        2 /  4372     0.0%

No. Our readings are an extension of their dictionary and read nothing
without it. That is what they were built to be.

Second: can ours give K&T's words back? Hide one of their signs, render its
line with our readings only, align the line to the cited passage in order,
and take as candidates the passage words that fall between the nearest
matched word before the hidden sign and the nearest after. Then reveal
their gloss. Control: our glosses shuffled among the signs. Ceiling: the
same method with the whole dictionary as anchors.

    616 K&T signs, 1392 occurrences, capped at three per sign

    anchors        presence   top-1   no anchor
    ours A+B          2.6%     0.4%      89.1%
    ours A-D          3.7%     0.5%      84.6%
    K&T + ours       10.9%     1.9%      39.7%
    shuffled          0.7%     0.1%

    ours A-D vs shuffled   4.4 sigma   needed 5   FAIL

The direction is right and the bar is not met. The reason is on the same
table: with our readings alone, nine lines in ten have nothing that matches
the passage, so there is nothing to bracket the slot; and even with the
whole dictionary as anchors the method finds the word only one time in
nine. The instrument is weak. What can be said is that ours alone reach
about a third of what the whole dictionary reaches by it, and beat a
shuffle of themselves by four sigma.

## Test 8 — from a random 30% of the words, can the rest be got back?

`harness/ktbootstrap.py` · `work/rohonc/ktbootstrap.txt`

A random 30% of every readable sign, K&T's and ours together, kept; the
other 70% hidden. Two stages, both bars declared first.

    readable signs 1580   seed 474   hidden 861 on cited folios
    the seed covers 19.2% of the tokens on those folios

Stage 1, which passage is this folio: render each cited folio with the seed
words only and pick, from the 285 passages any folio note cites, the one
that contains most of what is rendered.

    seed words          8.4% of folios right
    seed shuffled       0.3%  (chance 0.4%)      33.9 sigma     PASS

Stage 2, fill the holes: bracket each hidden sign's slot in the passage
between the nearest seed word before and after it, fill the narrowest
windows first with the rarest candidate, make the fills anchors, go round
again.

    true passages        filled 27.2%   recovered  0.9%
    predicted passages   filled 42.0%   recovered  0.7%
    seed shuffled                       recovered  0.0%   8.5 sigma   PASS

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
    K&T's         1374   19.1%     3.7%    10.2
    ours A+B       652   24.8%     4.0%    11.3    PASS   130% of K&T's rate
    ours C+D       299   23.4%     4.3%     6.9

This is the two codes proving each other. A random third of the dictionary
— theirs and ours mixed — places the other two thirds, theirs and ours
alike, five to six times better than chance, and our readings fit the
slots the seed brackets at least as well as theirs do. Occurrences where the
line held no seed word at all are set aside, not counted either way.

## Summary

    Test 1   source presence, held-out folios    A+B 17.5 sigma   99% of K&T    PASS
    Test 5   K&T's own sentence translations     A+B  8.6 sigma  153% of K&T    PASS
    Test 6   word order, held-out folios         A+B  6.9 sigma                 PASS
    Test 2   part of speech                      instrument fails on K&T's own words
    Test 3   blindfold, run clean                 4 of 24 strict, 16.7%; band 15-30%, consequence reaffirmed
    Test 4   illustrations                       blocked on the image mapping
    Test 7   K&T's words removed                 reads 11.9% from ours alone; recovery 4.4 sigma, FAIL
    Test 8   bootstrap from a random 30%          passage 33.9 sigma, recovery 8.5 sigma, PASS; absolute 8.4% and 0.9%
    Test 9   hidden 70% validated by the 30%       A+B 11.3 sigma, 130% of K&T's own rate   PASS

Four independent tests, four passes, for the 670 tier A/B readings. Tier
C/D passes Test 1 and is too thin for the other two. The guesses are
measured by Test 3: one in six strict, one in three lenient.

Also on record, from earlier the same day: K&T's own citations land on the
folio they name 89.2% of the time and the exact line 97.5% of those, against
1.9% by chance (`ktkeycheck.py`); and across all 926 readings there are zero
conflicts with their dictionary (`ktagree.py`).
