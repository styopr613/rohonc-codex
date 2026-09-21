"""Guess a dark word from its neighbours, the whole reference corpus, and the
page image -- and MEASURE the corpus half before trusting it.

The passage pool (ktguess.py) asks: which words of the verse the folio cites
does no sign carry? For a word that occurs once that pool holds the answer
7.8% of the time. This asks a different question: the words on either side
of the hole ARE read -- so where in the whole reference corpus (both Bibles,
the Golden Legend, the apocrypha, the missal, the Holy Week office, the
mystery plays: data/ref/rohonc/ALL.txt) do those neighbours stand near each
other, and what word stands between them there?

THE TEST, declared before the run:

  Leave-one-out over rare read words (<= 3 occurrences), the same trial
  population ktguess.py --rare draws. Hide the word and its gloss; take the
  content stems of up to two read words on each side of it; find every
  corpus sentence where at least two of those stems (one, if only one is
  known) fall within a six-word window; collect the free words inside that
  window; rank by (sentences hit, neighbours matched) and then by rarity.
  Score top-1 and top-3 over ALL trials.

  BAR: the corpus guess is worth using as the first candidate only if its
  top-1 rate over all rare trials is at least 6.0%, three times the passage
  pool's measured 2.0%. Below that it is reported and ranked second.

    python3 ktfill.py --test 400       the measurement
    python3 ktfill.py 052v             every hole on a folio, with the three
                                       signals: neighbours + corpus, passage
                                       pool, and the page image written to
                                       the scratchpad for viewing
    python3 ktfill.py HEX ...          the same for named signs

The image: data/rohonc/scan/nat-NNN.png is one spread; the folio number is
written on the left page, which is the RECTO (the book reads right to
left): nat-052 is 052r on the left and 051v on the right. `page FOLIO` writes that half, doubled, to /tmp/claude-1001/.../scratchpad.
"""
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

import corpus
import ktaffix as A
import ktcross as K
import ktguess as G
import ktleft as L
import kttranslate as T

ALL = os.path.join(corpus.ROOT, "data", "ref", "rohonc", "ALL.txt")
SCAN = os.path.join(corpus.ROOT, "data", "rohonc", "scan")
SCRATCH = os.environ.get("SCRATCH", "/tmp/claude-1001/-home-ubuntu/0ad29937-eb69-403f-b92e-05f471a83479/scratchpad")
SEED = 20260921
WIN = 6


REF = os.path.join(corpus.ROOT, "data", "ref", "rohonc")
PUNCT = ("bible_dr_verses.txt", "bible_kjv_verses.txt", "missal_roman_1865.txt",
         "office_holy_week_1875.txt", "barlaam.txt")
STREAM = ("golden_legend.txt", "apocrypha_wake.txt", "plays_chester.txt",
          "plays_ntown.txt", "plays_towneley.txt", "plays_york.txt")


def sentences():
    """[[stem,...]] for every sentence of the corpus, and {stem: {sentence ids}}.

    ALL.txt has had its punctuation stripped, so the first version of this
    read the whole 1.7M-word corpus as ONE sentence and every guess came
    back empty. The punctuated sources are split on sentence marks; the
    stripped ones (Golden Legend, apocrypha, the plays) are cut into
    40-word windows overlapping by 20, which is a sentence for this purpose.
    """
    stopstem = {K.stem(w) for w in K.STOP}
    sents, index = [], defaultdict(set)

    def add(ws):
        if len(ws) < 3:
            return
        st = [K.stem(w) if (len(w) > 2 and w not in K.STOP) else None for w in ws]
        st = [x if (x is None or x not in stopstem) else None for x in st]
        sid = len(sents)
        sents.append(st)
        for x in set(st):
            if x:
                index[x].add(sid)

    for name in PUNCT:
        path = os.path.join(REF, name)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8", errors="ignore").read().lower()
        for s in re.split(r"[.;:!?]+", text):
            add(re.findall(r"[a-z]+", s))
    for name in STREAM:
        path = os.path.join(REF, name)
        if not os.path.exists(path):
            continue
        ws = re.findall(r"[a-z]+", open(path, encoding="utf-8", errors="ignore").read().lower())
        for i in range(0, len(ws), 20):
            add(ws[i:i + 40])
    return sents, index


def neighbours(tk, j, gl, seg, var, prop, hidden=None):
    """Content stems of up to two read words each side of position j."""
    left, right = [], []
    for k in range(j - 1, -1, -1):
        b = A.strip(tk[k])[0]
        if b == hidden:
            continue
        st = G.stem_of(T.render_token(tk[k], gl, seg, False, var, prop)
                       .replace("_", " ").replace("-", " ").lstrip("+~?°"))
        st = {s for s in st if s and not s.startswith("[")}
        if st:
            left.append(st)
        if len(left) == 2:
            break
    for k in range(j + 1, len(tk)):
        b = A.strip(tk[k])[0]
        if b == hidden:
            continue
        st = G.stem_of(T.render_token(tk[k], gl, seg, False, var, prop)
                       .replace("_", " ").replace("-", " ").lstrip("+~?°"))
        st = {s for s in st if s and not s.startswith("[")}
        if st:
            right.append(st)
        if len(right) == 2:
            break
    return left, right


