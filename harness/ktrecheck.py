"""THE FOUR-WAY BLANK TEST: do our weak readings survive their other pages?

160 readings of tier C, D and G stand on two or more pages. Each was made
from one passage. K&T's own method says a reading must survive every other
place its sign occurs. This carries each one there and asks.

How. For every page a sign stands on (the first line on that page, at most
six pages), the line is rendered as the edition renders it for the gates
(sign by sign, own=False), with EVERY copy of the sign blanked. A model
(DeepSeek V4 Pro, the model that writes the English) is shown the line and
four words: our reading and three decoys drawn, with a fixed seed, from the
glosses of other readings (never one whose stem is already on the line, never
a repeat). It answers with a letter. The order of the four is shuffled.

THE BAR, set 2026-09-26 before the first run, not to be moved:

1. The instrument has to work first. The same test runs on a calibration set:
   60 tier A readings (seed 20260926) that stand on two or more pages. Its
   matched control is the same lines and the same four words, scored for one
   decoy chosen in advance instead of the reading. The test counts as an
   instrument only if the tier A hit rate is at least 50% AND beats the
   control by 5 sigma (binomial on the control's own rate). If it does not,
   the run is recorded as a failure and NO weak reading is judged by it.

2. If it works, each weak reading is sorted by what the model picked:
     holds   -- picked on every page it was tested on
     fails   -- picked on no page
     mixed   -- anything between
   From the tier A per-page rate r, the number of CORRECT readings expected
   to "fail" by chance is sum over readings of (1-r)^k, and it is printed
   beside the count. A fail is noise until a person reads its lines.

3. Nothing is changed by this script. A fail goes to hand review with
   ktcontext.py; a reading is withdrawn or lowered only by that review, and
   the reason is written into its evidence. A hold is NOT promoted: a model's
   pick among four is not the method's tier A test. It is noted in evidence.

    python3 ktrecheck.py            # run both sets, save to work/rohonc
"""
import json
import os
import random
import re
import sys
import time
import urllib.request
from collections import defaultdict

import ktcross as K
import ktaffix as A
import kttranslate as T

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "work", "rohonc", "recheck_20260926.json")
KEY = open("/opt/secrets/deepinfra_api_key").read().strip()
MODEL = "deepseek-ai/DeepSeek-V4-Pro"
URL = "https://api.deepinfra.com/v1/openai/chat/completions"
SEED = 20260926
MAXPAGES = 6

SYSTEM = """You are helping check readings of a medieval manuscript written in an unknown script.
Each line has been glossed word by word into rough English. One word is blanked as ___ (it may be blanked more than once, always the same word).
Choose which of the four candidate words best fills the blank, from the sense of the line.
Answer with the letter only: A, B, C or D."""


def stem(w):
    return re.sub(r"[^a-z]", "", w.lower())[:5]


def occurrences(doc, codes):
    """code -> [(page, line_no, tokens)] first line on each page, page order."""
    out = defaultdict(list)
    seen = set()
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            toks = [t for run in ln for t in run]
            for t in toks:
                b = K.hx(A.strip(t)[0])
                if b in codes and (b, p.page) not in seen:
                    seen.add((b, p.page))
                    out[b].append((p.page, i, toks))
    return out


def blanked(toks, code, gl, seg, var, prop):
    return " ".join("___" + A.strip(t)[1] if K.hx(A.strip(t)[0]) == code
                    else T.render_token(t, gl, seg, False, var, prop) for t in toks)


