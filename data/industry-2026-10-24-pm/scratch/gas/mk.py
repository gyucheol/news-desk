import json
D='2026-10-23'
U=dict(
 qatar='https://www.reuters.com/business/energy/qatarenergy-talks-with-venture-global-buy-lng-long-term-supply-deal-sources-say-2026-10-22/',
 qatar_tg='https://t.me/Trillion_labs/11171',
 canada_tg='https://t.me/Trillion_labs/11175',
 aus='https://www.bloomberg.com/news/articles/2026-10-23/australia-gas-generation-drops-to-lowest-since-2000-as-batteries-boom',
 welspun='https://www.reuters.com/business/energy/indias-welspun-bags-580-million-us-gas-pipeline-order-tied-data-centre-buildout-2026-10-23/',
 uk='https://www.reuters.com/business/energy/uk-gas-power-grids-ready-winter-despite-global-turmoil-operators-say-2026-10-23/',
 china='https://www.reuters.com/business/energy/china-calls-oil-gas-firms-boost-output-build-strategic-supply-bases-2026-10-23/',
 fin='https://t.me/The_MariTimes/63938',
 ttf='https://t.me/HANAchina/70762',
)
def S(d,o,u,nid,t): return dict(d=d,o=o,u=u,nid=nid,t=t)
state={
 'liquefaction':[
  S('2026-10-22','로이터',U['qatar'],'n-bbg-0646','카타르에너지는 셰니에르와 사빈패스·코퍼스크리스티에서 각 연 200만 톤씩 2031~2054년 23년간 사는 계약을 맺었고, 사빈패스 물량 중 연 100만 톤은 1단계 확장 최종투자결정에 달렸습니다 [사실]'),
  S(D,'텔레그램 트릴리온',U['canada_tg'],'n-bbg-0646','캐나다는 LNG 캐나다 2단계 확장 등으로 2030년 LNG 수출능력을 연 3,300만 톤으로 늘릴 예정이라는 전언입니다 [채널]'),
 ],
 'trade':[
  S('2026-10-22','로이터',U['qatar'],'n-bbg-0646','카타르에너지의 셰니에르 계약은 본선인도 방식에 헨리허브 연동 가격과 고정 수수료를 붙였고, 3월 라스라판 공격 뒤 걸프 밖 공급원을 찾는 카타르는 벤처글로벌과도 장기 구매를 협상 중입니다 [사실]'),
 ],
 'midstream':[
  S(D,'로이터',U['welspun'],'n-rtr-0683','웰스펀 미국 법인은 대형 기술기업 데이터센터 단지에 가스를 보낼 퍼미안 분지 가스관용 강관 약 5.8억 달러 주문을 따내 수주잔고가 약 52.5억 달러로 최대가 됐습니다 [사실]'),
 ],
 'demand':[
  S(D,'블룸버그',U['aus'],'n-bbg-0648','호주 전력시장의 3분기 가스발전은 전년보다 약 3분의 1 줄어 2000년 이후 같은 분기 최저였고, 저녁 4~9시 발전 비중은 배터리 약 8%로 가스 5.1%를 처음 앞섰습니다 [사실]'),
  S(D,'로이터',U['uk'],'n-rtr-0690','영국 내셔널가스는 겨울 최대 가스 수요를 하루 4억 9,300만 m³(2% 증가)로, 공급능력을 5억 9,200만 m³로 봤지만 최대 설비 고장 때 여유는 1,800만 m³로 줄어든다고 했습니다 [사실]'),
 ],
 'upstream':[
  S(D,'로이터',U['china'],'n-rtr-0709','중국 국가에너지국은 석유·가스 기업에 투자·탐사 확대를 주문하며 천연가스 생산은 빠르게 늘리라고 했고, 2030년 국내 석유·가스 공급 하한은 석유환산 4.4억 톤(2025년 4.2억 톤)입니다 [사실]'),
 ],
}
IS=[
 dict(d='2026-10-22',kind='demand',o='로이터',u=U['qatar'],nid='n-bbg-0646',t='카타르에너지는 셰니에르에서 2031~2054년 연 400만 톤(사빈패스·코퍼스크리스티 각 200만 톤)을 사는 23년 계약을 맺었습니다 [사실]'),
 dict(d=D,kind='demand',o='블룸버그',u=U['aus'],nid='n-bbg-0648',t='호주 NEM 3분기 가스발전은 전년보다 약 3분의 1 줄어 2000년 이후 최저였고, 계통 배터리 용량은 1년 새 3배 넘게 늘었으며 재생에너지 비중은 44.3%였습니다 [사실]'),
 dict(d=D,kind='supply',o='로이터',u=U['uk'],nid='n-rtr-0690',t='영국 겨울 가스 공급능력은 하루 5억 9,200만 m³로 최대 수요(4억 9,300만 m³)보다 9,900만 m³ 많고, 이란 전쟁 뒤 영국 근월물 가스값은 약 180% 올랐습니다 [사실]'),
 dict(d=D,kind='capex',o='로이터',u=U['welspun'],nid='n-rtr-0683',t='웰스펀 미국 법인의 데이터센터용 퍼미안 가스관 강관 수주는 약 5.8억 달러로, 2029 회계연도 납품이며 수주잔고는 약 52.5억 달러입니다 [사실]'),
]
flags=[
 dict(nid='n-bbg-0648',t='재검토 필요: 호주 가스발전이 배터리 확산으로 2000년 이후 최저로 줄어든 것은 수요 노드가 ③ 공급 과잉·④ 수익 악화 쪽을 가리키며, 저장 배터리가 피크 가스발전 수요를 직접 대체하기 시작했기 때문입니다 [유추]'),
]
def L(t,*src): return dict(t=t,src=[dict(o=o,d=d,u=u) for o,d,u in src])
insight={
 'a':[
  L('LNG의 무게중심이 카타르에서 북미로 옮겨 가고 있고, 이제는 카타르에너지 자신이 셰니에르에서 23년간 연 400만 톤을 사들이는 구매자가 됐습니다. 걸프 생산자까지 호르무즈 밖 공급원을 사면서 미국산 장기계약이 신규 액화 FID의 담보가 됩니다 [귀납]',
    ('로이터','2026-10-22',U['qatar']),('텔레그램 트릴리온','2026-09-22','https://t.me/Trillion_labs/9268')),
  L('자본 구조도 바뀌었습니다. 대체자산 운용사의 LNG·미드스트림 거래가 올해 203.5억 달러로 2024년 전체의 두 배를 넘었습니다 [사실]',
    ('로이터','2026-09-29','https://www.reuters.com/business/energy/alternative-capital-powers-americas-next-wave-lng-pipeline-projects-2026-09-29/')),
  L('생산국의 국내 물량 붙잡기가 제도화되고 있습니다. 호주가 수출량의 20% 국내 공급을 수출 허가 조건으로 걸고 중국 국가에너지국이 천연가스 증산을 주문해, 아시아행 여유 물량과 수입 수요가 정책으로 바뀔 수 있습니다 [유추]',
    ('블룸버그','2026-10-09','https://www.bloomberg.com/news/articles/2026-10-09/australia-to-release-final-plan-to-keep-more-lng-output-at-home'),('로이터',D,U['china'])),
 ],
 'b2':[
  L('데이터센터 자가발전이 예상보다 빨리 늘면 미국 안 수요가 헨리허브를 끌어올릴 수 있습니다. 데이터센터 단지에 가스를 보낼 퍼미안 가스관 강관 주문(웰스펀 약 5.8억 달러)이 이미 나왔습니다 [사실]',
    ('로이터','2026-09-29','https://www.reuters.com/business/energy/dash-small-gas-turbines-set-impact-data-center-costs--reeii-2026-09-29/'),('로이터',D,U['welspun'])),
  L('반대로 배터리가 피크 가스발전을 대체할 수 있습니다. 호주는 3분기 가스발전이 2000년 이후 최저로 줄고 저녁 피크에서 배터리 비중(약 8%)이 가스(5.1%)를 처음 앞섰습니다 [사실]',
    ('블룸버그',D,U['aus'])),
  L('원전 재가동이 이어지면 일본 LNG 수요 감소가 데이터센터 증가분을 웃돌 수 있습니다. 2월 재가동한 가시와자키카리와 원전 6호기(1,356MW) 한 기가 JERA 데이터센터 400MW의 3배를 넘습니다 [유추]',
    ('로이터','2026-10-01','https://www.reuters.com/business/energy/jera-teams-up-with-dell-rhaelm-ai-infrastructure-development-japan-2026-10-01/')),
 ],
}
cycle=dict(stage=2,conf='중간',
 why=[
  L('국면은 ② 그대로이고 근거를 새 뉴스로 바꿨습니다. 장기계약이 증설을 받칩니다. 카타르에너지가 셰니에르와 2031~2054년 연 400만 톤 계약을 맺었고 그중 연 100만 톤은 사빈패스 1단계 확장 FID에 달렸으며, 벤처글로벌과도 협상 중입니다 [사실]',('로이터','2026-10-22',U['qatar'])),
  L('LNG캐나다 2단계(연 1,400만 톤 증설)와 코스털가스링크 2단계가 확정됐고 캐나다 2030년 수출능력은 연 3,300만 톤으로 늘 예정이며, 2025년 이후 승인된 대형 LNG 사업 대부분에 사모·인프라 자본이 들어왔습니다 [사실]',('LNG Prime·로이터','2026-09-29','https://lngprime.com/americas/shell-partners-take-fid-on-lng-canada-phase-2/197607/'),('텔레그램 트릴리온',D,U['canada_tg'])),
  L('지금 가격이 높은 것은 카타르 트레인 손상과 호르무즈 차질 때문입니다. TTF 근월물은 10월 20일 장중 MWh당 90.16유로로 전쟁 전의 약 3배였고 EU 저장률은 약 74.6%로 같은 시점 2009년 이후 최저여서, 구조적 부족보다 사건이 만든 부족에 가깝습니다 [유추]',('텔레그램 하나증권 중국전략','2026-10-20',U['ttf']),('LNG Prime·로이터(기존 카드 확인)','2026-09-28','https://lngprime.com/?p=197220')),
  L('미국 헨리허브는 3달러대에 묶여 있고 EIA는 2027년 3.28달러로 더 내려갈 것으로 봅니다. 출구(액화)가 막힌 원산지는 이미 남는 쪽입니다 [사실]',('EIA 단기에너지전망(STEO)','2026-09-09','https://www.eia.gov/outlooks/steo/')),
 ],
 next='2027~2030년 미국·카타르·캐나다의 신규 액화가 한꺼번에 가동되면 ③ 공급 과잉으로 넘어갑니다. 카타르 복구나 호르무즈 통항 정상화가 빨라지면 그 시점이 앞당겨집니다 [유추]',
 watch=['JKM·TTF와 헨리허브의 차이','신규 액화 FID와 장기 구매계약(카타르·아시아 구매자)','EU·독일 가스 저장률','LNG선 현물 운임·계선 척수'],
 split=[])
