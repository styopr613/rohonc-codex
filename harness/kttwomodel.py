"""Test 18: two blind models. One reads a sign from part of its folios; the
other judges, on a folio the first never saw, whether that reading fits.

Every reading this project holds was checked at every place its sign stands
before it was kept, so no line is a holdout for the project's own readings.
This test does not pretend otherwise. It asks two things the project's
readings can be compared with:

  TRANSFER  does a reading made blind from some folios fit a folio from a
            different chapter that the reader never saw?
  AGREEMENT how often does that blind reading land on the project's word?

and it runs K&T's own words through the same steps first, as the known
answers. If their true words do not transfer, the instrument has no power
and nothing is concluded about ours.

DESIGN, declared 2026-09-30 before any call:

  Signs. Ours: tier A/B readings K&T do not read, whose first sense has a
  content word. K&T's: single-sense glosses with a content word, not a
  grammatical <...> entry, one matched to each of ours on the number of
  cited folios it stands on. A sign is used if one of its cited folios (the
  HIDDEN folio, drawn by seed) cites no chapter in common with at least one
  other; up to three of those others, drawn by seed, are its TRAINING
  folios. Folios sharing a chapter with the hidden folio are never shown.

  Reader: DeepSeek V3.2 (thinking off), one fresh call per sign, K&T's
  words only, the sign as [TARGET], the target sign removed from K&T's
  dictionary in their arm, every other unread sign as [?], and each
  training folio's cited Douay passage. It must give one gloss of at most
  three words. It sees no project gloss, note or translation, no hidden
  folio, and nothing saying which signs are K&T's.

  Judge: Gemini 2.5 Flash (thinking off), one fresh call per sign, temperature 0. It sees
  the hidden folio's lines around one occurrence (drawn by seed) with the
  sign as [BLANK], and the hidden folio's cited Douay passage, and three
  candidates in random order, labelled A B C: the reader's gloss for this
  sign and two rivals, which are the reader's glosses for two other signs
  of the same arm sharing no content stem with it or each other. It is not
  told where any candidate came from. It must pick one letter.

  All three candidates are the reader's glosses from other chapters, so
  under no signal they are exchangeable and chance is exactly 1/3.

BARS, declared 2026-09-30 before any call:

  CALIBRATION  K&T's arm: the judge picks the reader's gloss above 1/3,
               exact one-sided binomial p < 0.01, at least 30 judged. If
               not, TRANSFER and AGREEMENT are NO VERDICT.
  TRANSFER     our arm, the same rule. PASS or FAIL.
  AGREEMENT    the reader's gloss shares a lemma with the arm's own first
               sense (ktstrict.same). Ours must be at least half of K&T's
               rate. PASS or FAIL. NO VERDICT if K&T's rate is under 10%.

  Changes before this run, none after any reply was read: a first launch,
  with the reader thinking and Gemini 2.5 Pro as judge, was stopped for cost
  with no reply saved; both models were switched to thinking off and the
  judge to 2.5 Flash. After the reader stage and before any judge call, a
  variant spelling of the hidden sign was found to crash K&T's arm (it would
  also have shown the hidden word); it is now blanked as the sign itself.
  None of the saved reader prompts changed.

    python3 kttwomodel.py --refresh   # freeze design, reader, judge (in order)
    python3 kttwomodel.py             # score the frozen replies
"""
import json
import os
import random
import re
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from math import comb

import ktaffix as A
import ktcross as K
import ktleft as L
import ktstrict as ST
import kttestlib as TL
import kttranslate as T
import ktor


SEED = 20260930
MAXTRAIN = 3
READER = "deepseek/deepseek-v3.2"
READER_EXTRA = {"reasoning": {"enabled": False}}
JUDGE = "google/gemini-2.5-flash"
JUDGE_EXTRA = {"reasoning": {"enabled": False}}
CAP = 0.20   # dollars, both stages; checked before every call
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "work",
                   "rohonc", "outside", "twomodel")

READER_PROMPT = """You are reading one sign of an unknown sixteenth-century
script. Below are the lines where it stands on one or more pages, written
with the words of a published dictionary. [TARGET] is the sign; [?] marks
other signs that dictionary does not read. Each page retells the Bible
passage printed after it.

Give the single English gloss, at most three words, that best fits
[TARGET] in all of these places. The same sign must mean the same thing
everywhere, including pages you are not shown. You must give a gloss.

Answer ONLY with JSON: {"gloss": "..."}
"""

JUDGE_PROMPT = """Below are lines of a manuscript written with the words of a
published dictionary. [BLANK] is one sign; [?] marks signs the dictionary
does not read. The page retells the Bible passage printed after it.

Which candidate best fills [BLANK]? You must pick one.

Answer ONLY with JSON: {"choice": "A"} or "B" or "C".
"""


