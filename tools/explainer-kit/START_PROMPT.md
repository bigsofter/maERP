# maERP: демо-скрипт → серия видео-эксплейнеров → видеотека «по болям» на лендинге

Отвечай по-русски. Ты — Lead/режиссёр серии в репозитории `/Users/ivan-gurkin/Dev/maERP`.
Задача из трёх частей, все — до конца: **S** демо-скрипт (сценарий серии, в git maERP); **A** база коротких
motion-graphics видео о maERP в стиле серии maTransports; **B** видеотека на витрине maERP
(`tinycio.{ru,com,ma,es}/products/maerp`, **репозиторий tinycio**, `sites/tinycio-landing`), где ролики разложены
**по болям** владельца/финдиректора производственного или торгового предприятия, а не по разделам конфигурации.

Пайплайн — `tmp/explainer/` (НЕ в git; `tmp/` в `.git/info/exclude`). Если папки нет — разверни из
`tools/explainer-kit/` (см. `docs/plans/video-explainers.md`, раздел «Перенос»). Донор — серия maTransports:
образцы в `tools/explainer-kit/series/_donor/` и `tools/explainer-kit/donor-web/` (код видеотеки, планы, полный
сценарий); на машине владельца — `/Users/ivan-gurkin/orca/workspaces/maTransports/Видео-для-демо`.

## Чем maERP отличается от донора (учти до плана)

- **Это не SaaS, а конфигурация 1С:Предприятие 8.5** (`src/cf`, EDT: `.mdo` метаданные, `.bsl` модули, формы —
  `Form.form`). Интерфейс в роликах — формы 1С (Такси), перерисованные из РЕАЛЬНЫХ форм конфигурации: состав полей,
  команды, табличные части, подписи — из `.mdo`/`Form.form`, оформление — `docs/FORMS-STYLE.md`. Код (`.bsl`, запросы,
  имена реквизитов латиницей) на экране — никогда.
- **Подписи — синонимы метаданных на 4 языках** (Русский, Французский, Английский, Испанский в `Configuration.mdo`;
  в XML `<synonym><key>fr</key><value>…</value>`). `tools/ui_strings.py` донора читает JSON-каталоги web — перепиши
  под синонимы `.mdo`/`Form.form` (ключ = путь метаданных, напр. `Document.ЗаказКлиента.Attribute.Контрагент`).
  Французские строки проходят ревью носителем — `docs/FRENCH-REVIEW.xlsx`: брать проверенные.
- **Что реально есть** — `docs/ROADMAP.md`, `docs/CHANGELOG.md`, `docs/TECHDEBT.md`, механизмы по образцу УНФ
  (`docs/UNF-ADOPTION.md`), реестр тестов `docs/TESTING.md`/`TESTS.xlsx`. Кейсы клиентов — `docs/cases/*`
  (2MZL — производство под заказ, Isofroid) — источник болей; **в кадре** клиенты вымышленные, если владелец не скажет
  иначе (для кейса 2MZL раскрытие разрешено только в карточке кейса, не в видео).
- **Цена и онбординг** живут в хабе tinycio (`~/Dev/tinycio/docs/plans/feature-maerp-onboarding.md`: внедрение +
  абонплата за пользователя, модули на витрине — состав, не прайс; регистрация → аппрув → база) — в видео только то,
  что подтверждено там и в коде хаба.
- **Языки серии:** ru-мастер + fr/en/es (как у конфигурации и витрины). Решение владельца — в общем вопросе.

## 0. Подготовка

1. Правила: `CLAUDE.md` maERP (исходники только `src/cf`, `build/` и XML-выгрузку не трогать), `.ai/README.md`;
   для части B — `~/Dev/tinycio/CLAUDE.md`, `AI_GUIDE.md`, `AGENTS.md`, `sites/tinycio-landing/README.md`.
2. Плейбук серии: `tmp/explainer/series/README.md` (§1 обязательны), `DESIGN.md`, `prompts/`, эталоны `_donor/`.
3. Адаптация пайплайна (сделано: путь в `BATCH_ORCHESTRATOR.md`/`POLISH.md`, реферер `tinycio.ma` в `web_assets.mjs`,
   `titlePrefix: "maerp/"`). Остальное: тексты README/DESIGN/prompts про «TMS» → maERP (1С, формы Такси); пути кода
   (`src/cf`); `ui_strings.py` (выше); `publish.mjs`/`web_assets.mjs` — куда писать `videos.json`, `.vtt`, постеры:
   в репозиторий tinycio (`sites/tinycio-landing/...`), а не в maERP; `build.py` — шрифты (Manrope для кириллицы).
