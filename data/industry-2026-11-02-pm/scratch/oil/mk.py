import json
B = '/home/user/news-desk'
old = json.load(open(f'{B}/work/nightly-2026-11-02/chains/oil.json'))
U_EX = "https://www.bloomberg.com/news/articles/2026-10-30/exxon-reaps-record-oil-refining-profits-on-war-driven-gasoline-diesel-spikes"
U_BIG = "https://www.bloomberg.com/news/articles/2026-10-31/big-oil-is-grappling-with-how-to-spend-its-windfall-profits"
U_REL = "https://www.bloomberg.com/news/articles/2026-11-02/reliance-industries-surges-most-in-nine-months-on-earnings-beat"
U_OPEC = "https://www.bloomberg.com/news/articles/2026-11-01/opec-set-to-stick-with-plan-for-steady-quotas-delegates-say"
U_POL = "https://t.me/The_MariTimes/64167"
U_GS = "https://www.bloomberg.com/news/articles/2026-11-02/goldman-hikes-oil-price-forecasts-on-substantial-supply-risks"
U_CN = "https://www.bloomberg.com/news/articles/2026-10-30/cnooc-profit-rises-as-oil-rally-boosts-upstream-operations"
U_JP = "https://www.bloomberg.com/news/articles/2026-10-30/japan-to-scale-back-fuel-subsidies-as-iran-war-costs-mount"
U_ID = "https://www.reuters.com/business/energy/indonesia-energy-ministry-consider-additional-quota-subsidised-fuel-demand-rises-2026-10-23/"
U_BASH = "https://www.bloomberg.com/news/articles/2026-10-31/ukraine-strikes-bashneft-refineries-as-russia-attacks-power-grid"
U_DSL = "https://www.bloomberg.com/news/articles/2026-10-31/russia-extends-ban-on-most-diesel-exports-through-january"
U_PK = "https://www.bloomberg.com/news/articles/2026-11-01/pakistan-lng-cargo-attacked-near-hormuz-had-iranian-approval"
U_HZ = "https://t.me/The_MariTimes/64171"
U_EIA = "https://www.reuters.com/business/energy/us-refiners-have-run-harder-2026-tight-diesel-supplies-boost-margins-eia-says-2026-10-22/"
U_DPA = "https://www.reuters.com/business/energy/trump-invokes-cold-war-era-defense-production-act-oil-production-refining-2026-10-22/"

def S(d, o, u, nid, t): return {"d": d, "o": o, "u": u, "nid": nid, "t": t}

state = {
 "refining": [
  S("2026-10-30", "블룸버그", U_EX, "n-bbg-0848", "엑손의 3분기 정제이익은 90억 5,000만 달러로 사상 최대였고 셰브런 다운스트림 이익도 49억 달러(전년 11억 달러)로 뛰어, 정제 고리가 사슬에서 가장 큰 이익을 내고 있습니다 [사실]"),
  S("2026-10-31", "블룸버그", U_BASH, "n-tg-0121", "우크라이나가 10월 31일 러시아 바시네프트 정유소를 타격했다는 보도가 나와, 10월 중순 비공식 중단됐던 러시아 정유시설 공습이 다시 이어지고 있습니다 [제목]"),
 ],
 "products": [
  S("2026-10-31", "블룸버그", U_DSL, "n-tg-0121", "러시아는 10월 31일 일부 예외를 두고 대부분의 경유 수출 금지를 1월까지 연장해, 러시아발 경유 공급 회복이 늦어지게 됐습니다 [사실]"),
  S("2026-11-02", "블룸버그", U_REL, "n-bbg-0848", "릴라이언스의 9월 분기 휘발유 크랙은 배럴당 24.9달러(196%↑), 경유 크랙은 65.8달러(252%↑)였고 O2C EBITDA는 약 68% 늘어, 아시아에서도 제품 마진이 크게 벌어졌습니다 [사실]"),
  S("2026-10-30", "블룸버그", U_JP, "n-rtr-0671", "일본은 휘발유 소매가 상한을 매달 리터당 5엔씩 올려 보조금을 줄이기로 해, 휘발유값이 12월 약 175엔, 1월 약 180엔으로 오를 수 있습니다 [사실]"),
 ],
 "transport": [
  S("2026-11-02", "텔레그램 Polaristimes", U_HZ, "n-tg-0688", "UKMTO는 오만 카사브 북동쪽 25해리에서 소형 보트가 유조선 선체에 폭발물 2개를 붙여 기관실 화재가 났다고 밝혔고, 2월 전쟁 이후 이 수법의 첫 성공 사례로 거론됩니다 [채널]"),
  S("2026-11-01", "블룸버그", U_PK, "n-tg-0688", "이란의 승인을 받고 호르무즈 인근을 지나던 파키스탄행 LNG 화물선도 공격받아, 통항 승인이 안전을 보장하지 못한다는 신호가 나왔습니다 [제목]"),
 ],
 "opec": [
  S("2026-11-01", "블룸버그", U_OPEC, "n-bbg-0854", "사우디·러시아 등 OPEC+ 7개 핵심국은 12월에도 9월 생산 목표를 유지해 3개월 연속 쿼터를 동결했습니다 [사실]"),
 ],
 "price": [
  S("2026-11-02", "블룸버그", U_GS, "n-bbg-0854", "골드만삭스는 12월 브렌트 전망을 배럴당 90달러에서 105달러로, 2027년 평균을 88달러로 올렸고, 걸프 생산이 하루 350만 배럴 적게 유지되면 2027년 140달러도 가능하다고 봤습니다 [사실]"),
 ],
 "nonopec": [
  S("2026-10-30", "블룸버그", U_CN, "n-bbg-0856", "CNOOC의 3분기 실현 원유가격은 배럴당 88.03달러로 32.1% 올랐지만 유가 연동 세금·로열티와 가스 판매 7% 감소로 순이익은 2.7% 느는 데 그쳤습니다 [사실]"),
 ],
 "stocks": [
  S("2026-11-02", "텔레그램 Polaristimes", U_POL, "n-bbg-0854", "미국은 트럼프 행정부의 대규모 전략비축유 방출 가운데 마지막 물량을 낙찰해, 미국발 비축유 방출이 마무리 단계에 들어갔습니다 [채널]"),
 ],
 "demand": [
  S("2026-10-23", "로이터", U_ID, "n-rtr-0671", "인도네시아의 보조 연료 소비가 6월 비보조 연료값 인상 뒤 할당량 2,927만 kL보다 약 10% 빠르게 늘어, 에너지부가 추가 쿼터를 검토합니다 [사실]"),
 ],
}

