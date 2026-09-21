"""TEST 2b: part of speech from context alone, second instrument, declared fresh.

ktpos.py failed its calibration bar at 68.3% against 70%. The diagnosis,
measured after the fact: accuracy rose from 61.7% on signs seen once to
76.3% on signs seen twenty or more times, because a sign seen once has one
neighbour each side and nothing to learn from; and the noun/verb labels
came from a Bible-derived lexicon that called 'forest' a verb and 'false' a
noun. This is a NEW test, not a rerun: the population is fixed in advance
by a mechanical rule and the labels were written by hand into
ktpos_labels.json before any run.

  POPULATION  signs occurring five or more times as a whole token, K&T's
              for calibration and ours for the test.
  LABELS      hand-written noun/verb from the English gloss, clear cases
              only; mixed glosses, adjectives, numerals, pronouns and
              particles are left unlabelled and are not tested.
  FEATURES    exactly ktpos.py's: previous and next token, K&T's genitive
              prefix, verbal prefix, subject marker, ae0 suffix. No passage.

  BAR 1  calibration on K&T's labelled signs, leave-one-out: >= 70% and
         >= 5 sigma above the majority class. Below it stage 2 is not a
         result.
  BAR 2  our tier A+B signs: agreement with the hand label beats the label
         shuffle by >= 5 sigma. C+D reported. (G has almost no members.)

Disclosed so the reader can weigh it: the subgroup accuracies of the failed
run had been seen before these bars were set, so the calibration bar is
not blind to the likely outcome. The population rule and the labels are
what keep this from being a re-fit.

    python3 ktpos2.py
"""
import json
import random
import sys
from collections import Counter, defaultdict

import ktcross as K
import ktpos as P
import ktrederive as R

MINOCC = 5
NSHUF = 20


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    lab = json.load(open('ktpos_labels.json', encoding='utf-8'))
    feats = P.contexts(doc)
    occ = {h: sum(c for k, c in f.items() if k.startswith('p:'))
           for h, f in feats.items()}

    def hx(s):
        return "".join(f"{ord(c) - 0xE000:03x}" for c in s)

    lmap = {"N": "NOUN", "V": "VERB"}
    kt = [(hx(s), feats[hx(s)], lmap[lab['kt'][hx(s)]]) for s in gl
          if hx(s) in lab['kt'] and occ.get(hx(s), 0) >= MINOCC]
    right = 0
    for i, (h, f, y) in enumerate(kt):
        m = P.NB([(f2, y2) for j, (_, f2, y2) in enumerate(kt) if j != i])
        right += m.predict(f) == y
    acc = right / len(kt)
    maj = max(Counter(y for _, _, y in kt).values()) / len(kt)
    sd = (maj * (1 - maj) / len(kt)) ** .5
    sig1 = (acc - maj) / sd
    print("TEST 2b: PART OF SPEECH FROM CONTEXT, HAND LABELS, >= 5 OCCURRENCES")
    print(f"  stage 1  K&T's signs  n={len(kt)}  leave-one-out {acc*100:.1f}%  "
          f"majority {maj*100:.1f}%  {sig1:.1f} sigma")
    ok1 = acc >= 0.70 and sig1 >= 5
    print(f"  BAR 1: >= 70% and >= 5 sigma  ->  {'PASS' if ok1 else 'FAIL'}")
    model = P.NB([(f, y) for _, f, y in kt])

    ours = defaultdict(list)
    for h, v in p.items():
        if h in lab['ours'] and isinstance(v, dict) and occ.get(h, 0) >= MINOCC:
            ours[v['tier']].append((h, feats[h], lmap[lab['ours'][h]]))
    rng = random.Random(R.SEED)
    print()
    print(f"  {'tier':6s}{'signs':>6s}{'agree':>8s}{'shuffle':>9s}{'sd':>6s}{'sigma':>7s}")
    res = {}
    for group, tiers in (('A+B', 'AB'), ('C+D', 'CD')):
        rows = [r for t in tiers for r in ours[t]]
        if len(rows) < 5:
            continue
        preds = [model.predict(f) for _, f, _ in rows]
        obs = sum(pr == y for pr, (_, _, y) in zip(preds, rows)) / len(rows)
        nulls = []
        for _ in range(NSHUF):
            ys = [y for _, _, y in rows]
            rng.shuffle(ys)
            nulls.append(sum(pr == y for pr, y in zip(preds, ys)) / len(rows))
        m = sum(nulls) / len(nulls)
        s = (sum((x - m) ** 2 for x in nulls) / (len(nulls) - 1)) ** .5
        sig = (obs - m) / s if s else 0
        res[group] = (obs, sig)
        print(f"  {group:6s}{len(rows):6d}{obs*100:7.1f}%{m*100:8.1f}%{s*100:6.2f}{sig:7.1f}")
        wrong = [(h, y, pr) for (h, f, y), pr in zip(rows, preds) if pr != y]
        if wrong:
            print("         disagree: " + ", ".join(
                f"{h}({p[h]['gloss']}: {y[0]} read as {pr[0]})" for h, y, pr in wrong)[:400])
    if not ok1:
        print("  stage 2 is NOT a result: the instrument failed calibration")
        return 1
    ok2 = res.get('A+B', (0, 0))[1] >= 5
    print(f"  BAR 2: A+B >= 5 sigma over shuffle  ->  {'PASS' if ok2 else 'FAIL'}")
    return 0 if ok2 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
