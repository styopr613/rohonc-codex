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

## Test 3 — the blindfold, ready to run

`harness/ktblind.py` · `work/rohonc/blindfold_1790006519.txt` · `BLINDFOLD.md`

Twenty-five of K&T's own entries hidden; a reader who has not seen the
dictionary reads them from the same evidence the pipeline gives; then the
answers are revealed and scored. This measures the accuracy of the
procedure that produces guesses, on words whose answers are known. The
sample is drawn with a fresh seed and the context shows K&T's dictionary
only — a leak that let this project's own readings into the context was
fixed the same day. Consequences by score band are declared in
`ktrederive.py`. Not yet run: it needs a blind reader.

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

## Summary

    Test 1   source presence, held-out folios    A+B 17.5 sigma   99% of K&T    PASS
    Test 5   K&T's own sentence translations     A+B  8.6 sigma  153% of K&T    PASS
    Test 6   word order, held-out folios         A+B  6.9 sigma                 PASS
    Test 2   part of speech                      instrument fails on K&T's own words
    Test 3   blindfold                           drawn, needs a blind reader
    Test 4   illustrations                       blocked on the image mapping
    Test 7   K&T's words removed                 reads 11.9% from ours alone; recovery 4.4 sigma, FAIL
    Test 8   bootstrap from a random 30%          passage 33.9 sigma, recovery 8.5 sigma, PASS; absolute 8.4% and 0.9%

Three independent tests, three passes, for the 670 tier A/B readings. Tier
C/D passes Test 1 and is too thin for the other two. The guesses are
measured by Test 3 when it is run.

Also on record, from earlier the same day: K&T's own citations land on the
folio they name 89.2% of the time and the exact line 97.5% of those, against
1.9% by chance (`ktkeycheck.py`); and across all 926 readings there are zero
conflicts with their dictionary (`ktagree.py`).
