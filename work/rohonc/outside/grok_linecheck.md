# Question

I want an independent critique of a proposed test before it is run. Be blunt. If it is badly designed or pointless, say so and say why.

CONTEXT. The Rohonc Codex is a 448-page manuscript in an unknown logographic script. Király and Tokai (K&T, Cryptologia 2018) published a dictionary of 841 glossed signs and argue it is a paraphrase of Christian scripture. A project extended their dictionary. Current coverage of the 29,997 word tokens:
- read by K&T's own dictionary (one sense, several senses, compositions, their variant spellings): 82.1%
- this project's added readings, tiers A and B (670 signs): 11.6% of tokens
- this project's bracketed guesses, tier G: 3.3%
- unread: 0.2%

How a tier A/B reading is made: each folio has a cited Bible passage (chapter and verse). For an unread sign, a reader looks at its lines rendered in K&T's English words, takes candidate words from the cited passage (minus words K&T already assign to other signs), picks one, and keeps it only if it is consistent at every other occurrence of the sign.

Relevant tests already run (bars declared before each run):
- Test 1: on folios not used to choose a reading, the reading's word appears in that folio's cited passage 25.5% of the time; K&T's own words 26.0%; shuffled glosses 5.5%. PASS.
- Test 3: 25 of K&T's own entries hidden; a fresh reader with the rendered lines, the chapter and verse and the passage's free words guessed them: 4 of 24 strict (16.7%), about 7 of 24 lenient.
- Test 13: for 95 A/B signs whose folios cite 3+ distinct chapters, 62 (65.3%) have some other common word (answer, tell, enter, depart...) present in every cited chapter; bar was 40%, FAIL. But 0 of the 95 chosen glosses themselves pass that chapter rule, so the rule is not the one that made the readings. The census did not ask whether a rival word fits the sign's actual lines.
- Test 14: an outside reader filling gaps on pages given the right vs a deliberately wrong passage: 3.8 fills per page vs 0.0; said "matches" 13/18 vs 0/20.
- Test 15/17: an outside reader named the cited chapter on 9/20 pages from K&T's words alone vs 0/20 when the words were shuffled among signs; asked by folio number alone it knew 0/20.

PROPOSED TEST ("line check"). Sample tier A/B readings. For each, take its lines on folios named in its evidence, rendered in K&T's words plus the other readings, with the target sign blanked, plus the folio's cited verses. Offer an outside model k candidates in random order: the chosen gloss plus k-1 rivals drawn from the same cited passage's free words (the same pool the method drew from). Ask which fits the blank. Chance = 1/k. PASS if the chosen gloss is picked at >= 2x chance, binomial p < 0.01.

QUESTIONS.
1. Does this test make sense? What would a PASS and a FAIL actually show?
2. Is it circular, given that the readings were chosen by a reader looking at the same lines and passage? Does agreement show truth, or only that the choice is reproducible?
3. How should the rivals be drawn so the test is fair (frequency matching, part of speech, excluding near-synonyms)?
4. Would held-out occurrences (lines not used to choose the reading) be the right target instead?
5. Is there a better test of whether these readings are identified by their lines rather than merely licensed?
6. What bar would you set, and what sample size?


# Grok 4.7 reply

The test is not worth running as specified. A PASS would be the expected result of the selection process, not evidence the glosses are right. It asks whether a second reader, handed the same lines, the same verses, and a weaker shortlist, repeats a cloze choice that was already optimized on those lines. That is reproducibility of an English fill-in-the-blank. It is not identification, and it is not truth.

### 1. What PASS and FAIL would actually show

PASS would show only this: among the chosen gloss and some other unused words from the cited passage, an outside reader prefers the word a previous reader already picked to fit those same lines. That is likely whenever the distractors are grammatically or collocationally worse, which random “free words” usually are. It does not show the sign means that word. It does not show the line did the work rather than the verse. It does not beat the null that both agents are competent English speakers doing the same task. A fabricated decipherment that always picks the most obvious passage word for the gap would pass too.

FAIL would show that the chosen gloss is not even the obvious completion of the evidence lines. That hurts the claim that the lines identify the word. It does not refute “licensed and not contradicted,” and it may not refute truth either. Test 3 already found that a fresh reader with the lines, the verse, and the free words recovered only 4 of 24 hidden K&T entries strict. If stipulated readings often lose a cloze, cloze-losing is not a validity criterion for this text. So FAIL is ambiguous, and the result you would treat as success is the one that means least. That is a bad test.

Two further defects make a PASS cheap:

- Chance is not 1/k unless rivals are exchangeable with the chosen gloss. They will not be. Binomial p against 1/k is then anti-conservative, and it gets worse because lines share folios, passages, and other project readings. Those are not independent trials.
- The bar “≥ 2× chance” loosens as you add bad distractors. At k=2 it demands 100%. At k=10 it demands 20%. A design whose pass line gets easier as the foils get worse is not a design.

### 2. Circularity

Yes. The gloss was kept because it fit these lines and this passage. Scoring those same evidence lines measures whether you succeeded at the task you optimized, plus whether a second judge agrees. Agreement shows the choice is reproducible, not that it is correct.

