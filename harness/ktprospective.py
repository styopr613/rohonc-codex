"""Prospective occurrence holdout with a fresh outside reader.

This experiment was added after the evidence-folio parser correction.  It
does not pretend that the project's existing readings were made blind.
Instead, it gives a fresh reader one training folio for each sampled sign,
keeps another cited folio secret, freezes the reader's proposed glosses, and
only then scores those glosses on the concealed folios.

The prompt contains K&T's words, gaps for everything else, and the cited
Douay passage for the training folio.  It contains none of this project's
glosses, evidence notes, translations, or held-out folios.

    python3 ktprospective.py --refresh   # freeze manifest, prompt and reply
    python3 ktprospective.py             # score the cached reply
"""
import json
import os
import random
import re
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktorder as O
import ktrederive as R
import ktstrict as ST
import kttestlib as TL
import kttranslate as T
import ktor


SEED = 20260929
N = 40
NSHUF = 1000
NORDER = 100
MODEL = "deepseek/deepseek-v3.2"
EXTRA = {"reasoning": {"enabled": False}}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "work",
                   "rohonc", "outside", "prospective_occurrence")


PROMPT_HEAD = """You are the blind reader in a prospective test of an unknown
sixteenth-century script. Each numbered item concerns one sign. You see ONE
training occurrence (or several occurrences on the same training folio),
rendered using only an independently published dictionary. [TARGET] is the
sign to read; [?] marks other signs that dictionary does not read. The cited
Douay-Rheims passage follows the manuscript context.

For each item, propose a concise English gloss of at most three words only if
the passage and context determine it. Otherwise answer "none". Do not guess.
The same gloss must be capable of travelling to occurrences you have not
seen. Items are unrelated; do not transfer an answer between them.

Answer ONLY with one JSON object whose keys are the item numbers and whose
values are the gloss or "none". Do not add commentary.
"""


def unhex(h):
    return "".join(chr(0xE000 + int(h[i:i + 3], 16))
                   for i in range(0, len(h), 3))


def occurrences(doc):
    out = defaultdict(set)
    for pg in doc:
        for t in pg.tokens:
            out[A.strip(t)[0]].add(pg.page)
    return out


def render_context(pg, target, gl, var):
    hit_lines = []
    for i, ln in enumerate(pg.lines):
        if any(A.strip(t)[0] == target for run in ln for t in run):
            hit_lines.append(i)
    keep = {j for i in hit_lines for j in (i - 1, i, i + 1)
            if 0 <= j < len(pg.lines)}
    lines = []
    for i, ln in enumerate(pg.lines):
        if i not in keep:
            continue
        words = []
        for run in ln:
            for t in run:
                b = A.strip(t)[0]
                if b == target:
                    words.append("[TARGET]")
                elif b in gl or b in var:
                    words.append(T.render_token(t, gl, {}, False, var, None)
                                 .replace("~", ""))
                else:
                    words.append("[?]")
        lines.append(f"line {i + 1}: " + " ".join(words))
    return "\n".join(lines)


def make_design(gl, doc, var, refs, proposals):
    where = occurrences(doc)
    candidates = []
    for h, v in proposals.items():
        if not isinstance(v, dict) or v.get("tier") not in "AB":
            continue
        s = unhex(h)
        if s in gl or s in var:
            continue
        folios = sorted(where.get(s, set()) & refs.keys())
        if len(folios) >= 2:
            candidates.append((h, folios))
    rng = random.Random(SEED)
    chosen = rng.sample(sorted(candidates), min(N, len(candidates)))
    design = []
    for i, (h, folios) in enumerate(chosen, 1):
        fs = folios[:]
        rng.shuffle(fs)
        design.append({"item": i, "code": h, "train": fs[0], "test": fs[1]})
    return design


