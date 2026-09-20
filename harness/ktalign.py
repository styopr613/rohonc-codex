"""Extending the dictionary by sequence alignment, gated on recovering known glosses.

Two earlier attempts failed their gates and are recorded in ktextend.py's
history: bag-of-words alignment scored real pages below random word bags, and
neighbourhood enrichment around a page's gospel locus returned the same five
words -- lord, him, god, Jesus, son -- for every code asked about. Both threw
away order. This uses it.

Name-anchored localisation works (87% of pages beat the random median, against
50%), so each page has a gospel locus. Around that locus the codex page and the
gospel passage are two sequences. A local alignment lines them up on the words
we can already read; an undefined code that falls between two matched anchors
is aligned to whatever gospel word falls between the same anchors. One page is
weak evidence. A code drawing the same candidate from several pages is a
proposal.

The gate is the same as before and is run first: hide the commonest codes the
dictionary does define and ask the method to recover them. Its hit rate on
those is the credibility of everything it proposes for codes nobody has
defined. Below a stated bar it proposes nothing.
"""
import math
import re
from collections import Counter, defaultdict

import ktextend as E
import ktdict
import rohonc_kt as KT

RADIUS = 160          # gospel words either side of the locus
GAP = -0.6
MISMATCH = -0.3
BAR_TOP5 = 0.30       # the method must recover >=30% of held-out glosses in its top 5


def stems_of(glosses):
    out = set()
    for s in glosses:
        s2 = E.META.sub(" ", s)
        out |= {E.stem(w) for w in E.WORD.findall(E.fold(s2).lower())
                if w not in E.STOP and len(w) > 2}
    return out


def build(gl):
    doc = KT.load()
    wins, gw = E.gospel_windows()
    gstem = [E.stem(w) for w in gw]
    bg = Counter(gstem)
    N = sum(bg.values())
    idf = {w: math.log(N / c) for w, c in bg.items()}
    names = {}
    for c, g in gl.items():
        for s in g:
            s2 = E.META.sub(" ", s).strip()
            m = re.fullmatch(r"([A-Z][a-z]{2,})(?: \(.*\))?", s2)
            if m:
                names.setdefault(c, set()).add(E.stem(E.fold(m.group(1)).lower()))
    gpos = defaultdict(list)
    nameset = {x for v in names.values() for x in v}
    for i, s in enumerate(gstem):
        if s in nameset:
            gpos[s].append(i)
    return doc, gstem, idf, names, gpos


def locus(page, names, gpos):
    ns = Counter()
    for t in page.tokens:
        if t in names:
            for nm in names[t]:
                if gpos[nm]:
                    ns[nm] += 1
    if len(ns) < 2:
        return None
    best = None
    for nm in ns:
        for i in gpos[nm]:
            d = sum(min(abs(i - j) for j in gpos[o]) for o in ns if o != nm)
            if best is None or d < best[1]:
                best = (i, d)
    return best[0]


def align(page_tokens, stems_for, gseq, idf):
    """Smith-Waterman on (codex token, gospel stem); returns matched pairs.

    A codex token scores against a gospel word by the idf of the shared stem,
    so a shared 'jerusalem' anchors hard and a shared 'man' barely at all.
    Undefined tokens never match but can sit in the path between anchors.
    """
    n, m = len(page_tokens), len(gseq)
    H = [[0.0] * (m + 1) for _ in range(n + 1)]
    P = [[0] * (m + 1) for _ in range(n + 1)]
    best, bi, bj = 0.0, 0, 0
    for i in range(1, n + 1):
        st = stems_for(page_tokens[i - 1])
        for j in range(1, m + 1):
            g = gseq[j - 1]
            s = idf.get(g, 1.0) if g in st else MISMATCH
            diag = H[i - 1][j - 1] + s
            up = H[i - 1][j] + GAP
            left = H[i][j - 1] + GAP
            v = max(0.0, diag, up, left)
            H[i][j] = v
            P[i][j] = 1 if v == diag else (2 if v == up else (3 if v == left else 0))
            if v > best:
                best, bi, bj = v, i, j
    path = []
    i, j = bi, bj
    while i > 0 and j > 0 and H[i][j] > 0:
        if P[i][j] == 1:
            path.append((i - 1, j - 1))
            i, j = i - 1, j - 1
        elif P[i][j] == 2:
            i -= 1
        elif P[i][j] == 3:
            j -= 1
        else:
            break
    return best, path[::-1]


