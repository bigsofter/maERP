# Continue the maTransports explainer-video series on this machine

You are taking over a production pipeline that was started on another computer. Episode 0 (the trailer) is finished
and approved in 4 languages; your job is to continue with **episode 1 (E01)** and onward, one episode at a time, in the
same style and with the same rigour. Everything you need is in this repo plus the handoff archive the owner gives you.

## The owner's brief (verbatim intent — keep it in mind on every decision)

> Make a dynamic 60–120 second motion-graphics video about each step [episode], one by one, that shows what an
> incredible motion designer you are. And not too fast — people should actually understand what the video is about.
> You can use components of the code to showcase [= redraw the REAL product UI components from the code; never show
> source code]. Use the HyperFrames explainer and the ElevenLabs API to generate audio in all necessary languages.
> Spawn parallel agents when necessary and don't use a strong model where Sonnet can do the job. No music — just
> accurate, dynamic, cool-looking visuals with a voice explaining. Decompose the plan into parts and do them one by
> one, each part in every language.
>
> Texts: `tools/demo-script/explainer/explainer.{ru,fr,en,es}.md`. Russian is the master text, the others are its
> translations. If something is called differently in the code and in the text, use the code's name — the customer
> will see the frontend.
>
> Watch grammar and cases in all languages; have a separate agent re-check.
> Keep the main context clean: spawn agents so the main session only receives what it needs.

## 1. Setup (do these in order; verify each; stop and ask the owner if one fails)

1. **Unpack the handoff archive at the repo root** (the owner will give you `maTransports-explainer-handoff-*.tar.gz`):
   `tar -xzf <archive> -C <repo-root>` → creates `tmp/explainer/series/…` and `tmp/explainer/facts/trailer/…`.
   `tmp/` is untracked scratch space inside the repo — **never commit it**.
2. **ElevenLabs key.** Ask the owner to create the key file themselves (you must never see, print or commit the key):
   `! printf 'ELEVENLABS_API_KEY=%s\n' 'PASTE_KEY_HERE' > tmp/explainer/.env`
   Verify with `tmp/explainer/series/tools/quota.sh` (prints tier, used/left, reset date — never the key).
3. **HyperFrames skills:** `npx skills add heygen-com/hyperframes`, then `npx hyperframes skills update faceless-explainer`.
   If your Skill tool doesn't list them until a restart, read the skill files from disk
   (`ls ~/.claude/skills ~/.agents/skills`) — `hyperframes-core/SKILL.md` + `references/` and
   `faceless-explainer/references/motion-language.md` are what the pipeline uses. Run `npx hyperframes doctor`.
4. **Tools:** Node ≥ 18, `ffmpeg`/`ffprobe`, Chrome (headless render), Python 3 with numpy + scipy:
   `python3 -m venv tmp/explainer/series/.venv && tmp/explainer/series/.venv/bin/pip install -r tmp/explainer/series/requirements.txt`
5. **Smoke test on the trailer** (costs 0 ElevenLabs chars — the audio is cached; this only rebuilds the WAVs from MP3):
   ```
   cd tmp/explainer/series/00-trailer
   for l in ru fr en es; do node ../tools/tts.mjs vo/$l.txt audio/$l $l; done   # expect "chars synthesised this run: 0"
   python3 build.py --timing | grep total      # expect ru 113.92, fr 117.04, en 119.18, es 118.57
   python3 build.py --lang fr --out build/_smoke-fr && (cd build/_smoke-fr && npx hyperframes lint)   # 0 errors
   ```

## 2. Read before planning (in this order)

1. `tmp/explainer/series/README.md` — **the playbook: owner's standing rules, the 14-step pipeline with model
   assignment and parallelism, decisions already taken, pitfalls.** It is binding. Save its §1 rules to your
   persistent memory if you have one.
2. `tmp/explainer/series/EPISODES.md` — all 44 episodes, suggested folder names, narration size per language.
3. `tmp/explainer/series/DESIGN.md` — the scene-worker guide (the visual and motion standard).
4. Look at `tmp/explainer/series/_reference/trailer-contact-sheet-{fr,ru}.png` (one frame per trailer scene) — this is
   the approved look. Skim `00-trailer/` as the worked example: `episode.json`, `vo/*.txt`, `i18n/`, `briefs/s0*.md`,
   `src/compositions/*.html`, `AUDIT.md`, `PRODUCT_BUGS.md`.
5. `tmp/explainer/series/prompts/` — templates for every agent (fact-check, proofread, worker, review, audit, fix, final
   gate). Give an agent a 1–3 line prompt: "Read <template> and follow it with {EP} = …, {SID} = …".
6. `tmp/explainer/facts/trailer/*.md` — already-verified facts (shell, devis, missions, driver app, documents,
   invoices, bank, forecast, margins, roles, branding) with file:line evidence; reuse them, re-verify only what the new
   episode adds.
7. The episode's card in `tools/demo-script/explainer/explainer.ru.md` (master) and the same section in fr/en/es.

The repo's own `CLAUDE.md` / `AI_GUIDE.md` orchestration gates (`.ai/bin/ai-*`) govern **product-code** changes. This
work does not change product code: don't edit anything outside `tmp/` (product i18n bugs are logged in the episode's
`PRODUCT_BUGS.md`, not fixed) unless the owner asks.

## 3. The task now

Produce **episode 1 — «E01 · Рабочее место: одна система вместо Excel, WhatsApp и папок»** in ru, fr, en, es, each
60–120 s, by the playbook (README §2): quota check → `tools/new_episode.sh 01-e01 "<heading>"` → parallel fact-check →
VO with code names → proofread → TTS → strings → timing → briefs → one Sonnet worker per scene in parallel → 4
per-language reviewers + fact auditor in parallel → per-scene fixers in parallel → final gate → `./render.sh` →
contact-sheet look → **report and stop**. Then wait for the owner's go before E02 (E01–E03 form "Part I").

Notes for E01:
- It overlaps the trailer's opening (Excel/WhatsApp/folders → one portal) — vary the staging, don't repeat the
  trailer's shots; keep the same visual language.
- fr narration is the longest (~1.7k chars): plan pauses so every language stays ≤ 120 s (`python3 build.py --timing`).
- The script's storyboard and claims are often wrong against the code (the trailer had ~20 fixes) — fact-check first.

## 4. Working style

- **Main session (you, the strongest model)**: plan, decide, write VO/copy/briefs, art-direct, run the gates.
  **Sonnet agents**: everything else (fact-check, build, review, fix, proofread, audit). Haiku only for trivial chores.
- **Parallelise** every independent step; you may start the next episode's fact-check while the current one renders
  (but do not start its TTS or build without the owner's go).
- Agents reply in ≤ 15–25 lines; long outputs go to files. Don't read raw transcripts, big dumps or many snapshots in
  the main session — one contact sheet per finished episode is your own visual check.
- Budget ElevenLabs: ~38 k chars available until 2026-11-02 (re-check with `tools/quota.sh`), an episode costs
  ≈ its Σ in EPISODES.md + ~10 % retakes. If the next episode won't fit, stop and ask the owner (upgrade or wait).
- **End-of-episode report** (then stop): the 4 MP4 paths in `tmp/explainer/series/_renders/` with durations; what
  changed vs the script and why (code names, false claims); product bugs found; ElevenLabs chars used / left; tokens
  (main session + sum of agent tokens from the task notifications).
- Owner's general rules: answer in the owner's language (they often write Russian); never print e-mail addresses,
  personal data or keys; never mention AI/Claude in commit messages (there should be no commits for this work anyway);
  if you use git worktrees, ask the owner what to do with them when done.