It is worse than ordinary resubstitution. The rendering includes other A/B readings fit to the same passages, so the context is jointly optimized. “Folios named in its evidence” are the folios already selected as support. Giving the cited verses hands the judge the source the original reader used. An LLM is a particularly bad judge here: it completes biblical English from the verse, and it may have seen K&T. You would be scoring the translation layer, not the script.

Test 1 was the non-circular check (word in the passage on folios not used to choose it: 25.5% vs 5.5% shuffled). This proposal walks back from that toward the fitting set. Also note what Test 1 implies: “consistent at every occurrence” does not mean the gloss is in each cited passage. Passage membership on unused folios is only about one in four. These readings are mostly licensed by a loose semantic judgment, not pinned by the citations.

### 3. Rivals

Drawing k−1 random free words and calling the null 1/k is not fair. Many will be illegal in the blank (“the ___ of God” will not take a numeral or “said”). The model will discard them, and the true chance among surviving options will be far above 1/k.

If you run any forced choice:

- Match part of speech and the inflectional slot the blank actually licenses. Match rough frequency in the passage.
- Drop near-synonyms from the primary contrast. English context often cannot separate them, and a win over a synonym is not identification.
- Prefer the original runner-up, if it was recorded before the gloss was locked. That is the only rival that matters. A shortlist rebuilt after the fact is hindsight.
- Include one high-frequency attractor (said, God, lord) as a named control, so you can see pure biblical collocation.
- Do not claim a theoretical null. Estimate it by rotating glosses among matched signs, or by rescoring the same candidate sets after the line is shuffled. If you cannot build exchangeable rivals, you do not have a 1/k test.

Matching on features the original reader already used does not create new evidence. It only stops you from laundering those features as confirmation.

### 4. Held-out lines

Necessary, not sufficient. And you probably do not have them. “Kept only if consistent at every other occurrence” means every occurrence was inspected. Rescoring those lines is not holdout. Calling a subset “evidence” and the rest “held out” after both were looked at is still resubstitution.

A real holdout is prospective: lock the gloss from a discovery subset before anyone reads the holdout folios, then score one precommitted unseen occurrence per sign. Even then, withhold the holdout folio’s verse. If the gloss wins only when the verse is shown, the verse licensed it and the line did not identify it.

Hapaxes cannot be identified by cross-occurrence at all. A one-line reading chosen to fit that line is only licensed, and no check on that line can promote it. Stratify by occurrence count. If most of the 670 signs are hapaxes or dis legomena, most of the extension is unfalsifiable by this family of tests, and the sample size for a real test may not exist.

### 5. Better test

The quantity you want is the incremental value of the line over the verse, on occurrences not used to choose the gloss, against a null from the same pipeline — and it has to be calibrated on readings you are treating as known.

Do that, or don’t bother:

1. Line-only vs verse-only vs both, on true holdout lines. Candidates are POS-matched, not random. Primary estimand: accuracy(line, no verse) minus the permutation null, and accuracy(line+verse) minus accuracy(verse only). The second difference is “identified rather than licensed.” If the line adds nothing once the verse is shown, the readings are licensed.
2. Same protocol on hidden K&T entries. This is mandatory. Test 3 says the method barely recovers them (4/24 strict, ~7/24 lenient). If K&T glosses fail your bar and A/B glosses pass, that is evidence the new readings were selected for cloze-obviousness, not evidence they are right. A criterion that known entries fail is the wrong criterion. Do not invert that.
3. Specificity: build pseudo-readings with the same reader rules on shifted or wrong citations, and require that they fail the same bar. Test 14 (3.8 fills vs 0.0; “matches” 13/18 vs 0/20) is encouraging but is a different task. “Can you fill a gap?” is not “does a precommitted gloss beat matched rivals?”
4. Unit is the sign, one vote each. Permute within sign, or use a sign-level permutation test. Do not binomial-test lines.

I would not use an open “which word fits?” judged in English as proof of a logographic reading. At best this family of tests can show constraint. It cannot show the paraphrase is the text.

### 6. Bar and sample size

Drop “≥ 2× chance.” Pre-register a sign-level permutation test, alpha 0.01, on the line-minus-verse increment, plus the K&T calibration and the shifted-citation control. A useful bar is something like a +15 point increment of line+verse over verse-only, and line-only above the matched permutation null by a similar margin, with the same protocol not failing on K&T while passing on A/B. If the K&T increment is ~0, stop using cloze as a gate.

Power is secondary to bias, but for orientation: detecting 50% vs a true null of 25% at one-sided alpha 0.01 and 80% power takes on the order of 30–40 independent signs. Dependence and a harder contrast push that up. I would want all eligible signs with at least one unseen occurrence, and I would not claim anything about the 670 unless at least ~50 signs are actually eligible. If fewer exist, the finding is that the extension cannot be checked this way. Do not pool hapaxes in to inflate n. Do not optional-stop. Separate tier A from tier B.

Test 13 is the more honest result you already have: for 95 A/B signs, a generic word sits in every cited chapter 65% of the time (bar 40%, fail), and 0 of the 95 chosen glosses themselves meet that chapter rule. The citation environment is full of alternative words, and the chosen glosses are not stable across the cited chapters. A line check on the fitting set would be a way to paper over that. It would not answer it.