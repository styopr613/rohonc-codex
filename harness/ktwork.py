"""Locate a folio in a named non-biblical source, and pool candidates from it.

Most of the Rohonc is not scripture. It is liturgy and legend -- the
Reproaches of Good Friday, the apologue of the man in the pit, saints'
lives, the Gospel of Nicodemus -- and those pages have been reading as
"coherent but untestable", because ktleft.py can only pool from a chapter
and verse. This closes that gap for the works whose texts are here.

THE HUMAN ASSERTS THE WORK; THE MACHINE FINDS THE PASSAGE. A folio is only
searched in a work its own translation note names. Nothing here decides that
a page comes from Barlaam; a person already wrote that down. What this does
is find where in Barlaam, and say whether that location is trustworthy.

THE FIRST VERSION OF THIS FAILED, AND THE FAILURE IS THE REASON FOR THE
SECOND. It scored a window by how many DISTINCT stems of the folio it
contained, and required the best window to stand 4 sigma above the mean
window of the work. Every folio cleared that bar -- 4.2 to 4.6 sigma -- and
every answer was wrong. Folio 148v, whose apologue of the man in the pit had
already been matched to Barlaam by hand (the unicorn, the pit, the tree, the
two mice one white and one black), was placed instead in a passage about the
devil renouncing the good, because that passage happens to contain man,
evil, good, glory and honour. Counting distinct matches treats *mouse* and
*evil* as worth the same, and in a devotional corpus the common religious
words decide every contest. The sigma bar was not too low; the statistic was
measuring the wrong thing.

THE SECOND VERSION ALSO FAILED ITS OWN BAR, AND THAT IS RECORDED TOO.
Weighting each matched stem by its inverse document frequency -- a stem
occurring f times in a work of N words is worth log(N/f), so *mouse*
outweighs *lord* by the amount the work itself says it should -- fixed the
answer for Barlaam: the best window is the interpretation of the apologue
and it carries the unicorn, the pit, the tree and the two mice together.
But the declared bar was 6 sigma above the mean window and it scored 5.5,
which is a miss, and 048v scored 4.5 and landed on Pilate's hall rather
than the Reproaches. Neither figure was moved afterwards.

THE THIRD VERSION REPLACES THE CHANCE CALCULATION WITH A MATCHED CONTROL,
which is what this project requires everywhere else and what should have
been here from the start. Sigma over sliding windows is not a real null:
adjacent windows share 149 of their 150 words, so the scores are heavily
autocorrelated and the standard deviation of that series does not describe
the spread of independent draws. The control has to be made of the same
stuff as the claim.

THE THIRD VERSION FAILED THAT CONTROL OUTRIGHT, AND THE FAILURE NAMED ITS
OWN CAUSE. Folio 148v, which demonstrably contains the Barlaam apologue,
scored 57.0 in Barlaam while the best of 24 unrelated codex folios scored
98.2; it beat only 5 of the 24. The reason is a length confound the control
existed to expose: the score was a SUM over matched stems, so a folio with
sixty readable content words outscores one with twenty-three whatever the
work is. 148v has 23. The control was right and the statistic was wrong
again.

THE BAR, fixed before the fourth run and not moved.

  Score a window by the fraction of the FOLIO's own information it accounts
  for: the inverse-document-frequency mass of the folio stems inside the
  window, divided by the idf mass of all that folio's stems that occur in
  the work at all. That is bounded in [0, 1] and does not reward a folio for
  being long, so folios are comparable.

      for folio P asserted to come from work W, a localisation is USABLE
      only if P's best window outscores the best window of EVERY ONE of 24
      other codex folios, drawn by a fixed seed from folios whose notes do
      NOT name W, measured the same normalised way.

  A rank rule over real folios, with nothing in it to tune after the fact.

  AND, before any of its output is used, it must reproduce two answers that
  are already known independently of it:

      148v must land on the unicorn, the pit, the tree and the two mice
           in Barlaam, which a person matched by reading.
      048v must land on the Reproaches in the missal, which the folio's
           own note named before this file existed.

  If it cannot recover those, it does not get to propose anything about a
  folio nobody has read. `python ktwork.py --selftest` runs exactly that.
  Four versions of this have now been tried; if the fourth fails, the
  attempt is written up as a failure and its output is not used.

THE FOURTH VERSION FAILED TOO, AND THIS FILE IS A RECORD OF A FAILURE.
Normalising fixed the confound it was meant to fix -- 148v rose from beating
5 of 24 controls to beating 14 -- and it still did not beat them all:

    148v in Barlaam           0.348   best control 0.525   beat 14 of 24
    048v in the Roman Missal  0.262   best control 0.692   beat  1 of 24

and this is with the Barlaam window being RIGHT: it is the interpretation of
the apologue and it contains the unicorn, the pit, the tree and the two mice
together. The method finds the passage and cannot prove it found it.

WHY IT FAILS, WHICH IS THE USEFUL PART. A devotional page shares nearly all
its vocabulary with any other devotional text: lord, god, man, say, good,
evil, heaven, sin. What would localise a page is its rare words -- mouse,
unicorn, pit, cruse, Rabshakeh -- and those are exactly the words the codex
CANNOT READ YET, because rare words are the holes. So the readable part of a
folio is precisely its generic part, and generic vocabulary localises
nothing. The tool is weakest exactly where it would be most useful, and it
gets better only as the holes close, which is the thing it was supposed to
help with.

So nothing here proposes a reading. The corpora it was built for are worth
keeping anyway and are used by hand: reading the Barlaam text is what
confirmed 148v, including the detail that the apologue's own moral calls the
falling man "the race of ADAM", which is why the codex writes him with
Király & Tokai's Adam sign. That confirmation was made by a person reading,
not by this file.

OCR AND LATIN. The missal and the Holy Week office are Google scans of
19th-century two-column books, so the Latin and the English interleave and
the OCR invents words. A token is kept only if it occurs in the 1.75M words
of period English already in data/ref/rohonc/ALL.txt. That drops "Popule",
"metis" and "ingratUude" alike, and it is stated here rather than tuned:
anything the reference English never says is not offered as a candidate.

    python ktwork.py             # every folio whose note names a work here
    python ktwork.py 148v 048v   # those folios: the located passage and pool
    python ktwork.py --works     # the works, their files and their sizes
"""
import os
import re
import sys
from collections import Counter

