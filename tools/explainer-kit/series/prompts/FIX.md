You are fixing ONE scene of a maTransports explainer episode after a full QA round.
Episode folder (repo-relative): {EP}; paths below are relative to it.
Edit ONLY src/compositions/{FILE} (sid {SID}). Read tmp/explainer/series/DESIGN.md (binding), briefs/{SID}.md, src/assets/kit.css and kit.js first.

Changes since the scene was built (narration, timing, copy) are listed here by the director: {CHANGES}
The build is the truth — rebuild before judging; timings in the reports refer to the OLD build.

Inputs to fix — read the sections about {SID} in ALL of:
build/_review-ru/REVIEW.md, build/_review-fr/REVIEW.md, build/_review-en/REVIEW.md, build/_review-es/REVIEW.md, AUDIT.md.
Fix every MUST and SHOULD there for {SID}; fix NITs when cheap. Times in those reports refer to the OLD timing — re-locate each issue in the new build.
Decisions already taken by the director (do NOT re-litigate): amounts stay fr-FR formatted ("30 000,00", "18,4 %") and dates dd.MM.yyyy in EVERY language — that is what the product does; on-screen labels stay exactly the product tokens even where the product itself uses two words (ru "Миссия" vs "рейс"); diegetic Moroccan data (bank wording "VIR …", supplier names, chat bubbles) may stay French. Episode-specific: {DECISIONS}

Global rules for this pass (apply them even if no reviewer mentioned it):
- Every lower-third title must be FULLY revealed and readable for ≥ 2.2 s before T.out in every language. Bring it in at the moment its idea lands (usually the cue it belongs to + 0.2 … + 0.6), never later than T.out − 2.8. If two titles, the first must also get ≥ 2.0 s.
- Any text a viewer must read (alert, note, sentence) stays fully visible ≥ 1.5 s.
- Nothing within 60 px of the frame edges except deliberate full-bleed elements; nothing in the title band (y > 850, x < 1500) while a title is up.
- No element crossing/striking through text (threads, connectors, shields).
- Keep the "not too fast" feel: one focal change at a time.
Director notes for this scene: {EXTRA}

Verify: build es, ru, fr (and en once) with --only {SID} --out build/_w/{SID}fix-<lang>; lint + check clean for #{SID}-*; snapshot every cue+0.7, every title's mid-hold, T.out−0.2 and the scene start+0.3 — READ them. Iterate until clean.
Reply ≤ 12 lines: what you fixed (by reviewer item), anything you deliberately did not fix and why.
