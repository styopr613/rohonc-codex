"""ktsite.py -- build the public page oona13.com/rohonc/ from the project's own files.

    /opt/publish-app/venv/bin/python ktsite.py            # writes /var/www/oona13/rohonc
    /opt/publish-app/venv/bin/python ktsite.py --out DIR  # anywhere else

(The publish venv is used only because it has python-markdown; nothing else
from the studio is touched.)

What goes up, and the rule for each:

  the documents      TESTS.md, METHOD.md, ROHONC.md, DATA_PROVENANCE.md,
                     FINALPASS.md, BLINDFOLD.md, DARK.md -- rendered as they
                     are, no edits, so the page can never say something the
                     repository does not.
  the dictionary     harness/proposals.json -- this project's readings, every
                     tier, withdrawn ones included, with the evidence line.
  the reading        the English written for each folio from its gloss
                     (work/rohonc/translation/english.json), in Kiraly and
                     Tokai's page order, taken from the reader's edition.
  the saved runs     every work/rohonc/*.txt, and the outside readers' replies.
  the figures        parsed from the edition header and TESTS.md, never typed.

What does NOT go up, by the position settled in DATA_PROVENANCE.md: Kiraly and
Tokai's dictionary, their transcription, their pages, and the scans. They are
credited by name and linked, not rehosted. Their translation is unpublished
and nothing here is it.
"""
import argparse
import html
import json
import os
import re
import shutil
import sys

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The prose of the site is written by an outside model from a fact sheet
# (ktsitecopy.py) and read back by a person; this file only places it.
COPY = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ktsite_copy.json"), encoding="utf-8"))


def paras(key, cls=""):
    """A copy piece as <p> paragraphs."""
    c = f' class="{cls}"' if cls else ""
    return "".join(f"<p{c}>{html.escape(t.strip())}</p>" for t in COPY[key].split("\n\n") if t.strip())
WORK = os.path.join(ROOT, "work", "rohonc")
TR = os.path.join(WORK, "translation")
OUT_DEFAULT = "/var/www/oona13/rohonc"
BG = "#0B0D10"   # the family's dark ground; the page is a sheet laid on it
V = "20260921"

DOCS = [
    # (slug, file, nav label, page title, one line for the data index)
    ("tests", "TESTS.md", "Tests", "Tests",
     "whether the added readings are true: nine tests, then the outside review's six"),
    ("method", "METHOD.md", "Method", "Method",
     "the loop that reads an unread sign, and the standing orders for whoever runs it"),
    ("writeup", "ROHONC.md", "Write-up", "The write-up",
     "the full account: the line-break result, the dictionary, seventeen extension attempts, what the book says"),
    ("provenance", "DATA_PROVENANCE.md", "Sources", "Sources and what is owed",
     "where every file came from and what may be done with it"),
    ("finalpass", "FINALPASS.md", None, "The final pass",
     "the vocabulary checked before the guesses"),
    ("blindfold", "BLINDFOLD.md", None, "The blindfold test",
     "the one check the project cannot run on itself"),
    ("dark", "DARK.md", None, "The dark words",
     "the last 3.6% of the book, and what reading them taught"),
]

NAV = [("index", "Overview"), ("reading", "The reading"), ("dictionary", "Dictionary"),
       ("tests", "Tests"), ("method", "Method"), ("writeup", "Write-up"),
       ("data", "Data")]

CREDIT = html.escape(COPY["credit_line"].strip())