old=json.load(open('/home/user/news-desk/work/nightly-2026-10-24/chains/gas.json'))
gaps=old['gaps']+' 10월 24일 저녁 업데이트도 검색·열람 없이 입력 뉴스 7건으로만 반영했습니다. 카타르에너지–벤처글로벌 장기계약 협상은 소식통 전언(제목)이고, 캐나다 2030년 수출능력 3,300만 톤은 채널 전언이며, 데본에너지 인수 후보와 캐나다 M&A 사상 최고 발언은 제목·채널 기준이라 근거로 쓰지 않았습니다.'
news=[json.loads(l)['id'] for l in open('/home/user/news-desk/data/industry-2026-10-24-pm/news/gas.jsonl')]
nst=sum(len(v) for v in state.values())
out=dict(id='gas',summary='',state=state,industryState=IS,flags=flags,insight=insight,cycle=cycle,nodeStage={},gaps=gaps,
 note=f'뉴스 7건 반영: 카타르에너지 셰니에르서 23년 연 400만 톤 구매, 호주 가스발전 2000년 이후 최저·배터리가 피크 앞섬, 웰스펀 데이터센터용 가스관 5.8억 달러 수주. 국면 ② 그대로(근거 교체), 근거 {nst}줄, 수치 {len(IS)}줄, 인사이트 a·b2 고침, 재검토 신호 {len(flags)}건, 검색 0회',
 applied=news,searches=0,fetches=0)
json.dump(out,open('/home/user/news-desk/data/industry-2026-10-24-pm/out/gas.json','w'),ensure_ascii=False,indent=1)
