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
there are two numbers and one of them is much weaker. **96.4% of the words now
have *a* reading, and 80.1% of the lines have every word read.** The second is
the one that matters: a sentence with one unreadable word in it is not a
sentence you can read. It stood at 2.8% before any of this, at 62.4% on the
morning of 2026-09-20, and at 74.9% on the morning of 2026-09-21.

Even the word figure overstates how much is understood. Only about one word in
eight has a single meaning with no choice to make; most carry several senses
each, and the rule for choosing between them is in the grammar paper Kiraly
and Tokai have not published.

**What moved it from 74.9% to 80.1% was not more reading of lines. It was three
small instruments that read the dictionary instead.** Each asks a mechanical
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
two lines above ours on the same folio modifying the same phrase, and which
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

**What the 80.1% is made of.** A percentage without a tier distribution
behind it is a claim, not a result. `ktprov.py` computes this and reads none
of the prose of the evidence field -- every class is worked out from the sign
itself against Kiraly and Tokai's dictionary, so a reviewer can rerun it.

    THE WHOLE RENDERING, WORD BY WORD          29,997 words

      K&T's dictionary, unchanged              17,673   58.9%
      by composition of signs they read         7,617   25.4%
      this project, anchored on a K&T entry     1,871    6.2%
      this project, anchored on a reading
        of its own                                277    0.9%
      this project, read from a passage         1,457    4.9%
      a tagged guess                               15    0.1%
      no reading                                1,087    3.6%

    THIS PROJECT'S 891 READINGS, BY TIER

      A  survives every occurrence, or proved by an identical
         formula, a numeral, or K&T's own citation          462
      B  survives most occurrences                          178
      C  one passage, or source-checked                     238
      D  a single occurrence, read from one line              5
      G  a guess, never counted as read                       8

    THE SAME READINGS, BY WHERE THE WORD CAME FROM

      anchored on a K&T entry        502 signs  56.3%
        of which: holds one of theirs whole 257,
        one glyph from one 171, sits inside one 74
      anchored on a reading of ours   91 signs  10.2%
      read from a passage            290 signs  32.5%
      a tagged guess                   8 signs   0.9%
      judgments flagged as such in the evidence: 4

**Two thirds of this project's readings are co-signed by the published work**
-- they were got from Kiraly and Tokai's own entries by decomposition, by
containment or by a single-glyph match, so the word is theirs and only the
placement is ours. The 290 read from a passage are the ones that stand or fall
on this project's evidence alone, and they are the ones a reviewer should go
at first.

Where a hole cannot be read at all, the rendering now carries a fourth class.
A **tier G** word is a guess: chosen by reading the line, its source passage
and its neighbours, marked in the text with a degree sign (`°word`), and
counted separately everywhere. A line containing one is **not** counted as a
line with every word read. That is why two figures are printed -- 80.1% read,
80.5% complete including guesses -- and the gap between them is exactly how
much of the book is being guessed at.

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

Three hundred and two of the 441 folios are now translated, and two
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
translation, and it stays private with the rest of the work.

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
- `VOYNICH_PLAN.md` — the plan and the survey of prior work.
- Five of our own conclusions were overturned by our own follow-up tests.
  All are recorded in `RESULTS.md` section 6, none quietly amended.

Private for now. Publish if there is ever a reason to.
