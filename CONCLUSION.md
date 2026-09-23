# Conclusion, in plain English

Written 2026-09-20, after the work in `RESULTS.md`. That file has the
numbers and the tables. This one has what they add up to.

## The short version

There is very probably nothing to translate.

The text has the surface look of writing. Underneath, it behaves like a
process that fills one line at a time with word-shaped strings, not like
a message that happens to be written in lines. Every cipher we built
failed for a structural reason, not a tuning reason. Every mindless
line-filling process we built came close, and the one with the fewest
rules came closest.

## The three findings that carry the weight

**1. The structure stops at the right margin.**
In real language the link between one word and the next carries on
across a line break, because sentences do not care where the margin is.
Italian keeps 93% of it across a break. The manuscript drops to zero at
every line, on two independent transcriptions. Whatever made this text
started fresh at each line.

**2. Ciphers cannot buy both properties at once.**
The manuscript's letters are unusually predictable from the one before,
and its words are strongly linked end-to-start. A cipher can reach the
first by giving each plain letter many disguises, but that destroys the
second. A cipher that keeps the second cannot reach the first. We built
both kinds and each hit the wall it was predicted to hit.

**3. Copying makes things worse, not better.**
The leading "meaningless" hypothesis says the scribe copied nearby words
and changed them slightly. We built that and turned the copying rate
down step by step. Every measure improved as copying was removed, and
the model with no copying at all scored best. Copying preserves the
start of a word. The manuscript's constraint runs from the end of one
word to the start of the next. Those are different things.

## The control we were missing

A test pointed at only one book is not a test. So the line-break measurement
was run on a second uncracked manuscript, the Rohonc Codex, which ought to come
out the other way. It does, on two independent transcriptions made years apart
by different methods.

On the scholarly transcription, more than a third of the word sequences that
straddle a line break also appear inside a line somewhere else in the book,
against a chance level of about a fifth. In the Voynich the two numbers are the
same. Normalised so the books are comparable, the Rohonc sits in the same band
as Italian and Hebrew prose and the Voynich sits with the meaning-free
generators. The Rohonc repeats long passages at different distances from the
margin, so text split across a break in one place sits whole inside a line in
another. That is what a real text laid out by a scribe looks like. The Voynich
never does it once.

The first write-up got the unit wrong -- it counted glyphs where the other
manuscripts were counted in words -- and the number moved when that was fixed.
It moved into the language band, not out of it.

## Is the Rohonc solved?

Probably, and that was checked rather than assumed. Király and Tokai announced
a decipherment in 2018 and have never published the translation. Their
dictionary is online so it can be verified, and it was: it covers 62% of the
running text; its twenty commonest entries are and, this, be, in, Lord, man,
say, come, all, son, disciple, God, give, because -- a function-word core with
a gospel vocabulary behind it, which is a property of the codex they did not
control; and the names it identifies cluster in the gospel text where a real
paraphrase would put them, 87% of the time against a 50% chance.

Finishing the translation was attempted seventeen ways. Fourteen failed, each
against a bar set before the run and never moved. The eleventh was a specific
prediction of mine and it was wrong: the alignment method had been pointed at
the four canonical gospels, so the reference was rebuilt from the sources
Kiraly names -- the whole Bible, the apocryphal infancy and Nicodemus gospels,
the four English mystery cycles, Caxton's Golden Legend -- and the method
scored no better than before.

The twelfth and thirteenth worked, and the reason the first eleven did not is
that they all treated a code as a single word with a single meaning to guess.
Many codes are not words. They are short phrases written without a space, and
the dictionary already contains both halves. Kiraly and Tokai say so in their
2022 paper: the codex does not conjugate, so instead of a pronoun it repeats
the name sign of whoever is being spoken about, and they print one code as
"you-Mary" -- their own word for *you* followed by their own sign for *Mary*.

That construction was confirmed here without using any of their glosses, by
showing that a code ending in a name sign turns up where that name turns up,
far beyond what matched controls do. Cutting the codes apart on that basis
reads 1,282 of them that their published dictionary does not contain, and
takes the share of the book that can be read from 58% to 78%. What comes out
is what a devotional book should say: Lord Jesus Christ, of the Lord, the
Virgin Mary, God the Father, the Holy Word, Saint John, Saint Luke.

The one code that survived the earlier attempts, which could only be called a
noun somewhere in the vocabulary of the adversary, turns out to be two signs,
and the second is their own sign for Lucifer. There was never a meaning to
infer. The word was sitting inside it.

The grammar is theirs. What is new is checking it independently and running it
across the whole book.

