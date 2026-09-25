#!/usr/bin/env bash
# Commit only when all three checkers pass, using their real exit status.
#
# Three commits went in with a failing checker because the command line was
#     python3 check_rohonc.py | tail -1 && git commit ...
# and the pipe reports tail's exit status, not the checker's. This script
# runs each checker unpiped and refuses to commit on any failure.
#
#     ./ktcommit.sh "Translate 108r-110v: ... 200 -> 206 folios; 59.3% lines"
set -u
cd "$(dirname "$0")" || exit 1
msg="${1:-}"
if [ -z "$msg" ]; then echo "usage: ./ktcommit.sh \"commit message\" [path ...]"; exit 2; fi
shift
# Paths after the message: commit ONLY those. Without them the whole tree is
# swept (see below). The owner asked on 2026-09-25 why the relevant files
# could not simply be committed on their own. They can; this is how.
paths=("$@")
# Regenerate the saved run BEFORE ktbump reads it. This was a real failure:
# work/rohonc/kttranslate.txt had not been regenerated for days, so ktbump
# carried 61.1% lines-fully-read into ROHONC.md while the live figure was
# 80.1%, and check_rohonc.py passed -- because it compared the prose against
# the same stale file. A checker that compares two stale things agrees with
# itself. The saved run is now rebuilt on every commit.
python3 kttranslate.py > ../work/rohonc/kttranslate.txt 2>/dev/null || {
  echo "kttranslate failed"; exit 1; }
# And the reader's edition, for the same reason and after a worse failure.
# ktretellcheck reads Book One's quotations against the gloss in
# rohonc_readers_edition.md. That file was NOT regenerated here, so it went
# stale behind the readings: on 2026-09-22 it still carried "anointed",
# "eternal" and "[equal]" at places the readings now give "~place", "heaven"
# and "finger". The gate passed the whole time, because Book One and the file
# it was checked against were stale together. Forty-six quotations were
# wrong. Regenerated here, before any checker reads it.
python3 ktreader.py > /tmp/ktreader.out 2>&1 || {
  cat /tmp/ktreader.out; echo "ktreader failed"; exit 1; }
tail -1 /tmp/ktreader.out
python3 ktbump.py > /tmp/ktbump.out 2>&1 || { cat /tmp/ktbump.out; echo "ktbump failed"; exit 1; }
tail -1 /tmp/ktbump.out
ok=1
# The list lives in gates.txt, which ktpush.sh reads too. It used to be typed
# out here and nowhere else; a second script with a second copy of it is the
# same drift this project keeps paying for. A gate that is not run on every
# commit is not a gate.
while read -r c; do
  case "$c" in ''|\#*) continue ;; esac
  if python3 "$c" > "/tmp/$c.out" 2>&1; then
    echo "  ok    $c   $(tail -1 /tmp/$c.out)"
  else
    echo "  FAIL  $c"; grep -n "FAIL\|MISMATCH\|Error" "/tmp/$c.out" | head -10; ok=0
  fi
done < gates.txt
if [ "$ok" != 1 ]; then echo "NOT COMMITTED: fix the failure above first"; exit 1; fi
cd .. || exit 1
# SAY WHAT IS BEING COMMITTED. `git add -A` is right -- anything else silently
# drops new files, which is worse -- but it is a sweep, and an unnarrated sweep
# is how this repository acquired things nobody chose to publish: GPT's commit
# went out inside the Atlas commit f97f327, a 6.4MB duplicate of the EPUB went
# out on 2026-09-22, and 10MB of the site's own artwork -- five atlas plates,
# the book rendered in 3D, the glass textures -- sat in a repository whose
# README says it holds everything needed to check the attempt. .gitignore now
# refuses those by name. This prints the rest, so the next one is visible
# before it goes in rather than found later by a reader.
if [ "${#paths[@]}" -gt 0 ]; then
  git add -A -- "${paths[@]}"
else
  git add -A
fi
echo
echo "  committing:"
git diff --cached --name-status | sed 's/^/    /'
echo
git commit -q -m "$msg

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" && git log --oneline | head -1
