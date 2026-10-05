"""Фрагмент редакции 10 (см. gen10.py): исполняется exec с глобальными s (текст формы) и re; результат - в s."""
# Закладка «Передача в переработку», колонка ПФ/ГП строки передачи и таблица свойств ПФ/ГП справа (2026-10-05).
ЯЗЫКИ = ['ru', 'fr', 'en', 'es']


def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (s.count(old), old[:100])
    s = s.replace(old, new)


def локализация(ind, тег, значения):
    return ''.join('%s<%s>\n%s  <key>%s</key>\n%s  <value>%s</value>\n%s</%s>\n'
                   % (ind, тег, ind, к, ind, з, ind, тег) for к, з in zip(ЯЗЫКИ, значения))


граница = s.index('\n  <attributes>')
счетчик = [max(int(x) for x in re.findall(r'<id>(\d+)</id>', s[:граница]))]


def новый_id():
    счетчик[0] += 1
    return счетчик[0]


def подсказка(ind, имя):
    return ('%s<extendedTooltip>\n%s  <name>%sРасширеннаяПодсказка</name>\n%s  <id>%d</id>\n%s  <type>Label</type>\n'
            '%s  <autoMaxWidth>true</autoMaxWidth>\n%s  <autoMaxHeight>true</autoMaxHeight>\n'
            '%s  <extInfo xsi:type="form:LabelDecorationExtInfo">\n%s    <horizontalAlign>Left</horizontalAlign>\n'
            '%s  </extInfo>\n%s</extendedTooltip>\n'
            % (ind, ind, имя, ind, новый_id(), ind, ind, ind, ind, ind, ind, ind))


def контекстное_меню(ind, имя):
    return ('%s<contextMenu>\n%s  <name>%sКонтекстноеМеню</name>\n%s  <id>%d</id>\n%s  <autoFill>true</autoFill>\n'
            '%s</contextMenu>\n' % (ind, ind, имя, ind, новый_id(), ind, ind))


def видимость(ind):
    return ('%s<visible>true</visible>\n%s<enabled>true</enabled>\n%s<userVisible>\n%s  <common>true</common>\n'
            '%s</userVisible>\n' % (ind, ind, ind, ind, ind))


def поле(ind, имя, путь, заголовки, вид, обработчики=(), обработчики_ext=(), ширина=None, подсказки=None):
    id_ = новый_id()
    текст = '%s<items xsi:type="form:FormField">\n%s  <name>%s</name>\n%s  <id>%d</id>\n' % (ind, ind, имя, ind, id_)
    текст += локализация(ind + '  ', 'title', заголовки)
    if подсказки:
        текст += локализация(ind + '  ', 'toolTip', подсказки)
    текст += видимость(ind + '  ')
    текст += '%s  <dataPath xsi:type="form:DataPath">\n%s    <segments>%s</segments>\n%s  </dataPath>\n' % (
        ind, ind, путь, ind)
    for событие, обработчик in обработчики:
        текст += '%s  <handlers>\n%s    <event>%s</event>\n%s    <name>%s</name>\n%s  </handlers>\n' % (
            ind, ind, событие, ind, обработчик, ind)
    текст += подсказка(ind + '  ', имя) + контекстное_меню(ind + '  ', имя)
    текст += '%s  <type>%s</type>\n%s  <editMode>Enter</editMode>\n%s  <showInHeader>true</showInHeader>\n' % (
        ind, вид, ind, ind)
    текст += '%s  <headerHorizontalAlign>Left</headerHorizontalAlign>\n%s  <showInFooter>true</showInFooter>\n' % (
        ind, ind)
    ext = 'InputFieldExtInfo' if вид == 'InputField' else 'LabelFieldExtInfo'
    текст += '%s  <extInfo xsi:type="form:%s">\n' % (ind, ext)
    for событие, обработчик in обработчики_ext:
        текст += '%s    <handlers>\n%s      <event>%s</event>\n%s      <name>%s</name>\n%s    </handlers>\n' % (
            ind, ind, событие, ind, обработчик, ind)
    if ширина:
        текст += '%s    <width>%d</width>\n%s    <autoMaxWidth>false</autoMaxWidth>\n' % (ind, ширина, ind)
    else:
        текст += '%s    <autoMaxWidth>true</autoMaxWidth>\n' % ind
    текст += '%s    <autoMaxHeight>true</autoMaxHeight>\n' % ind
    if вид == 'InputField':
        текст += '%s    <textEdit>true</textEdit>\n%s    <textSize>Normal</textSize>\n' % (ind, ind)
    текст += '%s  </extInfo>\n%s</items>\n' % (ind, ind)
    return текст


# 1. Заголовок закладки.
а = s.index('<name>СтраницаПереработки</name>')
б = s.index('<visible>', а)
кусок = s[а:б]
for старое, новое in [('Переработка', 'Передача в переработку'), ('Sous-traitance', 'Transfert en sous-traitance'),
                      ('Subcontracting', 'Subcontracting transfer'), ('Subcontratación', 'Envío a subcontratación')]:
    assert кусок.count('<value>%s</value>' % старое) == 1, старое
    кусок = кусок.replace('<value>%s</value>' % старое, '<value>%s</value>' % новое)