CSS = """
:root{--bg:#0B0D10;--ink:#1d1a16;--soft:#5a5248;--paper:#f5efe3;--paper2:#ece5d5;--rub:#7a2418;--ivory:#e9e2d3;--line:#d9cfb9}
body{margin:0;background:var(--bg);color:var(--ivory);font-family:"EB Garamond",Garamond,"Times New Roman",serif;font-size:19px;line-height:1.55}
header.rh{padding:34px 20px 8px;text-align:center}
header.rh .mark{font-family:Cinzel,"Times New Roman",serif;font-size:30px;letter-spacing:.12em;color:var(--ivory);text-decoration:none;text-transform:uppercase}
header.rh .tag{margin:8px 0 0;color:#b7ad9b;font-style:italic;font-size:18px}
nav.sub{margin:20px 0 0;font-size:14px;letter-spacing:.09em;text-transform:uppercase}
nav.sub a{color:#bdb3a1;text-decoration:none;margin:0 10px;padding-bottom:3px;display:inline-block}
nav.sub a:hover{color:#e6c979}
nav.sub a.here{color:#e6c979;border-bottom:1px solid #e6c979}
main.sheet{max-width:860px;margin:26px auto 60px;background:var(--paper);color:var(--ink);padding:52px 64px 60px;border-radius:3px;box-shadow:0 12px 40px rgba(0,0,0,.55)}
.prose h1,.prose h2,.prose h3,.prose h4{font-family:Cinzel,"Times New Roman",serif;font-weight:400;color:var(--rub);line-height:1.2;letter-spacing:.03em}
.prose h1{font-size:30px;margin:0 0 .6em}
.prose h2{font-size:22px;margin:1.8em 0 .5em}
.prose h3{font-size:18px;margin:1.5em 0 .4em}
.prose h4{font-size:17px;margin:1.3em 0 .3em;color:var(--ink)}
.prose p{margin:0 0 1em}
.prose a{color:var(--rub)}
.prose pre{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13.5px;line-height:1.45;background:var(--paper2);padding:14px 16px;border-radius:3px;overflow-x:auto;white-space:pre}
.prose code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.85em;background:var(--paper2);padding:1px 4px;border-radius:2px}
.prose pre code{background:none;padding:0;font-size:inherit}
.prose blockquote{margin:1em 0;padding:0 0 0 18px;border-left:3px solid var(--line);color:var(--soft)}
.prose table{border-collapse:collapse;font-size:16px;margin:1em 0}
.prose th,.prose td{border-bottom:1px solid var(--line);padding:5px 10px;text-align:left;vertical-align:top}
.prose .tw{overflow-x:auto}
.prose hr{border:0;border-top:1px solid var(--line);margin:2em 0}
.prose ul,.prose ol{padding-left:1.4em}
.prose li{margin:.25em 0}
.prose img{max-width:100%}
.lead{font-size:21px}
.fig{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:14px;line-height:1.5;background:var(--paper2);padding:14px 18px;border-radius:3px;margin:1em 0;white-space:pre;overflow-x:auto}
.credit{border-top:1px solid var(--line);margin-top:2.5em;padding-top:1em;color:var(--soft);font-size:16.5px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;margin:1.2em 0}
.card{display:block;background:var(--paper2);padding:14px 16px;border-radius:3px;text-decoration:none;color:var(--ink)}
.card b{display:block;font-family:Cinzel,serif;font-weight:400;font-size:15px;letter-spacing:.06em;color:var(--rub);margin-bottom:4px}
.card span{font-size:16px;color:var(--soft)}
/* the reading */
.folio{margin:0 0 1.6em}
.folio h2{margin:1.4em 0 .3em}
.folio h2 small{font-family:"EB Garamond",serif;font-size:17px;color:var(--soft);letter-spacing:0;margin-left:10px;text-transform:none}
.folio p{text-indent:0}
.nof{color:var(--soft);font-style:italic}
/* the dictionary */
.tools{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:1em 0 1.2em}
.tools input{font:inherit;font-size:17px;padding:6px 10px;border:1px solid var(--line);border-radius:3px;background:#fffdf8;color:var(--ink);min-width:240px}
.tools button{font:inherit;font-size:14px;letter-spacing:.06em;text-transform:uppercase;padding:6px 10px;border:1px solid var(--line);border-radius:3px;background:var(--paper2);color:var(--ink);cursor:pointer}
.tools button.on{background:var(--rub);color:#fff;border-color:var(--rub)}
.tools .n{color:var(--soft);font-size:16px;margin-left:auto}
table.dict{width:100%;font-size:16.5px}
table.dict td.code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;white-space:nowrap;color:var(--soft)}
table.dict td.tier{font-family:Cinzel,serif;font-size:13px;letter-spacing:.06em;white-space:nowrap}
table.dict td.ev{font-size:15px;color:var(--soft)}
table.dict td.ev .more{cursor:pointer;color:var(--rub)}
table.dict td.ev .full{display:none}
table.dict tr.open td.ev .full{display:inline}
table.dict tr.open td.ev .short,table.dict tr.open td.ev .more{display:none}
.tiers{font-size:16.5px;background:var(--paper2);padding:12px 16px;border-radius:3px}
.tiers b{font-family:Cinzel,serif;font-weight:400;color:var(--rub)}
@media(max-width:700px){body{font-size:17.5px}main.sheet{margin:14px 10px 40px;padding:26px 20px 34px}header.rh .mark{font-size:22px}nav.sub a{margin:0 6px 6px}.prose h1{font-size:24px}.tools .n{margin-left:0}}
"""


