"""A Llull-style combinatoric machine.

Ramon Llull's Ars Magna (c. 1305) used concentric rotating disks, each carrying
a set of terms; a rotation produced a combination. The device was known in the
fifteenth century and is a standing candidate for a mechanical text generator
that predates and is simpler than a grille.

Each word slot is a disk. A word is the concatenation of whatever sits at the
selected position on each disk. Rotations are not uniform: a disk tends to
advance by one step, which is what turning a wheel by hand actually does, and
is the only source of local structure the device has.

Disk contents are drawn from the training text's own syllable inventory, so the
machine is given the manuscript's raw material and has to account only for how
the material is combined.
"""
import random
from collections import Counter

import corpus
import layout
from . import register

DEFAULTS = {"disks": 5, "faces": 14, "p_advance": 0.55, "p_blank": 0.3}


def syllables(words, n_per_slot=60):
    """Positional syllable inventory: what tends to appear at each slot."""
    slots = [Counter() for _ in range(6)]
    for w in words:
        parts, i = [], 0
        while i < len(w):
            for size in (3, 2, 1):
                if w[i:i + size]:
                    parts.append(w[i:i + size])
                    i += size
                    break
        for j, p in enumerate(parts[:6]):
            slots[j][p] += 1
    return [[s for s, _ in c.most_common(n_per_slot)] or [""] for c in slots]


def build_disks(train_words, cfg, rng):
    inv = syllables(train_words)
    disks = []
    for j in range(cfg["disks"]):
        pool = inv[min(j, len(inv) - 1)]
        faces = [pool[rng.randrange(len(pool))] for _ in range(cfg["faces"])]
        if j not in (0, 1):
            n_blank = max(1, int(cfg["faces"] * cfg["p_blank"]))
            for b in range(n_blank):
                faces[rng.randrange(cfg["faces"])] = ""
        disks.append(faces)
    return disks


@register("llull", kind="stream", label="Llull combinatoric disks",
          note="rotating disks over the manuscript's own syllable inventory")
def generate(spec, train, seed=0, cfg=None):
    cfg = {**DEFAULTS, **(cfg or {})}
    rng = random.Random(seed + 9)
    disks = build_disks(corpus.words(train), cfg, rng)
    pos = [0] * len(disks)

    def write():
        for i in range(len(disks)):
            if rng.random() < cfg["p_advance"]:
                pos[i] = (pos[i] + 1) % len(disks[i])
            else:
                pos[i] = rng.randrange(len(disks[i]))
        w = "".join(disks[i][pos[i]] for i in range(len(disks)))
        return w or "o"

    doc = []
    for ps in spec:
        lines = []
        for budget in ps.budgets:
            ln, used = [], 0
            while True:
                w = write()
                cost = len(w) + (1 if ln else 0)
                if ln and used + cost > budget:
                    break
                ln.append(w)
                used += cost
            lines.append(ln)
        doc.append(corpus.Para(folio=ps.folio, lines=lines, section=ps.section,
                               lang=ps.lang, hand=ps.hand))
    return doc, {"cfg": cfg, "cite": "Llull, Ars Magna (c.1305); Eco (1995) ch.4"}
