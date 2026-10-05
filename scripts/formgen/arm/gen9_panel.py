"""Фрагмент редакции 9 (см. gen9.py): исполняется exec с глобальными s (текст формы) и re; результат - в s."""
# Панель фильтров, запрос списка заказов, пагинатор с легендой, команды страниц.
def rep(old,new,cnt=1):
    global s
    assert s.count(old)==cnt,(s.count(old),old[:120])
    s=s.replace(old,new)
def L(tag,vals,ind):
    return ''.join(f'{ind}<{tag}>\n{ind}  <key>{l}</key>\n{ind}  <value>{v}</value>\n{ind}</{tag}>\n' for l,v in zip(['ru','fr','en','es'],vals))

# --- 1. remove РежимОчереди item
a=s.index('          <items xsi:type="form:FormField">\n            <name>РежимОчереди</name>')
b=s.index('          <items xsi:type="form:FormField">\n            <name>ОтборКлиент</name>')
s=s[:a]+s[b:]
# --- remove РежимОчереди attribute
a=s.index('  <attributes>\n    <name>РежимОчереди</name>')
b=s.index('  <attributes>\n    <name>Заказы</name>')
s=s[:a]+s[b:]
# --- 2. types of filter attributes
for nm,t in [('ОтборКлиент','CatalogRef.Контрагенты'),('ОтборПродукция','CatalogRef.Номенклатура')]:
    a=s.index(f'  <attributes>\n    <name>{nm}</name>')
    b=s.index('  </attributes>',a)
    blk=s[a:b]
    old='''    <valueType>
      <types>String</types>
        <stringQualifiers>
          <length>100</length>
        </stringQualifiers>
    </valueType>'''
    assert old in blk
    blk=blk.replace(old,f'    <valueType>\n      <types>{t}</types>\n    </valueType>')
    s=s[:a]+blk+s[b:]

# --- new attributes after ОтборПродукция
def attr(name,id_,types,title=None):
    t=L('title',title,'    ') if title else ''
    return f'''  <attributes>
    <name>{name}</name>
{t}    <id>{id_}</id>
    <valueType>
{types}
    </valueType>
    <view>
      <common>true</common>
    </view>
    <edit>
      <common>true</common>
    </edit>
  </attributes>
'''
num='''      <types>Number</types>
        <numberQualifiers>
          <precision>10</precision>
          <scale>0</scale>
          <nonNegative>true</nonNegative>
        </numberQualifiers>'''
newattrs=(attr('ОтборСтадия',44,'      <types>EnumRef.СтатусыЗаказовПокупателя</types>',('Стадия','Étape','Stage','Etapa'))
 +attr('ОтборПериодОтгрузки',45,'      <types>StandardPeriod</types>',('Дата отгрузки','Date d\'expédition','Shipment date','Fecha de envío'))
 +attr('НомерСтраницы',46,num)+attr('ВсегоСтраниц',47,num))
a=s.index('  <attributes>\n    <name>ОтборПродукция</name>')
b=s.index('  </attributes>\n',a)+len('  </attributes>\n')
s=s[:b]+newattrs+s[b:]

