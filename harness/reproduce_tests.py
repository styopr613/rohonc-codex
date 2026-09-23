"""Replay every saved result named on the Rohonc tests page.

Run from the repository root:

    python3 harness/reproduce_tests.py

Each program is run twice with different Python hash seeds.  Its stdout must
match the archived run byte for byte.  Exit status 1 is allowed because several
tests intentionally preserve a declared FAIL or NO VERDICT; crashes are not.
Test 4 is not included: it is explicitly BLOCKED and has no result or saved run.
The outside-reader tests score the committed raw replies without making network
requests.  Test 3 scores the committed blind reader's filled worksheet; drawing
a new sample is a new experiment, not a reproduction of the published one.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable

# label, arguments after Python, archived stdout
CASES = [
    ("Test 1", ["harness/ktheldout.py"], "work/rohonc/ktheldout.txt"),
    ("Test 2", ["harness/ktpos.py"], "work/rohonc/ktpos.txt"),
    ("Test 2b", ["harness/ktpos2.py"], "work/rohonc/ktpos2.txt"),
    ("Test 3 score", ["harness/ktblind.py", "--score", "../work/rohonc/blindfold_1790006519.txt",
                      "--seed", "1790006519"], "work/rohonc/blindfold_1790006519_score.txt"),
    ("Test 5", ["harness/ktsentence.py"], "work/rohonc/ktsentence.txt"),
    ("Test 6", ["harness/ktorder.py"], "work/rohonc/ktorder.txt"),
    ("Test 7", ["harness/ktrecover.py"], "work/rohonc/ktrecover.txt"),
    ("Test 8", ["harness/ktbootstrap.py"], "work/rohonc/ktbootstrap.txt"),
    ("Test 9", ["harness/ktseedcheck.py"], "work/rohonc/ktseedcheck.txt"),
    ("Test 10", ["harness/ktnullreplay.py"], "work/rohonc/ktnullreplay.txt"),
    ("Test 10b", ["harness/ktnullreplay2.py"], "work/rohonc/ktnullreplay2.txt"),
    ("Test 10c", ["harness/ktnullreplay3.py"], "work/rohonc/ktnullreplay3.txt"),
    ("Test 11", ["harness/ktpassid.py"], "work/rohonc/ktpassid.txt"),
    ("Test 12", ["harness/ktstrict.py"], "work/rohonc/ktstrict.txt"),
    ("Test 12b Gemini", ["harness/ktstrict.py", "--score",
                         "../work/rohonc/outside/reglosser_gemini.json"],
     "work/rohonc/ktstrict_reglosser_gemini.txt"),
    ("Test 12b Grok", ["harness/ktstrict.py", "--score",
                       "../work/rohonc/outside/reglosser_grok.json"],
     "work/rohonc/ktstrict_reglosser_grok.txt"),
    ("Test 13", ["harness/ktcensus.py"], "work/rohonc/ktcensus.txt"),
    ("Test 14", ["harness/ktblindfill.py"], "work/rohonc/ktblindfill.txt"),
    ("Test 15", ["harness/ktpassid2.py"], "work/rohonc/ktpassid2.txt"),
    ("Test 16", ["harness/ktopen.py"], "work/rohonc/ktopen.txt"),
]

INPUTS = {
    "data/rohonc/latest.txt": "ac0d744234c5cb4299f1dcb3adbcccd55bd78f2fbbfc1f9ba1c097d0bd6e528b",
    "data/rohonc/kt/dict_en.json": "6c74ec8725e49b978aa7694cd76179f65e0bb3bb5f80898e0420e6b693ef4cbc",
    "data/rohonc/kt/pagelist.json": "466154fcc6e13ef8cbce4c67549dd9222576ede1a5cc708ca8262589938a8864",
    "data/ref/rohonc/bible_kjv_verses.txt": "0204adaed1f25700aa854218cae63c7172228c41088f335e99167a071eed83c0",
    "data/ref/rohonc/bible_dr_verses.txt": "65ffc9eff384c1c8ffe1cbd2bf58964b228f8057c516ac7594196068f6a65c4b",
}
PAGES_SHA256 = "6a1be6144883e6d74505c82b3926f6ffb64b393fc3b3189f904a0794d58d4064"
PYTHON_VERSION = (3, 10, 12)
NUMPY_VERSION = "2.2.6"


def check_inputs() -> list[str]:
    errors = []
    for name, expected in INPUTS.items():
        path = ROOT / name
        if not path.is_file():
            errors.append(f"missing input: {name}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            errors.append(f"input differs from the published run: {name}")
    pages = sorted((ROOT / "data/rohonc/kt/pages").glob("*.json"))
    digest = hashlib.sha256()
    for path in pages:
        digest.update(path.name.encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
    if len(pages) != 447:
        errors.append(f"Király–Tokai page count is {len(pages)}, expected 447")
    elif digest.hexdigest() != PAGES_SHA256:
        errors.append("Király–Tokai page set differs from the published run")
    return errors


def check_runtime() -> list[str]:
    errors = []
    if sys.version_info[:3] != PYTHON_VERSION:
        errors.append(f"Python is {'.'.join(map(str, sys.version_info[:3]))}, expected 3.10.12")
    try:
        import numpy
    except ImportError:
        errors.append("numpy is missing, expected 2.2.6")
    else:
        if numpy.__version__ != NUMPY_VERSION:
            errors.append(f"numpy is {numpy.__version__}, expected {NUMPY_VERSION}")
    return errors


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--hash-seeds", default="0,1",
                    help="comma-separated PYTHONHASHSEED values (default: 0,1)")
    ap.add_argument("--only", action="append", default=[],
                    help="run labels containing this text; repeatable")
    ns = ap.parse_args(argv)
    input_errors = check_runtime() + check_inputs()
    if input_errors:
        print("Cannot reproduce with a missing or different runtime/input:", file=sys.stderr)
        for error in input_errors:
            print(f"  {error}", file=sys.stderr)
        print("See DATA_PROVENANCE.md for sources and exact editions.", file=sys.stderr)
        return 2
    seeds = [s.strip() for s in ns.hash_seeds.split(",") if s.strip()]
    cases = [c for c in CASES if not ns.only or any(q.lower() in c[0].lower() for q in ns.only)]
    failures = 0
    for label, args, saved_name in cases:
        saved = (ROOT / saved_name).read_text(encoding="utf-8")
        good = True
        note = []
        for seed in seeds:
            env = os.environ.copy()
            env["PYTHONHASHSEED"] = seed
            try:
                p = subprocess.run([PY, *args], cwd=ROOT, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   timeout=300)
            except subprocess.TimeoutExpired:
                good = False
                note.append(f"hash seed {seed}: TIMEOUT")
                continue
            if p.returncode not in (0, 1):
                good = False
                note.append(f"hash seed {seed}: exit {p.returncode}; {p.stderr.strip()[:240]}")
            if p.stdout != saved:
                good = False
                diff = "".join(difflib.unified_diff(
                    saved.splitlines(True), p.stdout.splitlines(True),
                    fromfile=saved_name, tofile=f"replay (hash seed {seed})", n=2))
                note.append(diff[:1800].rstrip())
        print(f"{'PASS' if good else 'FAIL'}  {label}  ({len(seeds)} hash seeds)")
        if not good:
            failures += 1
            for line in note:
                print(line, file=sys.stderr)
    print(f"\n{len(cases) - failures}/{len(cases)} saved runs reproduced exactly; Test 4 remains BLOCKED.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
