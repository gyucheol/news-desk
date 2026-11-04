import json
B = '/home/user/news-desk'
old = json.load(open(f'{B}/work/nightly-2026-11-02/chains/metals.json'))
U_OT = "https://www.bloomberg.com/news/articles/2026-10-29/rio-tinto-s-oyu-tolgoi-mine-suspended-underground-operations"
U_CL = "https://www.bloomberg.com/news/articles/2026-10-30/chile-copper-mines-deliver-worst-quarter-in-at-least-two-decades"
U_AU = "https://www.bloomberg.com/news/articles/2026-11-02/gold-climbs-back-from-one-year-low-as-dip-buyers-arrest-slide"
U_AU_TG = "https://t.me/The_MariTimes/64165"
U_RE_CN = "https://www.bloomberg.com/news/articles/2026-10-31/china-metals-gold-nickel-rhenium-reserves-xinhua-strategic-resources"
U_DTEC = "https://t.me/The_MariTimes/64152"
U_FR = "https://www.bloomberg.com/news/articles/2026-11-01/billionaire-friedland-to-build-major-us-backed-rare-earths-mine"
U_ST = "https://www.bloomberg.com/news/articles/2026-11-02/chinese-steel-group-chides-mills-for-ignoring-output-curb-calls"
U_CITI = "https://www.bloomberg.com/news/articles/2026-11-02/citi-cuts-lithium-forecasts-on-worsening-battery-demand-outlook"
U_CU = "https://www.bloomberg.com/news/articles/2026-10-30/copper-declines-as-tech-selloff-oil-rally-dent-risk-appetite"

def S(d, o, u, nid, t): return {"d": d, "o": o, "u": u, "nid": nid, "t": t}

state = {
 "copper": [
  S("2026-10-29", "블룸버그", U_OT, "n-bbg-0610", "리오틴토는 10월 29일 단층대 진동으로 직원 3명이 다친 뒤 몽골 오유톨고이 지하 작업을 멈췄고 재개 시점을 밝히지 않아, 구리 광산 차질이 칠레 밖으로 번졌습니다 [사실]"),
  S("2026-10-30", "블룸버그", U_CL, "n-bbg-0610", "칠레 9월 구리 생산은 15.1% 줄어 1~9월 생산이 366만 톤(8.6%↓)이었고, 3분기는 적어도 20여 년 만의 최악 분기였습니다 [사실]"),
 ],
 "precious": [
  S("2026-10-30", "블룸버그", U_AU, "n-bbg-0701", "금 현물은 10월 30일 3.6% 내린 온스당 약 3,876달러로 약 1년 만의 최저였고, 4,000달러 아래로 밀린 뒤 11월 2일 저가 매수에 반등했습니다 [사실]"),
  S("2026-11-02", "텔레그램 Polaristimes", U_AU_TG, "n-bbg-0701", "선전 슈이베이 금시장에 귀금속 구매 인파가 몰렸고 중국 은행들은 금 적립계좌 수수료를 일부 0%까지 낮췄다는 전언입니다 [채널]"),
 ],
 "critical": [
  S("2026-11-01", "텔레그램 Polaristimes", U_DTEC, "n-bbg-0851", "미국 지분 51%의 DTEC이 6억 달러를 들여 3년 안에 말레이시아에 연 5,000톤 규모 희토류 정제소를 짓겠다고 했고, 희토류 탄산염 최대 700톤 수출 허가도 받았습니다 [사실]"),
  S("2026-11-02", "블룸버그", U_FR, "n-bbg-0851", "억만장자 프리들랜드가 미국 정부 지원을 받는 대형 희토류 광산을 짓는다는 보도가 나와, 중국 밖 희토류 사슬에 자본이 계속 들어옵니다 [제목]"),
 ],
 "steel": [
  S("2026-11-02", "블룸버그", U_ST, "n-bbg-0892", "중국철강협회가 감산 요구를 무시한 제철소들을 공개 질타해, 9월 45개 철강그룹과 낸 목표·강제 수단 없는 자율 감산 촉구가 지켜지지 않고 있습니다 [제목]"),
 ],
 "battery": [
  S("2026-11-02", "블룸버그", U_CITI, "n-tg-0766", "씨티는 배터리 수요 둔화를 들어 3개월 탄산리튬 전망을 톤당 2만 달러에서 1.2만 달러로, 스포듀민을 2,000달러에서 1,200달러로 낮추고 구매자들이 구매를 미룰 수 있다고 봤습니다 [사실]"),
 ],
}

