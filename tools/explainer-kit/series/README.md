# maTransports explainer series — playbook

Narrated motion-graphics explainers (HyperFrames + ElevenLabs), one per episode of the customer's script,
each in **ru, fr, en, es**. Episode 0 (trailer) is delivered and approved as the style reference.

- Customer script (in git): `tools/demo-script/explainer/explainer.{ru,fr,en,es}.md` — **ru is the master**, the
  others are its translations. Each episode card = storyboard («Раскадровка»), voice-over («Закадровый текст», the
  `>` lines), on-screen titles («Титр»), and «Что вы получаете».
- Work folder: `tmp/explainer/series/` (inside the repo, **untracked — never commit it**). Facts live in
  `tmp/explainer/facts/<episode>/`. The ElevenLabs key lives in `tmp/explainer/.env` (`ELEVENLABS_API_KEY=...`).
- Plan and status of all 44 episodes: `EPISODES.md`. Deliverables: `_renders/<NN-slug>.<lang>.mp4`.

## 1. Owner's standing rules (binding)

1. **Nothing that is not in the code.** The script is often wrong. Every claim, label, behaviour and format shown or
   said is verified against the repo (`apps/web`, `apps/mobile`, `services/core-service`). The trailer had ~20
   corrections (e.g. "the bank reconciles itself" → only exact matches auto-reconcile, the rest is proposed and a person
   confirms; margins are not "always" two figures; only *required* documents block an assignment).