It is worth being exact about what a percentage of the book means, because
there are three numbers and they mean very different things. **96.6% of the
words have *a* reading; 81.5% of the lines have every word read; and 98.9% of
the lines are complete once bracketed guesses are counted.** The middle one is
the one that matters, because a sentence with one unreadable word in it is not
a sentence you can read. It stood at 2.8% before any of this, at 62.4% on the
morning of 2026-09-20, at 74.9% on the morning of 2026-09-21, and at 82.3%
that evening. It then went DOWN, to the figure at the head of this section:
the hardening sweeps of 21 and 22 September withdrew readings that did not
survive every occurrence, and a withdrawal takes a line out of the fully-read
count. A number that only ever rises is a number nobody is checking. The third number is not a decipherment figure at all; it is the
reader's edition having a word in every slot, 3.3% of them guesses.

Even the word figure overstates how much is understood. Only about one word in
eight has a single meaning with no choice to make; most carry several senses
each, and the rule for choosing between them is in the grammar paper Kiraly
and Tokai have not published.

**What moved it from 74.9% to 80.1% was not more reading of lines. It was three
small instruments that read the dictionary instead.** (A fourth, described
further down, took it from 80.1% to 82.3% by following Kiraly and Tokai's own
folio-line citations back into the manuscript.) Each asks a mechanical
question about the shape of a sign, and each found words that hours of reading
passages had walked past:

    ktinside.py   an unread sign sitting INSIDE a sign K&T already read.
                  Their 520af0a105204e4 'wipe with kerchief' minus the
                  garment sign is the towel of John 13:4. Their 'cling'
                  entry contains the clinging of the man in the pit.
                  Joachim and his_household are the two halves of one of
                  their compounds, standing alone on consecutive lines of
                  the folio that compound is about.

    ktcover.py    a sign almost entirely MADE of signs already read, with
                  the gap measured. 021v:14 is a single unspaced string
                  that covers out to Lord, mother, Mary, Holy Spirit and
                  Joseph -- a naming formula written as one word, which is
                  the central fact K&T established about this script.

    ktnear.py     a sign ONE GLYPH from a sign already read. This is how
                  the codex's own spelling wanders, and K&T's apparatus
                  records it with var. entries.

`ktnear.py` also audited this project against K&T on its first run, and the
first thing it found was an error here. Five signs had been read as *child*
from the story on the folio -- Augustine and the boy by the sea. They are one
glyph from K&T's `5400609a2670690`, *a little while; little*, whose form stands
two lines above this project's on the same folio modifying the same phrase, and which
gives *the tip of his finger* at Luke 16:24. All five were corrected to
*little*. Three more of this project's readings went the same way in the same
pass: *evil* twice to **serpent**, *remain* twice to **whom** (both lines have
the seeking beside them -- John 18:4 and 18:7, *Whom seek ye?*), and *exist* to
**Nicodemus**. The rule that costs the least to follow: **before reading a sign
from its context, check whether it is one glyph from a sign already read.** A
story that fits is not evidence; a near-match to their dictionary is.

So the obstacle has moved rather than gone. It used to be missing vocabulary.
It is now two things: missing grammar, which is theirs to publish, and 826
signs that occur exactly once in the manuscript and that their dictionary never
mentions. A sign that occurs once cannot be checked against a second
occurrence, which is the whole method, so a reading of one is a guess about a
line rather than a reading of a sign.

The three figures below are not interchangeable, and a version of this
paragraph got that wrong on 2026-09-21 and was corrected in place: it claimed
that reading every remaining recurring sign would reach 90%. It will not.

    read every recurring unread sign (117 left)         83.5%
    read every once-only sign (826 left)                bounded by the lines
                                                        they stand on
    read both                                          100%

The once-only signs are worth more than the recurring ones simply because
there are seven times as many, which means **no route past the mid-eighties
avoids them**. Each is a reading of a line rather than of a sign, so tier C is
the ceiling on its evidence unless Kiraly and Tokai's own apparatus happens to
name it -- and that seam, which looked worked out at six signs, turned out to
hold about seventy once the three instruments above were pointed at it.