def ask(line, cands):
    body = f"Line: {line}\n\n" + "\n".join(f"{L}. {c}" for L, c in zip("ABCD", cands))
    for attempt in range(4):
        try:
            req = urllib.request.Request(URL, data=json.dumps({
                "model": MODEL, "temperature": 0, "max_tokens": 400,
                "messages": [{"role": "system", "content": SYSTEM},
                             {"role": "user", "content": body}]}).encode(),
                headers={"Authorization": "Bearer " + KEY, "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.loads(r.read())
            txt = d["choices"][0]["message"]["content"].strip()
            m = re.search(r"\b([ABCD])\b", txt)
            return (m.group(1) if m else "?"), d.get("usage", {})
        except Exception as e:  # noqa: BLE001
            time.sleep(3 * (attempt + 1))
            err = e
    return "?", {"error": str(err)}


def run(codes, prop_raw, occ, gl, seg, var, prop, pool, rng, label):
    rows = []
    for code in codes:
        g = prop_raw[code]["gloss"]
        for page, i, toks in occ[code][:MAXPAGES]:
            line = blanked(toks, code, gl, seg, var, prop)
            onl = {stem(w) for w in re.split(r"[\s\-_]+", line)}
            dec = []
            for c in rng.sample(pool, len(pool)):
                if stem(c) in onl or stem(c) == stem(g) or any(stem(c) == stem(x) for x in dec):
                    continue
                dec.append(c)
                if len(dec) == 3:
                    break
            cands = [g] + dec
            rng.shuffle(cands)
            rows.append({"set": label, "code": code, "gloss": g, "tier": prop_raw[code]["tier"],
                         "page": page, "line": i, "text": line, "cands": cands, "decoy": dec[0]})
    # prompts are fixed above, in seed order; only the asking is parallel
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(8) as ex:
        answers = list(ex.map(lambda r: ask(r["text"], r["cands"]), rows))
    for r, (ans, use) in zip(rows, answers):
        r["pick"] = r["cands"]["ABCD".index(ans)] if ans in "ABCD" and ans != "?" else None
        r["hit"] = r["pick"] == r["gloss"]
        r["decoy_hit"] = r["pick"] == r["decoy"]
        r["answered"] = ans
    print(f"{label}: {len(rows)} lines, {sum(r['pick'] is None for r in rows)} unanswered", flush=True)
    return rows


def main():
    gl, doc, seg, var, prop, inv = K.build()
    raw = {k: v for k, v in json.load(open(os.path.join(ROOT, "harness", "proposals.json"),
                                           encoding="utf-8")).items() if isinstance(v, dict)}
    occ = occurrences(doc, set(raw))
    weak = sorted(k for k, v in raw.items() if v.get("tier") in ("C", "D", "G") and len(occ[k]) >= 2)
    strong = sorted(k for k, v in raw.items() if v.get("tier") == "A" and len(occ[k]) >= 2)
    rng = random.Random(SEED)
    calib = sorted(rng.sample(strong, min(60, len(strong))))
    pool = sorted({v["gloss"] for v in raw.values() if v.get("tier") != "withdrawn" and len(v["gloss"]) < 25})
    print(f"weak {len(weak)}, tier A on 2+ pages {len(strong)}, calibration {len(calib)}, decoy pool {len(pool)}")
    rows = run(calib, raw, occ, gl, seg, var, prop, pool, rng, "A")
    json.dump(rows, open(OUT, "w"), ensure_ascii=False, indent=0)
    n = len(rows); h = sum(r["hit"] for r in rows); c = sum(r["decoy_hit"] for r in rows)
    p0 = max(c / n, 1 / n)
    sig = (h - n * p0) / (n * p0 * (1 - p0)) ** 0.5
    print(f"\nCALIBRATION  tier A {h}/{n} = {h/n:.1%}   control decoy {c}/{n} = {c/n:.1%}   {sig:.1f} sigma")
    if not (h / n >= 0.5 and sig >= 5):
        print("INSTRUMENT FAILED THE BAR. No weak reading is judged by it.")
        return 1
    rows += run(weak, raw, occ, gl, seg, var, prop, pool, rng, "weak")
    json.dump(rows, open(OUT, "w"), ensure_ascii=False, indent=0)
    r = h / n
    by = defaultdict(list)
    for x in rows:
        if x["set"] == "weak":
            by[x["code"]].append(x["hit"])
    holds = [k for k, v in by.items() if all(v)]
    fails = [k for k, v in by.items() if not any(v)]
    expect = sum((1 - r) ** len(v) for v in by.values())
    print(f"\nWEAK  {len(by)} readings: holds {len(holds)}, mixed {len(by)-len(holds)-len(fails)}, "
          f"fails {len(fails)}   (correct readings expected to fail by chance: {expect:.1f})")
    return 0


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main())
