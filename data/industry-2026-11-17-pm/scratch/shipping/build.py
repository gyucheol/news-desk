import json
B='/home/user/news-desk'
p=json.load(open(f'{B}/work/nightly-2026-11-17/chains/shipping.json'))
ids=[json.loads(l)['id'] for l in open(f'{B}/data/industry-2026-11-17-pm/news/shipping.jsonl')]
def S(d,o,u,nid,t): return dict(d=d,o=o,u=u,nid=nid,t=t)
H1='https://t.me/Trillion_labs/12100'; H2='https://t.me/Trillion_labs/12136'; H3='https://t.me/Trillion_labs/12159'
Y='https://t.me/Trillion_labs/12167'
BS='https://t.me/The_MariTimes/64651'
state={
 'routes':[S('2026-11-15','텔레그램 트릴리온',H1,'n-tg-0688','이란은 11월 15일 유조선 5척이 불법 항로로 다니다 기뢰에 부딪혔다고 했고, 혁명수비대는 200만 배럴 넘게 실은 초대형 유조선 등 2척이 폭발했다고 주장했지만 독립 확인은 없습니다 [사실]'),
           S('2026-11-15','텔레그램 트릴리온',Y,'n-rtr-0372','사우디 지원 예멘 남부군이 11월 15일 두바브·바브엘만데브 일대에서 아덴 방어를 위해 물러나 재배치하면서, 후티가 해협을 내려다보는 요지를 쥐었습니다 [사실]')],
 'tankers':[S('2026-11-16','텔레그램 트릴리온',H3,'n-tg-0688','UKMTO는 11월 16일 호르무즈 해협을 나서던 유조선이 정체불명 발사체에 맞아 기관실 화재가 났다고 밝혔고, IMO·UKMTO 자료로 60일간 공격 57건 가운데 42건이 유류·제품·화학 운반선이었습니다 [사실]'),
            S('2026-11-15','텔레그램 Polaristimes',BS,'n-tg-0162','흑해에서는 불가리아 앞바다 선박 침몰과 루마니아 수역 화학제품 유조선 2척 화재로 선원 7~8명이 실종됐고, 불가리아·루마니아는 러시아를 배후로 지목했습니다 [사실]')],
}
IS=[
 dict(d='2026-11-16',kind='supply',o='텔레그램 트릴리온',u=H2,nid='n-tg-0688',t='호르무즈 해상 수송량은 10일 새 50% 줄어 전쟁 전 하루 2,050만 배럴을 크게 밑돈다는 전언이고, JMIC는 11월 1일 이후 무산담 앞바다 공격 5건을 집계했습니다 [채널]'),
 dict(d='2026-11-16',kind='supply',o='텔레그램 트릴리온',u=H2,nid='n-tg-0688',t='IMO·UKMTO 자료로 60일간 선박 56척이 57건 공격받았고, 유류·제품·화학 운반선 42건, LNG·LPG선 5건, 기타 9건이었습니다 [채널]'),
 dict(d='2026-11-16',kind='supply',o='텔레그램 트릴리온',u=Y,nid='n-rtr-0372',t='사우디는 호르무즈 차질로 하루 약 400만 배럴을 동서 송유관으로 얀부에 돌리고 있고, 후티는 11월 11~16일 이 송유관 펌프장 공격을 잇달아 주장했습니다 [사실]'),
]
old=p['insight']['b2'][0]
b2=[dict(t='반대라면 항로 차질이 길어지는 경우입니다. 호르무즈 해상 수송량이 11월 10일 새 50% 줄었다는 전언이 있고, 후티가 바브엘만데브를 내려다보는 요지를 쥐었으며, 수에즈 통과 컨테이너 선복은 아직 홍해 위기 전의 절반 남짓이어서 늘어난 배가 우회 거리에 흡수될 수 있습니다 [유추]',
  src=[dict(o='텔레그램 트릴리온',d='2026-11-16',u=H2),dict(o='텔레그램 트릴리온',d='2026-11-16',u=Y)]+old['src'][:1])]
gaps=p['gaps']+' 11월 17일 저녁 업데이트도 검색·열람 없이 입력 뉴스 3건으로만 반영했습니다. 이란이 기뢰 피격을 주장한 유조선 5척의 이름과 피해, 16일 발사체 피격 유조선의 이름, 호르무즈 수송량 50% 감소와 60일 57건 집계(채널 전언)의 원자료, 후티의 동서 송유관 PS5·6 파괴 주장, 흑해 침몰 선박의 선종·이름은 확인하지 못했습니다.'
out=dict(id='shipping',summary='',state=state,industryState=IS,flags=[],insight=dict(b2=b2),cycle=None,nodeStage={},gaps=gaps,
 note='뉴스 3건 반영: 이란의 유조선 5척 기뢰 피격 주장·호르무즈 수송 10일 새 50% 감소 전언, 60일간 공격 57건, 후티 바브엘만데브 요지 장악. 국면 ②(분할) 그대로, 근거 4줄, 수치 3줄, 재검토 신호 0건, 인사이트 b2 고침, 검색 0회',
 applied=ids,searches=0,fetches=0)
json.dump(out,open(f'{B}/data/industry-2026-11-17-pm/out/shipping.json','w'),ensure_ascii=False,indent=1)
