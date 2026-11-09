import os,re,sys,unicodedata as U
import xml.etree.ElementTree as ET
N=lambda s:U.normalize('NFC',s)
ln=lambda t:t.split('}')[-1]
KX={'Attribute':'attr','TabularSection':'ts','Dimension':'dim','Resource':'res','EnumValue':'enum','AddressingAttribute':'attr'}
KE={'attributes':'attr','tabularSections':'ts','dimensions':'dim','resources':'res','enumValues':'enum','addressingAttributes':'attr'}
def xmlc(path):
    out={}
    obj=list(ET.parse(path).getroot())[0]
    def walk(el,pref):
        for c in el:
            if ln(c.tag)=='ChildObjects':
                for x in c:
                    t=ln(x.tag)
                    if t in KX:
                        nm=[q.text for p in x if ln(p.tag)=='Properties' for q in p if ln(q.tag)=='Name'][0]
                        k=f"{pref}{KX[t]}.{nm}"; out[N(k)]=x.get('uuid'); walk(x,k+'/')
    walk(obj,''); return out
def edtc(path):
    out={}
    def walk(el,pref):
        for c in el:
            t=ln(c.tag)
            if t in KE and c.get('uuid'):
                nm=[q.text for q in c if ln(q.tag)=='name'][0]
                k=f"{pref}{KE[t]}.{nm}"; out[N(k)]=c.get('uuid'); walk(c,k+'/')
    walk(ET.parse(path).getroot(),''); return out
F,M=sys.argv[1],sys.argv[2]
tot=bad=0
for t in sorted(os.listdir(F)):
    p=os.path.join(F,t)
    if not os.path.isdir(p) or t in ('Ext','Languages'): continue
    for f in os.listdir(p):
        if not f.endswith('.xml'): continue
        o=f[:-4]; me=os.path.join(M,t,U.normalize('NFC',o),U.normalize('NFC',o)+'.mdo')
        if not os.path.exists(me): continue
        a=xmlc(os.path.join(p,f)); b=edtc(me)
        for k,u in a.items():
            if k in b:
                tot+=1
                if b[k]!=u: bad+=1; print('DIFF',N(t+'/'+o),k)
print('common children',tot,'diff uuid',bad)
