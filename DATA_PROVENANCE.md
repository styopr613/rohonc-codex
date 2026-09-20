# Rohonc data: where each file came from and what may be done with it

None of this directory is in the repository. `data/` is gitignored, so the
transcriptions and scans stay local. If this project is ever published, the
code and the derived statistics go; the data does not. This file records what
each source permits so that decision does not depend on anyone's memory.

## 1. `latest.txt` — the anonymous open transcription, 2014

Revision 2.5, 2014-09-18. Originally at `quint.us/Roho/latest.txt`; that domain
now serves an unrelated browser game. Recovered from the Internet Archive:

    https://web.archive.org/web/20180421091607id_/http://quint.us/Roho/latest.txt

Glyph-level, no word separation. 214 pages, 4,250 lines, 60,407 readable
tokens, 987 types, 6.5% marked unreadable. Incomplete and partly produced by
the author's own scanning software.

**Terms:** the author's blog post announcing it reads "It's time for a free and
open transcription of the Rohonc Codex", which is as clear a statement of
intent as exists. No formal licence. The author is anonymous and the site is
gone, so permission cannot be asked. Credited as fully as it can be.

## 2. `kt/` — Kiraly & Tokai's transcription

Fetched from the public API of `rechnitzer-kodex.hu`, 447 pages.

Word-level, private-use-area encoding, with editorial markup and the authors'
own reading order for the pages. Underlies Kiraly & Tokai, *Cracking the code
of the Rohonc Codex*, Cryptologia 42:4 (2018), 285-315.

**Terms:** no licence is stated on the site. `robots.txt` is `User-agent: *` /
`Disallow:` with nothing after it, which permits crawling. Kiraly's 2022 paper
(*A Rohonci kodex teologiai karaktere*, in Hagyomany, Identitas, Tortenelem
2022, publ. 2023, footnote 13) explains that the site exists because the
dictionary is too typographically awkward to print, and that the digitised text
is there together with it so that -- his words -- "our claims about the text are
verifiable this way".

**So: analysing it is the stated purpose of the site. Redistributing it is not
covered by anything, and must not be done without asking the authors.**

**A courtesy failure to not repeat.** The first pull ran at 0.4s between
requests and tripped the site's rate limiter; 192 of 447 requests came back as
the limit page rather than JSON. The refetch runs at 1.5s with backoff. This is
a small academic server. Cache locally, never refetch what is already here.

**Owed to them:** an email. Our repeat-length measurement finds nothing
recurring beyond about three lines, which sits awkwardly with the seven-line
verbatim parallel they report between 133v07-134r02 and 101r04-09. That is
either a difference between transcriptions or a difference in what counts as a
parallel, and they would want to know either way.

## 3. `scan/` — the page images

`https://real-ms.mtak.hu/80/6/Rohonci_Codex_K_114cs.pdf`, the low-resolution
monochrome scan, 227 spreads at about 880x545, roughly 100 ppi of a 120x100 mm
book.

**Terms, as the repository states them:** "Gratis OA - Tudomanyos / Oktatasi
Felhasznalasra - Ne Add Tovabb!" — free open access, for academic or
educational use, do not pass on. Analysed locally and not redistributed, which
is within that. The high-resolution colour version on the same page is
restricted to repository staff and was not obtained.

## Citations owed in any write-up

- Levente Zoltan Kiraly and Gabor Tokai, "Cracking the code of the Rohonc
  Codex", *Cryptologia* 42:4 (2018), 285-315.
- Levente Zoltan Kiraly, "A Rohonci kodex teologiai karaktere", in *Hagyomany,
  Identitas, Tortenelem 2022*, KRE HTK, Budapest 2023, 363-376.
- Otto Gyurk (1970), on line breaks in the codex's repeated sequences -- the
  idea both the orientation test and the main result rest on.
- Benedek Lang, *The Rohonc Code: Tracing a Historical Riddle*, Penn State
  Press, 2021.
- The anonymous author of the 2014 open transcription.
