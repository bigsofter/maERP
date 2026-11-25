#!/usr/bin/env python3
"""Сверка прав ролей. Две проверки, у каждой — дефект, который у администратора
(все права по умолчанию) не воспроизводится:

1. У ссылочного объекта с правом «Просмотр» должно быть и «Ввод по строке».
   Без него поле ввода не подбирает значение по набранному тексту —
   пользователь видит только историю выбора (ОператорПроизводства, 2026-11-01).
   Явный запрет (<value>false</value>) при «Просмотре» тоже расхождение: иначе
   дефект возвращается одной правкой роли. Исключение — объекты, где «Ввод по
   строке» явно снят у роли «Администратор» (служебные ПВХ и план счетов): это
   эталон, другие роли его не расширяют.
2. Роль, которая видит документ, видит и его команды печати (Commands/Печать*).
   Без права на команду меню «Печать» формы и закладок рабочих мест её не
   показывает (акты переработки у оператора производства, 2026-11-01).
   Исключения:
   - PRICE_COMMANDS: формы с ценами у роли, от которой суммы скрыты
     (ФирменнаяПечать.ЦеныСкрыты): нефирменные формы с ценами и фирменные без
     варианта «без цен». Печать им всё равно отказывает на сервере при любом
     наборе ролей (ПечатныеФормы.ПроверитьПечатьБезЦен) — право только
     показало бы кнопку, которая падает;
   - EXTERNAL_ROLES: роли клиентов и обмена. Фирменная печать читает
     подписантов и тарифные ставки организации, а эти роли их не читают и
     читать не должны. Их печать — отдельное решение владельца.
   Командой печати считается команда документа с именем «Печать*» или с
   модулем, вызывающим печать (АктОбОказанииУслуг, PrintLettreDePaiement).

3. Роль вне EXTERNAL_ROLES, которая видит хоть одну команду печати документа, видит
   и окно печати CommonForm.ПечатьДокументов. Без него каждая печать падает
   «Недостаточно прав для просмотра»: права 26.08 остались на удалённой форме
   ПредварительныйПросмотр, окно открывал только администратор (тикет 2605475,
   2026-11-15).
4. Право роли на общую форму, которой нет в CommonForms, — висячее: так и
   осталось незамеченным переименование окна печати.
5. Роль вне NAV_EXTERNAL_ROLES, которая видит объект (обработку, отчёт, справочник,
   документ, регистр), видит и его команды навигации: группы NavigationPanel*,
   FormNavigationPanel*, «Отчёты» и «Перейти». Право на команду у ролей без
   «независимых прав подчинённых» отдельное: без него команды нет в меню раздела и в
   панели «Перейти», хотя объект роли доступен. Открытие при запуске
   (ОткрытьФорму) этого права не требует — так АРМ закупок и производства пропали
   из раздела «Производство» у оператора и складских ордеров, а живая проверка
   через автозапуск их видела (тикет 2605465, 2026-11-19). Команды печати — п. 2,
   «Отправить почтой» и действия в командной панели формы — решение по роли, не
   проверяются. NAV_BROKEN — команды с неверным обработчиком: право им не выдаётся,
   пока обработчик не исправлен (docs/TECHDEBT.md).

Проверяются все роли: роль без своего права на клиент работает в паре с другой
(«Складские ордера» с «Оператором производства»).

Использование: scripts/rolecheck.py [каталог EDT-проекта или его src]. Код возврата 1 — есть
расхождения.

6. Рабочая роль (с правами запуска, вне NAV_EXTERNAL_ROLES), которой разрешён тонкий
   клиент, запускает и веб-клиент: иначе пользователь входит с рабочего места и не
   входит через браузер (решение владельца 2026-11-22).
"""
import os
import re
import sys
import unicodedata

KINDS = ("Catalog.", "Document.", "ChartOfCharacteristicTypes.", "ChartOfAccounts.",
         "ExchangePlan.", "BusinessProcess.", "Task.", "ChartOfCalculationTypes.")