def shell(slug, title, desc, body, extra_head=""):
    nav = "".join(
        f'<a href="/rohonc/{"" if s == "index" else s + ".html"}"'
        f'{" class=here" if s == slug else ""}>{html.escape(lab)}</a>'
        for s, lab in NAV)
    t = html.escape(title)
    d = html.escape(desc)
    url = "https://oona13.com/rohonc/" + ("" if slug == "index" else slug + ".html")
    return f"""<!doctype html><html lang="en"><head>
<style>html{{background:{BG}}}</style>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="https://oona13.com/fam/fam.css?v=20260909b">
<title>{t} · The Rohonc Codex · OONA 13</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{t} · The Rohonc Codex"><meta property="og:description" content="{d}">
<meta property="og:type" content="article"><meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Cinzel:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style>{extra_head}
</head><body>
<script src="https://oona13.com/fam/fam.js?v={V}"></script>
<header class="rh"><div class="wrap">
  <a class="mark" href="/rohonc/">The Rohonc Codex</a>
  <p class="tag">{html.escape(COPY["tagline"].strip())}</p>
  <nav class="sub">{nav}</nav>
</div></header>
<main class="sheet"><article class="prose">
{body}
<p class="credit">{CREDIT}</p>
</article></main>
<script src="https://oona13.com/fam/foot.js" data-note="{html.escape(re.sub('<[^>]+>', '', CREDIT))}" defer></script>
</body></html>
"""


def md(text):
    out = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    # a wide table must scroll inside its own box, never the page
    return out.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")


def read(p):
    return open(p, encoding="utf-8").read()


# ---- the figures: read out of the files, never typed ---------------------------------

def edition_figures():
    txt = read(os.path.join(TR, "rohonc_readers_edition.md"))
    g = {}
    for key, pat in (
            ("words", r"words in the manuscript\s+([\d,]+)"),
            ("read", r"\n    read\s+([\d,]+) \(([\d.]+)%\)"),
            ("soft", r"read from one passage, marked \*\s+([\d,]+) \(([\d.]+)%\)"),
            ("rest", r"restored, in brackets\s+([\d,]+) \(([\d.]+)%\)"),
            ("dark", r"dark, printed as an ellipsis\s+([\d,]+) \(([\d.]+)%\)"),
            ("lread", r"lines with every word read\s+([\d,]+) of ([\d,]+) \(([\d.]+)%\)"),
            ("lall", r"restorations\s+([\d,]+) of ([\d,]+) \(([\d.]+)%\)")):
        m = re.search(pat, txt)
        if not m:
            raise SystemExit(f"ktsite: no {key} in the edition header")
        g[key] = m.groups()
    return g


def tests_summary():
    txt = read(os.path.join(ROOT, "TESTS.md"))
    m = re.search(r"\n## Summary\n\n((?:    .*\n|\n)+?)\n(?=[^\s])", txt)
    if not m:
        raise SystemExit("ktsite: no Summary block in TESTS.md")
    block = "\n".join(l[4:] if l.startswith("    ") else l for l in m.group(1).rstrip("\n").split("\n"))
    kt = re.search(r"dictionary of (\d+) signs", txt)
    return block, (kt.group(1) if kt else "?")


