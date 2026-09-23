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
import glob
import html
import json
import os
import re
import shutil
import tempfile
import sys

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The prose of the site is written by an outside model from a fact sheet
# (ktsitecopy.py) and read back by a person; this file only places it.
COPY = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ktsite_copy.json"), encoding="utf-8"))


def items(key, tag="li", kt="t", kd="d"):
    """A copy list (steps, mistakes, citations) as <li> rows."""
    out = []
    for x in COPY[key]:
        t = html.escape(str(x.get(kt, "")).strip().rstrip("."))
        d = html.escape(str(x.get(kd, "")).strip())
        out.append(f"<{tag}><b>{t}.</b> {d}</{tag}>" if t else f"<{tag}>{d}</{tag}>")
    return "".join(out)


_URL = re.compile(r"https?://[^\s<>\"]+?(?=[.,;:)]*(?:\s|$))")


def linkify(escaped):
    """A web address written out in the copy becomes a link to itself, shown
    without its scheme. The owner found the repository's address printed as
    plain text on the Data page; escaping is not the same as rendering."""
    return _URL.sub(lambda m: f'<a href="{m.group(0)}">{m.group(0).split("://", 1)[1]}</a>', escaped)


def paras(key, cls=""):
    """A copy piece as <p> paragraphs."""
    c = f' class="{cls}"' if cls else ""
    return "".join(f"<p{c}>{linkify(html.escape(t.strip()))}</p>" for t in COPY[key].split("\n\n") if t.strip())
WORK = os.path.join(ROOT, "work", "rohonc")
TR = os.path.join(WORK, "translation")
OUT_DEFAULT = "/var/www/oona13/rohonc"
BG = "#0B0D10"   # the family's dark ground; the page is a sheet laid on it
V = "20260923"

# The project's own working documents. They are DESCRIBED here; METHOD.md, the
# standing orders, is also published whole at orders.html:
# they are written for whoever runs the project next, they argue with earlier
# versions of themselves, and a reader is not the audience. Anyone who wants one
# can ask. The pages on this site are written from them instead.
DOCS = [
    ("ROHONC.md", "The full account",
     "The line-break measurement that started it, the dictionary, all seventeen attempts to "
     "extend it with the ten that failed, what the book turns out to say, and what none of it "
     "decides. The longest of them by far."),
    ("METHOD.md", "The standing orders",
     "What the next person is to do, in order, and the arithmetic of how much of the book is "
     "still unread. Three earlier versions of that arithmetic were wrong and are kept on the "
     "page beside the right one."),
    ("TESTS.md", "The tests in full",
     "Every test with the bar it declared before it ran, the control it was measured against, "
     "and the saved run it produced."),
    ("DATA_PROVENANCE.md", "Where each file came from",
     "Every source, the terms it carries, what may be done with it, and one courtesy failure "
     "recorded so it is not repeated."),
    ("FINALPASS.md", "The vocabulary before the guesses",
     "Why the words had to be checked before the bracketed restorations were, and what that changed."),
    ("BLINDFOLD.md", "The blindfold test",
     "The one check the project cannot run on itself, written as instructions for a stranger."),
    ("DARK.md", "The last unread words",
     "The final few per cent of the manuscript, how they were closed, and what the attempt taught."),
]

CONTACT = "info@oona13.com"

# "The reading" is NOT in this list, deliberately. It sat beside "Read it" and
# the two names told a visitor nothing apart: "Read it" is the book, the
# narrative and the complete gloss; reading.html is a summary written from the
# gloss, one paragraph a folio. It keeps its front-page card, its links from
# the pages that need it, and its place in the sitemap at priority 0.8 -- the
# book is behind a JS reader, so those 441 paragraphs are the largest piece of
# the codex's text a crawler can see. Out of the menu, not off the site.
NAV = [("index", "Overview"), ("read", "Read it"), ("script", "The script"), ("atlas", "Atlas"),
       ("finds", "Discoveries"), ("corpus", "The corpus"), ("dictionary", "Dictionary"), ("tests", "Tests"), ("method", "Method"),
       ("sources", "Sources"), ("data", "Data")]

# THE FOOT OF EVERY PAGE IS LINKS, NOT A CREDIT. It carried a sentence crediting
# Kiraly and Tokai; the owner cut it on 2026-09-23 -- every page already credits
# them where it matters -- and asked for the useful things instead: the licence,
# how to cite, the sources, the data, the repository, a way to write in.
FOOT = [("Licence", "https://github.com/styopr613/rohonc-codex/blob/master/LICENSE"),
        ("How to cite", "https://doi.org/10.5281/zenodo.22902166"),
        ("Sources", "/rohonc/sources.html"),
        ("Data", "/rohonc/data.html"),
        ("Repository", "https://github.com/styopr613/rohonc-codex"),
        ("Contact", "mailto:" + CONTACT)]
FOOT_HTML = " · ".join(f'<a href="{u}">{html.escape(t)}</a>' for t, u in FOOT)

