#!/usr/bin/env python3
"""Сверка командного интерфейса подсистем: что реально покажется в меню разделов.

Команда объекта, у которой в CommandInterface.cmi нет фрагмента видимости, видима
по умолчанию и встаёт в группу из своего <group> в .mdo объекта. Из-за этого
фактическое меню расходится с тем, что записано в commandsOrder, и правка .cmi
«по списку порядка» ничего не меняет. Проверка считает это по файлам.

Что ищется:
  НЕЯВНАЯ ВИДИМОСТЬ - команда объекта из состава подсистемы без фрагмента <visible>;
  ОБЪЕКТ ДВАЖДЫ    - объект представлен и своей командой, и стандартной OpenList/Open:
                     решить, кто из них виден (tiny1C mdo-005);
  МЁРТВАЯ КОМАНДА  - своя команда открывает тот же список без отбора, что стандартная -
                     удалять вместе с модулем;
  РЕГИСТР В МЕНЮ   - регистр накопления или сведений виден в панели навигации;
  СОЗДАНИЕ         - видимая StandardCommand.Create у документа, который вводится
                     только на основании другого (<basedOn> в .mdo);
  ВИСЯЧАЯ ССЫЛКА   - фрагмент .cmi ссылается на объект вне <content> подсистемы.

Запуск: scripts/menucheck.py [--section Имя] [--quiet]
Выход: 0 - расхождений нет; 1 - есть.
"""

import argparse
import re
import sys
from pathlib import Path
from xml.etree import ElementTree

SRC = Path(__file__).resolve().parent.parent / "src" / "cf" / "src"
SUBSYSTEMS = SRC / "Subsystems"

# Корневой элемент .mdo и .cmi идёт с префиксом, а дочерние - без него и потому
# вне пространства имён: искать их надо голыми именами.
MD = ""
CMI = ""

# Каталог метаданных в имени вида «Catalog.Номенклатура» -> каталог на диске.
KIND_DIRS = {
    "Catalog": "Catalogs",
    "Document": "Documents",
    "DocumentJournal": "DocumentJournals",
    "Report": "Reports",
    "DataProcessor": "DataProcessors",
    "InformationRegister": "InformationRegisters",
    "AccumulationRegister": "AccumulationRegisters",
    "AccountingRegister": "AccountingRegisters",
    "ChartOfAccounts": "ChartsOfAccounts",
    "ChartOfCharacteristicTypes": "ChartsOfCharacteristicTypes",
    "Constant": "Constants",
    "Enum": "Enums",
    "Task": "Tasks",
    "BusinessProcess": "BusinessProcesses",
    "CommonForm": "CommonForms",
    "CommonCommand": "CommonCommands",
    "CommonModule": "CommonModules",
    "ScheduledJob": "ScheduledJobs",
    "FilterCriterion": "FilterCriteria",
    "Sequence": "Sequences",
    "ExchangePlan": "ExchangePlans",
}

# Списочная стандартная команда по виду объекта.
LIST_COMMAND = {
    "Catalog": "OpenList",
    "Document": "OpenList",
    "DocumentJournal": "OpenList",
    "InformationRegister": "OpenList",
    "AccumulationRegister": "OpenList",
    "AccountingRegister": "OpenList",
    "ChartOfAccounts": "OpenList",
    "ChartOfCharacteristicTypes": "OpenList",
    "Task": "OpenList",
    "BusinessProcess": "OpenList",
    "ExchangePlan": "OpenList",
    "Report": "Open",
    "DataProcessor": "Open",
    "Constant": "Open",
    "CommonForm": "Open",
    "FilterCriterion": "OpenList",
}

CREATE_KINDS = {"Catalog", "Document", "Task", "BusinessProcess", "ExchangePlan",
                "ChartOfCharacteristicTypes"}
REGISTER_KINDS = {"AccumulationRegister", "InformationRegister", "AccountingRegister"}
# Перечисления и общие модули команд в панели раздела не дают.
SILENT_KINDS = {"Enum", "CommonModule", "Sequence", "ScheduledJob"}


