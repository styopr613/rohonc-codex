# x-ai/grok-4.7

The bar you do not meet is the one that actually settled Linear B, Egyptian, and Maya: a key fixed in advance must predict material that was not used to build it, and the prediction must be checkable against something other than the analyst’s own passage assignments. Ventris was believed after unpublished tablets came out Greek, including morphology he had not stipulated. Champollion and Knorosov had an external crib plus geographic or linguistic confirmation. The modern computational analogue (Snyder, Barzilay & Knight on Ugaritic) scores token-level agreement with an independent gold mapping, against a baseline that includes model selection. Above-chance in-sample fit under a post-selection shuffle is necessary and nowhere near sufficient. You have no unread folios, no known target language, and no locked crib. Nothing below is a request for another consistency statistic on the same fitted glosses.

Circularity already in the reported tests, so you do not rerun them as if they were clean:

- Tests 1, 3, and 4 use folio-to-passage identifications made while translating with the full reading. The target was fitted, then treated as ground truth.
- “Kept only if consistent everywhere” means test 1’s hit criterion was the inclusion criterion. Dropping the discovery folio does not make the other occurrences held-out if those occurrences were required for inclusion.
- Shuffling glosses after selection does not model the search. It cannot support a sigma claim.
- Test 2 is the only external anchor, and 81.6% against 53.2% for K&T’s own headwords is a warning, not a comfort. Beating the author dictionary on its own sentences means the echo rule is loose or the glosses were fitted to those sentences. Striking “evidence mentions” does not strike analyst memory.
- Zero conflicts with K&T is entailed by the keep-rule.
- Test 7’s 34 sigma at 8.4% absolute accuracy means the seed usually names the wrong passage. Any test that conditions on “the” passage is conditioning on a miss.
- Test 5 already estimates the single-line procedure at about 17% strict. The 848 guesses are noise under your own instrument. The 926 readings differ from those guesses by a consistency filter that was also the evaluation filter.

Bars below are declared here, before any rerun.

### 1. Replay the search on a null corpus
What it measures: whether “consistent reading” and your downstream sigmas are produced by the search itself.

Control: two nulls, same inclusion rule written down as an algorithm before you run it. (a) Permute sign tokens within each folio, preserving unigram frequencies. (b) Rotate passage assignments by a pre-registered offset so folio *i* receives folio *i+17*’s passage. On each null, run the identical candidate-stem search you ran on the real book — not a shuffle of glosses you already chose. If the original search was human and unlogged, you cannot reconstruct it; the mechanical proxy is then: for every sign with ≥3 occurrences, assign the stem that maximises cross-occurrence presence in the cited passages, and keep it only if it hits every occurrence.

Failure: either null yields at least half as many kept readings as the real book, or readings extracted from a null still beat their own shuffled glosses by ≥5 sigma on test 1 or test 3. Either result voids the published sigmas. Absence of a search log is itself a fail on any claim that the null was matched to the procedure.

Data: transcription, the Bible and legend texts actually searched, occurrence index, written keep-rule, and the search log if it exists.

### 2. Passage identification from K&T alone, against decoys
What it measures: whether the folio-to-passage map is recoverable without your 926 readings. If it is not, tests 1, 3, and 4 have no external target.

Control: score each folio, using only the 841 K&T glosses, against every chapter-scale candidate in the corpus you searched. Decoys are not random chapters: for each folio take the passage that maximises overlap on the 50 most frequent biblical stems and is not the assigned passage, plus a length-matched passage from a different genre. Also rank under K&T glosses shuffled once, seed fixed in advance.

Failure: median rank of your assigned passage worse than the top 5% of candidates, or your assignment fails to beat the frequency-matched decoy on a sign test at p<0.01. Report absolute top-1 accuracy beside any sigma. A 34-sigma result with single-digit accuracy is a fail on this test regardless of sigma.

Data: K&T dictionary only, sealed folio-passage table, full candidate corpus. Your readings may not be consulted until scores are frozen.

### 3. Rare-stem, non-parallel retest
What it measures: whether confirmation survives once common stems and synoptic double-counting are removed. “God” or “said” sitting in a gospel chapter is cheap. Matthew and Luke retelling the same pericope are one event, not two.

Control: freeze the passage map from test 2, not from your translation. Collapse occurrences whose citations are synoptic or legend parallels of one pericope into a single trial. Score only stems in the bottom quartile of frequency in the candidate corpus. Shuffle glosses inside that frequency band.

Failure: rare-stem hit rate within 3 sigma of that shuffle, or absolute hit rate under 15%. Common-stem hits do not count and must not be pooled back in after a fail.

Data: pericope alignment of every citation, stem frequencies computed on the candidate corpus only, occurrence lists marked by which folio was used to propose the gloss.

### 4. Strict rescore of the only external test
What it measures: whether test 2 is anything other than synonym-tolerant echo of sentences the analyst had read.

Control: a coder who has not read your commentary scores a hit only if the lemma itself is in K&T’s English, synonyms pre-registered as non-hits. Shuffle control as you already defined it. Separately, a second reader who has K&T’s dictionary and those sentences, and does not have your glosses, proposes the unread signs.

