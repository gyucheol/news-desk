import json
B = '/home/user/news-desk'
old = json.load(open(f'{B}/work/nightly-2026-11-02/chains/gas.json'))
U_JP2 = "https://www.bloomberg.com/news/articles/2026-11-02/tokyo-chubu-power-price-hit-multi-year-high-as-fuel-costs-climb"
U_JP1 = "https://www.bloomberg.com/news/articles/2026-10-19/japan-power-price-at-four-year-high-with-rising-coal-lng-costs"
U_HF = "https://www.bloomberg.com/news/articles/2026-10-30/hedge-funds-boost-natural-gas-short-positions-to-most-on-record"
U_DR = "https://www.bloomberg.com/news/newsletters/2026-10-30/us-natural-gas-drillers-scale-up-as-demand-grows"
U_RV = "https://www.bloomberg.com/news/articles/2026-10-30/exxon-increases-stake-in-mozambique-gas-project-via-eni-swap"
U_PK = "https://www.bloomberg.com/news/articles/2026-11-01/pakistan-lng-cargo-attacked-near-hormuz-had-iranian-approval"
U_TTF = "https://t.me/Trillion_labs/11467"
U_DE = "https://www.bloomberg.com/news/articles/2026-11-01/germany-misses-gas-storage-target-as-cold-snap-sets-in"
U_RU = "https://www.bloomberg.com/news/articles/2026-11-02/us-pushes-for-russia-to-resume-gas-sales-to-europe-wsj-reports"
U_ND = "https://t.me/Trillion_labs/11447"

def S(d, o, u, nid, t): return {"d": d, "o": o, "u": u, "nid": nid, "t": t}

state = {
 "upstream": [
  S("2026-10-31", "블룸버그", U_HF, "n-bbg-0855", "헤지펀드의 헨리허브 숏 포지션이 62만 5,150계약으로 2013년 집계 이래 최대였고, 포근한 겨울 예보에 미국 천연가스 선물은 한 주 새 15% 넘게 내렸습니다 [사실]"),
  S("2026-10-30", "블룸버그", U_DR, "n-bbg-0855", "미국 가스 시추업체들이 수요 증가에 맞춰 생산을 늘리고 있다는 분석이 나와, 수출 능력에 막힌 원산지 공급이 더 쌓일 수 있습니다 [제목]"),
 ],
 "liquefaction": [
  S("2026-10-30", "블룸버그", U_RV, "n-bbg-0860", "엑손모빌은 에니와의 자산 스왑으로 약 300억 달러, 연 1,860만 톤 규모 모잠비크 로부마 LNG 지분을 50%로 늘렸고, 2026년 말 FID와 2031년 첫 생산을 목표로 합니다 [사실]"),
  S("2026-10-30", "텔레그램 트릴리온", U_ND, "n-tg-0810", "넥스트디케이드 리오그란데 1·2호기 공정률은 합쳐 79.7%, 3호기 55.2%이며 올해 말 1호기 첫 가스와 2027년 2분기 첫 생산이 예상된다는 전언입니다 [채널]"),
 ],
 "shipping": [
  S("2026-11-01", "블룸버그", U_PK, "n-tg-0688", "이란의 승인을 받고 호르무즈 인근을 지나던 파키스탄행 LNG 화물선이 공격받아, 통항 승인을 받은 LNG선도 안전하지 않다는 신호가 나왔습니다 [제목]"),
 ],
 "regas": [
  S("2026-11-01", "블룸버그", U_DE, "n-tg-0761", "독일 가스 저장률은 61.7%로 11월 1일 법정 목표에 못 미쳤고 이탈리아는 거의 91%였으며, 3억 유로를 쓴 이탈리아는 가격 급등을 독일 탓으로 돌렸습니다 [사실]"),
 ],
 "trade": [
  S("2026-10-30", "텔레그램 트릴리온", U_TTF, "n-tg-0761", "유럽 TTF 가스값이 10월 28일 MWh당 100유로로 2022년 12월 이후 처음 100유로를 넘었고, 30일에도 트럼프의 이란 옵션 검토 속에 100유로 위로 올랐다는 전언입니다 [채널]"),
  S("2026-11-02", "블룸버그", U_RU, "n-tg-0761", "WSJ 보도로 미국이 우크라이나 경유 러시아 가스의 유럽 판매 재개를 압박하고 있다고 전해져, 외교가 유럽 공급을 바꿀 변수로 다시 떠올랐습니다 [제목]"),
 ],
 "demand": [
  S("2026-11-02", "블룸버그", U_JP2, "n-bbg-0413", "연료비 상승에 도쿄·주부 지역 전력값이 수년 만의 최고를 기록해, LNG·석탄값 상승이 일본 발전 비용으로 옮겨 가고 있습니다 [제목]"),
 ],
}