4. **Ключи и своя библиотека Bunny на месте** (созданы 2026-10-14): `tmp/explainer/.env` (`ELEVENLABS_API_KEY`,
   `BUNNY_API_KEY` — ключ аккаунта, `BUNNY_STREAM_LIBRARY_KEY` — ключ ЭТОЙ библиотеки; не печатать, не коммитить),
   `tmp/explainer/bunny.json`: библиотека **`maerp-explainers`** (id 779611), CDN-хост `vz-bceb3b94-d33.b-cdn.net`,
   настройки как у maTransports (без referrer'а → 403, MP4-fallback, 240p–1080p). **Referrer'ы разрешены:**
   `tinycio.{ma,com,es,ru}`, `www.tinycio.*`, `localhost`, `localhost:3000`. Если витрина переедет на
   `erp.tinycio.*` (см. `~/Dev/tinycio/docs/plans/1c-landing-*.md`) — добавить хосты через
   `POST https://api.bunny.net/videolibrary/779611/addAllowedReferrer {"Hostname":"…"}` (ключ аккаунта).
   Свой домен видео пока не нужен (`customHosts: {}`); захочет владелец — CNAME на CDN-хост + `video_hosts.mjs`.
   Квота ElevenLabs общая с maTransports/maOptique/ShukranPay (`tools/quota.sh`) — планируй объём вместе с владельцем.
   Окружение: venv + `pip install -r requirements.txt`; HyperFrames-скиллы глобально; пин `hyperframes@0.8.111`.

## S. Демо-скрипт — первым

Сценарий пишешь ТЫ по коду конфигурации (у донора сценарий заказчика врал в 5–20 местах на эпизод). Формат —
`_donor/script-sample.ru.md` и полный `donor-web/docs/explainer-script-full.ru.md`.
1. **Карта болей** (6–8, языком клиента): «заказ клиента теряется между продажами, закупкой и производством»,
   «не знаю себестоимость заказа до отгрузки», «склад и бухгалтерия расходятся», «французская отчётность и
   документы — вручную», … — только то, что снимают РЕАЛЬНЫЕ механизмы конфигурации (сверка с `src/cf` и ROADMAP).
2. **Эпизоды** (`tmp/explainer/series/EPISODES.md`): трейлер (~2 мин — сквозной путь заказа от клиента до денег) +
   «Знакомство» (рабочее место 1С, принципы форм) + «боль → как снимается», 60–120 с каждый + честный эпизод
   «что в разработке» (без сроков, которых нет в ROADMAP).
3. **Один вопрос владельцу** одним сообщением: карта болей, эпизоды, языки, можно ли упоминать реальные кейсы,
   промис финальной карточки (с витрины `/products/maerp`).
4. Сценарий — `docs/demo-script/explainer.{ru,fr,en,es}.md` в git maERP (ru — мастер), доказательства —
   `tmp/explainer/facts/<эп>/*.md` с путями `src/cf/...`.

## A. Производство роликов

Правила, решения владельца и ограничения машины — **как у донора без изменений** (подробно — в
`docs/plans/video-explainers.md` §A): ничего, чего нет в коде; подписи из синонимов того объекта/формы, где они стоят;
грамматика 4 языков + корректор; никакого кода; 60–120 с; без музыки; вымышленные компании; формат денег/дат — как
рисует форма 1С; голос «Daniel»; «Что вы получаете» — на финальной карточке; эталон (трейлер + E01) со стопом, затем
пакетный режим (`prompts/BATCH_ORCHESTRATOR.md`); ≤ 20 субагентов на машину, ≤ 5 запросов к ElevenLabs, рендер через
общий `tools/render_slot.sh`, чужие процессы не трогать, чистить диск. Баги конфигурации → `<эп>/PRODUCT_BUGS.md` →
`docs/plans/explainer-findings.md` (maERP) + промпт сессии доработок; конфигурацию в этой работе НЕ править.

## B. Видеотека на витрине maERP (репозиторий tinycio)

Работа в `~/Dev/tinycio` — своя ветка/worktree от свежего `main`, процесс tinycio (`CLAUDE.md`/`AI_GUIDE.md`, гейты
`.ai/bin` если есть); в tinycio параллельно работают сессии лендинга — согласуй через ветку, не правь их файлы.
Образец — `tools/explainer-kit/donor-web/` (видеотека maTransports). Витрина: `sites/tinycio-landing/app/products/maerp/`
(`fsd-pages/product-maerp/`), язык по домену (next-intl `getLocale()`, `messages/{ru,fr,en,es}.json`; сегмента
`[locale]` нет), каталог модулей — из Product Hub.
1. **`/products/maerp/videos`** — видеотека по болям (чипы, все карточки в HTML, якоря), группа «Знакомство» сверху;
   **`/products/maerp/videos/<slug>`** — страница эпизода: плеер (`preload="none"`), WebVTT с нашего origin,
   «какую боль снимает», 3 пункта, расшифровка, CTA заявки (как на витрине), OG с ЛОКАЛЬНЫМ постером, JSON-LD
   `VideoObject`, sitemap, hreflang по доменам tinycio.
2. **Входы:** «Смотреть видео · N мин» в первом экране `/products/maerp`, видео в блоках модулей/болей витрины,
   ссылка из меню продуктов (если продуктовое меню tinycio это допускает — `docs/plans/landing-products-menu-*.md`).
3. **Видео на страницах** — главный эпизод рядом с заголовком блока, «Видео по этой боли», навигация эпизода
   (крошки `?from=`, предыдущий/следующий, оглавление) — как у донора (`FeaturePage.tsx`, `RelatedVideos.tsx`,
   `EpisodeIndex.tsx`).
4. **Тексты витрины против продукта:** каждое обещание `/products/maerp` (и `products/1c/erp`, если про maERP) сверить
   с конфигурацией и хабом; неправду исправить, строки — в разделе E `docs/plans/explainer-findings.md` maERP;
   спорное — вопросом владельцу. Сверься с `docs/plans/landing-claims-registry.md` tinycio (реестр утверждений).
5. CSP `media-src` витрины — `vz-bceb3b94-d33.b-cdn.net`; тесты (как у донора) — по тестовой инфраструктуре tinycio.

## Разрешения и выкладка

Публикация в Bunny и выкладка витрины — только после явной фразы владельца («разрешаю публикацию …», «разрешаю
выкладку …»). Выкладка tinycio-landing — по процессу tinycio (`docs/`, `deploy/`), с merge свежего `main` и проверкой
на живом домене.

## Отчёты

После сценария — вопрос; после эталона — стоп; после пакета — сводка (эпизоды/MP4, правки против сценария, «Самое
важное» из багов, ElevenLabs, долги QA, что осталось по публикации и витрине — `docs/plans/video-library-rollout.md`).
