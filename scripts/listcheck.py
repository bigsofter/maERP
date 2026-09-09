#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка динамических списков форм: колонки против текста произвольного запроса.

Ловит расхождение между произвольным запросом динамического списка и колонками
таблицы, которая этот список показывает: колонка ссылается на поле, которого в
запросе нет, или запрос вовсе выбирает не из той таблицы, что указана в
mainTable. Ни CheckConfig, ни EDT, ни смок-тест такого не видят: запрос сам по
себе валиден, а данные списка платформа читает только при отрисовке таблицы на
клиенте — то есть уже у пользователя (инцидент 2026-09-09, список поступления
товаров и услуг, docs/TECHDEBT.md).

Проверяются формы со списками, у которых включён ПроизвольныйЗапрос
(customQuery):
  1. поля колонок: каждый путь «Список.Поле» в таблице формы должен быть среди
     псевдонимов (КАК Поле) или полей верхнего уровня запроса;
  2. основная таблица: mainTable должна встречаться в тексте запроса — иначе
     список выбирает данные не того объекта.

Стандартные поля списка (Ref/Ссылка у справочников и документов, Code,
Description, DefaultPicture и родня) платформа отдаёт без запроса — они в
STANDARD_FIELDS и не проверяются.

Известные и осознанно принятые расхождения лежат в scripts/listcheck-known.txt:
строка «форма|список|поле», решётка — комментарий.

Использование:
  scripts/listcheck.py [каталог-исходников]      проверить (код возврата 1 при находках)
  scripts/listcheck.py --update-known            переписать файл известных расхождений
