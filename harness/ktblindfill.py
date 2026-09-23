"""TEST 14: the blind rotated run, with an outside reader.

The one test every reviewer asked for and Test 10 could not deliver by
machine: run the gap-filling loop on pages that have been handed the WRONG
passage, and see whether it still produces readings. If a reader with a
passage in hand fills gaps at the same rate whether or not the passage is
the page's, the loop manufactures readings and the 670 need a different
defence.

THE RUN, declared before it is made:
  * 40 cited folios drawn by seed from those with a Douay passage of at
    least three verses and at least five signs K&T did not read;
  * the first 20 get their own cited passage (REAL), the other 20 get the
    passage of the cited folio seventeen places on (ROTATED);
  * each page is rendered in K&T's words only -- their glosses and listed
    variants, nothing of ours, no segmentation -- with every unread sign
    shown as a numbered gap, the same number for the same sign;
  * the reader (DeepSeek V4 Pro through OpenRouter, temperature 0) is told
    nothing about arms. It is asked whether the page retells the passage,
    and, for each gap, to give one English word if the passage and the
    surrounding words determine it, else "none";
  * replies are saved raw before anything is scored.

SCORING:
  match     the reader says the page retells the passage
  fills     gaps given a word, per folio
  agree     in the REAL arm, a filled gap whose sign has a reading of ours,
            and the reader's word is our first sense by the strict lemma
            rule of Test 12; reported for tiers A/B and for all tiers,
            beside the ROTATED arm's agreement, which is what agreement by
            accident looks like.

BARS, declared before the run, not moved:
  MANUFACTURE  FAIL if fills per folio in the ROTATED arm are at least half
               the REAL arm's. Test 10's clause, on the actual loop.
  DETECTION    FAIL if the reader does not say "matches" more often in the
               REAL arm than the ROTATED at p < 0.01 (Fisher, one-sided).
  Agreement with ours is reported against the blindfold's bands: it is a
  fresh reader on the same evidence, and a fresh reader scored 16.7%
  strict on K&T's own words.

    python3 ktblindfill.py            (score the cached replies; no network)
    python3 ktblindfill.py --refresh  (request replies that are not cached)
"""
import json
import math
import os
import random
import re
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import ktaffix as A
import ktcross as K
import ktleft as L
import kttranslate as T
import ktor
import ktstrict as ST
import kttestlib as TL

SEED = 20260921
N = 40
OFFSET = 17
MODEL = "deepseek/deepseek-v4-pro-0813"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "work", "rohonc", "outside", "blindfill")


def fisher_greater(a, b, c, d):
    """one-sided P for table [[a,b],[c,d]] that row 1 has the higher rate"""
    n = a + b + c + d
    r1, c1 = a + b, a + c
    def h(x):
        return math.comb(r1, x) * math.comb(n - r1, c1 - x) / math.comb(n, c1)
    return sum(h(x) for x in range(a, min(r1, c1) + 1))


def reading_of(s, ours, seg, var, gl):
    """(tier, gloss) of our reading of an unread sign, or ('', '')."""
    if s in ours:
        return ours[s]
    if s in seg:
        parts = []
        for q in seg[s]:
            if q in gl:
                parts.append(sorted(gl[q])[0])
            elif q in ours:
                parts.append(ours[q][1])
            elif q in var and var[q] in gl:
                parts.append(sorted(gl[var[q]])[0])
        return ("cut", " ".join(parts)) if parts else ("", "")
    if s in var and var[s] in gl:
        return ("var", sorted(gl[var[s]])[0])
    return ("", "")


def render_page(pg, gl, var):
    gaps, lines = {}, []
    for ln in pg.lines:
        out = []
        for run in ln:
            for t in run:
                b = A.strip(t)[0]
                if b in gl or b in var:
                    out.append(T.render_token(t, gl, {}, False, var, None).replace("~", ""))
                else:
                    if b not in gaps:
                        gaps[b] = len(gaps) + 1
                    out.append(f"[?{gaps[b]}]")
        lines.append(" ".join(out))
    return lines, gaps


