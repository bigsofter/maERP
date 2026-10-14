# Proofread: 00-trailer (RU / FR / EN / ES)

Status: finished. Files read in full: vo/{ru,fr,en,es}.txt, i18n/copy.json, i18n/ui.json. No file edited except this report.
Format: file + key/line -> current -> corrected -> why.

## RU

### Must fix
1. copy.json demo.queue_1 (ru) -> "1 ждут отправки" -> "1 ждёт отправки" -> число 1 требует единственного числа (шаблон queue_pending склеен механически).
2. copy.json demo.mission_title (ru) -> "Миссия M-1042" -> "Рейс M-1042" -> в трейлере (VO и demo.mission_title_quote, s03.title) то же самое называется "рейс"; два названия в одном языке.

### Optional
- copy.json demo.week6_detail: "Неделя 6 — строк: 4" -> "Неделя 6 — 4 строки" -> "строк: 4" грамматически допустимо, но на экране звучит как служебное; значение известно, можно подставить готовую форму.
- copy.json demo.margin_after_label: "после 116 520,00 распределённых накладных" -> "после 116 520,00 MAD распределённых накладных расходов" -> без валюты число читается как количество; "накладные" в перевозках ещё и накладные CMR, двусмысленно.
- vo/ru.txt l.8: "после накладных" -> "после накладных расходов" -> та же двусмысленность (накладная = транспортный документ).
- copy.json s05.title2: "Ошибка — только авуаром" -> "Ошибка — только кредит-нотой" -> "авуар" это французская калька, носитель русского её не использует (в продукте тоже "Авуар", см. product bugs).
- vo/ru.txt l.6: "машина или водитель ... не встанут" -> допустимо; при желании "не будут назначены на рейс" -> "на рейс не встанут" разговорное.

## FR

### Must fix
1. copy.json demo.week6_detail (fr) -> "Semaine 6 — 4 ligne(s)" -> "Semaine 6 — 4 lignes" -> значение известно (4), "ligne(s)" это недозаполненный шаблон.
2. vo/fr.txt (l.2, 5, 6, 7, 8) и copy.json demo.event_status, demo.gate (fr): перед « : ; ? ! » и внутри « » обычный пробел (nbsp/U+202F нигде нет). Исправить: "fois :" -> "fois :" (узкий неразрывный перед ; ? ! и ":" допускается  ), "« combien il y aura en fin de trimestre »" -> "« combien ... trimestre »", "Statut : En transit" -> "Statut : En transit", "affecté : Permis" -> "affecté : Permis". Причина: типографика, возможен перенос строки перед двоеточием в субтитрах и на экране.
   Затронутые места VO: l.2 "fois :", l.5 "téléphone :", l.6 "cher :", l.7 "même ;" (после "mêmes"? это "se rapprochent d’elles-mêmes ;") и «…» в l.7.

### Optional
- vo/fr.txt l.2: "dispatcheur" -> "exploitant" (в продукте роль называется "Exploitant", team_roles.dispatcher) -> единый термин; "dispatcheur" допустим, но не совпадает с интерфейсом.
- vo/fr.txt l.10 и copy.json s09.tagline: "au même endroit" -> "en un seul endroit" -> мастер RU "в одном месте" (в одном, а не в том же); s02.title уже "Un seul endroit".
- Термины: "voyage" (l.2, l.10, s02, s09) и "mission" (l.3, l.4) для одного объекта; мастер использует один "рейс". Допустимо как слоган, но если нужна строгость, l.2 "un voyage" -> "une mission" (и "tout le voyage" -> "toute la mission").
- copy.json demo.queue_1 (fr) "1 en attente d’envoi" верно.
- Цифры 28 500,00 и т.п. с обычным пробелом: заменить на U+202F, чтобы число не рвалось (касается всех языков, см. общий пункт).

## EN

### Must fix
1. vo/en.txt l.6: "a truck or a driver with an expired paper won’t be put on a mission" -> "a truck or a driver with an expired document won’t be assigned to a mission" -> "an expired paper" не говорят (paper как документ только во мн.ч. "papers"/"paperwork"); "put on a mission" неестественно.
2. copy.json s05.title1 (en): "An expired paper keeps the truck in the yard." -> "An expired document keeps the truck in the yard." -> то же.
3. copy.json demo.week6_detail (en): "Week 6 — 4 line(s)" -> "Week 6 — 4 lines" -> число известно.

### Optional
- vo/en.txt l.7: "doesn’t tell you where you’ll be at the end of the quarter" -> "doesn’t tell you how much cash you’ll have at the end of the quarter" -> мастер "сколько будет" (сумма), EN теряет смысл "сколько".
- vo/en.txt l.3: "brings the whole mission together in a single dossier" -> "brings the mission together in a single dossier" -> слово "whole" добавлено, в RU его нет (но в слогане "whole trip" есть; допустимо).
- Термины: "trip" (l.2, l.10, s02, s09, demo.note_missions "38 invoiced trips") и "mission" (l.3, l.4, s03, demo.mission_title) для одного объекта. Рекомендация: везде "mission" (как в продукте) или везде "trip"; "38 invoiced missions".
- copy.json demo.err_cmr (en): "Consignment note not signed for M-1042." -> "CMR not signed for M-1042." -> везде (VO, ui invoicing.cmr_pending) используется "CMR".
- Цифры с обычным пробелом (см. общий пункт).

## ES

### Must fix
1. copy.json demo.queue_1 (es): "1 pendientes de envío" -> "1 pendiente de envío" -> число 1 требует единственного числа.
2. copy.json demo.week6_detail (es): "Semana 6 — 4 línea(s)" -> "Semana 6 — 4 líneas" -> число известно.