# --- 3. dyn list query
qa=s.index('      <queryText>ВЫБРАТЬ\n\tДокументЗаказПокупателя.Ссылка')
qb=s.index('</queryText>',qa)
q='''      <queryText>ВЫБРАТЬ
	Заказы.Ссылка КАК Ссылка,
	Заказы.ПометкаУдаления КАК ПометкаУдаления,
	Заказы.Проведен КАК Проведен,
	Заказы.Номер КАК Номер,
	Заказы.Дата КАК Дата,
	Заказы.ДатаОтгрузки КАК ДатаОтгрузки,
	Заказы.Контрагент КАК Контрагент,
	Заказы.Менеджер КАК Менеджер,
	Заказы.Сумма КАК Сумма,
	Заказы.ВидОперации КАК ВидОперации,
	История.СтатусЗаказаПокупателя КАК Статус,
	История.Индикатор КАК Индикатор
ИЗ
	Документ.ЗаказПокупателя КАК Заказы
		ЛЕВОЕ СОЕДИНЕНИЕ РегистрСведений.ИсторияЗаказовПокупателейПоСтатусам.СрезПоследних КАК История
		ПО Заказы.Ссылка = История.ЗаказПокупателя
ГДЕ
	Заказы.ВидОперации = ЗНАЧЕНИЕ(Перечисление.ВидыОперацийЗаказаПокупателя.Производство)
	И (&amp;ЛюбойКлиент
			ИЛИ Заказы.Контрагент = &amp;Клиент)
	И (&amp;ЛюбаяПродукция
			ИЛИ Заказы.Ссылка В
				(ВЫБРАТЬ
					ТоварыОтбора.Ссылка
				ИЗ
					Документ.ЗаказПокупателя.ТЧТовары КАК ТоварыОтбора
				ГДЕ
					ТоварыОтбора.Номенклатура = &amp;Продукция))
	И (&amp;ЛюбаяСтадия
			ИЛИ ЕСТЬNULL(История.СтатусЗаказаПокупателя, ЗНАЧЕНИЕ(Перечисление.СтатусыЗаказовПокупателя.Черновик)) = &amp;Стадия)
	И (НЕ &amp;ЕстьНачалоОтгрузки
			ИЛИ Заказы.ДатаОтгрузки &gt;= &amp;НачалоОтгрузки)
	И (НЕ &amp;ЕстьКонецОтгрузки
			ИЛИ Заказы.ДатаОтгрузки &lt;= &amp;КонецОтгрузки)'''
s=s[:qa]+q+s[qb:]

# --- 4. filter panel fields: after ОтборПродукция item
a=s.index('          <items xsi:type="form:FormField">\n            <name>ОтборПродукция</name>')
b=s.index('\n          </items>\n',a)+len('\n          </items>\n')
prod=s[a:b]
def field(name,id0,title,extra=''):
    return f'''          <items xsi:type="form:FormField">
            <name>{name}</name>
            <id>{id0}</id>
{L('title',title,'            ')}            <visible>true</visible>
            <enabled>true</enabled>
            <userVisible>
              <common>true</common>
            </userVisible>
            <dataPath xsi:type="form:DataPath">
              <segments>{name}</segments>
            </dataPath>
            <titleLocation>Top</titleLocation>
            <handlers>
              <event>OnChange</event>
              <name>ОтборПриИзменении</name>
            </handlers>
            <extendedTooltip>
              <name>{name}РасширеннаяПодсказка</name>
              <id>{id0+1}</id>
              <type>Label</type>
              <autoMaxWidth>true</autoMaxWidth>
              <autoMaxHeight>true</autoMaxHeight>
              <extInfo xsi:type="form:LabelDecorationExtInfo">
                <horizontalAlign>Left</horizontalAlign>
              </extInfo>
            </extendedTooltip>
            <contextMenu>
              <name>{name}КонтекстноеМеню</name>
              <id>{id0+2}</id>
              <autoFill>true</autoFill>
            </contextMenu>
            <type>InputField</type>
            <editMode>Enter</editMode>
            <showInHeader>true</showInHeader>
            <headerHorizontalAlign>Left</headerHorizontalAlign>
            <showInFooter>true</showInFooter>
            <extInfo xsi:type="form:InputFieldExtInfo">
              <autoMaxWidth>true</autoMaxWidth>
              <autoMaxHeight>true</autoMaxHeight>
              <clearButton>true</clearButton>
{extra}              <textEdit>true</textEdit>
              <textSize>Normal</textSize>
            </extInfo>
          </items>
'''
newf=field('ОтборСтадия',551,('Стадия','Étape','Stage','Etapa'))+field('ОтборПериодОтгрузки',554,('Дата отгрузки',"Date d'expédition",'Shipment date','Fecha de envío'))
s=s[:b]+newf+s[b:]

# clearButton for client/product
for nm in ['ОтборКлиент','ОтборПродукция']:
    a=s.index(f'          <items xsi:type="form:FormField">\n            <name>{nm}</name>')
    b=s.index('\n          </items>\n',a)
    blk=s[a:b]
    old='              <autoMaxHeight>true</autoMaxHeight>\n              <textEdit>true</textEdit>'
    assert old in blk,nm
    blk=blk.replace(old,'              <autoMaxHeight>true</autoMaxHeight>\n              <clearButton>true</clearButton>\n              <textEdit>true</textEdit>')
    s=s[:a]+blk+s[b:]

