"""The rejection test: propose a meaning, then try to kill it everywhere.

The sixth attempt (ktread.py) read six blinded codes from context and got one
to two right, single-shot. That is roughly what Kiraly and Tokai get on a first
pass too. The difference is not the guessing. It is that a guess there is
carried to every occurrence of the code and discarded if it fails at any one of
them, and this harness never built that step.

This builds it. A candidate meaning for a code is scored not by how well it
fits the passage that suggested it, but by how it survives the others. The
scoring is distributional and needs no reader: if a code means what a candidate
means, it should keep the company that candidate's synonyms keep. So the test
asks whether the code's neighbours across the whole book look like the
neighbours of the defined codes carrying that meaning.

    survival = similarity of the code's context profile to the pooled profile
               of every defined code whose gloss contains the candidate word

A candidate that fits one passage and nothing else scores near zero. A
candidate that fits everywhere scores high. That asymmetry is the whole point:
rejection is cheap and reliable where generation is not.

Gated like every other attempt, and the bar is set before the run. Blind a
defined code, generate candidates from its contexts, rank them by survival, and
ask where the true gloss lands. Bar: the true meaning in the top five for 30%
of held-out codes -- the same bar the five mechanical methods failed.
"""
import argparse
import math
from collections import Counter, defaultdict

import ktdict
import ktextend as E
import rohonc_kt as KT

BAR_TOP5 = 0.30
MIN_OCC = 6
CTX = (-2, -1, 1, 2)


def lines_of(blocktypes=("main", "picture")):
    out = []
    for p in KT.load(blocktypes=blocktypes):
        for runs in p.lines:
            for run in runs:
                if run:
                    out.append(run)
    return out


def context_profiles(lines, vocab):
    prof = defaultdict(Counter)
    for ln in lines:
        for i, t in enumerate(ln):
            for d in CTX:
                j = i + d
                if 0 <= j < len(ln) and ln[j] in vocab:
                    prof[t][(d, ln[j])] += 1
    return prof


def ppmi_vectors(prof):
    ctx_tot, grand = Counter(), 0
    for c in prof.values():
        for k, n in c.items():
            ctx_tot[k] += n
            grand += n
    out = {}
    for t, c in prof.items():
        tot = sum(c.values())
        if tot < 4:
            continue
        v = {}
        for k, n in c.items():
            pa, pb = tot / grand, ctx_tot[k] / grand
            if pa and pb:
                m = math.log((n / grand) / (pa * pb))
                if m > 0:
                    v[k] = m
        if v:
            nrm = math.sqrt(sum(x * x for x in v.values()))
            out[t] = {k: x / nrm for k, x in v.items()}
    return out


def pooled(vecs, codes):
    """Mean unit vector of several codes: the profile a meaning keeps."""
    acc = Counter()
    n = 0
    for c in codes:
        v = vecs.get(c)
        if not v:
            continue
        n += 1
        for k, x in v.items():
            acc[k] += x
    if not n:
        return None
    nrm = math.sqrt(sum(x * x for x in acc.values()))
    return {k: x / nrm for k, x in acc.items()} if nrm else None


def cos(a, b):
    if not a or not b:
        return 0.0
    if len(a) > len(b):
        a, b = b, a
    return sum(x * b.get(k, 0.0) for k, x in a.items())


def sense_index(gl, hide=frozenset()):
    """{meaning word: [codes whose gloss carries it]} over the dictionary."""
    idx = defaultdict(list)
    for c, g in gl.items():
        if c in hide:
            continue
        for w in E.gloss_stems(gl, c) if hasattr(E, "gloss_stems") else ():
            idx[w].append(c)
    return idx


def stems(gl, code):
    out = set()
    for s in gl.get(code, ()):
        s2 = E.META.sub(" ", s)
        out |= {E.stem(w) for w in E.WORD.findall(E.fold(s2).lower())
                if w not in E.STOP and len(w) > 2}
    return out


def survival(target, candidate_word, vecs, idx, hide):
    codes = [c for c in idx.get(candidate_word, ()) if c not in hide and c != target]
    if len(codes) < 2:
        return None
    p = pooled(vecs, codes)
    return cos(vecs.get(target), p) if p else None


def candidates_from_context(target, lines, gl, hide, topn=400):
    """Meanings carried by codes that sit near the target: the pool to reject from."""
    near = Counter()
    for ln in lines:
        for i, t in enumerate(ln):
            if t != target:
                continue
            for d in CTX:
                j = i + d
                if 0 <= j < len(ln):
                    o = ln[j]
                    if o in gl and o not in hide:
                        for w in stems(gl, o):
                            near[w] += 1
    return [w for w, _ in near.most_common(topn)]


def run_gate(gl, n_hidden=40):
    lines = lines_of()
    freq = Counter(t for ln in lines for t in ln)
    defined = [t for t, _ in freq.most_common() if t in gl and freq[t] >= MIN_OCC]
    hidden = defined[45:45 + n_hidden]
    hideset = frozenset(hidden)
    vocab = {t for t in gl if t not in hideset}
    vecs = ppmi_vectors(context_profiles(lines, vocab))
    idx = defaultdict(list)
    for c in gl:
        if c in hideset:
            continue
        for w in stems(gl, c):
            idx[w].append(c)

    hit1 = hit5 = hit20 = tested = 0
    rows = []
    for t in hidden:
        truth = stems(gl, t)
        if not truth or t not in vecs:
            continue
        cands = candidates_from_context(t, lines, gl, hideset)
        scored = []
        for w in cands:
            s = survival(t, w, vecs, idx, hideset)
            if s is not None:
                scored.append((s, w))
        if len(scored) < 5:
            continue
        scored.sort(reverse=True)
        tested += 1
        rank = next((i for i, (_, w) in enumerate(scored, 1) if w in truth), None)
        if rank:
            hit1 += rank <= 1
            hit5 += rank <= 5
            hit20 += rank <= 20
        rows.append((rank, freq[t], "/".join(sorted(truth))[:22],
                     ", ".join(w for _, w in scored[:5])))
    return tested, hit1, hit5, hit20, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hidden", type=int, default=40)
    a = ap.parse_args()
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    print("HELD-OUT GATE -- generate from context, then reject across the book\n")
    tested, h1, h5, h20, rows = run_gate(gl, a.hidden)
    print(f"{'rank':>5s} {'freq':>6s}  {'true gloss':22s}  survived best")
    for rank, f, t, c in rows[:20]:
        print(f"{str(rank) if rank else '-':>5s} {f:6d}  {t:22s}  {c}")
    print(f"\ntested {tested} hidden codes")
    for lab, h in (("true meaning ranked #1", h1), ("in top 5", h5), ("in top 20", h20)):
        print(f"  {lab:24s} {h:3d}  ({h/max(1,tested)*100:.0f}%)")
    ok = tested and h5 / tested >= BAR_TOP5
    print(f"\nbar: top-5 >= {BAR_TOP5*100:.0f}%  ->  {'PASS' if ok else 'FAIL'}")


if __name__ == "__main__":
    main()