def unhex(h):
    return "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))


def tohex(s):
    return "".join(f"{ord(c) - 0xE000:03x}" for c in s)


def occurrences(doc):
    out = defaultdict(set)
    for pg in doc:
        for t in pg.tokens:
            out[A.strip(t)[0]].add(pg.page)
    return out


def render(pg, target, gl, var, mark, only=None):
    """Lines around the target (or around line `only`), target as `mark`."""
    hit = [i for i, ln in enumerate(pg.lines)
           if any(A.strip(t)[0] == target for run in ln for t in run)]
    if only is not None:
        hit = [only]
    keep = {j for i in hit for j in (i - 1, i, i + 1) if 0 <= j < len(pg.lines)}
    lines = []
    for i in sorted(keep):
        words = []
        for run in pg.lines[i]:
            for t in run:
                b = A.strip(t)[0]
                if b == target or var.get(t) == target:   # a variant spelling is the sign
                    words.append(mark)
                elif b in gl or b in var:
                    words.append(T.render_token(t, gl, {}, False, var, None).replace("~", ""))
                else:
                    words.append("[?]")
        lines.append(f"line {i + 1}: " + " ".join(words))
    return "\n".join(lines)


def passage(vd, refs, f):
    return "\n".join(f"{k[0]} {k[1]}:{k[2]} {txt}" for k, txt in L.passage(vd, refs[f])[:40])


def chapters(refs, f):
    return {(b, c) for b, c, _, _ in refs[f]}


def split(folios, refs, rng):
    options = []
    for h in folios:
        train = [f for f in folios if f != h and not (chapters(refs, f) & chapters(refs, h))]
        if train:
            options.append((h, train))
    if not options:
        return None
    h, train = rng.choice(options)
    return h, sorted(rng.sample(train, min(MAXTRAIN, len(train))))


def make_design(gl, doc, var, refs, proposals):
    where = occurrences(doc)
    ours = []
    for h in sorted(proposals):
        v = proposals[h]
        if not isinstance(v, dict) or v.get("tier") not in ("A", "B"):
            continue
        s = unhex(h)
        if s in gl or s in var:
            continue
        gloss = ST.first_sense(v["gloss"]).strip()
        folios = sorted(where.get(s, set()) & refs.keys())
        if TL.content(gloss) and len(folios) >= 2:
            ours.append((h, gloss, folios))
    kt = []
    for s in sorted(gl):
        senses = sorted(gl[s])
        if len(senses) != 1 or senses[0].lstrip().startswith("<"):
            continue
        gloss = ST.first_sense(senses[0]).strip()
        folios = sorted(where.get(s, set()) & refs.keys())
        if TL.content(gloss) and len(folios) >= 2:
            kt.append((tohex(s), gloss, folios))
    rng = random.Random(SEED)
    rng.shuffle(kt)
    rows = []
    for code, gloss, folios in ours:
        sp = split(folios, refs, rng)
        if not sp:
            continue
        match = None
        for cand in sorted(kt, key=lambda r: abs(len(r[2]) - len(folios))):
            msp = split(cand[2], refs, rng)
            if msp:
                match = (cand, msp)
                break
        if not match:
            continue
        kt.remove(match[0])
        for arm, (cc, gg, _), (hid, train) in (("ours", (code, gloss, folios), sp),
                                              ("kt", match[0], match[1])):
            rows.append({"arm": arm, "code": cc, "gloss": gg, "hidden": hid, "train": train})
    for row in rows:
        pg_lines = [i for i, ln in enumerate(PAGES[row["hidden"]].lines)
                    if any(A.strip(t)[0] == unhex(row["code"]) for run in ln for t in run)]
        row["line"] = rng.choice(pg_lines)
    rng.shuffle(rows)
    for i, row in enumerate(rows, 1):
        row["item"] = i
    return rows


def dict_for(row, gl):
    if row["arm"] == "kt":
        s = unhex(row["code"])
        return {k: v for k, v in gl.items() if k != s}
    return gl


def reader_prompt(row, gl, var, refs, vd):
    s = unhex(row["code"])
    g = dict_for(row, gl)
    parts = [READER_PROMPT]
    for n, f in enumerate(row["train"], 1):
        parts.append(f"\nPAGE {n}\n{render(PAGES[f], s, g, var, '[TARGET]')}\n"
                     f"BIBLE PASSAGE\n{passage(vd, refs, f)}\n")
    return "\n".join(parts)


