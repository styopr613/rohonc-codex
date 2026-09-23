"""TEST 2 OF WHETHER OUR ADDITIONS ARE TRUE: does each sign behave, in the
book, like the part of speech its English gloss says it is?

This test never looks at the Bible passage a folio cites. It looks only at
how the sign sits among other signs -- what stands before it, what stands
after it, whether it takes K&T's genitive prefix b60 or their verbal prefix
520, whether their subject marker 910 follows it. A sign that is really a
noun keeps noun company; a verb keeps verb company. A gloss invented from a
verse can get the sense of a line right and still put a verb where the book
has a noun.

Two stages, both bars declared before the run.

  STAGE 1, calibration. Take K&T's own glossed signs, label each NOUN or
  VERB from its English gloss (by a lexicon built from the Douay and King
  James: a word that follows the/a/his/thy is a noun, one that follows
  shall/did/he/they is a verb), and train a naive-Bayes classifier on the
  sign's context in the book. Leave-one-out.

    BAR 1: >= 70% accuracy on K&T's signs, and >= 5 sigma above the
           majority-class baseline. Below it the instrument cannot see
           parts of speech and stage 2 is NOT a result.

  STAGE 2, the test. Apply the classifier to every sign this project read
  that has a noun or verb gloss. Agreement = classifier's call matches the
  gloss's part of speech.

    CONTROL: the gloss labels shuffled among our signs, 20 times.
    BAR 2: tiers A+B beat the shuffle by >= 5 sigma. C+D and G reported
           with their sigma.

The context features are the identity of the previous token and the next
token (the 60 commonest each), the four morphological facts above, and
nothing from any passage.

    python3 ktpos.py    [--shuf N]
"""
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R

NSHUF = 20
NOUN_CUES = {"the", "a", "an", "his", "her", "my", "thy", "their", "our",
             "your", "this", "that", "these", "those", "every", "of"}
VERB_CUES = {"shall", "will", "did", "do", "doth", "hath", "not", "they",
             "he", "she", "ye", "we", "i", "thou", "who", "which", "and",
             "to"}
VERBISH = {"shall", "be", "is", "was", "were", "are", "do", "did", "doth",
           "go", "went", "came", "come", "say", "said", "saith", "hath",
           "have", "had", "let", "may", "can", "cannot", "must"}
TOPN = 60


def lexicon():
    """word -> (noun votes, verb votes) from the two Bibles."""
    votes = defaultdict(lambda: [0, 0])
    for verses in (L.verses(), L.verses_dr()):
        for txt in verses.values():
            ws = re.findall(r"[a-zA-Z]+", txt.lower())
            for i in range(1, len(ws)):
                w, prev = ws[i], ws[i - 1]
                if len(w) < 3:
                    continue
                if prev in NOUN_CUES:
                    votes[w][0] += 1
                elif prev in VERB_CUES:
                    votes[w][1] += 1
    return votes


def gloss_pos(gloss, lex):
    """NOUN, VERB or None for an English gloss."""
    g = re.sub(r"[<\[(][^>\])]*[>\])]", " ", gloss).replace("_", " ")
    ws = [w for w in re.findall(r"[a-zA-Z]+", g.lower())]
    if any(w in VERBISH for w in ws):
        return "VERB"
    if ws and ws[-1].endswith(("eth", "est")) and len(ws[-1]) > 5:
        return "VERB"
    for w in ws:
        if w in K.STOP or len(w) < 3:
            continue
        n, v = lex.get(w, (0, 0))
        if n + v < 3:
            continue
        if n >= 3 * v:
            return "NOUN"
        if v >= 3 * n:
            return "VERB"
        return None
    return None


def contexts(doc):
    """hex -> Counter of context features."""
    feats = defaultdict(Counter)
    tokc = Counter()
    seqs = []
    for pg in doc:
        for ln in pg.lines:
            toks = [K.hx(A.strip(t)[0]) for run in ln for t in run]
            seqs.append(toks)
            tokc.update(toks)
    top = {t for t, _ in tokc.most_common(TOPN)}
    types = set(tokc)
    for toks in seqs:
        for i, t in enumerate(toks):
            prev = toks[i - 1] if i else "<bol>"
            nxt = toks[i + 1] if i + 1 < len(toks) else "<eol>"
            feats[t]["p:" + (prev if prev in top or prev in ("<bol>",) else "other")] += 1
            feats[t]["n:" + (nxt if nxt in top or nxt in ("<eol>",) else "other")] += 1
    # morphology: does the sign appear inside these frames anywhere?
    for h in list(feats):
        if "b60" + h in types:
            feats[h]["m:genitive"] += 1
        if "520" + h in types or "521" + h in types:
            feats[h]["m:verbal"] += 1
        if h + "910" in types:
            feats[h]["m:subject"] += 1
        if h + "ae0" in types:
            feats[h]["m:ae0"] += 1
    return feats


