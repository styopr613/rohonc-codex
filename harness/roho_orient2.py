"""Orientation, decided by the codex's own repeated passages.

The first attempt at this (`roho_orient.py`) failed its own control and its
verdict was discarded: line-opener and line-closer pools in the Rohonc are too
weak to classify anything, so the measurement had no power. This one uses the
property the Rohonc actually has in abundance, and the one Gyurk used in 1970 --
long verbatim repeats.

The logic. Under either storage orientation, the within-line token sequences
are mirror images of each other, so any inventory built from them has the same
size and the same repeat structure; orientation alone cannot be read off from
inside a line. The line BOUNDARY is different. Under reading order the boundary
runs (tail of this line, head of the next); under the reversed reading it runs
(head of this line, tail of the next). Those are different sequences, not
mirror images, so the two hypotheses make different predictions.

The test: build the inventory of token n-grams that occur strictly inside a
line, then ask how often a sequence straddling a line break is one the codex
also writes inside a line. If the text is continuous, the correct orientation
makes boundary sequences look like ordinary text and the wrong one makes them
look like nonsense.

The baseline is a shuffle of which line follows which within a page, which
preserves every line intact and destroys only the pairing. That is the rate of
accidental matches for these lines and this inventory.

    python roho_orient2.py
"""
import random
from collections import Counter

import rohonc

SEED = 408
SHUFFLES = 20


def line_tokens(doc):
    """Per page, the list of lines as flat token lists (storage order)."""
    out = []
    for p in doc:
        ls = [[t for run in runs for t in run] for runs in p.lines]
        out.append([l for l in ls if l])
    return out


def inventory(pages, n, rev):
    inv = Counter()
    for ls in pages:
        for l in ls:
            s = l[::-1] if rev else l
            for i in range(len(s) - n + 1):
                inv[tuple(s[i:i + n])] += 1
    return inv


def boundary_grams(pages, n, rev, order=None):
    """n-grams straddling a line break, half from each side."""
    h = n // 2
    out = []
    for pi, ls in enumerate(pages):
        idx = order[pi] if order else list(range(len(ls)))
        for a, b in zip(idx, idx[1:]):
            x = ls[a][::-1] if rev else ls[a]
            y = ls[b][::-1] if rev else ls[b]
            if len(x) >= h and len(y) >= n - h:
                out.append(tuple(x[-h:]) + tuple(y[:n - h]))
    return out


def rate(grams, inv):
    if not grams:
        return 0.0
    return sum(1 for g in grams if inv.get(g, 0) > 0) / len(grams) * 100


def main():
    doc = rohonc.load()
    pages = line_tokens(doc)
    rng = random.Random(SEED)

    print(f"{len(pages)} pages, {sum(len(l) for l in pages)} lines")
    for n in (2, 3, 4):
        inv_f = inventory(pages, n, False)
        rep_f = sum(1 for g, c in inv_f.items() if c > 1)
        print(f"\n{n}-gram inventory inside lines: {len(inv_f)} distinct, "
              f"{rep_f} of them repeated")
        print(f"{'':26s} {'boundary in inventory':>22s} {'shuffled':>10s} "
              f"{'sd':>7s} {'sigma':>7s}")
        for lab, rev in (("stored order (as-is)", False),
                         ("reversed (visual->reading)", True)):
            inv = inventory(pages, n, rev)
            obs = rate(boundary_grams(pages, n, rev), inv)
            nulls = []
            for _ in range(SHUFFLES):
                order = []
                for ls in pages:
                    idx = list(range(len(ls)))
                    rng.shuffle(idx)
                    order.append(idx)
                nulls.append(rate(boundary_grams(pages, n, rev, order), inv))
            m = sum(nulls) / len(nulls)
            sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
            sig = (obs - m) / sd if sd else 0.0
            print(f"  {lab:24s} {obs:21.2f}% {m:9.2f}% {sd:7.2f} {sig:7.1f}")

    print("\n  The orientation whose boundary sequences the codex also writes")
    print("  inside its lines is the reading order. A large sigma on one side")
    print("  and not the other decides it; two similar values mean the test")
    print("  has no power here and the question stays open.")


if __name__ == "__main__":
    main()
