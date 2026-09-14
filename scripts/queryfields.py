#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сверка полей в текстах запросов модулей с реквизитами метаданных.

Ловит обращение к полю, которого у документа или справочника нет: «Док.ХозяйственнаяОперация»
при «Документ.ВыпускПродукции КАК Док». Запрос с таким полем падает только при выполнении
(«Поле не найдено»), а если он стоит в клиентском обработчике — например, в панели «Детали»
списка по активации строки, — его не видят ни CheckConfig, ни смок (инцидент 2026-09-14,
списки выпуска продукции и акта разбора, docs/TECHDEBT.md).

Проверяются тексты запросов в модулях .bsl — строковые литералы с продолжениями «|»:
  1. псевдонимы «Документ.Имя КАК П», «Справочник.Имя КАК П», «Документ.Имя.ТабличнаяЧасть КАК П»;
  2. каждое «П.Поле» внутри того же запроса пакета и той же ветки ОБЪЕДИНИТЬ — среди реквизитов
     и табличных частей .mdo, стандартных полей и общих реквизитов.
Разыменование через точку глубже первого уровня («П.Поле.Реквизит») не проверяется.

В модулях форм документа (Documents/Имя/Forms/Форма/Module.bsl), где текст запроса объявляет «Документ.Имя КАК Док»,
дополнительно проверяются:
  3. условия, склеенные из строк вне литерала запроса («"Док.Сумма " + ЗнакУсловия(...)») — панель отборов списка;
  4. поля отборов динамического списка по имени — «УстановитьОтборПоПолю("Поле", ...)», «Отборы.Вставить("Поле", ...)».

Известные и осознанно принятые расхождения лежат в scripts/queryfields-known.txt:
строка «модуль|таблица|поле», решётка — комментарий.

Использование:
  scripts/queryfields.py [каталог-исходников]      проверить (код возврата 1 при находках)
  scripts/queryfields.py --update-known            переписать файл известных расхождений
