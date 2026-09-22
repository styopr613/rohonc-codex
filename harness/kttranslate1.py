"""Translate: the gloss in, readable English out. Part by part.

    python3 kttranslate1.py I            print Part I
    python3 kttranslate1.py all          write work/rohonc/translation/translation.md

The translator is given the folio's gloss lines and a glossary of the formulas
and particles, and is told to translate: subjects, verbs, sentences, consistent
renderings. Restorations stay in brackets. Gaps stay as ... . Nothing else is
held back. The folio number closes every paragraph so the gloss at the back can
be checked against it.
"""
import json, os, re, sys, time, urllib.request
import corpus, ktbook, ktenglish as KE

OUT = os.path.join(corpus.ROOT, "work", "rohonc", "translation", "translation.md")
PER_CALL = 6

GLOSSARY = """
exist / then-exist        the copula: is, was, there is, there was; "and then there was"
and_then, in_turn         and then; next / in turn (a list particle)
somebody, man^            a man, a person, someone
this-Lord, to-Lord        the Lord (this is the manuscript's way of pointing)
Lord-<suffix_of_divine_name>, from-father-<suffix_of_divine_name>
                          the Lord God; God the Father
<preposition_of_genitive>-X    of X
<subject_marker>, ^, ~, *  grammar and apparatus marks: do not print them
X-+name                   a proper name the sign carries (e.g. brother-+name = a brother by name)
hide_oneself-angel        Lucifer, the angel who hides himself (render it as Lucifer after first mention)
one-on-sky                heaven
heart                     a sign the dictionary glosses "heart"; in "heart one-on-sky and earth"
                          it is the making of heaven and earth; in "before heart of somebody" it is
                          before the making of man; in "heart breathe on Adam" it is the breath of life
grab                      take; carry = bring; write = write down / set down
each,_every               every, all
chapter-oh                a rubric: "Chapter." Print it as a heading line.
ten-ten-ten-ten           forty; six-six twelve; two-half-hundred-year seven = two hundred and fifty-seven years
|                         a gap in the manuscript: write ...
[word]                    a restored word: keep the brackets
Jew(ish)                  the Jews
holy-gospel               the holy gospel
"""

SYSTEM = """You are translating a sixteenth-century manuscript into readable English.

You are given its text folio by folio as a word-for-word gloss in the manuscript's own
order, and a glossary of its formulas and particles. TRANSLATE IT. Write English sentences
a reader can follow: subjects, verbs, tenses, articles, pronouns, connectives. Resolve the
formulas the way the glossary says and render each one the same way every time. Keep the
manuscript's order of events and its content; do not add an event, a name or a clause the
gloss does not carry, and do not smooth a genuine gap into sense: where the gloss has |
write ... and move on. Where a passage repeats a formula many times, translate it as the
repetition it is, in plain words. Keep restored words in [brackets]. Do not comment, do not
explain, do not quote the gloss, do not add notes. End every paragraph with the folio(s) it
renders in brackets, like (004v) or (004v-004r).

Return only the translation.""" + "\n\nGLOSSARY\n" + GLOSSARY

def ask(body):
    req = urllib.request.Request(KE.URL, data=json.dumps({"model": KE.MODEL,
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": body}],
        "temperature": 0.3, "max_tokens": 2400}).encode(),
        headers={"Authorization": "Bearer " + KE.KEY, "Content-Type": "application/json"})
    for i in range(3):
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                t = (json.load(r)["choices"][0]["message"]["content"] or "").strip()
            if t: return t
        except Exception:
            if i == 2: raise
        time.sleep(3)

PROOF = """You are the copy editor of a translation of a sixteenth-century manuscript. You are given
a draft translation, paragraph by paragraph, each paragraph ending with the folio number it
renders in brackets. Make it read as clear, natural English prose that a reader can follow
without help.

Do: fix fragments into sentences; give each sentence a subject and a verb; drop stray labels
and line numbers that leaked in (such as a folio number on its own line); merge choppy runs;
keep every paragraph's closing folio citation exactly as it is, and keep it at the end.
Keep words in [brackets] in brackets. Keep ... where the draft has ... . Keep the order of
events. Render a repeated name or formula the same way every time.

Do not: add an event, a person, a place, a speech or a detail that is not in the draft; do not
explain; do not comment; do not add notes or headings; do not remove a folio citation.

Return only the edited prose, paragraphs separated by blank lines."""