OBJECT = re.compile(r"<object>\s*<name>([^<]+)</name>(.*?)</object>", re.S)
RIGHT = re.compile(r"<name>(\w+)</name>\s*<value>(\w+)</value>")
EXTERNAL_ROLES = ("Клиент", "ECommerce", "ОбменМобильнаяДоставка")
NAV_EXTERNAL_ROLES = EXTERNAL_ROLES + ("ЛичныйКабинет", "MobileClient")
NAV_GROUPS = ("NavigationPanel", "FormNavigationPanel", "CommandGroup.Отчёты", "CommandGroup.Перейти")
FOLDERS = {"Catalog": "Catalogs", "Document": "Documents", "DataProcessor": "DataProcessors", "Report": "Reports",
           "InformationRegister": "InformationRegisters", "AccumulationRegister": "AccumulationRegisters",
           "AccountingRegister": "AccountingRegisters", "CalculationRegister": "CalculationRegisters",
           "ChartOfCharacteristicTypes": "ChartsOfCharacteristicTypes", "ChartOfAccounts": "ChartsOfAccounts",
           "ChartOfCalculationTypes": "ChartsOfCalculationTypes", "ExchangePlan": "ExchangePlans",
           "BusinessProcess": "BusinessProcesses", "Task": "Tasks", "DocumentJournal": "DocumentJournals"}
# Команда «Планирование закупок» открывает «Ведомость по продажам» (обработчик скопирован) — TECHDEBT.
NAV_BROKEN = ("Report.ПланированиеЗакупок.Command.ВедомостьПоПродажам",)
COMMAND = re.compile(r"<commands uuid=\"[^\"]*\">(.*?)</commands>", re.S)
PRINT_FORM = "CommonForm.ПечатьДокументов"
PRICE_COMMANDS = {
    "ОператорПроизводства": (
        "Document.ЗаказПокупателя.Command.ПечатьПроформа",
        "Document.РеализацияТоваровУслуг.Command.ПечатьТоварнаяНакладная",
        "Document.РеализацияТоваровУслуг.Command.ПечатьСчетНаОплату",
        "Document.РеализацияТоваровУслуг.Command.ПечатьЧека",
        "Document.РеализацияТоваровУслуг.Command.ПечатьЧекаНаПринтер",
        "Document.ВозвратОтПокупателя.Command.ПечатьЧека",
        "Document.ВозвратОтПокупателя.Command.ПечатьЧекаНаПринтер",
        "Document.ПоступлениеТоваровУслуг.Command.ПечатьПоступлениеТоваров",
    ),
    # Мобильный пересчёт видит документ, но печати и себестоимости в нём нет: без права на команду сервер печатает
    # опись без сумм (Документы.ПересчётТоваров.Печать, docs/plans/inventory-print.md).
    "MobileClient": (
        "Document.ПересчётТоваров.Command.ПечатьИнвентаризационнаяОпись",
        "Document.ПересчётТоваров.Command.ПечатьСличительнаяВедомость",
    ),
}


def print_commands(src_dir, document):
    folder = os.path.join(src_dir, "Documents", document, "Commands")
    if not os.path.isdir(folder):
        return []
    commands = []
    for name in sorted(os.listdir(folder)):
        module = os.path.join(folder, name, "CommandModule.bsl")
        text = open(module, encoding="utf-8").read() if os.path.exists(module) else ""
        # Имя каталога на диске бывает в NFD («й» разложена), а Rights.rights и платформа - в NFC.
        name = unicodedata.normalize("NFC", name)
        if name.startswith("Печать") or "ПечатныеФормыКлиент." in text:
            commands.append(name)
    return commands


