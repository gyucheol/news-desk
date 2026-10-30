# 후보 목록(all.tsv)과 거르기 입력(in/F1~F4.tsv), 기존 뉴스 목록(existing.tsv)을 만든다.
# 빼는 것: seen(newsSeen*), 직전 회차 all.tsv(이미 걸러 버린 것 포함), 텔레그램은 progressV4.telegram.new 이하 id
import json,glob,os,re,sys
R='/home/user/news-desk'; W=f'{R}/data/mix-2026-10-30b'; LIVE=f'{R}/work/live47'
os.makedirs(f'{W}/in',exist_ok=True); os.makedirs(f'{W}/out',exist_ok=True)
seen=set(open(f'{R}/work/seen_urls.txt').read().split())
prev=set()
for pp in ['mix-2026-10-29','mix-2026-10-30']:
    prev|={l.rstrip('\n').split('\t')[-1] for l in open(f'{R}/data/{pp}/all.tsv')}
last=json.load(open(f'{LIVE}/meta/progressV4.json'))['telegram']['new']
rows=[]
def clean(s): return re.sub(r'\s+',' ',s).strip()
for s in ['bbg','rtr']:
    for l in open(f'{R}/work/sm20/{s}.txt'):
        if l.startswith('#'):continue
        p=l.rstrip('\n').split('\t'); u=p[-1]; t=p[1]
        if u in seen or u in prev: continue
        title=p[3] if s=='bbg' and p[3].strip() else re.sub(r'-',' ',u.rstrip('/').rsplit('/',1)[-1])
        rows.append([s,t,clean(title),u])
# 연준 공식 연설·증언·성명(사용자 지시 10월 15일): python3 tools/fedspeech.py <since> --out work/sm20/fed.txt
# 줄: 'YYYY-MM-DD HH:MM'(KST) \t 기관 \t 발언자 성 \t 제목 \t 주소
if os.path.exists(f'{R}/work/sm20/fed.txt'):
    for l in open(f'{R}/work/sm20/fed.txt'):
        p=l.rstrip('\n').split('\t')
        if len(p)<5 or p[4] in seen or p[4] in prev: continue
        rows.append(['fed:'+p[1],p[0][5:16],clean((p[2]+': ' if p[2] else '')+p[3]),p[4]])
for f in glob.glob(f'{R}/work/dump20/*.jsonl'):
    ch=os.path.basename(f)[:-6]
    for l in open(f):
        d=json.loads(l); u=f'https://t.me/{ch}/{d["id"]}'
        if d['id']<=last.get(ch,0) or not d['x'].strip() or u in seen or u in prev: continue
        rows.append(['tg:'+ch,d['t'][5:10]+' '+d['t'][11:16],clean(d['x']),u])
rows.sort(key=lambda r:(r[1],r[3]))
with open(f'{W}/all.tsv','w') as o:
    for i,r in enumerate(rows,1): o.write('\t'.join([str(i)]+r)+'\n')
n=len(rows); k=int(sys.argv[1]) if len(sys.argv)>1 else 4; sz=-(-n//k)
for j in range(k):
    with open(f'{W}/in/F{j+1}.tsv','w') as o:
        for i,r in enumerate(rows[j*sz:(j+1)*sz],j*sz+1):
            o.write('\t'.join([str(i),r[0],r[1],r[2][:260],r[3]])+'\n')
import collections
print(n, collections.Counter(r[0][:2] for r in rows))