CSS = """
/* fam.js lays an opaque veil over every arrival and fades it out over .17s even
   when the browser's own view transition is doing the hop. On a light page that
   veil is the page's own cream and nobody sees it; here it is #0B0D10 over a cream
   sheet, so every hop read as the page going black and lighting up again --
   measured live at 150->22 brightness on each click. The veil is dropped on
   ARRIVAL with no fade. On the way OUT (html.oona-leaving) it keeps its fade, so
   a hop to another OONA property still dims before it goes. */
html:not(.oona-leaving) #oona-veil.out{transition:none!important}
/* The family stylesheet enables cross-document view transitions globally. On
   these pages the active item in the local menu changes at the same moment,
   so Chromium briefly blended two copies of the menu. Use a direct navigation
   within Rohonc instead. A stable scrollbar gutter keeps short and long pages
   at the same content width. */
@view-transition{navigation:none}
html{scrollbar-gutter:stable}
:root{--bg:#0B0D10;--ink:#1d1a16;--soft:#5a5248;--paper:#f5efe3;--paper2:#ece5d5;--rub:#7a2418;--ivory:#e9e2d3;--line:#d9cfb9}
body{margin:0;background:var(--bg);color:var(--ivory);font-family:"EB Garamond",Garamond,"Times New Roman",serif;font-size:19px;line-height:1.55}
header.rh{padding:34px 20px 8px;text-align:center}
header.rh .mark{font-family:Cinzel,"Times New Roman",serif;font-size:30px;letter-spacing:.12em;color:var(--ivory);text-decoration:none;text-transform:uppercase}
header.rh .tag{margin:8px 0 0;color:#b7ad9b;font-style:italic;font-size:18px}
nav.sub{margin:20px 0 0;font-size:14px;letter-spacing:.09em;text-transform:uppercase}
nav.sub a{color:#bdb3a1;text-decoration:none;margin:0 10px;padding-bottom:3px;border-bottom:1px solid transparent;display:inline-block}
nav.sub a:hover{color:#e6c979}
nav.sub a.here{color:#e6c979;border-bottom-color:#e6c979}
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
table.tests{width:100%;font-size:15.5px}
table.tests th{font-weight:400;color:var(--soft);font-size:13px;letter-spacing:.06em;text-transform:uppercase;white-space:nowrap}
table.tests tbody th{color:var(--ink);font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13.5px;text-transform:none;letter-spacing:0}
table.tests td{line-height:1.4}
table.tests td.verdict{font-family:Cinzel,serif;font-size:12.5px;letter-spacing:.07em;white-space:nowrap}
table.tests .v-pass{color:#3b6b3a}
table.tests .v-fail{color:var(--rub)}
table.tests .v-none{color:var(--soft)}
table.tests .v-band{color:#7a5a1e}
table.tests td.verdict.v-note{color:var(--soft);font-family:"EB Garamond",serif;font-size:14px;letter-spacing:0;text-transform:none;white-space:normal;font-style:italic}
table.tests tr.cap td{color:var(--soft);font-style:italic;border-bottom:0;padding-top:12px}
table.tests tr.cap+tr.cap td{padding-top:2px}
@media(max-width:620px){
  table.tests,table.tests tbody,table.tests tr,table.tests td,table.tests tbody th{display:block;width:auto}
  table.tests thead{display:none}
  table.tests tr{border-bottom:1px solid var(--line);padding:10px 0}
  table.tests td,table.tests tbody th{border:0;padding:2px 0}
  table.tests tbody th{float:left;padding-right:10px}
  table.tests td.verdict{float:right;padding-top:3px}
  table.tests td:nth-child(2){clear:both;font-style:italic;color:var(--soft)}
  table.tests tr.cap{padding:14px 0 2px}
}
.prose hr{border:0;border-top:1px solid var(--line);margin:2em 0}
.prose ul,.prose ol{padding-left:1.4em}
.prose li{margin:.25em 0}
.prose img{max-width:100%}
.lead{font-size:21px}
.fig{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:14px;line-height:1.5;background:var(--paper2);padding:14px 18px;border-radius:3px;margin:1em 0;white-space:pre;overflow-x:auto}
.credit{border-top:1px solid var(--line);margin-top:2.5em;padding-top:1em;color:var(--soft);font-size:15px;letter-spacing:.02em}
.credit a{color:var(--soft);text-decoration:none;border-bottom:1px solid var(--line)}.credit a:hover{color:var(--rub);border-color:var(--rub)}
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
/* the illuminated initial: a rubric capital in the display face, set in a
   paper-coloured square with a double rule, the way a manuscript opens */
.hero .blurb p.dc::first-letter{float:left;font-family:Cinzel,"Times New Roman",serif;font-size:4.9em;line-height:.82;color:var(--rub);padding:.14em .16em .08em .12em;margin:.06em .16em 0 0;background:var(--paper2);border:1px solid var(--rub);outline:1px solid var(--rub);outline-offset:2px}
.hero .blurb p.dc{margin-top:.3em}
.orders h1{font-size:24px;margin-top:1.6em}.orders h2{font-size:20px}.orders pre{font-size:13px}.orders code{font-size:.82em}
/* the front page: the book, the scroller */
.hero{display:grid;grid-template-columns:minmax(0,1fr) 236px;gap:34px;align-items:center;margin:0 0 6px}
.hero .blurb p:first-child{margin-top:0}
.hero .bk{margin:0}
.hero .bk img{width:100%;height:auto;display:block;filter:drop-shadow(0 16px 26px rgba(0,0,0,.32))}
.book-peek{display:block;width:100%;padding:0;border:0;background:transparent;color:var(--rub);font:inherit;cursor:pointer}
.book-peek img{transition:transform .18s ease,filter .18s ease}
.book-peek:hover img{transform:translateY(-3px);filter:drop-shadow(0 19px 28px rgba(0,0,0,.38))}
.book-peek:focus-visible{outline:2px solid var(--rub);outline-offset:8px;border-radius:2px}
.book-peek-note{display:block;margin:.8em 0 0;text-align:center;font-size:14px;font-style:italic;color:var(--soft)}
.book-modal{width:min(620px,calc(100vw - 40px));max-height:calc(100vh - 40px);box-sizing:border-box;overflow:auto;padding:38px 42px 32px;border:1px solid var(--line);border-radius:4px;background:var(--paper);color:var(--ink);box-shadow:0 20px 70px rgba(0,0,0,.65)}
.book-modal::backdrop{background:rgba(5,6,8,.78)}
.book-modal h2{margin:0 35px .8em 0}
.book-modal p{font-size:18px;line-height:1.5}
.book-modal .modal-close{position:absolute;top:13px;right:15px;width:34px;height:34px;padding:0;border:0;background:transparent;color:var(--soft);font:28px/1 Georgia,serif;cursor:pointer}
.book-modal .modal-close:hover,.book-modal .modal-close:focus{color:var(--rub)}
.book-modal .acts{margin-bottom:0}
body:has(.book-modal[open]){overflow:hidden}
/* THE DOOR TO THE READER IS A BUTTON. This rule was scoped to .hero, so the same
   markup on the Read page -- the one page whose whole job is to open the book --
   printed as two plain underlined links with a space between them: "Open the book
   EPUB", which reads as one string and says nothing about the book opening here.
   Unscoped, with the standalone one given the size of a page's primary action.
   (2026-09-22) */
.acts{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:1.5em 0}
.acts a{display:inline-block;text-decoration:none;font-family:Cinzel,serif;font-size:13.5px;letter-spacing:.08em;text-transform:uppercase;padding:9px 14px;border:1px solid var(--rub);border-radius:3px;color:var(--rub)}
.acts a.go{background:var(--rub);color:#fff}
.acts a:hover{background:var(--rub);color:#fff}
.hero .acts{margin:14px 0 0}
.prose .acts{gap:14px}
.prose .acts a.go{font-size:17px;padding:15px 30px;border-radius:4px;box-shadow:0 2px 0 rgba(122,36,24,.35)}
.prose .acts a.go:hover{box-shadow:0 1px 0 rgba(122,36,24,.35);transform:translateY(1px)}
.hero .sz{font-size:15px;color:var(--soft);margin:10px 0 0}
.strip{margin:1.6em -64px;padding:var(--top) 0 22px;background:var(--paper2);position:relative;--padl:0px;--padr:0px;--lens:104px}
.strip .win{position:relative;height:var(--win)}
.strip .track{position:absolute;inset:0;overflow-x:auto;overflow-y:hidden;scrollbar-width:none;-ms-overflow-style:none;overscroll-behavior-x:contain}
.strip .track::-webkit-scrollbar{height:0;display:none}
.strip .track:focus-visible{outline:2px solid var(--rub);outline-offset:-3px;border-radius:3px}
.strip .rail{display:flex;width:max-content;height:100%;align-items:center;gap:34px;padding:0 var(--padr) 0 var(--padl)}
.strip .it{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;min-width:58px}
.strip .it .sv{color:var(--ink)}
.strip .it b{font-weight:400;font-size:16px;white-space:nowrap}
.strip .it span{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:11.5px;color:var(--soft);letter-spacing:.06em}
.strip .fade{position:absolute;inset:0;pointer-events:none;background:linear-gradient(90deg,var(--paper) 0,transparent 8%,transparent 92%,var(--paper) 100%)}
.strip .glass,.strip .lens,.strip .nudge,.strip .rcap{display:none}
/* with JS the strip becomes a thing you drag, and the glass reads what passes under it */
.strip.glassed .track{cursor:grab}
.strip.glassed .track.grabbing{cursor:grabbing}
.strip.glassed .it{flex-direction:row}
.strip.glassed .it b,.strip.glassed .it span{position:absolute;width:1px;height:1px;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.strip.glassed .glass{display:block;position:absolute;left:50%;top:50%;width:var(--gw);height:var(--gh);margin:calc(var(--gy) * -1) 0 0 calc(var(--gx) * -1);pointer-events:none;transform-origin:var(--gx) var(--gy);will-change:transform}
.strip.glassed .lens{display:block;position:absolute;left:50%;top:50%;width:var(--lens);height:var(--lens);margin:calc(var(--lens)/-2) 0 0 calc(var(--lens)/-2);border-radius:50%;overflow:hidden;background:var(--paper2);pointer-events:none}
.strip .lens .rail{position:absolute;left:0;top:50%;transform-origin:0 50%;will-change:transform}
.strip .rim{display:block;width:100%;height:100%}
.strip.glassed .nudge{display:block;position:absolute;top:50%;width:38px;height:38px;margin-top:-19px;padding:0;border:1px solid var(--line);border-radius:50%;background:var(--paper);color:var(--soft);font:400 26px/1 "EB Garamond",Garamond,serif;cursor:pointer}
.strip .nudge:hover{color:var(--rub);border-color:var(--rub)}
.strip .nudge[disabled]{opacity:.25;cursor:default;color:var(--soft);border-color:var(--line)}
.strip .nudge.l{left:12px}
.strip .nudge.r{right:12px}
.strip.glassed .rcap{display:block;text-align:center;margin:var(--cap) 0 0;padding:0 16px;min-height:28px}
.strip .rcap b{font-weight:400;font-size:21px;color:var(--rub)}
.strip .rcap span{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px;color:var(--soft);letter-spacing:.06em;margin-left:12px}
.shot{margin:1.6em 0}
.shot img{width:100%;display:block;border:1px solid var(--line);background:#fff}
.shot figcaption{font-size:15.5px;color:var(--soft);padding-top:8px}
ol.steps,ul.steps{padding-left:1.3em}
ol.steps li,ul.steps li{margin:0 0 .8em}
ol.steps li b,ul.steps li b{font-weight:400;color:var(--rub)}
/* the script page */
.demo{background:var(--paper2);border-radius:3px;padding:18px 20px;margin:1.2em 0}
.demo h3{font-family:Cinzel,serif;font-weight:400;font-size:15px;letter-spacing:.08em;text-transform:uppercase;color:var(--rub);margin:0 0 10px}
.sign{display:flex;flex-wrap:wrap;gap:18px;align-items:baseline}
.sign .code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:15px;color:var(--soft);letter-spacing:.08em}
.sign .gl{font-size:26px}
.sign .glyph{font-family:"Rohonc Codex";font-size:34px;line-height:1.1}
.sign .meta{font-size:15px;color:var(--soft);width:100%}
.sign .ev{font-size:15.5px;width:100%;margin:0}
.ctl{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:14px}
.ctl button{font:inherit;font-size:14px;letter-spacing:.06em;text-transform:uppercase;padding:7px 12px;border:1px solid var(--line);border-radius:3px;background:var(--paper);color:var(--ink);cursor:pointer}
.ctl button:hover{border-color:var(--rub);color:var(--rub)}
.ctl button.on{background:var(--rub);border-color:var(--rub);color:#fff}
.ctl .sp{margin-left:auto;font-size:15px;color:var(--soft)}
.parts{display:flex;flex-wrap:wrap;gap:10px;align-items:stretch;margin:2px 0 0}
.parts .pc{background:var(--paper);border:1px solid var(--line);border-radius:3px;padding:8px 12px;min-width:92px}
.parts .pc b{display:block;font-size:19px;font-weight:400}
.parts .pc span{font-size:13px;color:var(--soft);font-family:ui-monospace,monospace}
.parts .op{align-self:center;color:var(--rub);font-size:20px}
.sums{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:15px;line-height:1.9}
.sums b{color:var(--rub);font-weight:400}
.gloss{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:14.5px;line-height:1.8;overflow-x:auto}
.gloss .m{border-bottom:2px solid var(--rub);cursor:help}
.plates{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px;margin:1.2em 0}
.plates figure{margin:0}
.plates img{width:100%;display:block;border:1px solid var(--line);background:#fff}
.plates figcaption{font-size:15.5px;color:var(--soft);padding-top:7px}
/* THE ATLAS. Each plate is an inline SVG with a viewBox and no size, so it takes the
   column; the page's EB Garamond reaches into it. Marked items are <g class="ev"> and
   the popup below is positioned fixed from the click. [hidden] is guarded because a
   display rule on the popup would otherwise beat the attribute. */
.atlas figure{margin:2.4em 0 0}
.atlas svg{width:100%;height:auto;display:block;border:1px solid var(--line);border-radius:3px;background:#f6f1e7}
.atlas figcaption{font-size:16px;color:var(--soft);padding-top:8px;font-style:italic}
.atlas .ev{cursor:pointer;outline:none}
.atlas .ev:hover circle,.atlas .ev:focus circle,.atlas .ev:hover polygon,.atlas .ev:focus polygon{stroke:#b9543b;stroke-width:3}
.atlas .ev:hover rect[rx],.atlas .ev:focus rect[rx]{stroke-width:2.6}
.tlpop{position:fixed;z-index:60;max-width:min(360px,calc(100vw - 24px));background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:4px;padding:14px 38px 14px 16px;box-shadow:0 12px 40px rgba(0,0,0,.55);font-size:16px;line-height:1.45}
.tlpop[hidden]{display:none}
.tlpop b{display:block;font-family:Cinzel,serif;font-weight:400;color:var(--rub);letter-spacing:.03em;font-size:15px;margin-bottom:2px}
.tlpop i{display:block;color:var(--soft);font-size:14px;margin-bottom:6px}
.tlpop p{margin:0}
.tlpop button{position:absolute;top:2px;right:6px;border:0;background:none;font:22px/1 Georgia,serif;cursor:pointer;color:var(--soft)}
.atlas-src{margin-top:2.4em;font-size:15px;color:var(--soft)}
.atlas-src summary{cursor:pointer;color:var(--rub)}
.atlas-src ul{padding-left:1.2em}.atlas-src li{margin:.35em 0}
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
@media(max-width:860px){.hero{grid-template-columns:1fr;gap:20px}.hero .bk{max-width:220px;margin:0 auto;order:-1}.strip{margin-left:-20px;margin-right:-20px}}
@media(max-width:700px){body{font-size:17.5px}main.sheet{margin:14px 10px 40px;padding:26px 20px 34px}header.rh .mark{font-size:22px}nav.sub a{margin:0 6px 6px}.prose h1{font-size:24px}.book-modal{padding:32px 24px 26px}.tools .n{margin-left:0}}
"""


FAM_CSS = "https://oona13.com/fam/fam.css?v=20260909b"
FONTS_URL = ("https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;"
             "0,600;1,400;1,500&family=Cinzel:wght@400;600&display=swap")


# The social card and the traffic tag. These pages were behind the sign-in gate
# from 2026-09-21 until they were published, so they never carried either: no
# og:image, and none of the Google Analytics property the rest of oona13 uses.
# A page nobody could reach needs no tag; a published one does.
OG_IMAGE = "https://oona13.com/rohonc/img/book3d.png"
GA_ID = "G-RYS4E6EW16"
ANALYTICS = (
    f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>\n'
    '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
    f"gtag('js',new Date());gtag('config','{GA_ID}');</script>\n")


def shell(slug, title, desc, body, extra_head=""):
    nav = "".join(
        f'<a href="/rohonc/{"" if s == "index" else s + ".html"}"'
        f'{" class=here" if s == slug else ""}>{html.escape(lab)}</a>'
        for s, lab in NAV)
    t = html.escape(title)
    d = html.escape(desc)
    url = "https://oona13.com/rohonc/" + ("" if slug == "index" else slug + ".html")
    return f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="dark">
<link rel="expect" href="#oona-fam-ready" blocking="render">
<style>html{{background:{BG}}}body{{background:{BG}}}</style>
<link rel="stylesheet" href="{FAM_CSS}">
<title>{t} · The Rohonc Codex · OONA 13</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{t} · The Rohonc Codex"><meta property="og:description" content="{d}">
<meta property="og:type" content="article"><meta property="og:url" content="{url}">
<meta property="og:site_name" content="OONA 13"><meta property="og:image" content="{OG_IMAGE}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{OG_IMAGE}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS_URL}" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="{FONTS_URL}" rel="stylesheet"></noscript>
<style>{CSS}</style>
{ANALYTICS}{extra_head}
</head><body>
<script src="https://oona13.com/fam/fam.js?v={V}"></script><i id="oona-fam-ready" hidden></i>
<header class="rh"><div class="wrap">
  <a class="mark" href="/rohonc/">The Rohonc Codex</a>
  <p class="tag">{html.escape(COPY["tagline"].strip())}</p>
  <nav class="sub">{nav}</nav>
