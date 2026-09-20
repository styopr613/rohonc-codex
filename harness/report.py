"""Render the results as tables. `--markdown` emits the blocks RESULTS.md uses,
so no figure in the write-up is retyped by hand.

    python report.py                      # console table, main split
    python report.py --detail fivecomp    # a process's five worst metrics
    python report.py --markdown > ../work/tables.md
"""
import argparse
import json
import os

import corpus
import profile as prof

WORK = os.path.join(corpus.ROOT, "work")

ORDER = ["noise_floor", "fivecomp", "fivecomp_scribe", "fivecomp_lines", "manual",
         "naibbe_latin", "naibbe_italian", "naibbe_wb", "naibbe_wb_italian",
         "naibbe_word", "verbose_det", "verbose_det_italian", "grille", "grille_bigtable", "selfcite", "llull",
         "abbrev", "gibberish", "natlang_italian", "natlang_latin",
         "natlang_hebrew", "subst", "subst_homophonic"]

# the metrics the write-up argues from
HEADLINE = [("text", "h2 (char)", "h2", "{:.2f}"),
            ("text", "h1 (char)", "h1", "{:.2f}"),
            ("text", "TTR", "TTR", "{:.3f}"),
            ("text", "mean word len", "word len", "{:.2f}"),
            ("struct", "zipf slope (top500)", "Zipf", "{:.3f}"),
            ("text", "cross-word MI", "cross-word MI", "{:.3f}")]

LINE_KEYS = ["m line-final %", "gallows para-start lift", "cross-line repeat %",
             "para vocab coherence", "word-section MI (bits)", "word-len autocorr"]
LINE_SHORT = ["m line-final", "gallows lift", "cross-line rep",
              "para coherence", "section MI", "len autocorr"]


def load(split="main"):
    p = os.path.join(WORK, f"results_{split}.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None


def rows(res):
    out = []
    for n in ORDER + [k for k in res["processes"] if k not in ORDER]:
        r = res["processes"].get(n)
        if r and "means" in r:
            out.append((n, r))
    return out


def worst(res, name, k=5):
    r = res["processes"][name]
    flat = [(b, m, e) for b in prof.BLOCKS for m, e in r["floor_errors"][b].items()]
    flat.sort(key=lambda x: -x[2])
    return [(b, m, r["values"][b][m], res["reference"][b][m], e) for b, m, e in flat[:k]]


def md_main(res, rev=None):
    print("| process | what it is | fp42 APE | fp42 floor | line floor | median floor |")
    print("|---|---|---:|---:|---:|---:|")
    for n, r in rows(res):
        m, f = r["means"], r["floor_means"]
        med = r["floor_medians"]["overall"]
        rv = ""
        if rev and n in rev["processes"] and "floor_medians" in rev["processes"][n]:
            rv = f" ({rev['processes'][n]['floor_medians']['overall']:.2f})"
        print(f"| `{n}` | {r['label']} | {m['fingerprint44']:.1f}% | "
              f"{f['fingerprint44']:.2f}x | {f['line']:.2f}x | {med:.2f}x{rv} |")


def md_headline(res):
    ref = res["reference"]
    hdr = " | ".join(h[2] for h in HEADLINE)
    print(f"| process | {hdr} |")
    print("|---" * (len(HEADLINE) + 1) + "|")
    vals = " | ".join(f"**{h[3].format(ref[h[0]][h[1]])}**" for h in HEADLINE)
    print(f"| **the manuscript** | {vals} |")
    for n, r in rows(res):
        vals = " | ".join(h[3].format(r["values"][h[0]][h[1]]) for h in HEADLINE)
        print(f"| `{n}` | {vals} |")


def md_line(res):
    ref = res["reference"]
    print("| process | " + " | ".join(LINE_SHORT) + " |")
    print("|---" * (len(LINE_KEYS) + 1) + "|")
    print("| **the manuscript** | " + " | ".join(
        f"**{ref['line'][k]:.2f}**" for k in LINE_KEYS) + " |")
    for n, r in rows(res):
        print(f"| `{n}` | " + " | ".join(
            f"{r['values']['line'][k]:.2f}" for k in LINE_KEYS) + " |")


def md_worst(res, names):
    for n in names:
        if n not in res["processes"]:
            continue
        print(f"\n**`{n}` — {res['processes'][n]['label']}**\n")
        print("| block | metric | it produced | the manuscript | floor units |")
        print("|---|---|---:|---:|---:|")
        for b, m, g, r, e in worst(res, n):
            print(f"| {b} | {m} | {g:.3f} | {r:.3f} | {e:.1f}x |")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="main")
    ap.add_argument("--detail", default=None)
    ap.add_argument("--markdown", action="store_true")
    args = ap.parse_args()
    res = load(args.split)
    if not res:
        print(f"no results for split {args.split}")
        return
    if args.markdown:
        rev = load("reverse") if args.split == "main" else None
        print("<!-- RANKING -->")
        md_main(res, rev)
        print("\n<!-- HEADLINE -->")
        md_headline(res)
        print("\n<!-- LINE -->")
        md_line(res)
        print("\n<!-- WORST -->")
        md_worst(res, ["fivecomp", "fivecomp_scribe", "naibbe_latin",
                       "naibbe_wb_italian", "grille_bigtable", "abbrev",
                       "gibberish"])
        return
    print(f"split: {res['split']}, held-out {res['ref_tokens']} tokens\n")
    print(f"{'process':24s} {'fp42':>8s} {'fp42 flr':>9s} {'line flr':>9s} {'median':>8s}")
    print("-" * 62)
    for n, r in rows(res):
        print(f"{n:24s} {r['means']['fingerprint44']:7.1f}% "
              f"{r['floor_means']['fingerprint44']:8.2f}x "
              f"{r['floor_means']['line']:8.2f}x "
              f"{r['floor_medians']['overall']:7.2f}x")
    if args.detail:
        for n in args.detail.split(","):
            print(f"\n--- {n}: five worst ---")
            for b, m, g, r_, e in worst(res, n):
                print(f"  {b:7s} {m:28s} {g:10.3f} vs {r_:10.3f}  {e:6.1f}x")


if __name__ == "__main__":
    main()
