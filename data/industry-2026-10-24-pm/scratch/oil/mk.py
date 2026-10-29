import json
D='2026-10-23'
U=dict(
 sino='https://www.bloomberg.com/news/articles/2026-10-23/shipowner-sinokor-dominates-hormuz-transits-as-oil-flows-rebound',
 iranlong='https://t.me/Trillion_labs/11134',
 brent='https://www.reuters.com/business/energy/russian-espo-oil-sellers-seek-record-premiums-gulf-exports-uncertain-2026-10-23/',
 brent_tg='https://t.me/insidertracking/67117',
 brent_rtr2='https://www.reuters.com/business/energy/oil-little-changed-supply-concern-lingers-amid-houthi-attacks-saudi-arabia-2026-10-23/',
 china='https://www.reuters.com/business/energy/china-calls-oil-gas-firms-boost-output-build-strategic-supply-bases-2026-10-23/',
 chevron='https://www.reuters.com/business/energy/chevron-uses-permian-playbook-breathe-life-into-argentinas-dead-cow-oil-region-2026-10-23/',
 eia='https://www.reuters.com/business/energy/us-refiners-have-run-harder-2026-tight-diesel-supplies-boost-margins-eia-says-2026-10-22/',
 rosn='https://t.me/Trillion_labs/11163',
 joliet='https://www.bloomberg.com/news/articles/2026-10-22/michigan-ohio-gas-prices-spike-further-amid-refinery-breakdown',
 rusdiesel='https://www.reuters.com/business/energy/tanker-carrying-40000-t-russian-diesel-heads-new-york-after-putin-trump-deal-2026-10-23/',
 aal='https://www.reuters.com/business/wizz-air-proposes-buyout-some-uk-pilots-bloomberg-news-reports-2026-10-23/',
 aal_b='https://www.bloomberg.com/news/articles/2026-10-23/wizz-air-offers-uk-pilots-buyouts-as-soaring-jet-fuel-costs-bite',
 dpa='https://www.reuters.com/business/energy/trump-invokes-cold-war-era-defense-production-act-oil-production-refining-2026-10-22/',
 indo='https://www.reuters.com/business/energy/indonesia-energy-ministry-consider-additional-quota-subsidised-fuel-demand-rises-2026-10-23/',
 japan='https://www.reuters.com/business/energy/japan-weighs-phasing-out-gasoline-subsidies-december-costs-mount-officials-say-2026-10-23/',
 cftc='https://www.reuters.com/business/energy/us-regulator-is-probing-suspicious-iran-oil-trading-official-says-2026-10-22/',
 trump='https://t.me/insidertracking/67085',
 rigzone='https://rigzone.com/news/north_america_adds_rigs_for_3_straight_weeks_bh_count_shows-12-oct-2026-184827-article',
 mugg='https://mugglehead.com/bp-third-quarter-net-debt-refining-margins/',
)
def S(d,o,u,nid,t): return dict(d=d,o=o,u=u,nid=nid,t=t)
state={
 'transport':[
  S(D,'블룸버그',U['sino'],'n-bbg-0645','한국 선주 시노코르 선박이 9월 호르무즈 VLCC 통항의 47%, 10월 첫 열흘의 절반 이상을 차지했고 그중 6척은 이란 측 블랙리스트에 올라 통항이 소수 선주에 쏠려 있습니다 [사실]'),
  S(D,'텔레그램 트릴리온',U['iranlong'],'n-tg-0729','이란은 호르무즈 해협 7개 조건을 거두지 않은 채 해저 케이블·데이터센터·에너지 시설·미군 기지·상선을 위협 대상으로 삼으며 장기 대결에 대비하고 있다는 전언입니다 [채널]'),
 ],
 'opec':[
  S(D,'텔레그램 미국 주식 인사이더',U['brent_tg'],'n-tg-0723','Kpler 기준 18일까지 한 주 호르무즈·대체 항로 원유 수출은 하루 평균 2,400만 배럴로 전쟁 전 2,330만 배럴을 넘었다는 전언이 나왔습니다 [채널]'),
  S(D,'로이터',U['brent'],'n-tg-0723','사우디는 아람코 샤이바 유전을 노린 드론을 요격해 운영 차질이 없었지만, 걸프 수출이 불확실해지자 러시아 ESPO 원유 판매자들은 사상 최고 프리미엄을 요구하고 있습니다 [사실]'),
 ],
 'nonopec':[
  S(D,'로이터',U['china'],'n-rtr-0709','중국 국가에너지국은 석유·가스 기업에 투자·탐사 확대와 전략 공급기지 조성을 주문했고, 원유 생산은 지난해 2.16억 톤으로 최대였으며 2030년 공급 하한은 석유환산 4.4억 톤입니다 [사실]'),
  S(D,'로이터',U['chevron'],'n-tg-0734','셰브론은 아르헨티나 엘트라피알 광구(하루 약 4만 boe)에 퍼미안식 인력·장비를 들여 2029년 초까지 리그를 1기에서 3기로 늘리며, 138억 달러 30년 계획은 정부 승인이 남았습니다 [사실]'),
 ],
 'refining':[
  S(D,'로이터',U['eia'],'n-rtr-0677','EIA는 미국 정유 가동률이 5~9월 평균 95%를 넘어 같은 기간 1998년 이후 최고였고 미국 정제 능력은 2019년 이후 4% 줄었다고 했으며, 발레로 3분기 정제마진은 배럴당 39.24달러로 거의 3배가 됐습니다 [사실]'),
  S(D,'텔레그램 트릴리온',U['rosn'],'n-tg-0121','블룸버그 집계로 우크라이나는 올해 러시아 정유시설을 최소 114차례 공격해 지난해 같은 기간의 두 배를 넘었고, 로스네프트는 재피격을 우려해 정유소 복구를 몇 주~몇 달로 늦추고 있습니다 [사실]'),
 ],
 'products':[
  S('2026-10-22','블룸버그',U['joliet'],'n-tg-0450','엑손모빌 졸리엣 정유공장의 하루 5만 배럴 개질 설비가 10월 20일 멈춘 뒤 미시간 휘발유는 하룻밤 새 약 17센트 오른 갤런당 4.61달러로 전국 평균 4.27달러를 웃돌았습니다 [사실]'),
  S('2026-10-22','로이터',U['rusdiesel'],'n-tg-0724','푸틴·트럼프 합의에 따른 첫 러시아 경유 화물 4만 톤이 10월 22일 프리모르스크항에서 선적돼 뉴욕으로 향하고 있으며, Kpler는 11월 7일 도착을 예상했습니다 [사실]'),
 ],
 'stocks':[
  S(D,'로이터',U['eia'],'n-rtr-0677','9월 말 미국 중간유분 재고는 5년 계절 평균보다 약 13% 적었고, EIA는 호르무즈 운송이 정상화되면 2027년 디젤 마진이 누그러질 수 있다고 봤습니다 [사실]'),
 ],
 'price':[
  S(D,'로이터',U['brent'],'n-tg-0723','후티의 사우디 공격과 미국·이스라엘의 이란 재공습 우려로 브렌트유는 22일 113.17달러로 마감한 뒤 23일 장중 114.72달러까지 올라 5월 이후 최고를 기록했습니다 [사실]'),
 ],
 'demand':[
  S(D,'로이터',U['aal'],'n-rtr-0667','아메리칸항공의 3분기 연료비는 67.5% 늘어난 46억 달러(갤런당 3.85달러, 전년 2.37달러)였고 2026년 조정 주당손실 1.00~1.60달러를 전망해, 고유가가 항공 수요 쪽 이익을 깎고 있습니다 [사실]'),
 ],
 'policy':[
  S('2026-10-22','로이터',U['dpa'],'n-tg-0722','트럼프 대통령은 10월 22일 국방물자생산법 각서로 탐사·생산, 파이프라인, 저장, 해상 터미널에 정부 구매·대출·대출보증을 허용했고, 특정 사업과 금액 상한은 정하지 않았습니다 [사실]'),
 ],
}
IS=[
 dict(d=D,kind='price',o='로이터',u=U['brent'],nid='n-tg-0723',t='브렌트유는 23일 장중 배럴당 114.72달러로 5월 이후 최고였고 22일 종가는 113.17달러였습니다 [사실]'),
 dict(d=D,kind='supply',o='로이터',u=U['eia'],nid='n-rtr-0677',t='EIA 집계로 미국 정유 가동률은 5~9월 평균 95%를 넘어 같은 기간 1998년 이후 최고였고, 9월 말 중간유분 재고는 5년 평균보다 약 13% 적었습니다 [사실]'),
 dict(d=D,kind='supply',o='텔레그램 미국 주식 인사이더',u=U['brent_tg'],nid='n-tg-0723',t='Kpler 기준 18일까지 한 주 호르무즈·대체 항로 원유 수출은 하루 2,400만 배럴(전쟁 전 2,330만 배럴)이었고, 미 상업 원유 재고는 310만 배럴 줄어 4억 1,250만 배럴이었습니다 [채널]'),
 dict(d=D,kind='demand',o='로이터',u=U['indo'],nid='n-rtr-0671',t='인도네시아 보조 연료 소비가 할당량 2,927만 kL보다 약 10% 빠르게 늘어 추가 쿼터를 검토하고, 일본은 보조금 축소 시 휘발유값이 12월 리터당 약 175엔, 1월 약 180엔으로 오를 수 있습니다 [사실]'),
]
flags=[
 dict(nid='n-tg-0722',t='재검토 필요: 국방물자생산법 발동이 정제를 넘어 탐사·생산·파이프라인·저장·해상 터미널에 정부 대출·보증을 열어 ② 자본 유입·증설 국면을 가리키며, 정책 자금이 사슬 상류까지 증설을 앞당기려 하기 때문입니다 [유추]'),
 dict(nid='n-tg-0723',t='재검토 필요: 호르무즈·대체 항로 원유 수출이 하루 2,400만 배럴로 전쟁 전을 넘었다는 Kpler 전언은 ③ 공급 과잉 국면을 가리키며, 원유 물량이 회복되면 제품 병목이 풀리는 순간 가격이 빠르게 꺾일 수 있기 때문입니다 [유추]'),
]
def L(t,*src): return dict(t=t,src=[dict(o=o,d=d,u=u) for o,d,u in src])
insight={
 'a':[
  L('전쟁이 원유보다 석유제품·수송 고리를 더 오래 막는 구조가 굳어지고 있습니다. 걸프 원유 수출은 전쟁 전의 75%를 넘었지만 IEA는 경유 부족이 2027년까지 간다고 봤고, 비톨은 원유 통항이 늘어도 선박 연료 부족이 이어진다고 했습니다 [귀납]',
    ('텔레그램 상상인 김진범(IEA 10월 보고서)','2026-10-15','https://t.me/PipeBeom/6705'),('로이터','2026-10-16','https://www.reuters.com/business/energy/global-fuel-oil-market-stays-tight-conflicts-hit-mideast-russia-supplies-vitol-2026-10-16/')),
  L('증설이 안보 정책으로 사슬 전체에 번지고 있습니다. 트럼프 대통령은 10월 22일 국방물자생산법으로 탐사·생산·파이프라인·저장·해상 터미널에 정부 구매·대출·보증을 열었고, 미국 정제 능력은 2019년 이후 4% 줄어 있어 정유 증설이 정책의 첫 대상입니다 [사실]',
    ('로이터','2026-10-22',U['dpa']),('로이터','2026-10-22',U['eia'])),
 ],
 'b':[
  L('공급 쪽은 원유와 제품이 더 갈렸습니다. 호르무즈·대체 항로 원유 수출이 하루 2,400만 배럴로 전쟁 전을 넘었다는 Kpler 전언이 나온 반면, 우크라이나는 올해 러시아 정유시설을 최소 114차례 공격했고 로스네프트는 복구를 몇 달로 늦추고 있습니다 [귀납]',
    ('텔레그램 미국 주식 인사이더',D,U['brent_tg']),('텔레그램 트릴리온',D,U['rosn'])),
  L('수요 쪽은 고유가가 소비를 줄이고 있습니다. IEA는 올해 세계 수요가 하루 260만 배럴 줄고 2027년 소비도 2025년보다 하루 62만 배럴 적을 것으로 봤고, 아메리칸항공은 3분기 연료비가 67.5% 늘어 2026년 적자를 전망했습니다 [귀납]',
    ('텔레그램 상상인 김진범(IEA 10월 보고서)','2026-10-15','https://t.me/PipeBeom/6705'),('로이터',D,U['aal'])),
 ],
 'c':[
  L('Kpler는 18일까지 한 주 호르무즈·대체 항로 원유 수출이 전쟁 전 수준을 넘었다고 집계했고, 트럼프 대통령은 호르무즈 통과 석유가 분쟁 전보다 많으며 이란 문제를 곧 끝내면 유가가 급락한다고 말했습니다 [채널]',
    ('텔레그램 미국 주식 인사이더',D,U['brent_tg']),('텔레그램 미국 주식 인사이더',D,U['trump'])),
  L('EIA는 호르무즈 운송이 정상화되면 2027년 디젤 마진이 누그러질 수 있다고 봤고, 중국은 석유·가스 증산을, 셰브론은 아르헨티나 바카무에르타 리그 확대를 추진해 비걸프 공급도 늘어날 길이 있습니다 [사실]',
    ('로이터',D,U['eia']),('로이터',D,U['china']),('로이터',D,U['chevron'])),
 ],
 'c1':[
  L('아직은 덮지 못합니다. 브렌트는 23일 장중 114.72달러로 5월 이후 최고였고, 미국·이스라엘이 11월 3일 선거 뒤 이란 공습을 재개할 수 있다는 보도에 이란은 걸프 석유시설 보복을 위협하며 7개 조건을 거두지 않았습니다 [사실]',
    ('로이터',D,U['brent']),('텔레그램 트릴리온',D,U['iranlong'])),
  L('원유 물량이 돌아와도 미국 중간유분 재고가 5년 평균보다 약 13% 적고 정유 가동률이 이미 95%를 넘어, 제품 부족은 원유 회복보다 늦게 풀릴 가능성이 큽니다 [유추]',
    ('로이터',D,U['eia'])),
 ],
 'd':[
  L('유가가 정치 변수가 됐습니다. 트럼프 대통령은 디젤 수출량 상한제를 할 수 있다고 했고 대러 제재 면제·비축유 교환·국방물자생산법을 함께 쓰며, CFTC는 3월 23일·4월 7일 대이란 정책 발표 직전의 이례적 원유 거래를 조사하고 있어 11월 선거 전후로 공급 정책과 가격이 크게 흔들릴 수 있습니다 [유추]',
    ('로이터','2026-10-20','https://www.reuters.com/business/energy/iea-ready-go-if-further-oil-stocks-release-needed-chief-says-2026-10-20/'),('로이터','2026-10-22',U['cftc'])),
  L('고유가의 부담은 재정과 운송으로 옮겨 갑니다. 일본은 12월부터 휘발유 보조금 단계적 축소를, 인도네시아는 보조 연료 추가 쿼터를 검토하고, 위즈에어는 조종사 희망퇴직을 제안해 수요 파괴가 정부 예산과 항공사 비용에서 먼저 드러납니다 [귀납]',
    ('로이터',D,U['japan']),('로이터',D,U['indo']),('블룸버그',D,U['aal_b'])),
  L('HSBC CEO는 걸프의 대체 경로로 호르무즈가 5년 안에 불필요해질 수 있다고 했지만, 우회 송유관은 사우디·UAE만 갖고 있고 사우디 동서 송유관도 드론 공격으로 감량 재가동된 상태라 해협의 값이 빨리 사라지지는 않습니다 [유추]',
    ('로이터','2026-10-20','https://www.reuters.com/business/energy/hsbc-ceo-says-alternative-routes-could-make-strait-hormuz-redundant-five-years-2026-10-20/')),
 ],
}
cycle=dict(stage=1,conf='중간',
 why=[
  L('국면은 ① 그대로이고 근거를 새 뉴스로 바꿨습니다. 정제 고리가 한계까지 돌고 있습니다. EIA는 미국 정유 가동률이 5~9월 평균 95%를 넘어 같은 기간 1998년 이후 최고였고 9월 말 중간유분 재고는 5년 평균보다 약 13% 적었다고 했습니다 [사실]',('로이터',D,U['eia'])),
  L('사슬 중간의 마진이 사상 최고권입니다. 발레로 3분기 정제마진은 배럴당 39.24달러로 거의 3배가 됐고, BP(46.7달러)·셸(42달러)·토탈(33.2달러)도 3분기 정제 마진이 크게 뛰었습니다 [사실]',('로이터',D,U['eia']),('Mugglehead(BP 3분기 트레이딩 업데이트)','2026-10-13',U['mugg'])),
  L('가격도 다시 올랐습니다. 후티의 사우디 공격과 미국·이스라엘의 이란 재공습 우려로 브렌트는 23일 장중 114.72달러로 5월 이후 최고였고, 에니는 3분기 브렌트 평균 97달러에 특별배당 약 13억 유로를 내놨습니다 [사실]',('로이터',D,U['brent']),('텔레그램 Polaristimes',D,'https://t.me/The_MariTimes/63945')),
  L('자본 유입은 정책 주도로 시작됐지만 상류는 아직 신중합니다. 국방물자생산법 발동으로 탐사·생산·파이프라인·저장에 정부 대출·보증이 열렸으나, 미국 원유 리그는 462개로 1년 새 44개 늘어나는 데 그쳤습니다 [귀납]',('로이터','2026-10-22',U['dpa']),('Rigzone(베이커휴즈 집계)','2026-10-12',U['rigzone'])),
 ],
 next='호르무즈 원유 물량 회복에 이어 제품 통항과 미국 중간유분 재고가 다시 쌓이기 시작하면 운임·마진·유가가 함께 내려 ③ 공급 과잉으로 넘어갈 수 있습니다. 반대로 전쟁이 길어진 채 국방물자생산법 자금과 신규 정유소·유조선 발주가 실제 착공·계약으로 이어지면 ② 자본 유입·증설로 진행합니다 [유추]',
 watch=['미국 상업용 원유·중간유분 재고(EIA 주간)','호르무즈 통항량·걸프 제품 수출(Kpler)','유럽·아시아 경유 크랙과 미국 정유 가동률','국방물자생산법 대출·보증 집행과 신규 정유소 착공','11월 3일 미 선거 뒤 이란 공습 재개 여부'],
 split=[])
