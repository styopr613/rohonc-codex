"""Cut traced words into their signs: our own sign set, in the scribe's pen.

kttrace.py finds whole words in the scan and traces them, because a word is
distinctive enough to find and a lone sign is not. This takes each word that
passed its agreement bar and cuts it into the signs it is made of.

HOW. The word's key was laid out from Király and Tokai's outlines, so it says
roughly where each sign sits, left to right. Each stroke of the traced ink
(a connected run of it) goes to the sign whose span holds its centre; a stroke
that runs across two spans is split at the boundary. Every sign then has one
cut per word it occurs in.

THE CHECK. A cut is compared with their outline of that sign -- both scaled to
the same box -- and with the other cuts of the same sign. The cut kept is the
one that agrees best with the others; their outline decides only whether the
cut is the right sign at all. Nothing of their outline is kept.

A sign is ACCEPTED when its kept cut overlaps their outline at 0.40 or more
(intersection over union, both filled, same box). That line is a working
setting, not a tested bar; the sheet is the gate, and every sign is looked at.

    python3 ktcut.py            cut the words kttrace.py accepted
"""
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as nd

import kttrace as T
import ktpen

OUT = os.path.join(T.ROOT, "work", "rohonc", "ourGlyphs.json")
SHEET = os.path.join(T.OUTDIR, "glyphs.png")
KEEP_IOU = 0.40


def parts(code, sg):
    """Unit x-span of each sign in the word, as compose() lays it out."""
    gl = [(code[i:i + 3], sg[code[i:i + 3]]) for i in range(0, len(code), 3)]
    x, out = sum(g["w"] for _, g in gl), []
    for c, g in gl:
        x -= g["w"]
        out.append((c, x, x + g["b"][0], x + g["b"][2]))
    return out


