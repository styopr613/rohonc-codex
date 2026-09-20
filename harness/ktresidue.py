"""Rank the unknown PIECES that block the most words, not the words themselves.

Reading one sign at a time closes one sign at a time. But most unread words
are compounds: a run of pieces this project can already read, plus one piece
it cannot. The blocking piece is often shared by many different words, and
reading it closes all of them at once.

So: cut every unread word into known pieces plus AT MOST ONE unknown piece,
maximising the glyphs covered by known pieces (ktaffix's rule -- minimising
the number of pieces makes the whole word one unknown piece and always
wins). Then tally the unknown pieces by how many DISTINCT words they block
and how many tokens those words carry.

Nothing here reads anything. It says where reading would pay most.

    python ktresidue.py            # ranked blocking pieces
    python ktresidue.py 4b0        # the words one piece blocks, with counts
"""
import sys
from collections import Counter, defaultdict

import ktcontext as X
import ktcoverage as C
import ktsegment as S
import ktaffix as A


def inventory():
    gl, doc, seg, var = X.load()          # seg already extended, PROP filled
    inv = set(gl) | set(seg) | set(var) | set(X.PROP)
    return gl, doc, seg, var, inv


def cut_one(code, inv):
    """(pieces, unknown) covering the most glyphs with at most one unknown.

    best[i][u] = (covered, pieces) for the prefix of length i using u unknown
    pieces. u is 0 or 1. A known piece adds its length to `covered`; the one
    unknown piece adds nothing, so the search maximises known coverage and
    the unknown piece is whatever is left over.
    """
    n = len(code)
    best = [[None, None] for _ in range(n + 1)]
    best[0][0] = (0, [])
    for i in range(1, n + 1):
        for j in range(i):
            piece = code[j:i]
            known = piece in inv
            for u in (0, 1):
                if best[j][u] is None:
                    continue
                cov, ps = best[j][u]
                nu = u if known else u + 1
                if nu > 1:
                    continue
                cand = (cov + (len(piece) if known else 0), ps + [piece])
                cur = best[i][nu]
                if cur is None or cand[0] > cur[0] or (
                        cand[0] == cur[0] and len(cand[1]) < len(cur[1])):
                    best[i][nu] = cand
    r = best[n][1]
    if r is None:
        return None, None
    cov, ps = r
    if cov == 0:
        return None, None                  # nothing known: no information
    unk = [p for p in ps if p not in inv]
    return ps, unk[0]


def main(argv):
    gl, doc, seg, var, inv = inventory()
    toks = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    unread = [t for t in toks if t not in inv]

    words = defaultdict(list)              # unknown piece -> [(word, count)]
    for t in unread:
        ps, unk = cut_one(t, inv)
        if unk is None:
            continue
        words[unk].append((t, toks[t], ps))

    if argv:
        for h in argv:
            c = X.unhx(h)
            ws = sorted(words.get(c, []), key=lambda x: -x[1])
            tot = sum(n for _, n, _ in ws)
            print(f"\n=== {h}  blocks {len(ws)} words, {tot} tokens "
                  f"(itself {toks.get(c,0)} tokens) ===")
            for t, n, ps in ws:
                s = " + ".join(("[?" + X.hx(p) + "]" if p not in inv
                                else X.word(p, gl, seg, var)) for p in ps)
                print(f"  {n:4d}  {X.hx(t):26s}  {s}")
        return 0

    rank = sorted(words.items(),
                  key=lambda kv: -(sum(n for _, n, _ in kv[1]) + toks.get(kv[0], 0)))
    print(f"{len(unread)} unread word types, {sum(toks[t] for t in unread)} tokens")
    print(f"{len(words)} distinct blocking pieces\n")
    print(f"{'piece':26s} {'words':>6s} {'their tokens':>13s} {'own tokens':>11s}")
    for c, ws in rank[:60]:
        print(f"{X.hx(c):26s} {len(ws):6d} {sum(n for _, n, _ in ws):13d} "
              f"{toks.get(c,0):11d}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