2. **Code names win.** If the script and the code call something differently, use the code's name — the customer sees
   the frontend. On-screen labels come from the product's i18n catalogs per language (`tools/ui_strings.py`). A label
   shown on a screen must be the one THAT screen uses (phone «En route» vs office «En transit»; ru devis screens say
   «рейс», mission screens «Миссия» — keep each screen's own word).
3. **Grammar in every language** — cases, gender, plurals with numbers, French typography. A separate proofreading
   agent checks the VO before TTS and the on-screen copy before render. Product templates filled mechanically are the
   usual culprits («{doc} просрочен» → «Водительское удостоверение просрочено»): show the correct form in the video and
   log the product string in the episode's `PRODUCT_BUGS.md`.
4. **No code on screen**, ever (no source, SQL, file paths, API codes). Proof is what a user sees in the UI.
5. **60–120 s per video**, every language. "Dynamic and cool-looking, but **not too fast** — people must actually
   understand." Clarity beats spectacle.
6. **No music.** Voice + sparse picture-locked SFX only.
7. **Delegate to keep the main context clean.** Agents do every heavy read/build/review and reply with ≤ 15–25 lines;
   long tables are generated into files by scripts, not printed. Main session = direction, briefs, decisions, gates.
8. **Models:** strongest model (the main session) plans, writes briefs, art-directs, decides, runs the final gate.
   **Sonnet** executes: fact-checks, scene builds, reviews, fixes, proofreading, audits. Haiku only for trivially
   mechanical chores. **Parallelise** everything independent (fact-check slices, scenes, per-language reviews, per-scene
   fixes; next episode's fact-check while the current one renders).
9. **Stop after each episode** (all 4 languages rendered) and report: paths, durations, what changed vs the script and
   why, product bugs found, ElevenLabs chars used / left, tokens (main + agents). Continue only when the owner says so.
10. Confidential data: never print e-mail addresses or personal data found in the repo/configs; never print the API key.

## 2. Pipeline for one episode

| # | Step | Who | Output |
|---|---|---|---|
| 0 | `tools/quota.sh` — enough ElevenLabs chars? (episode needs ≈ Σ in EPISODES.md + 10 %) | main | go / ask owner |
| 1 | `tools/new_episode.sh NN-slug "<heading>"` | main | episode folder |
| 2 | Fact-check: split the episode's claims into 2–4 domain slices; one agent per slice, **in parallel** (`prompts/FACTCHECK.md`) | Sonnet ×N | `tmp/explainer/facts/<ep>/*.md` |
| 3 | VO: write `vo/<lang>.txt` from the script with corrections (code names, true claims); one paragraph per line; `{cue}` markers before the words the picture syncs to — **same cue ids in the same order in all 4 files** (`python3 ../tools/vo_check.py`) | main | `vo/*.txt` |
| 4 | Proofread VO (`prompts/PROOFREAD.md`); apply must-fixes | Sonnet | `i18n/proofread.md` |
| 5 | TTS: `for l in ru fr en es; do node ../tools/tts.mjs vo/$l.txt audio/$l $l; done` (cached per paragraph — only changed lines are re-billed) | main (bg) | `audio/<lang>/` |
| 6 | Strings: list needed product keys in `i18n/ui-keys.txt` → `python3 ../tools/ui_strings.py i18n/ui-keys.txt i18n/ui.json`; compose `i18n/copy.json` (titles from the script's «Титр», filled templates, demo values) | main | `i18n/*.json` |
| 7 | Timing: fill `episode.json` (`gaps`, `scenes` = [id, file, start cue, lead]) → `python3 build.py --timing`; every language ≤ 120 s (tune `gap_scale` / `gap_override` / `tail_lang`; `tempo` ≤ 1.05 as last resort) | main | `episode.json` |
| 8 | Briefs: one `briefs/sNN.md` per scene — VO excerpt, cues, product truth, layout, time-coded shot sequence keyed to cues, SFX list, tokens; then `python3 ../tools/brief_tables.py` appends the 4-language string tables | main | `briefs/` |
| 9 | Build scenes: one agent per scene, **all in parallel** (`prompts/WORKER.md`) | Sonnet ×scenes | `src/compositions/sNN-*.html` |
| 10 | QA: 4 full-film reviewers (one per language, `prompts/REVIEW.md`) + 1 fact auditor (`prompts/AUDIT.md`), **in parallel**; second proofread of changed copy | Sonnet ×6 | `build/_review-*/REVIEW.md`, `AUDIT.md` |
| 11 | Fix: main decides what to change (copy/VO/timing itself; re-TTS changed paragraphs only), then one fix agent per scene, **in parallel** (`prompts/FIX.md`) | Sonnet ×scenes | updated scenes |
| 12 | Final gate (`prompts/FINAL_GATE.md`) | Sonnet | `build/_final-REPORT.md` |
| 13 | `./render.sh` (builds, lints, renders, loudness −16 LUFS) → `_renders/` ; main pulls one frame per scene into a contact sheet and looks | main (bg) | 4 MP4 |
| 13a | `node tools/publish.mjs <NN-slug>` — uploads the 4 MP4 to Bunny Stream (title `<episode>.<lang>`, re-render replaces), waits for encoding, rewrites `apps/web/components/landing/videos.json` (tracked — commit it with the page that uses the video). Keys: `BUNNY_STREAM_LIBRARY_KEY` in `tmp/explainer/.env`, library in `tmp/explainer/bunny.json` | main | manifest |
| 13b | (once per domain) `node tools/video_hosts.mjs [ma com es ru]` — after the owner adds `video CNAME vz-bcb32097-72a.b-cdn.net` at the registrar: free cert, force HTTPS, live 206 check; only then the domain enters `customHosts` of the landing manifest | main | manifest |
| 14 | Report to owner and stop | main | — |

Prompt templates in `prompts/` use placeholders (`{EP}` = episode folder repo-relative, `{SID}`, `{FILE}`, `{LANG}`,
`{EXTRA}`, `{CHANGES}`, `{DECISIONS}`, `{SLICE}`, `{CLAIMS}`, `{EPISODE_HEADING}`, `{EP_SLUG}`, `{N}`, `{SLICE_SLUG}`):
pass an agent a 1–3 line prompt "Read <template> and follow it with {X} = …".

## 3. How the build works (`<episode>/build.py`)

- Scene templates in `src/compositions/*.html` contain tokens: `{{ui:<key>}}` (exact product label), `{{copy:<key>}}`
  (composed/narrative text), `{{T}}` (scene timing JSON), `{{LANG}}`. The build writes one HyperFrames project per
  language into `build/<lang>/` (or `--out`), inlines fonts + `kit.css` + `kit.js` into `index.html`, places one voice
  clip per paragraph, renders the SFX track from each scene's `<script type="application/json" id="sNN-sfx">` block.
- **Each language keeps its own pacing**: paragraphs back to back + `gaps`; each scene starts at a cue minus `lead`;
  `T` gives every cue id in scene-local seconds plus `in`, `out` (exit start), `dur`. Scenes overlap 0.25 s.
- French typography (narrow no-break spaces, ’) is applied automatically to every token value.
- Russian display text uses Manrope (Sora has no Cyrillic) — set in `build.py` (`DISPLAY_FONT`).
- `--only s03 s04` builds an index with just those scenes (for workers); `--timing` prints the table.
- The SFX synth (`tools/sfxlib.py`, numpy + scipy) runs with `tmp/explainer/series/.venv/bin/python` if present,
  else `$SFX_PY`, else the current python.

## 4. Look and motion (keep it identical across the series)

The full worker guide is `DESIGN.md`. In short: deep-navy stage (`bg.html`) with soft glows and dot grid; product UI
redrawn at ~2× from the real tokens (dusk theme: dark rail, white topbar, light cards; driver app = dark cockpit with
amber action tiles); fonts Sora / Inter / JetBrains Mono (Manrope for ru display); lower-third title per beat
(amber bar + display text, bottom-left); motifs: source chip, lock, "new line on top", traffic light (red ONLY for a
refusal), numbered amber callouts, the amber "thread" = the trip. Motion: power3.out arrivals, power2.inOut travel,
no bounce, no loops, reveal on the voice cue, hold ≥ 1 s, camera moves only between beats, `K.*` helpers from
`kit.js` everywhere. Reference: `00-trailer/src/compositions/` and `_reference/trailer-contact-sheet-fr.png`.

## 5. Decisions already taken (don't re-litigate)

- Amounts are fr-FR formatted («30 000,00», «18,4 %») and dates dd.MM.yyyy **in every language** — that is what the
  product renders (`InvoicesView.formatAmount`, `formatDay`).
- Diegetic Moroccan data may stay French in every language (chat bubbles, sticky notes, bank wording «VIR …»,
  supplier names); illustrative catalogue line labels are translated per language for comprehension.
- Demo data comes from the seed but **no real companies** as clients/suppliers (the seed has Marjane, Cosumar, Leoni
  — don't show them). MERCADOMA SL / CITRUS SOUSS SARL are used (MERCADOMA resembles Mercadona — owner may rename).
- Closing card URL: `transport.tinycio.ma` (landing); product promise line «Votre espace de travail en 9 minutes».
- Voice: ElevenLabs «Daniel» `onwK4e9ZLuTAKqWW03F9`, model `eleven_v4`, same voice for all languages; Starter plan
  (commercial use OK, no credit line needed). If a language must shrink, prefer shorter pauses, then `tempo` ≤ 1.05.

## 6. Lessons from episode 0 (pitfalls)

- Titles appearing late is the #1 QA finding: every lower-third title must be fully readable ≥ 2.2 s before `T.out`.
- GSAP `fromTo` renders its from-state immediately → an element that waits for a later click (ripple, ring, tooltip)
  shows at 0,0 from t=0. Use `tl.set(el, from, at)` + `tl.to(el, to, at)` (kit's `K.click` already does).
- `npx hyperframes snapshot --at` with > 6 timestamps per call drifts ~0.5 s — batch small.
- `K.swap` overlapping texts trips `check` content_overlap — use a sequential crossfade.
- Short gaps between cues in one language compress beats; design every beat to read whether the gap is short or long,
  and give paragraphs whose picture needs time a longer `gaps` entry.
- When a narration claim changes, re-TTS only that paragraph (cache keys on text) and re-check totals ≤ 120 s.
- Workers must re-read `timing.json` after any VO/gap change; reviewers' times refer to their own build.
- Product bugs found go to `<episode>/PRODUCT_BUGS.md` AND into the repo plan `docs/plans/explainer-findings.md` (owner hands it to a parallel session) (trailer's list: `00-trailer/PRODUCT_BUGS.md`) — the video
  shows the correct form; never edit the product's catalogs without the owner asking.

## 7. Environment

Node ≥ 18, Python 3 with `pip install -r requirements.txt` (numpy, scipy) — recommended in `series/.venv`;
`ffmpeg`/`ffprobe`; Chrome (HyperFrames renders headless); HyperFrames skills (`npx skills add heygen-com/hyperframes`,
then `npx hyperframes skills update faceless-explainer`); `npx hyperframes doctor` to verify. Episode projects pin
`hyperframes@0.8.111` in `src/package.json`.