def proof(pars):
    out = []
    for i in range(0, len(pars), 8):
        body = "\n\n".join(pars[i:i+8])
        req = urllib.request.Request(KE.URL, data=json.dumps({"model": KE.MODEL,
            "messages": [{"role": "system", "content": PROOF}, {"role": "user", "content": body}],
            "temperature": 0.2, "max_tokens": 3000}).encode(),
            headers={"Authorization": "Bearer " + KE.KEY, "Content-Type": "application/json"})
        t = ""
        for k in range(3):
            try:
                with urllib.request.urlopen(req, timeout=240) as r:
                    t = (json.load(r)["choices"][0]["message"]["content"] or "").strip()
                if t: break
            except Exception:
                if k == 2: raise
            time.sleep(3)
        out.extend(x.strip() for x in t.split("\n\n") if x.strip())
    return out


EDIT = """You are the final editor of a translation of a sixteenth-century manuscript, and this
pass is a check against the original. You are given one paragraph of the translation and,
under it, the ORIGINAL it was made from: the manuscript's own text as a word-for-word
gloss, line by line, for exactly the folios that paragraph renders. Compare them.

Correct the paragraph wherever it departs from the original: something added that the
gloss does not carry, something the gloss carries that was dropped, an event out of order,
a name or a number changed, a formula rendered differently from elsewhere. Keep the
paragraph readable English while you do it: this is a translation for people to read, not
a gloss. Keep [bracketed] restorations in brackets and ... for a gap. Keep the closing
folio citation exactly as it stands. Do not add comments or notes.

Return only the corrected paragraph."""

CITE = re.compile(r"\((\d{3}[rv](?:\s*[-–,]\s*\d{3}[rv])*)\)\s*$")


def cited(par, order):
    m = CITE.search(par.strip())
    if not m: return []
    out = []
    for bit in re.split(r"\s*,\s*", m.group(1)):
        ends = re.split(r"\s*[-–]\s*", bit)
        if len(ends) == 2 and ends[0] in order and ends[1] in order:
            a, b = order.index(ends[0]), order.index(ends[1])
            out.extend(order[min(a, b):max(a, b) + 1])
        else:
            out.extend(e for e in ends if e in order)
    return out


def call(system, body, max_tokens=2400, temperature=0.2):
    req = urllib.request.Request(KE.URL, data=json.dumps({"model": KE.MODEL,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": body}],
        "temperature": temperature, "max_tokens": max_tokens}).encode(),
        headers={"Authorization": "Bearer " + KE.KEY, "Content-Type": "application/json"})
    for k in range(3):
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                t = (json.load(r)["choices"][0]["message"]["content"] or "").strip()
            if t: return t
        except Exception:
            if k == 2: raise
        time.sleep(3)
    return ""


EDIT_MODEL = "deepseek/deepseek-v4-pro-0813"          # DeepSeek through OpenRouter
EDIT_EXTRA = {"reasoning": {"enabled": False}}
EDIT_FOLIOS = 8                                         # folios of gloss per call


