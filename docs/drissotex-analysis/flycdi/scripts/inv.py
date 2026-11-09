# Инвентаризация: объекты, реквизиты, ТЧ, значения перечислений, формы, макеты, команды, методы BSL.
import os, re, sys, json
import xml.etree.ElementTree as ET
KX={'Attribute':'attr','TabularSection':'ts','EnumValue':'enum','Dimension':'dim','Resource':'res','Form':'form',
    'Template':'tpl','Command':'cmd','AddressingAttribute':'attr','Column':'col','AccountingFlag':'attr','ExtDimensionAccountingFlag':'attr'}
KE={'attributes':'attr','tabularSections':'ts','enumValues':'enum','dimensions':'dim','resources':'res','forms':'form',
    'templates':'tpl','commands':'cmd','addressingAttributes':'attr','columns':'col','accountingFlags':'attr','extDimensionAccountingFlags':'attr'}
def ln(t): return t.split('}')[-1]
def xml_obj(path, key, out):
    root=ET.parse(path).getroot()
    obj=[c for c in root][0]
    def walk(el, pref):
        co=None
        for c in el:
            if ln(c.tag)=='ChildObjects': co=c
        if co is None: return
        for c in co:
            t=ln(c.tag)
            if t in KX:
                if t in ('Form','Template','Command') and c.text and c.text.strip() and len(c)==0:
                    out.add(f"{pref}/{KX[t]}.{c.text.strip()}"); continue
                nm=None
                for p in c:
                    if ln(p.tag)=='Properties':
                        for q in p:
                            if ln(q.tag)=='Name': nm=q.text
                if nm:
                    k=f"{pref}/{KX[t]}.{nm}"; out.add(k); walk(c,k)
            elif len(c)==0 and c.text and t not in ('Language',):
                pass
    walk(obj,key)
def edt_obj(path, key, out):
    root=ET.parse(path).getroot()
    def walk(el,pref):
        for c in el:
            t=ln(c.tag)
            if t in KE:
                if len(c)==0 and c.text:  # e.g. <forms>Name</forms>? 
                    out.add(f"{pref}/{KE[t]}.{c.text.strip().split('.')[-1]}"); continue
                nm=None
                for q in c:
                    if ln(q.tag)=='name': nm=q.text
                if nm:
                    k=f"{pref}/{KE[t]}.{nm}"; out.add(k); walk(c,k)
    walk(root,key)
MRE=re.compile(r'^\s*(?:&\S+\s*)*?(?:Асинх\s+)?(Процедура|Функция)\s+([\wА-Яа-яЁё]+)\s*\((.*?)\)(\s+Экспорт)?',re.M|re.I)
def methods(text):
    res={}
    lines=text.splitlines()
    cur=None; buf=[]
    for l in lines:
        m=re.match(r'^\s*(?:Асинх\s+)?(Процедура|Функция)\s+([\wА-Яа-яЁё]+)\s*\(',l,re.I)
        if m and cur is None:
            cur=m.group(2); buf=[l]; continue
        if cur is not None:
            buf.append(l)
            if re.match(r'^\s*Конец(Процедуры|Функции)\b',l,re.I):
                res[cur]='\n'.join(buf); cur=None
    return res
def normbody(b):
    b=re.sub(r'//.*','',b)
    b=re.sub(r"НСтр\(\"(.*?)\"\)", lambda m: 'НСтр("'+';'.join(p for p in m.group(1).split(';') if p.strip().startswith('ru'))+'")', b, flags=re.S)
    return re.sub(r'\s+',' ',b).strip().lower()
def scan(root, fmt):
    objs=set(); meth={}
    for dp,_,fs in os.walk(root):
        for f in fs:
            p=os.path.join(dp,f); r=os.path.relpath(p,root)
            parts=r.split(os.sep)
            if fmt=='xml':
                if len(parts)==2 and f.endswith('.xml') and parts[0] not in ('Ext','Languages'):
                    key=f"{parts[0]}/{f[:-4]}"; objs.add(key); xml_obj(p,key,objs)
                if f.endswith('.bsl'):
                    q=[x for x in parts if x not in ('Ext',)]
                    if 'Form' in q: q.remove('Form')
                    if parts[0]=='Ext': q=['Configuration']+q
                    mk='/'.join(q)
            else:
                if f.endswith('.mdo') and len(parts)==3:
                    key=f"{parts[0]}/{parts[1]}"; objs.add(key); edt_obj(p,key,objs)
                if f.endswith('.bsl'):
                    mk='/'.join(parts)
            if f.endswith('.bsl'):
                t=open(p,encoding='utf-8-sig',errors='replace').read()
                for n,b in methods(t).items(): meth[mk+'::'+n]=normbody(b)
    return objs, meth
root,fmt,out=sys.argv[1:4]
o,m=scan(root,fmt)
import unicodedata as U
N=lambda s:U.normalize('NFC',s)
json.dump({'objs':sorted(N(x) for x in o),'meth':{N(k):N(v) for k,v in m.items()}},open(out,'w'),ensure_ascii=False)
print(out,len(o),len(m))