class NB:
    def __init__(self, rows):
        self.cls = Counter()
        self.fc = {"NOUN": Counter(), "VERB": Counter()}
        self.tot = {"NOUN": 0, "VERB": 0}
        self.vocab = set()
        for f, y in rows:
            self.cls[y] += 1
            for k, c in f.items():
                self.fc[y][k] += c
                self.tot[y] += c
                self.vocab.add(k)

    def predict(self, f):
        best, arg = None, None
        V = len(self.vocab) + 1
        for y in ("NOUN", "VERB"):
            if not self.cls[y]:
                continue
            s = math.log(self.cls[y])
            for k, c in f.items():
                s += c * math.log((self.fc[y][k] + 0.5) / (self.tot[y] + 0.5 * V))
            if best is None or s > best:
                best, arg = s, y
        return arg


def main(argv):
    nshuf = int(argv[argv.index('--shuf') + 1]) if '--shuf' in argv else NSHUF
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    lex = lexicon()
    feats = contexts(doc)

    def hx(s):
        return "".join(f"{ord(c) - 0xE000:03x}" for c in s)

    # ---- stage 1: K&T
    kt = []
    for s, g in gl.items():
        h = hx(s)
        if h not in feats:
            continue
        votes = Counter(gloss_pos(x, lex) for x in g)
        votes.pop(None, None)
        if not votes:
            continue
        y, n = votes.most_common(1)[0]
        if len(votes) > 1 and list(votes.values()).count(n) > 1:
            continue
        kt.append((h, feats[h], y))
    right = 0
    for i, (h, f, y) in enumerate(kt):
        m = NB([(f2, y2) for j, (_, f2, y2) in enumerate(kt) if j != i])
        right += m.predict(f) == y
    acc = right / len(kt)
    maj = max(Counter(y for _, _, y in kt).values()) / len(kt)
    sd = (maj * (1 - maj) / len(kt)) ** .5
    sig1 = (acc - maj) / sd if sd else 0
    print("TEST 2: PART OF SPEECH FROM CONTEXT ALONE")
    print(f"  stage 1, K&T's own signs   n={len(kt)}   "
          f"leave-one-out accuracy {acc*100:.1f}%   "
          f"majority class {maj*100:.1f}%   {sig1:.1f} sigma")
    ok1 = acc >= 0.70 and sig1 >= 5
    print(f"  BAR 1: >= 70% and >= 5 sigma  ->  {'PASS' if ok1 else 'FAIL'}")
    if not ok1:
        print("  the instrument cannot see parts of speech; stage 2 is NOT a result")
    model = NB([(f, y) for _, f, y in kt])

    # ---- stage 2: ours
    ours = defaultdict(list)
    for h, v in p.items():
        if h.startswith('_') or not isinstance(v, dict):
            continue
        t = v.get('tier')
        if t not in 'ABCDG' or h not in feats or hx(chr(0)) == h:
            continue
        y = gloss_pos(v.get('gloss', ''), lex)
        if y:
            ours[t].append((h, feats[h], y))
    rng = random.Random(R.SEED)
    print()
    print(f"  {'tier':6s}{'signs':>6s}{'agree':>8s}{'shuffle':>9s}{'sd':>6s}{'sigma':>7s}")
    res = {}
    for group, tiers in (('A+B', 'AB'), ('C+D', 'CD'), ('G', 'G')):
        rows = [r for t in tiers for r in ours[t]]
        if not rows:
            continue
        preds = [model.predict(f) for _, f, _ in rows]
        obs = sum(pr == y for pr, (_, _, y) in zip(preds, rows)) / len(rows)
        nulls = []
        for _ in range(nshuf):
            ys = [y for _, _, y in rows]
            rng.shuffle(ys)
            nulls.append(sum(pr == y for pr, y in zip(preds, ys)) / len(rows))
        m = sum(nulls) / len(nulls)
        s = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** .5
        sig = (obs - m) / s if s else 0
        res[group] = sig
        print(f"  {group:6s}{len(rows):6d}{obs*100:7.1f}%{m*100:8.1f}%{s*100:6.2f}{sig:7.1f}")
    if ok1 and 'A+B' in res:
        print(f"  BAR 2: A+B >= 5 sigma  ->  {'PASS' if res['A+B'] >= 5 else 'FAIL'}")
    return 0 if ok1 and res.get('A+B', 0) >= 5 else 1


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main(sys.argv[1:]))