def object_path(full_name):
    """Путь к .mdo объекта по имени вида «Catalog.Номенклатура»."""
    kind, _, name = full_name.partition(".")
    directory = KIND_DIRS.get(kind)
    if not directory:
        return None, kind, name
    return SRC / directory / name / f"{name}.mdo", kind, name


class MetaObject:
    """Объект метаданных: свои команды панелей и признаки, важные для меню."""

    _cache = {}

    def __init__(self, full_name):
        self.full_name = full_name
        self.path, self.kind, self.name = object_path(full_name)
        self.custom_commands = []   # [(имя, группа)]
        self.based_on = []
        self.use_standard = True
        self.exists = bool(self.path and self.path.exists())
        if self.exists:
            self._read()

    def _read(self):
        try:
            root = ElementTree.parse(self.path).getroot()
        except ElementTree.ParseError:
            return
        use = root.find(f"{MD}useStandardCommands")
        if use is not None and (use.text or "").strip() == "false":
            self.use_standard = False
        for based in root.findall(f"{MD}basedOn"):
            if based.text:
                self.based_on.append(based.text.strip())
        for command in root.findall(f"{MD}commands"):
            name = command.findtext(f"{MD}name")
            group = command.findtext(f"{MD}group") or ""
            # Параметризуемые команды в панель раздела не попадают.
            if command.find(f"{MD}commandParameterType") is not None:
                continue
            if name and (group.startswith("NavigationPanel") or group.startswith("ActionsPanel")):
                self.custom_commands.append((name.strip(), group.strip()))

    def command_is_plain_list(self, command_name):
        """Модуль своей команды открывает тот же список без отбора и параметров."""
        if not self.path:
            return False
        module = self.path.parent / "Commands" / command_name / "CommandModule.bsl"
        if not module.exists():
            return False
        text = module.read_text(encoding="utf-8-sig")
        opened = re.search(r'ОткрытьФорму\(\s*"([^"]+)"', text)
        if not opened:
            return False
        form = opened.group(1)
        if not form.endswith("ФормаСписка"):
            return False
        # Отбор или иные параметры формы - команда не пустая.
        return not re.search(r'Новый\s+Структура\s*\(\s*"[^"]', text)

    @classmethod
    def get(cls, full_name):
        if full_name not in cls._cache:
            cls._cache[full_name] = cls(full_name)
        return cls._cache[full_name]


def read_subsystem(mdo_path):
    """Состав, дочерние подсистемы и участие в командном интерфейсе."""
    root = ElementTree.parse(mdo_path).getroot()
    relative = mdo_path.parent.relative_to(SUBSYSTEMS)
    return {
        "name": " / ".join(part for part in relative.parts if part != "Subsystems"),
        "content": [c.text.strip() for c in root.findall(f"{MD}content") if c.text],
        "in_interface": (root.findtext(f"{MD}includeInCommandInterface") or "").strip() == "true",
        "path": mdo_path,
    }


def read_cmi(cmi_path):
    """Видимость и упомянутые команды из CommandInterface.cmi.

    Возвращает (видимость, все упомянутые команды). Пустой <visible/> - скрыто,
    <visible><common>true</common></visible> - показано.
    """
    visibility, mentioned = {}, set()
    if not cmi_path.exists():
        return visibility, mentioned
    root = ElementTree.parse(cmi_path).getroot()
    for fragment in root.iter(f"{CMI}visibilityFragments"):
        command = fragment.findtext(f"{CMI}command")
        if not command:
            continue
        command = command.strip()
        visible = fragment.find(f"{CMI}visible")
        shown = visible is not None and (visible.findtext("common") or "").strip() == "true"
        visibility[command] = shown
        mentioned.add(command)
    for tag in (f"{CMI}placementFragments", f"{CMI}orderFragments"):
        for fragment in root.iter(tag):
            for command in fragment.findall(f"{CMI}commands"):
                if command.text:
                    mentioned.add(command.text.strip())
    return visibility, mentioned


def subsystem_commands(content):
    """Команды, которые объект состава приносит в панели раздела."""
    result = []
    for full_name in content:
        meta = MetaObject.get(full_name)
        if meta.kind in SILENT_KINDS or not meta.exists:
            continue
        if meta.use_standard:
            list_command = LIST_COMMAND.get(meta.kind)
            if list_command:
                result.append((f"{full_name}.StandardCommand.{list_command}", meta, "standard"))
            if meta.kind in CREATE_KINDS:
                result.append((f"{full_name}.StandardCommand.Create", meta, "create"))
        for name, _group in meta.custom_commands:
            result.append((f"{full_name}.Command.{name}", meta, "custom"))
    return result


