# 검사를 통과한 결과로 문서별 update 파일(바뀐 필드만)과 batch 목록을 만듭니다.
import json,os
M=json.load(open('hl/map.json'));C=json.load(open('hl/checked.json'));V=json.load(open('hl/versions.json'))
out={int(k):v for k,v in C['out'].items()};bad=set(C['bad']);assert not bad
docs={}
for k,u in enumerate(M):
    d=docs.setdefault(u['doc'],json.load(open(f'db/news/{u["doc"]}.json')))
    o=d;p=u['path']
    for s in p[:-1]: o=o[s]
    assert o[p[-1]].replace('{{','').replace('}}','')==u['text']
    o[p[-1]]=out[k]
os.makedirs('hl2/upd',exist_ok=True);W=[]
for i,d in docs.items():
    o=json.load(open(f'db/news/{i}.json'));up={}
    for f in ('title','one','added','items','detail','insight2'):
        if f in d and d[f]!=o.get(f): up[f]=d[f]
    # 강조 기호를 빼면 원래 문서와 같아야 함
    for f in up: assert json.dumps(up[f],ensure_ascii=False).replace('{{','').replace('}}','')==json.dumps(o[f],ensure_ascii=False).replace('{{','').replace('}}',''),(i,f)
    if not up: continue
    json.dump(up,open(f'hl2/upd/{i}.json','w'),ensure_ascii=False)
    W.append({'op':'update','collection':'news','doc_id':i,'file_path':os.path.abspath(f'hl2/upd/{i}.json'),'if_version':V[i]})
B=[W[j:j+50] for j in range(0,len(W),50)]
for j,b in enumerate(B): json.dump(b,open(f'hl2/batch{j:02d}.json','w'),ensure_ascii=False)
print('docs',len(W),'batches',len(B),'max bytes',max(os.path.getsize(w['file_path']) for w in W),'batch bytes',[sum(os.path.getsize(w['file_path']) for w in b) for b in B])
