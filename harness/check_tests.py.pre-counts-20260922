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
    txt = ""
    for f in files:
        for cand in (os.path.join(WORK, os.path.basename(f)), os.path.join(corpus.ROOT, f),
                     os.path.join(WORK, f)):
            if os.path.isfile(cand):
                txt += open(cand, encoding="utf-8", errors="replace").read() + "\n"
                break
    return txt


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
    for nums, files, body in secs:
        run = load(files)
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
            if f not in run:
                bad.append((nums, f, files))
    for nums, f, files in bad:
        print(f"  FAIL  Test {'/'.join(nums)}: {f} is not in {', '.join(os.path.basename(x) for x in files)}")
    print(f"{'PASS' if not bad else 'FAIL'}: {len(bad)} figures not in their run, of {checked} checked; bar was 0")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
