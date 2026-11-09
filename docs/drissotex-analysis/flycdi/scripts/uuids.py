import os,re,sys,unicodedata as U
N=lambda s:U.normalize('NFC',s)
def xml(root):
    d={}
    for t in os.listdir(root):
        p=os.path.join(root,t)
        if not os.path.isdir(p) or t in('Ext','Languages'): continue
        for f in os.listdir(p):
            if f.endswith('.xml'):
                s=open(os.path.join(p,f),encoding='utf-8-sig').read(3000)
                m=re.search(r'<\w+ uuid="([^"]+)"',s.split('<MetaDataObject',1)[1])
                if m: d[N(t+'/'+f[:-4])]=m.group(1)
    return d
def edt(root):
    d={}
    for t in os.listdir(root):
        p=os.path.join(root,t)
        if not os.path.isdir(p): continue
        for o in os.listdir(p):
            f=os.path.join(p,o,o+'.mdo')
            if os.path.exists(f):
                m=re.search(r'uuid="([^"]+)"',open(f,encoding='utf-8').read(2000))
                if m: d[N(t+'/'+o)]=m.group(1)
    return d
F=xml(sys.argv[1]); M=edt(sys.argv[2])
same=[k for k in F if k in M and F[k]==M[k]]; diff=[k for k in F if k in M and F[k]!=M[k]]
print('common',len(same)+len(diff),'same uuid',len(same),'diff uuid',len(diff))
for k in diff: print('  DIFF',k)
