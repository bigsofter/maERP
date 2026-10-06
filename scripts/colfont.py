#!/usr/bin/env python3
"""Шрифт шапки колонок таблиц: у каждой колонки Form.form явный titleFont.

Интерфейс 8.5 на macOS рисует шапку колонки без явного titleFont своим шрифтом
с разрядкой кириллицы, и ни стиль конфигурации, ни шрифт таблицы на неё не действуют
(проба 2026-10-06, сборка 2.0.16.21; правило tiny1C forms-022). Явный titleFont -
ссылка на Style.NormalTextFont без полужирного - шапку чинит.

Использование:
  scripts/colfont.py         проверка: список колонок без titleFont, код 1, если есть
  scripts/colfont.py --fix   проставить titleFont всем таким колонкам
"""
import re, sys, glob, os
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src', 'cf', 'src')
WRITE = '--fix' in sys.argv
FONT=['<titleFont xsi:type="core:FontRef">','  <font>Style.NormalTextFont</font>','  <bold>false</bold>','  <italic>false</italic>',
      '  <underline>false</underline>','  <strikeout>false</strikeout>','  <scale>100</scale>','</titleFont>']
open_re=re.compile(r'^(\s*)<items xsi:type="form:(\w+)">\s*$')
total=0; files=0; already=0; missing=[]
for path in glob.glob(ROOT+'/**/Form.form',recursive=True):
    lines=open(path,encoding='utf-8').read().split('\n')
    stack=[]  # (indent,type,start_line)
    cols=[]
    for i,l in enumerate(lines):
        m=open_re.match(l)
        if m:
            stack.append((len(m.group(1)),m.group(2),i)); continue
        m=re.match(r'^(\s*)</items>\s*$',l)
        if m and stack and stack[-1][0]==len(m.group(1)):
            ind,typ,st=stack.pop()
            if typ=='FormField':
                # ancestors
                col=False
                for a in reversed(stack):
                    if a[1]=='FormGroup': continue
                    col = a[1]=='Table'; break
                if col: cols.append((st,ind))
    if not cols: continue
    ins=[]
    for st,ind in cols:
        # own direct children are at ind+2
        ci=' '*(ind+2)
        j=st+1
        assert lines[j].startswith(ci+'<name>'),(path,lines[j])
        j+=1
        assert lines[j].startswith(ci+'<id>'),(path,lines[j])
        pos=j+1
        while lines[pos].strip()=='<title>':
            while lines[pos].strip()!='</title>':
                pos+=1
            pos+=1
        k=pos
        has=False
        while k<len(lines) and not lines[k].startswith(ci+'<visible>') and not lines[k].startswith(ci+'<enabled>') and not lines[k].startswith(ci+'<dataPath'):
            if lines[k].startswith(ci+'<titleFont'): has=True
            if lines[k].startswith(' '*ind+'</items>'): break
            k+=1
        if lines[pos].startswith(ci+'<titleFont') or lines[pos].startswith(ci+'<titleTextColor'): has=True
        if has: already+=1; continue
        ins.append((pos,ci))
    if not ins: continue
    files+=1; total+=len(ins)
    missing.extend(os.path.relpath(path,ROOT)+' :'+str(p+1) for p,_ in ins)
    if WRITE:
        for pos,ci in sorted(ins,reverse=True):
            lines[pos:pos]=[ci+x for x in FONT]
        open(path,'w',encoding='utf-8').write('\n'.join(lines))
if WRITE:
    print(f'Шрифт шапки проставлен: колонок {total} в формах {files}')
else:
    for p in missing: print('нет titleFont:', p)
    print(f'Колонки без шрифта шапки: {total} (в формах {files}); с titleFont: {already}')
    sys.exit(1 if total else 0)
