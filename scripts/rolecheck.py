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

Проверяются все роли: роль без своего права на клиент работает в паре с другой
(«Складские ордера» с «Оператором производства»).

Использование: scripts/rolecheck.py [каталог EDT-проекта или его src]. Код возврата 1 — есть
расхождения.
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
    findings = []
    for role in sorted(os.listdir(roles)):
        path = os.path.join(roles, role, "Rights.rights")
        if not os.path.exists(path):
            continue
        text = unicodedata.normalize("NFC", open(path, encoding="utf-8").read())
        if "<setForNewObjects>true" in text:
            continue
        objects = {match.group(1): dict(RIGHT.findall(match.group(2))) for match in OBJECT.finditer(text)}
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
    for line in findings:
        print(line)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
