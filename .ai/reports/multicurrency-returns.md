# multicurrency-returns — возвраты, налоговые накладные, прочие расходы, переработка в валюте (2.0.16.25)

План: docs/plans/multicurrency-returns.md. Codex в лимите — все обязательные гейты на субагентах Claude.

| Гейт | Итог |
|---|---|
| ai-review-plan (architecture-critic) | approve_with_changes, 5 × P1 внесены в план |
| ai-review (код) | request_changes: P0 (серверный вызов клиентской процедуры в форме прочих расходов), P1 (налоговые отчёты складывали валюту с основной) → исправлено |
| ai-database | approve_with_changes (P2: точная `СуммаРегл` накладной, тест переноса оплат) → исправлено, остальное — TECHDEBT |
| ai-review --verify | approve; P3 по документации исправлены после круга |
| ai-test / ai-final-check | 6/6 гейтов; уровни 1–3 и EDT — у владельца |

Отчёты: .ai/reviews/multicurrency-returns/01…04-*-claude.md. Открытое — TECHDEBT «Документы в валюте».
