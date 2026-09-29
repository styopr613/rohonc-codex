# Are Király and Tokai's results valid?

A text like
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

**The readings agree beyond the folios named in their evidence, but this is
not held out.** On other pages where the same sign appears, the reading lands
in the cited passage about as often as Király and Tokai's own dictionary
words do, and more often than shuffled words. These pages were nevertheless
checked while deciding which readings to keep, so this is a
selection-conditioned diagnostic, not evidence from somewhere nobody looked.

    Test 1   (ktheldout.txt)
    K&T's own words     26.0%
    project readings    24.8%
    shuffled             7.6%

An earlier run said 25.5% against 5.5%. Its evidence parser recognized
`033v` but missed the usual compact form `033v05`, so named evidence folios
were incorrectly counted as excluded. The corrected run also reduces the
word-order diagnostic from 8.3 to 5.7 sigma. Neither diagnostic now carries
an independent PASS verdict.

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
set in advance. All of it is on the [tests page](/rohonc/tests.html), beside the passes. And
the samples are small: the scrambled test and the memory check use 20
pages, the wrong-passage test 38. The odds against chance are still
long, but more pages would make them longer.

There is no untouched occurrence-level holdout for the added readings: the
method required proposed fills to be checked at every occurrence before they
were admitted. A future generalisation claim therefore needs material hidden
during selection or a prospective evaluation on newly available evidence.

That prospective check was then run with a fresh, stateless reader. It saw
one occurrence of each sampled sign and a different occurrence was concealed.
Its new glosses reached concealed source passages more often than shuffled
glosses, but almost never agreed with this project's glosses; the stronger
word-order measure did not separate significantly.

    Test 18   (ktprospective.txt)
    concealed passage hits      8/26  30.8%
    shuffled                           12.4%
    difference                          3.2 sigma
    agreement with project       2/26   7.7%
    word order                           2.0 sigma

Thus a blind reader extracts recurring passage-level signal; this run does
not independently recover the project's dictionary. It is reported without
a verdict because no outcome bar was declared before the run.

Whether human readers, performing the same tests, would be more or less
biased is an open question as well, but it would be a welcome test.
