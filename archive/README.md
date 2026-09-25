# Archive

Files that are no longer part of the edition, kept because the record of how a
reading changed is itself evidence.

## backups-20260922/ (moved off the repository 2026-09-25)

Now at `~/backups/voynich-archive-backups-20260922/` on Rachel, 211 files, 33 MB, out of
every release zip. Git keeps their history up to that day. What it was:

Every `*.pre-*` file that had accumulated in the working tree: 195 of them, 179
already tracked by git and moved with `git mv`, so their history is intact.
They are snapshots taken before an edit, under the house rule of backing up
before changing a file.

They were archived because they had stopped being a safety net and started
being camouflage. A tree with a hundred and seventy-nine dead files in it is a
tree where nobody can see which file is live, and on 2026-09-22 that cost a
day: a checker was reading `retelling.md`, a draft superseded when Book One was
rewritten, and its 1,142 quotations made it look like the strictest gate in the
project while the printed book went unchecked.

**The rule now.** Back up before editing, as before. But a backup belongs here
once the edit is committed, because git already holds the history of anything
tracked. Nothing in this directory is read by any program. If a program ever
needs a file in here, that is a bug in the program, not a reason to move the
file back.

## superseded-20260923/

`NEXT.md`, a one-page handoff written on 2026-09-20 when 105 of the 441 folios
had been translated. It was superseded within two days by `METHOD.md`, which
carries the same loop and keeps its arithmetic current, and by the session
handoff, which is no longer tracked. Nothing read it. It is kept because it
records what the state of the reading was on that date, and it is out of the
root because a stale count in a file called NEXT.md is a trap.
