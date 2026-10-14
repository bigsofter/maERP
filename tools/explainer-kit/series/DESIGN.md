# maTransports explainer series — scene worker guide (read fully before writing a line)

You build ONE scene of a 60–120 s narrated motion-graphics episode for **maTransports**, a TMS for
Moroccan road hauliers (Tanger Med → Europe). Every episode is rendered in **four languages (ru, fr, en, es)**
from the same scene file. `<EP>` below = the episode folder, e.g. `tmp/explainer/series/01-e01-workspace`
(paths are relative to the repo root). The audience is end users (dispatchers, accountants, owners) — **no code, SQL,
file paths or API words on screen, ever**. Everything shown must be what the real product shows; the
labels you need are given to you as tokens (exact strings from the product's own catalogs).

The bar: this has to look like the work of a top motion-design studio — calm, precise, physical,
expensive — and it must be EASY TO FOLLOW. The owner's words: "dynamic, cool-looking, but not too
fast; people must actually understand what the video is about." Clarity beats spectacle every time.

## 1. Your files

- You write exactly ONE file: `src/compositions/<your-scene-file>.html`. Never edit kit, build, other
  scenes, i18n, audio.
- Read first: this guide, your brief `<EP>/briefs/<sid>.md`, `<EP>/src/assets/kit.css`, `<EP>/src/assets/kit.js`,
  `<EP>/src/compositions/bg.html` (a minimal valid sub-composition), and from the installed HyperFrames skills
  (`ls ~/.claude/skills ~/.agents/skills 2>/dev/null` to locate them): `hyperframes-core/SKILL.md`,
  `hyperframes-core/references/sub-compositions.md`, `hyperframes-core/references/determinism-rules.md`.
- Style reference: `tmp/explainer/series/00-trailer/src/compositions/*.html` (the approved trailer) and
  `tmp/explainer/series/_reference/trailer-contact-sheet-fr.png`. Match that look and motion feel.
- Build & check (from `<EP>/`, use YOUR own out dir so workers don't collide):
  ```
  python3 build.py --lang es --only <sid> --out build/_w/<sid>-es   # SFX synth uses ../.venv (numpy+scipy) automatically
  cd build/_w/<sid>-es && npx hyperframes lint && npx hyperframes check
  npx hyperframes snapshot --at <t1>,<t2>,...     # ABSOLUTE times: scene start (see timing.json) + local time
  ```
  Look at every snapshot (Read the jpg/png files) in batches of ≤ 6 timestamps (bigger batches drift ~0.5 s).
  Do this for **es** and **ru** at least (longest texts; ru uses the Manrope display face), and fr once. `timing.json` in the out dir gives your scene's
  absolute `start` and its `T`.
- Workers write nothing else on disk except inside `build/_w/<sid>-*`.

## 2. Tokens (the build substitutes them per language)

- `{{ui:<key>}}` — an exact product label, e.g. `{{ui:web.quotes.st_accepted}}` → "Accepté"/"Принято"/…
- `{{copy:<key>}}` — composed or narrative text, e.g. `{{copy:s03.title}}`, `{{copy:demo.total}}`.
- `{{T}}` — your timing object. Use it as `const T = {{T}};` at the top of your script.
- Use ONLY keys listed in your brief. Never hard-code a visible word in any language (numbers/codes
  given as `copy:demo.*` tokens too). Icons/shapes are yours to draw (inline SVG).
- `T` (seconds, scene-local) has every voice cue id (e.g. `T.accept` = the instant the narrator says
  the word that cue marks), `T.in` (0), `T.out` (your exit starts), `T.dur`. Cues differ per language,
  so **every time in your timeline must be expressed from T** (`T.accept - 0.2`, `T.lines + 1.1`, …),
  never a bare number except tiny offsets. Each language then stays in sync with its own voice.
- Gaps between cues vary by language by up to ~1.5 s. Design each beat so it reads well whether the
  gap to the next cue is short or long (land the beat, then hold — holding is fine).

## 3. HyperFrames contract (violations break the render)

- File shape: `<template>` holding `<style>`, ONE root `<div id="<sid>-root" data-composition-id="<sid>"
  data-width="1920" data-height="1080">`, and `<script>`. Everything inside `<template>`.
- Root styled by id: `#<sid>-root { position:absolute; inset:0; overflow:hidden; }`. Prefix EVERY
  selector and id with `#<sid>-root` / `<sid>-` so nothing leaks across scenes.
- One `const tl = gsap.timeline({ paused: true });` … `window.__timelines["<sid>"] = tl;` at the end.
- Entrances with `fromTo` only. No `gsap.from`. No CSS transitions/animations/@keyframes. No
  `repeat`/`yoyo`. No `Math.random`, `Date.now`. No `<br>` in body text. No `class="clip"` needed
  inside your scene (the host clip is timed by the index) — don't add timed `data-start` children.
- Never put a CSS `transform` on an element you also tween with x/y/scale/rotation — set initial state
  in `fromTo`. Center with flex/inset, not translate(-50%).
- Transformed elements must be block/inline-block with a real size.
- Text: `max-width` + wrapping; long labels must fit the **longest language** (sizes in your brief).
  `white-space: nowrap` only on short labels you verified in es and ru.
- Fonts: `var(--f-display)` (titles, card titles, big numbers in display), `var(--f-body)` (UI text),
  `var(--f-mono)` (refs, amounts, codes). Never name a font family directly.
- SFX: put a block in your template:
  `<script type="application/json" id="<sid>-sfx">[{"cue":"accept","off":0.05,"type":"stamp","gain":1}]</script>`
  `cue` = any T key, `off` seconds after it, types: `click key type pop whoosh swell error stamp shimmer`.
  Sound is sparse and picture-locked: clicks on real clicks, soft `pop` on chips, `stamp` on a lock /
  status change, `error` ONLY on a red refusal, `whoosh` on big camera moves, `key` per typed digit.
  10–16 events in a scene is plenty. Gains 0.5–1.0.

## 4. The look (one film, nine scenes)

- **Stage**: deep navy with soft glows and a faint dot grid — painted by `bg.html` under every scene.
  Your scene's background is TRANSPARENT; you never paint a full-bleed backdrop.
- **Product surfaces** use the kit: `.k-card`, `.k-pill`, `.k-chip`, `.k-btn`, `.k-row`, `.k-alert`,
  `.k-shell/.k-rail/.k-topbar`, `.k-stepper`, `.k-phone` + `.k-tile`, `.k-cursor`, `.k-ripple`,
  `.k-callout`, `.k-title`. They are the real product's tokens at ~2× scale. Compose and size them;
  add scene-local CSS for layout. Do not restyle kit classes globally.
- **Scale & legibility**: UI text never under 20 px; the thing the narrator is talking about is big
  (key labels 26–34 px, key numbers 40–90 px). Fewer elements, bigger. Leave air: ≥ 100 px margins.
- **Depth**: cards float on the stage with the kit shadow. A card may arrive with a slight 3D tilt
  (`rotationY` ≤ 10°, `rotationX` ≤ 6°, `transformPerspective: 1600`) and settle flat. Focus by
  depth of field: when one element is the subject, dim the rest (opacity 0.35–0.5, `filter: blur(2–3px)`),
  then restore.
- **Camera**: wrap everything in `<div class="cam">` (entrance/exit) → `<div class="world">` (the
  camera you move). Move `.world` with x/y/scale (scale ≤ 1.4) to frame a detail or travel to the next
  station: 1.0–1.6 s, `power2.inOut` (K.MOVE), and ONLY between beats — never while the viewer must
  read. No slow drift, no breathing, no pan in the back half of a hold.
- **Motifs** (they recur across the film — use them where your brief says):
  - *Source chip* — small uppercase chip next to a computed number; pops with a soft click.
  - *Lock* — a padlock that snaps shut on something that can no longer change (amber glyph #FBBF24).
  - *New line on top* — a correction never edits: the old row stays, the new row slides in under it.
  - *Traffic light* — green / amber / red always mean ok / soon / stop. Red ONLY for a refusal.
  - *Callout ①②③* — numbered amber circle pointing at what to look at.
  - *The thread* — a thin amber line (#FBBF24, 3–4 px, round caps, soft glow) = the trip itself.
- **Lower-third title** (`.k-title` with `.k-title-bar` + `.k-title-text`): bottom-left. While a title
  is visible, keep the band y > 850 (and x < 1500) free of UI. `K.title(tl, el, t)` animates it.
  If your scene has two titles, `K.titleOut` the first before `K.title` of the second.

## 5. Motion doctrine (load-bearing)

1. **Smooth, never bouncy.** Arrivals `power3.out` (K.OUT) 0.5–0.9 s; travel `power2.inOut`;
   exits `power2.in`. No back/elastic/bounce. Pops scale from 0.7 with power3.out (no overshoot).
2. **Reveal on the voice.** Almost nothing is on screen at the start; each element arrives on ITS cue
   (≈ 0.1–0.25 s before the word, so picture and word land together). Never dump the scene in the
   first quarter. One new focal thing at a time.
3. **Hold.** After a beat lands, let it sit ≥ 1.0 s before the next motion (unless the next cue comes
   sooner). Still frames are fine. The only sanctioned "aliveness" in a hold is `K.jitter` (tiny),
   used rarely.
4. **Seams.** Your scene overlaps its neighbours by 0.25 s on each side. Start with
   `K.camIn(tl, cam, 0)` and end with `K.camOut(tl, cam, T.out)` unless your brief defines a custom seam.
5. **Clicks are physical.** Cursor travels (K.cursorTo, 0.7–0.9 s) → `K.click` (cursor dips, target
   presses, ripple) → the result appears 0.1–0.2 s after the click. Cursor enters from off-frame or
   fades in near its first target; it leaves (fade) when no longer needed.
6. **Numbers count** (K.count) only when the counting means something (a total forming); otherwise
   they simply appear.
7. Use `K.*` helpers for the shared moves so every scene feels like the same hand.

## 6. Return checklist

- [ ] Every lower-third title fully readable ≥ 2.2 s before T.out (≥ 2.0 s for a first title when there are two);
      any sentence the viewer must read visible ≥ 1.5 s.
- [ ] Nothing visible before its first use: never `fromTo` with a visible from-state on an element that waits
      for a later moment (GSAP renders the from-state immediately — that is how ripples sat at 0,0) — use
      `tl.set(el, {...}, at)` + `tl.to(...)`.
- [ ] `npx hyperframes lint` → 0 errors; `npx hyperframes check` → no findings on your elements
      (`#<sid>-*`), for es and ru builds.
- [ ] Snapshots read: at each cue + 0.8 s, and mid-hold, for es and ru (and one fr pass). Text fits,
      nothing clipped, nothing overlapping the title band, nothing important hidden.
- [ ] Every visible word comes from a token in your brief; no word hard-coded.
- [ ] Every timeline time derives from T.
- [ ] Return ≤ 15 lines: what you built, the snapshot times you checked, anything you could not do.