s = s[:а] + кусок + s[б:]

# 2. Колонка «Продукция» реквизита «Переработки».
а = s.index('\n  <attributes>\n    <name>Переработки</name>')
б = s.index('\n  </attributes>', а)
реквизит = s[а:б]
номер = max(int(x) for x in re.findall(r'\n      <id>(\d+)</id>', реквизит)) + 1
колонка = '''
    <columns>
      <name>Продукция</name>
      <id>%d</id>
      <valueType>
        <types>CatalogRef.Номенклатура</types>
      </valueType>
      <view>
        <common>true</common>
      </view>
      <edit>
        <common>true</common>
      </edit>
    </columns>''' % номер
s = s[:б] + колонка + s[б:]

# 3. Реквизиты таблицы свойств.
номер_реквизита = max(int(x) for x in re.findall(r'\n  <attributes>\n    <name>\w+</name>\n(?:    <title>\n(?:.*\n)*?    </title>\n)*    <id>(\d+)</id>', s)) + 1


def колонка_реквизита(имя, id_, типы):
    return ('    <columns>\n      <name>%s</name>\n      <id>%d</id>\n      <valueType>\n%s\n      </valueType>\n'
            '      <view>\n        <common>true</common>\n      </view>\n      <edit>\n        <common>true</common>\n'
            '      </edit>\n    </columns>\n' % (имя, id_, типы))


ТИП_ЗНАЧЕНИЯ = '''        <types>CatalogRef.ЗначенияДополнительныхРеквизитов</types>
        <types>CatalogRef.Контрагенты</types>
        <types>CatalogRef.Номенклатура</types>
        <types>String</types>
        <types>Date</types>
        <types>Boolean</types>
        <types>Number</types>
        <numberQualifiers>
          <precision>15</precision>
          <scale>3</scale>
        </numberQualifiers>
        <stringQualifiers>
          <length>200</length>
        </stringQualifiers>
        <dateQualifiers>
          <dateFractions>Date</dateFractions>
        </dateQualifiers>'''
реквизиты = '''  <attributes>
    <name>СвойстваПродукции</name>
%s    <id>%d</id>
    <valueType>
      <types>ValueTable</types>
    </valueType>
    <view>
      <common>true</common>
    </view>
    <edit>
      <common>true</common>
    </edit>
%s  </attributes>
  <attributes>
    <name>ПродукцияСвойств</name>
    <id>%d</id>
    <valueType>
      <types>CatalogRef.Номенклатура</types>
    </valueType>
    <view>
      <common>true</common>
    </view>
    <edit>
      <common>true</common>
    </edit>
  </attributes>
''' % (локализация('    ', 'title', ['Свойства ПФ/ГП', 'Propriétés SF/PF', 'SFG/FG properties', 'Propiedades SE/PT']),
       номер_реквизита,
       колонка_реквизита('Свойство', 1, '        <types>ChartOfCharacteristicTypesRef.ДополнительныеРеквизиты</types>')
       + колонка_реквизита('Заголовок', 2, '        <types>String</types>')
       + колонка_реквизита('Подсказка', 3, '        <types>String</types>')
       + колонка_реквизита('Обязательный', 4, '        <types>Boolean</types>')
       + колонка_реквизита('ТипЗначения', 5, '        <types>TypeDescription</types>')
       + колонка_реквизита('Значение', 6, ТИП_ЗНАЧЕНИЯ),
       номер_реквизита + 1)
вставка = s.index('\n  <formCommands') + 1
s = s[:вставка] + реквизиты + s[вставка:]

# 4. Поле «ПФ/ГП» после «Материала» в таблице передач.
а = s.index('<name>ПереработкиМатериал</name>')
отступ_поля = s.rindex('\n', 0, s.rindex('<items xsi:type="form:FormField">', 0, а)) + 1
пробелы = s[отступ_поля:s.index('<items', отступ_поля)]
конец_материала = s.index('\n' + пробелы + '</items>\n', а) + len('\n' + пробелы + '</items>\n')
поле_продукции = поле(пробелы, 'ПереработкиПродукция', 'Переработки.Продукция', ['ПФ/ГП', 'SF/PF', 'SFG/FG', 'SE/PT'],
                      'InputField', обработчики=[('OnChange', 'ПереработкиПродукцияПриИзменении')],
                      обработчики_ext=[('StartChoice', 'ПереработкиПродукцияНачалоВыбора')], ширина=16,
                      подсказки=['Полуфабрикат или готовая продукция заказа, для которой передаётся материал; пусто - по составу заказа',
                                 'Semi-fini ou produit fini de la commande pour lequel la matière est transférée ; vide - selon la composition de la commande',
                                 'Semi-finished or finished product of the order the material is transferred for; empty - by the order composition',
                                 'Semielaborado o producto terminado del pedido para el que se transfiere el material; vacío - según la composición del pedido'])