"""

import io
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DEFAULT = os.path.join(ROOT, "src", "cf", "src")
KNOWN_FILE = os.path.join(ROOT, "scripts", "queryfields-known.txt")

COLLECTIONS = {"Документ": "Documents", "Справочник": "Catalogs"}

# Поля, которые есть у объекта без описания в .mdo.
STANDARD_FIELDS = {
    "Ссылка", "Дата", "Номер", "Проведен", "ПометкаУдаления", "МоментВремени", "Представление",
    "Код", "Наименование", "Родитель", "Владелец", "ЭтоГруппа", "Предопределенный",
    "ИмяПредопределенныхДанных", "ВерсияДанных", "НомерСтроки",
}

IDENT = r"[А-Яа-яЁёA-Za-z_][А-Яа-яЁёA-Za-z0-9_]*"


def nfc(text):
    # macOS хранит имена файлов в разложенном виде: без нормализации «ё» и «й» не совпадают.
    return unicodedata.normalize("NFC", text)


class Metadata:
    """Реквизиты и табличные части документов и справочников по .mdo."""

    def __init__(self, src):
        self.src = src
        self.dirs = {}
        for russian, folder in COLLECTIONS.items():
            base = os.path.join(src, folder)
            if os.path.isdir(base):
                for name in os.listdir(base):
                    self.dirs[(russian, nfc(name))] = os.path.join(base, name)
        common = os.path.join(src, "CommonAttributes")
        self.common = {nfc(n) for n in os.listdir(common)} if os.path.isdir(common) else set()
        self.cache = {}

    def fields(self, collection, name, section):
        key = (collection, name, section)
        if key not in self.cache:
            self.cache[key] = self._read(collection, name, section)
        return self.cache[key]

    def _read(self, collection, name, section):
        folder = self.dirs.get((collection, name))
        if not folder:
            return None
        files = [f for f in os.listdir(folder) if f.endswith(".mdo")]
        if not files:
            return None
        text = nfc(io.open(os.path.join(folder, files[0]), encoding="utf-8").read())
        sections = list(re.finditer(r'<tabularSections uuid="[^"]*">(.*?)\n  </tabularSections>', text, re.S))
        top = text
        for match in sections:
            top = top.replace(match.group(0), "")
        if section is None:
            result = set(re.findall(r'<attributes uuid="[^"]*">\s*<name>([^<]+)</name>', top))
            for match in sections:
                result.add(re.search(r"<name>([^<]+)</name>", match.group(1)).group(1))
            return result
        for match in sections:
            if re.search(r"<name>([^<]+)</name>", match.group(1)).group(1) == section:
                return set(re.findall(r'<attributes uuid="[^"]*">\s*<name>([^<]+)</name>', match.group(1)))
        return None


def query_literals(lines):
    """Тексты запросов: строка с открывающей кавычкой и продолжения «|». Возвращает (номер строки, текст)."""
    index = 0
    while index < len(lines):
        if '"' in lines[index] and index + 1 < len(lines) and lines[index + 1].lstrip().startswith("|"):
            start = index
            block = [lines[index].split('"', 1)[1]]
            index += 1
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                block.append(lines[index].lstrip()[1:])
                index += 1
            yield start + 1, "\n".join(block)
        else:
            index += 1


def parts(text):
    """Запросы пакета и ветки объединения: у каждой ветки свои псевдонимы."""
    for query in re.split(r";\s*\n", text):
        for branch in re.split(r"(?m)^\s*ОБЪЕДИНИТЬ(?:\s+ВСЕ)?\s*$", query):
            yield branch


class Checker:

    def __init__(self, src):
        self.src = src
        self.meta = Metadata(src)
        self.findings = []

    def run(self):
        for base, _dirs, files in os.walk(self.src):
            for name in sorted(files):
                if name.endswith(".bsl"):
                    self.check_module(os.path.join(base, name))
        return self.findings

    def check_module(self, path):
        where = nfc(os.path.relpath(path, ROOT))
        source = nfc(io.open(path, encoding="utf-8").read())
        lines = source.split("\n")
        for line, text in query_literals(lines):
            for branch in parts(text):
                self.check_branch(where, line, branch)
        self.check_form_filters(where, lines)

    def check_form_filters(self, where, lines):
        match = re.match(r"src/cf/src/Documents/(" + IDENT + r")/Forms/" + IDENT + r"/Module\.bsl$", where)
        if not match:
            return
        name = match.group(1)
        source = "\n".join(lines)
        known = self.meta.fields("Документ", name, None)
        if known is None or not re.search(r"Документ\." + re.escape(name) + r"\s+КАК\s+Док\b", source):
            return
        table = "Документ.%s" % name
        list_fields = self.list_query_fields(where)
        checks = []
        for number, text in enumerate(lines, 1):
            if text.lstrip().startswith("|") or text.lstrip().startswith("//"):
                continue
            for field in re.findall(r'"Док\.(' + IDENT + r')', text):
                checks.append((number, field, "условие «Док.%s»" % field))
            for field in re.findall(r'(?:УстановитьОтборПоПолю|Отборы\.Вставить)\(\s*"(' + IDENT + r')"', text):
                checks.append((number, field, "отбор списка по полю «%s»" % field))
        for number, field, what in checks:
            if field in known or field in STANDARD_FIELDS or field in self.meta.common:
                continue
            # Отбор динамического списка может стоять на вычисляемом поле его произвольного запроса.
            if what.startswith("отбор") and field in list_fields:
                continue
            self.findings.append((
                "%s|%s|%s" % (where, table, field),
                "%s:%d" % (where, number),
                "%s — у %s нет реквизита «%s»" % (what, table, field),
            ))

    @staticmethod
    def list_query_fields(where):
        """Псевдонимы произвольных запросов динамических списков формы (Form.form рядом с модулем)."""
        form = os.path.join(ROOT, os.path.dirname(where), "Form.form")
        if not os.path.exists(form):
            return set()
        text = nfc(io.open(form, encoding="utf-8").read())
        fields = set()
        for match in re.finditer(r"<queryText>(.*?)</queryText>", text, re.S):
            fields |= set(re.findall(r"КАК\s+(" + IDENT + r")", match.group(1)))
        return fields

    def check_branch(self, where, line, branch):
        pattern = r"(Документ|Справочник)\.(" + IDENT + r")(?:\.(" + IDENT + r"))?\s+КАК\s+(" + IDENT + r")"
        for match in re.finditer(pattern, branch):
            collection, name, section, alias = match.groups()
            known = self.meta.fields(collection, name, section)
            if known is None:
                continue
            table = "%s.%s%s" % (collection, name, "." + section if section else "")
            usage = r"(?<![А-Яа-яЁёA-Za-z0-9_.&])" + re.escape(alias) + r"\.(" + IDENT + r")"
            for field in sorted(set(re.findall(usage, branch))):
                if field in known or field in STANDARD_FIELDS or field in self.meta.common:
                    continue
                self.findings.append((
                    "%s|%s|%s" % (where, table, field),
                    "%s:%d" % (where, line),
                    "поле «%s.%s» — у %s нет реквизита «%s»" % (alias, field, table, field),
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
    for key, _where, note in findings:
        keys.setdefault(key, note)
    with io.open(KNOWN_FILE, "w", encoding="utf-8") as file:
        file.write("# Известные расхождения scripts/queryfields.py: «модуль|таблица|поле» и причина.\n")
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
        print("Сверка полей запросов: расхождений нет (известных — %d)" % len(known))
        return 0

    print("Сверка полей запросов: новых расхождений — %d" % len(fresh))
    for _key, where, note in sorted(fresh, key=lambda f: f[1]):
        print("  %s" % note)
        print("      %s" % where)
    return 1


if __name__ == "__main__":
    sys.exit(main())
