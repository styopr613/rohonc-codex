"""Does the reading prove itself? Three gates, declared here before the run.

The claim under test is the one that matters: that a text assembled from
guesses is not thereby coherent. If the signs read here are right, then lines
on folios that contributed NOTHING to any reading should still land on the
passage they are telling, because a right reading travels and a wrong one does
not. If the signs are wrong, those lines land at chance, which is what the
frequency-matched control measures.

Kiraly & Tokai's dictionary is tested on the same footing. It is a hypothesis
too, not ground truth, and nothing here assumes otherwise.

    GATE A -- held-out generalisation.
      Take every line that is now fully read and that sits on a folio cited in
      NO reading's evidence. Score its content stems against the 1.75M-word
      reference corpus. Bar: mean score at least 1.5x its frequency-matched
      control, at 5 sigma.

    GATE B -- do this project's own readings carry signal?
      The same measure, restricted to held-out lines that contain at least one
      code read by this project. If those readings are filled-in noise they sit
      at control. Bar: at least 1.3x control, at 3 sigma.

    GATE C -- diagnostic, no bar, and it may go against us.
      For each code occurring 8+ times on scored lines, compare the mean score
      of lines containing it with the mean of lines without. A code whose
      presence LOWERS the match is a candidate misreading, whoever read it.
      Reported as a list, not a verdict.

A near miss is a miss. The bars above are not to be moved after the run.

RESULT, 2026-09-20: GATE A 1.04x (bar 1.5) FAIL. GATE B 1.03x (bar 1.3) FAIL.
Both are recorded as failures and the bars were not touched.

AFTERWARDS, and labelled as what it is -- a diagnostic run after seeing the
result, not a gate -- the same measure was put to six lines whose source
passage is known by hand. It found the right passage for two of them: 119v:4
landed on "the sheep which was lost ... joy shall be in heaven over one
sinner that repenteth", and 187r:6 landed on "the way of the wilderness of
the Red Sea ... and Moses". So the instrument is not blind. But it could not
do it reliably, which means GATE A and GATE B could not have detected a true
reading either, and their failure is therefore NOT evidence that the reading
is wrong. It is evidence that this measure cannot settle the question.

The cause is visible in the queries. A line enters the search as the stems of
EVERY sense of every code on it. "Blessed is the womb" goes in as eleven
stems -- among, away, bless, call, generation, ish, jew, nation, people, thus,
womb -- of which two are the intended reading and nine are other senses of the
same codes. Restricting to the first sense, which is what the rendered page
uses, cut the queries roughly in half and put two of six on the right passage,
but the score still does not separate from control. Choosing the right sense
per occurrence is the missing step, and this document has said from the start
that it needs their grammar, which is unpublished.

    python ktproof.py
"""
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

import corpus
import ktcontext as X
import ktextend as E
import ktsegment as S
import kttranslate as T
import ktverse as V

BAR_A_RATIO, BAR_A_SIGMA = 1.5, 5.0
BAR_B_RATIO, BAR_B_SIGMA = 1.3, 3.0
SEED = 20260920
NSHUF = 40


def cited_folios():
    """Every folio named in any reading's evidence, plus DONE translated ones."""
    import json
    raw = json.load(open(T.PROPOSALS, encoding="utf-8"))
    f = set()
    for h, v in raw.items():
        if h.startswith("_"):
            continue
        f |= set(re.findall(r"\b(\d{3}[rv])\b", v.get("evidence", "")))
    return f


def stems_of(code, gl, seg, var, prop):
    """Content stems a code contributes, from whatever reads it."""
    out = set()
    parts = [code] if (code in gl or code in var or code in prop) else seg.get(code, [code])
    for p in parts:
        if p in gl:
            out |= S.stems(gl[p])
        elif p in var and var[p] in gl:
            out |= S.stems(gl[var[p]])
        elif p in prop:
            out |= {E.stem(w) for w in re.findall(r"[a-z]+", prop[p][0].lower())
                    if w not in E.STOP and len(w) > 2}
    return {s for s in out if s not in E.STOP and len(s) > 2}