ind = [
 {"d": "2026-10-31", "kind": "price", "o": "블룸버그", "u": U_HF, "nid": "n-bbg-0855",
  "t": "헤지펀드의 헨리허브 숏 포지션은 62만 5,150계약으로 1주 전 기록(59만 9,731계약)을 넘었고 순매도는 22만 3,591계약으로 2020년 2월 이후 최대였습니다 [사실]"},
 {"d": "2026-10-30", "kind": "price", "o": "텔레그램 트릴리온", "u": U_TTF, "nid": "n-tg-0761",
  "t": "유럽 TTF는 10월 28일 MWh당 100유로로 2022년 12월 이후 최고였고, 이탈리아 노체 국장은 1월이 추우면 150~180유로까지 오를 수 있다고 봤다는 전언입니다 [채널]"},
 {"d": "2026-11-01", "kind": "supply", "o": "블룸버그", "u": U_DE, "nid": "n-tg-0761",
  "t": "독일 가스 저장률은 61.7%로 11월 1일 법정 목표에 못 미쳤고, EU 전체는 10월 24일 74.6%로 1년 전 82.9%보다 낮았습니다 [사실]"},
 {"d": "2026-10-30", "kind": "capex", "o": "블룸버그", "u": U_RV, "nid": "n-bbg-0860",
  "t": "엑손은 약 300억 달러, 연 1,860만 톤 규모 로부마 LNG 지분을 50%로 늘리고 파푸아 LNG 지분도 34%로 높이기로 했습니다 [사실]"},
]

flags = [
 {"nid": "n-bbg-0855", "t": "재검토 필요: 헨리허브 숏 포지션 사상 최대와 미국 시추업체 증산은 원산지 쪽이 ③ 공급 과잉 국면에 더 깊이 들어가고 있음을 가리키며, 액화 증설보다 생산이 먼저 늘면 미국 가격이 더 눌리기 때문입니다 [유추]"},
]

a1o = old['insight']['a1']; co = old['insight']['c']
insight = {
 "a1": [
  {"t": a1o[0]['t'], "src": a1o[0]['src']},
  {"t": a1o[1]['t'], "src": a1o[1]['src']},
  {"t": "2030년대 공급 후보가 더 늘었습니다. 알래스카 LNG와 탄자니아 420억 달러 협정, YPF 연 1,200만 톤 사업에 더해 엑손이 연 1,860만 톤 로부마 LNG 지분을 50%로 늘려 2026년 말 FID를 노립니다. 과잉이 오면 그 폭이 커질 가능성이 큽니다 [유추]",
   "src": a1o[2]['src'][:2] + [{"o": "블룸버그", "d": "2026-10-30", "u": U_RV}]},
 ],
 "c": [
  {"t": co[0]['t'], "src": co[0]['src']},
  {"t": co[1]['t'], "src": co[1]['src']},
  {"t": "당장의 부족은 더 깊어졌습니다. 독일 저장률은 61.7%로 11월 1일 법정 목표에 못 미쳤고, TTF는 10월 28일 MWh당 100유로로 2022년 12월 이후 최고였으며, 우드맥켄지는 3월 말 유럽 저장률이 17~20%까지 낮아질 수 있다고 봤다는 전언입니다 [채널]",
   "src": [{"o": "블룸버그", "d": "2026-11-01", "u": U_DE}, {"o": "텔레그램 트릴리온", "d": "2026-10-30", "u": U_TTF}]},
 ],
}