</div></header>
<main class="sheet"><article class="prose">
{body}
<p class="credit">{FOOT_HTML}</p>
</article></main>
<script src="https://oona13.com/fam/foot.js" data-note="{html.escape(FOOT_HTML)}" defer></script>
</body></html>
"""


def md_inline(text):
    """One line of markdown (the *italics* in a citation), without a <p> around it."""
    out = markdown.markdown(text)
    return re.sub(r"^<p>|</p>$", "", out.strip())


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


def how_far(g):
    """The reading figures in a sentence, generated from the edition header.

    This paragraph was stored prose in ktsite_copy.json and nothing carried
    it: it said 93.4% read, 3.2% from one passage and 81.6% of lines while the
    edition said 94.1, 2.5 and 81.5. Model-written copy goes stale exactly
    like typed copy, and the figures belong to the run, so the sentence is
    built here and the stored key is no longer read.
    """
    return (
        f"<p>The manuscript contains {int(g['words'][0].replace(',', '')):,} words. "
        f"The project has a reading for {g['read'][1]}% of them. "
        f"{g['soft'][1]}% of all words are read from one passage only. "
        f"{g['rest'][1]}% are restored in brackets. {g['dark'][1]}% are dark. "
        f"{g['lread'][2]}% of lines have every word read. "
        f"Lines are {g['lall'][2]}% complete once brackets are counted.</p>")


def tests_summary():
    txt = read(os.path.join(ROOT, "TESTS.md"))
    m = re.search(r"\n## Summary\n\n((?:    .*\n|\n)+?)\n(?=[^\s])", txt)
    if not m:
        raise SystemExit("ktsite: no Summary block in TESTS.md")
    block = "\n".join(l[4:] if l.startswith("    ") else l for l in m.group(1).rstrip("\n").split("\n"))
    kt = re.search(r"dictionary of (\d+) signs", txt)
    return block, (kt.group(1) if kt else "?")


VERDICT_CLASS = (("NO VERDICT", "v-none"), ("IN BAND", "v-band"), ("PASS", "v-pass"),
                 ("FAIL", "v-fail"), ("reported", "v-note"))


def summary_table(block):
    """The tests summary as a table. TESTS.md keeps it as pipe-separated rows,
    test | what it asks | result | verdict, so the document reads on its own and
    the page can give the verdict its own column. A line without pipes is a
    caption row: the legend, or the line that says the outside review began."""
    rows, cap = [], []
    def flush():
        if cap:
            rows.append(f'<tr class="cap"><td colspan="4">{html.escape(" ".join(cap))}</td></tr>')
            cap.clear()
    for line in block.split("\n") + [""]:
        if not line.strip():
            flush()
            continue
        if "|" not in line:
            cap.append(line.strip())
            continue
        flush()
        cells = [c.strip() for c in line.split("|")]
        while len(cells) < 4:
            cells.append("")
        test, what, result, verdict = cells[:4]
        cls = "v-note"
        for word, c in VERDICT_CLASS:
            if verdict.startswith(word):
                cls = c
                break
        tm = re.match(r"Test (\d+)", test)
        cell = (f'<a href="/rohonc/code.html#test-{tm.group(1)}">{html.escape(test)}</a>' if tm else html.escape(test))
        rows.append(f'<tr><th scope="row">{cell}</th><td>{html.escape(what)}</td>'
                    f'<td>{html.escape(result)}</td><td class="verdict {cls}">{html.escape(verdict)}</td></tr>')
    return ('<div class="tw"><table class="tests"><thead><tr><th>test</th><th>what it asks</th>'
            '<th>result</th><th>verdict</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table></div>")


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


def sample_lines(folio="004v", first=10, last=11):
    """A real stretch of the rendering, straight out of the reader's edition, so the
    page explaining the marks is showing the book rather than an invented example."""
    txt = read(os.path.join(TR, "rohonc_readers_edition.md"))
    m = re.search(r"^## %s — .*?$(.*?)(?=^## )" % folio, txt, re.M | re.S)
    if not m:
        raise SystemExit("ktsite: no %s in the reader's edition" % folio)
    out = []
    for ln in m.group(1).split("\n"):
        g = re.match(r"^\s{1,3}(\d+)\s\s(.*)$", ln)
        if g and first <= int(g.group(1)) <= last:
            out.append((g.group(1), g.group(2).rstrip()))
    if not out:
        raise SystemExit("ktsite: no lines %d-%d on %s" % (first, last, folio))
    return out


def signs():
    """Every sign of the script as an outline, from ktsigns.py."""
    p = os.path.join(WORK, "signs.json")
    return json.load(open(p, encoding="utf-8")) if os.path.isfile(p) else {"signs": {}, "upm": 1000}


def sign_svg(code, sg, h=52, cls="sv"):
    """Draw a reading's signs as one SVG, laid out RIGHT TO LEFT, the way the
    manuscript is written: the first sign of the code sits on the right."""
    gl = [sg["signs"].get(code[i:i + 3]) for i in range(0, len(code), 3)]
    gl = [g for g in gl if g]
    if not gl:
        return ""
    total = sum(g["w"] for g in gl)
    y0 = min(g["b"][1] for g in gl)
    y1 = max(g["b"][3] for g in gl)
    pad = 40
    parts, x = [], total
    for g in gl:
        x -= g["w"]
        parts.append(f'<path d="{g["d"]}" transform="translate({x} 0)"/>')
    vb = f"0 {-y1 - pad} {total} {y1 - y0 + 2 * pad}"
    w = round(h * (total / max(1, (y1 - y0 + 2 * pad))))
    return (f'<svg class="{cls}" viewBox="{vb}" width="{w}" height="{h}" '
            f'role="img" aria-label="the sign read {html.escape(code)}">'
            f'<g transform="scale(1,-1)" fill="currentColor">{"".join(parts)}</g></svg>')


def plates():
    p = os.path.join(WORK, "plates.json")
    return json.load(open(p, encoding="utf-8")) if os.path.isfile(p) else []


def folio_order():
    """Kiraly and Tokai's page order and this edition's folio titles, from the
    reader's edition headings."""
    out = []
    for m in re.finditer(r"^## (\d{3}[rv]) — (.*)$", read(os.path.join(TR, "rohonc_readers_edition.md")), re.M):
        out.append((m.group(1), m.group(2).strip()))
    return out


# ---- pages ------------------------------------------------------------------------

# The glass over the strip: a brass ring, a short handle, a sheen. Drawn here
# rather than fetched so it cannot arrive after the signs, and drawn in the
# lens's own coordinates -- the viewBox is centred on the lens, so the circle
# the CSS clips and the ring the SVG paints are the same circle by construction.
STRIP_OPEN = 4   # which sign the strip opens under the glass

# The glass itself is a photograph made with Seedream (harness/ktglass.py), cut
# so that the lens is a real hole. Nothing about its geometry is typed here: the
# cutter measured the hole it left and wrote the numbers to work/rohonc/glass.json,
# and everything below is computed from them, so a different glass -- a thicker
# rim, a handle at another angle -- needs no CSS touched, only the file swapped.
SIGN_PX = 36     # how tall a sign is drawn on the strip
LENS_PX = 150         # the hole, on screen
LENS_MOBILE_PX = 118  # ... on a narrow screen
LENS_SMALL_PX = 104   # ... on the narrowest
WIN_PX = 104     # the height of the row the signs sit in
TUCK = 5         # the clipped rail runs this much under the rim, so no seam of
                 # paper shows between the magnified sign and the brass


def glass_geom(lens=None):
    lens = LENS_PX if lens is None else lens
    g = json.load(open(os.path.join(WORK, "glass.json"), encoding="utf-8"))
    k = lens / (2.0 * g["r"])
    above = g["cy"] * k                     # how far the rim stands above the lens
    below = (g["h"] - g["cy"]) * k          # how far the handle hangs below it
    half = WIN_PX / 2
    return {
        "w": round(g["w"] * k), "h": round(g["h"] * k),
        "cx": round(g["cx"] * k), "cy": round(g["cy"] * k),
        "clip": lens + TUCK,
        # the band opens above the highest ink and the caption clears the lowest,
        # whatever picture it is and whatever size the lens is set to
        "top": max(18, round(above - half + 14)),
        "cap": max(16, round(below - half + 14)),
    }


def glass_vars(gg):
    return (f'--lens:{gg["clip"]}px;--gw:{gg["w"]}px;--gh:{gg["h"]}px;'
            f'--gx:{gg["cx"]}px;--gy:{gg["cy"]}px;--cap:{gg["cap"]}px;--top:{gg["top"]}px')


def strip_css():
    """Every size the glass is drawn at, as a stylesheet rule.

    These were inline on the element to begin with, and a media query can never
    beat an inline style, so the phone kept the wide sheet's 150px glass and it
    covered the whole band. They live here, after the main stylesheet, where the
    narrow rules win by coming later. A phone is not a wide sheet: at 150px the
    glass hides the signs either side of it, which is the one thing the strip is
    for. Each smaller lens is the SAME measurement run again at a smaller size,
    so the rim and the hole still agree."""
    return ("<style>.strip{" + glass_vars(glass_geom()) + f";--win:{WIN_PX}px" + "}"
            + "@media(max-width:620px){.strip{" + glass_vars(glass_geom(LENS_MOBILE_PX)) + "}}"
            + "@media(max-width:400px){.strip{" + glass_vars(glass_geom(LENS_SMALL_PX)) + "}}</style>")


def strip_html(rows, sg, n=54):
    """The strip of signs and the glass over it. The strip does not move by
    itself: the reader drags it, and whatever sign passes under the lens is
    magnified and named underneath. Rendered into the page, not fetched: it has
    to be there in the first frame, and it is the first thing anyone will look
    at. Without JavaScript the same markup is a plain scrollable row with every
    sign's reading under it, which is what this was before the glass."""
    pick = [r for r in rows if r["tier"] in ("A", "B") and 3 <= len(r["code"]) <= 9 and r["gloss"]
            and " " not in r["gloss"] and "<" not in r["gloss"]]
    pick.sort(key=lambda r: (-r["n"], r["gloss"]))
    pick = [r for r in pick[:n] if sign_svg(r["code"], sg, SIGN_PX)]
    if not pick:
        return ""
    def spaced(code):
        return " ".join(code[i:i + 3] for i in range(0, len(code), 3))
    def gloss(r):
        # proposals.json joins a compound gloss with underscores and marks an
        # ambiguity with a slash; the caption has room to say both properly
        return r["gloss"].replace("_", " ").replace("/", " / ")
    it = "".join(
        f'<span class="it">{sign_svg(r["code"], sg, SIGN_PX)}'
        f'<b>{html.escape(gloss(r))}</b>'
        f'<span>{html.escape(spaced(r["code"]))}</span></span>'
        for r in pick)
    # the strip opens a few signs in, so the glass has signs on both sides of
    # it; the caption is rendered from that same sign, so the first paint says
    # something true without waiting for a frame of JavaScript
    op = min(STRIP_OPEN, len(pick) - 1)
    cap = (f'<p class="rcap"><b>{html.escape(gloss(pick[op]))}</b>'
           f'<span>{html.escape(spaced(pick[op]["code"]))}</span></p>')
    gg = glass_geom()
    return (f'<div class="strip" data-open="{op}"><div class="win">'
            f'<div class="track" tabindex="0" role="group" '
            f'aria-label="signs of the codex: drag the strip, or use the left and right arrow keys">'
            f'<div class="rail">{it}</div></div>'
            f'<div class="lens"><div class="rail">{it}</div></div>'
            f'<div class="glass"><img class="rim" src="/rohonc/img/glass.png" alt="" '
            f'width="{gg["w"]}" height="{gg["h"]}"></div>'
            f'<div class="fade"></div>'
            f'<button class="nudge l" type="button" aria-label="previous sign">‹</button>'
            f'<button class="nudge r" type="button" aria-label="next sign">›</button>'
            f'</div>{cap}</div>')


