"""Change one reading in proposals.json, keeping the file readable.

    python3 ktset.py HEX --gloss WORD --tier G --why "..."
    python3 ktset.py HEX --show

Writes the same JSON shape the file already uses: two-space indent, sorted
keys, UTF-8 kept as characters. Refuses to create a key that is not there.
"""
import json
import sys


def main(argv):
    h = argv[0]
    p = json.load(open('proposals.json', encoding='utf-8'))
    if h not in p:
        print(f"{h}: not in proposals.json"); return 1
    v = p[h]
    if '--show' in argv:
        print(json.dumps(v, indent=1, ensure_ascii=False)); return 0
    old = dict(v)
    if '--gloss' in argv:
        v['gloss'] = argv[argv.index('--gloss') + 1]
    if '--tier' in argv:
        v['tier'] = argv[argv.index('--tier') + 1]
    if '--why' in argv:
        v['evidence'] = argv[argv.index('--why') + 1]
    with open('proposals.json', 'w', encoding='utf-8') as f:
        json.dump(p, f, indent=1, ensure_ascii=False, sort_keys=True)
    print(f"{h}: {old.get('gloss')!r} [{old.get('tier')}] -> "
          f"{v.get('gloss')!r} [{v.get('tier')}]")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
