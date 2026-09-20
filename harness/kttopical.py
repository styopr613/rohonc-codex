"""Find the undefined codes worth attacking: the topically concentrated ones.

An earlier attempt (ktextend.py, gate 2) tried to crack undefined codes by the
gospel words enriched near the pages they appear on. It returned the same five
words -- lord, him, god, Jesus, son -- for every code, and scored 5%. The flaw
was targeting, not method: it treated function words and content words alike,
and a function word spread evenly through the book has no neighbourhood to be
enriched in.

This separates them. For each undefined code, measure how far its distribution
across the codex departs from the book's own, by KL divergence over twenty-folio
bands. A code confined to one stretch is tied to whatever that stretch is about
and can be reached through the section's readable vocabulary. A code spread
evenly is grammatical and cannot.

It works as a filter: of 47 undefined codes occurring 25 or more times, the two
most concentrated sit entirely -- 100% of 33 and 31 occurrences -- inside
folios 140-159, while the flattest sit at KL 0.04 with no band holding more
than 15%.

It does not by itself solve anything. The first code it surfaced produced a
clean hypothesis from the section's vocabulary (the kingdom-of-heaven formula
beside virgins and maidens, so the code between them reads as "like"), and the
hypothesis died on the other twenty-one occurrences. What the filter buys is
that the hypothesis was worth forming and cheap to kill.
"""
import math
from collections import Counter

import ktsolve


def folio(pg):
    try:
        return int(pg[:3])
    except (TypeError, ValueError):
        return None


def concentration(gl, doc, min_occ=25, band=20):
    freq = Counter(t for p in doc for t in p.tokens)
    und = {t for t, c in freq.items() if t not in gl and c >= min_occ}
    per, allb = {}, Counter()
    for p in doc:
        f = folio(p.page)
        if f is None:
            continue
        b = f // band * band
        allb[b] += len(p.tokens)
        for t in p.tokens:
            if t in und:
                per.setdefault(t, Counter())[b] += 1
    tot = sum(allb.values())
    rows = []
    for t, c in per.items():
        n = sum(c.values())
        if n < min_occ:
            continue
        kl = 0.0
        for b, k in c.items():
            pp, q = k / n, allb[b] / tot
            if pp > 0 and q > 0:
                kl += pp * math.log(pp / q)
        peak, pk = c.most_common(1)[0]
        rows.append({"code": t, "kl": kl, "n": n, "peak": peak,
                     "peak_share": pk / n})
    rows.sort(key=lambda r: -r["kl"])
    return rows


def section_vocabulary(gl, doc, lo, hi, k=18):
    sec = []
    for p in doc:
        f = folio(p.page)
        if f is not None and lo <= f < hi:
            sec += p.tokens
    c = Counter(t for t in sec if t in gl)
    return [("/".join(sorted(gl[t]))[:58], n) for t, n in c.most_common(k)]


if __name__ == "__main__":
    gl, doc = ktsolve.load()
    rows = concentration(gl, doc)
    print(f"{len(rows)} undefined codes with 25+ occurrences\n")
    print("MOST CONCENTRATED (content words, worth attacking)")
    print(f"{'KL':>5s} {'n':>5s} {'peak band':>11s} {'% there':>8s}")
    for r in rows[:8]:
        print(f"{r['kl']:5.2f} {r['n']:5d}  {r['peak']:3d}-{r['peak']+19:<4d}"
              f" {r['peak_share']*100:7.0f}%")
    print("\nFLATTEST (grammatical, not reachable this way)")
    for r in rows[-5:]:
        print(f"{r['kl']:5.2f} {r['n']:5d}  {r['peak']:3d}-{r['peak']+19:<4d}"
              f" {r['peak_share']*100:7.0f}%")
    lo = rows[0]["peak"]
    print(f"\nwhat folios {lo}-{lo+19} are about, by readable vocabulary:")
    for g, n in section_vocabulary(gl, doc, lo, lo + 20):
        print(f"   {n:4d}  {g}")
