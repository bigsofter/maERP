# Polish pass on a rendered episode (2026-10-04)

You fix the KNOWN defects of one already-rendered episode `{EP}` and re-render only the languages that change.
Working dir: `tmp/explainer/series/` of the worktree `/Users/ivan-gurkin/Dev/maERP`.
Answer the main session in Russian, ≤ 20 lines.

Read first: `README.md` (playbook — owner rules §1 are binding), `DESIGN.md`, `prompts/FIX.md`, `{EP}/CHANGES.md`,
`{EP}/AUDIT.md` if present, the scene file(s) concerned and `{EP}/build/<lang>/timing.json`.

## Defects to fix (owner scope: ONLY these — no redesigns, no VO/TTS changes unless stated)
{DEFECTS}

## Method
1. Locate each defect in the scene HTML. Confirm it on a snapshot of the language(s) concerned
   (`python3 build.py --lang <l>` then `npx hyperframes snapshot --at t1,t2,… ` from `build/<l>/`, ≤ 6 timestamps per call;
   heavy snapshot batches go through `../tools/render_slot.sh`).
2. Fix in `src/compositions/*.html` / `i18n/copy.json` (copy changes: product labels stay from `i18n/ui.json`; any changed
   on-screen copy must be proofread for grammar in all 4 languages — do it yourself carefully, French typography is automatic).
   A fix in a shared scene affects all languages: re-check the other languages that render that scene too.
3. Verify on fresh snapshots that the defect is gone and nothing new appeared (titles readable ≥ 2.2 s before `T.out`,
   nothing off-frame, no overlap). `npx hyperframes lint` = 0 errors.
4. Render ONLY the changed languages: from `{EP}/`: `HF_CAPTURE_PARALLEL_STREAM=true ../tools/render_slot.sh ./render.sh <langs>`
   (run in background and wait; one render ≈ 2–3 min per language once a slot is free; other sessions share the 2 slots).
   Check each new `_renders/{EP}.<l>.mp4`: ffprobe duration 60–120 s; pull 1 frame per fixed scene (`ffmpeg -ss … -frames:v 1`)
   and LOOK at it.
5. Append a dated «Доводка 2026-10-04» section to `{EP}/CHANGES.md`: what was fixed, languages re-rendered, new durations,
   what you deliberately left and why. Then delete `{EP}/build/*/renders` and any `_review-*`/`_w` dirs to free disk.

## Hard limits
- Never kill/pkill processes you did not start; never delete `/tmp/matransports-render-slots`.
- No code on screen; no music; do not edit anything outside `{EP}/` (and `_renders/{EP}.*`); never touch git.
- Never print e-mails, personal data or API keys. No ElevenLabs calls unless the defect list says so.
- A real product bug you notice → one line in `{EP}/PRODUCT_BUGS.md`, mention it in the reply; do not fix the product.

Reply: per defect fixed / left (why), languages re-rendered with durations, frames you looked at.