def navigation_commands(src_dir, name, cache={}):
    """Команды навигации объекта метаданных «Вид.Имя»: имена команд из его .mdo."""
    if name not in cache:
        kind, short = name.split(".")
        path = os.path.join(src_dir, FOLDERS.get(kind, ""), short, short + ".mdo")
        if kind not in FOLDERS or not os.path.exists(path):
            path = os.path.join(src_dir, FOLDERS.get(kind, ""), unicodedata.normalize("NFD", short),
                                unicodedata.normalize("NFD", short) + ".mdo")
        text = unicodedata.normalize("NFC", open(path, encoding="utf-8").read()) if os.path.exists(path) else ""
        result = []
        for block in COMMAND.finditer(text):
            command = re.search(r"<name>([^<]+)</name>", block.group(1)).group(1)
            group = re.search(r"<group>([^<]+)</group>", block.group(1))
            if group and group.group(1).startswith(NAV_GROUPS):
                result.append(command)
        cache[name] = result
    return cache[name]


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "src", "cf")
    roles = os.path.join(src, "Roles")
    if not os.path.isdir(roles):
        src = os.path.join(src, "src")
        roles = os.path.join(src, "Roles")
    admin = open(os.path.join(roles, "Администратор", "Rights.rights"), encoding="utf-8").read()
    denied = {match.group(1) for match in OBJECT.finditer(admin)
              if dict(RIGHT.findall(match.group(2))).get("InputByString") == "false"}
    common_forms = {unicodedata.normalize("NFC", name) for name in os.listdir(os.path.join(src, "CommonForms"))}
    findings = []
    for role in sorted(os.listdir(roles)):
        path = os.path.join(roles, role, "Rights.rights")
        if not os.path.exists(path):
            continue
        text = unicodedata.normalize("NFC", open(path, encoding="utf-8").read())
        if "<setForNewObjects>true" in text:
            continue
        objects = {match.group(1): dict(RIGHT.findall(match.group(2))) for match in OBJECT.finditer(text)}
        for name in objects:
            if name.startswith("CommonForm.") and name.split(".", 1)[1] not in common_forms:
                findings.append(f"Право на несуществующую общую форму — {role}: {name}")
        sees_print = False
        for name, rights in objects.items():
            if not name.startswith(KINDS) or name.count(".") != 1 or rights.get("View") != "true":
                continue
            if name not in denied and rights.get("InputByString") != "true":
                findings.append(f"Просмотр без «Ввода по строке» — {role}: {name}")
            if not name.startswith("Document.") or role in EXTERNAL_ROLES:
                continue
            for command in print_commands(src, name.split(".")[1]):
                full = f"{name}.Command.{command}"
                if full in PRICE_COMMANDS.get(role, ()):
                    if objects.get(full, {}).get("View") == "true":
                        findings.append(f"Форма с ценами у роли без цен — {role}: {full}")
                elif objects.get(full, {}).get("View") != "true":
                    findings.append(f"Документ виден, команда печати нет — {role}: {full}")
        for name, rights in objects.items():
            if (name.startswith("Document.") and ".Command." in name and rights.get("View") == "true"
                    and name.split(".Command.")[1] in print_commands(src, name.split(".")[1])):
                sees_print = True
                break
        if unicodedata.normalize("NFC", role) not in NAV_EXTERNAL_ROLES:
            for name, rights in objects.items():
                if name.count(".") != 1 or rights.get("View") != "true" or name.split(".")[0] not in FOLDERS:
                    continue
                for command in navigation_commands(src, name):
                    full = f"{name}.Command.{command}"
                    if full not in NAV_BROKEN and objects.get(full, {}).get("View") != "true":
                        findings.append(f"Объект виден, команды навигации нет — {role}: {full}")
        launch = next((rights for name, rights in objects.items() if name.startswith("Configuration")), None)
        if (launch and launch.get("ThinClient") == "true" and launch.get("WebClient") != "true"
                and unicodedata.normalize("NFC", role) not in NAV_EXTERNAL_ROLES):
            findings.append(f"Тонкий клиент разрешён, веб-клиент нет — {role}")
        if sees_print and role not in EXTERNAL_ROLES and objects.get(PRINT_FORM, {}).get("View") != "true":
            findings.append(f"Команды печати есть, окна печати нет — {role}: {PRINT_FORM}")
    for line in findings:
        print(line)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
