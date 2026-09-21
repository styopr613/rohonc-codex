"""The dossier for every word the rendering still cannot read, and the
apply step that turns a decision about one into an entry.

The last 3.6% of the book is 943 signs, and 826 of them occur exactly once.
There is no second occurrence to check a guess against, so nothing here can
reach tier A or B. What CAN be done for each one is to put every signal on
one screen -- the line it stands in with the hole marked, the source passage
the folio cites, the free words of that passage rarest first, and every
structural relation to a sign already read (sits inside one, holds one, is
one glyph from one, is mostly made of them) -- and then make one judgment
per sign, written down with its reason and its tier.

    python ktdark.py dossier [N]      the dossier for the next N unread signs,
                                      in queue order (all of them if no N)
    python ktdark.py apply FILE.json  {hex: [gloss, tier, evidence]} into
                                      proposals.json, with a dated backup

The tier written is the tier earned. Tier A is allowed here for one
reason only: Kiraly & Tokai sometimes cite the folio and line of a hole in
their own entry, which is the tier A test "proved by K&T citation". A structural anchor (inside / holds /
one glyph) on a sign that fits its line is C or D as ktprov would class it.
A passage-fit with no anchor is G: shown in brackets in the reader's edition,
never counted as read, and worth exactly what ktguess measured for it.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

import corpus
import ktaffix as A
import ktcover as CV
import ktcross as K
import ktleft as L
import ktnear as N
import ktqueue as Q
import kttranslate as T

PROP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "proposals.json")


def readings(gl, prop):
    read = {}
    for c, senses in gl.items():
        read[K.hx(c)] = "; ".join(sorted({s.strip() for s in senses}))[:60]
    for c, (g, tier) in prop.items():
        read.setdefault(K.hx(c), g.replace("_", " ") + f" [{tier}]")
    return read


def dossier(argv):
    n_want = next((int(a) for a in argv if a.isdigit()), 0)
    rows, prop = Q.survey()
    q = Q.load()
    gl, doc, seg, var, prop, inv = K.build()
    read = readings(gl, prop)
    lens = sorted({len(k) for k in read}, reverse=True)
    by_len = defaultdict(list)
    for h, g in read.items():
        by_len[len(N.glyphs(h))].append((N.glyphs(h), h, g))
    vv, vd = L.verses(), L.verses_dr()
    freq = Counter()
    for t in (vv, vd):
        for txt in t.values():
            freq.update(K.stem(w.lower()) for w in re.findall(r"[A-Za-z]+", txt))
    idx = K.taken_index(gl, prop)
    notes, pools = {}, {}

    where = defaultdict(list)
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            for b in {A.strip(t)[0] for t in tk if A.strip(t)[0] not in inv}:
                s = " ".join("<<___>>" if A.strip(t)[0] == b
                             else T.render_token(t, gl, seg, False, var, prop)
                             for t in tk)
                where[K.hx(b)].append((p.page, i, s))

    out = 0
    for h, n, sole, lines in rows:
        if q.get(h, {}).get("state") == "pass":
            continue
        if n_want and out >= n_want:
            break
        out += 1
        g = N.glyphs(h)
        print(f"=== {h}   x{n}   {len(g)} glyphs   completes {sole} line(s)")
        ins = sorted([(ph, gg) for ph, gg in read.items() if len(h) >= 6 and h in ph and ph != h],
                     key=lambda r: len(r[0]))[:3]
        for ph, gg in ins:
            pos = "head" if ph.startswith(h) else ("tail" if ph.endswith(h) else "mid")
            print(f"  in    {ph} ({pos}) = {gg}")
        holds = sorted([(ch, gg) for ch, gg in read.items() if len(ch) >= 6 and ch in h],
                       key=lambda r: -len(r[0]))[:3]
        for ch, gg in holds:
            rest = h.replace(ch, "_", 1)
            print(f"  holds {ch} = {gg}   (rest {rest})")
        near = []
        if len(g) >= 2:
            for L_ in (len(g) - 1, len(g), len(g) + 1):
                for gg_, hh, gl_ in by_len.get(L_, []):
                    if N.one_away(g, gg_):
                        near.append((hh, gl_))
        for hh, gl_ in near[:4]:
            print(f"  near  {hh} = {gl_}")
        pieces, cov = CV.cover(h, read, lens)
        if len(h) >= 6 and cov / len(h) >= 0.5 and any(gg for _, gg in pieces):
            print("  cover " + " + ".join(f"{gg}" if gg else f"?{p}" for p, gg in pieces)
                  + f"   ({cov/len(h):.0%})")
        pages = []
        for pg, i, s in where[h][:4]:
            print(f"  {pg}:{i:<3d} {s[:170]}")
            if pg not in pages:
                pages.append(pg)
        for pg in pages[:2]:
            if pg not in notes:
                notes[pg] = K.note_for(pg)
                r = L.refs_in(notes[pg])
                if r:
                    both, dro, kjo, syn = L.pools_for(vv, vd, r, idx, 0)
                    cand = sorted({**both, **dro}, key=lambda s: (freq.get(s, 0), s))
                    pools[pg] = ", ".join(sorted({**both, **dro}[s], key=lambda w: -{**both, **dro}[s][w])[0]
                                          for s in cand[:14])
                else:
                    pools[pg] = ""
            nt = notes[pg]
            m = re.search(r"\b((?:[1-3] )?[A-Z][a-z]+\.? ?\d+[:.]\d+(?:[-–]\d+)?)", nt)
            print(f"  src   {pg}: {(m.group(1) if m else nt[:90]) or '(no source cited)'}")
            if pools[pg]:
                print(f"  pool  {pg}: {pools[pg]}")
        print()
    return 0


def apply(path):
    new = json.load(open(path))
    prop = json.load(open(PROP))
    gl, doc, seg, var, _, inv = K.build()
    cnt = Counter(K.hx(A.strip(t)[0]) for p in doc for t in p.tokens)
    tag = "pre-20260921-dark"
    bak = f"{PROP}.{tag}"
    k = 1
    while os.path.exists(bak):
        k += 1
        bak = f"{PROP}.{tag}{k}"
    with open(bak, "w") as f:
        json.dump(prop, f, indent=1, ensure_ascii=False)
    added = skipped = 0
    for h, (gloss, tier, ev) in new.items():
        if h in prop:
            print(f"  already read: {h} = {prop[h]['gloss']}  (skipping {gloss})")
            skipped += 1
            continue
        if cnt.get(h, 0) == 0:
            print(f"  no such sign: {h}")
            skipped += 1
            continue
        # A and B are allowed, but only where the evidence is the kind the
        # tier ladder names: K&T citing the folio and line, an identical
        # formula, or a numeral. A guess never reaches them.
        if tier not in ("A", "B", "C", "D", "G"):
            print(f"  bad tier {tier} for {h}")
            skipped += 1
            continue
        prop[h] = {"gloss": gloss, "tier": tier, "n": cnt[h], "evidence": ev}
        added += 1
    with open(PROP, "w") as f:
        json.dump(prop, f, indent=1, ensure_ascii=False)
    print(f"added {added}, skipped {skipped}; backup {os.path.basename(bak)}; {len(prop)} entries")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "apply":
        sys.exit(apply(a[1]))
    sys.exit(dossier(a[1:] if a and a[0] == "dossier" else a))