import ktaffix as A
import ktcross as K
import ktleft as L
import kttranslate as T

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(os.path.dirname(HERE), "data", "ref", "rohonc")

WINDOW = 150
N_CONTROL = 24
SEED = 20260920
RARE_IDF = 6.0

# What a translation note may call a work -> the file that holds it.
WORKS = [
    (r"barlaam|josaphat|ioasaph|man in the (pit|well)", "barlaam.txt", "Barlaam and Ioasaph"),
    (r"improperia|reproaches|good friday|holy week|missal|the mass\b",
     "missal_roman_1865.txt", "Roman Missal (1865 English)"),
    (r"improperia|reproaches|holy week|tenebrae",
     "office_holy_week_1875.txt", "Office of Holy Week (1875)"),
    (r"golden legend|voragine|caxton", "golden_legend.txt", "Caxton's Golden Legend"),
    (r"nicodemus|protevangel|infancy|vita ada|life of adam|adam and eve|gospel of james",
     "apocrypha_wake.txt", "Apocryphal gospels (Wake)"),
    (r"york (play|cycle)", "plays_york.txt", "York plays"),
    (r"towneley", "plays_towneley.txt", "Towneley plays"),
    (r"chester (play|cycle)", "plays_chester.txt", "Chester plays"),
    (r"n-town|ludus coventriae", "plays_ntown.txt", "N-Town plays"),
]

_LEX = None