def judge_prompt(row, cands, gl, var, refs, vd):
    s = unhex(row["code"])
    g = dict_for(row, gl)
    lines = render(PAGES[row["hidden"]], s, g, var, "[BLANK]", only=row["line"])
    opts = "\n".join(f"{l}: {c}" for l, c in zip("ABC", cands))
    return (f"{JUDGE_PROMPT}\nMANUSCRIPT\n{lines}\n"
            f"BIBLE PASSAGE\n{passage(vd, refs, row['hidden'])}\n\nCANDIDATES\n{opts}\n")


def parse(text, key):
    m = re.search(r"\{.*?\}", text or "", re.S)
    try:
        v = json.loads(m.group(0)).get(key) if m else None
    except ValueError:
        v = None
    return v.strip() if isinstance(v, str) else None


def cost_of(usage):
    usage = usage or {}
    return float(usage.get("cost") or (usage.get("cost_details") or {}).get("upstream_inference_cost") or 0)


SPENT = [0.0]   # dollars across both stages, from each saved reply's usage


def ask_all(jobs, model, extra, path):
    """jobs: {key: prompt}. Each reply is saved the moment it arrives, so a
    stop loses nothing paid for. No call starts once SPENT reaches CAP."""
    import threading
    done = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    todo = [k for k in sorted(jobs) if k not in done]
    lock = threading.Lock()
    def one(k):
        with lock:
            if SPENT[0] >= CAP:
                return
        try:
            text, usage = ktor.ask(model, jobs[k], extra=extra, tries=2)
        except Exception as e:
            print(f"  {model} item {k}: {e}", file=sys.stderr)
            return
        with lock:
            done[k] = {"prompt": jobs[k], "reply": text, "usage": usage}
            SPENT[0] += cost_of(usage)
            with open(path + ".tmp", "w", encoding="utf-8") as f:
                json.dump(done, f, ensure_ascii=False, indent=1, sort_keys=True)
            os.replace(path + ".tmp", path)
    with ThreadPoolExecutor(8) as ex:
        list(ex.map(one, todo))
    if SPENT[0] >= CAP:
        print(f"  STOP: the ${CAP:.2f} cap was reached", file=sys.stderr)
    return done


def rivals(row, glosses, rng):
    mine = TL.content(glosses[row["item"]])
    pool = [r for r in DESIGN if r["arm"] == row["arm"] and r["item"] != row["item"]
            and r["item"] in glosses]
    rng.shuffle(pool)
    picked, used = [], set(mine)
    for r in pool:
        st = TL.content(glosses[r["item"]])
        if st and not (st & used):
            picked.append(glosses[r["item"]])
            used |= st
        if len(picked) == 2:
            return picked
    return None


def binom_p(k, n, p=1 / 3):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


PAGES, DESIGN = {}, []


