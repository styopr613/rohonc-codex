# google/gemini-2.5-pro

As an outside reviewer, I propose the following independent tests, ranked from most to least likely to falsify the decipherment. These tests are designed to break the existing circularity where the project's folio-to-passage identifications underpin the validation of the readings derived from them.

---

### **Proposed Independent Tests**

**Test 1: Independent Folio-to-Source Identification**

*   **What it Measures:** The objectivity and reproducibility of the core claim that specific folios are paraphrases of specific biblical or apocryphal passages. This directly attacks the central circularity of the project.
*   **Control:** The project's existing list of folio-to-passage mappings. The null hypothesis control is a random mapping, which should show near-zero correlation.
*   **Failure Criterion:** An independent expert (or panel of experts in theology and medieval iconography), given high-resolution images of the manuscript folios (especially the illustrations) and the corpus of potential source texts, produces a set of mappings that has a low or statistically insignificant correlation (e.g., <25% agreement on specific chapter/verse assignments) with the project's mappings.
*   **Data Needed:**
    1.  High-resolution, unannotated images of all manuscript folios.
    2.  The complete corpus of source texts used by the project (e.g., Vulgate, specific apocrypha, Golden Legend versions).
    3.  The project's final list of folio-to-passage mappings (to be used only for comparison *after* the independent test is complete).

**Test 2: Predictive Decipherment of a Held-Out Folio (The "Bilingual" Test)**

*   **What it Measures:** The decipherment's predictive power, the gold standard for any successful decipherment. It simulates the discovery of a new bilingual text.
*   **Control:** A "translation" of the same held-out folio generated using a dictionary where the project's 926 new readings have their glosses shuffled.
*   **Failure Criterion:** The translation produced by the project's full dictionary is judged by a blind panel to be no more semantically similar to the true source text than the shuffled-gloss control. A stronger failure would be if the panel cannot match the project's translation to its correct source from a list of 10 plausible (but incorrect) source passages.
*   **Data Needed:**
    1.  A single, randomly selected folio designated as "held-out." Its identity is known, but its proposed source text is kept secret from the project team.
    2.  An independent expert must first identify the source text for this folio (as in Test 1). This provides the "ground truth."
    3.  The project team is then given the folio's text and asked to produce a line-by-line translation using their full, finalized dictionary.

**Test 3: Grammatical and Morphological Coherence**

*   **What it Measures:** Whether the deciphered text exhibits plausible linguistic structure, specifically morphological marking (e.g., prefixes/suffixes for tense, plurality, case) that is consistent and non-random. A true decipherment should reveal a language system, not just a sequence of correctly-guessed content words.
*   **Control:** The same analysis performed on a version of the text where glosses are randomly shuffled within each line. This preserves local word frequencies but destroys syntax and morphology.
*   **Failure Criterion:** Proposed grammatical markers fail to correlate with the grammatical categories of the words they attach to at a rate significantly above the shuffled control. For example, if a sign proposed as a plural noun suffix appears attached to verbs, adverbs, or already-plural nouns as often as it does to singular nouns.
*   **Data Needed:**
    1.  The full, tokenized manuscript text.
    2.  The complete dictionary (K&T + project) with any proposed grammatical functions for specific signs.
    3.  A part-of-speech-tagged version of the full translated text.

**Test 4: Illustration-to-Text Congruence (Independent of Source)**

*   **What it Measures:** The correspondence between the visual information in the illustrations and the semantic content of the *project's translation* of the text on the same folio, without reference to the proposed biblical source. This uses the illustrations as an independent data channel.
*   **Control:** For each folio, a lineup consisting of the project's translation for that folio and 5-10 "foil" translations from other, randomly selected folios.
*   **Failure Criterion:** A blind reviewer (an art historian or theologian), when shown a folio's illustration, cannot select the correct corresponding text translation from the lineup at a rate significantly better than chance.
*   **Data Needed:**
    1.  High-resolution images of all illustrated folios.
    2.  The project's full, line-by-line English translations for all folios.

**Test 5: The K&T "Poison Pill" Test**

*   **What it Measures:** Whether the project's new readings are semantically and grammatically compatible with the higher-confidence, independently-derived sentence translations from K&T. It tests if the new puzzle pieces break the parts of the puzzle already considered solved.
*   **Control:** The original K&T translations, which serve as the baseline for coherence. A second control involves inserting randomly selected (shuffled) project glosses into the same slots.
*   **Failure Criterion:** A significant portion (>20-25%) of the newly "completed" K&T sentences are flagged as nonsensical, contradictory, or grammatically malformed by a blind linguistic reviewer, compared to a near-zero baseline for the original K&T sentences.
*   **Data Needed:**
    1.  The full set of K&T's example sentences (Rohonc text and English translation).
    2.  The project's specific readings for signs that appear within those K&T sentences.

**Test 6: Cross-Linguistic Frequency Profile**

*   **What it Measures:** Whether the frequency of concepts in the deciphered text aligns with the frequency of those same concepts in the claimed source texts. A paraphrase should roughly preserve the topical focus.
*   **Control:** The frequency profile of a "shuffled" decipherment, where the mapping from sign to gloss is randomized.
*   **Failure Criterion:** The vector of concept frequencies (e.g., frequency of "God," "angel," "sin," "tree") in the project's translation shows a low or insignificant correlation with the frequency vector of the same concepts in the proposed source corpus (Vulgate, etc.). The correlation should not be significantly higher than that achieved by a simple bag-of-words model based on the illustrations alone.
*   **Data Needed:**
    1.  The full translated text from the project.
    2.  The full text of the proposed source corpus.
    3.  A pre-defined list of ~200 key theological and narrative concepts to be counted.

---

### **Comparison to Historical Decipherment Standards**

The gold standard in historical decipherment (Linear B, Maya Glyphs) is **predictive validity confirmed by external evidence.**

*   **Linear B:** The decipherment by Ventris was confirmed when a newly discovered tablet from Pylos, which had not been used in the decipherment, was read using his system and produced a sensible inventory of tripods and vases that matched the tablet's ideograms. This is the principle behind my proposed **Test 2**.
*   **Maya Glyphs:** Progress relied heavily on "bilinguals" in the form of dates (matching the Long Count calendar to the Gregorian calendar) and names/places that could be tied to external king lists or archaeology. This is the principle behind **Test 1** (reproducing the link to a "known" source) and **Test 4** (using illustrations as an external data source).
*   **Egyptian Hieroglyphs:** The Rosetta Stone was a true trilingual text, providing the ultimate external key.

The project's current tests, while showing impressive internal consistency, largely fail to meet this external standard. Tests 1, 3, and 4 as described in the prompt are circular because the "ground truth" (the folio-to-passage mapping) was generated by the same process it is being used to validate. Test 2 (checking against K&T sentences) is the strongest existing test as it uses an external baseline. However, it only validates a subset of readings.

To be considered successful by the standards of the field, the decipherment must pass a test equivalent to **Test 1** or **Test 2** above. Failure on Test 1 would invalidate the methodology's foundation; failure on Test 2 would prove the resulting dictionary lacks predictive power, a fatal flaw for any claimed decipherment.