def new_here():
    txt = read(os.path.join(ROOT, "ROHONC.md"))
    m = re.search(r"\*\*What is new here and what is not\.\*\*(.*?)\n\n", txt, re.S)
    if not m:
        raise SystemExit("ktsite: ROHONC.md lost its 'what is new here' paragraph")
    return " ".join(m.group(1).split())


def proposals():
    p = json.load(open(os.path.join(ROOT, "harness", "proposals.json"), encoding="utf-8"))
    about = p.get("_about", "")
    rows = []
    for code, v in p.items():
        if not isinstance(v, dict):
            continue
        c = code
        if c.startswith("_withdrawn_"):
            c = c[len("_withdrawn_"):]
        rows.append({"code": c, "gloss": v.get("gloss", ""), "tier": v.get("tier", ""),
                     "n": v.get("n", 0), "evidence": v.get("evidence", "")})
    return about, rows


def folio_order():
    """Kiraly and Tokai's page order and this edition's folio titles, from the
    reader's edition headings."""
    out = []
    for m in re.finditer(r"^## (\d{3}[rv]) — (.*)$", read(os.path.join(TR, "rohonc_readers_edition.md")), re.M):
        out.append((m.group(1), m.group(2).strip()))
    return out


# ---- pages ------------------------------------------------------------------------

def page_index(fig, summary, ktn, newpara, tiers, nfolio):
    tier_line = "   ".join(f"{t} {tiers.get(t, 0):,}" for t in ("A", "B", "C", "D", "G"))
    body = f"""
<h1>What this is</h1>
{paras("intro", "lead")}

<h2>How far it reads</h2>
{paras("how_far")}
<div class="fig">words in the manuscript        {fig['words'][0]:>7}
read                           {fig['read'][0]:>7}   {fig['read'][1]}%
read from one passage only     {fig['soft'][0]:>7}   {fig['soft'][1]}%
restored, in brackets          {fig['rest'][0]:>7}   {fig['rest'][1]}%
dark                           {fig['dark'][0]:>7}   {fig['dark'][1]}%

lines with every word read     {fig['lread'][0]:>7} of {fig['lread'][1]}   {fig['lread'][2]}%
lines complete with brackets   {fig['lall'][0]:>7} of {fig['lall'][1]}   {fig['lall'][2]}%</div>
<p>This project's own readings, in its <a href="/rohonc/dictionary.html">dictionary</a>, by tier:</p>
<div class="fig">{tier_line}</div>
{paras("tiers")}

<h2>What is new here and what is not</h2>
{paras("new_here_lead")}
{md(newpara)}

<h2>Is it true?</h2>
{paras("is_it_true")}
<div class="fig">{html.escape(summary)}</div>
<p>The write-ups are on the <a href="/rohonc/tests.html">tests page</a>. The saved runs are in the <a href="/rohonc/data.html">data</a>.</p>

<h2>What is here</h2>
<div class="cards">
<a class="card" href="/rohonc/reading.html"><b>The reading</b><span>{html.escape(COPY["card_reading"].strip())}</span></a>
<a class="card" href="/rohonc/dictionary.html"><b>Dictionary</b><span>{html.escape(COPY["card_dictionary"].strip())}</span></a>
<a class="card" href="/rohonc/tests.html"><b>Tests</b><span>{html.escape(COPY["card_tests"].strip())}</span></a>
<a class="card" href="/rohonc/method.html"><b>Method</b><span>{html.escape(COPY["card_method"].strip())}</span></a>
<a class="card" href="/rohonc/writeup.html"><b>Write-up</b><span>{html.escape(COPY["card_writeup"].strip())}</span></a>
<a class="card" href="/rohonc/data.html"><b>Data</b><span>{html.escape(COPY["card_data"].strip())}</span></a>
</div>

<h2>The edition</h2>
{paras("edition")}

<h2>Credit and position</h2>
{paras("credit")}
<p>Their site: <a href="https://rechnitzer-kodex.hu/" rel="noopener">rechnitzer-kodex.hu</a>. Citations owed and the terms of every source are under <a href="/rohonc/provenance.html">Sources</a>.</p>
"""
    return shell("index", "Overview",
                 "The Rohonc Codex read into English on Király and Tokai's dictionary, extended and tested: the reading, the dictionary, fifteen tests, the method and all the data.",
                 body)


