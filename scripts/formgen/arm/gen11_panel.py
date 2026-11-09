"""Фрагмент редакции 11 (см. gen11.py): исполняется exec с глобальными s (текст формы) и re; результат - в s."""
# Замечания владельца 2026-10-06: штатные стрелки списка заказов, количество ПФ/ГП в передаче, порядок колонок,
# выбор материала и ПФ/ГП сразу из отобранного.
ЯЗЫКИ = ['ru', 'fr', 'en', 'es']
граница = s.index('\n  <attributes>')
счетчик = [max(int(x) for x in re.findall(r'<id>(\d+)</id>', s[:граница]))]


def новый_id(m=None):
    счетчик[0] += 1
    return '<id>%d</id>' % счетчик[0]


def конец_элемента(s, начало):
    глубина = 0
    for m in re.finditer(r'<items[ >]|</items>', s[начало:]):
        if m.group(0).startswith('</'):
            глубина -= 1
            if глубина == 0:
                return начало + m.end()
        else:
            глубина += 1
    raise ValueError(начало)


def дети(s, начало, конец):
    """Непосредственные дочерние items (кроме вложенных в autoCommandBar) - список (имя, начало, конец)."""
    результат = []
    позиция = s.index('>', начало) + 1
    while True:
        m = re.compile(r'<items xsi:type="form:\w+">').search(s, позиция, конец)
        if not m:
            return результат
        вложено = s.rfind('<autoCommandBar>', начало, m.start()) > s.rfind('</autoCommandBar>', начало, m.start())
        к = конец_элемента(s, m.start())
        if not вложено:
            имя = re.search(r'<name>(\w+)</name>', s[m.start():к]).group(1)
            результат.append((имя, m.start(), к))
        позиция = к


# 1. Дополнения таблицы «Заказы» и поиск вне таблицы: без явных дополнений штатная навигация списка остаётся.
а = s.index('<items xsi:type="form:Table">\n            <name>Заказы</name>')
б = конец_элемента(s, а)
таблица = s[а:б]
ind = '            '
дополнения = ''
for тег, имя, тип, ext in [('searchStringAddition', 'ЗаказыСтрокаПоиска', None, 'SearchStringAdditionExtInfo'),
                           ('viewStatusAddition', 'ЗаказыСостояниеПросмотра', 'ViewStatusAddition',
                            'ViewStatusAdditionExtInfo'),
                           ('searchControlAddition', 'ЗаказыУправлениеПоиском', 'SearchControlAddition',
                            'SearchControlAdditionExtInfo')]:
    дополнения += ('%s  <%s>\n%s    <name>%s</name>\n%s    %s\n%s    <extendedTooltip>\n%s      <name>%sРасширеннаяПодсказка</name>\n'
                   '%s      %s\n%s      <type>Label</type>\n%s      <autoMaxWidth>true</autoMaxWidth>\n'
                   '%s      <autoMaxHeight>true</autoMaxHeight>\n%s      <extInfo xsi:type="form:LabelDecorationExtInfo">\n'
                   '%s        <horizontalAlign>Left</horizontalAlign>\n%s      </extInfo>\n%s    </extendedTooltip>\n'
                   '%s    <contextMenu>\n%s      <name>%sКонтекстноеМеню</name>\n%s      %s\n%s      <autoFill>true</autoFill>\n'
                   '%s    </contextMenu>\n'
                   % (ind, тег, ind, имя, ind, новый_id(), ind, ind, имя, ind, новый_id(), ind, ind, ind, ind, ind, ind,
                      ind, ind, ind, имя, ind, новый_id(), ind, ind))
    if тип:
        дополнения += '%s    <type>%s</type>\n' % (ind, тип)
    дополнения += ('%s    <source>Заказы</source>\n%s    <extInfo xsi:type="form:%s">\n%s      <autoMaxWidth>true</autoMaxWidth>\n'
                   '%s    </extInfo>\n%s  </%s>\n' % (ind, ind, ext, ind, ind, ind, тег))
конец_панели = таблица.index('</autoCommandBar>\n') + len('</autoCommandBar>\n')
таблица = таблица[:конец_панели] + дополнения + таблица[конец_панели:]
assert таблица.count('<viewStatusLocation>None</viewStatusLocation>') == 1
таблица = таблица.replace('<viewStatusLocation>None</viewStatusLocation>',
                          '<viewStatusLocation>None</viewStatusLocation>\n' + ind + '  <searchControlLocation>None</searchControlLocation>')
s = s[:а] + таблица + s[б:]

