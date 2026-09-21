"""TEST 15: passage identification by an outside reader, from K&T's words.

Gemini's first ask: an independent party identifies what each folio
retells, from the dictionary alone, without our notes. Test 11 did this
mechanically with a bag of stems against every chapter of the Bible. This
hands the same pages to a reader who knows the Bible -- DeepSeek V4 Pro
through OpenRouter, temperature 0 -- and asks which chapter the page
retells. Our notes, our readings and our translation are not in the
prompt.

  the first 20 folios of Test 14's sample (its REAL arm), rendered in
  K&T's words only, gaps as [?n]; halved from 40 before the run for cost
  CONTROL: the same 40 pages with K&T's glosses shuffled among their
  signs, the seed of Test 11 -- the same English words on the wrong signs

  chapter hit   the reader's (book, chapter) is one the note cites
  book hit      the reader's book is one the note cites

BARS, declared before the run, not moved:
  FAIL if the real pages do not beat the shuffled pages on chapter hits at
  p < 0.01 (sign test on discordant folios), or if the real chapter-hit
  rate is under 25% -- twice what the bag of stems managed in Test 11. A
  reader who knows the Bible and has six words in ten of a page should do
  better than a bag of stems, or the words are not carrying the story.

    python3 ktpassid2.py     (replies cached under work/rohonc/outside/passid/)
"""
import json
import math
import os
import random
import re
import sys
from concurrent.futures import ThreadPoolExecutor

import ktaffix as A
import ktcross as K
import ktleft as L
import ktblindfill as B
import ktor
import kttestlib as TL

SEED = 20260921
MODEL = B.MODEL
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "work", "rohonc", "outside", "passid")

PROMPT = """Below is one page of a sixteenth-century manuscript written in an unknown script, transcribed sign by sign. Where the published dictionary of the script gives an English word for a sign, that word is printed. Signs the dictionary does not read are printed as numbered gaps, [?1], [?2] and so on. Word order is the manuscript's own. The manuscript is believed to retell Christian scripture.

Which passage of the Bible does this page retell? Answer with the book and chapter, and the verses if you can. If you cannot tell, give null for the book.

Answer ONLY with JSON: {{"book": "...", "chapter": n, "verses": "a-b", "confidence": 0.0 to 1.0}}

PAGE
{page}
"""


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    refs = TL.cited(doc)
    vd = L.verses_dr()
    chosen, arms = B.sample(doc, refs, vd, gl, var)
    chosen = chosen[:20]
    pages = {pg.page: pg for pg in doc}
    os.makedirs(OUT, exist_ok=True)
    signs = sorted(gl)
    perm = signs[:]
    random.Random(SEED + 1).shuffle(perm)
    gl_shuf = {a: gl[b] for a, b in zip(signs, perm)}

    jobs = []
    for f in chosen:
        for cond, g in (("real", gl), ("shuffled", gl_shuf)):
            lines, gaps = B.render_page(pages[f], g, var)
            jobs.append((f, cond, PROMPT.format(page="\n".join(lines))))

    def run(job):
        f, cond, prompt = job
        path = os.path.join(OUT, f"{f}_{cond}.json")
        if os.path.exists(path):
            try:
                if isinstance(json.load(open(path, encoding="utf-8")).get("reply"), str):
                    return f
            except Exception:
                pass
            os.remove(path)          # an empty reply (thinking budget spent) is fetched again
        if not os.path.exists(path):
            txt, usage = ktor.ask(MODEL, prompt)
            json.dump({"folio": f, "cond": cond, "reply": txt, "usage": usage, "prompt": prompt},
                      open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    with ThreadPoolExecutor(4) as ex:
        list(ex.map(run, jobs))

    print("TEST 15: PASSAGE IDENTIFICATION BY AN OUTSIDE READER, K&T'S WORDS ONLY")
    print(f"  reader {MODEL}; {len(chosen)} folios; seed {SEED}\n")
    hits = {"real": {}, "shuffled": {}}
    bookhits = {"real": {}, "shuffled": {}}
    cost = 0.0
    detail = []
    for f, cond, _ in jobs:
        d = json.load(open(os.path.join(OUT, f"{f}_{cond}.json"), encoding="utf-8"))
        u = d.get("usage") or {}
        cost += float(u.get("cost") or (u.get("cost_details") or {}).get("upstream_inference_cost") or 0)
        m = re.search(r"\{.*\}", d["reply"], re.S)
        try:
            ans = json.loads(m.group(0))
        except Exception:
            ans = {}
        cited = {(b, c) for b, c, _, _ in refs[f]}
        got = None
        if ans.get("book"):
            r = L.refs_in(f"{ans['book']} {ans.get('chapter') or 0}")
            if r:
                got = (r[0][0], r[0][1])
        hits[cond][f] = got in cited if got else False
        bookhits[cond][f] = bool(got) and got[0] in {b for b, _ in cited}
        if cond == "real":
            detail.append((f, sorted(cited)[0], got))
    for f, c, got in detail:
        print(f"    {f}  cited {c[0]} {c[1]:<4d} reader {got[0] + ' ' + str(got[1]) if got else 'null':22s}"
              f" {'HIT' if hits['real'][f] else ''}")
    n = len(chosen)
    hr, hs = sum(hits["real"].values()), sum(hits["shuffled"].values())
    br, bs = sum(bookhits["real"].values()), sum(bookhits["shuffled"].values())
    disc_r = sum(1 for f in chosen if hits["real"][f] and not hits["shuffled"][f])
    disc_s = sum(1 for f in chosen if hits["shuffled"][f] and not hits["real"][f])
    p = sum(math.comb(disc_r + disc_s, i) for i in range(disc_r, disc_r + disc_s + 1)) / 2 ** (disc_r + disc_s) if disc_r + disc_s else 1.0
    print(f"\n  {'condition':10s}{'chapter hit':>13s}{'book hit':>10s}")
    print(f"  {'real':10s}{hr:8d}/{n:<3d}{hr/n*100:5.1f}%{br:6d}/{n:<3d}{br/n*100:5.1f}%")
    print(f"  {'shuffled':10s}{hs:8d}/{n:<3d}{hs/n*100:5.1f}%{bs:6d}/{n:<3d}{bs/n*100:5.1f}%")
    print(f"  discordant folios real-only {disc_r}, shuffled-only {disc_s}, sign test p = {p:.2e}")
    print(f"  Test 11's bag of stems on all 298 folios: top-1 12.4%")
    print(f"  cost ${cost:.3f}")
    ok = p < 0.01 and hr / n >= 0.25
    print(f"  BAR: p < 0.01 and real chapter hit >= 25%  ->  {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
