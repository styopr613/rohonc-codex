"""Fill the <!--TABLE:X--> placeholders in RESULTS.md from the results JSON.

Every figure in the write-up's tables comes from the data this way, so the
document cannot drift from the run that produced it. Prose figures are still
written by hand; `check_results.py` verifies those against the JSON.

    python build_results.py            # rewrite RESULTS.md in place
    python build_results.py --check    # fail if it is out of date
"""
import argparse
import io
import os
import re
import subprocess
import sys

import corpus

DOC = os.path.join(corpus.ROOT, "RESULTS.md")
HERE = os.path.dirname(os.path.abspath(__file__))

MARK = re.compile(r"<!--TABLE:(\w+)-->(?:\n(?:\|.*\n|\n(?=\|))*)?")


def tables():
    out = subprocess.run([sys.executable, os.path.join(HERE, "report.py"),
                          "--markdown"], capture_output=True, text=True, cwd=HERE)
    if out.returncode:
        raise SystemExit(out.stderr)
    blocks, cur, name = {}, [], None
    for line in out.stdout.splitlines():
        m = re.match(r"<!-- (\w+) -->", line)
        if m:
            if name:
                blocks[name] = "\n".join(cur).strip()
            name, cur = m.group(1), []
            continue
        cur.append(line)
    if name:
        blocks[name] = "\n".join(cur).strip()
    return blocks


def render():
    blocks = tables()
    src = open(DOC, encoding="utf-8").read()

    def sub(m):
        key = m.group(1)
        if key not in blocks:
            raise SystemExit(f"no table named {key}; have {sorted(blocks)}")
        return f"<!--TABLE:{key}-->\n{blocks[key]}\n"

    return MARK.sub(sub, src)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    new = render()
    old = open(DOC, encoding="utf-8").read()
    if args.check:
        ok = new == old
        print("RESULTS.md tables are " + ("current" if ok else "OUT OF DATE"))
        return 0 if ok else 1
    open(DOC, "w", encoding="utf-8").write(new)
    n = len(MARK.findall(new))
    print(f"filled {n} tables in RESULTS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
