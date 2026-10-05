"""Фрагмент редакции 10 (см. gen10.py): исполняется exec с глобальными s (текст формы) и re; результат - в s."""
# Количественные колонки уже, заголовки короче; полное имя - в подсказке колонки (замечание владельца 2026-10-05).
ЯЗЫКИ = ['ru', 'fr', 'en', 'es']
ТАБЛИЦЫ = ['Продукция', 'ЗаказыПоставщику', 'Поступления', 'Выпуски', 'Отгрузки', 'Переработки',
           'ПоступленияПереработки']
# колонка -> (короткие заголовки или None, ширина)
КОЛОНКИ = {
    'КоличествоУпаковок': (('Кол-во', 'Qté', 'Qty', 'Cant.'), 8),
    'Упаковка': (('Упак.', 'Cond.', 'Pack', 'Emb.'), 7),
    'Характеристика': (('Характ.', 'Caract.', 'Charact.', 'Caract.'), 10),
    'Цена': (None, 9),
    'Сумма': (None, 10),
    'ПроцентПотерь': (None, 7),
    'СтоимостьУслуг': (None, 9),
    'Поступления': (('Поступления', 'Réceptions', 'Receipts', 'Recepciones'), 16),
    'НомерВходящегоДокумента': (('№ накл.', 'N° fact.', 'Inv. no.', 'N.º fact.'), 9),
    'ДатаВходящегоДокумента': (('Дата накл.', 'Date fact.', 'Inv. date', 'Fecha fact.'), 10),
}


def блок_поля(s, имя):
    начало = s.index('<items xsi:type="form:FormField">\n', s.index('<name>%s</name>' % имя) - 120)
    отступ = s.rindex('\n', 0, начало) + 1
    пробелы = s[отступ:начало]
    конец = s.index('\n' + пробелы + '</items>\n', начало) + len('\n' + пробелы + '</items>\n')
    return отступ, конец


def заголовки(ind, тег, значения):
    return ''.join('%s<%s>\n%s  <key>%s</key>\n%s  <value>%s</value>\n%s</%s>\n'
                   % (ind, тег, ind, к, ind, з, ind, тег) for к, з in zip(ЯЗЫКИ, значения))


for таблица in ТАБЛИЦЫ:
    for колонка, (короткие, ширина) in КОЛОНКИ.items():
        имя = таблица + колонка
        if s.find('<name>%s</name>' % имя) < 0:
            continue
        а, б = блок_поля(s, имя)
        блок = s[а:б]
        ind = re.search(r'\n(\s*)<name>' + имя + '</name>', блок).group(1)
        прежние = dict(re.findall(ind + r'<title>\n\s*<key>(\w+)</key>\n\s*<value>([^<]*)</value>\n\s*</title>\n', блок))
        if короткие and set(прежние) == set(ЯЗЫКИ):
            assert '<toolTip>' not in блок, имя
            новые = заголовки(ind, 'title', короткие) + заголовки(ind, 'toolTip', [прежние[к] for к in ЯЗЫКИ])
            блок = re.sub('(' + ind + r'<title>\n(?:.*\n)*?' + ind + r'</title>\n)+', lambda m: новые, блок, count=1)
        ext = блок.rindex('<extInfo xsi:type="form:')
        хвост = блок[ext:]
        if '<width>' in хвост:
            хвост = re.sub(r'<width>\d+</width>', '<width>%d</width>' % ширина, хвост, count=1)
        else:
            хвост = re.sub(r'(\s*)<autoMaxWidth>', lambda m: '%s<width>%d</width>%s<autoMaxWidth>'
                           % (m.group(1), ширина, m.group(1)), хвост, count=1)
        хвост = хвост.replace('<autoMaxWidth>true</autoMaxWidth>', '<autoMaxWidth>false</autoMaxWidth>', 1)
        блок = блок[:ext] + хвост
        s = s[:а] + блок + s[б:]
