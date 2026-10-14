# Product i18n issues found while making the trailer

The video shows the correct form; the product still shows the wrong one. Files: `apps/web/i18n/messages/<lang>/*.json`, `apps/mobile/src/i18n/<lang>.json`.

| # | Key | Lang | Product shows | Problem | Suggested fix |
|---|---|---|---|---|---|
| 1 | `missions.gate_doc_expired` (portal-work) | ru | «Водительское удостоверение просрочен 14.09.2026» | `{doc} просрочен {date}` ignores the document's gender (удостоверение = neuter) | «{doc}: срок истёк {date}» (gender-free) |
| 2 | same | fr / es | «… expiré le …» / «… caducado el …» | same agreement problem for feminine document names (e.g. «carte grise», «visita técnica») | fr «{doc} : expiré(e) le» → better «{doc} — échéance dépassée le {date}»; es «{doc}: caducó el {date}» |
| 3 | `board.queue_pending` (mobile) | ru / es | «1 ждут отправки» / «1 pendientes de envío» | no plural forms | ICU plural: ru `{count, plural, one {# ждёт} few {# ждут} many {# ждут} other {# ждут}} отправки`; es `one {# pendiente} other {# pendientes}` |
| 4 | `forecast.week_detail` (portal-data) | fr / en / es | «4 ligne(s)», «4 line(s)», «4 línea(s)» | "(s)" instead of a plural | ICU plural |
| 5 | `forecast.curve_baseline` | ru | «Высота столбца это запас над ним.» | missing dash | «Высота столбца — это запас над ним.» |
| 6 | several (e.g. `invoicing.cmr_warning`, `forecast.curve_baseline`) | fr | `l'émission`, `d'une` | straight apostrophe where the rest of the catalog uses ’ | use ’ consistently |
| 7 | `forecast.kind_effet` | en | «Paper» | not the English term | «Bill of exchange» |
| 8 | `group_pilotage` (shell) | es | «Pilotaje» | unusual in Spanish business UI | «Gestión» |
| 9 | `missions.page_step_economy` vs `sec_economy_title` | en | «Economy» vs «Economics» | two words for one section | «Economics» in both |
| 10 | terminology | ru | «Миссия» (missions screens) vs «рейс» (devis screens); «Счета» (invoices title) vs «Фактуры» (menu) | one thing, two names | pick one per concept |

Not bugs, kept as-is in the video on purpose: amounts always fr-FR («30 000,00») and dates dd.MM.yyyy in every language (that is what the product renders); «Авуар» in ru.
