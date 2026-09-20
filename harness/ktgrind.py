"""The worklist for the remaining unread signs, with every constraint attached.

Nothing here decides anything. For one unread sign it prints, in one place,
everything that bears on it:

  * every line it stands on, rendered as far as the line reads
  * the source note this project wrote for that folio, if there is one
  * READ signs one glyph away, and what they mean (candidates, not readings:
    ktswap.py measured that one glyph of distance preserves the reading only
    2.1% of the time, so this is a shortlist to test against context)
  * READ signs sharing a stem of three or more glyphs (the stronger relation:
    eleven spellings of the book's Joseph share the stem 286a10, and Kiraly
    and Tokai define one of them)
  * how many of the lines it stands on would be fully read if it were read

    python3 ktgrind.py                 # the worklist, best first
    python3 ktgrind.py HEX [HEX ...]   # the dossier for these signs
"""
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K

MIN_STEM = 3


def hx(s):
    return "".join(f"{ord(c)-0xE000:03x}" for c in s)


def shared(a, b):
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]:
        n += 1
    return n


def ed1(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(1 for x, y in zip(a, b) if x != y) == 1
    if len(a) > len(b):
        a, b = b, a
    i = 0
    while i < len(a) and a[i] == b[i]:
        i += 1
    return a[i:] == b[i + 1:]


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    cnt = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    read = [t for t in cnt if t in inv]
    unread = [t for t in cnt if t not in inv]
    G = lambda t: K.T.render_token(t, gl, seg, False, var, prop)

    # how many lines each unread sign is the ONLY hole on
    solo = Counter()
    lines_of = defaultdict(list)
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            miss = {A.strip(t)[0] for t in tk if A.strip(t)[0] not in inv}
            for b in miss:
                lines_of[b].append((p.page, i, tk))
            if len(miss) == 1:
                solo[next(iter(miss))] += 1

    def relatives(u):
        near = [r for r in read if len(r) >= 3 and ed1(u, r)]
        stem = [r for r in read
                if len(r) >= MIN_STEM and shared(u, r) >= MIN_STEM and r not in near]
        stem.sort(key=lambda r: -shared(u, r))
        return near, stem[:4]

    if argv:
        for h in argv:
            u = "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))
            near, stem = relatives(u)
            print(f"\n=== {h}   {cnt.get(u,0)} occurrence(s), sole hole on {solo[u]} line(s)")
            for r in near:
                print(f"    one glyph away : {hx(r):24s} {G(r)[:60]}")
            for r in stem:
                print(f"    shares {shared(u,r)} glyphs : {hx(r):24s} {G(r)[:60]}")
            for page, i, tk in lines_of.get(u, []):
                s = " ".join("<<___>>" if A.strip(t)[0] == u else G(t) for t in tk)
                print(f"    {page}:{i:<3d} {s[:150]}")
                note = K.note_for(page)
                if note:
                    print(f"         source: {note[:200]}")
        return 0

    rows = []
    for u in unread:
        if not solo[u]:
            continue
        near, stem = relatives(u)
        rows.append((solo[u], len(near) + len(stem), hx(u), cnt[u], near, stem))
    rows.sort(key=lambda r: (-r[0], -r[1]))
    print(f"{len(rows)} unread signs are the ONLY hole on at least one line")
    print(f"{sum(1 for r in rows if r[4] or r[5])} of them have a read relative\n")
    print(f"{'lines':>5s} {'n':>3s}  {'sign':24s} relatives")
    for solon, _, h, n, near, stem in rows[:50]:
        rel = "; ".join(G(r)[:24] for r in (near + stem)[:3])
        print(f"{solon:5d} {n:3d}  {h:24s} {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