# The lens is a second copy of the same rail, scaled about a point and slid so
# that the content under the middle of the strip sits under the middle of the
# lens. Both rails carry the same pixel padding (--pad, set here, never a
# percentage) so one coordinate serves both; a percentage would resolve against
# two different boxes and the magnified sign would drift off the one below it.
STRIP_JS = """<script>
(function(){
  var strip=document.querySelector('.strip'); if(!strip||!strip.querySelector('.glass')) return;
  var track=strip.querySelector('.track'), rail=track.firstElementChild,
      lens=strip.querySelector('.lens'), mag=lens.firstElementChild,
      glass=strip.querySelector('.glass'),
      prev=strip.querySelector('.nudge.l'), next=strip.querySelector('.nudge.r'),
      cap=strip.querySelector('.rcap'), capw=cap.querySelector('b'), capc=cap.querySelector('span'),
      items=Array.prototype.slice.call(rail.children),
      M=1.8, mid=[], cur=-1,
      calm=window.matchMedia('(prefers-reduced-motion: reduce)');
  if(!items.length) return;
  strip.classList.add('glassed');

  // ---- the detents ---------------------------------------------------------
  function nearest(p){
    var best=0,d=Infinity;
    for(var i=0;i<mid.length;i++){var v=Math.abs(mid[i]-p); if(v<d){d=v;best=i;}}
    return best;
  }
  function stop(i){
    var x=mid[Math.max(0,Math.min(mid.length-1,i))]-track.clientWidth/2;
    return Math.max(0,Math.min(track.scrollWidth-track.clientWidth,x));
  }
  function here(){ return nearest(track.scrollLeft+track.clientWidth/2); }

  // ---- the click -----------------------------------------------------------
  // A short burst of decaying noise through a bandpass: a wooden tick, not a
  // beep. Built once, on the first gesture, because a page may not open an
  // AudioContext before the reader has touched it.
  var ac=null, noise=null;
  function audio(){
    if(ac||calm.matches) return;
    var C=window.AudioContext||window.webkitAudioContext; if(!C) return;
    ac=new C();
    var n=Math.floor(ac.sampleRate*0.03), b=ac.createBuffer(1,n,ac.sampleRate), d=b.getChannelData(0);
    for(var i=0;i<n;i++) d[i]=(Math.random()*2-1)*Math.pow(1-i/n,7);
    noise=b;
  }
  function tick(speed){
    if(!ac||!noise) return;
    if(ac.state==='suspended') ac.resume();
    var s=ac.createBufferSource(); s.buffer=noise;
    s.playbackRate.value=0.85+Math.min(0.5,speed*0.25);
    var f=ac.createBiquadFilter(); f.type='bandpass'; f.frequency.value=1900; f.Q.value=1.1;
    var g=ac.createGain(); g.gain.value=0.05+Math.min(0.05,speed*0.03);
    s.connect(f); f.connect(g); g.connect(ac.destination);
    s.start();
  }

  // ---- the loop ------------------------------------------------------------
  // One animation loop drives everything that moves: the throw after a drag,
  // the glide onto a detent, and the flick of the glass as each sign passes.
  // Two loops writing scrollLeft is how this kind of thing starts stuttering.
  // scrollLeft reads back as a whole number. An animation that adds a fraction
  // of the remaining distance each frame therefore STOPS DEAD once that fraction
  // rounds to nothing, and this one parked four pixels short of the detent every
  // single time. The position is kept here as a float and written out each frame.
  var raf=0, last=0, pos=0, vel=0, flick=0, armed=false,
      goal=null, from=0, t0=0, dur=0;
  function run(){ if(!raf) raf=requestAnimationFrame(loop); }
  function sync(){ pos=track.scrollLeft; }
  var aim=-1;                                         // the detent being glided to
  function glide(i){
    aim=Math.max(0,Math.min(mid.length-1,i));
    sync(); from=pos; goal=Math.round(stop(aim)); t0=0;
    dur=Math.max(170,Math.min(430,170+Math.abs(goal-from)*1.1));
    run();
  }
  function put(x){
    var max=track.scrollWidth-track.clientWidth;
    pos=Math.max(0,Math.min(max,x));
    track.scrollLeft=pos;
    return pos!==x;                                   // true if it hit an end
  }
  function loop(ts){
    raf=0;
    var dt=last?Math.min(40,ts-last):16; last=ts;
    var busy=false;
    // while a hand is on it the hand is the only thing that moves it; the loop
    // still runs, but only to spring the glass back
    if(down){ }
    else if(goal!==null){
      if(!t0) t0=ts;
      var u=Math.min(1,(ts-t0)/dur), e=1-Math.pow(1-u,3);
      put(from+(goal-from)*e);
      if(u>=1) goal=null; else busy=true;
    }
    else if(Math.abs(vel)>0.04){
      if(put(pos-vel*dt)) vel=0;
      else vel*=Math.pow(0.0012,dt/1000);
      if(Math.abs(vel)<=0.04){ vel=0; glide(here()); }
      busy=true;
    }
    if(flick!==0){
      flick*=Math.pow(0.0009,dt/1000);
      if(Math.abs(flick)<0.04) flick=0;
      glass.style.transform=flick?'rotate('+flick.toFixed(2)+'deg)':'';
      busy=busy||flick!==0;
    }
    draw();
    if(busy) run(); else last=0;
  }

  function draw(){
    var p=track.scrollLeft+track.clientWidth/2;
    mag.style.transform='translate('+(lens.clientWidth/2-M*p)+'px,-50%) scale('+M+')';
    var i=nearest(p);
    if(i!==cur){
      var was=cur;
      cur=i;
      capw.textContent=items[i].querySelector('b').textContent;
      capc.textContent=items[i].querySelector('span').textContent;
      prev.disabled=(i===0); next.disabled=(i===mid.length-1);
      if(armed&&was>=0){                              // a sign has passed the glass
        var sp=Math.abs(vel);
        tick(sp);
        if(!calm.matches){ flick=(i>was?-1:1)*(2.2+Math.min(1.8,sp*0.8)); run(); }
      }
    }
  }

  var opened=false;
  function layout(){
    // enough padding at each end that the FIRST and LAST signs can reach the
    // middle; taken from those two signs, because they are not the same width
    // as each other and neither is the width the CSS floor happens to be
    var half=track.clientWidth/2;
    strip.style.setProperty('--padl',(half-items[0].offsetWidth/2)+'px');
    strip.style.setProperty('--padr',(half-items[items.length-1].offsetWidth/2)+'px');
    var x0=rail.getBoundingClientRect().left;
    mid=items.map(function(el){var r=el.getBoundingClientRect();return r.left-x0+r.width/2;});
    if(!opened&&mid.length){opened=true;
      track.scrollLeft=stop(+strip.dataset.open||0);}
    cur=-1; draw();
  }

  // ---- input ---------------------------------------------------------------
  var nudge=0;
  track.addEventListener('scroll',function(){ if(!raf) { draw(); rest(); } },{passive:true});
  function rest(){                                    // settle after a native throw
    clearTimeout(nudge);
    nudge=setTimeout(function(){
      if(!down&&goal===null&&Math.abs(vel)<=0.04){ armed=true; glide(here()); }
    },130);
  }
  window.addEventListener('resize',layout);

  function step(d){ audio(); armed=true; vel=0; glide((goal!==null?aim:here())+d); }
  prev.addEventListener('click',function(){step(-1);});
  next.addEventListener('click',function(){step(1);});
  track.addEventListener('keydown',function(e){
    if(e.key==='ArrowRight'){step(1);e.preventDefault();}
    else if(e.key==='ArrowLeft'){step(-1);e.preventDefault();}
  });

  // Mouse drag with a throw. A touch already scrolls the box natively and with
  // the platform's own momentum, so it is left alone and only settled at the end;
  // handling it here as well moved the strip at twice the speed of the finger.
  var down=false,x0=0,s0=0,px=0,pt=0;
  track.addEventListener('pointerdown',function(e){
    if(e.pointerType==='touch'||e.button) return;
    audio(); armed=true;
    down=true; vel=0; goal=null; sync();
    x0=px=e.clientX; s0=track.scrollLeft; pt=e.timeStamp;
    track.classList.add('grabbing'); track.setPointerCapture(e.pointerId);
  });
  track.addEventListener('pointermove',function(e){
    if(!down) return;
    var dt=e.timeStamp-pt;
    if(dt>0){ var v=(e.clientX-px)/dt; vel=Math.max(-4,Math.min(4,vel*0.7+v*0.3)); px=e.clientX; pt=e.timeStamp; }
    put(s0-(e.clientX-x0));
    draw(); e.preventDefault();
  });
  function release(e){
    if(!down) return;
    down=false; track.classList.remove('grabbing');
    if(e&&e.timeStamp-pt>90) vel=0;                   // let go after a pause: no throw
    sync();
    if(Math.abs(vel)<=0.04){ vel=0; glide(here()); } else run();
  }
  track.addEventListener('pointerup',release);
  track.addEventListener('pointercancel',release);
  track.addEventListener('dragstart',function(e){e.preventDefault();});
  track.addEventListener('touchstart',function(){audio();armed=true;},{passive:true});

  layout();
  if(document.fonts&&document.fonts.ready) document.fonts.ready.then(layout);
})();
</script>"""


def page_index(fig, summary, ktn, newpara, tiers, nfolio, sg, rows, pl):
    tier_line = ("readings " + "   ".join(f"{t} {tiers.get(t, 0):,}" for t in ("A", "B", "C", "D"))
                 + f"   =  {sum(tiers.get(t, 0) for t in ('A', 'B', 'C', 'D')):,}"
                 + f"\nrestorations in brackets, counted as a reading nowhere   {tiers.get('G', 0):,}")
    # The page count is read off the print PDF on the SHELF, never typed. The
    # shelf PDF is still built -- it is what goes to KDP -- it is just not
    # served from the site any more, so this reads the shelf copy, not a
    # published one.
    pages_note = ""
    try:
        import subprocess
        info = subprocess.run(["pdfinfo", "/opt/publish-app/data/u1/books/20260921-052535-r0hc/print.pdf"],
                              capture_output=True, text=True).stdout
        m = re.search(r"Pages:\s+(\d+)", info)
        if m:
            pages_note = f" · {m.group(1)} pages"
    except Exception:
        pass
    shot = ""
    if pl:
        x = pl[min(2, len(pl) - 1)]
        shot = (f'<figure class="shot"><img src="/rohonc/plates/{html.escape(x["file"])}" '
                f'alt="{html.escape(x["folio"])} redrawn" loading="lazy">'
                f'<figcaption>{html.escape(x["caption"])} Redrawn from the manuscript\'s own '
                f'drawing; not a reproduction.</figcaption></figure>')
    intro_html = paras("intro").replace("<p>", '<p class="dc">', 1)
    cover_blurb = paras("cover_blurb")
    body = f"""
<div class="hero">
  <div class="blurb">{intro_html}
    <div class="acts"><a class="go" href="/read/rohonc.php">Read it here</a>
      <a href="/rohonc/book/the-rohonc-codex.epub" download>EPUB</a>
      <a href="https://www.amazon.com/dp/B0HKQCWV2S" rel="noopener">Read on Kindle</a></div>
    <p class="sz">All {nfolio} folios{pages_note} · the translation and the evidence in one volume.</p>
  </div>
  <figure class="bk"><button class="book-peek" id="book-peek" type="button" aria-haspopup="dialog" aria-controls="book-blurb">
    <img src="/rohonc/img/book3d.png" alt="The Rohonc Codex, the printed edition" width="576" height="900">
    <span class="book-peek-note">Turn it over</span>
  </button></figure>
</div>
<dialog class="book-modal" id="book-blurb" aria-labelledby="book-blurb-title">
  <form method="dialog"><button class="modal-close" aria-label="Close" value="close">×</button></form>
  <h2 id="book-blurb-title">The back of the book</h2>
  {cover_blurb}
  <div class="acts"><a class="go" href="/read/rohonc.php">Read it here</a>
    <a href="https://www.amazon.com/dp/B0HKQCWV2S" rel="noopener">Read on Kindle</a></div>
</dialog>
<script>
(function(){{
  var opener=document.getElementById('book-peek');
  var dialog=document.getElementById('book-blurb');
  if(!opener||!dialog) return;
  opener.addEventListener('click',function(){{
    if(typeof dialog.showModal==='function') dialog.showModal();
    else dialog.setAttribute('open','');
  }});
  dialog.addEventListener('click',function(e){{
    if(e.target!==dialog) return;
    if(typeof dialog.close==='function') dialog.close();
    else dialog.removeAttribute('open');
  }});
  dialog.querySelector('.modal-close').addEventListener('click',function(){{
    if(typeof dialog.close!=='function') dialog.removeAttribute('open');
  }});
}})();
</script>
{strip_html(rows, sg)}
<p class="nof">{html.escape(COPY["strip_note"].strip())} Drag it, or use the arrows: the glass magnifies whatever sign passes under it and names this project's reading of that sign and its code. The outlines are drawn from Király and Tokai's own font. <a href="/rohonc/script.html">More about the script →</a></p>
{shot}

<h2>How far it reads</h2>
{how_far(fig)}
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
{summary_table(summary)}
<p>What each test asked is on the <a href="/rohonc/tests.html">tests page</a>. The saved runs are in the <a href="/rohonc/data.html">data</a>.</p>

<h2>What is here</h2>
<div class="cards">
<a class="card" href="/rohonc/script.html"><b>The script</b><span>{html.escape(COPY["card_script"].strip())}</span></a>
<a class="card" href="/rohonc/atlas.html"><b>Atlas</b><span>{html.escape(COPY["card_atlas"].strip())}</span></a>
<a class="card" href="/rohonc/reading.html"><b>Summary of the gloss</b><span>{html.escape(COPY["card_reading"].strip())}</span></a>
<a class="card" href="/rohonc/dictionary.html"><b>Dictionary</b><span>{html.escape(COPY["card_dictionary"].strip())}</span></a>
<a class="card" href="/rohonc/tests.html"><b>Tests</b><span>{html.escape(COPY["card_tests"].strip())}</span></a>
<a class="card" href="/rohonc/method.html"><b>Method</b><span>{html.escape(COPY["card_method"].strip())}</span></a>
<a class="card" href="/rohonc/code.html"><b>The programs</b><span>Every program behind the readings, as plain text, grouped by what it does.</span></a>
<a class="card" href="/rohonc/data.html"><b>Data</b><span>{html.escape(COPY["card_data"].strip())}</span></a>
</div>

<h2>The edition</h2>
{paras("edition")}

<h2>Credit and position</h2>
{paras("credit")}
<p>Their site: <a href="https://rechnitzer-kodex.hu/" rel="noopener">rechnitzer-kodex.hu</a>. Citations owed and the terms of every source are under <a href="/rohonc/sources.html">Sources</a>.</p>
{STRIP_JS}
"""
    return shell("index", "Overview",
                 "The Rohonc Codex read into English on Király and Tokai's dictionary, extended and tested: the reading, the dictionary, fifteen tests, the method and all the data.",
                 body, strip_css())