def lexicon():
    """Every word the 1.75M words of period English in ALL.txt actually use."""
    global _LEX
    if _LEX is None:
        p = os.path.join(REF, "ALL.txt")
        if not os.path.exists(p):
            _LEX = set()
        else:
            _LEX = set(re.findall(r"[a-z]+",
                                  open(p, encoding="utf-8", errors="ignore").read().lower()))
    return _LEX


def tokens(path):
    """The work as a list of lowercase English words, OCR noise dropped."""
    lex = lexicon()
    raw = re.findall(r"[A-Za-z]+",
                     open(path, encoding="utf-8", errors="ignore").read())
    return [w.lower() for w in raw if len(w) > 2 and (not lex or w.lower() in lex)]


def page_stems(page, doc, gl, seg, var, prop, inv):
    """The content-word stems this folio already reads, and its rendered lines."""
    stems, lines = set(), []
    stopstem = {K.stem(w) for w in K.STOP}
    for p in doc:
        if p.page != page:
            continue
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            if not tk:
                continue
            s = " ".join(("[?]" if A.strip(t)[0] not in inv
                          else T.render_token(t, gl, seg, False, var, prop)) for t in tk)
            lines.append((i, s))
            for w in re.findall(r"[a-zA-Z]+", s.replace("_", " ")):
                lw = w.lower()
                if len(lw) < 3 or lw in K.STOP:
                    continue
                st = K.stem(lw)
                if st not in stopstem:
                    stems.add(st)
    return stems, lines


def idf(toks):
    """{stem: log(N/f)} over a work -- how much a match on it is worth."""
    import math
    c = Counter(K.stem(w) for w in toks)
    n = sum(c.values())
    return {st: math.log(n / f) for st, f in c.items()}


def locate(toks, stems, weight):
    """(best normalised score, index, mean, sd, n, rare matched).

    The score is the idf mass of the folio's stems inside the window over
    the idf mass of every folio stem the work contains anywhere, so it is a
    fraction of what this folio could possibly match here and does not grow
    with how much of the folio is readable.
    """
    stemmed = [K.stem(w) for w in toks]
    n = len(stemmed)
    if n < WINDOW * 2:
        return 0.0, 0, 0.0, 0.0, 0, []
    total = sum(weight[st] for st in stems if st in weight)
    if total <= 0:
        return 0.0, 0, 0.0, 0.0, 0, []
    have = Counter()
    cur = 0.0
    scores = []
    for i, st in enumerate(stemmed):
        if st in stems:
            if have[st] == 0:
                cur += weight.get(st, 0.0)
            have[st] += 1
        if i >= WINDOW:
            out = stemmed[i - WINDOW]
            if out in stems:
                have[out] -= 1
                if have[out] == 0:
                    cur -= weight.get(out, 0.0)
        if i >= WINDOW - 1:
            scores.append(cur / total)
    m = sum(scores) / len(scores)
    sd = (sum((x - m) ** 2 for x in scores) / len(scores)) ** 0.5
    best = max(scores)
    at = scores.index(best)
    win = set(stemmed[at:at + WINDOW]) & stems
    rare = sorted((w for w in win if weight.get(w, 0) >= RARE_IDF),
                  key=lambda w: -weight[w])
    return best, at, m, sd, len(scores), rare


def controls(doc, work_pat, n=N_CONTROL):
    """n folios of the codex whose own notes do NOT name this work."""
    import random
    pool = [p.page for p in doc
            if not re.search(work_pat, K.note_for(p.page) or "", re.I)]
    return random.Random(SEED).sample(pool, min(n, len(pool)))


def judge(pg, f, pat, doc, gl, seg, var, prop, inv, tcache, wcache):
    """(best, at, rare, beaten, n) -- does this folio beat every control?"""
    if f not in tcache:
        tcache[f] = tokens(os.path.join(REF, f))
        wcache[f] = idf(tcache[f])
    toks, w = tcache[f], wcache[f]
    stems, lines = page_stems(pg, doc, gl, seg, var, prop, inv)
    best, at, m, sd, nw, rare = locate(toks, stems, w)
    ctrl = []
    for q in controls(doc, pat):
        qs, _ = page_stems(q, doc, gl, seg, var, prop, inv)
        b, *_ = locate(toks, qs, w)
        ctrl.append(b)
    beaten = sum(1 for c in ctrl if best > c)
    return best, at, rare, beaten, len(ctrl), lines, max(ctrl) if ctrl else 0.0