ind = [
 {"d": "2026-11-02", "kind": "price", "o": "블룸버그", "u": U_GS, "nid": "n-bbg-0854",
  "t": "골드만삭스는 12월 브렌트 전망을 배럴당 90달러에서 105달러로, WTI를 94달러로, 2027년 평균을 88달러로 올리고 2027년 기본 시나리오에 하루 100만 배럴 공급 차질을 넣었습니다 [사실]"},
 {"d": "2026-10-31", "kind": "capex", "o": "블룸버그", "u": U_BIG, "nid": "n-bbg-0848",
  "t": "엑손 CEO는 2030년까지 설비투자 1천억 달러를 계획했고 발레로는 휴업한 텍사스 정유소를 재가동하며, 메이저 5사 3분기 조정 순이익 합계는 563억 달러로 역대 세 번째였습니다 [사실]"},
 {"d": "2026-10-30", "kind": "policy", "o": "블룸버그", "u": U_JP, "nid": "n-rtr-0671",
  "t": "일본은 휘발유 소매가 상한을 매달 리터당 5엔씩 올려 보조금을 줄이며, 6월 3.1조 엔 추경이 빠르게 줄어 예비비 1.1조 엔을 추가 배정했습니다 [사실]"},
 {"d": "2026-10-31", "kind": "supply", "o": "블룸버그", "u": U_BASH, "nid": "n-tg-0121",
  "t": "우크라이나는 올해 러시아 정유시설을 최소 114차례 공격해 지난해 같은 기간의 두 배를 넘었고, 로스네프트는 재피격에 복구를 며칠에서 몇 달로 늦추고 있습니다 [사실]"},
]

flags = [
 {"nid": "n-bbg-0848", "t": "재검토 필요: 엑손의 2030년까지 설비투자 1천억 달러 계획과 발레로의 휴업 정유소 재가동은 정제·상류 노드가 ② 자본 유입·증설 국면으로 옮겨 가고 있음을 가리키며, 사상 최대 정제이익이 증설 결정을 앞당기기 때문입니다 [유추]"},
 {"nid": "n-bbg-0854", "t": "재검토 필요: 골드만의 2027년 평균 88달러 전망과 베센트 재무장관의 유가 40달러 가능 발언은 원유 노드의 ③ 공급 과잉 국면을 가리키며, 전쟁 뒤 걸프 증산과 수요 감소가 겹치면 원유가 먼저 남기 때문입니다 [유추]"},
]