def page_reading(order, eng):
    parts = ['<h1>The reading, folio by folio</h1>',
             paras("reading_lead", "lead"),
             '<p>A word in brackets is a restoration. The line-by-line gloss each paragraph rests on is in the <a href="/rohonc/data.html">rendering</a>.</p>']
    n = 0
    for fol, title in order:
        e = eng.get(fol, {}).get("english", "").strip()
        parts.append(f'<div class="folio" id="f{fol}"><h2>{fol}<small>{html.escape(title)}</small></h2>')
        if e:
            parts.append(f"<p>{html.escape(e)}</p></div>")
            n += 1
        else:
            parts.append('<p class="nof">No English was written for this folio: the gloss carries too little to say anything true.</p></div>')
    return shell("reading", "The reading",
                 f"The Rohonc Codex in English, one paragraph per folio for all {len(order)} folios, written from the gloss alone.",
                 "\n".join(parts)), n


def page_dictionary(about, rows, ktn):
    tiers = {}
    for r in rows:
        tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1
    counts = "   ".join(f"{t} {tiers.get(t, 0):,}" for t in ("A", "B", "C", "D", "G", "withdrawn"))
    body = f"""
<h1>The dictionary of added readings</h1>
{paras("dictionary_lead", "lead")}
<p>The drawn signs are on <a href="https://rechnitzer-kodex.hu/" rel="noopener">their site</a>. From the file itself: {html.escape(about)}</p>
<div class="tiers"><b>A</b> fits every occurrence checked, or is proved by an identical formula or a numeral &nbsp;·&nbsp; <b>B</b> fits most &nbsp;·&nbsp; <b>C</b> and <b>D</b> read from one passage, nothing in the book able to refuse them &nbsp;·&nbsp; <b>G</b> a guess, printed in brackets and never counted &nbsp;·&nbsp; <b>withdrawn</b> a reading that was made and then refused, kept with the reason</div>
<div class="fig">{counts}</div>
<div class="tools">
  <input id="q" type="search" placeholder="search a reading or a sign" autocomplete="off">
  <button data-t="" class="on">All</button><button data-t="A">A</button><button data-t="B">B</button><button data-t="C">C</button><button data-t="D">D</button><button data-t="G">G</button><button data-t="withdrawn">Withdrawn</button>
  <span class="n" id="n"></span>
</div>
<div class="tw"><table class="dict"><thead><tr><th>Sign</th><th>Reading</th><th>Tier</th><th>Times</th><th>Evidence</th></tr></thead><tbody id="tb"></tbody></table></div>
<p><a href="/rohonc/data/proposals.json">Download the file</a> (JSON, every entry with its full evidence).</p>
<script>
(function(){{
var ROWS=[];var T='',Q='';
var tb=document.getElementById('tb'),nn=document.getElementById('n');
function esc(s){{return String(s).replace(/[&<>"]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c];}});}}
function grp(c){{return c.replace(/(...)/g,'$1 ').trim();}}
function draw(){{
  var q=Q.toLowerCase(),out=[],k=0;
  for(var i=0;i<ROWS.length;i++){{var r=ROWS[i];
    if(T&&r.tier!==T)continue;
    if(q&&r.gloss.toLowerCase().indexOf(q)<0&&r.code.indexOf(q.replace(/\\s+/g,''))<0)continue;
    k++; if(out.length>=400)continue;
    var ev=r.evidence||'',sh=ev.length>160?ev.slice(0,160)+'…':ev;
    out.push('<tr><td class=code>'+esc(grp(r.code))+'</td><td>'+esc(r.gloss)+'</td><td class=tier>'+esc(r.tier)+'</td><td>'+r.n+'</td><td class=ev><span class=short>'+esc(sh)+'</span>'+(ev.length>160?' <span class=more>more</span><span class=full>'+esc(ev)+'</span>':'')+'</td></tr>');
  }}
  tb.innerHTML=out.join('');
  nn.textContent=k.toLocaleString()+' of '+ROWS.length.toLocaleString()+(k>400?' — first 400 shown, narrow the search':'');
}}
tb.addEventListener('click',function(e){{if(e.target.classList.contains('more'))e.target.closest('tr').classList.add('open');}});
document.getElementById('q').addEventListener('input',function(){{Q=this.value.trim();draw();}});
Array.prototype.forEach.call(document.querySelectorAll('.tools button'),function(b){{b.addEventListener('click',function(){{
  Array.prototype.forEach.call(document.querySelectorAll('.tools button'),function(x){{x.classList.remove('on');}});
  b.classList.add('on');T=b.getAttribute('data-t');draw();}});}});
fetch('/rohonc/data/dictionary.json').then(function(r){{return r.json();}}).then(function(j){{
  ROWS=j; var ord={{A:0,B:1,C:2,D:3,G:4,withdrawn:5}};
  ROWS.sort(function(a,b){{return (ord[a.tier]-ord[b.tier])||(b.n-a.n)||(a.gloss<b.gloss?-1:1);}});
  draw();}}).catch(function(){{nn.textContent='The dictionary file did not load.';}});
}})();
</script>
"""
    return shell("dictionary", "Dictionary",
                 "This project's readings for Rohonc Codex signs Király and Tokai's dictionary leaves undefined, by tier, with count and evidence.",
                 body)


