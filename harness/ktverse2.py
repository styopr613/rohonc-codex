"""Why ktverse.py failed, and a second gate on lines the diagnosis never saw.

ktverse.py located 213 anchor lines and recovered a hidden gloss from the
relocated passage 15.5% of the time against a 40% bar. Signal at 18.5 sigma,
nowhere near enough to read a word. Before trying again the failure has to be
understood, and trying again has to be done in a way that cannot be tuning.

THE SPLIT. The anchors are ranked by score. Odd ranks are the DEVELOPMENT
half; even ranks are the TEST half. Everything below is chosen on the
development half only. The test half is scored exactly once, at the end,
against the bar declared here.

THE DIAGNOSIS, on the development half. Recovery is broken down three ways:
  1. by anchor strength   -- top 25 / 50 / all
  2. by relocation        -- did hiding the word move the located window?
  3. by gloss kind        -- a proper name, a concrete noun, or anything else

THE SELECTION RULE, declared before the diagnosis is run: whichever SINGLE
one of those three cuts gives the highest recovery on the development half,
with at least 40 cases, becomes the population rule for the test half. Not a
combination, not the best two -- one cut, picked by that rule.

THE GATE on the test half, identical bar to ktverse.py and not moved:
  recovery >= 40%, >= 2x the random-window control, >= 5 sigma.

If the test half fails, the refinement failed, and it is written up as the
seventeenth failure. If it passes, the rule it passed under says which words
a located passage can be trusted to give up, and only those are read.

    python ktverse2.py
"""
import random
import re
import sys

import ktdict
import ktsegment as S
import rohonc_kt as KT
import ktverse as V

CONCRETE = re.compile(r"^(sheep|stone|garden|brook|tree|fruit|cup|wine|water|bread|"
                      r"sword|fire|star|donkey|ox|manger|hay|house|city|town|gate|throne|"
                      r"foot|hand|eye|mouth|head|blood|bone|lamb|dove|cloud|earth|sun|moon|"
                      r"night|day|year|field|mount|mountain|king|servant|son|father|mother|"
                      r"wife|prophet|angel|apostle|book|word|debt|denarius|silver|kiss|"
                      r"serpent|branch|ark|rain|heaven|hell|soul|body|cross|tomb|door|"
                      r"road|way|ship|boat|net|fish|loaf|oil|lamp|coin|money|tax)$")


def gloss_kind(glosses):
    plain = [S.best_sense(glosses)]
    for g in plain:
        g0 = g.strip().split(",")[0].split(" ")[0]
        if re.match(r"^[A-Z][a-z]+$", g0):
            return "name"
        if CONCRETE.match(S.E.stem(g0.lower())):
            return "concrete"
    return "other"


def cases_for(anchors, gl, seg, index, idf, wins):
    """One case per hidden code: (rank, moved?, kind, truth, hit, win_id)."""
    out = []
    for rank, (s, marg, page, i, toks, k, q) in enumerate(anchors, 1):
        for t in sorted(set(toks)):
            if t not in gl:
                continue
            truth = S.stems(gl[t])
            if not truth:
                continue
            rest = V.line_stems(toks, gl, seg, skip=t)
            if len(rest) < 3:
                continue
            s2, k2, _ = V.best(rest, index, idf)
            if k2 < 0:
                continue
            moved = abs(k2 - k) > 1
            hit = bool(truth & wins[k2])
            out.append((rank, moved, gloss_kind(gl[t]), truth, hit))
    return out


def rate(cs):
    return (sum(1 for c in cs if c[4]) / len(cs)) if cs else 0.0


def control(cs, wins, rng, trials=200):
    nulls = []
    for _ in range(trials):
        c = sum(1 for _r, _m, _k, truth, _h in cs
                if truth & wins[rng.randrange(len(wins))])
        nulls.append(c / len(cs) if cs else 0.0)
    m = sum(nulls) / len(nulls)
    sd = (sum((v - m) ** 2 for v in nulls) / max(1, len(nulls) - 1)) ** 0.5
    return m, sd


