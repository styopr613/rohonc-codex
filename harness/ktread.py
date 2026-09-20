"""The method the other five were not: read the passage and guess from context.

Five mechanical attempts failed (ktextend.py, ktalign.py, ktdistrib.py). All
five aligned or counted. Kiraly and Tokai did neither: they read a passage,
guessed a code's meaning from what surrounded it, checked the guess against
every other place the code occurs, and kept it only if it worked everywhere.

This renders the evidence a reader would need. For a target code it prints
every line containing it with all OTHER codes glossed, so the target appears as
a blank in readable context. Whoever reads it -- a person, or the model running
this harness -- proposes a meaning. The proposal is then checked the way
Kiraly's are: against every occurrence, not the ones that suggested it.

It is gated exactly like the other five and for a sharper reason. Guessing a
word from context is what a language model does, and it is also how a language
model produces confident nonsense. So the gate is run on codes the dictionary
already defines, with their glosses hidden, and the reader's answers are
compared with Kiraly and Tokai's. A reader who cannot recover known glosses has
no standing to propose unknown ones.

    python ktread.py --hide 6 --skip 45   # blind contexts for held-out codes
    python ktread.py --undefined 6        # contexts for undefined codes

RESULT OF THE FIRST GATE RUN, recorded here because it is the whole point.

Six defined codes ranked 46-51 by frequency were blinded and read from context
by the model running this harness. Codes below the top forty were chosen
deliberately: the twenty commonest had already been printed with their glosses
earlier in the session, so recalling them would not have been reading. The
guesses were written down before the answers were looked at.

    target  occurrences  guessed              dictionary
    1       75           temple               Jerusalem
    2       72           sin / transgress     will / want / future auxiliary
    3       71           with / among         among / call / from / from among
    4       71           to (dative)          end / side
    5       69           father               father / forefather
    6       68           paradise / garden    away / to

One clean hit by reading (3). One correct but obtained by cross-referencing an
earlier printout in which that position was already glossed, which is a real
technique and not the one under test (5). One near miss in the right semantic
field (1). Three wrong (2, 4, 6).

So one to two of six, single-shot. Better than any of the five mechanical
methods, which reached 8-15% while allowed five guesses each, and nowhere near
enough to put a meaning on an undefined code.

Target 4 is the reason this gate exists. The context was a formula repeated
verbatim on two folios -- glory and thanks given, then the target, then "you" --
which reads unmistakably as a dative. The confidence was high. The dictionary
gives "end; side". Clean reasoning, confident output, completely wrong, caught
only by checking against a known answer. A method whose failures look exactly
like its successes has to be scored on solved cases before it is pointed at
unsolved ones.

What separates this from what Kiraly and Tokai do is not the guessing, which is
shared and unreliable for both. It is that a guess there is carried to all
seventy-five occurrences and discarded if it fails at any one of them, then
made again the next day. This was one pass.
"""
import argparse
from collections import Counter

import ktdict
import ktextend as E
import rohonc_kt as KT

MAXCTX = 14


def load(blocktypes=("main", "picture")):
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load(blocktypes=blocktypes)
    return gl, doc


def short(gl, code, hide=frozenset(), width=22):
    """A compact gloss for rendering context: senses joined, metalanguage kept."""
    if code in hide or code not in gl:
        return None
    g = sorted(gl[code])
    out = []
    for s in g:
        s2 = s.strip()
        if s2.startswith("<") and s2.endswith(">"):
            s2 = s2[1:-1]
        out.append(s2)
    j = "/".join(out)
    return j[:width]


def contexts(gl, doc, target, hide=frozenset(), limit=MAXCTX):
    """[(page, line no, rendered line)] for lines containing `target`."""
    out = []
    for p in doc:
        for li, runs in enumerate(p.lines, 1):
            toks = [t for run in runs for t in run]
            if target not in toks:
                continue
            cells = []
            for t in toks:
                if t == target:
                    cells.append("[???]")
                else:
                    s = short(gl, t, hide)
                    cells.append(s if s else "·")
            out.append((p.page, li, "  ".join(cells)))
            if len(out) >= limit:
                return out
    return out


def truth_stems(gl, code):
    out = set()
    for s in gl.get(code, ()):
        s2 = E.META.sub(" ", s)
        out |= {E.stem(w) for w in E.WORD.findall(E.fold(s2).lower())
                if w not in E.STOP and len(w) > 2}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hide", type=int, default=0,
                    help="number of frequent DEFINED codes to blind and print")
    ap.add_argument("--skip", type=int, default=0)
    ap.add_argument("--code", default=None)
    ap.add_argument("--undefined", type=int, default=0,
                    help="print contexts for the N commonest UNdefined codes")
    ap.add_argument("--ctx", type=int, default=MAXCTX)
    a = ap.parse_args()
    gl, doc = load()
    freq = Counter(t for p in doc for t in p.tokens)

    if a.code:
        targets = [a.code]
        hide = frozenset(targets)
    elif a.undefined:
        targets = [t for t, _ in freq.most_common() if t not in gl][:a.undefined]
        hide = frozenset()
    else:
        defined = [t for t, _ in freq.most_common() if t in gl]
        targets = defined[a.skip:a.skip + a.hide]
        hide = frozenset(targets)

    for n, t in enumerate(targets, 1):
        print("=" * 78)
        print(f"TARGET {n}  (code occurs {freq[t]} times"
              + (f", {len(gl[t])} senses in the dictionary)" if t in gl else ", undefined)"))
        print("=" * 78)
        for pg, li, line in contexts(gl, doc, t, hide, a.ctx):
            print(f"  {pg}:{li:02d}  {line}")
        print()


if __name__ == "__main__":
    main()