**What the 81.5% is made of.** A percentage without a tier distribution
behind it is a claim, not a result. `ktprov.py` computes this and reads none
of the prose of the evidence field -- every class is worked out from the sign
itself against Kiraly and Tokai's dictionary, so a reviewer can rerun it.

    THE WHOLE RENDERING, WORD BY WORD          29,997 words

      K&T's dictionary, unchanged              17,673   58.9%
      by composition of signs they read         7,662   25.5%
      this project, anchored on a K&T entry     1,886    6.3%
      this project, anchored on a reading
        of its own                                421    1.4%
      this project, read from a passage         1,375    4.6%
      a tagged guess, bracketed, never counted    975    3.3%
      no reading at all                             5    0.0%

    THIS PROJECT'S 1,786 ENTRIES, BY TIER

      A  survives every occurrence, or proved by an identical
         formula, a numeral, or K&T's own citation          476
      B  survives most occurrences                          178
      C  one passage, or source-checked                     211
      D  a single occurrence, read from one line             82
      G  a guess, never counted as read                     839

    THE 947 READINGS THAT ARE NOT GUESSES, BY WHERE THEY CAME FROM

      anchored on a K&T entry        514 signs  54.3%
        of which: holds one of theirs whole 266,
        one glyph from one 172, sits inside one 76
      anchored on a reading of ours  108 signs  11.4%
      read from a passage            325 signs  34.3%
      judgments flagged as such in the evidence: 4

**Two thirds of this project's non-guess readings are co-signed by the
published work** -- they were got from Kiraly and Tokai's own entries by
decomposition, by containment or by a single-glyph match, so the word is
theirs and only the placement is ours. The 325 read from a passage are the
ones that stand or fall on this project's evidence alone, and they are the
ones a reviewer should go at first. The 839 tier G entries are not readings
at all and are excluded from every figure above except their own line.

**Two documents, because they have different jobs.** The deposit is strict:
`harness/proposals.json` carries one entry per sign with its tier and the
argument in full, and `ktprov.py`, `ktvarcheck.py`, `ktnull.py` and
`ktrederive.py` exist to be used against it. The **reader's edition**
(`work/rohonc/translation/rohonc_readers_edition.md`, generated by
`ktreader.py`) is the other thing: all 441 written pages as continuous text, with the
apparatus every damaged classical text uses --

    word      read
    word*     read from one passage, nothing in the book can refuse it
    [word]    restored: a guess from the folio's source and its neighbours
    [...]     dark

    read                             27,997   93.3%
    read from one passage, marked *   1,020    3.4%
    restored, in brackets               980    3.3%
    dark, printed as an ellipsis          0    0.0%

**There are no ellipses left.** Every word of the manuscript has an English
word against it. That is emphatically not the same as every word being read:
3.3% are brackets and the brackets are the weakest thing in the edition. They
were printed because a reader asked for the book completed rather than left in
holes, and because a bracket that is visible on the page can be stripped out
by anyone who wants only what is established.

What a bracket is worth was measured before any were printed. On words as rare
as these, the folio's cited passage contains the true word 7.8% of the time,
and when it is there the best candidate is right about one time in four;
against Kiraly and Tokai's hidden entries the top candidate scored 0.0%. What
can be checked from inside the book is that three quarters of the content
guesses land on a word that actually stands in the verse the folio cites. The
weakest are the last two leaves, 224r and 224v, the worst-preserved in the
manuscript, whose brackets are tagged WEAK in the deposit.

Five brackets carry a chapter number that differs from folio to folio. One
sign, written as four strokes, a mark and four strokes, stands in the
chapter-citation slot on five folios, and the passage that follows it is
Matthew 16 on 195v, Matthew 18 on 134r, Matthew 22 on 202v and Luke 14 on
071r. One sign cannot be four chapters, so it is not read; `ktfolio.py` simply
prints the chapter each folio's own following text shows.

## The dictionary cites the manuscript, and the citations had never been followed back

Kiraly and Tokai's entries carry an apparatus: the folio and line where a word
stands, and where a *variant spelling* of it stands. "[var. 065v01, 218v09]".
"185r07 Heraclius". "088v11 covered with wounds". That apparatus points at the
manuscript, so it can be run backwards.

For every line this project could not fully read, ask whether any K&T entry
cites that exact line. 398 do. Where such a line has exactly one hole AND the
word their entry names is not already rendered somewhere else in the line,
their entry names the hole.

That gave 44 readings in an afternoon, eleven at tier A -- the tier reserved
for "proved by K&T citation", which had almost never been reachable before.
Holy Anne. In Nain. The aged, which is Joseph's standing epithet. Holy Mark,
holy James, Heraclius, arrived, fourteen, to Bethany, confess, exist. None is
a guess; each is Kiraly and Tokai's own reading of that line, in a spelling
the open transcription writes differently from their headword.

It had been missed for six years, and the reason is exact: the variant reader
keyed on headwords, so a form carrying a prefix -- their sign for "holy" in
front of Mark, of Anne, of James -- never matched anything.

The same screen is also what says no, and says it far more often. On 36 cited
lines the word their entry names is already rendered in the line, so the
citation reaches a different token and cannot fill the hole. Those are written
down as failures, not quietly counted.

