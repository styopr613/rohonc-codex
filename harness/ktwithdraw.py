"""Withdraw a reading of ours, keeping the record and the reason.

The key is renamed to _withdrawn_<hex>, which the renderer and every count
ignore, and the reason is written into the entry. Use this, not deletion,
when a reading turns out to be wrong -- the next person needs to know it was
tried and why it failed.

    python3 ktwithdraw.py HEX --why "..."
"""
import json
import sys


def main(argv):
    h = argv[0]
    p = json.load(open('proposals.json', encoding='utf-8'))
    if h not in p:
        print(f"{h}: not in proposals.json"); return 1
    why = argv[argv.index('--why') + 1]
    v = p.pop(h)
    old = v.get('gloss')
    v['evidence'] = why + "  Prior gloss and evidence: " + repr(old) + " -- " \
        + v.get('evidence', '')
    v['gloss'] = '_withdrawn_'
    v['tier'] = 'withdrawn'
    p['_withdrawn_' + h] = v
    with open('proposals.json', 'w', encoding='utf-8') as f:
        json.dump(p, f, indent=1, ensure_ascii=False, sort_keys=True)
    print(f"{h}: withdrawn (was {old!r})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