def main(argv):
    global DESIGN
    gl, doc, seg, var, prop, inv = K.build()
    refs = TL.cited(doc)
    vd = L.verses_dr()
    PAGES.update({pg.page: pg for pg in doc})
    proposals = json.load(open("proposals.json", encoding="utf-8"))
    os.makedirs(OUT, exist_ok=True)
    paths = {k: os.path.join(OUT, f"{k}.json") for k in ("manifest", "reader", "judge")}
    refresh = "--refresh" in argv

    if not os.path.exists(paths["manifest"]):
        if not refresh:
            print("No frozen design. Run with --refresh.", file=sys.stderr)
            return 2
        with open(paths["manifest"], "w", encoding="utf-8") as f:
            json.dump(make_design(gl, doc, var, refs, proposals), f, indent=1)
    DESIGN = json.load(open(paths["manifest"], encoding="utf-8"))

    if refresh:
        for k in ("reader", "judge"):
            if os.path.exists(paths[k]):
                SPENT[0] += sum(cost_of(v["usage"]) for v in
                                json.load(open(paths[k], encoding="utf-8")).values())
        jobs = {str(r["item"]): reader_prompt(r, gl, var, refs, vd) for r in DESIGN}
        est = sum(len(p) for p in jobs.values()) / 4 / 1e6 * 0.28 * 3
        print(f"  reader: {len(jobs)} calls, est. ${est:.2f}", file=sys.stderr)
        ask_all(jobs, READER, READER_EXTRA, paths["reader"])
        if SPENT[0] >= CAP:
            return 2
    reader = json.load(open(paths["reader"], encoding="utf-8")) if os.path.exists(paths["reader"]) else {}
    glosses = {}
    for r in DESIGN:
        rec = reader.get(str(r["item"]))
        g = parse(rec["reply"], "gloss") if rec else None
        if g and TL.content(g):
            glosses[r["item"]] = g

    rng = random.Random(SEED + 1)
    items = {}
    for r in DESIGN:
        if r["item"] not in glosses:
            continue
        riv = rivals(r, glosses, rng)
        if not riv:
            continue
        cands = [glosses[r["item"]]] + riv
        rng.shuffle(cands)
        items[str(r["item"])] = (cands, "ABC"[cands.index(glosses[r["item"]])])

    if refresh:
        spent = sum(cost_of(v["usage"]) for v in reader.values())
        jobs = {k: judge_prompt(next(r for r in DESIGN if str(r["item"]) == k), c, gl, var, refs, vd)
                for k, (c, _) in items.items()}
        est = sum(len(p) for p in jobs.values()) / 4 / 1e6 * 0.30 + len(jobs) * 20 / 1e6 * 2.5
        print(f"  judge: {len(jobs)} calls, est. ${est:.2f}; spent so far ${spent:.4f}", file=sys.stderr)
        ask_all(jobs, JUDGE, JUDGE_EXTRA, paths["judge"])
    judge = json.load(open(paths["judge"], encoding="utf-8")) if os.path.exists(paths["judge"]) else {}

    cost = sum(cost_of(v["usage"]) for v in list(reader.values()) + list(judge.values()))
    res = {}
    print("TEST 18: TWO BLIND MODELS -- READ FROM SOME FOLIOS, JUDGED ON ANOTHER CHAPTER")
    print(f"  reader {READER}; judge {JUDGE}; seed {SEED}; cost ${cost:.4f}\n")
    for arm, name in (("kt", "K&T known words"), ("ours", "project A/B")):
        rows = [r for r in DESIGN if r["arm"] == arm]
        judged = []
        print(f"  {name}: {len(rows)} signs, {sum(r['item'] in glosses for r in rows)} read")
        print(f"  {'item':>4s} {'train':17s} {'hidden':6s} {'gloss':18s} {'reader':18s} agree  judge")
        for r in sorted(rows, key=lambda r: r["item"]):
            k = str(r["item"])
            if r["item"] not in glosses:
                continue
            agree = any(ST.same(a, b) for a in ST.words(glosses[r["item"]]) for b in ST.words(r["gloss"]))
            pick = parse(judge[k]["reply"], "choice") if k in judge else None
            win = None
            if k in items and pick and pick.upper()[:1] in "ABC":
                win = pick.upper()[:1] == items[k][1]
                judged.append(win)
            r["agree"] = agree
            print(f"  {r['item']:4d} {','.join(r['train']):17s} {r['hidden']:6s} {r['gloss'][:18]:18s} "
                  f"{glosses[r['item']][:18]:18s} {'yes' if agree else '-':5s}  "
                  f"{'-' if win is None else 'picked' if win else 'rival'}")
        n, w = len(judged), sum(judged)
        read = [r for r in rows if r["item"] in glosses]
        ag = sum(r["agree"] for r in read)
        res[arm] = (n, w, binom_p(w, n) if n else 1.0, ag, len(read))
        print()

    print(f"  {'arm':16s} {'judged':>6s} {'picked':>12s} {'chance':>7s} {'p':>9s} {'agree':>13s}")
    for arm, name in (("kt", "K&T known words"), ("ours", "project A/B")):
        n, w, p, ag, nr = res[arm]
        print(f"  {name:16s} {n:6d} {w:4d} {w / max(1, n) * 100:5.1f}%   33.3% {p:9.2g} "
              f"{ag:3d}/{nr:<3d} {ag / max(1, nr) * 100:5.1f}%")

    calib = res["kt"][0] >= 30 and res["kt"][2] < 0.01
    kt_ag = res["kt"][3] / max(1, res["kt"][4])
    our_ag = res["ours"][3] / max(1, res["ours"][4])
    if not calib:
        transfer = agreement = "NO VERDICT"
    else:
        transfer = ("NO VERDICT" if res["ours"][0] < 30 else
                    "PASS" if res["ours"][2] < 0.01 else "FAIL")
        agreement = ("NO VERDICT" if kt_ag < 0.10 else
                     "PASS" if our_ag >= kt_ag / 2 else "FAIL")
    print()
    print(f"  CALIBRATION  K&T's words transfer, p < 0.01, n >= 30   {'ok' if calib else 'FAILED'}")
    print(f"  TRANSFER     ours transfer, p < 0.01, n >= 30          {transfer}")
    print(f"  AGREEMENT    ours at least half of K&T's rate          {agreement}   "
          f"({our_ag * 100:.1f}% against {kt_ag * 100:.1f}%)")
    return 0 if calib and "FAIL" not in (transfer, agreement) else 1


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main(sys.argv[1:]))
