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
if [ -z "$msg" ]; then echo "usage: ./ktcommit.sh \"commit message\""; exit 2; fi
python3 ktbump.py > /tmp/ktbump.out 2>&1 || { cat /tmp/ktbump.out; echo "ktbump failed"; exit 1; }
tail -1 /tmp/ktbump.out
ok=1
for c in gate.py check_results.py check_rohonc.py; do
  if python3 "$c" > "/tmp/$c.out" 2>&1; then
    echo "  ok    $c   $(tail -1 /tmp/$c.out)"
  else
    echo "  FAIL  $c"; grep -n "FAIL\|MISMATCH\|Error" "/tmp/$c.out" | head -10; ok=0
  fi
done
if [ "$ok" != 1 ]; then echo "NOT COMMITTED: fix the failure above first"; exit 1; fi
cd .. && git add -A && git commit -q -m "$msg

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>" && git log --oneline | head -1