def make_prompt(design, pages, gl, var, refs, vd):
    blocks = [PROMPT_HEAD]
    for row in design:
        s = unhex(row["code"])
        context = render_context(pages[row["train"]], s, gl, var)
        passage = "\n".join(
            f"{k[0]} {k[1]}:{k[2]} {txt}"
            for k, txt in L.passage(vd, refs[row["train"]])[:40]
        )
        blocks.append(f"\nITEM {row['item']}\nMANUSCRIPT CONTEXT\n{context}\n"
                      f"CITED PASSAGE\n{passage}\n")
    return "\n".join(blocks)


def parse_reply(text, n):
    m = re.search(r"\{.*\}", text, re.S)
    raw = json.loads(m.group(0)) if m else {}
    out = {}
    for i in range(1, n + 1):
        value = raw.get(str(i), "none")
        out[i] = value.strip() if isinstance(value, str) else "none"
    return out


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    refs = TL.cited(doc)
    vd = L.verses_dr()
    proposals = json.load(open("proposals.json", encoding="utf-8"))
    pages = {pg.page: pg for pg in doc}
    os.makedirs(OUT, exist_ok=True)
    manifest_path = os.path.join(OUT, "manifest.json")
    prompt_path = os.path.join(OUT, "prompt.txt")
    reply_path = os.path.join(OUT, "reply.json")

    if os.path.exists(manifest_path):
        design = json.load(open(manifest_path, encoding="utf-8"))
    else:
        design = make_design(gl, doc, var, refs, proposals)
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(design, f, indent=1)
    prompt = make_prompt(design, pages, gl, var, refs, vd)
    if not os.path.exists(prompt_path):
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(prompt)

    if "--refresh" in argv:
        if os.path.exists(reply_path):
            raise SystemExit("reply already frozen; remove it explicitly to run a new experiment")
        text, usage = ktor.ask(MODEL, prompt, extra=EXTRA)
        # Raw reply and usage are committed before any scoring below occurs.
        with open(reply_path, "w", encoding="utf-8") as f:
            json.dump({"model": MODEL, "seed": SEED, "reply": text,
                       "usage": usage}, f, ensure_ascii=False, indent=1)

    if not os.path.exists(reply_path):
        print("No frozen reply. Run with --refresh.", file=sys.stderr)
        return 2
    saved = json.load(open(reply_path, encoding="utf-8"))
    answers = parse_reply(saved["reply"], len(design))
    answered = [(row, answers[row["item"]]) for row in design
                if answers[row["item"]].lower() != "none"]
    vv = L.verses()
    pools = {f: TL.passage_stems(vv, vd, refs[f])
             for row in design for f in (row["train"], row["test"])}

    rows = []
    for row in design:
        ans = answers[row["item"]]
        if not ans or ans.lower() == "none":
            continue
        stems = TL.content(ans)
        if not stems:
            continue
        test_pool = pools[row["test"]]
        train_pool = pools[row["train"]]
        v = proposals[row["code"]]
        agree = any(any(ST.same(a, b) for b in ST.words(ST.first_sense(v["gloss"])))
                    for a in ST.words(ans))
        rows.append((row, ans, stems, bool(stems & train_pool),
                     bool(stems & test_pool), agree))

    obs = sum(r[4] for r in rows) / max(1, len(rows))
    rng = random.Random(SEED + 1)
    nulls = []
    strict_nulls = []
    for _ in range(NSHUF):
        shuffled = [r[2] for r in rows]
        rng.shuffle(shuffled)
        hits = 0
        strict_hits = 0
        for r, stems in zip(rows, shuffled):
            hits += bool(stems & pools[r[0]["test"]])
            strict_hits += stems <= pools[r[0]["test"]]
        nulls.append(hits / max(1, len(rows)))
        strict_nulls.append(strict_hits / max(1, len(rows)))
    mu, sd, sig = TL.sigma(obs, nulls)
    p = (1 + sum(x >= obs for x in nulls)) / (NSHUF + 1)
    strict_obs = sum(r[2] <= pools[r[0]["test"]] for r in rows) / max(1, len(rows))
    strict_mu, strict_sd, strict_sig = TL.sigma(strict_obs, strict_nulls)
    strict_p = (1 + sum(x >= strict_obs for x in strict_nulls)) / (NSHUF + 1)

    # Post-hoc sensitivity: Test 6's ordered-stem measure on only the concealed
    # folio assigned to each frozen answer. It was added after the reply and is
    # explicitly not a preregistered result.
    passages, toks = {}, {}
    for row, answer in answered:
        f = row["test"]
        passages[f] = sum((O.ordered_stems(txt)
                           for _, txt in L.passage(vd, refs[f])), [])
        toks[f] = [t for ln in pages[f].lines for run in ln for t in run]
    def rendered(f, pm):
        return [R.stems(T.render_token(t, gl, seg, False, var, pm)) for t in toks[f]]
    base = {f: O.lcs(rendered(f, None), passages[f]) for f in passages}
    def order_gain(glosses):
        maps = defaultdict(dict)
        for (row, _), gloss in zip(answered, glosses):
            maps[row["test"]][unhex(row["code"])] = (gloss, "X")
        return sum(O.lcs(rendered(f, maps[f]), passages[f]) - base[f]
                   for f in passages)
    order_obs = order_gain([answer for _, answer in answered])
    order_nulls = []
    order_rng = random.Random(SEED + 2)
    for _ in range(NORDER):
        shuffled = [answer for _, answer in answered]
        order_rng.shuffle(shuffled)
        order_nulls.append(order_gain(shuffled))
    order_mu, order_sd, order_sig = TL.sigma(order_obs, order_nulls)
    order_p = (1 + sum(x >= order_obs for x in order_nulls)) / (NORDER + 1)
    usage = saved.get("usage") or {}
    cost = float(usage.get("cost") or
                 (usage.get("cost_details") or {}).get("upstream_inference_cost") or 0)

    print("PROSPECTIVE OCCURRENCE HOLDOUT, FRESH OUTSIDE READER")
    print(f"  reader {saved.get('model')}; seed {SEED}; sampled signs {len(design)}")
    print(f"  answered {len(answered)}; scorable glosses {len(rows)}; "
          f"declined {len(design) - len(answered)}; cost ${cost:.4f}\n")
    print(f"  {'item':>4s} {'train':5s} {'test':5s} {'answer':20s} {'train hit':9s} {'test hit':8s} {'ours':5s}")
    for row, ans, stems, train_hit, test_hit, agree in rows:
        print(f"  {row['item']:4d} {row['train']:5s} {row['test']:5s} {ans[:20]:20s} "
              f"{str(train_hit):9s} {str(test_hit):8s} {str(agree):5s}")
    print(f"\n  concealed-folio hits {sum(r[4] for r in rows)}/{len(rows)} = {obs*100:.1f}%")
    print(f"  shuffled glosses mean {mu*100:.1f}% (sd {sd*100:.2f}); "
          f"{sig:.1f} sigma; permutation p = {p:.4f}")
    print(f"  post-hoc, require every answer stem: "
          f"{sum(r[2] <= pools[r[0]['test']] for r in rows)}/{len(rows)} = {strict_obs*100:.1f}%; "
          f"shuffle {strict_mu*100:.1f}%; {strict_sig:.1f} sigma; p = {strict_p:.4f}")
    print(f"  post-hoc word-order sensitivity: gain {order_obs:+d}; "
          f"shuffle {order_mu:+.2f} (sd {order_sd:.2f}); {order_sig:.1f} sigma; "
          f"p = {order_p:.4f}")
    print(f"  agreement with the project's frozen A/B glosses "
          f"{sum(r[5] for r in rows)}/{len(rows)} = {sum(r[5] for r in rows)/max(1,len(rows))*100:.1f}%")
    return 0


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main(sys.argv[1:]))
