"""TEST 17: does Test 15's reader already know the answer?

Test 15 handed DeepSeek V3.2 twenty pages in K&T's words and it named the
cited chapter on 9 of 20, against 0 of 20 with the words shuffled. The
shuffle rules out a reader who finds the Bible in anything. It does not
rule out memory: Király and Tokai published which passage many folios
retell, and a model trained on that could recognise a page and recall the
chapter. A remembered page is recognised only in its real order, so memory
would also produce real-beats-shuffled.

This asks the same model, same settings (temperature 0, thinking off),
the same twenty folios by NUMBER ONLY -- no page, no words, no signs --
which Bible chapter the folio retells.

  chapter hit   the answer's (book, chapter) is one the folio's note cites,
                scored exactly as Test 15 scores it
  CONTROL       each answer scored against the OTHER folios' cited chapters:
                10,000 random derangements of answers over folios. This is
                what a reader gets by naming popular chapters with no memory
                of which folio is which.

BARS, declared before the run, not moved:
  MEMORY SHOWN if recall chapter hits >= 3 AND the derangement control
  gives p < 0.01 (share of derangements scoring at least as many hits).
  Otherwise NO MEMORY SHOWN.

  CONSEQUENCE, declared now: whatever the verdict, Test 15 is rescored on
  the folios whose recall answer was NOT a chapter hit, under Test 15's own
  bar (sign test p < 0.01 and real chapter hits >= 25%), and that result is
  reported beside the original. If MEMORY SHOWN, Test 15 is marked in
  TESTS.md as contaminated in part and the rescored figure is the one that
  stands.

What this cannot show: that the model knows nothing of K&T. A model can
fail to recall by folio number and still recognise a page's wording. This
tests recall by label, the cheap and likely route; it is reported as that.

    python3 ktmemory.py            (score the cached replies; no network)
    python3 ktmemory.py --refresh  (request replies that are not cached)
"""
import json
import os
import random
import re
import sys

import ktcross as K
import ktleft as L
import ktblindfill as B
import ktor
import kttestlib as TL

SEED = 20260929
MODEL = "deepseek/deepseek-v3.2"
EXTRA = {"reasoning": {"enabled": False}}
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "work", "rohonc", "outside", "memory")
PASSID = os.path.join(HERE, "..", "work", "rohonc", "outside", "passid")

PROMPT = """The Rohonc Codex is a manuscript of 448 pages in an undeciphered script, kept in Budapest. Király and Tokai (Cryptologia, 2018) and later work identified many of its pages as retelling particular passages of the Bible.

Which passage of the Bible does folio {folio} of the Rohonc Codex (page {page} of 448) retell? Answer from what you know about this manuscript. If you do not know, give null for the book.

Answer ONLY with JSON: {{"book": "...", "chapter": n, "confidence": 0.0 to 1.0}}
"""


def page_no(f):
    n, side = int(f[:-1]), f[-1]
    return 2 * n - 1 if side == "r" else 2 * n


def parse(reply):
    m = re.search(r"\{.*\}", reply or "", re.S)
    try:
        ans = json.loads(m.group(0))
    except Exception:
        return None
    if not ans.get("book"):
        return None
    r = L.refs_in(f"{ans['book']} {ans.get('chapter') or 0}")
    return (r[0][0], r[0][1]) if r else None


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    refs = TL.cited(doc)
    vd = L.verses_dr()
    chosen, arms = B.sample(doc, refs, vd, gl, var)
    chosen = chosen[:20]
    os.makedirs(OUT, exist_ok=True)

    refresh = "--refresh" in argv
    for f in chosen:
        path = os.path.join(OUT, f"{f}.json")
        if os.path.exists(path):
            continue
        if not refresh:
            print(f"TEST 17: no cached reply for {f}; use --refresh", file=sys.stderr)
            return 2
        prompt = PROMPT.format(folio=f, page=page_no(f))
        txt, usage = ktor.ask(MODEL, prompt, extra=EXTRA)
        json.dump({"folio": f, "reply": txt, "usage": usage, "prompt": prompt},
                  open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    cited = {f: {(b, c) for b, c, _, _ in refs[f]} for f in chosen}
    ans, cost = {}, 0.0
    for f in chosen:
        d = json.load(open(os.path.join(OUT, f"{f}.json"), encoding="utf-8"))
        u = d.get("usage") or {}
        cost += float(u.get("cost") or 0)
        ans[f] = parse(d["reply"])

    # Test 15's own real-arm answers, re-read from its cache
    t15 = {}
    for f in chosen:
        for cond in ("real", "shuffled"):
            d = json.load(open(os.path.join(PASSID, f"{f}_{cond}.json"), encoding="utf-8"))
            got = parse(d["reply"])
            t15[f, cond] = bool(got) and got in cited[f]

    hit = {f: bool(ans[f]) and ans[f] in cited[f] for f in chosen}
    h = sum(hit.values())
    rng = random.Random(SEED)
    n_perm, ge, tot = 10000, 0, 0
    for _ in range(n_perm):
        while True:
            p = chosen[:]
            rng.shuffle(p)
            if all(a != b for a, b in zip(chosen, p)):
                break
        k = sum(1 for a, b in zip(chosen, p) if ans[a] and ans[a] in cited[b])
        tot += k
        ge += k >= h
    pval = ge / n_perm

    print("TEST 17: RECALL BY FOLIO NUMBER, TEST 15'S READER, NO PAGE SHOWN")
    print(f"  reader {MODEL}; {len(chosen)} folios; seed {SEED}\n")
    for f in chosen:
        c = sorted(cited[f])[0]
        a = f"{ans[f][0]} {ans[f][1]}" if ans[f] else "null"
        print(f"    {f}  cited {c[0]} {c[1]:<4d} recall {a:22s} {'HIT' if hit[f] else '   '}"
              f"   Test 15 {'HIT' if t15[f, 'real'] else '-'}")
    answered = sum(1 for f in chosen if ans[f])
    n = len(chosen)
    print(f"\n  answered (not null)          {answered} / {n}")
    print(f"  recall chapter hits          {h} / {n}")
    print(f"  derangement control mean     {tot / n_perm:.2f}   p = {pval:.4f}")
    both = sum(1 for f in chosen if hit[f] and t15[f, 'real'])
    print(f"  of Test 15's {sum(t15[f, 'real'] for f in chosen)} hits, recalled by number  {both}")
    shown = h >= 3 and pval < 0.01
    print(f"  BAR: hits >= 3 and p < 0.01  ->  {'MEMORY SHOWN' if shown else 'NO MEMORY SHOWN'}")

    keep = [f for f in chosen if not hit[f]]
    hr = sum(t15[f, "real"] for f in keep)
    hs = sum(t15[f, "shuffled"] for f in keep)
    dr = sum(1 for f in keep if t15[f, "real"] and not t15[f, "shuffled"])
    ds = sum(1 for f in keep if t15[f, "shuffled"] and not t15[f, "real"])
    import math
    sp = (sum(math.comb(dr + ds, i) for i in range(dr, dr + ds + 1)) / 2 ** (dr + ds)) if dr + ds else 1.0
    ok = sp < 0.01 and hr / len(keep) >= 0.25
    print(f"\n  Test 15 rescored on the {len(keep)} folios not recalled:")
    print(f"    real {hr}/{len(keep)} {hr / len(keep) * 100:.1f}%   shuffled {hs}/{len(keep)}"
          f"   sign test p = {sp:.2e}   Test 15's bar -> {'PASS' if ok else 'FAIL'}")
    print(f"  cost ${cost:.4f}")
    return 0


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main(sys.argv[1:]))
