"""Every flagged reading, compactly, so a person can scan hundreds not tens."""
import json, sys
from collections import defaultdict
import ktaffix as A, ktcross as K, ktleft as L, ktrederive as R, kttranslate as T
import ktharden

def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    start = int(argv[argv.index('--from')+1]) if '--from' in argv else 0
    n = int(argv[argv.index('--n')+1]) if '--n' in argv else 40
    only = argv[argv.index('--tier')+1] if '--tier' in argv else None

    lines = defaultdict(list)
    for pg in doc:
        for i, ln in enumerate(pg.lines, 1):
            toks = [x for run in ln for x in run]
            rend = [T.render_token(t, gl, seg, False, var, prop) for t in toks]
            for t in toks:
                h = K.hx(A.strip(t)[0])
                if len(lines[h]) < 3:
                    lines[h].append((pg.page, i, ' '.join(rend)))

    ours = {k: v for k, v in p.items() if not k.startswith('_')
            and isinstance(v, dict) and v.get('tier') in ('A','B','C','D')}
    sel = sorted(k for k, v in ours.items()
                 if (not only or v['tier'] == only))
    sel = sel[start:start+n]
    for h in sel:
        v = ours[h]
        print(f"{h} [{v['tier']}] {v['gloss']}")
        for pg, i, ln in lines.get(h, []):
            print(f"   {pg}:{i} {ln[:132]}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
