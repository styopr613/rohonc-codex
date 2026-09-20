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

Finishing the translation was attempted three ways and failed three times,
each against a bar set before running. The four words in ten the dictionary
does not reach cannot be recovered from the gospels by alignment with the tools
here. That is the honest state: the reading is very probably right, and the
part that is still missing is the part its authors are still working on.

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