## The dark words were never the main damage

A finished page that read as word salad was assumed to be salad because of the
holes. It was not. Measured across every folio that cites a chapter and verse:

    rendered words with more than one K&T sense       9,437
    the printed first sense IS in the cited passage   1,650
    the first is NOT, but another sense of the
      same entry IS -- the printed word is wrong      1,628
    words with no reading at all, for comparison        322

Wrong-sense words outnumbered dark words five to one. "somebody" where the
verse says *man*. "each, every" where it says *whole*. "land" where it says
*kingdom*. "apostle" where it says *disciple*. The renderer printed Kiraly and
Tokai's first sense always -- which was itself an earlier fix, and only half
the job.

`ktsensefit.py` prints the sense the folio's own cited passage uses, choosing
only among senses they published for that sign. 755 words on 222 folios.

**The guard that made it honest.** The first version turned "and" into "also"
87 times, "from" into "away" 29 times, "this" into "thus" 12 times. The cause
was exact: a first sense like "and" contains no content word, so the test "is
the first sense in the passage?" could never pass, and every such sign fell
through to whatever later sense the passage happened to contain. A match on a
word that common is chance. The rule now stops before it starts when the first
sense is a function word. That one guard removed 610 changes and kept every
good one.

**What it costs, stated before it is used.** The rendering now fits the cited
passage *by construction*. So the fit of a page to its passage can never again
be evidence for the decipherment. Gate 2, which measured exactly that and
returned 18.6 sigma, was run on the unfitted rendering and its number stands.
Rerunning gate 2 after this would be circular and must not be done.


**The null control, because a method that cannot fail proves nothing.**
Three gates, each with its bar written down before the run, in
`harness/ktnull.py`. Two pass and one fails, and the failure is the useful
one.

    GATE 1  structurally related signs share a meaning
            2.1% against 0.2% when the glosses are permuted
            5.4 sigma, bar 5                                  PASS

    GATE 2  the folios are about the passages they cite
            27.8% against 16.9% when the folio-to-passage
            assignment is shuffled
            18.6 sigma, bar 5                                 PASS

    GATE 3  the rendering reads like language
            78.3% of adjacent word pairs occur together in
            scripture, against 70.6% for a frequency-matched
            shuffle of the dictionary
            2.3 sigma, bar 5                                  FAIL

Gate 1 clears its bar at ten times chance, but 2.1% is a small number and it
means the structural tools are candidate generators, not readers: an
arbitrary structural neighbour is wrong 98 times in 100, and what made a
reading was the judgment step, which this control does not measure.

Gate 2 is the strongest number in the project. The folios really are about the
passages they are said to be about.

Gate 3 failed and the bar was not moved. The finding underneath it is worth
more than a pass would have been: **a frequency-matched random assignment of
this dictionary already scores 70.6%**, because the commonest signs carry
Lord, God, say, man, and any arrangement of those produces pairs that occur
somewhere in scripture. "It reads like the Bible" is therefore a weak claim
and this project should stop making it. The claim that survives is narrower
and much stronger: it reads like *the particular passage the folio cites*.

**Gate 4, held-out rederivation: one failure and one invalid test, and both
are reported.** `ktrederive.py` masks 10% of Kiraly and Tokai's dictionary and
asks whether the pipeline puts it back.

    GATE 4a  mechanical rederivation, no structural neighbour
             5.4% against 4.6% with the tether cut
             0.2 sigma, bar 5                                FAIL

    GATE 4b  the judgment step, 25 masked signs read blind
             12 of 25, 48%  --  but the test was INVALID

Gate 4a says plainly what the mechanical part of this pipeline can do on its
own: nothing. The top candidate was correct 0.0% of the time in every stratum.
No reading in this project was ever made that way, and this is why.

Gate 4b failed in a more interesting manner. Of the 25 masked signs, twelve
had K&T entries this session had already met in some earlier check; those
scored 75%, and the thirteen that were genuinely unseen scored 23.1%. **A
blind test run by the reader who spent the day reading the dictionary is not
blind.** The 48% is discarded. The declared consequence for the 15-30% band
was applied without argument: 69 passage-read tier C readings were downgraded
to tier D. The percentage of the book read did not move -- it was 80.1% before
and after, because the downgrade is a confidence label, not a withdrawal.

So the judgment step is still the unmeasured part of this work, and it can
only be measured by a reader who has not seen Kiraly and Tokai's dictionary.
That is the cheapest and most damaging external check available, and anyone
may run it: `python ktrederive.py --dump` writes the sample.

