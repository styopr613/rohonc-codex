"""How much of the Rohonc can any method reach? An upper bound, from testability.

Seven attempts to extend Kiraly & Tokai's dictionary failed here. The eighth
line of attack -- reading the illustrations, which is how Tokai found his
entry points -- ran into something more basic, and this measures it.

A proposed meaning is only worth anything if it can be rejected. One kind of
rejection needs other occurrences: you carry the guess to the code's other
appearances and discard it if it fails at any. A code occurring once admits no
such test, and the figures below are the ceiling on THAT kind of verification.

They are not a ceiling on decipherment, and an earlier version of this file
said they were. A one-off code is still constrained by the sentence around it,
by a gospel parallel if the passage localises, and by any picture beside it --
none of which needs the code to recur. Those constraints get stronger as the
rest of the dictionary fills in, so the untestable residue is not a wall but
the last thing in a sequence. `kthapax.txt` measures the effect: solve every
code with three or more occurrences and 36.6% of one-off codes end up in a
sentence where every other word is known, against 4.9% today.

So the question is how much of the remaining text sits on codes that can be
checked against themselves -- which is what this measures -- and the rest is
reachable only after that work is done, not instead of it.

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
    print(f"  once: {hapax/n*100:.1f}% of the book. They cannot be checked against")
    print("  themselves. They can still be constrained by a sentence whose other")
    print("  words are known -- see kthapax.txt -- so this is a ceiling on")
    print("  self-verification, not on decipherment.")


if __name__ == "__main__":
    main()
