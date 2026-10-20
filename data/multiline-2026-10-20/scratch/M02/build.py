import json, sys
H='/home/user/news-desk/data/multiline-2026-10-20'
I=json.load(open(f'{H}/in/M02.json')); order=[x['id'] for x in I]
TAIL={'title':' (제목 기준)','channel':' (채널 전언)'}; basis={x['id']:x['basis'] for x in I}
docs={}; cur=None
for f in sys.argv[1:]:
    for ln in open(f, encoding='utf-8'):
        ln=ln.rstrip('\n').strip()
        if not ln: continue
        if ln.startswith('@'): cur=ln[1:].strip(); docs[cur]=[]
        else: docs[cur].append(ln.rstrip('.'))
out=[]
for i in order:
    if i in docs:
        s='\n'.join(docs[i]); t=TAIL.get(basis[i],'')
        if t and not s.endswith(t): s+=t
        out.append({'id':i,'one':s})
json.dump(out, open(f'{H}/out/M02.json','w'), ensure_ascii=False, indent=1)
for o in out:
    for k,l in enumerate(o['one'].split('\n')): 
        if not (25<=len(l)<=90 or (k==0 and 40<=len(l)<=90)) or (k==0 and len(l)<40): print(o['id'],k,len(l))
print('saved',len(out))
