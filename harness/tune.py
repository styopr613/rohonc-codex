"""Equal tuning budget for every process that has parameters.

Random search, seeded, scored on TRAIN only. The held-out half is never read
here -- gate.py checks that -- and the reversed split arbitrates anything the
search might have fitted to this one.

The budget is the same for every process so that no row wins by having been
given more attention than another. A process with no parameters (the controls,
the frozen models, the human samples) is skipped rather than given a free pass.

    python tune.py --only grille,abbrev --budget 200
"""
import argparse
import json
import os
import random

import corpus
import layout
import profile as prof
import floor as fl
import generators

WORK = os.path.join(corpus.ROOT, "work")
BUDGET = 200

# name -> {param: (low, high) or [choices]}
SPACES = {
    "grille": {
        "rows": (40, 9000),
        "tables": [2, 3, 4, 6],
        "stride": [1, 1, 1, 2, 3],
        "p_jump": (0.02, 0.9),
    },
    "llull": {
        "disks": [3, 4, 5, 6],
        "faces": (6, 40),
        "p_advance": (0.05, 0.95),
        "p_blank": (0.0, 0.6),
    },
    "abbrev": {
        "p_suspend": (0.0, 1.0),
        "p_contract": (0.0, 1.0),
        "p_sign": (0.0, 1.0),
        "p_nasal": (0.0, 1.0),
        "allographs": [1, 2, 3],
    },
}


# Timm & Schinner's own switches. Swept exhaustively rather than sampled,
# because there are only twenty of them -- the same courtesy the fingerprint
# repo extends their generator, so the row is not a straw man.
SELFCITE_GRID = [
    {"method.canFollow": cf, "method.morph": mo, "method.sourceChooser": sc}
    for cf in ("curveline", "statistic", "percent", "voynich", "none")
    for mo in ("slim", "extended")
    for sc in ("page", "position")
]


def sample(space, rng):
    out = {}
    for k, v in space.items():
        if isinstance(v, list):
            out[k] = v[rng.randrange(len(v))]
        elif isinstance(v[0], int) and isinstance(v[1], int):
            out[k] = rng.randint(v[0], v[1])
        else:
            out[k] = rng.uniform(v[0], v[1])
    return out


def objective(fs):
    """Median floor units over every metric.

    The median rather than the mean: a mean lets one runaway metric decide the
    search, and the runaway is usually an estimator artefact on a near-zero
    quantity rather than a property of the process.
    """
    import statistics
    return statistics.median([v for b in prof.BLOCKS for v in fs[b].values()])


def tune_one(name, train, budget, seed=408):
    """Search `name`'s parameter space against TRAIN. Returns the best config."""
    rng = random.Random(seed)
    grid = SELFCITE_GRID if name == "selfcite" else None
    space = SPACES.get(name)
    spec = layout.build(train, len(corpus.words(train)), seed=seed + 1)
    ref = prof.profile(train)
    scale = fl.build(train, ref)
    fn = generators.get(name)["fn"]

    best, best_cfg, trace = float("inf"), None, []
    n = len(grid) if grid else budget
    for i in range(n):
        cfg = grid[i] if grid else sample(space, rng)
        try:
            doc, _ = fn(spec, train, seed=7, cfg=cfg)
            v = objective(fl.score(prof.profile(doc), ref, scale))
        except Exception as e:
            trace.append({"cfg": cfg, "error": str(e)})
            continue
        trace.append({"cfg": cfg, "score": v})
        if v < best:
            best, best_cfg = v, cfg
    return best_cfg, best, trace


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    ap.add_argument("--budget", type=int, default=BUDGET)
    ap.add_argument("--reverse", action="store_true")
    args = ap.parse_args()

    generators.load_all()
    names = args.only.split(",") if args.only else list(SPACES) + ["selfcite"]
    doc = corpus.load()
    train, _ = corpus.split(doc, reverse=args.reverse)

    os.makedirs(WORK, exist_ok=True)
    split = "reverse" if args.reverse else "main"
    path = os.path.join(WORK, f"tuned_{split}.json")
    tuned = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}

    for n in names:
        if n not in SPACES and n != "selfcite":
            print(f"  {n:16s} no parameter space, skipped")
            continue
        cfg, score, trace = tune_one(n, train, args.budget)
        tuned[n] = {"cfg": cfg, "train_score": score, "budget": args.budget,
                    "evaluated": len(trace)}
        print(f"  {n:16s} best {score:.3f}x on TRAIN  {cfg}")

    json.dump(tuned, open(path, "w", encoding="utf-8"), indent=1)
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()
