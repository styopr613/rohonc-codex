"""Structural marks: glyphs that punctuate rather than mean.

Kiraly & Tokai's dictionary is a dictionary of words, so a glyph that marks
the end of a clause has no entry and every word carrying it comes out
unreadable. One such glyph exists and it is unmistakable.

E034 ends 293 words the dictionary does not define, and **99.7% of those
words are the last word of their run**, against 16.7% for words in general.
One occurrence in 293 is not. Nothing else in the book has that signature:
the next strongest candidate is run-final 55% of the time.

So E034 is a clause or line terminator, not a word. A word ending in it is
its stem plus a full stop, and reads as soon as the stem reads. That is 134
word types and 231 tokens recovered by a rule rather than a guess, and more
as stems are read.

This module is the one place that knows it, so the renderer, the gap finder
and the context printer agree.
"""

FULL_STOP = ""


def strip(code):
    """(stem, mark) -- mark is '.' if the code carries the terminator."""
    if len(code) > 1 and code.endswith(FULL_STOP):
        return code[:-1], "."
    return code, ""
