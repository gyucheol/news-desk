import json,re,sys,glob,os,copy
M=json.load(open('hl/map.json'))
strip=lambda s:s.replace('{{','').replace('}}','')
out={};P=[];W=[]
for f in sorted(glob.glob('hl/out/b[0-9][0-9].txt')):
    bi=int(f[-6:-4]);a=open(f'hl/in/b{bi:02d}.txt').read().split('\n');b=open(f).read().split('\n')
    if len(a)!=len(b): P.append(f'b{bi:02d} 줄 수 {len(a)}≠{len(b)}');continue
    for i,(x,y) in enumerate(zip(a,b)):
        if x.startswith('@@'):
            if x!=y: P.append(f'b{bi:02d} 이름표 줄 {i+1} 바뀜')
            k=int(x.split()[1]);out[k]=b[i+1]
TOT=HL=0;bad=set()
for k,u in enumerate(M):
    y=out.get(k)
    if y is None: bad.add(k);continue
    e=[]
    if strip(y)!=u['text']: e.append('글자 바뀜')
    if y.count('{{')!=y.count('}}') or re.search(r'\{\{[^}]*\{\{',y) or '{{}}' in y: e.append('괄호')
    ms=re.findall(r'\{\{(.+?)\}\}',y)
    for m in ms:
        if m!=m.strip(): e.append(f'공백 "{m}"')
        if re.search(r'\{[fpaiu]:|\]\(|https?:|\(제목 기준\)|\(채널 전언\)',m) or m.count('{')!=m.count('}') or m.count('[')!=m.count(']'): e.append(f'꼬리표·링크 "{m}"')
    # 링크·꼬리표 내부에 강조 기호가 끼었는지
    if re.search(r'\[[^\]]*\{\{[^\]]*\]\(|\]\([^)]*\{\{',y): e.append('링크 안 강조')
    if e: bad.add(k);P.append(f'#{k} {u["doc"]} {e[:2]}')
    n=len(u['text']);h=sum(map(len,ms));TOT+=n;HL+=h
    if not ms and n>=10: W.append(f'#{k} 강조 없음')
    elif n>=24 and h/n<.30: W.append(f'#{k} 적음 {h/n:.0%}')
    elif n>=30 and h/n>.86: W.append(f'#{k} 많음 {h/n:.0%}')
print(f'units {len(M)} got {len(out)} ratio {HL/max(TOT,1):.0%} PROBLEMS {len(P)} WARN {len(W)} bad {len(bad)}')
for x in P[:30]: print(' !',x)
for x in W[:15]: print(' ~',x)
json.dump({'out':out,'bad':sorted(bad),'warn':W},open('hl/checked.json','w'),ensure_ascii=False)