insight = {
 "a1": [
  {"t": "정제마진 호황이 정유사 이익을 사상 최대로 끌어올렸습니다. 엑손 정제이익 90억 5,000만 달러, 셰브런 다운스트림 49억 달러, 릴라이언스 O2C EBITDA 약 68% 증가처럼 지역을 가리지 않고 정제 고리가 이익을 가져가고 있습니다 [귀납]",
   "src": [{"o": "블룸버그", "d": "2026-10-30", "u": U_EX}, {"o": "블룸버그", "d": "2026-11-02", "u": U_REL}]},
  {"t": "늘어난 현금은 환원에 먼저 가지만 증설 쪽으로도 번지기 시작했습니다. 셸은 자사주 매입을 50억 달러로 키웠고, 엑손은 2030년까지 설비투자 1천억 달러를 계획했으며 발레로는 휴업한 텍사스 정유소를 재가동합니다 [귀납]",
   "src": [{"o": "블룸버그", "d": "2026-10-31", "u": U_BIG}, {"o": "블룸버그", "d": "2026-10-29", "u": "https://www.bloomberg.com/news/newsletters/2026-10-29/shell-ceo-faces-test-of-turning-a-cash-windfall-into-durable-growth"}]},
  {"t": "정제 고리로 외부 자본도 들어옵니다. 하루 70만 배럴 단고테 정유가 약 16억 3천만 달러 IPO에 90여 개국 청약을 받아, 높은 마진이 정유 자산의 상장·자금 조달로 이어질 가능성이 큽니다 [유추]",
   "src": [{"o": "블룸버그", "d": "2026-10-27", "u": "https://www.bloomberg.com/news/articles/2026-10-27/dangote-refinery-ipo-set-for-record-on-african-global-demand"}]},
 ],
 "c": [
  {"t": "제품 부족을 덜 정보가 이어집니다. 유럽은 3개월간 비축유 4,200만 배럴(약 절반 디젤)을 방출하고 한국은 11월부터 경유 수출 상한을 110%로 올리며, 미국은 대규모 전략비축유 방출의 마지막 물량을 낙찰했습니다 [채널]",
   "src": [{"o": "텔레그램 상상인 김진범", "d": "2026-10-30", "u": "https://t.me/PipeBeom/6925"}, {"o": "텔레그램 트릴리온", "d": "2026-10-29", "u": "https://t.me/Trillion_labs/11379"}, {"o": "텔레그램 Polaristimes", "d": "2026-11-02", "u": U_POL}]},
  {"t": "원유 공급도 돌아옵니다. 사우디의 페르시아만 원유 선적이 전쟁 이후 최고 수준이라는 위성 자료가 나왔고, Kpler 기준 걸프 수출은 10월 18일 주간 하루 2,400만 배럴로 전쟁 전 2,330만 배럴을 넘었다는 전언입니다 [채널]",
   "src": [{"o": "블룸버그", "d": "2026-10-30", "u": "https://www.bloomberg.com/news/articles/2026-10-29/satellites-show-saudi-persian-gulf-oil-loadings-hit-wartime-high"}, {"o": "텔레그램 미국 주식 인사이더", "d": "2026-10-23", "u": "https://t.me/insidertracking/67117"}]},
  {"t": "가격 쪽에서도 반대 의견이 나옵니다. 골드만은 12월 105달러를 보면서도 2027년 평균을 88달러로 잡았고, 베센트 재무장관은 이란 전쟁 뒤 증산으로 유가가 40달러까지 떨어질 수 있다고 주장했다는 전언입니다 [채널]",
   "src": [{"o": "블룸버그", "d": "2026-11-02", "u": U_GS}, {"o": "텔레그램 Polaristimes", "d": "2026-11-02", "u": U_POL}]},
 ],
}

