"""Timm & Schinner's self-citation generator (Cryptologia 2019/2020).

The scribe copies a word he has recently written and mutates it by a glyph or
two. Run from the authors' own executable jar, not a reimplementation, so the
row is their process rather than our reading of it.

Its configuration switches are swept and the best is kept, the same courtesy
the fingerprint repo extends it, so the comparison is not against a straw man.
The sweep is scored on TRAIN.
"""
import os
import re
import subprocess
import sys

import corpus
import layout
from . import register

FPROOT = os.path.join(corpus.ROOT, "refs", "voynich-fingerprint")
JAR = os.path.join(FPROOT, "tools", "scitext", "executable", "text-generator.jar")
CONF = os.path.join(FPROOT, "tools", "scitext", "executable", "conf.properties")
TMP = os.path.join(corpus.ROOT, "work", "scitext")


def run_jar(n_lines, over=None):
    os.makedirs(os.path.join(TMP, "generate"), exist_ok=True)
    conf = open(CONF, encoding="utf-8").read()
    for k, v in (over or {}).items():
        conf = re.sub(rf"(?m)^{re.escape(k)}=.*$", f"{k}={v}", conf)
    conf = re.sub(r"text\.lines_to_create=\d+", f"text.lines_to_create={n_lines}", conf)
    open(os.path.join(TMP, "conf.properties"), "w", encoding="utf-8").write(conf)
    subprocess.run(["java", "-jar", JAR], cwd=TMP, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    out = []
    for ln in open(os.path.join(TMP, "generate", "generated_text.txt"),
                   encoding="utf-8", errors="replace"):
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        ws = [w.strip("-") for w in ln.split() if w.strip("-")]
        ws = [w for w in ws if not re.search(r"[?!]", w)]
        if ws:
            out.append(ws)
    return out


@register("selfcite", kind="lines", label="self-citation (Timm & Schinner)",
          note="their own jar; switches swept on TRAIN, best kept")
def generate(spec, train, seed=0, cfg=None):
    n_lines = sum(p.n_lines for p in spec)
    over = dict(cfg or {})
    over.setdefault("method.random.pseudo.seed", 19 + seed)
    lines = run_jar(n_lines, over)
    return layout.group_lines(lines, spec), {
        "executable": "text-generator.jar", "switches": cfg or "default",
        "cite": "Timm & Schinner (2019/2020), Cryptologia 44(1)"}
