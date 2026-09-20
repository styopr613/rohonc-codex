"""How much of the Rohonc can any method reach? An upper bound, from testability.

Seven attempts to extend Kiraly & Tokai's dictionary failed here. The eighth
line of attack -- reading the illustrations, which is how Tokai found his
entry points -- ran into something more basic, and this measures it.

A proposed meaning is only worth anything if it can be rejected. Rejection
needs other occurrences: you carry the guess to the code's other appearances
and discard it if it fails at any. A code that occurs once in the book cannot
be tested by anyone, ever, by any method. Whatever is proposed for it is
unfalsifiable -- not hard, not unsolved, but outside the reach of evidence.

So the question is not how clever a method is. It is how much of the remaining
text sits on codes that occur often enough to be checked at all. That is a
ceiling, and it binds Kiraly and Tokai exactly as it binds this harness.

    python ktceiling.py
"""
from collections import Counter

import ktdict
import rohonc_kt as KT


def main():
    d = ktdict.load()
    defined = {c for c, _, _ in d}
    doc = KT.load(blocktypes=("main", "picture"))
    toks = [t for p in doc for t in p.tokens]
    types = Counter(toks)
    n = len(toks)

    cov = sum(c for t, c in types.items() if t in defined)
    und = {t: c for t, c in types.items() if t not in defined}
    print("=" * 74)
    print("THE TESTABILITY CEILING")
    print("=" * 74)
    print(f"text: {n} word tokens, {len(types)} types")
    print(f"dictionary covers {cov} tokens ({cov/n*100:.1f}%), "
          f"{sum(1 for t in types if t in defined)} types")
    print(f"undefined: {sum(und.values())} tokens ({sum(und.values())/n*100:.1f}%), "
          f"{len(und)} types\n")

    print("undefined vocabulary by how often it occurs:")
    print(f"{'occurrences':>12s} {'types':>7s} {'tokens':>8s} {'% of text':>10s}")
    bands = [(1, 1), (2, 2), (3, 4), (5, 9), (10, 29), (30, 10 ** 9)]
    for lo, hi in bands:
        ts = [t for t, c in und.items() if lo <= c <= hi]
        tk = sum(und[t] for t in ts)
        lab = f"{lo}" if lo == hi else (f"{lo}+" if hi > 10 ** 8 else f"{lo}-{hi}")
        print(f"{lab:>12s} {len(ts):7d} {tk:8d} {tk/n*100:9.2f}%")

    print("\nceiling: if a code needs k occurrences to be testable at all,")
    print("the best coverage any method could ever reach is\n")
    print(f"{'k':>4s} {'reachable types':>16s} {'ceiling coverage':>18s}")
    for k in (1, 2, 3, 5, 10):
        add = sum(c for t, c in und.items() if c >= k)
        ts = sum(1 for t, c in und.items() if c >= k)
        print(f"{k:4d} {ts:16d} {(cov + add)/n*100:17.1f}%")

    hapax = sum(c for t, c in und.items() if c == 1)
    print(f"\n  {sum(1 for c in und.values() if c == 1)} undefined codes occur exactly")
    print(f"  once: {hapax/n*100:.1f}% of the book, unfalsifiable by construction.")
    print("  No method reaches them, and none ever will.")


if __name__ == "__main__":
    main()
