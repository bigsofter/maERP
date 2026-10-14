# Product issues found while making E01

The video shows the correct form; the product still shows the wrong one. Not fixed in the product (owner's rule).

| # | Where | Lang | Product shows | Problem | Suggested fix |
|---|---|---|---|---|---|
| 1 | `invoicing.st_overdue` (portal-data) | ru | «Просрочен · 34 дн.» on an invoice | «фактура» is feminine → «Просрочена» | «Просрочена · {days} дн.» or gender-free «Просрочка · {days} дн.» |
| 2 | `demo_counts` (shell) | ru | «{rows} строк» for any number | no plural forms: «16402 строк» should be «строки», «1 строк» → «строка» | ICU plural `{rows, plural, one {# строка} few {# строки} other {# строк}}` (fr/en/es: `one`/`other`) |
| 3 | `DemoBanner` counts line | all | raw number «16405», ISO dates «2025-04-03 → 2026-10-03» | everywhere else the product formats numbers fr-FR («16 405») and dates dd.MM.yyyy | format with the same helpers as `InvoicesView` (`formatDay`, grouped integers) |
| 4 | `/team` (TeamView) | all | button «Inviter un membre» | no action (fixture screen, TD-09); there is no way to add an employee after signup | known tech-debt; the video does not promise inviting a colleague |
| 5 | Team role labels | fr | «Exploitant» (signup), «Dispatcheur» (team fixture), «Opérateur / Dispatch» (DB); «Mécanicien» vs DB «Chef de parc» | three names for one role | pick one label per role and use it everywhere |
| 6 | `nav_operator` vs `operator.title` | en | menu «Operator desk», page title «Dispatcher desk» | two names for one screen | one name in both |
