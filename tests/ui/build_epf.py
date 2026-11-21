#!/usr/bin/env python3
"""Собирает XML-исходник внешней обработки тестов интерфейса: каркас от scripts/print-preview/build_epf.py,
модуль формы целиком заменяется клиентским модулем (ядро выполняется на клиенте тест-менеджера).

Запуск: build_epf.py <ИмяОбработки> <модуль.bsl> <каталог-вывода>; вызывается из scripts/uitest.sh."""
import os
import subprocess
import sys
import tempfile

name, module, out = sys.argv[1], sys.argv[2], sys.argv[3]
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with tempfile.NamedTemporaryFile('w', suffix='.bsl', encoding='utf-8', delete=False) as stub:
    stub.write('&НаСервереБезКонтекста\nПроцедура Главная(Части, Лог)\nКонецПроцедуры\n')
subprocess.check_call([sys.executable, os.path.join(root, 'scripts/print-preview/build_epf.py'), name, stub.name, out])
os.unlink(stub.name)
text = open(module, encoding='utf-8').read()
with open(os.path.join(out, name, 'Forms/Форма/Ext/Form/Module.bsl'), 'w', encoding='utf-8-sig') as f:
    f.write(text)