# 2. Колонка «КоличествоПродукции» реквизита «Переработки».
а = s.index('\n  <attributes>\n    <name>Переработки</name>')
б = s.index('\n  </attributes>', а)
номер = max(int(x) for x in re.findall(r'\n      <id>(\d+)</id>', s[а:б])) + 1
s = s[:б] + '''
    <columns>
      <name>КоличествоПродукции</name>
      <id>%d</id>
      <valueType>
        <types>Number</types>
        <numberQualifiers>
          <precision>15</precision>
          <scale>6</scale>
          <nonNegative>true</nonNegative>
        </numberQualifiers>
      </valueType>
      <view>
        <common>true</common>
      </view>
      <edit>
        <common>true</common>
      </edit>
    </columns>''' % номер + s[б:]

# 3. Поле «Кол-во ПФ/ГП» и порядок колонок передачи: Материал, Кол-во, Упак., Характ., ПФ/ГП, Кол-во ПФ/ГП, ...
а = s.index('<items xsi:type="form:Table">', s.index('<name>Переработки</name>') - 200)
б = конец_элемента(s, а)
таблица = s[а:б]
колонки = дети(таблица, 0, len(таблица))
блоки = {имя: таблица[н:к] for имя, н, к in колонки}
порядок = [имя for имя, _, _ in колонки]
образец = блоки['ПереработкиКоличествоУпаковок']
новое = образец.replace('ПереработкиКоличествоУпаковок', 'ПереработкиКоличествоПродукции').replace(
    'Переработки.КоличествоУпаковок', 'Переработки.КоличествоПродукции')
новое = re.sub(r'<id>\d+</id>', новый_id, новое)
for язык, короткий, полный in [('ru', 'Кол-во ПФ/ГП', 'Сколько ПФ/ГП ожидается из материала строки; пусто - по норме заказа'),
                                ('fr', 'Qté SF/PF', 'Quantité de SF/PF attendue de la matière de la ligne ; vide - selon la norme de la commande'),
                                ('en', 'SFG/FG qty', 'SFG/FG quantity expected from the line material; empty - by the order norm'),
                                ('es', 'Cant. SE/PT', 'Cantidad de SE/PT esperada del material de la línea; vacío - según la norma del pedido')]:
    новое = re.sub(r'(<title>\s*<key>%s</key>\s*<value>)[^<]*(</value>)' % язык, lambda m: m.group(1) + короткий + m.group(2), новое, count=1)
    новое = re.sub(r'(<toolTip>\s*<key>%s</key>\s*<value>)[^<]*(</value>)' % язык, lambda m: m.group(1) + полный + m.group(2), новое, count=1)
новое = re.sub(r'\s*<handlers>\s*<event>OnChange</event>\s*<name>\w+</name>\s*</handlers>', '', новое)
блоки['ПереработкиКоличествоПродукции'] = новое
новый_порядок = []
for имя in порядок:
    if имя in ('ПереработкиКоличествоУпаковок', 'ПереработкиУпаковка', 'ПереработкиХарактеристика', 'ПереработкиПродукция'):
        continue
    новый_порядок.append(имя)
    if имя == 'ПереработкиМатериал':
        новый_порядок += ['ПереработкиКоличествоУпаковок', 'ПереработкиУпаковка', 'ПереработкиХарактеристика',
                          'ПереработкиПродукция', 'ПереработкиКоличествоПродукции']
первая, последняя = колонки[0][1], колонки[-1][2]
отступ = таблица[таблица.rindex('\n', 0, первая) + 1:первая]
таблица = таблица[:первая] + ('\n' + отступ).join(блоки[имя] for имя in новый_порядок) + таблица[последняя:]
s = s[:а] + таблица + s[б:]

# 4. Выбор материала и ПФ/ГП сразу из отобранного: кнопка выпадающего списка ввода по строке не показывается.
for имя in ['ЗаказыПоставщикуМатериал', 'ПоступленияМатериал', 'ПереработкиМатериал', 'ПереработкиПродукция']:
    а = s.index('<name>%s</name>' % имя)
    е = s.index('<extInfo xsi:type="form:InputFieldExtInfo">', а)
    к = s.index('</extInfo>', е)
    ext = s[е:к]
    assert 'dropListButton' not in ext, имя
    m = re.search(r'\n(\s*)<autoMaxHeight>true</autoMaxHeight>\n', ext)
    ext = ext[:m.end()] + '%s<dropListButton>false</dropListButton>\n%s<choiceButton>true</choiceButton>\n' % (
        m.group(1), m.group(1)) + ext[m.end():]
    s = s[:е] + ext + s[к:]
