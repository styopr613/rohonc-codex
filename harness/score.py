"""Run every process against the same ruler and write the results.

    python score.py                 # main split, all registered processes
    python score.py --reverse       # train on odd leaves, test on even
    python score.py --only a,b      # a subset
    python score.py --verify        # rerun and check determinism

Output is work/results_<split>.json: for every process, the full metric vector,
the per-metric error against the held-out half, and the block means.
"""
import argparse
import json
import os
import sys
import time
import traceback

import corpus
import layout
import profile as prof
import floor as fl
import generators

WORK = os.path.join(corpus.ROOT, "work")
SEEDS = (7, 21, 44)


def reference(test):
    return prof.profile(test)


def run_one(name, spec, train, seeds=SEEDS, tuned=None):
    """Generate with each seed, return the profiles and any notes."""
    entry = generators.get(name)
    cfg = (tuned or {}).get(name, {}).get("cfg")
    profiles, notes = [], {}
    for s in seeds:
        doc, n = (entry["fn"](spec, train, seed=s, cfg=cfg) if cfg is not None
                  else entry["fn"](spec, train, seed=s))
        profiles.append(prof.profile(doc))
        notes = n
        if entry["kind"] == "stream" and name in ("noise_floor",):
            break          # deterministic, no point running three identical seeds
    return profiles, notes


def mean_scores(profiles, ref, fscale):
    """Average the per-metric error over seeds, on both scales."""
    def avg(fn):
        scs = [fn(p) for p in profiles]
        return {b: {k: sum(s[b][k] for s in scs) / len(scs) for k in scs[0][b]}
                for b in prof.BLOCKS}
    return avg(lambda p: prof.score(p, ref)), avg(lambda p: fl.score(p, ref, fscale))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reverse", action="store_true")
    ap.add_argument("--only", default=None)
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--seeds", default=None)
    args = ap.parse_args()

    generators.load_all()
    names = args.only.split(",") if args.only else generators.names()
    seeds = tuple(int(x) for x in args.seeds.split(",")) if args.seeds else SEEDS

    doc = corpus.load()
    train, test = corpus.split(doc, reverse=args.reverse)
    spec = layout.build(train, len(corpus.words(test)))
    ref = reference(test)
    fscale = fl.build(train, ref)
    tpath = os.path.join(WORK, f"tuned_{'reverse' if args.reverse else 'main'}.json")
    tuned = json.load(open(tpath, encoding="utf-8")) if os.path.exists(tpath) else {}
    if tuned:
        print(f"tuned configs: {', '.join(sorted(tuned))}")

    split_name = "reverse" if args.reverse else "main"
    print(f"split: {split_name} | train {len(corpus.words(train))} tokens, "
          f"held-out {len(corpus.words(test))} tokens")
    print(f"layout spec: {len(spec)} paragraphs, {sum(p.n_lines for p in spec)} lines\n")

    results = {"split": split_name, "seeds": list(seeds),
               "reference": {b: ref[b] for b in prof.BLOCKS},
               "floor_scale": fscale,
               "ref_tokens": ref["_n"], "processes": {}}

    for name in names:
        t0 = time.time()
        try:
            profiles, notes = run_one(name, spec, train, seeds, tuned)
        except Exception as e:
            print(f"  {name:22s} FAILED: {e}")
            traceback.print_exc()
            results["processes"][name] = {"error": str(e)}
            continue
        sc, fs = mean_scores(profiles, ref, fscale)
        m = prof.means(sc)
        fm = fl.means(fs)
        fmed = fl.medians(fs)
        entry = generators.get(name)
        results["processes"][name] = {
            "label": entry.get("label", name),
            "kind": entry["kind"],
            "note": entry.get("note", ""),
            "notes": notes,
            "tuned": tuned.get(name, {}).get("cfg"),
            "tokens": profiles[0]["_n"],
            "values": {b: profiles[0][b] for b in prof.BLOCKS},
            "errors": sc,
            "floor_errors": fs,
            "means": m,
            "floor_means": fm,
            "floor_medians": fmed,
            "seconds": round(time.time() - t0, 1),
        }
        print(f"  {name:22s} fp42 {m['fingerprint44']:6.1f}%  line {m['line']:7.1f}%  "
              f"| floor: fp42 {fm['fingerprint44']:6.2f}x  line {fm['line']:6.2f}x  "
              f"median {fmed['overall']:5.2f}x   ({results['processes'][name]['seconds']}s)")

    os.makedirs(WORK, exist_ok=True)
    path = os.path.join(WORK, f"results_{split_name}.json")
    if args.verify and os.path.exists(path):
        old = json.load(open(path, encoding="utf-8"))
        drift = 0.0
        for n, r in results["processes"].items():
            o = old["processes"].get(n)
            if not o or "means" not in o or "means" not in r:
                continue
            for k in r["means"]:
                drift = max(drift, abs(r["means"][k] - o["means"][k]))
            for k in r.get("floor_means", {}):
                drift = max(drift, abs(r["floor_means"][k] - o["floor_means"][k]))
        print(f"\nverify: worst drift {drift:.6f} pp -> "
              f"{'DETERMINISTIC' if drift < 1e-9 else 'NON-DETERMINISTIC'}")
        return 0 if drift < 1e-9 else 1
    json.dump(results, open(path, "w", encoding="utf-8"), indent=1, default=float)
    print(f"\nwrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
