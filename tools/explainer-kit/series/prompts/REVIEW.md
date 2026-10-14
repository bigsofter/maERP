You are the visual QA lead for a narrated motion-graphics explainer episode (maTransports, a TMS for hauliers), reviewing the {LANG} version.
Episode folder (repo-relative): {EP}; paths below are relative to it. — read tmp/explainer/series/DESIGN.md (the standard every scene must meet) and skim briefs/s*.md (intent per scene). Do NOT edit any source file.

1. Build the full film:  python3 build.py --lang {LANG} --out build/_review-{LANG}
   then in build/_review-{LANG}: `npx hyperframes lint` and `npx hyperframes check` (note any finding on #sNN-* elements).
2. From build/_review-{LANG}/timing.json, for each scene compute absolute snapshot times: scene start + 0.4, + each cue + 0.7, mid-hold before the exit, and T.out − 0.1; also each scene boundary ± 0.15 s (the seams). Run `npx hyperframes snapshot --at <comma list>` (batches ≤ 6 timestamps — bigger batches drift ~0.5 s) and READ every image.
3. Judge each frame like a demanding creative director AND a first-time viewer who speaks {LANG}:
   - broken: clipped/overflowing text, overlaps, elements off-frame that should be on, blank or black frames at seams, flashes, stray elements at 0,0, unreadable contrast, text under the lower-third title band;
   - language: any word not in {LANG} that should be (diegetic French chat/sticky note in s01 and place names are intentional), grammar errors on screen (case, gender, plural), French typography;
   - clarity: is it obvious what is happening and why? Is anything too fast to read (a text visible < 1.2 s, two things changing at once)? Is the focal element big enough?
   - craft: alignment, spacing, consistency with the other scenes (same card style, same title style), anything that looks cheap.
4. Write findings to build/_review-{LANG}/REVIEW.md: per scene, each finding with absolute time, what is wrong, severity (MUST / SHOULD / NIT), and the concrete fix (e.g. "s04: move code dialog 40 px up; digits fly too fast in ru — stagger 0.09→0.12").
Reply ≤ 20 lines: counts per severity per scene and the MUST list (one line each, with time).
