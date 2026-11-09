import json,sys,collections
L=lambda n: json.load(open(f'{sys.argv[1]}/{n}.json'))['meth']
F,D,R,M=L('F'),L('D'),L('R'),L('M')
# M names by method name regardless of module (methods could move between modules)
mnames=collections.defaultdict(set)
for k in M: mnames[k.split('::')[1]].add(k)
new=[];chg=[]
for k,b in F.items():
    if k in D and D[k]==b: continue
    if k in R and R[k]==b: continue
    if k in M and M[k]==b: continue
    if k not in D and k not in R: new.append(k)
    else: chg.append(k)
def grp(l):
    c=collections.defaultdict(list)
    for k in l: c[k.split('::')[0]].append(k.split('::')[1])
    return c
print('NEW methods (absent in D and R):',len(new))
for m,ns in sorted(grp(new).items()):
    inM=[n for n in ns if f'{m}::{n}' in M]
    print(f"  {m}: {len(ns)} (in M same module: {len(inM)}) :: {', '.join(sorted(set(ns)-set(inM)))[:400]}")
print('CHANGED vs D and R:',len(chg))
for m,ns in sorted(grp(chg).items()):
    print(f"  {m}: {', '.join(ns)[:300]}")
json.dump({'new':new,'chg':chg},open(f'{sys.argv[1]}/meth.json','w'),ensure_ascii=False)