cycle = {
 "stage": 1, "conf": "중간",
 "why": [
  {"t": "국면은 ① 그대로이고 근거를 새 뉴스로 바꿨습니다. 정제 고리가 한계까지 돌고 있습니다. EIA는 미국 정유 가동률이 5~9월 평균 95%를 넘어 같은 기간 1998년 이후 최고였고 9월 말 중간유분 재고는 5년 평균보다 약 13% 적었다고 했습니다 [사실]",
   "src": [{"o": "로이터", "d": "2026-10-23", "u": U_EIA}]},
  {"t": "사슬 중간의 이익이 사상 최대입니다. 엑손 3분기 정제이익은 90억 5,000만 달러, 셰브런 다운스트림 이익은 49억 달러로 모두 사상 최대였고, 릴라이언스 경유 크랙은 배럴당 65.8달러(252%↑)였습니다 [사실]",
   "src": [{"o": "블룸버그", "d": "2026-10-30", "u": U_EX}, {"o": "블룸버그", "d": "2026-11-02", "u": U_REL}]},
  {"t": "가격 전망도 위로 고쳐지고 있습니다. 브렌트는 10월 23일 장중 114.72달러로 5월 이후 최고였고, 골드만삭스는 12월 브렌트 전망을 90달러에서 105달러로 올리며 상방 140달러를 제시했습니다 [사실]",
   "src": [{"o": "텔레그램 Polaristimes", "d": "2026-10-23", "u": "https://t.me/The_MariTimes/63945"}, {"o": "블룸버그", "d": "2026-11-02", "u": U_GS}]},
  {"t": "자본 유입은 아직 계획과 정책 단계입니다. 국방물자생산법으로 탐사·생산·파이프라인·저장에 정부 대출·보증이 열렸고 엑손은 2030년까지 1천억 달러 설비투자를 계획했지만, 메이저 현금은 자사주 매입에 먼저 쓰이고 있습니다 [귀납]",
   "src": [{"o": "로이터", "d": "2026-10-22", "u": U_DPA}, {"o": "블룸버그", "d": "2026-10-31", "u": U_BIG}]},
 ],
 "next": "호르무즈 원유 물량 회복에 이어 제품 통항과 미국 중간유분 재고가 다시 쌓이기 시작하면 운임·마진·유가가 함께 내려 ③ 공급 과잉으로 넘어갈 수 있습니다. 반대로 엑손의 설비투자 계획, 국방물자생산법 자금, 정유소 재가동·신규 발주가 실제 착공·계약으로 이어지면 ② 자본 유입·증설로 진행합니다 [유추]",
 "watch": [
  "미국 상업용 원유·중간유분 재고(EIA 주간)",
  "호르무즈 통항량·걸프 제품 수출(Kpler)",
  "유럽·아시아 경유 크랙과 우크라이나의 러시아 정유시설 공습",
  "메이저 설비투자 집행·정유소 재가동과 국방물자생산법 대출·보증",
  "11월 3일 미 선거 뒤 이란 공습 재개 여부",
 ],
 "split": [],
}

summary = ("원유·석유제품 산업은 OPEC+·미국 셰일 같은 생산자가 뽑은 원유를 유조선·송유관으로 정유공장에 보내 경유·휘발유·항공유 같은 제품으로 바꿔 운송·항공·산업 수요에 파는 사슬이며, 재고·전략비축유가 그 사이를 완충합니다. "
 "지금 가장 빠듯한 고리는 여전히 정제와 제품입니다. 엑손 정제이익(90억 5,000만 달러)과 셰브런 다운스트림 이익(49억 달러)이 사상 최대였고 릴라이언스 경유 크랙은 배럴당 65.8달러였으며, 우크라이나가 러시아 정유시설 공습을 다시 시작하고 러시아는 경유 수출 금지를 1월까지 늘렸습니다. "
 "수송 고리도 긴장이 이어져 호르무즈에서는 부착 폭발물 공격과 이란 승인 LNG선 피격이 나왔습니다. "
 "남는 쪽의 신호도 있습니다. OPEC+는 쿼터를 3개월째 묶었고 미국은 비축유 방출 마지막 물량을 낙찰했으며, 골드만은 12월 105달러를 보면서도 2027년 평균은 88달러로 잡았습니다.")

gaps = old["gaps"] + (" (11) 11월 2일 저녁 업데이트도 검색·열람 없이 입력 뉴스 9건만으로 반영했습니다. 노보쿠이비셰프스크 정유소 재타격과 로스네프트 복구 중단은 채널 전언이고, 바시네프트 정유소 타격은 기사 제목 수준이라 피해 규모를 확인하지 못했습니다. "
 "부착 폭발물 공격과 미국 전략비축유 마지막 물량 낙찰은 채널 전언이며 낙찰 물량은 확인하지 못했습니다. 베센트 재무장관의 유가 40달러 발언은 채널 전언입니다. 파키스탄행 LNG선 피격은 기사 제목뿐이라 피해를 확인하지 못했습니다. "
 "엑손의 1천억 달러 설비투자 가운데 정제 몫과 발레로 재가동 정유소의 능력은 입력에 없습니다.")

ids = [json.loads(l)['id'] for l in open(f'{B}/data/industry-2026-11-02-pm/news/oil.jsonl')]
out = {"id": "oil", "summary": summary, "state": state, "industryState": ind, "flags": flags, "insight": insight,
       "cycle": cycle, "nodeStage": {}, "gaps": gaps,
       "note": "뉴스 9건 반영: 엑손 정제이익 90억 5,000만 달러 사상 최대·릴라이언스 경유 크랙 65.8달러, 골드만 12월 브렌트 105달러 상향·OPEC+ 쿼터 3개월째 동결, 우크라 러 정유시설 공습 재개·러 경유 수출 금지 1월 연장. 국면 ① 그대로(근거 교체), 근거 12줄, 수치 4줄, 인사이트 a1·c 고침, 재검토 신호 2건, 검색 0회",
       "applied": ids, "searches": 0, "fetches": 0}
json.dump(out, open(f'{B}/data/industry-2026-11-02-pm/out/oil.json', 'w'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in state.values()))
