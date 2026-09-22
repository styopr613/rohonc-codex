#!/usr/bin/env bash
# ONE COMMAND. Regenerate everything from the readings, check it, push it out.
#
# The readings are the source of truth. Everything else -- the saved run, the
# reader's edition, Book One's accounting, the book on the shelf, its EPUB, the
# web reader's copy, the public site -- is derived from them. Each of those used
# to be rebuilt by hand, separately, whenever somebody remembered, and they
# drifted: on 2026-09-22 the reader's edition was a day behind the readings, the
# gate that reads it had been agreeing with itself the whole time, and the
# book's own front matter still printed 97.9% when the true figure was 71.1%.
#
# So there is one command, it runs in dependency order, and it refuses to push
# anything if any gate fails.
#
#     ./ktpush.sh                  regenerate, check, push to shelf and site
#     ./ktpush.sh --check          regenerate and check, push nothing
#     ./ktpush.sh --no-site        skip the public site
#     ./ktpush.sh --overwrite-shelf-edits    discard Book Maker edits
#
# NO PIPES ON ANYTHING THAT MATTERS. `build | tail` reports tail's status, which
# is how two commits went in over a broken build.
set -u -o pipefail
cd "$(dirname "$0")" || exit 1

SHELF=/opt/publish-app/data/u1/books/20260921-052535-r0hc
SITE_PY=/opt/publish-app/venv/bin/python
check_only=0; do_site=1; do_shelf=1; shelf_flags=""
for arg in "$@"; do
  case "$arg" in
    --check) check_only=1 ;;
    --no-site) do_site=0 ;;
    --no-shelf) do_shelf=0 ;;
    --overwrite-shelf-edits) shelf_flags="--overwrite-shelf-edits" ;;
    *) echo "unknown option: $arg"; exit 2 ;;
  esac
done

step() { printf '\n== %s\n' "$1"; }

step "1/5  regenerate what the readings produce"
python3 kttranslate.py > ../work/rohonc/kttranslate.txt 2>/dev/null || {
  echo "kttranslate failed"; exit 1; }
echo "  ok    kttranslate.txt"
python3 ktreader.py > /tmp/ktpush_reader.out 2>&1 || {
  cat /tmp/ktpush_reader.out; echo "ktreader failed"; exit 1; }
echo "  ok    reader's edition   $(grep -o 'read [0-9,]* ([0-9.]*%)' /tmp/ktpush_reader.out | head -1)"
python3 ktbump.py > /tmp/ktpush_bump.out 2>&1 || {
  cat /tmp/ktpush_bump.out; echo "ktbump failed"; exit 1; }
echo "  ok    prose figures      $(tail -1 /tmp/ktpush_bump.out)"

step "2/5  the gates"
ok=1
while read -r c; do
  case "$c" in ''|\#*) continue ;; esac
  if python3 "$c" > "/tmp/$c.out" 2>&1; then
    echo "  ok    $c   $(tail -1 "/tmp/$c.out")"
  else
    echo "  FAIL  $c"; grep -n "FAIL\|MISMATCH\|Error" "/tmp/$c.out" | head -10; ok=0
  fi
done < gates.txt
if [ "$ok" != 1 ]; then echo; echo "NOTHING PUSHED: a gate failed."; exit 1; fi

if [ "$check_only" = 1 ]; then echo; echo "checked, pushed nothing (--check)"; exit 0; fi

step "3/5  the book, to the shelf"
if [ "$do_shelf" = 1 ]; then
  # ktbook stops here by itself if the book was edited in Book Maker since the
  # last push, and names the chapters, rather than overwriting them.
  python3 ktbook.py --shelf "$SHELF" $shelf_flags || {
    echo "NOTHING FURTHER PUSHED: the book did not build"; exit 1; }
else
  echo "  skipped (--no-shelf)"
fi

step "4/5  the public site"
if [ "$do_site" = 1 ]; then
  "$SITE_PY" ktsite.py || { echo "site build failed"; exit 1; }
else
  echo "  skipped (--no-site)"
fi

step "5/5  done"
echo "The shelf book, its EPUB, the web reader's copy and the site are all"
echo "built from the readings as they stand right now."
