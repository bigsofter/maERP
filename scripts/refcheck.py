#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сверка ссылок из модулей с деревом метаданных EDT-проекта.

Ловит обращения к объектам, которых в конфигурации нет: удалённые константы и
перечисления, переименованные регистры, картинки из чужой библиотеки, вызовы
несуществующих экспортных методов общих модулей. Всё это компилируется, но
падает в рантайме — CheckConfig такие ошибки не видит, смок-тест видит только
те из них, что лежат на пути открытия формы.

Проверяются:
  1. обращения к менеджерам: Справочники.Х, Документы.Х, Константы.Х,
     Перечисления.Х, Регистры*.Х, БиблиотекаКартинок.Х и т.д.;
  2. типы в строках: Тип("ДокументСсылка.Х"), "СправочникСсылка.Х";
  3. полные имена в строковых литералах: "Документ.Х", "ОбщаяФорма.Х",
     "Документ.Х.Форма.Y", "Документ.Х.Макет.Z" — на них опирается печать
     и ОткрытьФорму;
  4. вызовы общих модулей: ОбщийМодуль.Метод() — метод должен существовать
     и быть экспортным.

Известные и осознанно принятые расхождения (стандартные картинки платформы,
наследие бухгалтерского контура и прочее из docs/TECHDEBT.md) лежат в
scripts/refcheck-known.txt: строка «вид.имя», решётка — комментарий.

Использование:
  scripts/refcheck.py [каталог-исходников]        проверить (код возврата 1 при находках)
  scripts/refcheck.py --update-known              переписать файл известных расхождений
