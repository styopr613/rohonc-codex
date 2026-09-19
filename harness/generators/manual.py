"""voynich-fingerprint's hand-executable scribal procedure.

Eight short tables and a die: the smallest procedure the repo could find that a
person with a quill could actually carry out, as against its five-component
model which needs rejection sampling on a joint distribution and a 151-row
table. It is in the table because "a machine can match the statistics" and "a
medieval scribe could have matched the statistics" are different claims, and
only the second one is about the manuscript.
"""
import json
import os
import random
import sys

import corpus
import layout
from . import register

FP = os.path.join(corpus.ROOT, "refs", "voynich-fingerprint", "analysis")
if FP not in sys.path:
    sys.path.insert(0, FP)

RESULT = os.path.join(FP, "SCRIBE_RESULT.json")


@register("manual", kind="self", label="hand-executable manual (fingerprint)",
          note="tables + a die; parameters from its own SCRIBE_RESULT.json")
def generate(spec, train, seed=0):
    from scribe_method import Manual, make_scribe, scribe_document
    res = json.load(open(RESULT, encoding="utf-8"))
    tw = corpus.words(train)
    man = Manual(tw, n_forms=res["n_forms"], merges=140)
    write = make_scribe(man, p_pair=res["p_pair"], p_reuse=res["p_reuse"])
    widths = [b for p in spec for b in p.budgets]
    para_lens = [p.n_lines for p in spec]
    doc = scribe_document(write, len(widths), widths, para_lens,
                          random.Random(seed + 11), gallows_p=res["gallows_p"])
    return layout.from_paras(spec, doc), {"params": "SCRIBE_RESULT.json"}
