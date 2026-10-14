You are fact-checking one slice of a narrated explainer episode for the maTransports TMS (repo root = the current
git repository). The video shows recreated product UI to real prospects, so every claim and every on-screen label must
match the CODE. Owner rule: when the script and the code name something differently, the CODE name wins.

Episode script: tools/demo-script/explainer/explainer.ru.md (master), section "{EPISODE_HEADING}" — storyboard
("Раскадровка"), voice-over ("Закадровый текст", the `>` lines) and "Что вы получаете". Translations: explainer.{fr,en,es}.md.
Earlier verified facts (reuse, don't redo): tmp/explainer/facts/**/*.md.

Your slice: {SLICE}
Claims to verify: {CLAIMS}

For each claim: verdict ✓ / ✗ / ~, evidence (file:line), and the correction when not ✓. For EVERY UI label you confirm,
give its i18n key and exact value in fr / ru / en / es — web: apps/web/i18n/messages/<lang>/*.json (top-level keys of
shell.json have no namespace), mobile: apps/mobile/src/i18n/<lang>.json. Say if a label is hard-coded. Also note how the
product FORMATS what you see (amounts are fr-FR "28 500,00" and dates dd.MM.yyyy in every locale — confirm if relevant).
Collect demo data usable on screen only from the demo seed (services/core-service/internal/service/demo*.go), with
file:line; never real company names as clients/suppliers (the seed contains some — flag them).
Write findings to tmp/explainer/facts/{EP_SLUG}/{N}-{SLICE_SLUG}.md. Do not edit anything else. No email addresses or
personal data in output. Reply ≤ 25 lines: the ✗/~ items and the key labels in 4 languages.
