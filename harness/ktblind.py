"""THE BLINDFOLD TEST -- the one check this project cannot run on itself.

Gate 4b in ktrederive.py measures the only unmeasured part of this work: the
judgment step, where a reader chooses among the candidates the tools propose.
It was run here and it came out INVALID, because the reader had spent the day
reading Kiraly and Tokai's dictionary and twelve of the twenty-five sampled
signs were ones he had already met. Those scored 75%. The thirteen he had not
met scored 23.1%.

So the test has to be run by someone who has not read the dictionary. This
file makes that easy to hand over. It draws a FRESH sample with a fresh seed
every time, so no two runs test the same signs and nobody can be primed by a
previous run's answers.

    python ktblind.py --new            draw a fresh blind sample
    python ktblind.py --score FILE     reveal and score it

The brief for whoever runs it is notes/BLINDFOLD.md. It is
written to be handed to a session that knows nothing about this project.
"""
import os
import random
import sys
import time

import ktcross as K
import ktrederive as R


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    if "--seed" in argv:
        R.SEED = int(argv[argv.index("--seed") + 1])
    if "--score" in argv:
        return R.score(gl, argv[argv.index("--score") + 1])
    seed = R.SEED if "--seed" in argv else int(time.time())
    R.SEED = seed
    R.BLIND = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                           "work", "rohonc", f"blindfold_{seed}.txt")
    print(f"THE BLINDFOLD TEST. fresh seed {seed}.")
    print("Score it with:  python3 ktblind.py --score <the file below> --seed %d\n" % seed)
    return R.dump(gl, doc)


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main(sys.argv[1:]))