ind = [
 {"d": "2026-10-30", "kind": "supply", "o": "블룸버그", "u": U_CL, "nid": "n-bbg-0610",
  "t": "칠레 9월 구리 생산은 15.1% 줄었고 1~9월 생산은 366만 톤으로 8.6% 줄었으며, 앵글로 3분기 구리 생산도 17만 4,900톤으로 5% 줄었습니다 [사실]"},
 {"d": "2026-10-30", "kind": "price", "o": "블룸버그", "u": U_AU, "nid": "n-bbg-0701",
  "t": "금 현물은 10월 30일 3.6% 내린 온스당 약 3,876달러로 약 1년 만의 최저에 마감했고, 12월 금리 인상 확률은 약 75~90%로 반영됐습니다 [사실]"},
 {"d": "2026-11-02", "kind": "price", "o": "블룸버그", "u": U_CITI, "nid": "n-tg-0766",
  "t": "씨티는 3개월 탄산리튬 전망을 톤당 2만 달러에서 1.2만 달러로, 수산화리튬을 1.7만 달러에서 1.2만 달러로, 스포듀민을 2,000달러에서 1,200달러로 내렸습니다 [사실]"},
 {"d": "2026-11-01", "kind": "capex", "o": "텔레그램 Polaristimes", "u": U_DTEC, "nid": "n-bbg-0851",
  "t": "DTEC의 말레이시아 희토류 정제소는 6억 달러 규모로 1단계 연 5,000톤, 최종 2곳 1만 톤이며 3년 안에 완공할 계획입니다 [사실]"},
]

flags = [
 {"nid": "n-bbg-0701", "t": "재검토 필요: 금이 온스당 약 3,876달러로 1년 최저까지 내린 것은 귀금속 노드가 ① 호황에서 ③ 공급 과잉·조정 쪽으로 옮겨 갈 수 있음을 가리키며, 금리 인상 베팅과 투기 포지션 청산이 가격을 끌어내리기 때문입니다 [유추]"},
]

bo = old['insight']['b']; co = old['insight']['c']; ao = old['insight']['a2']
insight = {
 "b": [
  {"t": "구리는 광산 생산 자체가 줄고 있습니다. 칠레 9월 생산이 15.1% 줄어 3분기가 적어도 20여 년 만의 최악이었고, BHP 7~9월 생산은 19%, 앵글로 3분기 생산은 5% 줄었으며, 리오틴토는 몽골 오유톨고이 지하 작업을 멈췄습니다 [사실]",
   "src": [{"o": "블룸버그", "d": "2026-10-30", "u": U_CL}, bo[0]['src'][0], {"o": "블룸버그", "d": "2026-10-29", "u": U_OT}]},
  {"t": bo[1]['t'], "src": bo[1]['src']},
  {"t": bo[2]['t'], "src": bo[2]['src']},
 ],
 "c": [
  {"t": co[0]['t'], "src": co[0]['src']},
  {"t": "금은 12월 금리 인상 베팅과 증거금 마련 매도에 10월 30일 온스당 약 3,876달러로 약 1년 만의 최저까지 내렸고, 상상인증권은 귀금속값 하락 등으로 고려아연 3분기 영업이익이 46.7% 줄 것으로 봤습니다 [귀납]",
   "src": [{"o": "블룸버그", "d": "2026-11-02", "u": U_AU}, co[1]['src'][2]]},
  {"t": co[2]['t'], "src": co[2]['src']},
 ],
 "a2": [
  {"t": ao[0]['t'], "src": ao[0]['src']},
  {"t": "대형 광산사의 증설과 수요 둔화가 가격 회복을 늦출 수 있습니다. 리오틴토가 아르헨티나 리튬에서 연 2.5만 톤을 더하는 사이, 씨티는 배터리 수요 둔화로 3개월 탄산리튬 전망을 톤당 1.2만 달러로 낮췄습니다 [유추]",
   "src": [ao[1]['src'][0], {"o": "블룸버그", "d": "2026-11-02", "u": U_CITI}]},
 ],
}

