"""Which end of a stored Rohonc line is the beginning of the sentence?

The codex is written right to left. The recovered transcription does not
document whether it stores each line in reading order or in visual order, and
the whole line-break measurement turns on the answer: mutual information is
symmetric, so the within-line figure is the same either way, but the
across-break pair is (end of this line, start of the next) and reversing the
storage swaps which token is which.

External clues point both ways. The delimiter symbol, which Kiraly & Tokai
report separates sentences, sits at the stored end of the line in 94% of its
appearances, which suits stored = reading order. The physical-damage marker
sits at the stored start more often than the stored end (126 to 77), which
suits the opposite. Neither settles it.

This settles it from the text. Pages were filled top to bottom, and Kiraly &
Tokai note that the bottom line of a page is sometimes incomplete. An
incomplete line has a genuine beginning -- the scribe started it normally --
and a spurious ending, because the text simply ran out. So:

    if storage is reading order, the stored-FIRST token of an incomplete line
    should look like a normal line opener, and its stored-LAST token should
    NOT look like a normal line closer;

    if storage is reversed, the reverse.

The two hypotheses make opposite predictions about the same measurement, which
is what makes the test decisive rather than a matter of relabelling. Measured
as the mean log2 lift of each token over its plain frequency, under opener and
closer distributions estimated from complete lines only.

    python roho_orient.py
"""
import math
from collections import Counter

import rohonc

ALPHA = 0.5          # add-alpha smoothing over the observed type inventory


def _lift(tokens, pool, base, types):
    """Mean log2 (P_pool(t) / P_base(t)), smoothed. Positive = fits the pool."""
    npool = sum(pool.values()) + ALPHA * types
    nbase = sum(base.values()) + ALPHA * types
    out = []
    for t in tokens:
        p = (pool[t] + ALPHA) / npool
        q = (base[t] + ALPHA) / nbase
        out.append(math.log2(p / q))
    return (sum(out) / len(out) if out else 0.0), len(out)


def main():
    doc = rohonc.load()
    lines = []          # (page index, line index within page, token list)
    for pi, p in enumerate(doc):
        for li, runs in enumerate(p.lines):
            toks = [t for run in runs for t in run]
            if toks:
                lines.append((pi, li, toks, li == len(p.lines) - 1))

    lens = sorted(len(t) for _, _, t, _ in lines)
    med = lens[len(lens) // 2]
    print(f"{len(lines)} lines, median length {med} tokens")

    # complete lines: not page-final, and of typical length or longer
    complete = [t for _, _, t, final in lines if not final and len(t) >= med]
    # incomplete lines: page-final and clearly short
    incomplete = [t for _, _, t, final in lines if final and len(t) <= med * 0.6]
    print(f"complete lines used to build the pools: {len(complete)}")
    print(f"incomplete page-final lines tested:     {len(incomplete)}")
    if len(incomplete) < 20:
        print("too few incomplete lines to decide")
        return

    base = Counter(t for toks in complete for t in toks)
    types = len(set(t for _, _, toks, _ in lines for t in toks))
    S = Counter(toks[0] for toks in complete)     # stored-first pool
    E = Counter(toks[-1] for toks in complete)    # stored-last pool

    s_lift, n1 = _lift([t[0] for t in incomplete], S, base, types)
    e_lift, n2 = _lift([t[-1] for t in incomplete], E, base, types)

    print("\nhow well each end of an incomplete line fits the matching pool,")
    print("in bits of lift over the token's plain frequency:\n")
    print(f"  stored-FIRST token vs the stored-first pool   {s_lift:+.3f} bits  (n={n1})")
    print(f"  stored-LAST  token vs the stored-last  pool   {e_lift:+.3f} bits  (n={n2})")

    # control: the same measurement on complete lines, held out
    half = len(complete) // 2
    a, b = complete[:half], complete[half:]
    bs = Counter(t for toks in a for t in toks)
    Sa, Ea = Counter(t[0] for t in a), Counter(t[-1] for t in a)
    cs, _ = _lift([t[0] for t in b], Sa, bs, types)
    ce, _ = _lift([t[-1] for t in b], Ea, bs, types)
    print(f"\n  control, complete lines held out:  first {cs:+.3f}   last {ce:+.3f}")
    print("  (both genuine, so both should be clearly positive and similar)")

    print()
    if s_lift > e_lift:
        print("  VERDICT: the stored FIRST token is the genuine one, so the file")
        print("  stores READING order and `rohonc.load()` needs no reversal.")
    else:
        print("  VERDICT: the stored LAST token is the genuine one, so the file")
        print("  stores VISUAL order and must be reversed to read it.")
    print(f"  margin: {abs(s_lift - e_lift):.3f} bits")


if __name__ == "__main__":
    main()