"""

import io
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DEFAULT = os.path.join(ROOT, "src", "cf", "src")
KNOWN_FILE = os.path.join(ROOT, "scripts", "listcheck-known.txt")

# Английские имена коллекций в mainTable — русские в тексте запроса.
COLLECTIONS = {
    "Document": "Документ",
    "DocumentJournal": "ЖурналДокументов",
    "Catalog": "Справочник",
    "Enum": "Перечисление",
    "InformationRegister": "РегистрСведений",
    "AccumulationRegister": "РегистрНакопления",
    "AccountingRegister": "РегистрБухгалтерии",
    "CalculationRegister": "РегистрРасчета",
    "ChartOfCharacteristicTypes": "ПланВидовХарактеристик",
    "ChartOfAccounts": "ПланСчетов",
    "ChartOfCalculationTypes": "ПланВидовРасчета",
    "ExchangePlan": "ПланОбмена",
    "BusinessProcess": "БизнесПроцесс",
    "Task": "Задача",
    "FilterCriterion": "КритерийОтбора",
}

# Хвосты виртуальных таблиц: в запросе стоит имя основной таблицы без них.
VIRTUAL_SUFFIXES = (
    ".Balance", ".Turnovers", ".BalanceAndTurnovers", ".RecordsWithExtDimensions",
    ".SliceLast", ".SliceFirst", ".DrCrTurnovers", ".Subconto", ".Records",
)

# Поля, которые динамический список отдаёт сам, без запроса: стандартные
# реквизиты и служебные поля отображения.
STANDARD_FIELDS = {
    "Ref", "Ссылка", "Code", "Код", "Description", "Наименование",
    "DeletionMark", "ПометкаУдаления", "Predefined", "Предопределенный",
    "IsFolder", "ЭтоГруппа", "Parent", "Родитель", "Owner", "Владелец",
    "Posted", "Проведен", "Date", "Дата", "Number", "Номер",
    "Period", "Период", "Recorder", "Регистратор", "LineNumber", "НомерСтроки",
    "PointInTime", "МоментВремени", "Presentation", "Представление",
    "DefaultPicture", "Filter", "Отбор",
}

IDENT = r"[А-Яа-яЁёA-Za-z_][А-Яа-яЁёA-Za-z0-9_]*"


def nfc(text):
    # macOS хранит имена файлов в разложенном виде: без нормализации «ё» и «й»
    # в именах каталогов не совпадают с теми же буквами в модулях.
    return unicodedata.normalize("NFC", text)


def unescape(text):
    for entity, char in (("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&apos;", "'"), ("&amp;", "&")):
        text = text.replace(entity, char)
    return text


def top_level_fields(query):
    """Поля верхнего уровня запроса: псевдонимы и имена после точки в списке выборки."""
    # Список выборки — до первого «ИЗ» в начале строки: у вложенных подзапросов
    # оно с отступом, у верхнего уровня — с начала строки.
    head = re.split(r"(?m)^(?:ИЗ|FROM)\b", query, 1)[0]
    fields = set(re.findall(r"(?:КАК|AS)\s+(" + IDENT + r")", head))
    fields |= set(re.findall(r"\.(" + IDENT + r")\s*(?:,|$)", head, re.M))
    return fields


class Checker:
    """Разбор форм: списки с произвольным запросом и колонки их таблиц."""

    def __init__(self, src):
        self.src = src
        self.findings = []

    def run(self):
        for path in sorted(self.forms()):
            self.check_form(path)
        return self.findings

    def forms(self):
        for base, _dirs, files in os.walk(self.src):
            for name in files:
                if name == "Form.form":
                    yield os.path.join(base, name)

    def check_form(self, path):
        text = io.open(path, encoding="utf-8").read()
        where = nfc(os.path.relpath(path, ROOT))
        for name, body in self.dynamic_lists(text):
            query = re.search(r"<queryText>(.*?)</queryText>", body, re.S)
            if not query or "<customQuery>true</customQuery>" not in body:
                continue
            query = unescape(query.group(1))
            self.check_main_table(where, name, body, query)
            self.check_columns(where, name, text, query)

    def dynamic_lists(self, text):
        for match in re.finditer(r"<attributes>\s*<name>(" + IDENT + r")</name>(.*?)</attributes>", text, re.S):
            if "form:DynamicListExtInfo" in match.group(2):
                yield nfc(match.group(1)), match.group(2)

    def check_main_table(self, where, name, body, query):
        main = re.search(r"<mainTable>([^<]*)</mainTable>", body)
        if not main or not main.group(1):
            return
        table = main.group(1)
        for suffix in VIRTUAL_SUFFIXES:
            if table.endswith(suffix):
                table = table[: -len(suffix)]
        if "." not in table:
            return
        collection, obj = table.split(".", 1)
        russian = COLLECTIONS.get(collection, collection) + "." + obj
        if russian not in nfc(query):
            self.findings.append((
                "%s|%s|ОСНОВНАЯ ТАБЛИЦА" % (where, name),
                where,
                "запрос списка «%s» не выбирает из %s" % (name, russian),
            ))

    def check_columns(self, where, name, text, query):
        fields = top_level_fields(nfc(query))
        columns = set(nfc(c) for c in re.findall(
            r"<segments>" + re.escape(name) + r"\.(" + IDENT + r")</segments>", text))
        for column in sorted(columns):
            if column in fields or column in STANDARD_FIELDS:
                continue
            self.findings.append((
                "%s|%s|%s" % (where, name, column),
                where,
                "колонка «%s.%s» — поля нет в запросе списка" % (name, column),
            ))


def read_known():
    if not os.path.exists(KNOWN_FILE):
        return set()
    known = set()
    for line in io.open(KNOWN_FILE, encoding="utf-8"):
        line = line.split("#", 1)[0].strip()
        if line:
            known.add(nfc(line))
    return known


def write_known(findings):
    keys = {}
    for key, where, note in findings:
        keys.setdefault(key, note)
    with io.open(KNOWN_FILE, "w", encoding="utf-8") as file:
        file.write("# Известные расхождения scripts/listcheck.py: «форма|список|поле» и причина.\n")
        file.write("# Сюда попадает то, что работает или осознанно отложено (docs/TECHDEBT.md).\n")
        file.write("# Новое расхождение = ошибка, разбирается до сдачи работы.\n\n")
        for key in sorted(keys):
            file.write("%s  # %s\n" % (key, keys[key]))
    return len(keys)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    update = "--update-known" in sys.argv
    src = args[0] if args else SRC_DEFAULT

    findings = Checker(src).run()

    if update:
        count = write_known(findings)
        print("Записано известных расхождений: %d (%s)" % (count, os.path.relpath(KNOWN_FILE, ROOT)))
        return 0

    known = read_known()
    fresh = [f for f in findings if f[0] not in known]
    if not fresh:
        print("Проверка динамических списков: расхождений нет (известных — %d)" % len(known))
        return 0

    print("Проверка динамических списков: новых расхождений — %d" % len(fresh))
    for key, where, note in sorted(fresh):
        print("  %s" % note)
        print("      %s" % where)
    return 1


if __name__ == "__main__":
    sys.exit(main())
