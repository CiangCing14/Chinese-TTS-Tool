import os,wave,math
import numpy as np
if not os.path.exists(pa:='RESULT_VOICE_SOURCE_2'):os.mkdir(pa)
for a in os.walk('RESULT_VOICE_SOURCE_1'):
    for b in a[2]:
        if'5'in b:
            if not os.path.exists('%s/%s'%(pa,b)):
                w=wave.open('%s/%s'%(a[0],b),'r')
                fr=w.getframerate()
                d=w.readframes(w.getnframes())
                w.close()
                d=list(np.frombuffer(d,dtype=np.int16))
                nd=[]
                for c in d:
                    nd.append(int(c/2))
                nd=np.array(nd,dtype=np.int16)
                f=wave.open('%s/%s'%(pa,b),'w')
                f.setnchannels(2)
                f.setsampwidth(2)
                f.setframerate(fr)
                f.writeframes(nd.tobytes())