### Optional
- vo/es.txt l.4: "se calcula con sus tarifas" -> "se calcula con su tarifario" (или "con su tabla de tarifas") -> RU "по вашей тарифной сетке": теряется понятие сетки, которое есть в FR/EN (grille, grid).
- vo/es.txt l.4: "se convierte en misión con un clic, con las mismas líneas" -> "se convierte en misión con un clic y con las mismas líneas" -> два "con" подряд, звучит рублено.
- vo/es.txt l.6 и s05.title1: "papel caducado" -> "documento caducado" -> в продукте "documento", "papel" разговорно.
- vo/es.txt l.6: "no sale a ruta" -> "no se asigna a ninguna misión" -> RU "на рейс не встанут" (назначение), ES говорит о выезде.
- vo/es.txt l.2: "jefe de tráfico" vs ui "Operador de tráfico" (team_roles.dispatcher) -> выбрать один термин.
- Термины: "viaje" (l.2, l.10) и "misión" (l.3, l.4) для одного объекта (как FR/EN).
- Типографика: кавычки «» последовательны, "¿¡" не требуются; ничего не найдено.

## Общие (все языки)
- Числа с тысячами в copy.json (demo.amt1, amt2, total, bank*_amt, floor, margin_*) разделены обычным пробелом: заменить на U+202F/U+00A0, иначе "28" и "500,00" могут разъехаться по строкам. Optional.
- Проверено без замечаний: s01.* (намеренно французские), даты, коды документов, склонения "Две маржи. Никогда одна." (ru), "Dos márgenes. Nunca uno." (es), "Jamais mélangées" (fr).

## Product bugs (ui.json, это ошибки самого продукта)

Must fix (реальные ошибки):
1. web.missions.gate_doc_expired (ru): "{doc} просрочен {date}" -> род зависит от документа (удостоверение = ср.р.: "просрочено", страховка = ж.р.: "просрочена", паспорт, полис ...). Нужны формы по роду документа (или безличный оборот: "{doc}: срок истёк {date}"). Это источник ошибки, пойманной владельцем. Аналогично FR "{doc} expiré le {date}" сломается для "Assurance" (-> "expirée"), "Carte" и т.п.; ES "{doc} caducado" для "Licencia/Tarjeta" (-> "caducada").
2. app.board.queue_pending (ru): "{count} ждут отправки" -> нужна плюрализация (1 ждёт, 2-4 ждут, 5+ ждут). ES: "{count} pendientes de envío" -> 1 "pendiente". FR/EN: плюрализация корректна для 1 ("1 en attente", "1 waiting").
3. web.forecast.week_detail: "строк: {count}" / "{count} ligne(s)" / "{count} line(s)" / "{count} línea(s)" -> плюрализация через ICU plural (4 строки, 1 строка, 5 строк; 1 ligne, 4 lignes ...). Скобочные "(s)" это незаконченный шаблон.
4. web.forecast.kind_effet (en): "Paper" -> "Bill of exchange" (или "Promissory note") -> "Paper" ничего не значит как вид платёжного документа.
5. web.group_pilotage (es): "Pilotaje" -> "Gestión" (или "Control de gestión") -> pilotaje это управление воздушным судном; галлицизм.
6. web.missions.page_step_economy (en): "Economy" -> "Economics" -> рядом sec_economy_title уже "Economics"; "Economy" (класс обслуживания/экономика страны) неверно.

Optional (стиль, непоследовательность):
- Термины рейс/миссия (ru): web.nav_missions "Миссии", missions.page_edit_title "Миссия M-{number}" vs quotes.act_create_mission "Создать рейс", quotes.open_mission "Рейс M-{number}". Выбрать одно.
- Термины счёт/фактура (ru): web.invoicing.title "Счета" vs nav_factures "Фактуры" vs treasury.doc_invoice "Фактура"; плюс kind_bill "Счёт поставщика". Статусы st_approved "Выставлен" / st_credited "Сторнирован авуаром" мужского рода, что согласуется только со "счёт"; для "фактура" нужно "Выставлена", "Сторнирована".
- web.invoicing.act_credit (ru) "Авуар" -> "Кредит-нота" (калька с французского).
- Термин CMR (en): invoicing.err_cmr "Consignment note not signed for {list}." vs cmr_pending "CMR not signed" -> "CMR not signed for {list}."
- web.quotes.title (ru) "Коммерческие предложения" vs nav_devis "Предложения" -> единообразие.
- web.group_pilotage (en) "Steering" -> "Management"/"Control" (калька).
- web.missions.sale_total (es) "Total servicios vendidos" -> "Total de servicios vendidos".
- web.nav_pouls (fr) "Pouls entreprise" -> "Pouls de l’entreprise"; missions.page_save_draft (fr) "Enregistrer brouillon" -> "Enregistrer le brouillon"; app.login.subtitle (fr) "Entrez votre numéro" -> "Entrez votre numéro de téléphone"; app.login.verify (fr) "Entrer" -> "Se connecter".
- Апострофы (fr): invoicing.note_draft "l'émission" и treasury.sec_candidates "Ce qu'elle" прямые ('), в остальном каталоге типографские (’) -> "l’émission", "Ce qu’elle".
- Статусы app.status.in_transit: en "On the road" / fr "En route" vs web.mission_status "In transit" / "En transit" -> один термин на статус.
- fr: перед « : » в ui.json стоит обычный пробел (event_status_changed, gate_blocked, note_accepted, code_office, note_draft, note_locked, overhead_on/off) -> nbsp.
- web.finance.margin_after_label (ru): "после {amount} распределённых накладных" -> см. RU optional, добавлять "расходов" и валюту.
