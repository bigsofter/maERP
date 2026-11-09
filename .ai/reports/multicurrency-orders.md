# multicurrency-orders — заказы, КП и предложения поставщиков в валюте (2.0.16.24)

План: docs/plans/multicurrency-orders.md. Codex в лимите — все обязательные гейты на субагентах Claude.

| Гейт | Итог |
|---|---|
| ai-review-plan (architecture-critic) | approve_with_changes, 4 × P1 внесены в план |
| ai-review (код) | approve_with_changes (2 × P2, 4 × P3) → исправлено |
| ai-database | approve_with_changes (P2: курс при вводе на основании — в «Что нового») |
| ai-review --verify | approve_with_changes; остаток (тексты, пересчёт копии) исправлен после круга |
| ai-test / ai-final-check | 6/6 гейтов; уровни 1–3 и EDT — у владельца |

Отчёты: .ai/reviews/multicurrency-orders/01…04-*-claude.md. Открытое — TECHDEBT «Документы в валюте».