def main():
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    defset = set(gl)
    seg = {}
    for t in {t for p in doc for t in p.tokens}:
        if t not in gl:
            s = S.segment(t, defset)
            if s and len(s) >= 2:
                seg[t] = s
    wins, ws = V.load_windows()
    index, idf = V.build_index(wins)
    lines = []
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            toks = [t for run in ln for t in run]
            if toks:
                lines.append((p.page, i, toks))
    scored = []
    for page, i, toks in lines:
        q = V.line_stems(toks, gl, seg)
        if len(q) < 3:
            continue
        s, k, marg = V.best(q, index, idf)
        scored.append((s, marg, page, i, toks, k, q))
    scored.sort(key=lambda x: -x[0])
    n_anchor = max(1, int(len(scored) * V.ANCHOR_PCT))
    anchors = scored[:n_anchor]
    dev = anchors[0::2]
    test = anchors[1::2]
    rng = random.Random(408)

    print("=" * 76)
    print("WHY THE ANCHOR GATE FAILED  (development half only)")
    print("=" * 76)
    cs = cases_for(dev, gl, seg, index, idf, wins)
    print(f"anchors {len(anchors)}: development {len(dev)}, test {len(test)}")
    print(f"development cases {len(cs)}, recovery {rate(cs)*100:.1f}%")
    cuts = {}
    print("\n  1. by anchor strength")
    for top in (25, 50, len(dev)):
        sub = [c for c in cs if c[0] <= top]
        cuts[f"top {top} anchors"] = (rate(sub), len(sub), lambda c, t=top: c[0] <= t)
        print(f"     top {top:3d}   cases {len(sub):4d}   recovery {rate(sub)*100:5.1f}%")
    print("\n  2. by whether hiding the word moved the located window")
    for moved in (False, True):
        sub = [c for c in cs if c[1] == moved]
        lab = "window moved" if moved else "window stable"
        cuts[lab] = (rate(sub), len(sub), lambda c, m=moved: c[1] == m)
        print(f"     {lab:14s} cases {len(sub):4d}   recovery {rate(sub)*100:5.1f}%")
    print("\n  3. by kind of gloss")
    for kind in ("name", "concrete", "other"):
        sub = [c for c in cs if c[2] == kind]
        cuts[f"gloss is a {kind}"] = (rate(sub), len(sub), lambda c, k=kind: c[2] == k)
        print(f"     {kind:14s} cases {len(sub):4d}   recovery {rate(sub)*100:5.1f}%")

    eligible = {k: v for k, v in cuts.items() if v[1] >= 40}
    pick = max(eligible, key=lambda k: eligible[k][0])
    print(f"\n  SELECTION RULE -> '{pick}'  ({eligible[pick][0]*100:.1f}% on {eligible[pick][1]} dev cases)")

    print()
    print("=" * 76)
    print("THE SECOND GATE  (test half, scored once)")
    print("=" * 76)
    ct = cases_for(test, gl, seg, index, idf, wins)
    rule = cuts[pick][2]
    sub = [c for c in ct if rule(c)]
    obs = rate(sub)
    m, sd = control(sub, wins, rng)
    sig = (obs - m) / sd if sd else 0.0
    ratio = obs / m if m else float("inf")
    print(f"  population rule                          {pick}")
    print(f"  test cases under the rule                {len(sub)}  (of {len(ct)})")
    print(f"  gloss found in the relocated window      {obs*100:5.1f}%")
    print(f"  same test against a random window        {m*100:5.1f}%  (sd {sd*100:.2f})")
    print(f"  ratio {ratio:.2f}x     sigma {sig:.1f}")
    ok = obs >= V.BAR_HIT and ratio >= V.BAR_RATIO and sig >= V.BAR_SIGMA
    print()
    print(f"  BAR: hit >= {V.BAR_HIT*100:.0f}%, ratio >= {V.BAR_RATIO}x, "
          f"sigma >= {V.BAR_SIGMA}  ->  {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
