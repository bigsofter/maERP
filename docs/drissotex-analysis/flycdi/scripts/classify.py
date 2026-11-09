import os, re, sys, json
def norm(b, path):
    try: t=b.decode('utf-8-sig')
    except: return b
    # keep only ru in v8:item blocks
    t=re.sub(r'<v8:item>\s*<v8:lang>(?!ru<)[^<]*</v8:lang>\s*<v8:content>.*?</v8:content>\s*</v8:item>\s*','',t,flags=re.S)
    if path.endswith('.bsl'):
        t=re.sub(r"НСтр\(\"(.*?)\"\)", lambda m: 'НСтр("'+ ';'.join(p for p in m.group(1).split(';') if p.strip().startswith('ru')) +'")', t, flags=re.S)
        t='\n'.join(l.rstrip() for l in t.splitlines() if l.strip())
    t=t.replace('Cmd+','Ctrl+')
    t=re.sub(r'\s+',' ',t)
    return t
def idx(root):
    d={}
    for dp,_,fs in os.walk(root):
        for f in fs:
            p=os.path.join(dp,f); r=os.path.relpath(p,root)
            if r.startswith('ConfigDumpInfo'): continue
            d[r]=p
    return d
F,D,R=idx('flycdi/cf'),idx('drissotex'),idx('rayssouni')
cache={}
def n(p):
    if p not in cache: cache[p]=norm(open(p,'rb').read(),p)
    return cache[p]
res={'newF':[], 'eqD':0,'eqR_only':[],'uniq':[],'missingF_vsD':[]}
for k,p in sorted(F.items()):
    if k not in D and k not in R: res['newF'].append(k); continue
    if k in D and n(p)==n(D[k]): res['eqD']+=1; continue
    if k in R and n(p)==n(R[k]): res['eqR_only'].append(k); continue
    res['uniq'].append(k)
res['missingF_vsD']=sorted(set(D)-set(F))
json.dump(res,open(sys.argv[1],'w'),ensure_ascii=False,indent=1)
print('eqD',res['eqD'],'eqR_only',len(res['eqR_only']),'uniq',len(res['uniq']),'newF',len(res['newF']),'missing_vs_D',len(res['missingF_vsD']))
