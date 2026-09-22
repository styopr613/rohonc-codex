"""The translation: the manuscript told straight through, in English.

    python3 ktnarrate.py sample I       one part, printed, nothing written
    python3 ktnarrate.py run            every part -> translation.md
    python3 ktnarrate.py status

WHY THIS FILE EXISTS. Book One was written as an editorial retelling: an editor
discussing the manuscript, with the gloss quoted inside it. The owner's verdict,
2026-09-21: "the gloss is already there, why reproduce it in the narrative, we
just want a translation". He is right, and the duplication was the defect. There
are three renderings of this book and only one of them should read like a book:

    the gloss          every sign, marked          the evidence
    the folio English  one paragraph per folio     the literal layer, gloss-only
    THIS               continuous English prose    the translation

So: no commentary, no remarks about what is strange or missing, no quotation of
the gloss, no editor in the first person. The story the book tells, in order,
with the folio numbers in brackets so any sentence can be checked against the
gloss printed at the back.

WHAT IT IS WRITTEN FROM. The folio English, and nothing else. That layer was
itself written from the gloss alone -- no source passage, no chapter title, no
page image -- and every folio of it passed the leak gate in ktenglish.py. So
this pass cannot import the Vulgate, because it never sees the Vulgate: it sees
English that has already been checked, and its job is to make it continuous.

THE GATE, and its bar is declared here before the first run. It is the SAME
instrument as ktenglish.py, applied at paragraph scale: every content word of a
paragraph is stemmed and looked for in the gloss of the folios that paragraph
itself cites. ktenglish declared a refusal bar of three times the folio median,
**5.7%**, and that bar stands unchanged here. A paragraph above it is not noise,
it is a paragraph that has started telling the story from memory; it is refused,
its leaked words are quoted back at it, and it is written again. A paragraph
that fails twice is REPLACED by the folio English of its own folios, which is
plainer but has already been checked. No paragraph enters the book unchecked and
the bar is not moved.

Leaks are printed, counted and kept.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request

import corpus
import ktbook
import ktenglish as KE

OUT = os.path.join(corpus.ROOT, "work", "rohonc", "translation",
                   "translation.md")
BAR = 5.7          # per cent of content words unsupported; ktenglish's own bar
PER_CALL = 7       # folios handed over at once
MODEL = KE.MODEL
URL = KE.URL
KEY = KE.KEY

SYSTEM = """You are translating a sixteenth-century manuscript into English.

You will be given a LITERAL CRIB of the manuscript, folio by folio: English
words standing in the manuscript's own order, which is not English order. It is
a crib, not a translation, and it does not read. DO NOT COPY IT. Do not keep its
word order, do not keep its stutter, do not repeat a noun six times because the
crib does. Work out what each passage is saying and write that in ordinary
English, the way a translator writes: a subject, a verb, a sentence that
resolves. One account, running on, in the order the manuscript has it.

WHAT YOU MUST NOT DO, and this is the whole point of the job:

- Do not comment. Never say a leaf is strange, that a passage is unclear, that
  something is missing, that a scene comes from a tradition, or what this
  edition does or does not know. You are not an editor and you have no opinions.
- Do not quote. There are no quotation marks, no guillemets, no italics around
  manuscript words. Nothing is set off as a specimen.
- Do not explain. No asides, no glosses in brackets of your own, no "that is",
  no "in other words".
- Do not add. No noun, verb, name, event or clause that is not in the text you
  were given. You will recognise much of this material; write what is in front
  of you, never what you know the passage says.

WHAT YOU SHOULD DO:

- Join the literal sentences into readable English. Supply connectives, articles
  and tense. Order a sentence the way English orders one.
- Keep the manuscript's own sequence of events. Do not move an episode.
- Where the text is elliptical, write a short plain sentence and move on. Where
  it is broken, let it be broken. Silence is correct; invention is not.
- Keep a word in [square brackets] in brackets: it is a restoration.
- Keep a foreign word exactly as it stands.
- Write ... where the text has ... . Do not fill the gap.
- Paragraph as the sense goes, several folios to a paragraph where they run on.
- End every paragraph with the folios it draws on, in brackets, like this:
  (012r-013v) or (012r, 015v).

