"""The manuscript's own TRAIN half, put through the identical measurement.

This is the row every other row is judged against. It is not a hypothesis: it
measures how far two halves of the same book sit apart when the only difference
between them is which leaves they are. A process whose error on a metric is at
or below this row has matched the manuscript as closely as the manuscript
matches itself, and nothing further can be claimed for it on that metric.

Unlike every other row it keeps its own paragraphs, line breaks and metadata
rather than being laid out on the shared spec. Laying real text onto sampled
metadata would scramble the association between words and sections, which is
precisely one of the things the line block measures, and would understate the
floor on exactly the metrics that matter most.
"""
import corpus
from . import register


@register("noise_floor", kind="real", label="manuscript, other half",
          note="not a hypothesis: the sampling floor between two halves of one book")
def generate(spec, train, seed=0):
    # match the held-out size using the spec's character budget
    target_chars = sum(sum(p.budgets) for p in spec)
    out, chars = [], 0
    for p in train:
        out.append(p)
        chars += sum(len(w) for ln in p.lines for w in ln)
        if chars >= target_chars:
            break
    return out, {"source": "TRAIN half, own paragraphs and metadata",
                 "paragraphs": len(out)}
