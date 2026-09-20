#!/bin/bash
# page.sh 004v 004r ...  -> the full-sense gloss for those folios
F=/home/ubuntu/voynich/work/rohonc/translation/rohonc_reading_full.txt
for pg in "$@"; do
  echo "=== $pg ==="
  awk -v P="=== $pg ===" '$0==P{f=1;next} f&&/^=== /{exit} f' "$F"
done
