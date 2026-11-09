"""Фрагмент редакции 9 (см. gen9.py): исполняется exec с глобальными s (текст формы) и re; результат - в s."""
# Закладка «Материалы»: ширины, короткие заголовки с подсказкой, «Способ изготовления» в конец.
start=s.index('              <name>Материалы</name>')
# table block start line
tstart=s.rindex('<items xsi:type="form:Table">',0,start)
tend=s.index('              <representation>Tree</representation>',start)
region=s[tstart:tend]
ind='              <items xsi:type="form:FormField">\n'
first=region.index(ind)
head=region[:first]
cols_text=region[first:]
blocks=[]
pos=0
while pos<len(cols_text):
    assert cols_text.startswith(ind,pos),cols_text[pos:pos+200]
    e=cols_text.index('\n              </items>\n',pos)+len('\n              </items>\n')
    blocks.append(cols_text[pos:e]); pos=e
names=[re.search(r'<name>(\w+)</name>',b).group(1) for b in blocks]
spec={
 'МатериалыМатериал':(None,20),
 'МатериалыПродукция':(None,16),
 'МатериалыХарактеристика':(('Характ.','Caract.','Charact.','Caract.'),10),
 'МатериалыПоСоставу':(('Состав','Compo.','BOM','Compos.'),9),
 'МатериалыПотребность':(('Нужно','Besoin','Need','Necesid.'),9),
 'МатериалыЗаказано':(None,9),
 'МатериалыПришло':(None,9),
 'МатериалыИзОстатка':(('Со склада','Du stock','From stock','De stock'),9),
 'МатериалыДефицит':(None,9),
 'МатериалыКПоступлению':(('Ожидается','Attendu','Expected','Esperado'),9),
 'МатериалыСпособИзготовления':(('Способ','Mode','Method','Método'),12),
}
langs=['ru','fr','en','es']
out=[]
for b,n in zip(blocks,names):
    short,w=spec[n]
    titles=re.findall(r'                <title>\n                  <key>(\w+)</key>\n                  <value>([^<]*)</value>\n                </title>\n',b)
    tdict=dict(titles)
    assert set(tdict)==set(langs),(n,tdict)
    if short:
        tt=''.join(f'                <title>\n                  <key>{l}</key>\n                  <value>{v}</value>\n                </title>\n' for l,v in zip(langs,short))
        tips=''.join(f'                <toolTip>\n                  <key>{l}</key>\n                  <value>{tdict[l]}</value>\n                </toolTip>\n' for l in langs)
        assert '<toolTip>' not in b,n
        b=re.sub(r'(                <title>\n(?:.*\n)*?                </title>\n)+',lambda m: tt+tips,b,count=1)
    old='                <extInfo xsi:type="form:LabelFieldExtInfo">\n                  <autoMaxWidth>true</autoMaxWidth>\n'
    assert old in b,n
    b=b.replace(old,f'                <extInfo xsi:type="form:LabelFieldExtInfo">\n                  <width>{w}</width>\n                  <autoMaxWidth>false</autoMaxWidth>\n')
    out.append((n,b))
order=[x for x in out if x[0]!='МатериалыСпособИзготовления']+[x for x in out if x[0]=='МатериалыСпособИзготовления']
new=head+''.join(b for _,b in order)
s=s[:tstart]+new+s[tend:]