def main():
    random.seed(SEED)
    gl, doc, seg, var = X.load()
    prop = dict(X.PROP)
    wins, ws = V.load_windows()
    index, idf = V.build_index(wins)
    cited = cited_folios() | X.DONE
    print(f"reference corpus {len(ws)} words, {len(wins)} windows")
    print(f"folios cited in evidence or already translated: {len(cited)}")

    rows = []                       # (score, has_prop, codes, stems)
    for p in doc:
        if p.page in cited:
            continue
        for ln in p.lines:
            toks = [t for run in ln for t in run]
            if not toks:
                continue
            import ktaffix as A
            bases = [A.strip(t)[0] for t in toks]
            if any(b not in gl and b not in seg and b not in var and b not in prop
                   for b in bases):
                continue                       # not fully read
            q = set()
            for b in bases:
                q |= stems_of(b, gl, seg, var, prop)
            if len(q) < 3:
                continue
            s, _, _ = V.best(q, index, idf)
            rows.append((s, any(b in prop for b in bases), bases, q))

    if not rows:
        print("\nGATE A: no held-out fully-read lines. UNRUNNABLE.")
        return 1
    print(f"held-out fully-read lines with 3+ content stems: {len(rows)}")

    # ---- control: same number of stems, drawn to match corpus frequency.
    pool = [s for s in idf]
    wts = [math.exp(-idf[s]) for s in pool]

    def control_mean(rs):
        outs = []
        for _ in range(NSHUF):
            tot = 0.0
            for s, _h, _b, q in rs:
                fake = set(random.choices(pool, weights=wts, k=len(q)))
                sc, _, _ = V.best(fake, index, idf)
                tot += sc
            outs.append(tot / len(rs))
        m = sum(outs) / len(outs)
        sd = (sum((o - m) ** 2 for o in outs) / max(1, len(outs) - 1)) ** .5
        return m, sd

    def gate(name, rs, bar_r, bar_s):
        if not rs:
            print(f"\n{name}: no testable lines. UNRUNNABLE -- not a pass.")
            return False
        obs = sum(r[0] for r in rs) / len(rs)
        cm, csd = control_mean(rs)
        ratio = obs / cm if cm else 0.0
        sig = (obs - cm) / csd if csd else 0.0
        ok = ratio >= bar_r and sig >= bar_s
        print(f"\n{name}   lines {len(rs)}")
        print(f"  observed mean score        {obs:8.2f}")
        print(f"  frequency-matched control  {cm:8.2f}  sd {csd:.2f}")
        print(f"  ratio {ratio:.2f}x  (bar {bar_r})     sigma {sig:.1f}  (bar {bar_s})")
        print(f"  ->  {'PASS' if ok else 'FAIL'}")
        return ok

    a = gate("GATE A  held-out generalisation", rows, BAR_A_RATIO, BAR_A_SIGMA)
    b = gate("GATE B  this project's readings",
             [r for r in rows if r[1]], BAR_B_RATIO, BAR_B_SIGMA)

    print("\nGATE C  diagnostic: codes whose presence lowers the match")
    occ = Counter()
    for _s, _h, bases, _q in rows:
        occ.update(set(bases))
    mean_all = sum(r[0] for r in rows) / len(rows)
    bad = []
    for c, n in occ.items():
        if n < 8:
            continue
        with_c = [r[0] for r in rows if c in r[2]]
        m = sum(with_c) / len(with_c)
        bad.append((m - mean_all, c, n, m))
    bad.sort()
    print(f"  {len(bad)} codes occur on 8+ held-out lines; mean over all lines {mean_all:.2f}")
    print(f"  {'delta':>8s}  {'n':>4s}  {'mean':>7s}  code / reading")
    for d, c, n, m in bad[:12]:
        who = ("this project" if c in prop else
               "K&T variant" if c in var else
               "K&T compound" if c in seg else "K&T")
        print(f"  {d:8.2f}  {n:4d}  {m:7.2f}  {X.hx(c):22s} {X.word(c, gl, seg, var)[:28]:30s} {who}")
    return 0 if (a and b) else 1


if __name__ == "__main__":
    sys.exit(main())
