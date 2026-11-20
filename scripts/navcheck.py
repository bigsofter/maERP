#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сверка панели навигации форм документов: ссылка «Файлы» регистра присоединённых файлов скрыта.

Регистр ПрисоединённыеФайлы с ведущим измерением «Объект» добавляет в панель навигации формы владельца ссылку
«Файлы». В форме без закладок в корне клиент 8.5 рисует навигацию переключателем «Основное ˅» и уносит командную
панель в его строку — строка заголовка остаётся пустой (тикет 2605137, 2.0.17.46). У документов из типа параметра
общей команды ФайлыДокумента ссылка дублирует эту команду и скрыта записью cmiFragmentRecord с пустым userVisible.

Проверяется каждая форма объекта (extInfo DocumentFormExtInfo) каждого такого документа: новая форма документа без
скрытой ссылки — находка. Вид формы в клиенте машиной не снимается, эта сверка держит только причину.

Использование: scripts/navcheck.py [каталог-исходников]   (код возврата 1 при находках)
"""
import glob
import io
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DEFAULT = os.path.join(ROOT, "src", "cf", "src")
LINK = "InformationRegister.ПрисоединённыеФайлы.StandardCommand.OpenByValue.Объект"
HIDDEN = re.compile(r"<cmiFragmentRecord>\s*<command>" + re.escape(LINK) + r"</command>\s*<userVisible/>")


def nfc(text):
    return unicodedata.normalize("NFC", text)


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else SRC_DEFAULT
    command = os.path.join(src, "CommonCommands", "ФайлыДокумента", "ФайлыДокумента.mdo")
    if not os.path.exists(command):
        print("Сверка навигации форм: общей команды ФайлыДокумента нет — проверять нечего")
        return 0
    documents = re.findall(r"<types>DocumentRef\.([^<]+)</types>", nfc(io.open(command, encoding="utf-8").read()))
    findings = []
    forms = 0
    for name in sorted(set(documents)):
        pattern = os.path.join(src, "Documents", name, "Forms", "*", "Form.form")
        for path in sorted({os.path.realpath(p) for p in glob.glob(pattern) + glob.glob(nfc(pattern))}):
            text = nfc(io.open(path, encoding="utf-8").read())
            if "form:DocumentFormExtInfo" not in text:
                continue
            forms += 1
            if not HIDDEN.search(text):
                findings.append(nfc(os.path.relpath(path, ROOT)))
    findings = sorted(set(findings))
    if not findings:
        print("Сверка навигации форм: ссылка «Файлы» скрыта во всех формах документов (форм — %d)" % forms)
        return 0
    print("Сверка навигации форм: ссылка «Файлы» не скрыта — %d" % len(findings))
    for path in findings:
        print("  %s" % path)
    return 1


if __name__ == "__main__":
    sys.exit(main())
