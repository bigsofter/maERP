# Промпт на начало разработки в хабе tinycio: онбординг maERP

Скопировать в новую сессию Claude Code в `~/Dev/tinycio` целиком. Это §15 плана
`docs/plans/feature-maerp-onboarding.md` того репозитория, развёрнутый под первую фазу.
Парный промпт по maERP — `docs/hub/stage12a-headless-first-run-prompt.md`.

---

Реализуй фичу **«maERP: онбординг через хаб»** по плану
`docs/plans/feature-maerp-onboarding.md` — прочитай его целиком, затем сверь §1 с кодом:
head миграций по папкам `services/*/migrations` (реестр `docs/ai/data/migrations.generated.md`
отстаёт), номера строк в `handler.go`, `routes.go`, `writes.go`. Волна `maerp-onboarding` в
`docs/plans/STATUS.yaml` уже заведена со статусом `planned` — переведи в `in_progress` первым
коммитом.

Перед P1 собери бриф по скиллу `task-brief` (STATUS.yaml, AGENTS.md затронутых каталогов —
`services/product-service`, `services/client-service`, `services/sales-service`,
`services/api-gateway`, `web`, `deploy`; grep CLAUDE.md по `product-hub`, `service_objects`,
`stage_graph`), покажи красную команду проверки фазы и только потом пиши код.

Строго по фазам P1 → P5 (§13), после каждой: коммит → деплой безопасным паттерном
(`deploy/AGENTS.md`: migrator отдельным `run --rm`, `up -d --build --no-deps <svc>`,
`nginx -s reload` последним) → команда проверки фазы → **стоп на подтверждение**. Один
репозиторий — tinycio; работы §14 (скрипты на 1С-сервере, headless-первый запуск) идут в
maERP отдельной сессией, их не делай и не жди — в P2 раннер проверяется fake-скриптом из
`testdata/`.

Конвенции: `httpx.ErrorJSON`, `ListXxxFilter`, `EventPublisher`, `RequireServiceToken`,
`svchttp.Client`; cross-DB только soft-ref + HTTP (ADR-001); каждый новый wildcard-роут
product-service прогоняется `TestRegisterHasNoRouteConflicts`; секреты раннеров — `secrets.Box`
(AES-GCM, показ один раз как `RotateWebhookSecret`); пароли пользователей 1С не пишутся ни в
`provisioning_jobs.result`, ни в логи — только одноразовый `credentials_enc`; публичные роуты —
только `publicMux`, тело вебхуков раннера форвардить сырым. Фронт портала — inline-стили,
`apiFetch`, max-lines 400, экраны products-hub manager-only. Лендинг — SSR через
`TINYCIO_API_INTERNAL_URL`, браузер ходит только в `/hub/*` (на tinycio.* nginx уводит `/api/*`
в sitebot); файл `ProductMaERPPage.tsx` не рефакторить, новые секции — в `sections/`.
Миграции: client 033, product 011/012, sales 056 → `node tools/gen-schema-docs.mjs` тем же
коммитом; `node tools/status-check.mjs` зелёный; в P1 не забудь WON-хук sales (§6: поиск объекта
по `type_code`, иначе у клиента появится второй объект обслуживания).

Открытые вопросы §12 не решай сам: §12.1–12.5 задай владельцу до начала P3 одним списком с
вариантами и своей рекомендацией; до ответа P1–P2 идут без них. Цены модулей не сидировать —
лендинг показывает «по запросу», пока владелец не заполнит «Модули и цены».

Коммиты по-русски, `feat|fix(область): …`; doc-хук блокирует первый `git commit` — повтори ту
же команду. После P5 — секция в CLAUDE.md (журнал) с инвариантами и граблями,
`docs/ai/services/product-service.md`, `docs/ai/contracts/maerp-runner.md`.

Начни с P1.