"""

import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DEFAULT = os.path.join(ROOT, "src", "cf", "src")
KNOWN_FILE = os.path.join(ROOT, "scripts", "refcheck-known.txt")


def nfc(text):
    # macOS хранит имена файлов в разложенном виде: без нормализации «ё» и «й»
    # в именах каталогов не совпадают с теми же буквами в модулях.
    return unicodedata.normalize("NFC", text)


# Коллекция метаданных: имя менеджера во множественном числе, имя в единственном
# числе (для полных имён и типов) и каталог EDT-проекта.
COLLECTIONS = [
    ("Справочники", "Справочник", "Catalogs"),
    ("Документы", "Документ", "Documents"),
    ("ЖурналыДокументов", "ЖурналДокументов", "DocumentJournals"),
    ("Перечисления", "Перечисление", "Enums"),
    ("Отчеты", "Отчет", "Reports"),
    ("Обработки", "Обработка", "DataProcessors"),
    ("ПланыВидовХарактеристик", "ПланВидовХарактеристик", "ChartsOfCharacteristicTypes"),
    ("ПланыСчетов", "ПланСчетов", "ChartsOfAccounts"),
    ("ПланыОбмена", "ПланОбмена", "ExchangePlans"),
    ("РегистрыСведений", "РегистрСведений", "InformationRegisters"),
    ("РегистрыНакопления", "РегистрНакопления", "AccumulationRegisters"),
    ("РегистрыБухгалтерии", "РегистрБухгалтерии", "AccountingRegisters"),
    ("БизнесПроцессы", "БизнесПроцесс", "BusinessProcesses"),
    ("Задачи", "Задача", "Tasks"),
    ("Константы", "Константа", "Constants"),
    ("КритерииОтбора", "КритерийОтбора", "FilterCriteria"),
    ("БиблиотекаКартинок", "ОбщаяКартинка", "CommonPictures"),
]

# Коллекции без менеджера: встречаются только в полных именах.
SINGULAR_ONLY = [
    ("ОбщийМодуль", "CommonModules"),
    ("ОбщаяФорма", "CommonForms"),
    ("ОбщийМакет", "CommonTemplates"),
    ("ОбщаяКоманда", "CommonCommands"),
    ("Роль", "Roles"),
    ("Подсистема", "Subsystems"),
]

# Ссылочные типы: «ДокументСсылка.Х» и родня.
TYPE_PREFIXES = {
    "СправочникСсылка": "Catalogs",
    "ДокументСсылка": "Documents",
    "ПеречислениеСсылка": "Enums",
    "ПланВидовХарактеристикСсылка": "ChartsOfCharacteristicTypes",
    "ПланСчетовСсылка": "ChartsOfAccounts",
    "ПланОбменаСсылка": "ExchangePlans",
    "БизнесПроцессСсылка": "BusinessProcesses",
    "ЗадачаСсылка": "Tasks",
    # «СправочникОбъект» и «ДокументОбъект» не берём: так принято называть переменные,
    # и проверка утонула бы в обращениях к их реквизитам.
}

# Имена, которые после точки означают не объект метаданных, а метод или свойство
# одноимённой переменной (таблицы значений, структуры, коллекции платформы).
NOT_OBJECT_NAMES = {
    "Найти", "НайтиПоНаименованию", "НайтиПоКоду", "НайтиПоНомеру", "НайтиПоРеквизиту",
    "Содержит", "Количество", "Добавить", "Удалить", "Изменить", "Вставить", "Получить",
    "Установить", "Очистить", "Индекс", "Выгрузить", "Загрузить", "Скопировать",
    "Сортировать", "Свойство", "Колонки", "Итог", "ВыгрузитьКолонку", "ЗаполнитьЗначения",
    "Ссылка", "ПустаяСсылка", "Дата", "Видимость", "Доступность", "Заголовок", "Имя",
    "ТипВсеСсылки", "ТипВсеСсылкиТочекМаршрутаБизнесПроцессов", "ТипВсеОбъекты",
    "ЗарегистрироватьИзменения", "ВыбратьИзменения", "УдалитьРегистрациюИзменений",
    "ИзменениеЗарегистрировано", "ВыбратьПоНомеру", "Выбрать", "СоздатьЭлемент",
    "СоздатьГруппу", "СоздатьДокумент", "СоздатьНаборЗаписей", "СоздатьМенеджерЗаписи",
    "СоздатьРегистраторРасчета", "ПолучитьМакет", "ПолучитьФорму", "ВыбратьИерархически",
    "СрезПоследних", "СрезПервых", "Остатки", "Обороты", "ОстаткиИОбороты", "Движения",
}

IDENT = r"[А-Яа-яЁёA-Za-z_][А-Яа-яЁёA-Za-z0-9_]*"


def read_names(src, folder):
    path = os.path.join(src, folder)
    if not os.path.isdir(path):
        return set()
    return set(nfc(name) for name in os.listdir(path) if not name.startswith("."))


def read_children(src, folder, child):
    """Подчинённые объекты: {объект: {имена форм | макетов | команд}}."""
    result = {}
    base = os.path.join(src, folder)
    if not os.path.isdir(base):
        return result
    for owner in os.listdir(base):
        if owner.startswith("."):
            continue
        sub = os.path.join(base, owner, child)
        names = set()
        if os.path.isdir(sub):
            names = set(nfc(n) for n in os.listdir(sub) if not n.startswith("."))
        result[nfc(owner)] = names
    return result


def export_methods(src):
    """Экспортные методы общих модулей: {модуль: {методы}}."""
    result = {}
    base = os.path.join(src, "CommonModules")
    if not os.path.isdir(base):
        return result
    pattern = re.compile(
        r"^\s*(?:Процедура|Функция|Procedure|Function)\s+(" + IDENT + r")\s*\([^)]*\)\s*Экспорт",
        re.IGNORECASE | re.MULTILINE)
    for module in os.listdir(base):
        path = os.path.join(base, module, "Module.bsl")
        if not os.path.isfile(path):
            continue
        text = open(path, encoding="utf-8-sig", errors="replace").read()
        # Многострочные объявления параметров: склеиваем перенос строки внутри скобок.
        text = re.sub(r",\s*\n\s*", ", ", text)
        result[nfc(module)] = set(nfc(m) for m in pattern.findall(text))
    return result


def split_code_and_strings(line, in_string):
    """Делит строку модуля на код (без комментария) и целые строковые литералы.

    Литерал в 1С продолжается на следующей строке (символ «|»), поэтому состояние
    «мы внутри строки» передаётся между строками: иначе текст запроса, где сплошь
    «РегистрСведений.Х.СрезПоследних», разбирается как код.

    Возвращает: код строки, литералы, целиком уместившиеся в этой строке,
    и признак «строка продолжается».
    """
    code, literal, literals = [], ([] if in_string else None), []
    started_here = not in_string
    i, n = 0, len(line)
    while i < n:
        ch = line[i]
        if literal is None:
            if ch == '"':
                literal = []
                started_here = True
            elif ch == "/" and i + 1 < n and line[i + 1] == "/":
                break
            else:
                code.append(ch)
        else:
            if ch == '"':
                if i + 1 < n and line[i + 1] == '"':
                    literal.append('"')
                    i += 1
                else:
                    if started_here:
                        literals.append("".join(literal))
                    literal = None
            else:
                literal.append(ch)
        i += 1
    return "".join(code), literals, literal is not None


class Checker:
    def __init__(self, src):
        self.src = src
        self.names = {}
        for plural, single, folder in COLLECTIONS:
            self.names[folder] = read_names(src, folder)
        for single, folder in SINGULAR_ONLY:
            self.names[folder] = read_names(src, folder)
        self.by_plural = {nfc(p): f for p, _, f in COLLECTIONS}
        self.by_single = {nfc(s): f for _, s, f in COLLECTIONS}
        self.by_single.update({nfc(s): f for s, f in SINGULAR_ONLY})
        self.forms = {}
        self.templates = {}
        self.commands = {}
        for _, single, folder in COLLECTIONS:
            self.forms[folder] = read_children(src, folder, "Forms")
            self.templates[folder] = read_children(src, folder, "Templates")
            self.commands[folder] = read_children(src, folder, "Commands")
        self.exports = export_methods(src)
        self.findings = []

        # Перед именем не должно быть точки: «РегистрыСведений.Лиды.СрезПоследних» — это
        # обращение к менеджеру регистра, а не к общему модулю с именем «Лиды».
        nodot = r"(?<![.\wА-Яа-яЁё])"
        self.re_manager = re.compile(
            nodot + r"(" + "|".join(sorted((p for p, _, _ in COLLECTIONS), key=len, reverse=True))
            + r")\.(" + IDENT + r")")
        self.re_type = re.compile(
            nodot + r"(" + "|".join(sorted(TYPE_PREFIXES, key=len, reverse=True)) + r")\.(" + IDENT + r")")
        singles = sorted((s for _, s, _ in COLLECTIONS), key=len, reverse=True)
        singles += sorted((s for s, _ in SINGULAR_ONLY), key=len, reverse=True)
        self.re_fullname = re.compile(
            r"^(" + "|".join(singles) + r")\.(" + IDENT + r")"
            r"(?:\.(Форма|Макет|Команда)\.(" + IDENT + r"))?$")
        module_names = sorted(self.exports, key=len, reverse=True)
        self.re_call = re.compile(
            nodot + r"(" + "|".join(re.escape(m) for m in module_names) + r")\.(" + IDENT + r")\s*\(") \
            if module_names else None

    def add(self, key, where, note):
        self.findings.append((key, where, note))

    def check_file(self, path, rel):
        text = nfc(open(path, encoding="utf-8-sig", errors="replace").read())
        # Имена, которыми в этом модуле названы переменные и параметры: одноимённый
        # общий модуль такой строкой не вызывается, проверять вызов бессмысленно.
        locals_here = set(re.findall(r"(?m)^\s*(" + IDENT + r")\s*=", text))
        locals_here |= set(re.findall(r"(?mi)^\s*Перем\s+(" + IDENT + r")", text))
        for params in re.findall(r"(?mi)^\s*(?:Процедура|Функция)\s+" + IDENT + r"\s*\(([^)]*)\)", text):
            locals_here |= set(re.findall(IDENT, params))

        in_string = False
        for number, raw in enumerate(text.split("\n"), 1):
            line = raw
            code, literals, in_string = split_code_and_strings(line, in_string)
            where = "%s:%d" % (rel, number)

            for collection, name in self.re_manager.findall(code):
                if name in NOT_OBJECT_NAMES:
                    continue
                folder = self.by_plural[collection]
                if name not in self.names[folder]:
                    self.add(collection + "." + name, where, "объекта нет в конфигурации")

            for prefix, name in self.re_type.findall(code) + self.re_type.findall(" ".join(literals)):
                folder = TYPE_PREFIXES[prefix]
                if name not in self.names[folder]:
                    self.add(prefix + "." + name, where, "типа нет в конфигурации")

            for literal in literals:
                match = self.re_fullname.match(literal.strip())
                if match:
                    self.check_fullname(match, where)

            if self.re_call:
                for module, method in self.re_call.findall(code):
                    module = nfc(module)
                    if module in locals_here:
                        continue
                    if method not in self.exports.get(module, set()):
                        self.add(module + "." + method, where,
                                 "в общем модуле нет такого экспортного метода")

    def check_fullname(self, match, where):
        single, owner, kind, child = match.group(1), match.group(2), match.group(3), match.group(4)
        folder = self.by_single[single]
        if owner not in self.names[folder]:
            self.add(single + "." + owner, where, "объекта нет в конфигурации")
            return
        if not kind:
            return
        source = {"Форма": self.forms, "Макет": self.templates, "Команда": self.commands}[kind]
        owned = source.get(folder, {}).get(owner)
        if owned is None:
            return
        if child not in owned:
            self.add("%s.%s.%s.%s" % (single, owner, kind, child), where,
                     "у объекта нет такого подчинённого объекта")

    def run(self):
        for root, dirs, files in os.walk(self.src):
            dirs[:] = [d for d in dirs if d not in (".git", "DT-INF")]
            for name in files:
                if name.endswith(".bsl"):
                    path = os.path.join(root, name)
                    self.check_file(path, os.path.relpath(path, ROOT))
        return self.findings


def read_known():
    known = set()
    if not os.path.isfile(KNOWN_FILE):
        return known
    for line in open(KNOWN_FILE, encoding="utf-8"):
        line = line.split("#")[0].strip()
        if line:
            known.add(nfc(line))
    return known


def write_known(findings):
    keys = {}
    for key, where, _ in findings:
        keys.setdefault(key, where)
    with open(KNOWN_FILE, "w", encoding="utf-8") as file:
        file.write("# Известные расхождения scripts/refcheck.py: имя и место первой встречи.\n")
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
        print("Сверка ссылок: расхождений нет (известных — %d)" % len(known))
        return 0

    grouped = {}
    for key, where, note in fresh:
        grouped.setdefault((key, note), []).append(where)
    print("Сверка ссылок: новых расхождений — %d" % len(grouped))
    for (key, note), places in sorted(grouped.items()):
        print("  %s — %s" % (key, note))
        for place in places[:5]:
            print("      %s" % place)
        if len(places) > 5:
            print("      ... ещё %d" % (len(places) - 5))
    return 1


if __name__ == "__main__":
    sys.exit(main())
