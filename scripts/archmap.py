#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Карта архитектуры maERP: генерирует docs/ARCHITECTURE.md из src/cf/src.

Запуск:
    python3 scripts/archmap.py           # переписать docs/ARCHITECTURE.md
    python3 scripts/archmap.py --check   # код 1, если файл отличается от свежей генерации

Только стандартная библиотека, python 3.9. Вывод детерминирован: без дат и
без зависимости от порядка обхода каталогов и локали.
"""
import html
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src", "cf", "src")
OUT = os.path.join(ROOT, "docs", "ARCHITECTURE.md")

TOP_BIG = 30

# Каталог типа -> (имя типа в ссылках метаданных, название для человека)
TYPES = [
    ("Subsystems", "Subsystem", "Подсистемы"),
    ("Catalogs", "Catalog", "Справочники"),
    ("Documents", "Document", "Документы"),
    ("DocumentJournals", "DocumentJournal", "Журналы документов"),
    ("Enums", "Enum", "Перечисления"),
    ("Reports", "Report", "Отчёты"),
    ("DataProcessors", "DataProcessor", "Обработки"),
    ("AccumulationRegisters", "AccumulationRegister", "Регистры накопления"),
    ("InformationRegisters", "InformationRegister", "Регистры сведений"),
    ("AccountingRegisters", "AccountingRegister", "Регистры бухгалтерии"),
    ("ChartsOfAccounts", "ChartOfAccounts", "Планы счетов"),
    ("ChartsOfCharacteristicTypes", "ChartOfCharacteristicTypes", "Планы видов характеристик"),
    ("ExchangePlans", "ExchangePlan", "Планы обмена"),
    ("Tasks", "Task", "Задачи"),
    ("Sequences", "Sequence", "Последовательности"),
    ("Constants", "Constant", "Константы"),
    ("DefinedTypes", "DefinedType", "Определяемые типы"),
    ("FilterCriteria", "FilterCriterion", "Критерии отбора"),
    ("FunctionalOptions", "FunctionalOption", "Функциональные опции"),
    ("FunctionalOptionsParameters", "FunctionalOptionsParameter", "Параметры функциональных опций"),
    ("CommonModules", "CommonModule", "Общие модули"),
    ("CommonForms", "CommonForm", "Общие формы"),
    ("CommonCommands", "CommonCommand", "Общие команды"),
    ("CommandGroups", "CommandGroup", "Группы команд"),
    ("CommonTemplates", "CommonTemplate", "Общие макеты"),
    ("CommonPictures", "CommonPicture", "Общие картинки"),
    ("CommonAttributes", "CommonAttribute", "Общие реквизиты"),
    ("EventSubscriptions", "EventSubscription", "Подписки на события"),
    ("ScheduledJobs", "ScheduledJob", "Регламентные задания"),
    ("SessionParameters", "SessionParameter", "Параметры сеанса"),
    ("HTTPServices", "HTTPService", "HTTP-сервисы"),
    ("Roles", "Role", "Роли"),
    ("StyleItems", "StyleItem", "Элементы стиля"),
    ("Styles", "Style", "Стили"),
]
TYPE_ORDER = {t[1]: i for i, t in enumerate(TYPES)}

REG_SHORT = {
    "AccumulationRegister": "РН",
    "InformationRegister": "РС",
    "AccountingRegister": "РБ",
    "CalculationRegister": "РР",
}

MODULE_FLAGS = [
    ("server", "server"),
    ("clientManagedApplication", "clientManagedApplication"),
    ("serverCall", "serverCall"),
    ("privileged", "privileged"),
    ("global", "global"),
]

RE_SYN_RU = re.compile(r"^  <synonym>\s*\n\s*<key>ru</key>\s*\n\s*<value>(.*?)</value>", re.M | re.S)
RE_CONTENT = re.compile(r"^  <content>(.*?)</content>", re.M)
RE_SUBSYS = re.compile(r"^  <subsystems>(.*?)</subsystems>", re.M)
RE_REGREC = re.compile(r"^  <registerRecords>(.*?)</registerRecords>", re.M)
RE_RIGHTS_OBJ = re.compile(r"<object>\s*<name>(.*?)</name>(.*?)</object>", re.S)
RE_RIGHT = re.compile(r"<right>\s*<name>(.*?)</name>\s*<value>(.*?)</value>", re.S)


def nfc(text):
    return unicodedata.normalize("NFC", text)


def listdir(path):
    """Имена в каталоге, отсортированные по NFC-форме: [(nfc_имя, полный_путь)]."""
    if not os.path.isdir(path):
        return []
    items = [(nfc(n), os.path.join(path, n)) for n in os.listdir(path) if not n.startswith(".")]
    return sorted(items)


def read(path):
    try:
        with open(path, encoding="utf-8-sig") as f:
            return f.read()
    except OSError:
        return ""


def line_count(path):
    """Число строк как у wc -l (число переводов строки); 0, если файла нет."""
    try:
        with open(path, "rb") as f:
            return f.read().count(b"\n")
    except OSError:
        return 0


def rel(path):
    return nfc(os.path.relpath(path, ROOT)).replace(os.sep, "/")


def cell(text):
    return html.unescape(text or "").replace("|", "\\|").replace("\n", " ").strip()


def synonym_ru(mdo_text):
    m = RE_SYN_RU.search(mdo_text)
    return cell(m.group(1)) if m else ""


def mdo_of(obj_dir, name):
    """Текст .mdo объекта; имя файла сверяется в NFC, на диске оно может быть в NFD."""
    for n, p in listdir(obj_dir):
        if n == name + ".mdo":
            return read(p)
    return ""


def objects(type_dir):
    """Объекты типа: [(имя, каталог)]."""
    return [(n, p) for n, p in listdir(os.path.join(SRC, type_dir)) if os.path.isdir(p)]


def table(headers, rows, align=None):
    align = align or ["l"] * len(headers)
    out = ["| " + " | ".join(headers) + " |"]
    out.append("|" + "|".join("---:" if a == "r" else "---" for a in align) + "|")
    for row in rows:
        out.append("| " + " | ".join(str(c) for c in row) + " |")
    return out


def code(name):
    return "`" + name + "`"


# --- разделы -----------------------------------------------------------------

def collect_subsystem(sub_dir, name):
    """Состав подсистемы вместе с вложенными: (множество объектов, число вложенных)."""
    text = mdo_of(sub_dir, name)
    content = set(nfc(c) for c in RE_CONTENT.findall(text))
    nested = 0
    for child, child_dir in listdir(os.path.join(sub_dir, "Subsystems")):
        if not os.path.isdir(child_dir):
            continue
        sub_content, sub_nested = collect_subsystem(child_dir, child)
        content |= sub_content
        nested += 1 + sub_nested
    return content, nested


def section_subsystems():
    rows = []
    for name, path in objects("Subsystems"):
        content, nested = collect_subsystem(path, name)
        by_type = {}
        for ref in content:
            kind = ref.split(".", 1)[0]
            by_type[kind] = by_type.get(kind, 0) + 1
        kinds = sorted(by_type, key=lambda k: (TYPE_ORDER.get(k, 999), k))
        parts = ", ".join("%s %d" % (k, by_type[k]) for k in kinds)
        rows.append([code(name), synonym_ru(mdo_of(path, name)), nested, len(content), parts or "—"])
    out = ["## Подсистемы верхнего уровня", ""]
    out.append("Состав — поле `content` подсистемы и всех вложенных, объект считается один раз.")
    out.append("")
    out += table(["Подсистема", "Синоним", "Вложенных", "Объектов", "По типам"], rows, ["l", "l", "r", "r", "l"])
    return out


def all_bsl():
    """Все модули: [(строк, относительный путь)], по убыванию размера."""
    found = []
    for base, dirs, files in os.walk(SRC):
        dirs.sort()
        for f in files:
            if f.endswith(".bsl"):
                p = os.path.join(base, f)
                found.append((line_count(p), rel(p)))
    return sorted(found, key=lambda x: (-x[0], x[1]))


def section_types(modules):
    lines_by_dir = {}
    count_by_dir = {}
    prefix = "src/cf/src/"
    for n, p in modules:
        d = p[len(prefix):].split("/", 1)[0]
        lines_by_dir[d] = lines_by_dir.get(d, 0) + n
        count_by_dir[d] = count_by_dir.get(d, 0) + 1
    known = set(t[0] for t in TYPES) | {"Configuration"}
    extra = [(n, n, n) for n, p in listdir(SRC) if os.path.isdir(p) and n not in known]
    rows = []
    total = 0
    for type_dir, _ref, title in TYPES + extra:
        cnt = len(objects(type_dir))
        if not cnt:
            continue
        total += cnt
        rows.append([title, code(type_dir), cnt, count_by_dir.get(type_dir, 0), lines_by_dir.get(type_dir, 0)])
    all_lines = sum(n for n, _p in modules)
    rows.append(["**Всего**", "", "**%d**" % total, "**%d**" % len(modules), "**%d**" % all_lines])
    out = ["## Типы метаданных", ""]
    out.append("Объекты — подкаталоги `src/cf/src/<тип>`; модули — все `.bsl` внутри типа, включая формы")
    out.append("и команды. В «Всего» по модулям входят и модули корня конфигурации (`Configuration/`).")
    out.append("")
    out += table(["Тип", "Каталог", "Объектов", "Модулей .bsl", "Строк кода"], rows, ["l", "l", "r", "r", "r"])
    return out


def short_reg(ref):
    kind, _, name = ref.partition(".")
    return "%s.%s" % (REG_SHORT.get(kind, kind), name)


def section_documents():
    """Таблица документов и обратный индекс регистр -> документы."""
    rows = []
    writers = {}
    for name, path in objects("Documents"):
        text = mdo_of(path, name)
        regs = [nfc(r) for r in RE_REGREC.findall(text)]
        for r in regs:
            writers.setdefault(r, []).append(name)
        regs_sorted = sorted(regs, key=lambda r: (list(REG_SHORT).index(r.split(".")[0])
                                                  if r.split(".")[0] in REG_SHORT else 99, r))
        rows.append([
            code(name),
            synonym_ru(text),
            ", ".join(short_reg(r) for r in regs_sorted) or "—",
            line_count(os.path.join(path, "ObjectModule.bsl")) or "—",
            line_count(os.path.join(path, "ManagerModule.bsl")) or "—",
        ])
    out = ["## Документы", ""]
    out.append("Движения — свойство `registerRecords` в `.mdo` (то, что платформа разрешает документу")
    out.append("писать), а не разбор кода проведения. РН — регистр накопления, РС — сведений,")
    out.append("РБ — бухгалтерии. Размеры — строки `ObjectModule.bsl` и `ManagerModule.bsl`.")
    out.append("")
    out += table(["Документ", "Синоним", "Движения", "Объект", "Менеджер"], rows, ["l", "l", "l", "r", "r"])
    return out, writers


def section_registers(writers):
    out = ["## Регистры и кто в них пишет", ""]
    out.append("Обратный индекс по `registerRecords` документов. «—» — документы-регистраторы не")
    out.append("заявлены: регистр сведений независимый либо пишется кодом напрямую.")
    for type_dir, ref, title in (
        ("AccumulationRegisters", "AccumulationRegister", "Регистры накопления"),
        ("InformationRegisters", "InformationRegister", "Регистры сведений"),
    ):
        rows = []
        for name, path in objects(type_dir):
            docs = sorted(writers.get("%s.%s" % (ref, name), []))
            rows.append([code(name), synonym_ru(mdo_of(path, name)), len(docs) or "—", ", ".join(docs) or "—"])
        out += ["", "### " + title, ""]
        out += table(["Регистр", "Синоним", "Док.", "Документы-регистраторы"], rows, ["l", "l", "r", "l"])
    return out


def section_big(modules):
    out = ["## Самые большие модули", ""]
    out.append("Топ-%d `.bsl` по числу строк: кандидаты на разрезку. Целиком их не читать —" % TOP_BIG)
    out.append("искать нужную процедуру поиском и открывать диапазон строк.")
    out.append("")
    rows = [[i + 1, n, code(p)] for i, (n, p) in enumerate(modules[:TOP_BIG])]
    out += table(["№", "Строк", "Файл"], rows, ["r", "r", "l"])
    return out


def module_description(path):
    """Первая содержательная строка комментария в начале модуля (до кода и областей)."""
    try:
        with open(path, encoding="utf-8-sig") as f:
            for _ in range(40):
                raw = f.readline()
                if not raw:
                    break
                line = raw.strip()
                if not line:
                    continue
                if not line.startswith("//"):
                    break
                text = line.lstrip("/").strip()
                # метки авторов вида «//++ Фамилия 01.01.2025 1C-123» описанием не считаются
                if not text or text.startswith(("++", "--")) or not re.search(r"\w", text):
                    continue
                return text
    except OSError:
        pass
    return ""


def section_common_modules():
    rows = []
    for name, path in objects("CommonModules"):
        text = mdo_of(path, name)
        flags = [label for tag, label in MODULE_FLAGS if "<%s>true</%s>" % (tag, tag) in text]
        module = os.path.join(path, "Module.bsl")
        descr = module_description(module)
        if len(descr) > 110:
            descr = descr[:107].rstrip() + "..."
        rows.append([code(name), ", ".join(flags) or "—", line_count(module), cell(descr) or "—"])
    out = ["## Общие модули", ""]
    out.append("Флаги — из `.mdo` (показаны только server, clientManagedApplication, serverCall,")
    out.append("privileged, global). Описание — первая строка комментария в начале `Module.bsl`,")
    out.append("если он стоит до кода и областей.")
    out.append("")
    out += table(["Модуль", "Флаги", "Строк", "Описание"], rows, ["l", "l", "r", "l"])
    return out


def section_roles():
    rows = []
    for name, path in objects("Roles"):
        text = read(os.path.join(path, "Rights.rights"))
        readable = 0
        total = 0
        for obj_name, body in RE_RIGHTS_OBJ.findall(text):
            if obj_name.count(".") != 1:
                continue  # реквизиты, табличные части, команды — не объекты верхнего уровня
            total += 1
            rights = dict(RE_RIGHT.findall(body))
            if rights.get("Read") == "true" or rights.get("View") == "true":
                readable += 1
        new_objects = "да" if "<setForNewObjects>true</setForNewObjects>" in text else "—"
        rows.append([code(name), synonym_ru(mdo_of(path, name)), readable, total, new_objects])
    out = ["## Роли", ""]
    out.append("Грубая оценка по `Rights.rights`: объекты верхнего уровня (`Тип.Имя`), у которых")
    out.append("Read или View равно true. RLS и права на реквизиты не учитываются. «Новые объекты» —")
    out.append("флаг `setForNewObjects`: роль получает права на всё, что добавят позже.")
    out.append("")
    out += table(["Роль", "Синоним", "Read/View", "Объектов в файле", "Новые объекты"], rows,
                 ["l", "l", "r", "r", "l"])
    return out


def is_workplace(name):
    return name.startswith("АРМ") or name == "VentesEnDetail"


def section_workplaces():
    rows = []
    for name, path in objects("DataProcessors"):
        if not is_workplace(name):
            continue
        synonym = synonym_ru(mdo_of(path, name))
        forms = [(n, p) for n, p in listdir(os.path.join(path, "Forms")) if os.path.isdir(p)]
        if not forms:
            rows.append([code(name), synonym, "—", "—", "—"])
        for form, form_dir in forms:
            rows.append([
                code(name), synonym, code(form),
                line_count(os.path.join(form_dir, "Module.bsl")) or "—",
                line_count(os.path.join(form_dir, "Form.form")) or "—",
            ])
    out = ["## Рабочие места", ""]
    out.append("Обработки с именем на `АРМ` и `VentesEnDetail` (розничная касса). Размеры — строки")
    out.append("`Module.bsl` и `Form.form` каждой формы в `DataProcessors/<обработка>/Forms/<форма>/`.")
    out.append("")
    out += table(["Обработка", "Синоним", "Форма", "Модуль", "Form.form"], rows, ["l", "l", "l", "r", "r"])
    return out


def section_howto():
    return [
        "## Как читать",
        "",
        "- Файл **генерируется** скриптом `scripts/archmap.py` из `src/cf/src` и переписывается",
        "  целиком. Руками не править: правка пропадёт при следующем запуске.",
        "- Обновить: `python3 scripts/archmap.py`. Проверить, что карта не отстала от исходников:",
        "  `python3 scripts/archmap.py --check` (код 1 — отстала).",
        "- Не хватает сведений — дорабатывается скрипт, а не этот файл. Решения и соглашения,",
        "  которые из исходников не выводятся, живут в `CLAUDE.md` и тематических файлах `docs/`.",
        "- Имена объектов — как в метаданных; путь к объекту: `src/cf/src/<каталог типа>/<имя>/`.",
        "- Числа строк совпадают с `wc -l`. Синоним — русский (`ru`) из `.mdo`.",
        "- Карта показывает структуру, а не поведение: движения взяты из свойств документа,",
        "  права — из файла прав без RLS. Перед правкой объекта читается он сам.",
    ]


def generate():
    modules = all_bsl()
    docs, writers = section_documents()
    sections = [
        ["# Архитектура maERP", "",
         "> Карта метаданных, сгенерирована `scripts/archmap.py` из `src/cf/src`. Руками не править —",
         "> см. «Как читать» в конце."],
        section_types(modules),
        section_subsystems(),
        docs,
        section_registers(writers),
        section_big(modules),
        section_common_modules(),
        section_roles(),
        section_workplaces(),
        section_howto(),
    ]
    return "\n\n".join("\n".join(s) for s in sections) + "\n"


def main(argv):
    if not os.path.isdir(SRC):
        sys.stderr.write("archmap: нет каталога %s\n" % SRC)
        return 2
    fresh = generate()
    if "--check" in argv:
        current = read(OUT) if os.path.exists(OUT) else None
        if current != fresh:
            sys.stderr.write("archmap: docs/ARCHITECTURE.md отстал от src/cf/src - запустите scripts/archmap.py\n")
            return 1
        print("archmap: docs/ARCHITECTURE.md актуален")
        return 0
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(fresh)
    print("archmap: записан %s, строк: %d" % (rel(OUT), fresh.count("\n")))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
