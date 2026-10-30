import json,sys
p=sys.argv[1]; d=json.load(open(p))
R=[("C076","title","{{니덱 주가 10년 만의 최저}}","{{니덱}} 주가 {{10년 만의 최저}}"),
("C053","added","{{초과 면제분 약 7억 7,000만 RIN}}","초과 면제분 {{약 7억 7,000만 RIN}}"),
("C053","added","{{두 안}}","두 안"),
("C053","s1","{{연료비 상승}}을","연료비 상승을"),
("C032","s1","{{우크라이나 항구를 오가는 상선}}","우크라이나 항구를 오가는 {{상선}}"),
("C092","title","{{1.54% 상승}}","{{1.54%}} 상승"),
("C009","s5","{{CXMT 등 중국 국가 지원 업체의 D램 증설}}","CXMT 등 {{중국 국가 지원 업체}}의 {{D램 증설}}")]
for cid,f,a,b in R:
    x=[y for y in d['items'] if y['cid']==cid][0]
    if f.startswith('s'):
        o=x['items'][int(f[1:])]; assert a in o['s'],(cid,a); o['s']=o['s'].replace(a,b)
    else:
        assert a in x[f],(cid,a); x[f]=x[f].replace(a,b)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
