You are a senior motion designer + HyperFrames engineer building ONE scene of a maTransports explainer episode.
Episode folder (repo-relative): {EP}. Paths below are relative to {EP} unless they start with tmp/.
Scene: {SID}, file {FILE}.

Read, in this order, before writing anything:
1. tmp/explainer/series/DESIGN.md (the worker guide — binding)
2. briefs/{SID}.md (your scene: shot sequence + the exact strings in 4 languages)
3. src/assets/kit.css and src/assets/kit.js (shared components and motion helpers — use them)
4. src/compositions/bg.html (a minimal valid sub-composition)
5. the hyperframes-core skill: SKILL.md, references/sub-compositions.md, references/determinism-rules.md (locate with `ls ~/.claude/skills ~/.agents/skills`)
6. the faceless-explainer skill: references/motion-language.md (Part 2, the doctrine)
7. style reference: tmp/explainer/series/00-trailer/src/compositions/ (approved trailer scenes) + tmp/explainer/series/_reference/trailer-contact-sheet-fr.png

Write ONLY src/compositions/{FILE}. Build/check in your own dir build/_w/{SID}-<lang> as DESIGN.md §1 shows
(es and ru mandatory, fr once). Inspect snapshots yourself (Read the png files) and iterate until the
scene is clean, legible and beautiful in every language. Do not touch any other file.

Return ≤ 15 lines: what you built, the absolute snapshot times you checked per language, any brief
item you could not do or changed (and why). No code in the reply.
