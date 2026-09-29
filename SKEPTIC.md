# For the skeptic

Written 2026-09-29, from a reply to a forum thread that asked the right
question: did the machine "solve" the Rohonc Codex, or is it a Rorschach
test? Every figure below is checked against the saved run it names, by
`harness/check_skeptic.py`, and every run is on the [tests page](/rohonc/tests.html) with its bar.

## The real question

The real debate is whether Király and Tokai's findings are valid. A text like
the Rohonc Codex, with no outside referents, can never be conclusively solved
without any doubt. So there are two questions. First, is it real language and
not a fraud? Second, if it is, which reading works best, without bias, since
absolute certainty is impossible?

And the Bible is so familiar that it could almost certainly be made to fit
anything. That is the Rorschach test. Several things go a long way toward
answering it.

## Is it language at all?

**Sentences run across line breaks.** In real writing, a sentence doesn't care
where the margin falls, so word pairs that straddle a line break also turn up
inside lines elsewhere. In the Rohonc, more than a third of them do, against
about a fifth by chance. That puts it in the same range as Italian and Hebrew
prose. The same test on the Voynich lands with the meaningless text
generators. So the test can tell the difference, and the Rohonc comes out on
the language side. It holds on two transcriptions made years apart by
different methods.

    found / chance   (crossline.txt)
    Rohonc, K&T     37.14%  18.23%
    Rohonc, 2014    84.37%  76.70%
    Italian prose   25.24%   9.64%
    Hebrew prose    21.43%   6.79%
    Voynich          6.46%   5.85%

**It repeats long passages at different places on the line.** The same run of
words sits across a line break in one place and whole inside a line in
another. That is what a scribe copying real text produces. Filler wouldn't
do it.

This shows it isn't meaningless filler. It can't rule out a clever forger
writing real sentences in an invented script. But if that is what it is, it
is still a text with content, and the question of reading it stays the same.

## Does Király and Tokai's reading hold?

**Scrambled, it stops fitting.** If the Bible could be made to fit anything,
it should fit scrambled pages too. It doesn't. An outside model was given 20
pages written only in Király and Tokai's words, with every unread sign left
blank, and asked which chapter of the Bible each one retells. It named the
right chapter on 9 of 20. With the same words shuffled among the signs, it
got 0 of 20.

    Test 15   (ktpassid2.txt)
    real pages       9/20  45.0%
    shuffled pages   0/20   0.0%

**It wasn't memory.** Király and Tokai published which passage many pages
retell, so the model might just remember. The same model was asked which
chapter each of those 20 pages retells, by page number only, with no page
shown. It didn't know a single one.

    Test 17   (ktmemory.txt)
    recall chapter hits   0 / 20

**Given the wrong passage, it notices.** The gap-filling step was given 20
pages paired with the wrong Bible passage and 18 with the right one, and the
model wasn't told which was which. On the wrong pages it filled nothing, and
it said every time that the page didn't match. On the right pages it filled
about four gaps a page. If the method just made the Bible fit, it should have
made the wrong passages fit too.

    Test 14   (ktblindfill.txt)
    right passage, 18 pages
      13 say it matches
      3.8 fills a page
    wrong passage, 20 pages
      0 say it matches
      0.0 fills a page

**The readings hold where nobody looked.** Each reading comes from one page.
On every other page where the same sign appears, the reading lands in the
cited passage about as often as Király and Tokai's own dictionary words do,
and about four times as often as shuffled words.

    Test 1   (ktheldout.txt)
    K&T's own words     26.0%
    project readings    25.5%
    shuffled             5.5%

**Király and Tokai's own work checks out.** When their dictionary cites a page
for a word, the word is on that page 89% of the time, against about 2% by
chance. Their transcription also matches an independent one made years
earlier, which nobody tuned to their reading: 91% of the signs agree where
both can be compared.

    citations   (keycheck.txt)
    on the cited page   89.2%
    page shuffled        1.9%

    Test 16   (ktopen.txt)
    glyphs agree        91.1%

## What this does not show

All of this was done with machine readers, and a skeptic can fairly discount
some, but not all, of that. Some of the tests couldn't separate a true reading
from one copied off Király and Tokai's translations, and two tests failed bars
set in advance. One of them arguably measured the wrong thing; it stays
a failure anyway, because a bar is not moved after the result. All of it is on the [tests page](/rohonc/tests.html), beside the passes. And
the samples are small: the scrambled test and the memory check use 20
pages, the wrong-passage test 38. The odds against chance are still
long, but more pages would make them longer.

Whether human readers, performing the same tests, would be more or less
biased is an open question as well, but it would be a welcome test.
