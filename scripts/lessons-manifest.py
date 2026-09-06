#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генерация и проверка машинного манифеста уроков docs/rules-1c/lessons/rules.json.

Манифест собирается из фронтматтеров файлов уроков — руками его не правят.
Поверх манифеста строится MCP-сервер правил (см. README уроков), поэтому здесь
же проверяется то, что сервер потом принимает на веру:

  1. id урока совпадает с именем файла, обязательные поля заполнены;
  2. категория и серьёзность — из закрытых списков;
  3. каждый адрес в `check` разрешается: файл существует, а якорь после «::»
     в нём встречается. Правило, назвавшее исчезнувший шаг проверки, — ошибка:
     иначе манифест обещает проверку, которой нет;
  4. у правила без машинной проверки (`check: []`) заполнено `ручная_проверка` —
     иначе правило не говорит, чем вообще ловится.

Использование:
  scripts/lessons-manifest.py             перегенерировать rules.json
  scripts/lessons-manifest.py --проверить проверить без записи (1 при расхождениях)
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "docs", "rules-1c", "lessons")
MANIFEST = os.path.join(LESSONS, "rules.json")

CATEGORIES = ["запросы", "модули", "формы-xml", "метаданные", "макеты", "процесс"]
SEVERITIES = ["критично", "важно", "справка"]
PLATFORMS = ["8.3", "8.5"]
REQUIRED = ["id", "категория", "серьёзность", "заголовок", "ключи", "платформы", "check"]
ORDER = ["id", "файл", "категория", "серьёзность", "платформы", "заголовок", "ключи",
         "check", "ручная_проверка"]


def parse_scalar(raw):
    """Значение фронтматтера: строка в кавычках, плоский список или голая строка."""
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        items, current, quote = [], "", None
        for ch in inner:
            if quote:
                if ch == quote:
                    quote = None
                else:
                    current += ch
            elif ch in "\"'":
                quote = ch
            elif ch == ",":
                items.append(current.strip())
                current = ""
            else:
                current += ch
        items.append(current.strip())
        return [item for item in items if item]
    if len(raw) > 1 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    return raw


def read_frontmatter(path):
    """Фронтматтер урока словарём; None, если блока --- ... --- нет."""
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None
    data = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        data[key.strip()] = parse_scalar(raw)
    return data


def check_address(address):
    """Проверка адреса «путь» или «путь::якорь». Возвращает текст ошибки или None."""
    path, _, anchor = address.partition("::")
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return "файла нет: %s" % path
    if not anchor:
        return None
    with open(full, encoding="utf-8") as handle:
        body = handle.read()
    if anchor not in body:
        return "в %s нет якоря «%s»" % (path, anchor)
    return None


def collect():
    """Разбор всех уроков. Возвращает (список правил, список ошибок)."""
    rules, errors = [], []
    names = sorted(name for name in os.listdir(LESSONS)
                   if name.endswith(".md") and name != "README.md")
    seen = set()
    for name in names:
        path = os.path.join(LESSONS, name)
        data = read_frontmatter(path)
        if data is None:
            errors.append("%s: нет фронтматтера" % name)
            continue
        rule_id = data.get("id", "")
        if rule_id != name[:-3]:
            errors.append("%s: id «%s» не совпадает с именем файла" % (name, rule_id))
        if rule_id in seen:
            errors.append("%s: id «%s» уже занят" % (name, rule_id))
        seen.add(rule_id)
        for field in REQUIRED:
            if field not in data:
                errors.append("%s: нет поля «%s»" % (name, field))
        if data.get("категория") not in CATEGORIES:
            errors.append("%s: неизвестная категория «%s»" % (name, data.get("категория")))
        if data.get("серьёзность") not in SEVERITIES:
            errors.append("%s: неизвестная серьёзность «%s»" % (name, data.get("серьёзность")))
        for platform in data.get("платформы", []):
            if platform not in PLATFORMS:
                errors.append("%s: неизвестная платформа «%s»" % (name, platform))
        checks = data.get("check", [])
        if isinstance(checks, str):
            errors.append("%s: check должен быть списком" % name)
            checks = [checks]
        for address in checks:
            problem = check_address(address)
            if problem:
                errors.append("%s: check — %s" % (name, problem))
        if not checks and not data.get("ручная_проверка"):
            errors.append("%s: пустой check без «ручная_проверка» — правило не говорит,"
                          " чем ловится" % name)
        rule = {"id": rule_id, "файл": name}
        for field in ORDER:
            if field in ("id", "файл"):
                continue
            if field in data:
                rule[field] = data[field]
        rules.append(rule)
    order = {name: index for index, name in enumerate(names)}
    rules.sort(key=lambda item: order[item["файл"]])
    return rules, errors


def build(rules):
    """Тело манифеста со сводкой по покрытию проверками."""
    without = [rule["id"] for rule in rules if not rule.get("check")]
    addresses = sorted({address for rule in rules for address in rule.get("check", [])})
    return {
        "версия": 2,
        "правил": len(rules),
        "с_машинной_проверкой": len(rules) - len(without),
        "без_машинной_проверки": without,
        "адреса_проверок": addresses,
        "правила": rules,
    }


def main():
    args = sys.argv[1:]
    dry_run = "--проверить" in args or "--check" in args
    rules, errors = collect()
    manifest = build(rules)
    body = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"

    for error in errors:
        print("ОШИБКА: %s" % error)

    if dry_run:
        stale = True
        if os.path.exists(MANIFEST):
            with open(MANIFEST, encoding="utf-8") as handle:
                stale = handle.read() != body
        if stale:
            print("ОШИБКА: rules.json разошёлся с уроками — перегенерировать"
                  " scripts/lessons-manifest.py")
        if errors or stale:
            return 1
        print("Манифест уроков: %d правил, из них с машинной проверкой %d"
              % (manifest["правил"], manifest["с_машинной_проверкой"]))
        return 0

    if errors:
        print("Манифест не записан: сначала разобрать ошибки выше.")
        return 1

    with open(MANIFEST, "w", encoding="utf-8") as handle:
        handle.write(body)
    print("Записан %s: правил %d, с машинной проверкой %d, без неё %d"
          % (os.path.relpath(MANIFEST, ROOT), manifest["правил"],
             manifest["с_машинной_проверкой"], len(manifest["без_машинной_проверки"])))
    if manifest["без_машинной_проверки"]:
        print("Ловятся только руками: %s" % ", ".join(manifest["без_машинной_проверки"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