def check_subsystem(entry, findings):
    """Расхождения одной подсистемы."""
    name, content = entry["name"], entry["content"]
    cmi_path = entry["path"].parent / "CommandInterface.cmi"
    visibility, mentioned = read_cmi(cmi_path)
    where = str(cmi_path.relative_to(SRC.parent.parent.parent))

    commands = subsystem_commands(content)
    known = {command for command, _meta, _kind in commands}

    for command, meta, kind in commands:
        shown = visibility.get(command)
        if shown is None:
            findings.append((name, "НЕЯВНАЯ ВИДИМОСТЬ", command,
                             f"{where}: фрагмента <visible> нет, команда видима по умолчанию"))
            shown = True
        if not shown:
            continue
        if kind == "create" and meta.based_on:
            findings.append((name, "СОЗДАНИЕ", command,
                             f"документ вводится на основании: {', '.join(meta.based_on)}"))
        if kind == "standard" and meta.kind in REGISTER_KINDS:
            findings.append((name, "РЕГИСТР В МЕНЮ", command,
                             f"{meta.kind} виден в панели навигации"))

    # Дубль: и своя навигационная команда, и стандартная списочная видимы.
    for full_name in content:
        meta = MetaObject.get(full_name)
        if not meta.exists or meta.kind in SILENT_KINDS or not meta.use_standard:
            continue
        list_command = LIST_COMMAND.get(meta.kind)
        if not list_command:
            continue
        standard = f"{full_name}.StandardCommand.{list_command}"
        if not visibility.get(standard, True):
            continue
        for command_name, group in meta.custom_commands:
            if not group.startswith("NavigationPanel"):
                continue
            own = f"{full_name}.Command.{command_name}"
            if not visibility.get(own, True):
                continue
            # Обе видимости заданы явно - автор так решил (полный список рядом с отборами).
            if own in visibility and standard in visibility:
                continue
            if meta.command_is_plain_list(command_name):
                findings.append((name, "МЁРТВАЯ КОМАНДА", own,
                                 f"открывает тот же список без отбора, что {list_command}"))
            else:
                findings.append((name, "ОБЪЕКТ ДВАЖДЫ", own,
                                 f"вместе со стандартной {list_command} (tiny1C mdo-005)"))

    for command in sorted(mentioned - known):
        owner = command.split(".StandardCommand.")[0].split(".Command.")[0]
        if owner.startswith("CommonCommand.") and owner in content:
            continue
        if owner in content:
            continue
        findings.append((name, "ВИСЯЧАЯ ССЫЛКА", command,
                         f"{where}: объекта нет в <content> подсистемы"))


def collect(section=None):
    """Подсистемы разделов, участвующих в командном интерфейсе."""
    roots = []
    for mdo in sorted(SUBSYSTEMS.glob("*/*.mdo")):
        if mdo.parent.parent != SUBSYSTEMS:
            continue
        entry = read_subsystem(mdo)
        if not entry["in_interface"]:
            continue
        if section and entry["name"] != section:
            continue
        roots.append(entry)
        for child in sorted(mdo.parent.glob("Subsystems/*/*.mdo")):
            roots.append(read_subsystem(child))
    return roots


def main():
    parser = argparse.ArgumentParser(description="Сверка меню разделов с составом подсистем")
    parser.add_argument("--section", help="проверить один раздел")
    parser.add_argument("--quiet", action="store_true", help="только итог")
    args = parser.parse_args()

    findings = []
    entries = collect(args.section)
    for entry in entries:
        check_subsystem(entry, findings)

    if not args.quiet:
        current = None
        for subsystem, kind, command, note in findings:
            if subsystem != current:
                print(f"\n{subsystem}")
                current = subsystem
            print(f"  {kind:17} {command}\n  {'':17} {note}")

    print(f"\nСверка меню: подсистем {len(entries)}, расхождений {len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
