#!/usr/bin/env python3
"""Сверка прав ролей: у ссылочного объекта с правом «Просмотр» должно быть и
«Ввод по строке». Без него поле ввода не подбирает значение по набранному
тексту — пользователь видит только историю выбора, а администратор (все права)
ошибки не воспроизводит (ОператорПроизводства, 2026-11-01).

Проверяются все роли: роль без своего права на клиент работает в паре с другой
(«Складские ордера» с «Оператором производства»). Явный запрет
(<value>false</value>) при «Просмотре» тоже расхождение: иначе дефект
возвращается одной правкой роли. Исключение — объекты, где «Ввод по строке»
явно снят у роли «Администратор» (служебные ПВХ и план счетов): это эталон,
другие роли его не расширяют.

Использование: scripts/rolecheck.py [каталог EDT-проекта или его src]. Код возврата 1 — есть
расхождения.
"""
import os
import re
import sys

KINDS = ("Catalog.", "Document.", "ChartOfCharacteristicTypes.", "ChartOfAccounts.",
         "ExchangePlan.", "BusinessProcess.", "Task.", "ChartOfCalculationTypes.")
OBJECT = re.compile(r"<object>\s*<name>([^<]+)</name>(.*?)</object>", re.S)
RIGHT = re.compile(r"<name>(\w+)</name>\s*<value>(\w+)</value>")


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "src", "cf")
    roles = os.path.join(src, "Roles")
    if not os.path.isdir(roles):
        roles = os.path.join(src, "src", "Roles")
    admin = open(os.path.join(roles, "Администратор", "Rights.rights"), encoding="utf-8").read()
    denied = {match.group(1) for match in OBJECT.finditer(admin)
              if dict(RIGHT.findall(match.group(2))).get("InputByString") == "false"}
    findings = []
    for role in sorted(os.listdir(roles)):
        path = os.path.join(roles, role, "Rights.rights")
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        for match in OBJECT.finditer(text):
            name = match.group(1)
            if not name.startswith(KINDS) or name.count(".") != 1 or name in denied:
                continue
            rights = dict(RIGHT.findall(match.group(2)))
            if rights.get("View") == "true" and rights.get("InputByString") != "true":
                findings.append(f"{role}: {name}")
    for line in findings:
        print(f"Просмотр без «Ввода по строке» — {line}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