def guess(left, right, sents, index, taken, freq, exclude=()):
    """Ranked [(stem, sentences_hit, best_match)] from the corpus.

    Sentence SETS per neighbour group are intersected first, so a common
    neighbour ("Lord": tens of thousands of postings) costs one set operation
    instead of a scan. The first version walked every posting and did not
    finish 400 trials in ten minutes.
    """
    groups = left + right
    if not groups:
        return []
    need = 2 if len(groups) >= 2 else 1
    sets = []
    for grp in groups:
        s = set()
        for st in grp:
            s |= index.get(st, set())
        sets.append(s)
    if need == 2:
        cands = set()
        for a in range(len(sets)):
            for b in range(a + 1, len(sets)):
                cands |= sets[a] & sets[b]
    else:
        cands = sets[0]
    if len(cands) > 4000:
        cands = set(sorted(cands)[:4000])
    score, seen, best = Counter(), Counter(), {}
    for sid in cands:
        st = sents[sid]
        gpos = defaultdict(list)
        for p, w in enumerate(st):
            if w:
                for gi, grp in enumerate(groups):
                    if w in grp:
                        gpos[gi].append(p)
        if len(gpos) < need:
            continue
        positions = sorted(p for ps in gpos.values() for p in ps)
        ok = False
        for i in range(len(positions)):
            span = [p for p in positions if positions[i] <= p <= positions[i] + WIN]
            grps = {gi for gi, ps in gpos.items() if any(p in span for p in ps)}
            if len(grps) >= need:
                ok = True
                lo, hi = min(span), max(span)
                break
        if not ok:
            continue
        pset = set(positions)
        for p in range(max(0, lo - 2), min(len(st), hi + 3)):
            w = st[p]
            if not w or w in taken or w in exclude or p in pset:
                continue
            score[w] += len(grps)
            seen[w] += 1
            if len(grps) > best.get(w, 0):
                best[w] = len(grps)
    return sorted(((w, seen[w], best[w]) for w in score),
                  key=lambda r: (-r[2], -r[1], freq.get(r[0], 0), r[0]))