def boxed(mask, n=48):
    ys, xs = np.nonzero(mask)
    if len(ys) == 0:
        return np.zeros((n, n), bool)
    m = mask[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    H, W = m.shape
    k = n / max(H, W)
    im = Image.fromarray(m.astype(np.uint8) * 255).resize((max(1, int(W * k)), max(1, int(H * k))), Image.BILINEAR)
    out = np.zeros((n, n), bool)
    a = np.array(im) > 127
    out[(n - a.shape[0]) // 2:(n - a.shape[0]) // 2 + a.shape[0], (n - a.shape[1]) // 2:(n - a.shape[1]) // 2 + a.shape[1]] = a
    return out


def iou(a, b):
    u = (a | b).sum()
    return float((a & b).sum() / u) if u else 0.0


def main():
    sg = json.load(open(T.SIGNS, encoding="utf-8"))["signs"]
    hits = json.load(open(os.path.join(T.OUTDIR, "hits.json")))
    words = json.load(open(T.OUT))["signs"]
    cache = {f: a for f, a in T.spreads()}
    cuts = {}
    for w, rec in words.items():
        if rec.get("status") != "ACCEPTED" or w not in hits:
            continue
        hl = T.dedupe([tuple(h) for h in hits[w]])[:T.TOPK]
        hl = [h for h in hl if h[6] == hl[0][6]]
        s = hl[0][6]
        ag = T.agreeing(T.crops(hl, cache))
        med = T.stack(ag[:5])
        mask, _ = T.centre_ink(med)
        B0 = T.compose(w, sg)["b"][0] if len(w) > 3 else sg[w]["b"][0]
        spans = [(c, x0, (u0 - B0) * s * T.UP + 5 * T.UP, (u1 - B0) * s * T.UP + 5 * T.UP)
                 for c, x0, u0, u1 in parts(w, sg)]
        lab, n = nd.label(mask)
        own = {c: np.zeros_like(mask) for c, *_ in spans}
        for i in range(1, n + 1):
            comp = lab == i
            ys, xs = np.nonzero(comp)
            cx = xs.mean()
            hit = [sp for sp in spans if sp[2] - 2 * T.UP <= cx <= sp[3] + 2 * T.UP]
            if len(hit) == 1 or not hit:
                sp = hit[0] if hit else min(spans, key=lambda sp: abs((sp[2] + sp[3]) / 2 - cx))
                own[sp[0]] |= comp
            else:
                # a stroke across two spans is split at the boundary between them
                for sp in hit:
                    m = comp.copy()
                    m[:, :int(max(0, sp[2] - T.UP))] = False
                    m[:, int(sp[3] + T.UP):] = False
                    own[sp[0]] |= m
        for c, xoff, c0, c1 in spans:
            if own[c].any():
                cuts.setdefault(c, []).append((w, own[c], s, xoff))
    # Every one of their signs, boxed, to ask whether a cut looks more like
    # ANOTHER sign than the one it was cut as. A rare sign with fine detail
    # (773, an O with dots, 11 times in the book) is otherwise "found" as the
    # common sign it resembles (a10, a plain O, 5,198 times).
    allk = {code: boxed(T.key(g, 0.1, ss=1) > 0.5) for code, g in sg.items()}
    done, rows = {"upm": 1000, "signs": {}}, []
    for c in sorted(cuts):
        k = T.key(sg[c], cuts[c][0][2] * T.UP, ss=1) > 0.5
        kb = boxed(k)
        cand = []
        for w, m, s, xoff in cuts[c]:
            b = boxed(m)
            peers = [iou(b, boxed(m2)) for w2, m2, *_ in cuts[c] if w2 != w]
            cand.append((np.mean(peers) if peers else 0.0, iou(b, kb), w, m, s, xoff))
        cand.sort(key=lambda t: (-t[0], -t[1]))
        peer, kt, w, m, s, xoff = cand[0]
        mb = boxed(m)
        rival, rv_iou = max(((o, iou(mb, kb2)) for o, kb2 in allk.items() if o != c), key=lambda t: t[1])
        own = iou(mb, allk[c])
        status = "ACCEPTED" if kt >= KEEP_IOU else "UNSURE"
        if rv_iou > own + 0.03:
            status = f"LOOKS LIKE {rival}"
        ys, xs = np.nonzero(m)
        pad = 2 * T.UP
        c0, c1 = max(0, xs.min() - pad), xs.max() + pad
        raw = m[:, c0:c1 + 1]
        sub = ktpen.pen(raw, k)                 # second pass: even pen stroke, their outline subtracts only
        d, shape = T.potrace_path(sub)
        # frame: the word's crop, shifted to this column and back into the sign's own units
        B0w = T.compose(w, sg)["b"][0] if len(w) > 3 else sg[w]["b"][0]
        frame = {"b": [B0w + c0 / (s * T.UP) - xoff, T.compose(w, sg)["b"][1] if len(w) > 3 else sg[w]["b"][1]]}
        path, b, adv = T.to_units(d, shape, {"b": [frame["b"][0], frame["b"][1]]}, s)
        done["signs"][c] = {"d": path, "w": adv, "b": b, "status": status, "from": w,
                            "kt_iou": round(kt, 2), "rival": rival, "rival_iou": round(rv_iou, 2), "own_iou": round(own, 2), "peer": round(peer, 2), "n": len(cuts[c])}
        rows.append((c, kb, [boxed(raw)], boxed(sub), status, kt, len(cuts[c])))
    rv = json.load(open(os.path.join(T.HERE if hasattr(T, "HERE") else os.path.dirname(__file__), "glyph_review.json")))
    for c, rec in done["signs"].items():
        rec["review"] = "ok" if c in rv["ok"] else ("no: " + rv["no"][c] if c in rv["no"] else "not looked at")
    json.dump(done, open(OUT, "w"), indent=0)
    cell = 56
    img = Image.new("L", (cell * 8 + 110, cell * len(rows) + 4), 255)
    dr = ImageDraw.Draw(img)
    for r, (c, kb, cs, keep, status, kt, n) in enumerate(rows):
        y = r * cell + 2
        dr.text((2, y + 2), c, fill=0)
        dr.text((2, y + 16), status, fill=0)
        dr.text((2, y + 30), f"kt {kt:.2f}  n{n}", fill=0)
        for j, t in enumerate([kb] + cs + [keep]):
            img.paste(Image.fromarray(np.where(t, 0, 255).astype(np.uint8)), (110 + j * cell + 4, y + 4))
        dr.line([(110 + cell - 2, y), (110 + cell - 2, y + cell)], fill=160)
    img.save(SHEET)
    acc = sum(1 for r in rows if r[4] == "ACCEPTED")
    print(f"ktcut: {len(rows)} signs from {len(set(x[0] for v in cuts.values() for x in v))} words, "
          f"{acc} accepted; sheet {SHEET}")


if __name__ == "__main__":
    sys.exit(main())
