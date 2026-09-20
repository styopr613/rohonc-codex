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

Finishing the translation was attempted thirteen ways. Ten failed, each
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

It is worth being exact about what "78% of the book" means, because it is the
weakest of three numbers. It means 78% of the words have *a* reading. Only
11.5% of them have a single meaning with no choice to make; the rest carry
several senses each, and the rule for choosing is in the grammar paper Király
and Tokai have not published. The number that matters most is lines: a
sentence with one unreadable word in it is not a sentence you can read, and
the share of lines where every word has a reading went from 2.8% to 20.6%.

So the obstacle has moved rather than gone. It used to be missing vocabulary.
It is now missing grammar, and that is theirs to publish.

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