def page_image(folio):
    """Write the half-spread for a folio to the scratchpad; return the path."""
    from PIL import Image
    # The codex reads right to left, so a spread shows the RECTO of leaf N on
    # the LEFT (the leaf number is written there: "52" on nat-052's left page,
    # "202" on nat-202's) and the verso of leaf N-1 on the right. The first
    # version had this backwards and served 132v as 134r.
    n, side = int(folio[:3]), folio[3]
    spread = n if side == "r" else n + 1
    src = os.path.join(SCAN, f"nat-{spread:03d}.png")
    if not os.path.exists(src):
        return None
    im = Image.open(src)
    w, h = im.size
    box = (0, 0, w // 2, h) if side == "r" else (w // 2, 0, w, h)
    out = im.crop(box).resize(((w // 2) * 2, h * 2), Image.LANCZOS)
    os.makedirs(SCRATCH, exist_ok=True)
    path = os.path.join(SCRATCH, f"{folio}.png")
    out.save(path)
    return path


def passage_sents(vv, vd, refs, wide=1):
    """The cited verses of both Bibles as a small sentence set + index."""
    sents, index = [], defaultdict(set)
    stopstem = {K.stem(w) for w in K.STOP}
    for _, txt in L.passage(vv, refs, wide) + L.passage(vd, refs, wide):
        for s in re.split(r"[.;:!?]+", txt.lower()):
            ws = re.findall(r"[a-z]+", s)
            if len(ws) < 3:
                continue
            st = [K.stem(w) if (len(w) > 2 and w not in K.STOP) else None for w in ws]
            st = [x if (x is None or x not in stopstem) else None for x in st]
            sid = len(sents)
            sents.append(st)
            for x in set(st):
                if x:
                    index[x].add(sid)
    return sents, index


def rankers(left, right, sents, index, psents, pindex, pool, taken, freq):
    """Three ranked candidate lists: corpus, passage-positional, fusion."""
    corp = [w for w, _, _ in guess(left, right, sents, index, taken, freq)]
    pos = [w for w, _, _ in guess(left, right, psents, pindex, taken, freq)] if psents else []
    if not pos and psents:
        # fall back to one neighbour when the passage is too short for two
        pos = [w for w, _, _ in guess(left[:1] or right[:1], [] if left else right[1:2],
                                       psents, pindex, taken, freq)]
    rare = sorted(pool, key=lambda s: (freq.get(s, 0), s))
    fus, seen = [], set()
    for w in pos + rare + corp:
        if w not in seen and w not in taken:
            seen.add(w)
            fus.append(w)
    return corp, pos, fus


def test(n_sample):
    gl, doc, seg, var, prop, inv = K.build()
    sents, index = sentences()
    vv, vd = L.verses(), L.verses_dr()
    cited = {}
    for p in sorted({p.page for p in doc}):
        r = L.refs_in(K.note_for(p))
        if r:
            cited[p] = r
    freq = Counter()
    for st in sents:
        freq.update(x for x in st if x)
    known = {}
    for c, senses in gl.items():
        st = set()
        for g in senses:
            st |= G.stem_of(g)
        if st:
            known[c] = st
    for c, (g, tier) in prop.items():
        st = G.stem_of(g.replace("_", " "))
        if st:
            known[c] = st
    base_idx = K.taken_index(gl, prop)
    owners = defaultdict(set)
    for st, hs in base_idx.items():
        for sign, _ in hs:
            owners[st].add(sign)
    occ = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    trials = []
    for p in doc:
        for ln in p.lines:
            tk = [t for run in ln for t in run]
            for j, t in enumerate(tk):
                b = A.strip(t)[0]
                if b in known and occ[b] <= 3:
                    trials.append((p.page, tk, j, b))
    random.Random(SEED).shuffle(trials)
    trials = trials[:n_sample] if n_sample else trials
    names = ("corpus", "passage-positional", "fusion")
    top1, top3, anyw = Counter(), Counter(), Counter()
    pcache = {}
    for pg, tk, j, b in trials:
        truth = known[b]
        h = K.hx(b)
        taken = {st for st in base_idx if not (st in truth and owners[st] <= {h})}
        left, right = neighbours(tk, j, gl, seg, var, prop, hidden=b)
        psents, pindex, pool = [], {}, {}
        if pg in cited:
            if pg not in pcache:
                pcache[pg] = passage_sents(vv, vd, cited[pg])
            psents, pindex = pcache[pg]
            idx = {st: v for st, v in base_idx.items() if st not in truth or not owners[st] <= {h}}
            both, dro, kjo, syn = L.pools_for(vv, vd, cited[pg], idx, 0)
            pool = {**both, **dro}
        lists = rankers(left, right, sents, index, psents, pindex, pool, taken, freq)
        for name, cand in zip(names, lists):
            pos = [i for i, w in enumerate(cand) if w in truth]
            if pos:
                anyw[name] += 1
                top1[name] += pos[0] == 0
                top3[name] += pos[0] < 3
    n = len(trials)
    print("LEAVE-ONE-OUT: three rankers on rare read words (<=3 occurrences), hidden one at a time")
    print(f"  hidden rare words tested   {n}")
    print(f"  {'ranker':22s} {'anywhere':>10s} {'top-1':>8s} {'top-3':>8s}   bar 6.0% top-1")
    for name in names:
        print(f"  {name:22s} {anyw[name]/n*100:9.1f}% {top1[name]/n*100:7.1f}% {top3[name]/n*100:7.1f}%   "
              f"{'PASS' if top1[name]/n*100 >= 6.0 else 'FAIL'}")
    print("  passage pool alone (ktguess --rare 400): top-1 2.0%, top-3 4.5%")
    return 0


def show(argv):
    gl, doc, seg, var, prop, inv = K.build()
    sents, index = sentences()
    freq = Counter()
    for st in sents:
        freq.update(x for x in st if x)
    taken = set(K.taken_index(gl, prop))
    vv, vd = L.verses(), L.verses_dr()
    folios = [a for a in argv if re.fullmatch(r"\d{3}[rv]", a)]
    hexes = {a for a in argv if re.fullmatch(r"[0-9a-f]{3,}", a)}
    done_img = {}
    for p in doc:
        if folios and p.page not in folios:
            continue
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            for j, t in enumerate(tk):
                b = A.strip(t)[0]
                if b in inv:
                    continue
                h = K.hx(b)
                if hexes and h not in hexes:
                    continue
                s = " ".join("<<___>>" if k == j else T.render_token(x, gl, seg, False, var, prop)
                             for k, x in enumerate(tk))
                print(f"=== {h}   {p.page}:{i}")
                print(f"  line    {s[:170]}")
                left, right = neighbours(tk, j, gl, seg, var, prop)
                print(f"  context {' '.join('/'.join(sorted(g)) for g in reversed(left))}  [x]  "
                      f"{' '.join('/'.join(sorted(g)) for g in right)}")
                cand = guess(left, right, sents, index, taken, freq)
                print("  corpus  " + (", ".join(f"{w}({n})" for w, n, m in cand[:10]) or "nothing"))
                r = L.refs_in(K.note_for(p.page))
                if r:
                    both, dro, kjo, syn = L.pools_for(vv, vd, r, K.taken_index(gl, prop), 0)
                    pool = {**both, **dro}
                    top = sorted(pool, key=lambda s: (freq.get(s, 0), s))[:10]
                    print("  passage " + ", ".join(sorted(pool[s], key=lambda w: -pool[s][w])[0] for s in top))
                if p.page not in done_img:
                    done_img[p.page] = page_image(p.page)
                print(f"  image   {done_img[p.page]}")
                print()
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--test" in a:
        n = next((int(x) for x in a if x.isdigit()), 0)
        sys.exit(test(n))
    if a and a[0] == "page":
        print(page_image(a[1]))
        sys.exit(0)
    sys.exit(show(a))