def sample(doc, refs, vd, gl, var):
    ok = []
    for pg in doc:
        if pg.page not in refs:
            continue
        verses = L.passage(vd, refs[pg.page])
        unread = {A.strip(t)[0] for t in pg.tokens if A.strip(t)[0] not in gl and A.strip(t)[0] not in var}
        if len(verses) >= 3 and len(unread) >= 5:
            ok.append(pg.page)
    ok.sort()
    rng = random.Random(SEED)
    chosen = rng.sample(ok, N)
    cited = sorted(refs)
    arms = {}
    for i, f in enumerate(chosen):
        if i < N // 2:
            arms[f] = ("REAL", f)
        else:
            j = cited.index(f)
            own = {(b, c) for b, c, _, _ in refs[f]}
            k = OFFSET
            # step on past any folio that happens to cite the same chapter
            while {(b, c) for b, c, _, _ in refs[cited[(j + k) % len(cited)]]} & own:
                k += 1
            arms[f] = ("ROTATED", cited[(j + k) % len(cited)])
    return chosen, arms


PROMPT = """Below is one page of a sixteenth-century manuscript written in an unknown script, transcribed sign by sign. Where the published dictionary of the script gives an English word for a sign, that word is printed. Signs the dictionary does not read are printed as numbered gaps, [?1], [?2] and so on; the same number always means the same sign. Word order is the manuscript's own.

After the page is a passage from the Bible in the Douay-Rheims translation.

Task 1. Does this page retell this passage? Judge only from the words you can see.
Task 2. For each gap, if the passage together with the words around the gap determines what the sign means, give ONE English word in its base form. If it does not determine it, answer "none". Do not guess. Fill a gap only when you are confident.

Answer ONLY with JSON of this shape:
{{"matches": true or false, "confidence": 0.0 to 1.0, "fills": {{"1": "word or none", "2": "word or none", ...}}}}

PAGE {folio}
{page}

PASSAGE
{passage}
"""


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    refs = TL.cited(doc)
    vd = L.verses_dr()
    chosen, arms = sample(doc, refs, vd, gl, var)
    pages = {pg.page: pg for pg in doc}
    os.makedirs(OUT, exist_ok=True)
    p = json.load(open('proposals.json', encoding='utf-8'))
    un = lambda h: "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))
    ours = {un(h): (v['tier'], v['gloss']) for h, v in p.items()
            if isinstance(v, dict) and v.get('tier') in 'ABCDG'}

    jobs = []
    for f in chosen:
        arm, src = arms[f]
        lines, gaps = render_page(pages[f], gl, var)
        passage = "\n".join(f"{k[0]} {k[1]}:{k[2]} {txt}" for k, txt in L.passage(vd, refs[src])[:60])
        prompt = PROMPT.format(folio=f, page="\n".join(lines), passage=passage)
        jobs.append((f, arm, src, gaps, prompt))
    json.dump({f: {"arm": a, "passage_of": s} for f, (a, s) in arms.items()},
              open(os.path.join(OUT, "manifest.json"), "w"), indent=1)

    refresh = "--refresh" in argv

    def run(job):
        f, arm, src, gaps, prompt = job
        path = os.path.join(OUT, f"{f}.json")
        if os.path.exists(path):
            try:
                if isinstance(json.load(open(path, encoding="utf-8")).get("reply"), str):
                    return f
            except Exception:
                pass
            os.remove(path)          # an empty reply (thinking budget spent) is fetched again
        if not os.path.exists(path) and not refresh:
            return f
        if not os.path.exists(path):
            try:
                txt, usage = ktor.ask(MODEL, prompt)
            except Exception as e:          # no answer: the page is reported, not scored
                print(f"  no answer for {f}: {str(e)[:80]}")
                return f
            json.dump({"folio": f, "reply": txt, "usage": usage, "prompt": prompt},
                      open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        return f

    with ThreadPoolExecutor(4) as ex:
        list(ex.map(run, jobs))

    print("TEST 14: THE BLIND ROTATED RUN, OUTSIDE READER")
    print(f"  reader {MODEL}; {N} folios, {N//2} real, {N//2} rotated by {OFFSET}; seed {SEED}\n")
    stat = {"REAL": defaultdict(int), "ROTATED": defaultdict(int)}
    cost = 0.0
    rows = []
    missing = [f for f, *_ in jobs if not os.path.exists(os.path.join(OUT, f"{f}.json"))]
    if missing:
        print(f"  pages with no answer, not scored: {', '.join(missing)}\n")
    for f, arm, src, gaps, prompt in jobs:
        if f in missing:
            continue
        d = json.load(open(os.path.join(OUT, f"{f}.json"), encoding="utf-8"))
        u = d.get("usage") or {}
        cost += float(u.get("cost") or (u.get("cost_details") or {}).get("upstream_inference_cost") or 0)
        m = re.search(r"\{.*\}", d["reply"], re.S)
        try:
            ans = json.loads(m.group(0))
        except Exception:
            ans = {"matches": None, "fills": {}}
        st = stat[arm]
        st["folios"] += 1
        st["gaps"] += len(gaps)
        st["match"] += bool(ans.get("matches"))
        fills = {k: v for k, v in (ans.get("fills") or {}).items()
                 if isinstance(v, str) and v.strip() and v.strip().lower() != "none"}
        st["fills"] += len(fills)
        byno = {n: s for s, n in gaps.items()}
        agree = {"AB": [0, 0], "ALL": [0, 0]}
        for n, w in fills.items():
            s = byno.get(int(n)) if str(n).isdigit() else None
            if s is None:
                continue
            # our reading of this sign as the full rendering gives it: a
            # proposal (tier marked), a composition of read parts, or a
            # variant K&T's own rule licenses. K&T's own glosses never
            # appear here because those signs were not gaps.
            tier, g = reading_of(s, ours, seg, var, gl)
            if not g:
                continue
            hit = any(any(ST.same(a, b) for b in ST.words(ST.first_sense(g))) for a in ST.words(w))
            for key in (("AB",) if tier in "AB" else ()) + ("ALL",):
                agree[key][1] += 1
                agree[key][0] += hit
            rows.append((arm, f, K.hx(s), w, tier, g, hit))
        for key in agree:
            st[f"agree_{key}"] += agree[key][0]
            st[f"tested_{key}"] += agree[key][1]
    print(f"  {'arm':9s}{'folios':>7s}{'gaps':>6s}{'matches':>9s}{'fills':>7s}{'fills/folio':>12s}"
          f"{'A/B agree':>12s}{'all tiers agree':>17s}")
    for arm in ("REAL", "ROTATED"):
        st = stat[arm]
        ab = f"{st['agree_AB']}/{st['tested_AB']}"
        al = f"{st['agree_ALL']}/{st['tested_ALL']}"
        print(f"  {arm:9s}{st['folios']:7d}{st['gaps']:6d}{st['match']:9d}{st['fills']:7d}"
              f"{st['fills']/max(1,st['folios']):12.1f}{ab:>12s}{al:>17s}")
    print()
    for arm, f, h, w, tier, g, hit in rows:
        if arm == "REAL":
            print(f"    {f} {h:22s} reader '{w[:16]:16s}' ours {tier:3s} '{g[:20]:20s}' {'AGREE' if hit else ''}")
    r, o = stat["REAL"], stat["ROTATED"]
    fpf_r = r["fills"] / max(1, r["folios"])
    fpf_o = o["fills"] / max(1, o["folios"])
    pf = fisher_greater(r["match"], r["folios"] - r["match"], o["match"], o["folios"] - o["match"])
    a = fpf_o < 0.5 * fpf_r
    b = pf < 0.01
    print(f"\n  fills per folio: real {fpf_r:.1f}, rotated {fpf_o:.1f}   "
          f"-> rotated is {fpf_o/max(fpf_r,1e-9)*100:.0f}% of real   MANUFACTURE {'ok' if a else 'FAIL'}")
    print(f"  says it matches: real {r['match']}/{r['folios']}, rotated {o['match']}/{o['folios']}   "
          f"p = {pf:.2e}   DETECTION {'ok' if b else 'FAIL'}")
    ab_r = r["agree_AB"] / max(1, r["tested_AB"])
    ab_o = o["agree_AB"] / max(1, o["tested_AB"])
    print(f"  agreement with our A/B readings on filled gaps: real {ab_r*100:.1f}% "
          f"({r['agree_AB']}/{r['tested_AB']}), rotated {ab_o*100:.1f}% ({o['agree_AB']}/{o['tested_AB']})"
          f"   blindfold band: {'>= 50%' if ab_r >= .5 else '30-50%' if ab_r >= .3 else '15-30%' if ab_r >= .15 else '< 15%'}")
    print(f"  cost ${cost:.3f}")
    print(f"  BAR  ->  {'PASS' if a and b else 'FAIL'}")
    return 0 if a and b else 1


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main(sys.argv[1:]))
