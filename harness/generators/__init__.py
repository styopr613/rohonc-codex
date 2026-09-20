"""Generator registry.

Every process exposes the same call:

    generate(spec, train, seed) -> (document, notes)

`spec` is the TRAIN-derived layout, `train` the TRAIN half of the manuscript
(whatever a process is allowed to learn from), `seed` an integer. `document` is
a list of corpus.Para. `notes` is a dict recorded in the results for anything
the reader needs to know about that row -- a shortfall, a plaintext source, a
parameter that was fixed rather than tuned.

No generator may read the TEST half. gate.py checks for it.
"""
REGISTRY = {}


def register(name, *, kind, **meta):
    def deco(fn):
        REGISTRY[name] = {"fn": fn, "kind": kind, **meta}
        return fn
    return deco


def get(name):
    return REGISTRY[name]


def names():
    return list(REGISTRY)


MODULES = ("noise_floor", "natlang", "subst", "fivecomp", "selfcite", "manual",
           "naibbe", "naibbe_wb", "verbose_det", "grille", "llull", "abbrev", "gibberish",
           "decorate", "linereset")


def load_all(strict=False):
    import importlib
    missing = []
    for m in MODULES:
        try:
            importlib.import_module(f"{__name__}.{m}")
        except ModuleNotFoundError:
            missing.append(m)
    if strict and missing:
        raise RuntimeError(f"generators not built yet: {missing}")
    return REGISTRY
