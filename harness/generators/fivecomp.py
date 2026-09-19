"""voynich-fingerprint's five-component generative model (Sachak 2026).

BPE syllable inventory -> bigram chain over syllables -> cross-word onset
conditioning -> reweighting on (length x final syllable) -> word-pair memory
with self-citation and mutation, plus a layout layer.

Run at its frozen configuration, which was tuned on the even-leaf half. We do
not retune it: it arrives already fitted to this split, and refitting it here
would give it a budget the other processes did not have.
"""
import os
import sys

import corpus
import layout
from . import register

FP = os.path.join(corpus.ROOT, "refs", "voynich-fingerprint", "analysis")
if FP not in sys.path:
    sys.path.insert(0, FP)

from voynich_artgen import ArtGenerator          # noqa: E402
from tier2_metrics import GALLOWS                # noqa: E402
import json                                       # noqa: E402

FROZEN = os.path.join(corpus.ROOT, "refs", "voynich-fingerprint",
                      "frozen", "FROZEN_CONFIG.json")


def _build(train, cfg):
    tw = corpus.words(train)
    tr_plain = corpus.plain(train)
    g = ArtGenerator(tw, merges=cfg["merges"])
    g.calibrate()
    g.calibrate_onset(tw)
    g.calibrate_cross_onset(tw)
    g.calibrate_common(tw)
    g.calibrate_pairs(tw)
    g.calibrate_lengths(tr_plain)
    g.fit_penalty = cfg["fit_penalty"]
    g.calibrate_proposal()
    g.calibrate_layout(tr_plain, gallows_p=0.0)
    g.gallows_scale = cfg["gallows_scale"]
    # line-initial gallows rate is calibrated to TRAIN, not to the held-out half
    target = sum(1 for ln in (l for p in tr_plain for l in p)
                 if ln and any(ln[0].startswith(x) for x in GALLOWS)) / \
        sum(1 for p in tr_plain for l in p if l)
    probe = [ln for p in g.document(n_paragraphs=40, seed=3) for ln in p]
    nat = sum(1 for ln in probe if ln and any(ln[0].startswith(x) for x in GALLOWS)) / len(probe)
    g.line_gallows_p = max(0.0, (target - nat) / (1 - nat))
    return g


@register("fivecomp", kind="self", label="five-component model (fingerprint)",
          note="frozen config, tuned on this same TRAIN half by its author")
def generate(spec, train, seed=0):
    cfg = json.load(open(FROZEN, encoding="utf-8"))
    g = _build(train, cfg)
    paras = g.document(
        n_paragraphs=len(spec), seed=seed + 7,
        p_copy=cfg["p_copy"], recency_alpha=cfg["recency_alpha"],
        recency_window=cfg["recency_window"], buffer_size=cfg["buffer_size"],
        cross_onset=cfg["cross_onset"], use_onset=cfg["use_onset"],
        gallows_scale=cfg["gallows_scale"], p_repeat=cfg["p_repeat"],
        p_pair=cfg["p_pair"], copy_decay=cfg["copy_decay"],
        line_fit=cfg["line_fit"])
    return layout.from_paras(spec, paras), {"config": "FROZEN_CONFIG.json"}