wo = old['cycle']['why']
cycle = {
 "stage": 2, "conf": "중간",
 "why": [
  {"t": "국면은 ② 그대로이고 구리 근거를 새 뉴스로 바꿨습니다. 구리 광산은 계속 빠듯합니다. 칠레 9월 생산이 15.1% 줄어 3분기가 적어도 20여 년 만의 최악이었고, 리오틴토는 오유톨고이 지하 작업을 멈췄으며, 정광 TC 지수는 10월 9일 -272.20달러였습니다 [사실]",
   "src": [{"o": "블룸버그", "d": "2026-10-30", "u": U_CL}, {"o": "블룸버그", "d": "2026-10-29", "u": U_OT}, wo[0]['src'][2]]},
  {"t": "신규 진입자와 국가 자금이 핵심광물로 몰립니다. EU 전략사업 46곳(약 211억 유로)과 세계은행 핵심광물 금융 5배 목표에 이어, 미국계 DTEC이 6억 달러 말레이시아 희토류 정제소를 짓고 프리들랜드가 미국 정부 지원 희토류 광산을 추진합니다 [귀납]",
   "src": [wo[1]['src'][0], wo[1]['src'][2], {"o": "텔레그램 Polaristimes", "d": "2026-11-01", "u": U_DTEC}, {"o": "블룸버그", "d": "2026-11-02", "u": U_FR}]},
  {"t": wo[2]['t'], "src": wo[2]['src']},
  {"t": wo[3]['t'], "src": wo[3]['src']},
 ],
 "next": old['cycle']['next'],
 "watch": old['cycle']['watch'],
 "split": old['cycle']['split'],
}

summary = ("금속·광물 산업은 광산에서 철광석·구리·리튬·금 같은 광석을 캐 제련·정련을 거쳐 철강·전기동·알루미늄·배터리 소재로 만들고 건설·전력망·자동차·배터리 업체에 파는 사슬이며, 가격은 거래소와 가격 지수가, 공급은 광산 리드타임과 자원국 정책이 정합니다. "
 "가장 빠듯한 곳은 여전히 구리 광산입니다. 칠레 9월 생산이 15.1% 줄어 3분기가 적어도 20여 년 만의 최악이었고 리오틴토는 오유톨고이 지하 작업을 멈췄으며, 정광 TC가 마이너스 300달러대라 중국 제련소들은 감산에 들어갔다는 전언입니다. "
 "다만 LME·COMEX 창고 재고의 약 90%가 미국에 있어 정련동은 미국에 남는 구조이고, 맥쿼리는 구리값이 공급 여건을 넘어섰다고 봤습니다. "
 "철강은 중국철강협회의 감산 요구가 지켜지지 않을 만큼 남고, 씨티는 배터리 수요 둔화로 탄산리튬 3개월 전망을 톤당 1.2만 달러로 낮췄습니다. 금은 10월 30일 약 3,876달러로 1년 최저까지 내린 뒤 저가 매수에 반등했습니다.")

gaps = old["gaps"] + (" 11월 2일 저녁 업데이트도 검색·열람 없이 입력 뉴스 6건만으로 반영했습니다. 오유톨고이 지하 작업 재개 시점과 생산 영향, 프리들랜드 희토류 광산의 위치·규모·지원 방식은 확인하지 못했고(후자는 기사 제목뿐), DTEC 정제소의 미 수출입은행 최대 6억 5,000만 달러 지원은 공식 확인되지 않았습니다. "
 "중국철강협회가 질타한 제철소 이름과 감산 실적, 중국 레늄 매장량 상향 수치의 근거는 기사 제목·채널 수준이며, 중국 금 구매 인파와 은행 수수료 인하는 채널 전언입니다.")

ids = [json.loads(l)['id'] for l in open(f'{B}/data/industry-2026-11-02-pm/news/metals.jsonl')]
out = {"id": "metals", "summary": summary, "state": state, "industryState": ind, "flags": flags, "insight": insight,
       "cycle": cycle, "nodeStage": {}, "gaps": gaps,
       "note": "뉴스 6건 반영: 칠레 3분기 20여 년 만의 최악 구리 생산·오유톨고이 지하 중단, 금 1년 최저 3,876달러 뒤 반등, 씨티 탄산리튬 전망 1.2만 달러로 하향·DTEC 말레이 희토류 정제소 6억 달러. 국면 ② 그대로(근거 교체), 근거 8줄, 수치 4줄, 인사이트 a2·b·c 고침, 재검토 신호 1건, 검색 0회",
       "applied": ids, "searches": 0, "fetches": 0}
json.dump(out, open(f'{B}/data/industry-2026-11-02-pm/out/metals.json', 'w'), ensure_ascii=False, indent=1)