Where a hole cannot be read at all, the rendering now carries a fourth class.
A **tier G** word is a guess: chosen by reading the line, its source passage
and its neighbours, marked in the text with a degree sign (`°word`), and
counted separately everywhere. A line containing one is **not** counted as a
line with every word read. That is why two figures are printed -- **81.5%
read, 98.9% complete including guesses** -- and the gap between them, 17.4
points, is exactly how much of the book is being guessed at. It is a large
gap and it is meant to be visible.

The fifteenth, sixteenth and seventeenth tried to work backwards from the passages that
are certainly right. All three failed their gates, the last one on a held-out half after the failure had been diagnosed, so that the retry could not be tuning. But the search that finds those
passages works, and it turned up the parable of the Unmerciful Servant and the
parable of the Lost Sheep on folios nobody had read, each carrying its own
proof: Király and Tokai's dictionary already has a word glossed for the
unmerciful servant, and the Lost Sheep page writes "ninety and nine" the way
Luke writes it.

The fourteenth asked whether unread codes one glyph away from a defined code
are variant spellings. Its gate failed, so none were inferred, and a later
measurement said why: of 4,824 pairs of signs that are both read and differ by
exactly one glyph, only 103 -- 2.1% -- mean the same thing. One glyph of
distance is almost always a different word. What their own dictionary
*declares* is another matter, and declaring is what it does at length: 88
variants their entries mark "var." had been dropped by the loader, and putting
those back took words with a reading to 78.8% at the time.

That turned out to be the largest seam in the project and it was found last.
Their entries are not just headwords: each carries variant spellings,
aggregates, negations, suffixed forms and worked examples, and every one of
those is a glyph string they have already read, usually with the folio and
line attached. Searching every unread sign against every entry body returned
370 signs covering 577 words. Working that list out in one session took lines
fully read from 62.4% to 74.0% and readings graded A from 147 to 458, at the
cost of no guesses at all: the gloss is theirs, the line is theirs. It read
Eve, Isaac, Abel, Noah, Joachim, Lazarus, Zacchaeus, Pilate, James, Michael,
Gabriel, seven spellings of Nazareth and four of Galilee, Capharnaum, Bethany,
Jericho, the Kidron, the crown of thorns, the money changer, the leper, the
paralytic, the host of the Eucharist, and the sign for the book's own author's
name.

Three hundred and fifteen of the 441 written pages are now translated, and two
passages in them settle what kind of book it is. Folios 48 recto and verso are the Reproaches sung on Good
Friday, and folio 52 verso is Longinus, the blind soldier healed by the blood
from the spear, who appears in no gospel. It is a late-medieval devotional
compilation, drawing on liturgy and legend as much as on scripture.

Six hundred and seventy-eight of the signs Kiraly and Tokai leave undefined in
their headword list have now been read, 458 of them at the top grade,
not by any of the seventeen statistical attempts, but by their own method:
guess a sign from a passage whose story is known, then keep the guess only if
it survives every other place the sign occurs. The method is written up in
METHOD.md.

Everything that can be read is rendered, page by page, in
`work/rohonc/translation/`. Each word is marked by how far it reads: one
sense, several senses with theirs first, a composed reading, a declared
variant, or no reading.
It is a rendering of their dictionary over their transcription, not their
translation. Király and Tokai have not published a translation, and this is
not a substitute for one.

Details in [`ROHONC.md`](ROHONC.md), including a first attempt at the
orientation question that failed its own control and was thrown away, and a
third transcription attempted from the scans that failed for lack of
resolution.

## What is left standing

The simplest process that fits: pick each word from the last letter of
the one before, start each line from a small stock of openers, flourish
the last word, fit to the space. No memory, no copying, no message.

## What this does not decide

- **Intent.** The numbers show a process, not a purpose. Deliberate
  fakery, a devotional practice, glossolalia on paper, or something not
  yet imagined would all look the same here.
- **Necessity.** Meaninglessness is *enough* to explain what we measured.
  Nobody has shown it is *required*. A cipher designed to mimic a
  mindless scribe is conceivable, but no one in the 1400s knew what
  such a scribe's statistics looked like, so they could not have aimed
  for them.
- **The pictures and labels.** Only the running text was measured.
  Labels and the circular text were excluded.

## Where things are

- `RESULTS.md` — every number, every table, every correction.
- `harness/` — the code. `gate.py` must pass after any change.
- Five of our own conclusions were overturned by our own follow-up tests.
  All are recorded in `RESULTS.md` section 6, none quietly amended.

Published 2026-09-22 with everything needed to check it, under the DOI in
the README. An earlier version of this file ended "Private for now. Publish if
there is ever a reason to", which is no longer true.