SELFTEST = {
    ("148v", "barlaam.txt", r"barlaam|josaphat|ioasaph|man in the (pit|well)"):
        ("mice", "pit", "tree", "unicorn"),
    ("048v", "missal_roman_1865.txt", r"improperia|reproaches|good friday|holy week|missal|the mass\b"):
        ("people", "egypt"),
}


def selftest(doc, gl, seg, var, prop, inv):
    """Recover two passages that are known independently of this file."""
    bad = 0
    tc, wc = {}, {}
    for (pg, f, pat), must in SELFTEST.items():
        best, at, rare, beaten, n, _, cmax = judge(pg, f, pat, doc, gl, seg, var,
                                                   prop, inv, tc, wc)
        win = " ".join(tc[f][at:at + WINDOW]).lower()
        hit = [x for x in must if x in win]
        ok = beaten == n and len(hit) >= len(must) - 1
        print(f"  {'ok  ' if ok else 'FAIL'} {pg} in {f}: score {best:.3f} vs best "
              f"control {cmax:.3f}; beat {beaten}/{n} controls; "
              f"found {hit} of {list(must)}")
        if not ok:
            print(f"       window: {win[:200]}")
            bad += 1
    print("  SELFTEST PASSES" if not bad else f"  SELFTEST FAILS ({bad})")
    return bad


def main(argv):
    if "--works" in argv:
        for pat, f, name in WORKS:
            p = os.path.join(REF, f)
            print(f"  {name:34s} {f:28s} "
                  f"{os.path.getsize(p) if os.path.exists(p) else 0:>9d} bytes")
        return 0

    gl, doc, seg, var, prop, inv = K.build()
    idx = K.taken_index(gl, prop)
    if "--selftest" in argv:
        return 1 if selftest(doc, gl, seg, var, prop, inv) else 0
    want = [a for a in argv if re.fullmatch(r"\d{3}[rv]", a)]

    pages = sorted({p.page for p in doc})
    todo = []
    for pg in pages:
        note = K.note_for(pg)
        if not note:
            continue
        for pat, f, name in WORKS:
            if re.search(pat, note, re.I) and os.path.exists(os.path.join(REF, f)):
                todo.append((pg, f, name, pat))
    if want:
        todo = [t for t in todo if t[0] in want]
    elif not todo:
        print("no translated folio names a work whose text is here")
        return 0

    if not want:
        print(f"{len({t[0] for t in todo})} folios name a work whose text is here")
        for pg, f, name, _ in todo:
            print(f"  {pg}  {name}")
        print("\nrun with folio numbers to locate and pool")
        return 0

    cache = {}
    wcache = {}
    for pg, f, name, pat in todo:
        best, at, rare, beaten, nc, lines, cmax = judge(pg, f, pat, doc, gl, seg,
                                                        var, prop, inv, cache, wcache)
        ok = beaten == nc
        print(f"\n=== {pg} in {name}")
        print(f"    best window scores {best:.3f}; best of {nc} control folios "
              f"scores {cmax:.3f}; beaten {beaten}/{nc}")
        print(f"    rare stems matched ({len(rare)}): {', '.join(rare[:10]) or 'none'}")
        if not ok:
            print(f"    NOT LOCALISED: the work fits {nc - beaten} unrelated folio(s) "
                  f"as well or better. No pool.")
            continue
        win = cache[f][at:at + WINDOW]
        print("    " + " ".join(win)[:520])
        free = L.pool(" ".join(win), idx)
        print(f"    {len(free)} content words in that passage carry no sign yet:")
        print("      " + L.show(free))
        for i, s in lines:
            if "[?]" in s:
                print(f"    {pg}:{i:<3d} {s[:140]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