def page_reading(order, eng):
    parts = ['<h1>An English summary of the gloss</h1>',
             paras("reading_lead", "lead"),
             '<p class="acts"><a class="go" href="/read/rohonc.php">Open the book</a></p>',
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
    return shell("reading", "An English summary of the gloss",
                 f"One paragraph of English for each of the {len(order)} written pages of the Rohonc Codex, summarising the gloss. "
                 "The full text, the narrative and the complete gloss, is in the book.",
                 "\n".join(parts)), n


def page_dictionary(about, rows, ktn):
    tiers = {}
    for r in rows:
        tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1
    # The top line must not lump what the legend separates: tier G is a bracketed
    # restoration, counted as a reading nowhere, and adding it to the total would
    # let one number say the opposite of the legend three lines below it.
    read = sum(tiers.get(t, 0) for t in ("A", "B", "C", "D"))
    counts = (f"readings        {read:>6,}     "
              + "   ".join(f"{t} {tiers.get(t, 0):,}" for t in ("A", "B", "C", "D"))
              + f"\nrestorations    {tiers.get('G', 0):>6,}     bracketed, counted as a reading nowhere"
              + f"\nwithdrawn       {tiers.get('withdrawn', 0):>6,}     made, then refused, and kept with the reason")
    body = f"""
<h1>The dictionary of added readings</h1>
{paras("dictionary_lead", "lead")}
<p>From the file itself: {html.escape(about)}</p>
<div class="tiers"><b>A</b> fits every occurrence checked, or is proved by an identical formula or a numeral &nbsp;·&nbsp; <b>B</b> fits most &nbsp;·&nbsp; <b>C</b> and <b>D</b> read from one passage, nothing in the book able to refuse them &nbsp;·&nbsp; <b>G</b> a guess, printed in brackets and never counted &nbsp;·&nbsp; <b>withdrawn</b> a reading that was made and then refused, kept with the reason</div>
<div class="fig">{counts}</div>
<div class="tools">
  <input id="q" type="search" placeholder="search a reading or a sign" autocomplete="off">
  <button data-t="" class="on">All</button><button data-t="A">A</button><button data-t="B">B</button><button data-t="C">C</button><button data-t="D">D</button><button data-t="G">G</button><button data-t="withdrawn">Withdrawn</button>
  <span class="n" id="n"></span>
</div>
<div class="tw"><table class="dict"><thead><tr><th>Sign</th><th>Reading</th><th>Tier</th><th>Times</th><th>Evidence</th></tr></thead><tbody id="tb"></tbody></table></div>
<p>The file itself, every entry with its full evidence, is in the repository: <a href="https://github.com/styopr613/rohonc-codex">github.com/styopr613/rohonc-codex</a>.</p>
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


def page_script(sample, pl, ktn):
    rows = []
    for n, line in sample:
        cells = []
        for w in line.split():
            cls = "m" if ("-" in w or w.endswith("*") or w.startswith("[") or "~" in w) else ""
            cells.append(f'<span class="{cls}">{html.escape(w)}</span>' if cls else html.escape(w))
        rows.append(f'{n.rjust(3)}  ' + " ".join(cells))
    gloss = "<br>".join(rows)
    plate_html = "".join(
        f'<figure><img src="/rohonc/plates/{html.escape(x["file"].replace(".png", ".jpg"))}" '
        f'alt="folio {html.escape(x["folio"])} redrawn" loading="lazy">'
        f'<figcaption>{html.escape(x["caption"])}</figcaption></figure>' for x in pl)
    body = f"""
<h1>The script</h1>
{paras("script_intro", "lead")}

<h2>One sign at a time</h2>
{paras("script_signs")}
<div class="demo">
  <div class="sign" id="sg">
    <span class="code" id="sgcode">…</span><span class="glyph" id="sgglyph" hidden></span>
    <span class="gl" id="sggl"></span>
    <span class="meta" id="sgmeta"></span><p class="ev" id="sgev"></p>
  </div>
  <div class="ctl">
    <button id="sgnext">Another sign</button>
    <button data-t="" class="on">Any tier</button><button data-t="A">A</button><button data-t="B">B</button><button data-t="C">C</button><button data-t="G">G</button>
    <span class="sp" id="sgn"></span>
  </div>
</div>
<p id="fontnote" class="nof">The signs are drawn in Király and Tokai's own font. This page does not host it; if you install it from <a href="https://rechnitzer-kodex.hu/" rel="noopener">their site</a> the drawn sign appears here beside its code.</p>

<h2>A sign can be a whole phrase</h2>
{paras("script_phrases")}
<div class="demo"><h3>folio 137v</h3>
  <div class="parts">
    <div class="pc"><b>you</b><span>569 · 932 times</span></div>
    <span class="op">+</span>
    <div class="pc"><b>Mary</b><span>607 · 59 times alone</span></div>
    <span class="op">=</span>
    <div class="pc"><b>you-Mary</b><span>569607 · one sign</span></div>
  </div>
  <p class="nof" style="margin:12px 0 0">Both halves are in their dictionary. The joined sign is not, and it is written without a space. Reading signs apart this way produced 1,282 readings their dictionary does not contain.</p>
</div>

<h2>The numerals</h2>
{paras("script_numerals")}
<div class="demo"><h3>checked against a number the source supplies</h3>
<div class="sums">
ten·ten·ten·ten &nbsp;=&nbsp; 10 + 10 + 10 + 10 &nbsp;=&nbsp; <b>forty</b> &nbsp;&nbsp;the forty days and forty nights<br>
two·two·ten &nbsp;=&nbsp; (2 + 2) × 10 &nbsp;=&nbsp; <b>forty</b> &nbsp;&nbsp;the forty days of rain<br>
six·two &nbsp;=&nbsp; 6 + 2 &nbsp;=&nbsp; <b>eight</b> &nbsp;&nbsp;the circumcision on the eighth day<br>
six·six &nbsp;=&nbsp; 6 + 6 &nbsp;=&nbsp; <b>twelve</b> &nbsp;&nbsp;the twelve apostles
</div></div>

<h2>The marks</h2>
{paras("script_marks")}
<div class="demo"><h3>folio 004v, lines {sample[0][0]} and {sample[-1][0]}, as this edition prints them</h3>
<div class="gloss">{gloss}</div>
<p class="nof" style="margin:12px 0 0">Underlined words carry a mark. <b>ten-ten-ten-ten</b> is the numeral above, read as the four signs it is built from. <b>hide_oneself-angel</b> is the fallen angel, one sign read as the smaller signs inside it. A <b>~</b> is a spelling their own apparatus files as a variant, and <b>*</b> is a word read from one passage only.</p>
</div>

<h2>The drawings</h2>
{paras("script_plates")}
<div class="plates">{plate_html}</div>

<script>
(function(){{
var ROWS=[],T="",cur=null;
var q=function(i){{return document.getElementById(i);}};
function grp(c){{return c.replace(/(...)/g,'$1 ').trim();}}
function pua(c){{var o="";for(var i=0;i+3<=c.length;i+=3){{o+=String.fromCharCode(0xE000+parseInt(c.substr(i,3),16));}}return o;}}
var FONT=false;
try{{
  var cv=document.createElement('canvas').getContext('2d'), t=pua("060270910");
  cv.font='34px serif'; var a=cv.measureText(t).width;
  cv.font='34px "Rohonc Codex", serif'; var b=cv.measureText(t).width;
  FONT=Math.abs(a-b)>0.5;   // fonts.check() answers true for any family that falls back, so measure instead
}}catch(e){{}}
if(FONT){{q('fontnote').hidden=true;}}
function pick(){{
  var pool=ROWS.filter(function(r){{return !T||r.tier===T;}});
  if(!pool.length){{return;}}
  var r=pool[Math.floor(Math.random()*pool.length)]; cur=r;
  q('sgcode').textContent=grp(r.code);
  if(FONT){{var g=q('sgglyph'); g.textContent=pua(r.code); g.hidden=false;}}
  q('sggl').textContent=r.gloss;
  q('sgmeta').textContent='tier '+r.tier+' · stands '+r.n+(r.n===1?' time':' times')+' in the book';
  q('sgev').textContent=r.evidence||'';
  q('sgn').textContent=pool.length.toLocaleString()+' signs in this tier';
}}
q('sgnext').addEventListener('click',pick);
Array.prototype.forEach.call(document.querySelectorAll('.ctl button[data-t]'),function(b){{
  b.addEventListener('click',function(){{
    Array.prototype.forEach.call(document.querySelectorAll('.ctl button[data-t]'),function(x){{x.classList.remove('on');}});
    b.classList.add('on'); T=b.getAttribute('data-t'); pick();}});}});
fetch('/rohonc/data/dictionary.json').then(function(r){{return r.json();}}).then(function(j){{
  ROWS=j.filter(function(r){{return r.tier!=='withdrawn'&&r.gloss;}}); pick();}})
 .catch(function(){{q('sgcode').textContent='The dictionary file did not load.';}});
}})();
</script>
"""
    return shell("script", "The script",
                 "How the Rohonc Codex's writing works: signs that stand for words and phrases, numerals that add and multiply, the marks this edition uses, and the manuscript's drawings redrawn.",
                 body)


def runtime():
    """What the programs run on, measured at build time, never typed."""
    ver = numpy = None
    try:
        m = re.search(r"^version\s*=\s*(\S+)", read(os.path.join(ROOT, ".venv", "pyvenv.cfg")), re.M)
        ver = m.group(1) if m else None
    except OSError:
        pass
    try:
        sp = glob.glob(os.path.join(ROOT, ".venv", "lib", "python3*", "site-packages", "numpy-*.dist-info"))
        numpy = os.path.basename(sp[0]).split("-")[1].replace(".dist", "") if sp else None
    except Exception:
        pass
    return ver, numpy


def test_rows():
    """(number, label, question, programs, runs, docs) for every test in TESTS.md,
    from its heading and the backtick line under it."""
    txt = read(os.path.join(ROOT, "TESTS.md"))
    rows = []
    for m in re.finditer(r"^## (Test [^\n—]+?)\s*—\s*([^\n]+)\n\n?((?:`[^\n]*\n?)+)?", txt, re.M):
        label, asks, line = m.group(1).strip(), m.group(2).strip(), (m.group(3) or "")
        num = int(re.match(r"Test (\d+)", label).group(1))
        progs, runs, docs = [], [], []
        for tok in re.findall(r"`([^`]+)`", line):
            for part in re.split(r"\s*,\s*", tok):
                part = part.strip()
                if part.endswith(".py"):
                    progs.append(os.path.basename(part))
                elif part.endswith(".md"):
                    docs.append(part)
                elif part.endswith(".txt") or part.startswith("_"):
                    runs.append(part)
        full = []                      # "ktpos2.txt" and "_score.txt" are written short
        for r in runs:
            if r.startswith("_") and full:
                r = full[-1].replace(".txt", "") + r
            full.append(os.path.basename(r))
        rows.append((num, label, asks, progs, full, docs))
    rows.sort()
    return rows


def cited():
    """The programs and saved runs the results page names. Those are what is
    served; the rest of the harness comes with the repository."""
    progs, runs = set(), set()
    for _, _, _, p, r, _ in test_rows():
        progs.update(p); runs.update(r)
    return progs, runs


def crosswalk(out):
    """Test number -> the program that produced it -> the saved run. A script is
    linked when its text is published under /rohonc/code/, a run when it is under
    /rohonc/data/runs/; anything else is named and not linked."""
    def plink(n):
        return f"<code>{html.escape(n)}</code>"
    def rlink(n):
        return html.escape(n)
    body = ""
    for n, label, asks, progs, runs, docs in test_rows():
        pr = ", ".join(plink(x) for x in progs) or "—"
        rn = ", ".join(rlink(x) for x in runs) + ("" if not docs else " · " + ", ".join(html.escape(d) for d in docs))
        body += f'<tr id="test-{n}"><th scope="row">{html.escape(label)}</th><td>{html.escape(asks)}</td><td>{pr}</td><td>{rn or "—"}</td></tr>'
    return ('<div class="tw"><table class="tests"><thead><tr><th>test</th><th>what it asks</th><th>program</th>'
            '<th>saved run</th></tr></thead><tbody>' + body + "</tbody></table></div>")


def page_code(out):
    ver, numpy = runtime()
    stack = "Python" + (f" {ver}" if ver else "") + (f" with numpy {numpy}" if numpy else "") + " and the standard library"
    body = ["<h1>The programs</h1>", paras("code_lead", "lead"),
            "<h2>What they run on</h2>",
            f"<p>{html.escape(stack)}, from the repository root, as <code>python3 harness/&lt;program&gt;.py</code>. "
            "Every test program names its test number and states its bar in its first lines, before any result. "
            "Three inputs are not in this repository: the anonymous open transcription of 2014, <code>latest.txt</code>, "
            "recoverable from the Internet Archive at the address on the <a href=\"/rohonc/sources.html\">Sources</a> page; "
            "Király and Tokai's dictionary, which is their published work and is not served here; and the reference corpora "
            "the folios are read against, all public-domain texts named under Sources and fetched from Project Gutenberg and "
            "archive.org. With those three in place every saved run below can be reproduced.</p>",
            "<p>From the repository root, <code>python3 harness/reproduce_tests.py</code> verifies the exact input "
            "files, runs every published result twice under different Python hash seeds, and requires byte-for-byte "
            "agreement with the saved runs. The blind and outside-reader tests score their committed replies without "
            "making network requests. Test 4 is explicitly blocked and has no result to reproduce.</p>",
            "<h2>Which program made which number</h2>",
            "<p>Every test on the <a href=\"/rohonc/tests.html\">checked-results page</a> names its program, and each program "
            "names its saved run. This table is read out of the tests document at build time.</p>",
            crosswalk(out),
            '<p>The programs and every saved run are in the repository, with their history: <a href="https://github.com/styopr613/rohonc-codex">github.com/styopr613/rohonc-codex</a>. Nothing is served '
            "from here, so nothing on this page can point at a copy that has gone stale.</p>"]
    return shell("code", "The programs",
                 "Which program produced each number on the checked-results page, what they run on, and every program in the harness as plain text.",
                 "\n".join(body))

ORDERS_REDACT = re.compile(r"/home/[\w-]+/[\w./-]*")


def page_corpus():
    """The books the codex was read against, one entry per book, from the
    provenance file: what it is, what it supplied, and where it can be read."""
    import ktcorpus
    body = ["<h1>The corpus</h1>",
            '<p class="lead">The codex is a compilation, and most of what its compiler wrote fits inside a small shelf of books. '
            "Every folio of the translation was read against the passage it retells, because an elliptical text does not become "
            "English on its own: the manuscript leads, and the source only ever says what one of its phrases means. "
            "This is that shelf. Every book on it is public domain, and each links to where it can be read.</p>",
            '<p>How each was fetched and under what terms is in the provenance file; the reading itself is in the '
            '<a href="/read/rohonc.php">book</a>, and every departure from these sources is named in its notes.</p>']
    for e in ktcorpus.entries():
        links = " · ".join(f'<a href="{html.escape(u)}" rel="noopener">{html.escape(l)}</a>' for l, u in e["links"])
        body.append(f'<h2 id="{html.escape(e["anchor"])}">{html.escape(e["name"])}</h2>')
        body.append(md(e["text"]))
        if links:
            body.append(f'<p class="nof">Read it: {links}</p>')
    return shell("corpus", "The corpus",
                 "The books the Rohonc Codex was read against: the Douay Bible, the Life of Adam and Eve, the Golden Legend, the apocryphal gospels, Barlaam, the Missal and the Office of Holy Week, Josephus, the play cycles; what each supplied and where to read it.",
                 "\n".join(body))


def page_orders():
    """METHOD.md, the file the next person works from, published as it is. It
    was written for an operator, not a reader, and that is left showing: the
    roughness is provenance, like the withdrawal entries. Local paths are the
    only thing in it that is nobody's business, and each is replaced by a
    visible mark; the count is measured, not typed."""
    raw = read(os.path.join(ROOT, "METHOD.md"))
    raw, n = ORDERS_REDACT.subn("[local path redacted]", raw)
    body = ('<h1>The standing orders</h1>'
            '<p class="lead">This is <code>METHOD.md</code>, the file the next person actually works '
            'from: what to do, in order, and the arithmetic of how much of the book is still unread. '
            'It is written for the operator and it is published unedited. '
            + (f'{n} local path{"s" if n != 1 else ""} {"are" if n != 1 else "is"} replaced by the mark '
               '<code>[local path redacted]</code>; nothing else is changed.' if n else 'Nothing in it is changed.')
            + ' The three earlier versions of its arithmetic that were wrong are kept on the page beside the right one, as it says.</p>'
            + '<div class="orders">' + md(raw) + '</div>')
    return shell("orders", "The standing orders",
                 "The project's own operating file, published whole and unedited: the loop for reading a sign, the standing orders, and the arithmetic of what is left.",
                 body)


def page_method():
    sl = items("method_steps")
    ml = items("method_mistakes_list")
    body = f"""
<h1>The method</h1>
{paras("method_intro", "lead")}

<h2>The loop, one sign at a time</h2>
{paras("method_loop")}
<ol class="steps">{sl}</ol>

<h2>The bar goes up before the run</h2>
{paras("method_bars")}

<h2>What cost the most time</h2>
{paras("method_mistakes")}
<ul class="steps">{ml}</ul>

<h2>The programs, and the orders</h2>
<p>The programs are listed at <a href="/rohonc/code.html">The programs</a>, as plain text. The file the next person actually works from is <a href="/rohonc/orders.html">the standing orders</a>, published whole and unedited: the loop, the orders, and the arithmetic of how much is still unread, with the three earlier versions of that arithmetic that were wrong kept beside the right one.</p>
"""
    return shell("method", "The method",
                 "How an unread sign is read and checked, the rule that the bar is declared before the run, and the mistakes that cost the most time.",
                 body)


# The book on the Read page is the same turning object the OONA 13 home page
# shows: a CSS box whose front, back and spine are real slices of the printed
# wrap (cut by ktspin.py into work/rohonc/spin-*.webp), drifting on a CSS
# animation until somebody grabs it. The geometry is read from the slices
# themselves, so a new trim or spine changes the box without touching this.
# No `filter` anywhere on the rotating subtree: a filter makes a containing
# block and flattens preserve-3d into a card. The floor ellipse is the shadow.
# THE SPINE IS LIT THE WAY THE STUDIO'S SNAPSHOT LIGHTS IT. Cover Maker's
# book3d.py draws no curl and no gradient: each face is a flat tone, the spine
# 0.82 of the front. That is the render on the hero. The home page's and Book
# Maker's ridge gradient (black .5 at the edges, a white band at the centre,
# stops in percent) is invisible on their dark art and paints stripes on a
# blank cream spine twice as wide; tried at full weight and at a quarter on
# 2026-09-23, both wrong. Now: a flat .18 over the spine and a 7px edge.
SPIN_FACES = ("front", "back", "spine")


def spin_geometry():
    from PIL import Image as _Im
    paths = {f: os.path.join(WORK, f"spin-{f}.webp") for f in SPIN_FACES}
    missing = [v for v in paths.values() if not os.path.isfile(v)]
    if missing:
        raise SystemExit("the book's faces are missing: " + " ".join(missing) + "\n   run: python3 ktspin.py")
    fw, fh = _Im.open(paths["front"]).size
    sw, sh = _Im.open(paths["spine"]).size
    return {"ratio": fh / fw, "spine": sw / fw, "fw": fw, "fh": fh, "sw": sw, "sh": sh}


def spin_css(g):
    return f"""<style>
.book3d-scene{{--bw:300px;--bh:calc(var(--bw)*{g['ratio']:.4f});--bt:calc(var(--bw)*{g['spine']:.4f});--bth:calc(var(--bw)*{g['spine']/2:.4f});
  perspective:1600px;display:flex;flex-direction:column;align-items:center;margin:2.2em auto 1.4em;padding-top:10px}}
.book3d{{position:relative;width:var(--bw);height:var(--bh);transform-style:preserve-3d;animation:book3d-spin 22s linear infinite;will-change:transform;
  cursor:grab;touch-action:pan-y;user-select:none;-webkit-user-select:none;-webkit-touch-callout:none}}
.book3d-scene:hover .book3d,.book3d-scene:focus-within .book3d{{animation-play-state:paused}}
.book3d img{{pointer-events:none;-webkit-user-drag:none;width:100%;height:100%;object-fit:cover;display:block}}
.book3d.is-manual{{animation:none;transform:rotateZ(-3deg) rotateX(8deg) rotateY(var(--spin,0deg))}}
.book3d.is-grabbed{{cursor:grabbing}}
.book3d:focus-visible{{outline:2px solid var(--rub);outline-offset:14px}}
@keyframes book3d-spin{{from{{transform:rotateZ(-3deg) rotateX(8deg) rotateY(0deg)}}to{{transform:rotateZ(-3deg) rotateX(8deg) rotateY(360deg)}}}}
.book3d .face{{position:absolute;backface-visibility:hidden}}
.book3d .b-front,.book3d .b-back{{inset:0;overflow:hidden;background:#e8dcc4}}
.book3d .b-front{{transform:translateZ(var(--bth));border-radius:2px 7px 7px 2px}}
.book3d .b-back{{transform:rotateY(180deg) translateZ(var(--bth));border-radius:7px 2px 2px 7px}}
.book3d .b-front::after,.book3d .b-back::after{{content:'';position:absolute;inset:0;border-radius:inherit;pointer-events:none}}
.book3d .b-front::after{{background:linear-gradient(90deg,rgba(0,0,0,.30) 0,rgba(0,0,0,.10) 6px,rgba(255,255,255,.12) 14px,rgba(255,255,255,0) 30px,rgba(0,0,0,0) calc(100% - 20px),rgba(0,0,0,.08) 100%)}}
.book3d .b-back::after{{background:linear-gradient(270deg,rgba(0,0,0,.30) 0,rgba(0,0,0,.10) 6px,rgba(255,255,255,.12) 14px,rgba(255,255,255,0) 30px,rgba(0,0,0,0) calc(100% - 20px),rgba(0,0,0,.08) 100%)}}
.book3d .b-spine{{top:0;left:0;width:var(--bt);height:100%;transform:translateX(calc(var(--bth)*-1)) rotateY(-90deg);border-radius:3px;overflow:hidden;background:#e8dcc4}}
.book3d .b-spine::after{{content:'';position:absolute;inset:0;pointer-events:none;background:linear-gradient(90deg,rgba(0,0,0,.30) 0,rgba(0,0,0,0) 7px,rgba(0,0,0,0) calc(100% - 7px),rgba(0,0,0,.30) 100%),linear-gradient(rgba(0,0,0,.18),rgba(0,0,0,.18))}}
.book3d .b-pages,.book3d .b-head{{background-color:#f6f1e4}}
.book3d .b-pages{{top:2px;right:0;width:var(--bt);height:calc(100% - 4px);transform:translateX(var(--bth)) rotateY(90deg);background-image:repeating-linear-gradient(90deg,#f6f1e4 0 2px,#d9cfb8 2px 3px)}}
.book3d .b-pages::after{{content:'';position:absolute;inset:0;pointer-events:none;background:linear-gradient(90deg,rgba(74,58,32,.30) 0,rgba(74,58,32,.08) 30%,rgba(74,58,32,.10) 70%,rgba(74,58,32,.32) 100%)}}
.book3d .b-head{{top:0;left:2px;width:calc(100% - 4px);height:var(--bt);transform:translateY(calc(var(--bth)*-1)) rotateX(90deg);background-image:repeating-linear-gradient(0deg,#f6f1e4 0 2px,#ddd4bf 2px 3px)}}
.book3d .b-head::after{{content:'';position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(74,58,32,.10),rgba(74,58,32,.22))}}
.book3d-floor{{width:var(--bw);height:calc(var(--bw)*.085);margin:calc(var(--bw)*-.02) auto 0;border-radius:50%;background:radial-gradient(closest-side,#00000045,#00000018 55%,transparent)}}
.book3d-note{{text-align:center;color:var(--soft);font-style:italic;font-size:15.5px;margin:0 0 1.6em}}
@media(max-width:700px){{.book3d-scene{{--bw:220px}}}}
@media(prefers-reduced-motion:reduce){{.book3d{{animation:none;transform:rotateZ(-3deg) rotateX(8deg) rotateY(-26deg)}}}}
</style>"""


def _v(name):
    """A content stamp on the face URLs. Cloudflare caches images by extension
    and served the previous jacket for hours after the faces were re-cut on
    2026-09-23; a new file must get a new URL."""
    import hashlib
    return hashlib.sha256(open(os.path.join(WORK, name), "rb").read()).hexdigest()[:8]


def spin_html(g):
    v = {f: _v(f"spin-{f}.webp") for f in SPIN_FACES}
    return f"""<div class="book3d-scene">
  <div class="book3d" id="book3d" tabindex="0" role="img" aria-label="The Rohonc Codex paperback, turning. Drag it, or use the left and right arrow keys, to turn it yourself.">
    <div class="face b-front"><img draggable="false" src="/rohonc/img/spin-front.webp?v={v['front']}" width="{g['fw']}" height="{g['fh']}" alt="The Rohonc Codex, front cover"></div>
    <div class="face b-back" aria-hidden="true"><img draggable="false" src="/rohonc/img/spin-back.webp?v={v['back']}" width="{g['fw']}" height="{g['fh']}" alt=""></div>
    <div class="face b-spine" aria-hidden="true"><img draggable="false" src="/rohonc/img/spin-spine.webp?v={v['spine']}" width="{g['sw']}" height="{g['sh']}" alt=""></div>
    <div class="face b-pages" aria-hidden="true"></div>
    <div class="face b-head" aria-hidden="true"></div>
  </div>
  <div class="book3d-floor" aria-hidden="true"></div>
</div>
<p class="book3d-note">The printed book. Drag it to turn it.</p>"""


# Grab-and-turn, ported from the OONA 13 home page. The cover drifts on the
# CSS animation; the first grab takes the angle over FROM THE ANIMATION'S
# CURRENT TIME so it never jumps, and keeps the same idle rate afterwards so a
# release eases back into the drift instead of stopping dead.
SPIN_JS = """<script>
(function(){
  var book = document.getElementById("book3d"); if (!book) return;
  var SPIN_MS = 22000, SENS = 0.6;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var IDLE = reduce ? 0 : 360 / (SPIN_MS / 1000);
  var angle = 0, vel = 0, raf = 0, last = 0, manual = false, dragging = false;
  var lastX = 0, lastMove = 0, onScreen = true, resting = false, look = false;
  function apply(){ book.style.setProperty("--spin", angle.toFixed(2) + "deg"); }
  function goManual(){
    if (manual) return;
    var anim = book.getAnimations ? book.getAnimations()[0] : null;
    var ct = anim && typeof anim.currentTime === "number" ? anim.currentTime : null;
    angle = ct !== null ? ((ct % SPIN_MS) / SPIN_MS) * 360 : -26;
    manual = true; book.classList.add("is-manual"); apply();
    last = performance.now(); if (!raf) raf = requestAnimationFrame(tick);
  }
  function tick(now){
    raf = 0;
    var dt = Math.min(0.05, (now - last) / 1000); last = now;
    if (!dragging) {
      var want = look ? 0 : IDLE;
      vel += (want - vel) * Math.min(1, dt * 1.6);
      angle += vel * dt; apply();
    }
    resting = !dragging && Math.abs(vel) < 0.05 && (look || IDLE === 0);
    if (onScreen && !document.hidden && !resting) raf = requestAnimationFrame(tick);
  }
  function wake(){ if (manual && !raf && onScreen) { last = performance.now(); raf = requestAnimationFrame(tick); } }
  book.addEventListener("pointerdown", function(e){
    if (e.button !== undefined && e.button !== 0) return;
    goManual(); dragging = true; vel = 0; lastX = e.clientX; lastMove = performance.now();
    book.setPointerCapture(e.pointerId); book.classList.add("is-grabbed");
  });
  book.addEventListener("pointermove", function(e){
    if (!dragging) return;
    var now = performance.now(), dx = e.clientX - lastX, dt = Math.max(8, now - lastMove) / 1000;
    angle += dx * SENS; vel = (dx * SENS) / dt; lastX = e.clientX; lastMove = now; apply(); e.preventDefault();
  });
  function up(e){
    if (!dragging) return;
    dragging = false; book.classList.remove("is-grabbed");
    if (performance.now() - lastMove > 120) vel = 0;
    if (e.type === "pointercancel") vel = 0;
    vel = Math.max(-720, Math.min(720, vel));
    last = performance.now(); if (!raf) raf = requestAnimationFrame(tick);
    try { book.releasePointerCapture(e.pointerId); } catch (_) {}
  }
  book.addEventListener("pointerup", up); book.addEventListener("pointercancel", up);
  book.addEventListener("keydown", function(e){
    var d = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0; if (!d) return;
    goManual(); vel = 0; angle += d * 15; apply(); last = performance.now();
    if (!raf) raf = requestAnimationFrame(tick); e.preventDefault();
  });
  book.addEventListener("dragstart", function(e){ e.preventDefault(); });
  var scene = book.parentElement;
  scene.addEventListener("pointerenter", function(){ look = true; wake(); });
  scene.addEventListener("pointerleave", function(){ look = false; wake(); });
  book.addEventListener("focus", function(){ look = true; wake(); });
  book.addEventListener("blur", function(){ look = false; wake(); });
  if (window.IntersectionObserver) new IntersectionObserver(function(en){
    onScreen = en[0].isIntersecting; if (onScreen && manual && !raf) { last = performance.now(); raf = requestAnimationFrame(tick); }
  }, {rootMargin: "80px"}).observe(book);
})();
</script>"""


def page_read():
    """No second reader. The book opens in the OONA reader at /read/rohonc.php,
    the same one the Free Library uses, with its own notes, contents and type
    controls. This page is the door to it, and the printed book turns on it."""
    g = spin_geometry()
    body = ("<h1>Read it here</h1>"
            + paras("read_lead", "lead")
            + '<p class="acts"><a class="go" href="/read/rohonc.php">Open the book</a> '
              '<a href="/rohonc/book/the-rohonc-codex.epub" download>Download EPUB</a> '
              '<a href="https://www.amazon.com/dp/B0HKQCWV2S" rel="noopener">Read on Kindle</a></p>'
            + spin_css(g) + spin_html(g) + SPIN_JS)
    return shell("read", "Read it here",
                 "The whole Rohonc Codex edition in the OONA reader: the translation and all 441 written pages with their marked lines.",
                 body)


def docs_html():
    return "".join(
        (f'<li><b><a href="/rohonc/orders.html">{html.escape(t)}</a></b> <span class="nof">{html.escape(d)} Published whole.</span></li>'
         if fn == "METHOD.md" else
         f'<li><b>{html.escape(t)}</b> <span class="nof">{html.escape(d)}</span></li>')
        for fn, t, d in DOCS)


def page_tests(summary):
    body = f"""
<h1>Are the readings true?</h1>
{paras("tests_intro", "lead")}
{summary_table(summary)}
{paras("tests_after")}
{paras("tests_note")}
<p>The saved run behind every line is in the <a href="/rohonc/data.html">data</a>, one
file per test, each stating its bar at the top. The reviewers' own specifications are
there too, quoted whole: <a href="/rohonc/outside-gemini.html">Gemini 2.5 Pro</a> and
<a href="/rohonc/outside-grok.html">Grok 4.7</a>. The programs are at
<a href="/rohonc/code.html">The programs</a>.</p>
"""
    return shell("tests", "Are the readings true?",
                 "Fifteen tests of the Rohonc readings, every bar declared before the run and none moved, with the failures kept beside the passes.",
                 body)


def citations():
    """The citations owed, read out of DATA_PROVENANCE.md. They are facts with
    accents in them, and a model asked to copy them back drops one."""
    txt = read(os.path.join(ROOT, "DATA_PROVENANCE.md"))
    m = re.search(r"## Citations owed in any write-up\n(.*?)(?=\n## |\Z)", txt, re.S)
    if not m:
        raise SystemExit("ktsite: DATA_PROVENANCE.md lost its citations")
    out = []
    for blk in re.split(r"\n(?=- )", m.group(1).strip()):
        c = " ".join(blk.lstrip("- ").split())
        if c:
            out.append(c.split(" -- ")[0])
    return out


def notes_sources():
    """The texts the endnotes read but did not fetch, from ktcorpus.note_sources()
    (DATA_PROVENANCE.md section 6): name, and the body with its addresses as links."""
    import ktcorpus
    out = []
    for e in ktcorpus.note_sources():
        body = html.escape(e["text"])
        body = re.sub(r"`(https?://[^`]+)`", lambda k: f'<a href="{k.group(1)}" rel="noopener">{re.sub(r"^https?://", "", k.group(1)).split("/")[0]}</a>', body)
        body = re.sub(r"\*(.+?)\*", r"<i>\1</i>", body)
        out.append((e["name"], body))
    return out



def page_finds():
    """Discovering the work: the readings of the facts the source check turned
    up, and the end-of-world count. ONE text: the book's appendix "What the
    sources turned up" in ktbook.back_matter(), rendered here, so the page and
    the book cannot drift."""
    import ktbook
    app = [a for a in ktbook.back_matter() if a["title"] == "What the sources turned up"]
    if not app:
        raise SystemExit("ktsite: the book has no appendix 'What the sources turned up'")
    # the appendix ends by pointing at this page; a page need not point at itself
    text = app[0]["text"].split("\n\nFinds after this printing")[0]
    body = f"""
<h1>Discovering the work</h1>
<p class="lead">Things the sources turned up that are readings of the facts rather than facts about the manuscript. They stand outside the endnotes for that reason, and each one says what is not known. The same text is printed in the book as the appendix "What the sources turned up".</p>
{md(text)}
<p>The facts these rest on are in the endnotes of Book One, and every text they cite is listed under <a href="/rohonc/sources.html">Sources</a>.</p>
"""
    return shell("finds", "Discovering the work",
                 "What reading the sources behind the Rohonc Codex turned up: the stolen cup's neighbours, Adam healed by the branch, Elijah at the fall of the angels, and the date the book gives the end of the world.",
                 body)

def page_atlas():
    """Maps and timelines of where the codex came out of. The plates are drawn
    by ktatlas.py from atlas.json and saved under work/rohonc/atlas/; this page
    only places them. Every date on them is in atlas.json with the line where it
    was read, and the list under the plates is generated from those lines."""
    adir = os.path.join(WORK, "atlas")
    man = os.path.join(adir, "atlas.json")
    if not os.path.isfile(man):
        raise SystemExit("ktsite: no atlas at %s -- run harness/ktatlas.py" % adir)
    plates = json.load(open(man, encoding="utf-8"))
    figs = []
    for pl in plates:
        svg = read(os.path.join(adir, pl["name"] + ".svg"))
        figs.append(f'<figure id="{html.escape(pl["name"])}">{svg}'
                    f'<figcaption>{html.escape(pl["caption"])}</figcaption></figure>')
    src = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "atlas.json"), encoding="utf-8"))
    items = []
    for e in src["events"]:
        items.append(f"<li><b>{html.escape(e['date'])} · {html.escape(e['label'])}.</b> {linkify(html.escape(e['source']))}</li>")
    for t in src["texts"]:
        items.append(f"<li><b>{html.escape(t['name'])}, {html.escape(t['date'])}.</b> {linkify(html.escape(t['source']))}</li>")
    for r in src["regions_1593"]:
        items.append(f"<li><b>{html.escape(r['name'].title())}.</b> {linkify(html.escape(r['source']))}</li>")
    tg = src["tongues"]
    for k, lab in (("areas_source", "The language areas"), ("marks_source", "The confessions"),
                   ("presses_source", "The presses"), ("glyphs_source", "The signs")):
        items.append(f"<li><b>{lab}.</b> {linkify(html.escape(tg[k]))}</li>")
    body = f"""
<h1>Atlas</h1>
{paras("atlas_lead", "lead")}
<div class="atlas">{"".join(figs)}</div>
<details class="atlas-src"><summary>Where every date and place on these plates was read</summary>
<p>Coastlines, rivers and lakes are Natural Earth, public domain. The borders of 1593 and the language areas are drawn by hand from the standard accounts and are approximate; every plate that uses them says so. Wikipedia pages were read on 23 September 2026; the book's own sources are cited to the book and to the provenance file.</p>
<ul>{"".join(items)}</ul></details>
<div class="tlpop" id="tlpop" hidden><button type="button" aria-label="Close">×</button><b></b><i></i><p></p></div>
<script>
(function(){{
  var pop=document.getElementById('tlpop');if(!pop)return;
  var t=pop.querySelector('b'),dt=pop.querySelector('i'),tx=pop.querySelector('p');
  function show(g,x,y){{
    t.textContent=g.getAttribute('data-label')||'';var d=g.getAttribute('data-date')||'';dt.textContent=(d===t.textContent)?'':d;
    tx.textContent=g.getAttribute('data-desc')||'';pop.hidden=false;
    var w=pop.offsetWidth,h=pop.offsetHeight,L=Math.min(x+14,window.innerWidth-w-10),T=y+14;
    if(T+h>window.innerHeight-10)T=y-h-14;if(T<10)T=10;if(L<10)L=10;
    pop.style.left=L+'px';pop.style.top=T+'px';
  }}
  document.querySelectorAll('.atlas .ev').forEach(function(g){{
    g.addEventListener('click',function(e){{e.stopPropagation();show(g,e.clientX,e.clientY)}});
    g.addEventListener('keydown',function(e){{if(e.key==='Enter'||e.key===' '){{e.preventDefault();var r=g.getBoundingClientRect();show(g,r.left+r.width/2,r.top+r.height/2)}}}});
  }});
  document.addEventListener('click',function(e){{if(!pop.contains(e.target))pop.hidden=true}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')pop.hidden=true}});
  pop.querySelector('button').addEventListener('click',function(){{pop.hidden=true}});
}})();
</script>
"""
    return shell("atlas", "Atlas",
                 "Maps and timelines of the Rohonc Codex: Hungary in 1593, the tongues and faiths around Rohonc, where its stories were written and when, and the codex's own history from the paper to the present.",
                 body)


def page_sources():
    cites = citations()
    gloss = [str(x) for x in COPY["sources_cites"]]
    cl = "".join(
        f'<li>{md_inline(c)}<br><span class="nof">{html.escape(gloss[i]) if i < len(gloss) else ""}</span></li>'
        for i, c in enumerate(cites))
    body = f"""
<h1>Sources and credit</h1>
{paras("sources_intro", "lead")}
<h2>What is cited</h2>
<ul class="steps">{cl}</ul>
<h2>References for the endnotes</h2>
{paras("sources_notes_lead")}
<ul class="steps">{"".join(f'<li><b>{md_inline(n)}</b><br><span class="nof">{b}</span></li>' for n, b in notes_sources())}</ul>
<h2>What is not here</h2>
{paras("sources_not_here")}
<p>Their site is <a href="https://rechnitzer-kodex.hu/" rel="noopener">rechnitzer-kodex.hu</a>, and it is the place to read them.</p>
<h2>The working documents</h2>
{paras("docs_lead")}
<ul class="steps">{docs_html()}</ul>
<p>Ask for any of them at <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
"""
    return shell("sources", "Sources and credit",
                 "Whose work each part of this rests on, what may be done with each source, and the project's own working documents.",
                 body)


def page_outside(slug, fname, title):
    text = read(os.path.join(WORK, "outside", fname))
    intro = paras("outside_lead", "lead") + '<p>The results are on the <a href="/rohonc/tests.html">tests page</a>.</p>'
    return shell(slug, title, f"{title}: the outside reviewer's specification of tests for the Rohonc readings, quoted whole.",
                 f"<h1>{html.escape(title)}</h1>" + intro + md(text))


def corpus_list():
    """The reference texts the folios are read against, from DATA_PROVENANCE.md:
    the bullets of its corpus section and the two sources added after."""
    txt = read(os.path.join(ROOT, "DATA_PROVENANCE.md"))
    out = []
    sec = re.search(r"^## 4\. `data/ref/rohonc/`.*?(?=^## )", txt, re.M | re.S)
    if sec:
        for b in re.findall(r"^- (\*\*.*?)(?=^- |\Z)", sec.group(0), re.M | re.S):
            one = " ".join(b.split())
            m = re.match(r"\*\*(.+?)\*\*\s*(?:[—-]+|,)\s*(.*)", one)
            if not m:
                continue
            name = re.sub(r"\*", "", m.group(1)).strip()
            src = m.group(2).split(".")[0]
            out.append((name, src))
    sec = re.search(r"^## 5\. Two sources added.*?(?=^## )", txt, re.M | re.S)
    if sec:
        for para in sec.group(0).split("\n\n"):
            m = re.match(r"\*\*`[^`]+`(?: and `[^`]+`)?\.\*\*\s*(.+?)\s*(?:\(|,\s*from|,\s*tr\.)", " ".join(para.split()))
            if m:
                src = "Project Gutenberg" if "Gutenberg" in para else ("Internet Archive" if "Internet Archive" in para else "")
                out.append((re.sub(r"\*", "", m.group(1)).strip().rstrip(","), src))
    return out


def page_data(outside):
    def li(href, name, desc, size):
        return (f'<li><a href="{href}">{html.escape(name)}</a> <span class="nof">{html.escape(desc)}'
                f'{" · " + size if size else ""}</span></li>')

    def sz(p):
        n = os.path.getsize(p)
        return f"{n/1024:.0f} KB" if n < 1024 * 1024 else f"{n/1024/1024:.1f} MB"

    body = ["<h1>Data</h1>", paras("data_lead", "lead"),
            "<h2>The corpus</h2>",
            "<p>The books the codex is compiled from, which every folio is read against. What each supplied and where to read it is on "
            "<a href=\"/rohonc/corpus.html\">The corpus</a>.</p><ul class=\"steps\">"]
    import ktcorpus
    for e in ktcorpus.entries():
        body.append(f'<li><b><a href="/rohonc/corpus.html#{html.escape(e["anchor"])}">{html.escape(e["name"])}</a></b></li>')
    body.append("</ul><h2>The outside review</h2><p>The two reviewers' specifications are quoted whole: "
                '<a href="/rohonc/outside-gemini.html">Gemini 2.5 Pro</a> and <a href="/rohonc/outside-grok.html">Grok 4.7</a>. '
                "Their replies as re-glossers and blind readers are files, and go up with the rest.</p>")
    body.append("<h2>Everything else</h2><p>The dictionary of added readings with its evidence, the folio English, the rendering, "
                "every saved run, the outside readers' replies, the working documents and the programs are posted to GitHub, "
                "with their history, so that nothing here links to a copy that can go stale. The standing orders are already "
                'published whole at <a href="/rohonc/orders.html">The standing orders</a>.</p>')
    return shell("data", "Data", "Every file the Rohonc pages are built from: the dictionary of added readings, the folio English, the rendering, the saved test runs and the outside readers' replies.",
                 "\n".join(body))


# ---- build ------------------------------------------------------------------------

def copy(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)


# The subtrees this program owns. Everything else under the site root -- book/,
# plates/ -- is put there by another program and is never touched here.
MANAGED = ("data", "code", "img", "atlas")


def _files(root):
    """Every file under root, as paths relative to it."""
    got = set()
    for base, _, names in os.walk(root):
        for n in names:
            got.add(os.path.relpath(os.path.join(base, n), root))
    return got


def publish(stage, final):
    """Move a finished build over the live tree, file by file, replacing.

    The build used to render straight into the live directory, and before
    rendering it deleted the served data files. A build that died in the
    middle -- a missing plate, a bad figure, a checker raising -- therefore
    took the site's data down with it and left half-written pages behind, and
    the nested data/outside/ folders were never cleared at all, so a renamed
    reply file stayed served for ever. So the build now renders into a staging
    directory and only reaches the live tree here, after it has succeeded.

    Each file lands by os.replace, which is atomic: a reader gets the old file
    or the new one, never a partial one. Stale files are taken down by name
    after the new ones are in place, and only inside MANAGED and the top-level
    pages, so no link can point at a copy this build no longer makes.
    """
    made = _files(stage)
    for rel in sorted(made):
        dst = os.path.join(final, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        tmp = dst + ".new"
        shutil.copyfile(os.path.join(stage, rel), tmp)
        os.replace(tmp, dst)
    gone = 0
    for rel in sorted(_files(final) - made):
        top = rel.split(os.sep)[0]
        if top in MANAGED or (os.sep not in rel and (rel.endswith(".html") or rel == "sitemap.xml")):
            os.remove(os.path.join(final, rel))
            gone += 1
    for sub in MANAGED:                       # drop folders left empty
        d = os.path.join(final, sub)
        for base, dirs, _ in os.walk(d, topdown=False):
            if base != d and not os.listdir(base):
                os.rmdir(base)
    return len(made), gone


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_DEFAULT)
    a = ap.parse_args(argv)
    final = a.out
    os.makedirs(final, exist_ok=True)
    # render into a staging directory beside the live one, never into it; see
    # publish(). Same filesystem, so the files land by rename, not by copy.
    out = tempfile.mkdtemp(prefix=".build-", dir=os.path.dirname(os.path.abspath(final)))
    try:
        return _build(out, final)
    finally:
        shutil.rmtree(out, ignore_errors=True)


def _build(out, final):
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
    sample = sample_lines()
    pl = plates()

    # the data itself goes up on GitHub. Only what the pages load is served: the
    # dictionary page searches dictionary.json. Copies served by earlier builds
    # are taken down by name in publish(), after this build has succeeded, so no
    # link anywhere can point at a stale file.
    json.dump(rows, open(os.path.join(out, "data", "dictionary.json"), "w", encoding="utf-8"), ensure_ascii=False)
    # the two pictures the pages need, from the repository: the glass over the
    # strip (three times its drawn size, sharp on a retina screen) and the 3-D
    # mock of the printed book, made by Cover Maker's own snapshot from the wrap
    from PIL import Image as _Im
    os.makedirs(os.path.join(out, "img"), exist_ok=True)
    gg = glass_geom()
    _g = _Im.open(os.path.join(WORK, "glass.png")).resize((gg["w"] * 3, gg["h"] * 3), _Im.LANCZOS)
    _g.save(os.path.join(out, "img", "glass.png"), optimize=True)
    _b3 = os.path.join(WORK, "book3d.png")
    if os.path.isfile(_b3):
        _m = _Im.open(_b3); _m.thumbnail((576, 900)); _m.save(os.path.join(out, "img", "book3d.png"))
    for _f in SPIN_FACES:   # the turning book's three faces, cut by ktspin.py
        copy(os.path.join(WORK, f"spin-{_f}.webp"), os.path.join(out, "img", f"spin-{_f}.webp"))
    files = []
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
    sg = signs()
    w("index.html", page_index(fig, summary, ktn, newpara, tiers, len(order), sg, rows, pl))
    w("script.html", page_script(sample, pl, ktn))
    w("orders.html", page_orders())
    w("corpus.html", page_corpus())
    w("read.html", page_read())
    w("method.html", page_method())
    w("code.html", page_code(out))
    rd, n_eng = page_reading(order, eng)
    w("reading.html", rd)
    w("dictionary.html", page_dictionary(about, rows, ktn))
    w("tests.html", page_tests(summary))
    w("sources.html", page_sources())
    w("finds.html", page_finds())
    w("atlas.html", page_atlas())
    # the atlas plates, as drawn: the SVGs the page inlines, and the PNGs for image search
    adir = os.path.join(WORK, "atlas")
    for fn in sorted(os.listdir(adir)):
        if fn.endswith((".svg", ".png")):
            copy(os.path.join(adir, fn), os.path.join(out, "atlas", fn))
    w("outside-gemini.html", page_outside("tests", "gemini_tests.md", "Outside review: Gemini 2.5 Pro"))
    w("outside-grok.html", page_outside("tests", "grok_tests.md", "Outside review: Grok 4.7"))
    w("data.html", page_data([]))
    # A sitemap, because these pages were behind the gate and no crawler has
    # ever seen them. Built from the files this run actually wrote, so it can
    # never list a page that does not exist or miss one that does.
    import datetime as _dt
    today = _dt.date.today().isoformat()
    pages = sorted(f for f in os.listdir(out) if f.endswith(".html"))
    locs = []
    for f in pages:
        loc = "https://oona13.com/rohonc/" + ("" if f == "index.html" else f)
        pri = "1.0" if f == "index.html" else "0.8" if f in ("reading.html", "tests.html", "dictionary.html") else "0.6"
        locs.append(f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod>"
                    f"<changefreq>monthly</changefreq><priority>{pri}</priority></url>")
    open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(locs) + "\n</urlset>\n")

    n_new, n_gone = publish(out, final)
    print(f"wrote {final}: {len(order)} folios ({n_eng} with English), {len(rows)} dictionary rows, "
          f"{10} pages, {len(pl)} plates, "
          f"{len(sg.get('signs', {}))} signs")
    print(f"published {n_new} files, took down {n_gone} stale")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
