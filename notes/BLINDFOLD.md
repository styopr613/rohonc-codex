# THE BLINDFOLD TEST

**One command, about an hour, and it is the only check this project cannot
run on itself.** If you have been asked to run it, you are probably a fresh
session or a person who has not worked on this manuscript. That is exactly
the qualification required. Do not read up on it first.

## What you are testing

The Rohonc Codex is a 16th-century manuscript in an unknown script. Two
Hungarian scholars, **Levente Király and Gábor Tokai**, published a partial
solution: a dictionary of signs and their meanings. This project extended
their dictionary by a few hundred signs, using tools that propose candidate
meanings and a human reader who chooses between the candidates.

Everything in that pipeline has been measured **except the reader**. Nobody
has ever scored whether the choosing step finds the truth or merely finds
something consistent. That is what you are here to measure.

## The method

The test hides a random sample of Király and Tokai's **own** dictionary
entries — words whose true meaning is known but is not shown to you — and
asks you to read them from the same evidence the pipeline gives. Then it
reveals the answers and scores you.

## What to do

```bash
cd /home/ubuntu/voynich/harness
python3 ktblind.py --new
```

This writes a file of **25 signs**. For each one you get:

- every line of the manuscript the sign appears on, with the other words
  rendered in English
- the chapter and verse that folio is believed to cite
- the words of that passage that no other sign has claimed
- any sign in the dictionary that this one sits inside, contains, or is
  one glyph away from

Write your best single English word or short phrase on each `READING:`
line. Then:

```bash
python3 ktblind.py --score ../work/rohonc/blindfold_<seed>.txt --seed <seed>
```

## The rules, and they matter

1. **Do not look at the dictionary.** Not `data/rohonc/kt/`, not
   `proposals.json`, not the translation in `work/rohonc/translation/`, not
   `ROHONC.md`. The whole value of the test is that you have not seen the
   answers. Grepping for a sign's hex code anywhere outside the sample file
   destroys the run.
2. **Commit every reading before scoring.** Fill in all 25, then score once.
   Do not score, look, and revise.
3. **Leave a line blank if you genuinely cannot read it.** A blank is scored
   as a non-attempt, not a miss, and that is more useful than a wild guess.
4. **Do not tune anything afterwards.** Report the number you got.

## How it is scored, and what the number means

A hit is a shared content word-stem with Király and Tokai's gloss. The rule
is strict and it will punish a right answer in the wrong English — *pence*
was scored a miss against their *denarius*. Report the strict score. If you
want, also report how many you think were semantically right, marked
separately as your own judgment.

The consequence bands were declared before this test was ever run and they
bind whatever the result:

| recovery | what follows |
|---|---|
| 50% or more | the judgment step does real work; the project's tier C readings stand as written |
| 30–50% | it adds something; tier C means "more likely than not" and no stronger |
| 15–30% | it adds little; passage-read tier C readings should be downgraded to tier D |
| under 15% | the passage-read class should be withdrawn wholesale |

## What happened when this project ran it on itself

It scored 12 of 25, **48%** — and the run was thrown out. Twelve of the
twenty-five signs were ones that session had already met while working. Those
scored **75%**. The thirteen genuinely unseen ones scored **23.1%**. A blind
test run by someone who has read the dictionary is not blind, so the 48% was
discarded, the 23.1% was taken as the estimate, and the declared consequence
was applied: 69 readings were downgraded from tier C to tier D.

That correction is why your run matters. Thirteen signs is a very wide
interval, and yours will be the first genuinely clean measurement.

## Report back

Four things: **the seed**, **the strict score**, **the 25 readings you
committed**, and **anything the evidence gave you that felt like a
giveaway** — the last is how the test itself gets better.
