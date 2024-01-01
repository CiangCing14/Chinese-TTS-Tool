import os,shutil
l0=['d','t','n','l','b','p','m','f','zh','ch','sh','r','z','g','c','k','s','h']
l1=['e','ou','ei','en','eng','a','ao','ai','an','ang','u','uo']
ls=[]
for a in l1:
    for b in l0:
        z=None
        if a=='uo':
            if b in['b','p','m','f']:
                z='o'
        for c in range(5):
            ls.append('%s%s%d'%(b,a if not z else z,c+1))
p="/home/a/Music/SPLIT/Comrade AP's Audio Sources 1"
pn=p.split('/')[-1]
if not os.path.exists(pn):os.mkdir(pn)
for a in os.walk(p):
    a[2].sort()
    n=0
    for b in a[2]:
        if not os.path.exists(pa:='%s/%s.wav'%(pn,ls[n])):shutil.copyfile('%s/%s'%(a[0],b),pa)
        n+=1

l0=['d','t','n','l','zh','ch','sh','r','z','g','c','k','s','h']
l1=['ui','un','ong','ua','uai','uan','uang']
ls=[]
for a in l1:
    for b in l0:
        for c in range(5):
            ls.append('%s%s%d'%(b,a,c+1))
p="/home/a/Music/SPLIT/Comrade AP's Audio Sources 2"
pn=p.split('/')[-1]
if not os.path.exists(pn):os.mkdir(pn)
for a in os.walk(p):
    a[2].sort()
    n=0
    for b in a[2]:
        if not os.path.exists(pa:='%s/%s.wav'%(pn,ls[n])):shutil.copyfile('%s/%s'%(a[0],b),pa)
        n+=1

l0=['d','t','n','l','b','p','m','zh','ch','sh','r','z','j','c','q','s','x']
l1=['i']
ls=[]
for a in l1:
    for b in l0:
        for c in range(5):
            ls.append('%s%s%d'%(b,a,c+1))
p="/home/a/Music/SPLIT/Comrade AP's Audio Sources 3"
pn=p.split('/')[-1]
if not os.path.exists(pn):os.mkdir(pn)
for a in os.walk(p):
    a[2].sort()
    n=0
    for b in a[2]:
        if not os.path.exists(pa:='%s/%s.wav'%(pn,ls[n])):shutil.copyfile('%s/%s'%(a[0],b),pa)
        n+=1

l0=['d','t','n','l','b','p','m','j','q','x']
l1=['ie','iu','in','ing','ia','iao','ian','iang']
ls=[]
for a in l1:
    for b in l0:
        for c in range(5):
            ls.append('%s%s%d'%(b,a,c+1))
p="/home/a/Music/SPLIT/Comrade AP's Audio Sources 4"
pn=p.split('/')[-1]
if not os.path.exists(pn):os.mkdir(pn)
for a in os.walk(p):
    a[2].sort()
    n=0
    for b in a[2]:
        if not os.path.exists(pa:='%s/%s.wav'%(pn,ls[n])):shutil.copyfile('%s/%s'%(a[0],b),pa)
        n+=1

l0=['d','t','n','l','j','q','x']
l1=['u','ue','o','un','iong','va','uao','uan','vang']
ls=[]
for a in l1:
    for b in l0:
        z=None
        if a=='u':
            if b=='n':
                z='v'
            if b=='l':
                z='v'
        if a=='ue':
            if b=='n':
                z='ve'
            if b=='l':
                z='ve'
        for c in range(5):
            ls.append('%s%s%d'%(b,a if not z else z,c+1))
p="/home/a/Music/SPLIT/Comrade AP's Audio Sources 5"
pn=p.split('/')[-1]
if not os.path.exists(pn):os.mkdir(pn)
for a in os.walk(p):
    a[2].sort()
    n=0
    for b in a[2]:
        if not os.path.exists(pa:='%s/%s.wav'%(pn,ls[n])):shutil.copyfile('%s/%s'%(a[0],b),pa)
        n+=1

l0=['er','e','ou','ei','en','eng','a','ao','ai','an','ang','wu','wo','wei','wen','weng','wa','wai','wan','wang','yi','ye','you','yin','ying','ya','yao','yan','yang','yu','yue','you','yun','yong','yva','yvao','yuan','yvang']
ls=[]
for a in l0:
    for c in range(5):
        ls.append('%s%d'%(a,c+1))
p="/home/a/Music/SPLIT/Comrade AP's Audio Sources 6"
pn=p.split('/')[-1]
if not os.path.exists(pn):os.mkdir(pn)
for a in os.walk(p):
    a[2].sort()
    n=0
    for b in a[2]:
        if not os.path.exists(pa:='%s/%s.wav'%(pn,ls[n])):
            shutil.copyfile('%s/%s'%(a[0],b),pa)
        n+=1

l0=['n']
ls=[]
for a in l0:
    for c in range(5):
        ls.append('%s%d'%(a,c+1))
p="/home/a/Music/SPLIT/Comrade AP's Audio Sources 7"
pn=p.split('/')[-1]
if not os.path.exists(pn):os.mkdir(pn)
for a in os.walk(p):
    a[2].sort()
    n=0
    for b in a[2]:
        if not os.path.exists(pa:='%s/%s.wav'%(pn,ls[n])):
            shutil.copyfile('%s/%s'%(a[0],b),pa)
        n+=1