def page_doc(slug, fname, title):
    text = read(os.path.join(ROOT, fname))
    return shell(slug, title, f"{title}: {fname} from the Rohonc Codex project, rendered as it stands in the repository.",
                 md(text))


def page_outside(slug, fname, title):
    text = read(os.path.join(WORK, "outside", fname))
    intro = paras("outside_lead", "lead") + '<p>The results are on the <a href="/rohonc/tests.html">tests page</a>.</p>'
    return shell(slug, title, f"{title}: the outside reviewer's specification of tests for the Rohonc readings, quoted whole.",
                 f"<h1>{html.escape(title)}</h1>" + intro + md(text))


def page_data(files, runs, outside):
    def li(href, name, desc, size):
        return (f'<li><a href="{href}">{html.escape(name)}</a> <span class="nof">{html.escape(desc)}'
                f'{" · " + size if size else ""}</span></li>')

    def sz(p):
        n = os.path.getsize(p)
        return f"{n/1024:.0f} KB" if n < 1024 * 1024 else f"{n/1024/1024:.1f} MB"

    body = ["<h1>Data</h1>",
            paras("data_lead", "lead"),
            '<p>What is not here, and why, is under <a href="/rohonc/provenance.html">Sources</a>.</p>',
            "<h2>The readings and the rendering</h2><ul>"]
    for href, name, desc, p in files:
        body.append(li(href, name, desc, sz(p)))
    body.append("</ul><h2>The documents</h2><ul>")
    for slug, fname, _, title, desc in DOCS:
        body.append(li(f"/rohonc/{slug}.html", fname, desc, ""))
    body.append("</ul><h2>The outside review</h2><ul>")
    for href, name, desc, p in outside:
        body.append(li(href, name, desc, sz(p) if p else ""))
    body.append("</ul><h2>Saved runs</h2><p>One file per test or measurement, exactly as the script that made it wrote it. The scripts are named in the documents; each run states its bar at the top.</p><ul>")
    for href, name, p in runs:
        body.append(li(href, name, "", sz(p)))
    body.append("</ul>")
    return shell("data", "Data", "Every file the Rohonc pages are built from: the dictionary of added readings, the folio English, the rendering, the saved test runs and the outside readers' replies.",
                 "\n".join(body))


# ---- build ------------------------------------------------------------------------