Failure: strict hit rate under 40%, or under 3 sigma over shuffle. Also a fail if your readings beat K&T’s own headwords by more than 10 points under the strict rule: that pattern means leakage, not superiority. Independent re-gloss agreement with you under 30% on those signs means the sentences do not determine your reading.

Data: K&T’s translated sentences, token alignment, your glosses in those sentences, two people who were not the translators.

### 5. Locked next-folio prediction
What it measures: the Ventris criterion. In-sample CV that hides signs but keeps a passage map built with those signs does not.

Control: pre-register a folio order. Derive passage IDs and glosses from the first half only, by the written rule, without opening the second half’s passage notes. Predict for each withheld folio the passage identity and the multiset of content stems. Baseline: K&T-only prediction from test 2, and a shuffle of training glosses.

Failure: content-stem F1 within 3 sigma of the shuffle, or passage top-1 no better than the K&T-only baseline. Reusing glosses already chosen on the full book is leakage and does not count as running this test. If every folio has already been translated, the honest version is a new analyst, or image pages whose transcription you seal before alignment — not a resimulation.

Data: a runner who does not know the withheld passage IDs; the written derivation rule; sealed predictions dated before unsealing.

### 6. Underdetermination census
What it measures: how often your keep-rule identifies a gloss, as opposed to licensing one.

Control: on the test-2 frozen map, for every A/B sign with ≥3 independent (post-collapse) occurrences, list every stem present in all of its passages. Chance rate of a stem surviving all passages is estimated by assigning random stems of matched frequency.

Failure: more than 40% of A/B signs have a second stem, not a morphological variant of the chosen one, that also satisfies the keep-rule. Those signs are not deciphered. They must be dropped and line-coverage recomputed. A companion count: fraction of kept glosses that were the unique content word in a slot bracketed by K&T words. If most “readings” are the only biblical word that fits the hole, you have Mad-Libs, and consistency across holes of the same shape is not independent evidence.

Data: passage texts, occurrence index, a declared variant-stem list frozen before the count.

### 7. Verbatim-formula crib
What it measures: the genre claim, which is stronger than bag-of-stems overlap and should be easy if true. A Catholic paraphrase book of this length should contain at least one near-verbatim formula.

Control: pre-register ten formulas (Pater Noster, Ave Maria, Sign of the Cross, Nicene incipit, John 1:1–5, Genesis 1:1, the crucifixion titulus, and three more you name before searching). Search the lemma rendering for the best window. Decoys, also pre-registered: the same formulas reversed, and ten length-matched passages from a non-biblical narrative corpus. Shuffle of your glosses is a second null.

Failure: no formula reaches lemma F1 above 0.6 across 12 consecutive tokens, or the best biblical formula does not beat the best decoy. Do not search and then choose the formula.

Data: lemma rendering with your A/B readings and, separately, with K&T only; formula list locked before the search.

### 8. Blind illustration test
What it measures: an evidence channel that is not the biblical text you fitted.

Control: an art historian labels every illustration from a fixed scene inventory, with no access to any gloss. Pre-tag which of your nouns are depictable (cross, tomb, star, manger, sword, devil) before seeing labels. Positive control: the same association test on K&T glosses. Null: depictable glosses shuffled among content nouns.

Failure: K&T’s association is real (odds ratio >2, p<0.01) and yours is inside the shuffle. If K&T also fails, the pictures do not carry word-level information and the test is inconclusive, not a pass. Any sign whose gloss you assigned by looking at the picture is excluded before scoring; if you cannot identify those signs, the whole channel is contaminated and this test cannot be claimed.

Data: image-to-folio alignment, which you do not yet have and must build blind to the reading; labels; the depictable list.

### 9. Productive structure, or an explicit logographic concession
What it measures: whether the glosses are a language rather than a stem bag. Constructed languages are more regular than natural ones, so “possibly constructed” does not weaken this.

Control: from gloss pairs differing by one grammatical feature, extract the sign-string difference and apply it to signs not used to infer the rule. Null: random edits of the same length. If you pre-register pure logography, the branch changes: a determinative or shape class must predict gloss semantic class on signs not used to define the class, against a shuffle of class labels.

Failure: both branches at shuffle. You do not get to skip the test by leaving the language unnamed.

Data: sign strings aligned to glosses; the pre-registered choice of morphological versus logographic branch.

### 10. Transcription audit on the unmapped images
What it measures: whether the occurrence index is about the object. Every test above inherits the ~2,900-type transcription.

Control: thirty pages chosen by a random seed, glyphs clustered by someone who does not have the transcription, then aligned. 

Failure: more than 5% of tokens would change gloss under the image clustering, or more than 10% of A/B readings depend on a sign split the images do not support. Until this is done, sigmas computed on the transcription are conditional on an unchecked copy.

Data: the low-resolution images, a blinded alignment to folio and line, the transcription.

Run 1 and 2 before anything else. If 1 fails, the sigmas you have published do not discriminate a decipherment from a search. If 2 fails, tests 1, 3, and 4 have no target that is independent of the glosses being tested. 4 is the only retest of an external anchor and should be rescored under the strict rule even if you dispute the rest. 5 is the standard; declining it because all 441 folios were already used concedes that the standard has not been met.