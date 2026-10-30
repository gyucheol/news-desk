import json
D='2026-10-23'
U=dict(
 kering='https://www.reuters.com/business/retail-consumer/kering-shares-drop-11-gucci-sales-slide-2026-10-23/',
 deckers='https://www.reuters.com/business/deckers-results-show-aggressive-discounts-rivals-are-hitting-premium-brands-2026-10-22/',
 pg='https://www.reuters.com/business/retail-consumer/pg-flags-bigger-hit-annual-profit-higher-commodity-costs-beats-revenue-estimates-2026-10-22/',
 pg_tg='https://t.me/insidertracking/67063',
 barilla='https://www.bloomberg.com/news/articles/2026-10-23/barilla-paid-750-million-for-goodles-in-an-all-cash-deal',
 bimbo='https://www.reuters.com/business/retail-consumer/mexicos-bimbo-lifts-lower-end-full-year-ebitda-outlook-2026-10-22/',
 italy='https://www.bloomberg.com/news/articles/2026-10-23/italian-truckers-lift-roadblocks-that-snarled-food-deliveries',
 heineken='https://www.reuters.com/legal/litigation/heineken-document-reveals-worries-over-weight-loss-drugs-beer-sales-2026-10-23/',
 electrolux='https://www.reuters.com/business/electrolux-q3-core-profit-tops-expectations-2026-10-23/',
 debenhams='https://www.reuters.com/business/retail-consumer/uks-debenhams-returns-profit-after-five-years-expects-further-cost-cuts-2026-10-23/',
 pnp='https://www.reuters.com/world/africa/south-africas-pick-n-pay-withdraws-restructuring-process-sees-narrower-interim-2026-10-22/',
 sodexo='https://www.reuters.com/business/sodexo-beats-expectations-signals-progress-turnaround-2026-10-23/',
 accor='https://www.reuters.com/business/accor-lifts-outlook-middle-east-rebounds-2026-10-22/',
 evoke='https://www.reuters.com/world/uk/william-hill-owner-evokes-q3-revenue-falls-uk-shop-closures-unfavourable-sports-2026-10-23/',
 hermes='https://www.bloomberg.com/news/articles/2026-10-23/hermes-cartier-s-last-reliable-shoppers-are-retreating-in-china',
)
def S(d,o,u,nid,t): return dict(d=d,o=o,u=u,nid=nid,t=t)
state={
 'apparel':[
  S(D,'로이터',U['kering'],'n-bbg-0642','구찌 3분기 매출은 12.9억 유로로 비교 기준 6% 줄고 직영 매장 동일 매장 매출이 9% 줄었으며, 케링은 올해 9개월간 105개 매장을 순폐점했고 주가는 11% 넘게 떨어졌습니다 [사실]'),
  S('2026-10-22','로이터',U['deckers'],'n-rtr-0689','데커스는 경쟁사의 공격적 할인으로 직접판매가 1.8% 줄었다며 연간 매출 전망을 57억~57억 2,500만 달러로 낮춰 컨센서스 약 58억 8,000만 달러를 밑돌았습니다 [사실]'),
 ],
 'household':[
  S('2026-10-22','로이터',U['pg'],'n-rtr-0682','P&G의 1분기 순매출은 233억 달러로 유기적 매출이 4% 늘었지만, 핵심 영업이익률은 25.9%로 80bp 떨어졌고 연간 핵심 EPS 0~3% 성장 전망은 유지했습니다 [사실]'),
 ],
 'food':[
  S(D,'블룸버그',U['barilla'],'n-bbg-0665','바릴라는 미국 맥앤치즈 브랜드 굿을스를 7억 5,000만 달러 전액 현금에 인수했고 실적 연동 추가 지급이 최소 1억 달러이며, 굿을스의 최근 12개월 순매출은 1억 9,000만 달러입니다 [사실]'),
  S('2026-10-22','로이터',U['bimbo'],'n-rtr-0691','빔보의 3분기 순이익은 22% 늘고 조정 EBITDA 마진은 15.7%였으며, 연간 마진 확대 전망 하단을 60bp에서 85bp로 올렸지만 2027년 멕시코·북미 물가 부담을 경고했습니다 [사실]'),
 ],
 'alcohol':[
  S(D,'로이터',U['heineken'],'n-rtr-0670','하이네켄은 영국 외식업 고객 자료에서 GLP-1 약물이 맥주·사이다 판매를 압박할 수 있다며 하프 파인트·저알코올 판촉을 권했고, JP모건 조사로 지난해 미국 약 1,000만 명이 이런 약을 썼습니다 [사실]'),
 ],
 'durables':[
  S(D,'로이터',U['electrolux'],'n-rtr-0731','일렉트로룩스의 3분기 조정 영업이익은 9억 1,200만 크로나로 예상을 넘었지만 순손실 3억 4,000만 크로나를 냈고, 연간 물량·가격·믹스 기여 전망을 긍정에서 중립으로 낮췄습니다 [사실]'),
 ],
 'retail':[
  S(D,'로이터',U['debenhams'],'n-rtr-0699','데버넘스 그룹은 6개월 세전이익 2,830만 파운드로 5년 만에 흑자를 냈지만 약 4,000만 파운드 일회성 리스 이익이 들어 있고, 매출은 3% 줄어 4억 960만 파운드였습니다 [사실]'),
  S('2026-10-22','로이터',U['pnp'],'n-rtr-0703','픽앤페이는 매장 직원 약 2만 2,000명 대상 감원 협의를 노조와 합의해 철회했고, 할인점 박서의 이익 증가로 상반기 주당 헤드라인 손실이 25~35% 줄 것으로 봤습니다 [사실]'),
 ],
 'dining':[
  S(D,'로이터',U['sodexo'],'n-rtr-0704','소덱소의 2026 회계연도 유기적 성장률은 2.0%로 가이던스(1.2~1.5%)를 넘었지만 북미는 -1.0%였고, 기초 영업이익률은 3.4%로 130bp 떨어졌습니다 [사실]'),
 ],
 'leisure':[
  S('2026-10-22','로이터',U['accor'],'n-rtr-0686','아코르의 3분기 RevPAR는 4.9% 늘어 연간 반복 EBITDA 전망 하단을 12억 7,000만 유로로 올렸지만, UAE RevPAR는 여전히 약 20% 낮고 중국 호텔 폐점으로 순객실 증가 목표를 3~3.5%로 낮췄습니다 [사실]'),
  S(D,'로이터',U['evoke'],'n-rtr-0698','윌리엄힐 모회사 에보크의 3분기 매출은 4억 600만 파운드로 7% 줄었고, 영국 온라인 도박세가 40%로 오른 가운데 매장 폐쇄가 당초 약 200곳에서 270곳으로 늘었습니다 [사실]'),
 ],
}
IS=[
 dict(d='2026-10-22',kind='price',o='텔레그램 미국 주식 인사이더',u=U['pg_tg'],nid='n-rtr-0682',t='P&G는 브렌트유 배럴당 약 100달러 가정에서 원자재·에너지 세후 비용 부담 전망을 약 14억 달러로 올렸고(종전 약 10억 달러), 영업이익 아래 항목까지 넣으면 약 19억 달러로 봤습니다 [채널]'),
 dict(d=D,kind='supply',o='로이터',u=U['kering'],nid='n-bbg-0642',t='케링은 올해 9개월간 105개 매장을 순폐점했고, 구찌 직영 매장 동일 매장 매출은 3분기 9% 줄었습니다 [사실]'),
 dict(d=D,kind='supply',o='로이터',u=U['evoke'],nid='n-rtr-0698',t='에보크의 윌리엄힐 매장 폐쇄는 당초 약 200곳에서 270곳으로 늘었고, 3분기 매출은 7% 줄어 4억 600만 파운드(동일 기준 -2%)였습니다 [사실]'),
 dict(d='2026-10-22',kind='demand',o='로이터',u=U['deckers'],nid='n-rtr-0689',t='데커스는 연간 매출 전망을 57억~57억 2,500만 달러로 낮춰 컨센서스 약 58억 8,000만 달러를 밑돌았고, 120달러 미만 가격대에서 점유율 손실 가능성이 크다고 했습니다 [사실]'),
]
flags=[
 dict(nid='n-bbg-0642',t='재검토 필요: 케링의 9개월 105개 매장 순폐점과 에보크의 매장 270곳 폐쇄는 명품·도박 노드가 ⑥ 공급 파괴·통합 국면으로 옮겨 가는 신호를 가리키며, 수요 부진이 매장 수 감축으로 이어지고 있기 때문입니다 [유추]'),
 dict(nid='n-rtr-0682',t='재검토 필요: P&G 1분기 유기적 매출이 판매량 주도로 4% 늘어난 것은 생활용품 노드가 ⑦ 바닥 형성 쪽에 있음을 가리킬 수 있으며, 킴벌리클라크의 물량 감소와 달리 필수재 물량이 버티고 있기 때문입니다 [유추]'),
]
def L(t,*src): return dict(t=t,src=[dict(o=o,d=d,u=u) for o,d,u in src])
insight={
 'b':[
  L('공급이 줄기 시작했고 명품·도박 매장으로 넓어졌습니다. 케링은 9개월간 105개 매장을 순폐점했고 에보크는 윌리엄힐 매장 폐쇄를 약 200곳에서 270곳으로 늘렸으며, 앞서 화이트브레드는 브랜드 식당 197곳 철수를, TWE는 브랜드를 76개에서 30개로 줄이기로 했습니다 [귀납]',
    ('로이터',D,U['kering']),('로이터',D,U['evoke']),('로이터','2026-10-13','https://www.reuters.com/business/premier-inn-owner-whitbread-urges-shareholders-reject-corvexs-board-seat-demand-2026-10-13/')),
  L('수요는 물량이 아니라 가격이 받치고 있습니다. NRF는 연말 매출 증가분의 약 절반이 가격 상승이라고 봤고, 데커스는 경쟁사의 공격적 할인으로 프리미엄 신발 판매가 타격을 받았다며 연간 매출 전망을 낮췄습니다 [귀납]',
    ('로이터','2026-10-15','https://www.reuters.com/business/retail-consumer/us-holiday-sales-growth-speed-up-shoppers-stay-resilient-nrf-forecasts-2026-10-15/'),('로이터','2026-10-22',U['deckers'])),
 ],
 'c':[
  L('필수재 물량이 버틴다는 정보가 나왔습니다. P&G의 1분기 유기적 매출이 판매량 주도로 4% 늘었고, 빔보는 조정 EBITDA 마진 전망 하단을 높였으며, 소덱소의 연간 유기적 성장률은 2.0%로 가이던스를 넘었습니다 [사실]',
    ('로이터','2026-10-22',U['pg']),('로이터','2026-10-22',U['bimbo']),('로이터',D,U['sodexo'])),
  L('여행 수요도 일부 돌아오고 있습니다. 아코르의 3분기 RevPAR는 4.9% 늘어 연간 EBITDA 전망을 올렸고 사우디·이집트·튀르키예는 늘었으며, 앞서 아마존은 연말 채용을 30만 명 이상으로 20% 늘렸습니다 [사실]',
    ('로이터','2026-10-22',U['accor']),('로이터','2026-10-20','https://www.reuters.com/legal/litigation/amazon-recruit-over-300000-workers-holiday-season-first-hiring-jump-three-years-2026-10-20/')),
 ],
 'c1':[
  L('덮을 만큼 크지는 않습니다. P&G도 핵심 영업이익률이 80bp 떨어지고 원자재·에너지 비용 부담이 커졌으며, 휘발유를 뺀 9월 판매는 0.2% 느는 데 그쳤고 구찌·데커스처럼 재량 소비재는 판매 감소와 할인 경쟁이 이어집니다 [귀납]',
    ('로이터','2026-10-22',U['pg']),('미국 인구조사국(9월 소매판매 속보)','2026-10-15','https://www.census.gov/retail/sales.html'),('로이터',D,U['kering'])),
 ],
 'd':[
  L('운영 위험 쪽에서 보면, 아홀드 온라인 배송이 최소 11일 멈추고 프랑스 슈퍼마켓 약 700곳이 냉장 관리 소프트웨어 공격을 받았으며, 이탈리아 트럭 시위로 라도리아가 남부 7개 공장을 멈추는 등 물류·사이버 차질이 식품 공급의 새 병목이 되고 있습니다 [귀납]',
    ('로이터','2026-10-19','https://www.reuters.com/business/albert-heijn-online-deliveries-stay-offline-until-least-thursday-after-cyber-2026-10-19/'),('블룸버그',D,U['italy'])),
  L('비만약이 수요의 구성을 바꾸고 있습니다. 하이네켄은 GLP-1 약물이 맥주 판매를 압박할 수 있다고 펍에 경고했고, 디아지오·칼스버그는 영향이 아직 제한적이라고 봤지만 단백질 식품 붐이 일고 있습니다 [사실]',
    ('로이터',D,U['heineken']),('로이터',D,'https://www.reuters.com/legal/litigation/weight-loss-drugs-fuel-protein-boom-with-more-consumer-scrutiny-2026-10-23/')),
  L('중국에서는 7개 부처가 전자상거래의 자동 가격 추종·전국 최저가 경쟁을 바로잡겠다고 해, 수요 회복이 아니라 정책으로 가격 경쟁이 누그러지는 경로가 열릴 수 있습니다 [유추]',
    ('텔레그램 하나증권 중국전략','2026-10-16','https://t.me/HANAchina/70174')),
 ],
}
old=json.load(open('/home/user/news-desk/work/nightly-2026-10-24/chains/consumer.json'))
summary=('소비재·유통은 농산물·섬유·펄프·전자부품 같은 원재료를 식품·주류·생활용품·의류·내구재 브랜드가 제품으로 만들고, 마트·편의점·온라인몰이 소비자에게 팔며, 외식·여행·카지노가 같은 지갑을 서비스로 나눠 갖는 사슬입니다. '
 '사슬 끝의 가계 지갑이 모든 노드의 판매량을 정하므로 실질 소득·물가·신용이 업황의 출발점입니다. '
 '미국 9월 소매판매는 0.8% 늘었지만 증가분의 약 71%가 휘발유값에서 나와 명목 지출 아래 실질 물량은 약하고, 원가 쪽에서는 P&G가 원자재·에너지 비용 부담 전망을 키우는 등 고유가가 마진을 누릅니다. '
 '가장 남는 쪽은 명품·재량 소비재로, 구찌 3분기 매출이 비교 기준 6% 줄고 유럽 명품 밸류에이션이 10년 만의 최저로 떨어졌으며 데커스는 경쟁사 할인에 전망을 낮췄습니다. '
 '케링 105개 매장 순폐점, 에보크 매장 270곳 폐쇄, 화이트브레드 식당 197곳 철수, 바릴라의 굿을스 인수처럼 공급을 줄이고 합치는 움직임이 넓어지는 반면, P&G 판매량 주도 성장과 아코르 전망 상향처럼 필수재·여행 일부는 버티고 있습니다.')