def edit_all():
    """The final editorial: the translation checked back against the original,
    a run of paragraphs at a time with all their gloss, through OpenRouter."""
    import shutil, concurrent.futures as cf
    import ktor
    fol = ktbook.folios()
    order = [pg for pg, _, _, _ in fol]
    gl = {pg: lines for pg, (_, lines) in KE.folios().items()}
    text = open(OUT, encoding="utf-8").read()
    shutil.copyfile(OUT, OUT + ".pre-edit-" + time.strftime("%Y%m%d-%H%M"))
    blocks = text.split("\n\n")
    # group consecutive paragraphs until they cover about EDIT_FOLIOS folios
    groups, cur, cur_pgs = [], [], []
    for i, par in enumerate(blocks):
        pgs = cited(par, order)
        if not pgs or par.startswith("#"):
            if cur: groups.append((cur, cur_pgs)); cur, cur_pgs = [], []
            continue
        cur.append(i); cur_pgs.extend(x for x in pgs if x not in cur_pgs)
        if len(cur_pgs) >= EDIT_FOLIOS:
            groups.append((cur, cur_pgs)); cur, cur_pgs = [], []
    if cur: groups.append((cur, cur_pgs))

    def job(idxs, pgs):
        tr = "\n\n".join(blocks[k].strip() for k in idxs)
        orig = "\n\n".join("[%s]\n%s" % (pg, "\n".join("%2d  %s" % (j+1, l) for j, l in enumerate(gl.get(pg, []))))
                            for pg in pgs if gl.get(pg))
        body = ("TRANSLATION (%d paragraphs; return the same number, in order, separated by blank lines)\n"
                % len(idxs)) + tr + "\n\nORIGINAL\n" + orig
        reply, usage = ktor.ask(EDIT_MODEL, EDIT.replace("one paragraph", "a run of paragraphs")
                                .replace("that paragraph renders", "those paragraphs render")
                                .replace("Return only the corrected paragraph.",
                                         "Return only the corrected paragraphs, the same number as given, in the same order, separated by blank lines."),
                                temperature=0.2, extra=EDIT_EXTRA)
        outs = [x.strip() for x in reply.split("\n\n") if x.strip()]
        return idxs, outs, usage

    done, cost = 0, 0.0
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(job, idxs, pgs) for idxs, pgs in groups]
        for f in cf.as_completed(futs):
            try:
                idxs, outs, usage = f.result()
            except Exception as e:
                print("  edit failed:", str(e)[:100], file=sys.stderr); continue
            cost += float((usage or {}).get("cost") or 0)
            # accept only a reply with one paragraph per input, each still cited
            if len(outs) == len(idxs) and all(CITE.search(o) for o in outs):
                for k, o in zip(idxs, outs):
                    blocks[k] = o
                done += 1
            else:
                print(f"  kept as was: {len(outs)} back for {len(idxs)}", file=sys.stderr)
            if done % 10 == 0:
                print(f"  edited {done}/{len(groups)} groups  ${cost:.2f}", file=sys.stderr, flush=True)
                open(OUT, "w", encoding="utf-8").write("\n\n".join(blocks))
    open(OUT, "w", encoding="utf-8").write("\n\n".join(blocks))
    print(f"edited {done} of {len(groups)} groups, ${cost:.2f} ->", OUT)


def parts():
    fol = ktbook.folios()
    gl = {pg: lines for pg, (_, lines) in KE.folios().items()}
    idx = {pg: i for i, (pg, _, _, _) in enumerate(fol)}
    bounds = sorted((idx.get(pg, 0), n, b) for pg, n, b in ktbook.PARTS)
    out = []
    for bi, (start, name, _) in enumerate(bounds):
        end = bounds[bi+1][0] if bi+1 < len(bounds) else len(fol)
        out.append((name, [pg for pg, _, _, _ in fol[start:end]], gl))
    return out

def body_for(pages, gl):
    return "\n\n".join("[%s]\n%s" % (pg, "\n".join("%2d  %s" % (i+1, l) for i, l in enumerate(gl.get(pg, []))))
                       for pg in pages if gl.get(pg))

def translate(name, pages, gl, say=print):
    pars = []
    for i in range(0, len(pages), PER_CALL):
        chunk = pages[i:i+PER_CALL]
        t = ask(body_for(chunk, gl))
        pars.extend(x.strip() for x in t.split("\n\n") if x.strip())
        say(f"  {name[:36]:38} {min(i+PER_CALL, len(pages)):>3}/{len(pages)}")
    return pars

def main(argv):
    want = argv[0] if argv else "I"
    if want == "edit":
        edit_all(); return
    ps = parts()
    md = ["# The Rohonc Codex", "", "A translation. The gloss it was made from is printed folio by folio at the back.", ""]
    for name, pages, gl in ps:
        num = name.split(".", 1)[0].strip()
        if want != "all" and num != want: continue
        pars = translate(name, pages, gl, say=lambda s: print(s, file=sys.stderr))
        pars = proof(pars)
        print(f"  {name[:36]:38} proofed", file=sys.stderr)
        md += [f"## {name}", "", f"### folios {pages[0]}–{pages[-1]}", ""] + [p + "\n" for p in pars]
    text = "\n".join(md)
    if want == "all":
        open(OUT, "w", encoding="utf-8").write(text); print("wrote", OUT)
    else:
        print(text)

if __name__ == "__main__":
    main(sys.argv[1:])