def copy(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_DEFAULT)
    a = ap.parse_args(argv)
    out = a.out
    os.makedirs(os.path.join(out, "data", "runs"), exist_ok=True)

    fig = edition_figures()
    summary, ktn = tests_summary()
    newpara = new_here()
    about, rows = proposals()
    tiers = {}
    for r in rows:
        tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1
    order = folio_order()
    eng = json.load(open(os.path.join(TR, "english.json"), encoding="utf-8"))

    # data files
    files = []
    copy(os.path.join(ROOT, "harness", "proposals.json"), os.path.join(out, "data", "proposals.json"))
    files.append(("/rohonc/data/proposals.json", "proposals.json",
                  "the dictionary of added readings, every tier, with evidence", os.path.join(out, "data", "proposals.json")))
    json.dump(rows, open(os.path.join(out, "data", "dictionary.json"), "w", encoding="utf-8"), ensure_ascii=False)
    copy(os.path.join(TR, "english.json"), os.path.join(out, "data", "english.json"))
    files.append(("/rohonc/data/english.json", "english.json",
                  "the English written for each folio from its gloss", os.path.join(out, "data", "english.json")))
    for fn, desc in (("rohonc_reading_plus.txt", "the whole book rendered word by word, every word marked by how far it reads"),
                     ("rohonc_readers_edition.md", "the reader's edition: every folio, its English, and its marked lines")):
        copy(os.path.join(TR, fn), os.path.join(out, "data", fn))
        files.append((f"/rohonc/data/{fn}", fn, desc, os.path.join(out, "data", fn)))

    runs = []
    for fn in sorted(os.listdir(WORK)):
        if fn.endswith(".txt") and os.path.isfile(os.path.join(WORK, fn)):
            copy(os.path.join(WORK, fn), os.path.join(out, "data", "runs", fn))
            runs.append((f"/rohonc/data/runs/{fn}", fn, os.path.join(out, "data", "runs", fn)))

    outside = [("/rohonc/outside-gemini.html", "gemini_tests.md", "Gemini 2.5 Pro's specification", os.path.join(WORK, "outside", "gemini_tests.md")),
               ("/rohonc/outside-grok.html", "grok_tests.md", "Grok 4.7's specification", os.path.join(WORK, "outside", "grok_tests.md"))]
    odir = os.path.join(WORK, "outside")
    for sub in ("blindfill", "passid", "passid_v4pro_partial"):
        d = os.path.join(odir, sub)
        if os.path.isdir(d):
            for fn in sorted(os.listdir(d)):
                copy(os.path.join(d, fn), os.path.join(out, "data", "outside", sub, fn))
            outside.append((f"/rohonc/data/outside/{sub}/", f"outside/{sub}/",
                            f"the outside reader's replies, one file per page ({len(os.listdir(d))} files)", None))
    for fn in ("reglosser_gemini.json", "reglosser_grok.json"):
        copy(os.path.join(odir, fn), os.path.join(out, "data", "outside", fn))
        outside.append((f"/rohonc/data/outside/{fn}", fn, "an outside re-glosser's readings for Test 12", os.path.join(odir, fn)))
    # a directory listing for the reply folders, so the links above land somewhere
    for sub in ("blindfill", "passid", "passid_v4pro_partial"):
        d = os.path.join(out, "data", "outside", sub)
        if os.path.isdir(d):
            items = "".join(f'<li><a href="{fn}">{html.escape(fn)}</a></li>' for fn in sorted(os.listdir(d)) if fn != "index.html")
            open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(
                shell("data", sub, f"the outside reader's replies for {sub}", f"<h1>outside/{sub}</h1><ul>{items}</ul>"))

    # pages
    w = lambda name, s: open(os.path.join(out, name), "w", encoding="utf-8").write(s)
    w("index.html", page_index(fig, summary, ktn, newpara, tiers, len(order)))
    rd, n_eng = page_reading(order, eng)
    w("reading.html", rd)
    w("dictionary.html", page_dictionary(about, rows, ktn))
    for slug, fname, _, title, _ in DOCS:
        w(f"{slug}.html", page_doc(slug, fname, title))
    w("outside-gemini.html", page_outside("tests", "gemini_tests.md", "Outside review: Gemini 2.5 Pro"))
    w("outside-grok.html", page_outside("tests", "grok_tests.md", "Outside review: Grok 4.7"))
    w("data.html", page_data(files, runs, outside))
    print(f"wrote {out}: {len(order)} folios ({n_eng} with English), {len(rows)} dictionary rows, "
          f"{len(DOCS) + 5} pages, {len(runs)} runs")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
