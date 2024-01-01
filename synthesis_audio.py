import re,jieba,os,wave
from pypinyin import pinyin, lazy_pinyin, Style
from pydub import AudioSegment
import numpy as np

def overlay(l1,l2):
    ll1=len(l1)
    ll2=len(l2)
    po=int(0.4*44100)
    l3=l1[-po:]
    l4=l2[:po]
    l5=[]
    for a in range(len(l3)):
        l5.append(int(0.5*(l3[a]+l4[a])))
    l6=l1[:-po]+l5+l2[po:]
    return l6

def waveread(pa):
    w=wave.open(pa,'r')
    d=w.readframes(w.getnframes())
    w.close()
    return list(np.frombuffer(d,dtype=np.int16))

def wavesave(pa,da):
    nd=np.array(da,dtype=np.int16)
    f=wave.open(pa,'w')
    f.setnchannels(2)
    f.setsampwidth(2)
    f.setframerate(44100)
    f.writeframes(nd.tobytes())
    f.close()

f=open('1.txt','r');t=f.read();f.close()
l=re.findall('[\\u4e00-\\u9fa5]+',t)
l=[jieba.lcut(a)for a in l]
sl=[]
for a in l:
    for b in a:
        sl.append(b)
psl=[]
for a in sl:
    psl.append(lazy_pinyin(a,style=Style.TONE3,neutral_tone_with_five=True))
#psl=[[b for b in a]for a in psl]

nnsl=l.copy()
nnsl=[[lazy_pinyin(b,style=Style.TONE3,neutral_tone_with_five=True)for b in a]for a in nnsl]
#nnsl=[[[c for c in b]for b in a]for a in nnsl]
nnsl=[['%s.wav'%''.join(b)for b in a]for a in nnsl]

f=open('durinf.dict','r');kd=eval(f.read());f.close()
dt=0.1
nkd={}
for a in range(len(sl)):
    tt=0
    lsl=len(sl[a])
    pp=[]
    for b in range(lsl):
        pp.append(tt)
        tt+=kd['%s.wav'%psl[a][b]]-(0 if b==0 else dt if b==lsl-1 else 2*dt)
    print(tt)
    fn=''
    for b in range(lsl):
        fn='%s%s'%(fn,psl[a][b])
    fn='%s.wav'%fn
    nkd[fn]=tt
    if not os.path.exists('syn1'):os.mkdir('syn1')
    if not os.path.exists(pa:='syn1/%s'%fn):
        ss=[waveread('RESULT_VOICE_SOURCE/%s.wav'%psl[a][b])for b in range(lsl)]
        s=ss[0]
        for b in range(len(ss)-1):
            s=overlay(s,ss[b+1])
            #silence=silence.overlay(ss[b],position=0)
        wavesave(pa,s)
        del ss
f=open('nkd.dict','w+');f.write(repr(nkd));f.close()

print('=====')
f=open('nkd.dict','r');nkd=eval(f.read());f.close()
dt=0.1
skd={}
sl=nnsl
psl=[[b[:-4]for b in a]for a in sl]
print(psl)
for a in range(len(sl)):
    tt=0
    lsl=len(sl[a])
    pp=[]
    for b in sl[a]:
        pp.append(tt)
        tt+=nkd[b]-(0 if b==0 else dt if b==lsl-1 else 2*dt)
        print(tt)
    fn='%s.wav'%(str(a).rjust(6).replace(' ','0'))
    skd[fn]=tt
    if not os.path.exists('syn2'):os.mkdir('syn2')
    if not os.path.exists(pa:='syn2/%s'%fn):
        ss=['syn1/%s'%sl[a][b]for b in range(len(sl[a]))]
        ss=[waveread('syn1/%s'%sl[a][b])for b in range(len(sl[a]))]
        s=ss[0]
        for b in range(len(ss)-1):
            s=overlay(s,ss[b+1])
        wavesave(pa,s)
        del ss
f=open('skd.dict','w+');f.write(repr(skd));f.close()

print('=====')
f=open('skd.dict','r');skd=eval(f.read());f.close()
dt=0.5
sl=[]
for a in os.walk('syn2'):
    a[2].sort()
    for b in a[2]:
        sl.append(b)
tt=0
lsl=len(sl)
pp=[]
for a in sl:
    pp.append(tt)
    tt+=skd[a]#+(0 if b==0 else dt)
    print(tt)
fn='result.wav'
ss=['syn2/%s'%sl[a]for a in range(lsl)]
ss=[waveread('syn2/%s'%sl[a])for a in range(lsl)]
s=ss[0]
slience=[0 for a in range(int(44100*0.5))]
for b in range(len(ss)-1):
    s=s+slience+ss[b+1]
wavesave(fn,s)
del ss

print(sl)
