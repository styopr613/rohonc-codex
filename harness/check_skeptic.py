"""Every figure SKEPTIC.md prints must stand in the saved run it names.

The bar is ZERO mismatches, declared here before the first run.

SKEPTIC.md is the page for the skeptic, written in plain words from a forum
reply. Its figures sit in indented blocks, and each block names its saved run
in brackets on its first line: `(ktpassid2.txt)`. Every number in the block --
a percentage, a count, a fraction like 9/20 or 0 / 20 -- must appear verbatim
in that run. A block that names no run, or a run that is missing, fails.
The test labels themselves ("Test 15") are not figures and are skipped.

    python3 check_skeptic.py
"""
import os
import re
import sys

import corpus

DOC = os.path.join(corpus.ROOT, "SKEPTIC.md")
WORK = os.path.join(corpus.ROOT, "work", "rohonc")
NUM = re.compile(r"\d+\s?/\s?\d+|\d+(?:\.\d+)?%?")


def blocks(txt):
    out, cur = [], []
    for line in txt.splitlines():
        if line.startswith("    ") and line.strip():
            if cur and re.search(r"\([\w.]+\.txt\)", line):
                out.append(cur)
                cur = []
            cur.append(line.strip())
        elif cur and not line.strip():
            continue
        elif cur:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def main():
    bad, n = [], 0
    for blk in blocks(open(DOC, encoding="utf-8").read()):
        m = re.search(r"\(([\w.]+\.txt)\)", blk[0])
        if not m:
            bad.append(f"block names no run: {blk[0]}")
            continue
        path = os.path.join(WORK, m.group(1))
        if not os.path.exists(path):
            bad.append(f"missing run {m.group(1)}")
            continue
        run = open(path, encoding="utf-8").read()
        for line in blk:
            line = re.sub(r"\([\w.]+\.txt\)|Test \d+", "", line)
            for tok in NUM.findall(line):
                n += 1
                if tok not in run:
                    bad.append(f"{m.group(1)}: {tok!r} not in run  ({line.strip()})")
    for b in bad:
        print("MISMATCH " + b)
    print(f"{'PASS' if not bad else 'FAIL'}: {len(bad)} figures not in their run, of {n} checked; bar was 0")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