def proposals(gl, hidden=frozenset(), min_pages=3):
    """{code: Counter(gospel stem)} for codes without a gloss (or hidden)."""
    doc, gstem, idf, names, gpos = build({c: g for c, g in gl.items() if c not in hidden})
    known = {c: stems_of(g) for c, g in gl.items() if c not in hidden}

    def stems_for(tok):
        return known.get(tok, set())

    votes = defaultdict(Counter)
    pages_seen = defaultdict(set)
    for p in doc:
        L = locus(p, names, gpos)
        if L is None:
            continue
        lo, hi = max(0, L - RADIUS), min(len(gstem), L + RADIUS)
        gseq = gstem[lo:hi]
        toks = p.tokens
        score, path = align(toks, stems_for, gseq, idf)
        if len(path) < 4:
            continue
        # an unknown token between two matched anchors: take the gospel words
        # that lie strictly between the anchors' gospel positions
        matched = [(ci, gj) for ci, gj in path if toks[ci] in known]
        for (c0, g0), (c1, g1) in zip(matched, matched[1:]):
            unk = [k for k in range(c0 + 1, c1) if toks[k] not in known]
            span = [gseq[j] for j in range(g0 + 1, g1)
                    if gseq[j] not in E.STOP and len(gseq[j]) > 2]
            if not unk or not span or len(span) > 6:
                continue
            for k in unk:
                for w in span:
                    votes[toks[k]][w] += 1.0 / len(span)
                pages_seen[toks[k]].add(p.page)
    return {c: v for c, v in votes.items() if len(pages_seen[c]) >= min_pages}, pages_seen


def gate(gl, n_hidden=60):
    doc = KT.load()
    types = Counter(t for p in doc for t in p.tokens)
    hidden = [t for t, _ in types.most_common() if t in gl][:n_hidden]
    votes, seen = proposals(gl, hidden=frozenset(hidden))
    hit1 = hit5 = hit20 = tested = 0
    rows = []
    for c in hidden:
        truth = stems_of(gl[c])
        v = votes.get(c)
        if not truth or not v:
            continue
        tested += 1
        ranked = [w for w, _ in v.most_common()]
        rank = next((i for i, w in enumerate(ranked, 1) if w in truth), None)
        if rank:
            hit1 += rank <= 1
            hit5 += rank <= 5
            hit20 += rank <= 20
        rows.append((rank, types[c], "/".join(sorted(truth))[:26], ", ".join(ranked[:4])))
    return tested, hit1, hit5, hit20, rows


if __name__ == "__main__":
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    print("HELD-OUT GATE -- sequence alignment\n")
    tested, h1, h5, h20, rows = gate(gl)
    print(f"{'rank':>5s} {'freq':>6s}  {'true gloss':26s}  proposed")
    for rank, f, t, prop in rows[:15]:
        print(f"{str(rank) if rank else '—':>5s} {f:6d}  {t:26s}  {prop}")
    print(f"\ntested {tested} hidden codes")
    for lab, h in (("ranked #1", h1), ("in top 5", h5), ("in top 20", h20)):
        print(f"  true gloss {lab:10s} {h:3d}  ({h/max(1,tested)*100:.0f}%)")
    ok = tested and h5 / tested >= BAR_TOP5
    print(f"\nbar: top-5 >= {BAR_TOP5*100:.0f}%  ->  {'PASS' if ok else 'FAIL'}")
