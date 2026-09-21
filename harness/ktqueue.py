"""The worklist, kept on disk, so the work survives a break in the session.

The reason this file exists: the grind stalls not because the next sign is
hard but because each new session has to rediscover WHICH sign is next, and
rediscovering it costs more than reading it. The queue is the memory.

WHAT IT RANKS. Every sign the rendering cannot read, ordered by what reading
it would actually buy: first the number of lines on which it is the ONLY
hole (reading it completes that line), then how often it occurs (an oftener
sign can be checked at more occurrences, so it can carry a real tier).

WHAT IT REMEMBERS. work/rohonc/queue.json holds one entry per sign that has
been dealt with:

    done   -- read; detected automatically the moment the sign appears in
              proposals.json, so nothing has to be marked by hand
    pass   -- looked at, not decided, with the reason written down; it drops
              to the bottom instead of reappearing at the top tomorrow
    open   -- never looked at

    python ktqueue.py next [N]      the next N, with every occurrence and
                                    the source note for each folio
    python ktqueue.py pass HEX why  park one, with the reason
    python ktqueue.py open HEX      un-park it
    python ktqueue.py status        how far the queue is, and what reading
                                    the rest of it would be worth
"""
import json
import os
import sys
from collections import Counter, defaultdict

import corpus
import ktaffix as A
import ktcross as K
import kttranslate as T

QUEUE = os.path.join(corpus.ROOT, "work", "rohonc", "queue.json")


def load():
    if os.path.exists(QUEUE):
        return json.load(open(QUEUE))
    return {}


def save(q):
    json.dump(q, open(QUEUE, "w"), indent=1, sort_keys=True)


def survey():
    """(rows, prop) -- rows are (hex, n_occurrences, n_sole_lines, [lines])."""
    gl, doc, seg, var, prop, inv = K.build()
    cnt = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    sole = Counter()
    where = defaultdict(list)
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            miss = {A.strip(t)[0] for t in tk if A.strip(t)[0] not in inv}
            if not miss:
                continue
            for b in miss:
                s = " ".join("<<___>>" if A.strip(t)[0] == b
                             else T.render_token(t, gl, seg, False, var, prop)
                             for t in tk)
                where[b].append((p.page, i, s, len(miss)))
            if len(miss) == 1:
                sole[next(iter(miss))] += 1
    rows = [(K.hx(b), cnt[b], sole[b], where[b]) for b in where]
    rows.sort(key=lambda r: (-r[2], -r[1], r[0]))
    return rows, prop


def main(argv):
    cmd = argv[0] if argv else "next"
    q = load()

    if cmd in ("pass", "open"):
        h = argv[1]
        if cmd == "open":
            q.pop(h, None)
        else:
            q[h] = {"state": "pass", "why": " ".join(argv[2:])}
        save(q)
        print(f"{h}: {cmd}")
        return 0

    rows, prop = survey()
    read = {K.hx(c) for c in prop}
    # anything now read is done, whatever the queue used to say
    for h in list(q):
        if h in read:
            q.pop(h)
    save(q)

    if cmd == "status":
        tot = sum(r[2] for r in rows)
        park = [h for h, v in q.items() if v["state"] == "pass"]
        rec = [r for r in rows if r[1] > 1]
        print(f"  unread signs                     {len(rows)}")
        print(f"    occurring more than once       {len(rec)}"
              f"   (sole hole on {sum(r[2] for r in rec)} lines)")
        print(f"    occurring once                 {len(rows) - len(rec)}"
              f"   (sole hole on {tot - sum(r[2] for r in rec)} lines)")
        print(f"  parked, with a reason            {len(park)}")
        print(f"  lines waiting on one sign        {tot}")
        return 0

    n = int(next((a for a in argv[1:] if a.isdigit()), 6))
    recur_only = "--all" not in argv
    shown = 0
    notes = {}
    for h, occ, sol, lines in rows:
        if h in read or (recur_only and occ < 2):
            continue
        st = q.get(h, {})
        if st.get("state") == "pass":
            continue
        print(f"\n=== {h}   x{occ}   sole hole on {sol} line(s)")
        for pg, i, s, nmiss in sorted(lines)[:8]:
            tag = "" if nmiss == 1 else f"  [{nmiss} holes]"
            print(f"  {pg}:{i:<3d}{tag} {s[:170]}")
            if pg not in notes:
                notes[pg] = K.note_for(pg)
            if notes[pg]:
                print(f"        src: {notes[pg][:250]}")
        shown += 1
        if shown >= n:
            break
    if not shown:
        print("queue empty at this filter")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
