"""Working out undefined codes from the company they keep, not from the gospels.

Three earlier attempts all failed (ktextend.py, ktalign.py), and all three
failed the same way: each tried to reach an unknown code through the gospel
text. That link is weak. The codex paraphrases rather than translates, it draws
on apocrypha and prayer the reference corpus does not contain, and every
comparison passes through two layers of translation -- Kiraly & Tokai's English
glosses against a modern English gospel.

This drops the gospels. A word is characterised by the words around it, and the
codex supplies that directly: for every code, count which known codes occur
immediately before and after it. Two codes used the same way have similar
profiles, whatever they mean. That is enough to say an unknown code behaves
like the codes for 'Lord', 'God' and 'Jesus' -- which is a real finding about
it, and needs no gospel at all.

The gate is the same as the others and is run first: hide codes the dictionary
does define, find each one's nearest neighbours by context alone, and ask
whether a neighbour shares a gloss with it. Nothing is proposed for genuinely
unknown codes unless the method can recover known ones.

Picture-caption blocks are included here, unlike elsewhere in this project:
Tokai read many codes off the illustrations beside them, so a caption is
exactly where a code sits closest to its meaning.
"""
import math
from collections import Counter, defaultdict

import ktdict
import ktextend as E
import rohonc_kt as KT

BAR_TOP5 = 0.30          # a neighbour sharing a gloss, for 30% of hidden codes
MIN_OCC = 8              # codes rarer than this have no usable profile


def streams(blocktypes=("main", "picture")):
    """Per-line token sequences, so context never crosses a line break."""
    out = []
    for p in KT.load(blocktypes=blocktypes):
        for runs in p.lines:
            for run in runs:
                if run:
                    out.append(run)
    return out


def profiles(lines, vocab):
    """{code: Counter of (slot, neighbour)} over a fixed set of context codes."""
    prof = defaultdict(Counter)
    freq = Counter()
    for ln in lines:
        for i, t in enumerate(ln):
            freq[t] += 1
            for d in (-2, -1, 1, 2):
                j = i + d
                if 0 <= j < len(ln) and ln[j] in vocab:
                    prof[t][(d, ln[j])] += 1
    return prof, freq


def ppmi(prof, freq):
    """Positive pointwise mutual information, so common neighbours stop dominating."""
    ctx_tot = Counter()
    grand = 0
    for t, c in prof.items():
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
            p = n / grand
            pa, pb = tot / grand, ctx_tot[k] / grand
            m = math.log(p / (pa * pb)) if pa and pb else 0.0
            if m > 0:
                v[k] = m
        if v:
            norm = math.sqrt(sum(x * x for x in v.values()))
            out[t] = {k: x / norm for k, x in v.items()}
    return out


def nearest(vecs, target, pool, k=10):
    a = vecs.get(target)
    if not a:
        return []
    sc = []
    for t in pool:
        if t == target:
            continue
        b = vecs.get(t)
        if not b:
            continue
        if len(a) > len(b):
            a2, b2 = b, a
        else:
            a2, b2 = a, b
        s = sum(x * b2.get(kk, 0.0) for kk, x in a2.items())
        if s > 0:
            sc.append((s, t))
    sc.sort(reverse=True)
    return sc[:k]


def gloss_stems(gl, code):
    out = set()
    for s in gl.get(code, ()):
        s2 = E.META.sub(" ", s)
        out |= {E.stem(w) for w in E.WORD.findall(E.fold(s2).lower())
                if w not in E.STOP and len(w) > 2}
    return out


def gate(gl, n_hidden=80):
    """Leave-one-out: only the code under test is treated as unknown.

    The first version hid all eighty at once and removed them from the context
    vocabulary too. Those eighty are the commonest codes in the book -- the
    function words that give every other code its shape -- so hiding them
    together destroyed the signal for all of them and scored 4%. In reality a
    code is unknown on its own, against a dictionary that still holds the rest.
    """
    lines = streams()
    freq_all = Counter(t for ln in lines for t in ln)
    known = [t for t in gl if freq_all[t] >= MIN_OCC]
    hidden = sorted(known, key=lambda t: -freq_all[t])[:n_hidden]
    vocab = set(known)                      # the whole dictionary stays as context
    prof, freq = profiles(lines, vocab)
    vecs = ppmi(prof, freq)
    hit1 = hit5 = hit10 = tested = 0
    rows = []
    for t in hidden:
        truth = gloss_stems(gl, t)
        if not truth or t not in vecs:
            continue
        pool = [o for o in known if o != t and o in vecs]
        nb = nearest(vecs, t, pool, 10)
        if not nb:
            continue
        tested += 1
        rank = None
        for i, (s, o) in enumerate(nb, 1):
            if gloss_stems(gl, o) & truth:
                rank = i
                break
        if rank:
            hit1 += rank <= 1
            hit5 += rank <= 5
            hit10 += rank <= 10
        rows.append((rank, freq_all[t], "/".join(sorted(truth))[:24],
                     "; ".join("/".join(sorted(gloss_stems(gl, o))[:2]) for _, o in nb[:3])))
    return tested, hit1, hit5, hit10, rows


if __name__ == "__main__":
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    print("HELD-OUT GATE -- distributional neighbours, gospels not used\n")
    tested, h1, h5, h10, rows = gate(gl)
    print(f"{'rank':>5s} {'freq':>6s}  {'true gloss':24s}  nearest by context")
    for rank, f, t, nb in rows[:18]:
        print(f"{str(rank) if rank else '-':>5s} {f:6d}  {t:24s}  {nb}")
    print(f"\ntested {tested} hidden codes")
    for lab, h in (("neighbour #1 shares a gloss", h1),
                   ("some neighbour in top 5", h5),
                   ("some neighbour in top 10", h10)):
        print(f"  {lab:28s} {h:3d}  ({h/max(1,tested)*100:.0f}%)")
    ok = tested and h5 / tested >= BAR_TOP5
    print(f"\nbar: top-5 >= {BAR_TOP5*100:.0f}%  ->  {'PASS' if ok else 'FAIL'}")
