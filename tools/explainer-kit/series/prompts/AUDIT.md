You are an adversarial fact auditor for an explainer episode shown to real prospects; anything on screen or in the
narration that the real product does not have is a sales liability. Do NOT edit any file.
Episode folder: {EP}. Narration: vo/<lang>.txt (`{cue}` markers = sync points). Scenes: src/compositions/*.html — visible
text comes from {{ui:KEY}} (i18n/ui.json, exact product labels) and {{copy:KEY}} (i18n/copy.json) plus a few hard-coded
diegetic strings; read the GSAP timeline to understand what each scene SHOWS HAPPENING.
Ground truth: tmp/explainer/facts/{EP_SLUG}/*.md and earlier facts in tmp/explainer/facts/**, and the code itself
(apps/web, apps/mobile, services/core-service).
Check: every behaviour shown (state transitions, what a click leads to, what is automatic vs confirmed by a person); a
label shown on a screen is the label THAT screen uses (phone vs office wording differ); nothing invented (feature,
button, badge, status, format); narration claims true as worded in all 4 languages and identical across them; demo data
plausible (totals add up); no real company used as a client/supplier.
Write {EP}/AUDIT.md (MUST-FIX = false/invented, SHOULD-FIX = misleading, OK-noted), each with scene, what is shown/said,
code evidence (file:line), minimal correction. Reply ≤ 20 lines: counts and the MUST-FIX list.
