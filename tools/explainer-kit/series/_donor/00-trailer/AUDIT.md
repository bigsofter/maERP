# AUDIT: trailer 00 (maTransports). Статус: закончено

Проверено: vo/{fr,ru,en,es}.txt, i18n/copy.json, i18n/ui.json, s01-s09 (разметка + GSAP-таймлайны), отчёты facts/trailer/1-4, код apps/web, apps/mobile, services/core-service. Файлов не правил.
Счёт: MUST-FIX 2, SHOULD-FIX 10, OK-noted 14.

## MUST-FIX (ложь или выдумка)

### M1. s04: пилюли очереди телефона показаны внутри карточки ОФИСА (метка на чужом экране)
- Показано: в веб-досье "Mission M-1042" (#s04-mview, #s04-pills, справа в шапке карточки) появляются "1 en attente d'envoi" (amber), затем "Tout est envoyé" (green). Токены app.board.queue_pending / app.board.queue_synced (copy: demo.queue_1).
- Код: эта пилюля живёт на ленте заданий ТЕЛЕФОНА: apps/mobile/app/(tabs)/index.tsx:68 (tone sky при ожидании, green при пусто). В веб-досье миссии такой пилюли нет (facts/2-driver-docs.md: pending queue UI только мобильный; офис очередь телефона не видит, он видит уже доставленное вложение). Сцена показывает офис, знающий об очереди телефона до отправки.
- Правка: убрать #s04-q1/#s04-q2 из #s04-mview и показать их на экране телефона (шапка списка заданий, где они реально есть; либо оставить на телефоне только подписи фото "En attente" -> "Envoyée", они уже есть: mission/[id]/index.tsx:302). В офисе до sg+0.2 вложения быть не должно, после - только "Pièces jointes" + "depuis l'app".

### M2. Нарратив и заголовок s07: "маржа ВСЕГДА двумя числами / Jamais une seule" (все 4 языка)
- Сказано: fr "la marge s'affiche toujours en deux chiffres ... Jamais mélangées"; en "margin always comes as two figures"; ru "маржа — всегда двумя числами"; es "el margen, siempre con dos cifras". Заголовок s07: "Deux marges. Jamais une seule." / "Two margins. Never one." / "Две маржи. Никогда одна." / "Dos márgenes. Nunca uno."
- Код: при выключенном распределении накладных вторая цифра НЕ считается (margin_after = null, экран показывает margin_after_off "seule la marge directe est calculée"): FinanceView.tsx:150-168, finance.go:157 (MarginAfter nil). Эту самую ситуацию сцена s07 сама и показывает (кнопка "Désactiver", вторая цифра исчезает). Плюс карточка миссии (lib/missions-view.ts:1165-1184) и /executive (kpi_margin_pct) показывают одну "Marge directe". Противоречие внутри ролика: "всегда две" и кадр, где одна.
- Правка (минимальная): убрать "всегда/toujours/always/siempre" и "jamais une seule": "Et la marge s'affiche en deux chiffres : directe ... et nette ... Jamais mélangées." Заголовок: "Deux marges, jamais mélangées" (ru "Две маржи. Не смешиваются.", en "Two margins. Never mixed.", es "Dos márgenes. Nunca mezclados.").

## SHOULD-FIX (вводит в заблуждение / неточно)

### S1. s05 + VO guard: "un papier expiré" слишком широко (все языки; заголовок s05.title1)
- Код: гейт блокирует только ОБЯЗАТЕЛЬНЫЕ документы: водитель permis+cin; тягач carte_grise+insurance+visite_technique; прицеп insurance+visite_technique; непросроченность по valid_until (fleet_gate.go:5-30, 58-62). Остальные (ADR, виза, паспорт) "never block" (fleet_gate.go:20-23). Блокирует и ОТСУТСТВИЕ документа.
- Правка: "un camion ou un chauffeur dont un document obligatoire est expiré ne part pas en mission" (en "a required document"; ru "обязательной бумагой"; es "un papel obligatorio"). Заголовок: "Un papier obligatoire expiré...".

### S2. VO money: "La prévision ne vous dit pas «combien en fin de trimestre»" (все языки)
- Код: прогноз как раз показывает остаток по неделям (таблица, col_closing "Solde fin", 13 недель = квартал; ForecastView) и карта "Position à 91 j" на странице Банк (TreasuryView.tsx:179, treasury.m_projected). Фраза "не говорит" неверна буквально.
- Правка: "La prévision ne se contente pas de dire «combien en fin de trimestre» : elle montre la semaine où ça deviendra difficile." (en "doesn't just tell you...", ru "не только показывает «сколько будет...»", es "no se limita a decir...").

### S3. s04 логин: один экран вместо двух шагов
- Показано (#s04-login): заголовок "Code de connexion" + подзаголовок "Entrez votre numéro" + поле "+212 6•• ••• •••" + 6 боксов кода + "Entrer" одновременно.
- Код: apps/mobile/app/login.tsx:77-121: шаг 1 "phone" (заголовок "Entrez votre numéro", кнопка next), шаг 2 "code" (заголовок "Code de connexion", текст "Demandez le code au bureau...", ОДНО поле с разрядкой, placeholder "6 chiffres", кнопка "Entrer"). Заголовок "Code de connexion" и "Entrez votre numéro" на одном экране не бывают.
- Правка: показать сначала экран телефона (subtitle + поле), затем экран кода (code_title + поле + "Entrer"); или убрать lg-sub и поле телефона со второго экрана.

### S4. s04: "Hors ligne" как баннер и цвет пилюли очереди
- Код: офлайн - серый текст (index.tsx:72-75; mission/[id]/index.tsx:153, показывается при fromCache), не баннер; пилюля очереди tone sky при ожидании (index.tsx:68), в сцене amber. Косметика, но "баннер" - выдуманный элемент.
- Правка: серый "Hors ligne" под шапкой; пилюля sky.

### S5. s06: знак "+" и дата без года в выписке; "+" в прогнозе
- Показано: "+ 30 000,00", "+ 94 800,00", "− 18 240,00" (выписка), "+ 41 200,00" (детализация недели), даты "06.10"/"07.10".
- Код: TreasuryView.tsx:260 и ForecastView.tsx:310 используют formatAmount без "+" (минус только у расходов в прогнозе: `line.side==='in' ? '' : '−'`); даты везде dd.MM.yyyy (InvoicesView.tsx:319). Формат "28 500,00" (fr-FR) соблюдён.
- Правка: убрать "+ " у приходов, даты "06.10.2026".
- Плюс: даты выписки 06.10/07.10 позже даты кода "03.10.2026" и "сегодня" сцены - выписка из будущего; сдвинуть на 29.09-01.10.2026.

### S6. s06: легенда прогноза "Seuil de trésorerie 180 000,00 MAD" - это подпись ПОЛЯ настройки
- Код: f_floor - метка настройки; под графиком продукт пишет curve_baseline: "Ligne de base : le seuil de {floor} {cur}. La hauteur d'une barre, c'est ce qui reste au-dessus." (ForecastView.tsx:394, amber 10.5px). ru f_floor "Неснижаемый остаток" там не используется на графике.
- Правка: легенду заменить на curve_baseline (ui-ключ web.forecast.curve_baseline) или оставить как условную подпись, не выдавая за подпись экрана.

### S7. s08: цвет пилюли "Émise" зелёный, в s05 синий; в коде approved = sky (lib/invoices-view.ts:38)
- Правка: в s08 `k-pill is-blue` как в s05.

### S8. s02: заголовок секции "1. Cadre" и моно-знак
- Код: заголовок секции "1. Cadre de la mission" (missions.sec_frame_title), "Cadre" только в степпере. Моно-знак рейла в s02 рисует линию "T", в продукте янтарный грузовик на градиентном квадрате (Brand.tsx; s09 рисует правильно).
- Правка: ui-ключ web.missions.sec_frame_title; в s02 использовать тот же грузовик, что в s09/icon.svg.

### S9. VO guard: "une facture sans CMR signé n'est pas émise" без оговорок
- Код: гейт работает только при подключённом модуле cmr и только для строк с миссией; отказывает ПРИ ВЫПУСКЕ ("Émettre"), не при создании черновика (invoice.go:502-552, 525, 598). В сцене показан именно выпуск - верно. Нарратив верен для демо-тенанта с модулем CMR.
- Правка (необязательная): "avec le module CMR" не нужна в ролике, но не обещать "всегда" в маркетинг-тексте. Оставить как OK, если ролик всегда демонстрируется на тенанте с CMR.

### S10. VO/title s03: "en un clic"
- Факт: accept работает только из статуса "Envoyé" (draft сначала "Envoyer"), "Créer la mission" - только owner/dispatcher (sales нет): quote.go:11-104, lib/quotes-view.ts:26. Нарратив "Un devis accepté devient une mission en un clic" - верно (accepté -> mission = один клик). Заголовок s03 "Du devis à la mission en un clic" шире: devis -> accepté -> mission = два клика (Accepter, Créer la mission), в самой сцене два клика.
- Правка: заголовок "Un devis accepté devient une mission en un clic" (ru "Принятое предложение — рейс одним кликом", en "An accepted quote becomes a mission in one click", es "Un presupuesto aceptado, misión en un clic").

## OK-noted (проверено, верно или допустимо)
1. s03/VO: чипы "tarif client" (28 500,00) и "catalogue" (1 500,00), Passage scanner из шаблона TC Export, Total HT = TTC 30 000,00 при "Exonéré (art. 92-35)" (экспорт): demo_quotes.go:40-50, quotes.exempt. Копирование строк в миссию "Issue du devis DV-2026-0012", чип "devis", раздел "8. Économie" / "Services vendus au client", Total = Σ HT до сантима: quote_mission.go:64-77, MissionPage.tsx:816-819.
2. s03 переходы: Envoyé -> Accepter -> Accepté (+ note_accepted), затем "Créer la mission" -> "Voir la mission" + "Mission M-1042" (ru "Рейс M-1042" на экране devis, "Миссия M-1042" на экране миссии - как в коде).
3. s02: 9 шагов степпера в топбаре, подписи верны (Cadre ... Documents); рейл Exploitation: Travail/Données/Documents, активный Missions, затем Devis. Опущен "Groupage" (lock) - допустимое сокращение.
4. s04 метки по экранам верны: телефон "En route" (app.status.in_transit), офис "Statut : En transit" (portal mission_status); ru оба "В пути", en "On the road" (phone) / "In transit" (office). Код "Inviter dans l'app" -> диалог "Code de connexion", "Valable jusqu'au 03.10.2026 · usage unique" (6 цифр, одноразовый). "Changer le statut — 1 tap", loading -> in_transit разрешён (mission/[id]/index.tsx:20-33). Фото: "Photo", "En attente" -> "Envoyée", в офисе "Pièces jointes" + "depuis l'app". Нюанс: в чек-лист строку "CMR" фото попадает только из списка документов, через кнопку Photo - в "Pièces jointes" (как и показано).
5. s05 гейт: текст "Youssef Benali ne peut pas être affecté : Permis de conduire expiré le 14.09.2026" - точная сборка gate_blocked + gate_doc_expired + doctypes.permis; отказ (409 assignment_blocked), не предупреждение; в "7. Ressources" (MissionPageContainer.tsx:143-153).
6. s05 CMR: "CMR non signé" -> "Émettre" -> "CMR non signé pour M-1042." -> "CMR reçu" (InvoiceForm.tsx:311, err_cmr). Нумерация: FA-2026-0412 при выпуске, "Brouillon: modifiable et sans numéro", "Document émis ... corrige par un avoir", AV-2026-0007 своя серия; формат FA/AV-YYYY-NNNN верен; последовательность непрерывна per-tenant per-year (invoice.go:918-929).
7. s06 банк: автосвязь только при совпадении суммы И номера в назначении ("VIR MERCADOMA SL FA-2026-0398", чипы "auto", "montant + référence"); вторая строка без номера - только предложение "Ce qu'elle pourrait régler" -> клик по кандидату = onMatch (TreasuryView.tsx:379) - "propose, vous confirmez" верно (treasury.go:794-846).
8. s06 прогноз: 13 недель (default horizon), порог = базовая линия, бары от порога, неделя ниже порога amber (bg-amber-400, ForecastView.tsx:382), остальные синие, клик по неделе открывает "Semaine 6 — 4 lignes" с колонками Nature/Tiers/Pièce/Montant, типы "Facture fourn."/"Effet"/"Facture", карта "Point de rupture · Semaine 6". Арифметика недели: +41 200 -64 300 -48 000 -37 900 = -109 000.
9. s07: подписи margin_title/before/after, формат "+ 412 860,00 MAD · 18,4 %" и "+ 296 340,00 13,2 %" (signed(), formatPct), "38 missions facturées"; 412 860 - 116 520 = 296 340 (net < direct, 18,4 % и 13,2 % согласованы с базой около 2,24 млн). Переключатель: статус "Répartition des frais généraux : activée/désactivée" + кнопка "Désactiver/Activer" - вкладка "Frais généraux"; панель Verdict выводится над вкладками (FinanceView.tsx:94), поэтому на одном экране; кнопка только при canEdit. При выключении прямая цифра остаётся, нетто заменяется margin_after_off - верно.
10. s08: данные изолированы (RLS на каждой мультитенантной таблице), роли: подписи из signup team_roles + owner "Propriétaire" (в UI /team подписи другие - фикстура; лендинг: "Directeur, dispatcheur"); число ролей в ролике не названо - корректно (7-я tinycio_admin внутренняя). "Documents gelés" верно для facture/avoir/BC/принятого devis; утверждённый счёт ПОСТАВЩИКА редактируем (purchase.go:688-691) - в ролике не показан. "Corrections en nouvelles lignes": invoice_payments (отрицательная строка), cash.balance_entries (append-only по GRANT), avoir.
11. s09: тэглайн "Tout le voyage, au même endroit" совпадает с озвучкой; URL transport.tinycio.ma - живой маркетинговый хост (tinycio-umbrella.conf:69; логин на my.transport.tinycio.ma). "9 minutes" - официальная цифра лендинга (landing.json cta.title, hero.stat3); в коде не измеряется, в озвучке не звучит.
12. Реальные компании: в кадре клиенты MERCADOMA SL, CITRUS SOUSS SARL - вымышленные имена демо-сида (demo.go:701-710), реальных марок (COSUMAR, MARJANE, LEONI, ATLAS BOTTLING из сида) в сценах НЕТ. Поставщики "STATION ATLAS CARBURANT", "PNEUS DU DÉTROIT", "GARAGE NORD POIDS LOURDS" (s06) - вымышленные. Риск: MERCADOMA созвучно Mercadona (испанская сеть) - при желании переименовать (например "MERCAMURCIA SL"). "Excel", "WhatsApp" - в заголовке s01 как названия классов инструментов (сторонние товарные знаки, не клиенты); при тревоге о правах - "Таблицы. Мессенджер. Папки."
13. Форматы: суммы "28 500,00" (fr-FR группировка во всех языках, copy.json совпадает), даты dd.MM.yyyy (03.10.2026, 14.09.2026), DV-2026-0012, FA-2026-0412, AV-2026-0007, M-1042 - всё как в коде. Номер миссии без нуля/года (M-1042).
14. Согласованность 4 языков: смысл абзацев fr/en/ru/es совпадает (проверены все 9 абзацев, ключевые утверждения те же; одни и те же оговорки S1/S2/M2 затрагивают все четыре). Расхождения только стилистические: ru нарратив говорит "рейс", а на экранах миссии "Миссия" (в devis-экранах "Рейс") - это внутренняя непоследовательность продукта (facts/1), не ошибка ролика.

## Временное
Временных файлов не создавал; записан только этот AUDIT.md.