# --- 5. pager group from list form
src=open(ЭТАЛОН_ПАГИНАТОРА,encoding='utf-8').read()
ga=src.rindex('<items xsi:type="form:FormGroup">',0,src.index('<name>ГруппаПагинация</name>'))
gb=src.index('                </items>',src.index('<name>НадписьЗаписей</name>'))
gb=src.index('                </items>\n',src.index('<type>UsualGroup</type>',gb-2000))+len('                </items>\n')
grp=src[ga:gb]
assert grp.count('<name>ГруппаПагинация</name>')==1 and 'Список' not in grp
# legend decoration inserted before group's <type>UsualGroup</type>
dec_a=grp.index('                  <items xsi:type="form:Decoration">\n                    <name>НадписьЗаписей</name>')
dec_b=grp.index('                  </items>\n',dec_a)+len('                  </items>\n')
leg=grp[dec_a:dec_b].replace('НадписьЗаписей','НадписьЛегенда')
leg=re.sub(r'(<name>НадписьЛегенда</name>\n\s*<id>\d+</id>\n)(?:\s*<title>\n.*?</title>\n)+',lambda m:m.group(1),leg,flags=re.S)
leg=leg.replace('                    <autoMaxWidth>true</autoMaxWidth>\n                    <autoMaxHeight>true</autoMaxHeight>\n                    <skipOnInput>',
                '                    <autoMaxWidth>true</autoMaxWidth>\n                    <autoMaxHeight>true</autoMaxHeight>\n                    <horizontalStretch>true</horizontalStretch>\n                    <skipOnInput>',1)
assert '<horizontalStretch>true' in leg
leg=leg.replace('<horizontalAlign>Left</horizontalAlign>\n                    </extInfo>','<horizontalAlign>Right</horizontalAlign>\n                    </extInfo>')
grp=grp[:dec_b]+leg+grp[dec_b:]
# remap ids sequentially from 557
nid=[557]
def nxt(m):
    v=nid[0]; nid[0]+=1
    return f'<id>{v}</id>'
grp=re.sub(r'<id>\d+</id>',nxt,grp)
# reindent to page level (10 spaces for items of page) — keep relative lines; EDT ignores whitespace
grp='          '+grp.rstrip('\n')+'\n'
pa=s.index('<name>СтраницаЗаказы</name>')
pb=s.index('          <type>Page</type>',pa)
s=s[:pb]+grp+s[pb:]

# --- viewStatusLocation on Заказы table
ta=s.index('<items xsi:type="form:Table">\n            <name>Заказы</name>')
tb=s.index('            <autoMaxCardHeight>true</autoMaxCardHeight>',ta)
assert s[ta:tb].count('<items xsi:type="form:Table">')==1
s=s[:tb]+'            <viewStatusLocation>None</viewStatusLocation>\n'+s[tb:]

# --- 6. commands
cmds=''
for i,nm in enumerate(['СтраницаПервая','СтраницаНазад','СтраницаВперед','СтраницаПоследняя']):
    ca=src.index(f'  <formCommands>\n    <name>{nm}</name>')
    cb=src.index('  </formCommands>\n',ca)+len('  </formCommands>\n')
    c=src[ca:cb]
    c=re.sub(r'\n    <id>\d+</id>\n',f'\n    <id>{39+i}</id>\n',c,count=1)
    cmds+=c
last=s.rindex('  </formCommands>\n')+len('  </formCommands>\n')
s=s[:last]+cmds+s[last:]

# Заказ без даты отгрузки в отбор по периоду не попадает (гейт плана 2026-10-05).
rep("""			ИЛИ Заказы.ДатаОтгрузки &lt;= &amp;КонецОтгрузки)</queryText>""", """			ИЛИ Заказы.ДатаОтгрузки &lt;= &amp;КонецОтгрузки
				И Заказы.ДатаОтгрузки &gt; ДАТАВРЕМЯ(1, 1, 1))</queryText>""")
