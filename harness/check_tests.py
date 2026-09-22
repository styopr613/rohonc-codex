"""Every figure TESTS.md prints for a test must stand in that test's saved run.

The bar is ZERO mismatches, declared here before the first run.

A test section is a `## Test N` heading followed by a backtick line naming
its program and its saved run(s). Every token of the form `NN.N sigma` or
`NN.N%` on an indented figure line of that section, and on the Summary row
for that test, must appear verbatim in one of the cited run files (a .md or
.json cited there counts too). Prose numbers are not checked: this guards
the figure blocks, which is where the site and the book read from.

    python3 check_tests.py
"""
import glob
import os
import re
import sys

import corpus

TESTS = os.path.join(corpus.ROOT, "TESTS.md")
WORK = os.path.join(corpus.ROOT, "work", "rohonc")
FIG = re.compile(r"(\d+(?:\.\d+)?)\s*(?:sigma|%)")


def sections(txt):
    out = []
    for m in re.finditer(r"^## (Test [^\n—]+?)\s*—[^\n]*\n\n?((?:`[^\n]*\n?)+)?(.*?)(?=^## )", txt, re.M | re.S):
        label, cite, body = m.group(1).strip(), m.group(2) or "", m.group(3)
        nums = [n for n in re.findall(r"Test (\d+)", label)]
        files = []
        for tok in re.findall(r"`([^`]+)`", cite):
            for part in re.split(r"\s*,\s*", tok):
                part = part.strip()
                if part.endswith((".txt", ".md", ".json")) or part.startswith("_"):
                    files.append(part)
        full = []
        for f in files:
            if f.startswith("_") and full:
                f = full[-1].replace(".txt", "") + f
            full.append(f)
        out.append((nums, full, body))
    return out


def load(files):
    """The cited run files, concatenated, and the ones that could not be found.

    This used to return only the text, and the caller failed a test just when
    NOTHING it cited existed. So a test citing three runs kept passing when
    two of them had been deleted, which is the case that matters: the figures
    from the surviving run go on matching and the rest are checked against
    nothing. Every cited file is now named and a single missing one fails.

    A citation may be a wildcard -- reglosser_*.json -- and those were never
    expanded, so they could only ever count as missing. They are expanded
    here, and a pattern matching no file is missing like any other.
    """
    txt, missing = "", []
    for f in files:
        got = []
        for cand in (os.path.join(WORK, os.path.basename(f)),
                     os.path.join(corpus.ROOT, f),
                     os.path.join(WORK, f)):
            if any(ch in cand for ch in "*?["):
                got = sorted(g for g in glob.glob(cand) if os.path.isfile(g))
            elif os.path.isfile(cand):
                got = [cand]
            if got:
                break
        if not got:
            missing.append(f)
            continue
        for g in got:
            txt += open(g, encoding="utf-8", errors="replace").read() + "\n"
    return txt, missing


def in_run(f, run):
    """Is this figure really in the run, as a NUMBER?

    Plain `f in run` was a substring test, so the document could print 68% and
    be "verified" by a run that says 68.4%, or 100% by 100.0%. Five figures
    were passing that way. A figure now has to stand as a whole number, with
    one documented latitude: a run that writes a whole number as N.0 satisfies
    a document that writes N.
    """
    for cand in (f, f + ".0") if "." not in f else (f,):
        if re.search(r"(?<![\d.])" + re.escape(cand) + r"(?![\d.])", run):
            return True
    return False


def opening_counts(txt):
    """The document's first paragraph says how many readings and how many
    bracketed restorations there are. Those were typed once and went stale by
    seven and one; the dictionary file is the only place that knows."""
    import json
    d = json.load(open(os.path.join(corpus.ROOT, "harness", "proposals.json"), encoding="utf-8"))
    t = {}
    for v in d.values():
        if isinstance(v, dict):
            t[v.get("tier")] = t.get(v.get("tier"), 0) + 1
    want = (sum(t.get(x, 0) for x in "ABCD"), t.get("G", 0))
    m = re.search(r"added (\d+) readings on top \(tiers A–D\) and (\d+) bracketed", txt)
    if not m:
        return ["the opening no longer states the reading and restoration counts"]
    got = (int(m.group(1)), int(m.group(2)))
    if got != want:
        return [f"the opening says {got[0]} readings / {got[1]} restorations; proposals.json has {want[0]} / {want[1]}"]
    return []


def main():
    txt = open(TESTS, encoding="utf-8").read()
    secs = sections(txt)
    summ = re.search(r"\n## Summary\n\n(.*?)\n\n[^\s]", txt, re.S)
    rows = {}
    for line in (summ.group(1) if summ else "").split("\n"):
        m = re.match(r"\s*Test (\d+)\S*\s*\|(.*)", line)
        if m:
            rows.setdefault(m.group(1), []).append(m.group(2))
    bad = []
    checked = 0
    for msg in opening_counts(txt):
        print(f"  FAIL  {msg}")
        bad.append((["opening"], "counts", ["proposals.json"]))
    for nums, files, body in secs:
        run, missing = load(files)
        if missing:
            # A test whose saved run has gone missing used to be skipped in
            # silence, so this checker could return PASS after the evidence for
            # a figure had disappeared. Missing evidence is now a failure, and
            # ONE missing file is enough -- not only the case where every file
            # a test cites has gone.
            print(f"  FAIL  Test {'/'.join(nums)}: cited run file(s) missing: {', '.join(missing)}")
            bad.append((nums, "missing run", missing))
            continue
        if not run:
            continue
        figs = []
        for line in body.split("\n"):
            if line.startswith("    "):
                figs += FIG.findall(line)
        for n in nums:
            for r in rows.get(n, []):
                figs += FIG.findall(r)
        for f in figs:
            checked += 1
            if not in_run(f, run):
                bad.append((nums, f, files))
    for nums, f, files in bad:
        print(f"  FAIL  Test {'/'.join(nums)}: {f} is not in {', '.join(os.path.basename(x) for x in files)}")
    print(f"{'PASS' if not bad else 'FAIL'}: {len(bad)} figures not in their run, of {checked} checked; bar was 0")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
