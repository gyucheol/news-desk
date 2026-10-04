import json, glob, re, sys
LBL = re.compile(r'\s*\[(사실|귀납|연역|유추|추측)[^\]]*\]\s*\.?\s*$')
KEY = re.compile(r'^([^:{}\[\]]{1,8}):\s*')
TAGHEAD = re.compile(r'^((?:동인|병목 이동|과열 신호|정책 충격|산업 통합|자본 철수|심리 극단|실물 공급 파괴)(?:\([^)]{1,12}\))?) — ')
DUPHEAD = re.compile(r'^이미 다룬 사건\(.*?\)의 새 내용(?:입니다 — |으로, )')
strip = lambda s: s.replace('{{','').replace('}}','')
JOSA = set('은는이가을를에의와과도로만')
def units(c):
    yield 'headline', c['headline']
    for i,f in enumerate(c['facts']): yield f'fact{i}', f
    for i,t in enumerate(c['tags']): yield f'tag{i}', t['t']
    for i,x in enumerate(c['cycles']): yield f'cyc{i}', x['why']
    yield 'incentive', c['incentive']; yield 'check', c['check']
P=[];W=[];tot=0;hl=0
verbose='-v' in sys.argv
for p in sorted(glob.glob('cards/*.json')):
    c=json.load(open(p)); k=c['key']
    if verbose: print('\n#####',k)
    for name,sraw in units(c):
        s=sraw
        s=LBL.sub('',s)
        if name.startswith('fact'):
            m=KEY.match(s)
            if m: s=s[m.end():]
            m=DUPHEAD.match(strip(s)) 
            if m:
                # head has no marks by rule; cut same plain length
                assert '{{' not in s[:m.end()], (k,name,'머리말에 강조')
                s=s[m.end():]
        if name.startswith('tag'):
            m=TAGHEAD.match(s)
            if m: s=s[m.end():]
            else: P.append(f'{k} {name}: 태그 머리말 없음')
        marks=re.findall(r'\{\{(.+?)\}\}',s)
        plain=strip(s); n=len(plain); h=sum(len(m) for m in marks); tot+=n; hl+=h
        if sraw.count('{{')!=sraw.count('}}') or re.search(r'\{\{[^}]*\{\{',sraw) or re.search(r'\}\}[^{]*\}\}',sraw) or '{{}}' in sraw or re.search(r'(?<!\{)\{(?!\{)|(?<!\})\}(?!\})',sraw): P.append(f'{k} {name}: 괄호 짝')
        for m in marks:
            if m!=m.strip(): P.append(f'{k} {name}: 공백 시작/끝 "{m}"')
            if re.search(r'\[(사실|귀납|연역|유추|추측)',m): P.append(f'{k} {name}: 꼬리표 강조 "{m}"')
            if m.count('(')!=m.count(')'): W.append(f'{k} {name}: 괄호 안 닫힘 "{m}"')
            if len(m)>30: W.append(f'{k} {name}: 덩어리 김({len(m)}) "{m}"')
            if re.match(r'^[,.)·]|[,(]$',m): W.append(f'{k} {name}: 문장부호 시작/끝 "{m}"')
            if len(m)==1 and m in JOSA: W.append(f'{k} {name}: 조사 한 글자 "{m}"')
        # mark immediately followed by more marks without separator
        if re.search(r'\}\}\{\{',sraw): W.append(f'{k} {name}: 강조가 붙어 있음')
        if not marks and n>=10: W.append(f'{k} {name}: 강조 없음')
        elif n>=24 and h/n<0.30: W.append(f'{k} {name}: 강조 적음 {h/n:.0%}')
        elif n>=30 and h/n>0.86: W.append(f'{k} {name}: 강조 많음 {h/n:.0%}')
        if verbose: print(f'[{name} {h/max(1,n):.0%}]', ' / '.join(marks))
print(f'\n강조 비율 {hl/max(1,tot):.0%}  PROBLEMS {len(P)}  WARN {len(W)}')
for x in P: print(' !',x)
for x in W: print(' ~',x)
