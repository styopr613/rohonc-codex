# Prospective occurrence holdout

Created 2026-09-29 after the compact-folio parser correction exposed that
Tests 1 and 6 were not genuine holdouts.

`manifest.json` was frozen first from seed 20260929. `prompt.txt` contains one
training folio per sampled sign, K&T's words only, and no project gloss,
evidence note, translation, sign code, or concealed-folio label. The reply in
`reply.json` was then obtained in one stateless OpenRouter call to
`deepseek/deepseek-v3.2`, reasoning disabled, and saved before scoring.

The primary score is Test 1's declared rule: any content stem of the frozen
answer occurs in the concealed folio's cited passage. Requiring every answer
stem and applying Test 6's word-order score were added after the reply and are
labelled post-hoc sensitivities. No outcome bar was declared before this run,
so the result is reported without a PASS or FAIL verdict.