gaps=old['gaps']+' (8) 10월 24일 저녁 업데이트는 검색·열람 없이 입력 뉴스 18건으로만 반영했습니다. P&G 원자재 비용 부담 약 14억 달러와 FCF 전망은 채널 전언이고, 치폴레 매출 둔화·셰인 FTC 합의·허쉬 단백질 초콜릿은 제목 수준이며, 유럽 명품 밸류에이션 10년 최저는 수치를 확인하지 못했습니다.'
news=[json.loads(l)['id'] for l in open('/home/user/news-desk/data/industry-2026-10-24-pm/news/consumer.jsonl')]
nst=sum(len(v) for v in state.values())
out=dict(id='consumer',summary=summary,state=state,industryState=IS,flags=flags,insight=insight,cycle=None,nodeStage={},gaps=gaps,
 note=f'뉴스 18건 반영: 구찌 3분기 매출 6% 감소·케링 105개 매장 순폐점, P&G 유기적 매출 4%·원자재 비용 부담 확대, 에보크 매장 270곳 폐쇄·아코르 전망 상향. 국면 ④ 그대로, 근거 {nst}줄, 수치 {len(IS)}줄, 재검토 신호 {len(flags)}건, 검색 0회',
 applied=news,searches=0,fetches=0)
json.dump(out,open('/home/user/news-desk/data/industry-2026-10-24-pm/out/consumer.json','w'),ensure_ascii=False,indent=1)