Return ONLY the prose. No heading, no preamble, no notes."""


def ask(body, caught=(), tries=3):
    if caught:
        body += ("\n\nYOUR LAST ATTEMPT FAILED THE CHECK. These words are in "
                 "what you wrote and in none of the text you were given:\n  "
                 + ", ".join(caught)
                 + "\n\nThat means you were completing the passage from "
                   "something you recognise. Write it again using only what is "
                   "in front of you. If that leaves it thin, leave it thin.")
    req = urllib.request.Request(
        URL,
        data=json.dumps({"model": MODEL,
                         "messages": [{"role": "system", "content": SYSTEM},
                                      {"role": "user", "content": body}],
                         "temperature": 0.3, "max_tokens": 2000}).encode(),
        headers={"Authorization": "Bearer " + KEY,
                 "Content-Type": "application/json"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                d = json.load(r)
            t = (d["choices"][0]["message"]["content"] or "").strip()
            if t:
                return t
        except Exception as e:
            if i == tries - 1:
                raise
        time.sleep(3 * (i + 1))
    raise RuntimeError("no prose back")


FOLIO_RE = re.compile(r"\((\d{3}[rv](?:\s*[-,–]\s*\d{3}[rv])*)\)\s*$")


def cited(par, order):
    """The folios a paragraph names. A range means every folio between, in the
    manuscript's own order, not in numeric order: this book's reading order is
    not its leaf order and 004v-003v is a real span."""
    m = FOLIO_RE.search(par.strip())
    if not m:
        return []
    out = []
    for bit in re.split(r"\s*,\s*", m.group(1)):
        ends = re.split(r"\s*[-–]\s*", bit)
        if len(ends) == 2 and ends[0] in order and ends[1] in order:
            a, b = order.index(ends[0]), order.index(ends[1])
            out.extend(order[min(a, b):max(a, b) + 1])
        else:
            out.extend(e for e in ends if e in order)
    return out


def parts():
    """Each part of the book: its name, and its folios in reading order."""
    fol = ktbook.folios()
    order = [pg for pg, _, _, _ in fol]
    eng = json.load(open(KE.OUT, encoding="utf-8"))
    gl = {pg: lines for pg, (_, lines) in KE.folios().items()}
    idx = {pg: i for i, (pg, _, _, _) in enumerate(fol)}
    bounds = sorted((idx.get(pg, 0), name, blurb) for pg, name, blurb in ktbook.PARTS)
    out = []
    for bi, (start, pname, pblurb) in enumerate(bounds):
        end = bounds[bi + 1][0] if bi + 1 < len(bounds) else len(fol)
        pages = [pg for pg, _, _, _ in fol[start:end]]
        out.append({"name": pname, "blurb": pblurb, "pages": pages,
                    "eng": eng, "gloss": gl, "order": order})
    return out


def chunk_body(pages, eng):
    lines = []
    for pg in pages:
        t = (eng.get(pg) or {}).get("english", "").strip()
        if t:
            lines.append(f"[{pg}]\n{t}")
    return "\n\n".join(lines)


def score(par, order, gloss):
    """Leak rate of one paragraph against the gloss of the folios it cites."""
    pgs = cited(par, order)
    if not pgs:
        return None, [], []
    have = []
    for pg in pgs:
        have.extend(gloss.get(pg, []))
    body = FOLIO_RE.sub("", par.strip())
    bad = KE.leaks(body, have)
    words = max(1, len(KE.stems(body)))
    return 100.0 * len(bad) / words, bad, pgs


def do_chunk(pages, p, log):
    body = chunk_body(pages, p["eng"])
    if not body.strip():
        return []
    caught = ()
    for attempt in (1, 2):
        text = ask(body, caught)
        pars = [x.strip() for x in text.split("\n\n") if x.strip()]
        worst, bad_all = 0.0, []
        for par in pars:
            rate, bad, pgs = score(par, p["order"], p["gloss"])
            if rate is None:
                # no citation: check it against the whole chunk instead
                have = [l for pg in pages for l in p["gloss"].get(pg, [])]
                bad = KE.leaks(par, have)
                rate = 100.0 * len(bad) / max(1, len(KE.stems(par)))
            if rate > worst:
                worst = rate
            bad_all.extend(bad)
        log.append({"pages": pages, "attempt": attempt, "worst": round(worst, 2),
                    "leaks": sorted(set(bad_all))})
        if worst <= BAR:
            return pars
        caught = sorted(set(bad_all))[:24]
    # twice over the bar: the literal layer stands instead. It is plainer and
    # it has already been checked.
    log[-1]["refused"] = True
    keep = [(p["eng"].get(pg) or {}).get("english", "").strip() for pg in pages]
    return [" ".join(x for x in keep if x) + f" ({pages[0]}-{pages[-1]})"]


def run(only=None, out=OUT):
    ps = parts()
    log, blocks = [], []
    for p in ps:
        num = p["name"].split(".", 1)[0].strip()
        if only and num != only:
            continue
        pars = []
        for i in range(0, len(p["pages"]), PER_CALL):
            got = do_chunk(p["pages"][i:i + PER_CALL], p, log)
            pars.extend(got)
            print(f"  {p['name'][:40]:42} {i + 1:>3}/{len(p['pages'])} "
                  f"worst {log[-1]['worst']:>5}%{' REFUSED' if log[-1].get('refused') else ''}",
                  flush=True)
        blocks.append((p["name"], p["pages"], pars))
    md = ["# The Rohonc Codex", "",
          "The manuscript in English, told straight through. The gloss every "
          "sentence was made from is printed folio by folio at the back.", ""]
    for name, pages, pars in blocks:
        md.append(f"## {name}")
        md.append("")
        md.append(f"### folios {pages[0]}–{pages[-1]}")
        md.append("")
        md.extend(x + "\n" for x in pars)
    text = "\n".join(md)
    if out:
        open(out, "w", encoding="utf-8").write(text)
        print("wrote", out)
    worst = max([l["worst"] for l in log], default=0)
    ref = sum(1 for l in log if l.get("refused"))
    print(f"chunks {len(log)}   worst paragraph {worst}%   bar {BAR}%   "
          f"refused {ref}")
    json.dump(log, open(os.path.join(corpus.ROOT, "work", "rohonc",
                                     "ktnarrate_log.json"), "w"), indent=1)
    return text


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["sample", "run", "status"])
    ap.add_argument("part", nargs="?")
    a = ap.parse_args(argv)
    if a.cmd == "status":
        print(OUT, os.path.getsize(OUT) if os.path.isfile(OUT) else "not written")
        return 0
    if a.cmd == "sample":
        print(run(only=a.part or "I", out=None))
        return 0
    run()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
