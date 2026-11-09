import json,sys
L=lambda n: json.load(open(f'{sys.argv[1]}/{n}.json'))
F,D,R,M=L('F'),L('D'),L('R'),L('M')
fo,do,ro,mo=[set(x['objs']) for x in (F,D,R,M)]
miss=sorted(fo-mo)
# collapse children of missing parents
top=[k for k in miss if not any(k.startswith(p+'/') for p in miss if p!=k)]
for k in top:
    src='D' if k in do else ('R' if k in ro else 'F-only')
    print(f"{src:6} {k}")
