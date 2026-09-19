"""The ruler. One metric vector, computed the same way for every process.

Three blocks:

  text    15 metrics, exactly voynich-fingerprint's tier-1 vector
  struct  27 metrics, exactly its tier-2 vector minus the two layout-given keys
          it skips when scoring ("paras", "para lines mean")
  line     8 metrics, new here: the line- and section-level properties that
          voynich-toolkit found and the fingerprint repo does not measure

The first two blocks are computed by calling the fingerprint repo's own
functions, so our numbers for those are directly comparable to the figures it
publishes. `gate.py` checks that they still are.

Scores are mean absolute percentage error against a reference profile, using
the fingerprint repo's `err()` so that a zero target is handled its way.
"""
import math
import random
import os
import sys
from collections import Counter, defaultdict

import corpus

FP = os.path.join(corpus.ROOT, "refs", "voynich-fingerprint", "analysis")
if FP not in sys.path:
    sys.path.insert(0, FP)

from refstats import fingerprint                      # noqa: E402
from generate_evaluate import edge_stats, cross_MI    # noqa: E402
from tier2_metrics import measure_document, GALLOWS   # noqa: E402
from tune_artgen import err                           # noqa: E402

# keys measure_document reports but compare_generators.py excludes from scoring
SKIP = {"paras", "para lines mean"}

BLOCKS = ("text", "struct", "line")

# metrics whose value is dictated by the layout spec every generator is handed,
# not earned by the process. Reported, but flagged in the write-up.
LAYOUT_GIVEN = {"lines", "line chars mean", "line chars sd", "words per line mean"}


# --------------------------------------------------------------------------
# block 1: text (15) -- fingerprint tier-1
# --------------------------------------------------------------------------
def text_block(ws):
    fp = fingerprint(ws)
    o5, f5, fy, t10 = edge_stats(ws)
    return {
        "h1 (char)": fp["h1_char"],
        "h2 (char)": fp["h2_char"],
        "H(word)": fp["h_word"],
        "TTR": fp["ttr"],
        "hapax %": fp["hapax_%"],
        "mean word len": fp["mean_len"],
        "sd word len": fp["sd_len"],
        "H init": fp["h_pos_init"],
        "H final": fp["h_pos_final"],
        "len dist TV": 0.0,          # comparative; filled by score()
        "top-5 onsets %": 100 * o5,
        "top-5 finals %": 100 * f5,
        "final-y %": 100 * fy,
        "top-10 word share %": 100 * t10,
        "cross-word MI": cross_MI(ws),
    }


# --------------------------------------------------------------------------
# block 3: line / section level (8) -- new
# --------------------------------------------------------------------------
def _cross_line_repeat(paras):
    """Currier 7a: a word almost never repeats across a line boundary."""
    n = rep = 0
    for p in paras:
        for a, b in zip(p.lines, p.lines[1:]):
            if not a or not b:
                continue
            n += 1
            if a[-1] == b[0]:
                rep += 1
    return 100 * rep / n if n else 0.0


def _line_final_char(paras, ch="m"):
    """Currier 7b: what share of all 'm' glyphs sit at the end of a line."""
    tot = fin = 0
    for p in paras:
        for ln in p.lines:
            if not ln:
                continue
            tot += sum(w.count(ch) for w in ln)
            if ln[-1].endswith(ch):
                fin += 1
    return 100 * fin / tot if tot else 0.0


def _gallows_para_lift(paras):
    """Simple gallows as capital letters: does a paragraph's first line start
    with one more often than its continuation lines?

    Measured on the line's FIRST word, the same convention as tier-2's
    "para/line-initial gallows %", so the two are read on the same scale.
    Reported in percentage points.
    """
    def rate(lines):
        lines = [ln for ln in lines if ln]
        if not lines:
            return 0.0
        return sum(1 for ln in lines
                   if any(ln[0].startswith(g) for g in GALLOWS)) / len(lines)
    first = [p.lines[0] for p in paras if p.lines]
    cont = [ln for p in paras for ln in p.lines[1:]]
    return 100 * (rate(first) - rate(cont))


def _para_coherence(paras):
    """Lines inside a paragraph share vocabulary; lines from different
    paragraphs share less. Both sides are line-vs-line, so the scopes match.
    """
    def jac(a, b):
        A, B = set(a), set(b)
        u = len(A | B)
        return len(A & B) / u if u else 0.0
    usable = [p for p in paras if len(p.lines) >= 2]
    intra = [jac(a, b) for p in usable for a, b in zip(p.lines, p.lines[1:])]
    # matched control: last line of one paragraph vs first line of the next
    inter = [jac(a.lines[-1], b.lines[0]) for a, b in zip(usable, usable[1:])]
    mi = sum(intra) / len(intra) if intra else 0.0
    me = sum(inter) / len(inter) if inter else 0.0
    return mi / me if me else 0.0