wo = old['cycle']['why']
cycle = {
 "stage": 2, "conf": "중간",
 "why": [
  {"t": wo[0]['t'], "src": wo[0]['src']},
  {"t": "증설 자본이 계속 들어옵니다. LNG캐나다 2단계(연 1,400만 톤)가 확정됐고, 엑손은 연 1,860만 톤 로부마 LNG 지분을 50%로 늘려 2026년 말 FID를 노리며, 넥스트디케이드 1호기는 올해 말 첫 가스를 앞뒀습니다 [사실]",
   "src": [wo[1]['src'][0], {"o": "블룸버그", "d": "2026-10-30", "u": U_RV}]},
  {"t": "지금 가격이 높은 것은 카타르 트레인 손상과 호르무즈 차질 때문입니다. TTF는 10월 28일 MWh당 100유로로 2022년 12월 이후 최고였고 독일 저장률은 61.7%로 법정 목표에 못 미쳐, 구조적 부족보다 사건이 만든 부족에 가깝습니다 [유추]",
   "src": [{"o": "텔레그램 트릴리온", "d": "2026-10-30", "u": U_TTF}, {"o": "블룸버그", "d": "2026-11-01", "u": U_DE}]},
  {"t": "출구(액화)가 막힌 미국 원산지는 이미 남는 쪽입니다. 포근한 겨울 예보에 미국 가스 선물은 한 주 새 15% 넘게 내렸고 헤지펀드 숏 포지션은 사상 최대였으며, EIA는 헨리허브가 2027년 3.28달러로 내려갈 것으로 봅니다 [사실]",
   "src": [{"o": "블룸버그", "d": "2026-10-31", "u": U_HF}, wo[3]['src'][0]]},
 ],
 "next": old['cycle']['next'],
 "watch": old['cycle']['watch'],
 "split": [],
}

summary = ("천연가스 사슬은 가스를 뽑는 상류와 가스관, 액화·수송·재기화, 거래, 수요로 이어지며, 미국 가스는 증산에도 액화·수출 능력에 막혀 헨리허브가 낮게 묶이고 해외 가격(TTF·JKM)과 큰 격차가 납니다. "
 "가장 빠듯한 곳은 유럽 저장과 수송로로, 독일 저장률은 61.7%로 11월 1일 법정 목표에 못 미쳤고 TTF는 10월 28일 MWh당 100유로로 2022년 12월 이후 최고였다는 전언입니다. 호르무즈에서는 이란 승인을 받은 파키스탄행 LNG선까지 공격받았습니다. "
 "반대로 미국 원산지는 더 남는 쪽으로 가, 포근한 겨울 예보에 미국 가스 선물이 한 주 새 15% 넘게 내렸고 헤지펀드 숏 포지션은 사상 최대입니다. "
 "그 사이 카타르의 미국산 장기 구매, 엑손의 로부마 LNG 지분 확대(연 1,860만 톤), 넥스트디케이드 1호기 연말 첫 가스처럼 액화 증설은 계속 이어집니다.")

gaps = old["gaps"] + (" 11월 2일 저녁 업데이트도 검색·열람 없이 입력 뉴스 7건으로만 반영했습니다. TTF 100유로 돌파, 노체 국장의 150~180유로 전망, 우드맥켄지의 3월 말 저장률 17~20%, 프랑스 전력 200유로 돌파는 채널 전언입니다. "
 "미국의 러시아 가스 유럽 판매 재개 압박은 WSJ 보도를 다룬 기사 제목 수준이고, 파키스탄행 LNG선 피격의 피해와 도쿄·주부 전력값 수치, 미국 시추업체 증산 규모는 확인하지 못했습니다. 넥스트디케이드 공정률은 채널 전언입니다.")

ids = [json.loads(l)['id'] for l in open(f'{B}/data/industry-2026-11-02-pm/news/gas.jsonl')]
out = {"id": "gas", "summary": summary, "state": state, "industryState": ind, "flags": flags, "insight": insight,
       "cycle": cycle, "nodeStage": {}, "gaps": gaps,
       "note": "뉴스 7건 반영: TTF 100유로 돌파·독일 저장 61.7% 법정 목표 미달, 헨리허브 숏 포지션 사상 최대·미 가스 선물 주간 15% 하락, 엑손 로부마 LNG 지분 50%. 국면 ② 그대로(근거 교체), 근거 10줄, 수치 4줄, 인사이트 a1·c 고침, 재검토 신호 1건, 검색 0회",
       "applied": ids, "searches": 0, "fetches": 0}
json.dump(out, open(f'{B}/data/industry-2026-11-02-pm/out/gas.json', 'w'), ensure_ascii=False, indent=1)