s = s[:конец_материала] + поле_продукции + s[конец_материала:]

# 5. Таблица передач и таблица свойств - рядом, в горизонтальной группе страницы.
а = s.index('<items xsi:type="form:Table">\n              <name>Переработки</name>')
начало_таблицы = s.rindex('\n', 0, а) + 1
конец_таблицы = s.index('\n            </items>\n            <type>Page</type>', а) + len('\n            </items>\n')
таблица = s[начало_таблицы:конец_таблицы]
таблица = '\n'.join(('  ' + строка) if строка else строка for строка in таблица.split('\n'))
таблица = таблица.rstrip(' ')


def группа(ind, имя, заголовки, вложенное, ориентация, показать_заголовок, ширина=None):
    текст = '%s<items xsi:type="form:FormGroup">\n%s  <name>%s</name>\n%s  <id>%d</id>\n' % (ind, ind, имя, ind, новый_id())
    if заголовки:
        текст += локализация(ind + '  ', 'title', заголовки)
    текст += видимость(ind + '  ') + подсказка(ind + '  ', имя) + вложенное
    текст += '%s  <type>UsualGroup</type>\n%s  <extInfo xsi:type="form:UsualGroupExtInfo">\n' % (ind, ind)
    текст += '%s    <group>%s</group>\n%s    <representation>None</representation>\n' % (ind, ориентация, ind)
    текст += '%s    <showLeftMargin>false</showLeftMargin>\n%s    <united>true</united>\n' % (ind, ind)
    текст += '%s    <showTitle>%s</showTitle>\n%s    <throughAlign>Auto</throughAlign>\n' % (
        ind, 'true' if показать_заголовок else 'false', ind)
    текст += '%s    <currentRowUse>Auto</currentRowUse>\n%s  </extInfo>\n%s</items>\n' % (ind, ind, ind)
    return текст


# Таблица свойств: шапка и хвост - по таблице «Материалы» (простая таблица формы этой же формы).
а = s.index('<items xsi:type="form:Table">\n              <name>Материалы</name>')
начало_м = s.rindex('\n', 0, а) + 1
первая_колонка = s.index('<items xsi:type="form:FormField">', а)
шапка = s[начало_м:s.rindex('\n', 0, первая_колонка) + 1]
хвост_начало = s.index('              <representation>Tree</representation>\n', а)
хвост_конец = s.index('\n            </items>\n', хвост_начало) + len('\n            </items>\n')
хвост = s[хвост_начало:хвост_конец]
шапка = шапка.replace('<name>Материалы</name>', '<name>СвойстваПродукции</name>')
шапка = шапка.replace('<segments>Материалы</segments>', '<segments>СвойстваПродукции</segments>')
шапка = шапка.replace('<name>МатериалыРасширеннаяПодсказка</name>', '<name>СвойстваПродукцииРасширеннаяПодсказка</name>')
шапка = шапка.replace('<name>МатериалыКонтекстноеМеню</name>', '<name>СвойстваПродукцииКонтекстноеМеню</name>')
шапка = шапка.replace('<name>МатериалыКоманднаяПанель</name>', '<name>СвойстваПродукцииКоманднаяПанель</name>')
шапка = шапка.replace('              <readOnly>true</readOnly>\n', '')
шапка = re.sub(r'<id>\d+</id>', lambda m: '<id>%d</id>' % новый_id(), шапка)
assert 'Материалы' not in шапка
шапка += ('              <handlers>\n                <event>OnStartEdit</event>\n'
          '                <name>СвойстваПродукцииПриНачалеРедактирования</name>\n              </handlers>\n')
хвост = хвост.replace('              <representation>Tree</representation>\n', '')
хвост = хвост.replace('<horizontalStretch>true</horizontalStretch>', '<horizontalStretch>false</horizontalStretch>')
колонки = поле('              ', 'СвойстваПродукцииЗаголовок', 'СвойстваПродукции.Заголовок',
               ['Свойство', 'Propriété', 'Property', 'Propiedad'], 'LabelField', ширина=14)
колонки += поле('              ', 'СвойстваПродукцииЗначение', 'СвойстваПродукции.Значение',
                ['Значение', 'Valeur', 'Value', 'Valor'], 'InputField',
                обработчики=[('OnChange', 'СвойстваПродукцииЗначениеПриИзменении')], ширина=16)
таблица_свойств = шапка + колонки + хвост
таблица_свойств = '\n'.join(('    ' + строка) if строка else строка for строка in таблица_свойств.split('\n')).rstrip(' ')
свойства = группа('              ', 'ГруппаСвойстваПродукции', ['Свойства ПФ/ГП', 'Propriétés SF/PF', 'SFG/FG properties',
                                                                'Propiedades SE/PT'],
                  таблица_свойств, 'Vertical', True)
обертка = группа('            ', 'ГруппаПереработкиИСвойства', None, таблица + свойства, 'AlwaysHorizontal', False)
s = s[:начало_таблицы] + обертка + s[конец_таблицы:]