def _mi_raw(paras, attr, labels=None):
    joint = defaultdict(Counter)
    for i, p in enumerate(paras):
        lab = labels[i] if labels is not None else getattr(p, attr)
        for w in p.words:
            joint[lab][w] += 1
    total = sum(sum(c.values()) for c in joint.values())
    if not total:
        return 0.0
    pw = Counter()
    for c in joint.values():
        pw.update(c)
    mi = 0.0
    for c in joint.values():
        ps = sum(c.values()) / total
        for w, n in c.items():
            pws = n / total
            mi += pws * math.log2(pws / (ps * pw[w] / total))
    return mi


def _word_section_MI(paras, attr="section", shuffles=5, seed=408):
    """Montemurro: does word identity carry information about the section?

    Plug-in MI is badly biased upward by vocabulary size, which would let a
    generator score well for having the right TTR and no section structure at
    all. So the reported value is raw MI minus the mean of a label-shuffle
    null: the paragraph labels are permuted, which preserves vocabulary,
    paragraph sizes and label frequencies and destroys only the association.
    What is left is the section-specificity itself.
    """
    raw = _mi_raw(paras, attr)
    labs = [getattr(p, attr) for p in paras]
    rng = random.Random(seed)
    nulls = []
    for _ in range(shuffles):
        perm = labs[:]
        rng.shuffle(perm)
        nulls.append(_mi_raw(paras, attr, labels=perm))
    return raw - sum(nulls) / len(nulls)


def _currier_jaccard(paras):
    """Vocabulary overlap between Currier language A and B."""
    A = set(w for p in paras if p.lang == "A" for w in p.words)
    B = set(w for p in paras if p.lang == "B" for w in p.words)
    u = len(A | B)
    return len(A & B) / u if u else 0.0


def _len_autocorr(paras):
    """Gaskell: gibberish clusters word lengths (short-short-long-long)."""
    xs = []
    for p in paras:
        for ln in p.lines:
            xs.extend(len(w) for w in ln)
    n = len(xs)
    if n < 3:
        return 0.0
    m = sum(xs) / n
    num = sum((xs[i] - m) * (xs[i + 1] - m) for i in range(n - 1))
    den = sum((x - m) ** 2 for x in xs)
    return num / den if den else 0.0


def _triple_repeats(ws):
    """Per 10k tokens: w w w. Gaskell flags triples as a gibberish signature."""
    n = sum(1 for a, b, c in zip(ws, ws[1:], ws[2:]) if a == b == c)
    return 10000 * n / max(1, len(ws))


def line_block(paras, ws):
    return {
        "cross-line repeat %": _cross_line_repeat(paras),
        "m line-final %": _line_final_char(paras, "m"),
        "gallows para-start lift": _gallows_para_lift(paras),
        "para vocab coherence": _para_coherence(paras),
        "word-section MI (bits)": _word_section_MI(paras, "section"),
        "Currier A/B jaccard": _currier_jaccard(paras),
        "word-len autocorr": _len_autocorr(paras),
        "triple repeats /10k": _triple_repeats(ws),
    }


# --------------------------------------------------------------------------
# assembly
# --------------------------------------------------------------------------
def profile(doc):
    """Metric vector of one document. `doc` is a list of corpus.Para."""
    ws = corpus.words(doc)
    struct, _ = measure_document(corpus.plain(doc))
    return {
        "text": text_block(ws),
        "struct": {k: v for k, v in struct.items() if k not in SKIP},
        "line": line_block(doc, ws),
        "_lendist": Counter(len(w) for w in ws),
        "_n": len(ws),
    }


def score(gen, ref):
    """Per-metric absolute percentage error, generated against reference."""
    out = {}
    for blk in BLOCKS:
        out[blk] = {k: err(gen[blk][k], ref[blk][k]) for k in ref[blk]}
    # len dist TV is comparative: total variation between the two length distributions
    g, r = gen["_lendist"], ref["_lendist"]
    gt, rt = sum(g.values()), sum(r.values())
    tv = 0.5 * sum(abs(g[k] / gt - r[k] / rt) for k in set(g) | set(r))
    out["text"]["len dist TV"] = 100 * tv      # target is 0, so TV *is* the error
    return out


def means(sc):
    """Block means and overall mean of a score dict."""
    per = {b: sum(sc[b].values()) / len(sc[b]) for b in BLOCKS}
    allv = [v for b in BLOCKS for v in sc[b].values()]
    per["overall"] = sum(allv) / len(allv)
    per["fingerprint44"] = (sum(sc["text"].values()) + sum(sc["struct"].values())) / (
        len(sc["text"]) + len(sc["struct"]))
    return per


if __name__ == "__main__":
    d = corpus.load()
    tr, te = corpus.split(d)
    p = profile(te)
    for b in BLOCKS:
        print(f"--- {b} ({len(p[b])}) ---")
        for k, v in p[b].items():
            flag = "  [layout-given]" if k in LAYOUT_GIVEN else ""
            print(f"  {k:30s} {v:10.4f}{flag}")
    print(f"\nheld-out tokens: {p['_n']}")
