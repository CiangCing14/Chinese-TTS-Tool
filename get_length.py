import wave,os
d={}
for a in os.walk('RESULT_VOICE_SOURCE'):
    for b in a[2]:
        f=wave.open('%s/%s'%(a[0],b))
        d[b]=f.getnframes()/f.getframerate()
        f.close()
f=open('durinf.dict','w+');f.write(repr(d));f.close()