summary=('원유·석유제품 산업은 OPEC+·미국 셰일 같은 생산자가 뽑은 원유를 유조선·송유관으로 정유공장에 보내 경유·휘발유·항공유 같은 제품으로 바꿔 운송·항공·산업 수요에 파는 사슬이며, 재고·전략비축유가 그 사이를 완충합니다. '
 '지금 가장 빠듯한 고리는 정제와 제품 재고입니다. EIA는 미국 정유 가동률이 5~9월 평균 95%를 넘어 1998년 이후 최고였는데도 9월 말 중간유분 재고가 5년 평균보다 약 13% 적었다고 했고, 발레로 3분기 정제마진은 배럴당 39.24달러로 거의 3배가 됐습니다. '
 '우크라이나의 러시아 정유시설 공격은 올해 최소 114차례로 늘었고 엑손 졸리엣 설비 정지로 미시간 휘발유가 4.61달러까지 오르는 등 정제 차질이 이어집니다. '
 '원유 물량은 Kpler 기준 호르무즈·대체 항로 수출이 전쟁 전 수준을 넘었다는 전언이 나와 덜 빠듯해졌지만, 사우디 피격과 이란 재공습 우려로 브렌트는 23일 장중 114.72달러로 5개월 최고에 올랐습니다.')
gaps=('이번 업데이트는 검색·열람 없이 입력 뉴스만으로 반영했고, 블룸버그·로이터 기사와 전재본은 열지 않았습니다. 아래는 확인하지 못했습니다. '
 '(1) Kpler의 18일까지 한 주 호르무즈·대체 항로 원유 수출 하루 2,400만 배럴(전쟁 전 2,330만 배럴)과 미 상업 원유 재고 4억 1,250만 배럴은 채널 전언이며, 같은 Kpler의 앞선 집계(최근 7일 호르무즈 선적 전쟁 전보다 약 41% 적음)와 범위가 다릅니다. '
 '(2) 미·이란의 카타르·파키스탄 중재안 예비 승인은 보도뿐이며, 이후 트럼프 대통령의 추가 타격 발언과 11월 3일 선거 뒤 공습 재개 보도로 협상 전망이 엇갈립니다. '
 '(3) 트럼프 대통령의 호르무즈 기뢰 보고 조작 주장과 하메네이의 3천만 명 희생 주장은 독립 검증이 없습니다. '
 '(4) VLCC 운임선물(11월 8%, 1분기 17% 상승)과 SLB 실적 수치는 채널 전언입니다. '
 '(5) 국방물자생산법의 실제 대출·보증 규모와 대상 사업은 정해지지 않았습니다. '
 '(6) 러시아산 경유 공급 계획(즉시 30만 톤, 11월 50만 톤)은 트럼프 발언이며 실제 선적은 첫 화물 4만 톤만 확인됐습니다. '
 '(7) 데본에너지 인수 후보와 캐나다 M&A 사상 최고 발언은 제목·채널 기준이라 근거로 쓰지 않았습니다.')
news=[json.loads(l)['id'] for l in open('/home/user/news-desk/data/industry-2026-10-24-pm/news/oil.jsonl')]
nst=sum(len(v) for v in state.values())
out=dict(id='oil',summary=summary,state=state,industryState=IS,flags=flags,insight=insight,cycle=cycle,nodeStage={},gaps=gaps,
 note=f'뉴스 18건 반영: 브렌트 장중 114.72달러 5개월 최고, 미 정유 가동률 5~9월 95% 넘어 1998년 이후 최고·발레로 정제마진 39.24달러, 국방물자생산법 발동. 국면 ① 그대로(근거 교체), 근거 {nst}줄, 수치 {len(IS)}줄, 재검토 신호 {len(flags)}건, 검색 0회',
 applied=news,searches=0,fetches=0)
json.dump(out,open('/home/user/news-desk/data/industry-2026-10-24-pm/out/oil.json','w'),ensure_ascii=False,indent=1)
