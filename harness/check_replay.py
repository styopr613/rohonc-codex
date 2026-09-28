"""Every saved test run must still come out of its program, byte for byte.

check_tests.py checks that each figure TESTS.md prints stands in its saved
run. It cannot see a saved run that no longer reproduces, and from 25 to 28
September fifteen of twenty did not: the readings changed and the runs were
not rewritten (TESTS.md, "Every run regenerated again"). This runs the replay
on every commit and every push, under one hash seed; the full two-seed replay
is `python3 harness/reproduce_tests.py`.

The bar is ZERO saved runs that fail to reproduce, declared here before this
gate first ran.

    python3 check_replay.py
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

p = subprocess.run([sys.executable, os.path.join(HERE, "reproduce_tests.py"), "--hash-seeds", "0"],
                   cwd=ROOT, text=True, capture_output=True)
out = p.stdout + p.stderr
bad = [l for l in out.splitlines() if l.startswith("FAIL")]
last = [l for l in out.splitlines() if "reproduced" in l]
print(last[-1] if last else out[-400:])
for l in bad:
    print(" ", l)
if p.returncode != 0 or bad:
    print("FAIL: a saved test run no longer reproduces; rerun it, read the diff, and "
          "carry every moved figure into TESTS.md")
    sys.exit(1)
print("PASS: every saved run reproduces; bar was 0 failures")
