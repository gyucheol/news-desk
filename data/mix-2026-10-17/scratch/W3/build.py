import json, re, sys

OUT = "/home/user/news-desk/data/mix-2026-10-17/out2/W3.json"

def it(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s is not None:
        x["s"] = s
    return x

B = "블룸버그"; R = "로이터"

items = []

# G1-003
items.append({
 "cid": "G1-003", "attachTo": "n-bbg-0230",
 "title": "트럼프, 그레이엄법 대러 제재·관세 유예…러 경유 거래에 의회 반발 확산",
 "one": "트럼프 대통령이 러시아산 경유 거래에 이어 그레이엄법의 대러 제재·관세 다수를 시행 직전 유예하면서, 의회에서 거래 저지 법안과 면허 철회 요구가 나오는 등 반발이 커지는 가운데 러시아 경유의 세계 시장 공급은 이어질 전망이다",
 "facts": [
  "무엇이: 트럼프 대통령은 10월 16일 지난달 서명한 그레이엄 대러·대이란 제재법의 제재·제한·관세 다수를 시행 직전 유예하고, 국익에 맞는다는 확인서를 의회에 냈다 [사실]",
  "관세: 유예 대상에는 러시아 원유 상위 5개 구매국의 모든 상품에 최대 100%까지 붙을 수 있던 관세가 들어 있고, 관세를 형식상 부과하되 시행을 미뤄 나중에 적용할 여지를 뒀다는 보도가 나왔다 [사실]",
  "의회: 하원의원 22명이 러시아산 경유 거래를 허용한 일반면허 135호 철회를 요구했고, 틸리스 공화당 상원의원은 법을 따르지 않는다는 주장에 일리가 있다고 했으며, 베선트 재무장관은 기존 법적 권한으로 거래를 이행하겠다고 했다 [사실]",
  "시장: 의회에 거래 저지 법안이 상정됐다는 소식에 브렌트유가 107달러를 되찾았다는 전언이 나왔다 [채널]",
  "기존: 러시아는 10월 10일부터 경유 수출 금지를 일부 풀어 프리모르스크항 선적을 재개했고, 골드만삭스는 초기 물량의 경유 도매가 하락 효과를 배럴당 1~2달러로 추정했다 [사실]"
 ],
 "basis": "verified",
 "check": "그레이엄법 유예·관세 처리·하원의원 22명 서한·틸리스·베선트 발언은 검색 결과 요약으로 확인. 10월 초 러시아 연료 수출 감소, 드미트리예프의 결제 협력, 젤렌스키 비판은 제목 기준, 트럼프의 경유 수출 상한 발언과 브렌트 107달러는 채널 전언",
 "src": [
  {"o": "백악관", "d": "2026-10-16", "u": "https://www.whitehouse.gov/presidential-actions/2026/10/implementing-the-lindsey-o-graham-sanctioning-russia-and-iran-act-of-2026/"},
  {"o": "Business Standard", "d": "2026-10-17", "u": "https://www.business-standard.com/world-news/trump-waives-russia-energy-tariffs-and-sanctions-under-graham-law-126101700093_1.html"},
  {"o": "Fox Business", "d": "2026-10-16", "u": "https://www.foxbusiness.com/politics/trump-waives-many-russian-sanctions-under-new-law-backed-lindsey-graham"},
  {"o": "Newsweek", "d": "2026-10-16", "u": "https://www.newsweek.com/trump-russia-diesel-deal-lindsey-graham-sanctions-law-12574804"}
 ],
 "inds": ["oil", "macro"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "oil", "node": "policy", "f": "공급", "dir": "up", "k": "실제", "t": "그레이엄법 대러 에너지 제재·관세 유예"},
  {"ind": "oil", "node": "products", "f": "공급", "dir": "up", "k": "예상", "t": "러시아 경유 세계 시장 공급 지속 전망"}
 ],
 "added": "이번 블룸버그·로이터 6건과 텔레그램 2건으로 트럼프의 그레이엄법 대러 제재·관세 유예와 의회의 경유 거래 저지 법안, 젤렌스키의 거래 비판이 추가됐다",
 "items": [
  it("러시아 연료 수출, 경유 금지 완화 전인 10월 초 감소", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/russian-fuel-flows-fell-in-early-october-before-diesel-ban-eased",
     "러시아의 연료 수출 물량이 경유 수출 금지가 풀리기 전인 10월 초 줄어들면서, 완화 전까지 세계 시장의 러시아산 연료 공급이 위축됐다 (제목 기준)"),
  it("트럼프 '러 경유 거래는 세계·농민 위한 것…미 경유 수출 상한도 가능'", "텔레그램 Polaristimes", "2026-10-17", "https://t.me/The_MariTimes/63760",
     "트럼프 대통령이 러시아 경유 거래는 자신이 아닌 세계와 미국 농민·목장주를 위한 것이라며, 미국 경유 수출에 상한을 둘 수도 있다고 말해 수출 제한 가능성을 열어뒀다"),
  it("미 의회, 트럼프 러 경유 거래 저지 법안 상정…브렌트 107달러", "텔레그램 Polaristimes", "2026-10-17", "https://t.me/The_MariTimes/63763",
     "미 의회에 공화당 1명과 민주당 다수가 참여한 러시아 경유 거래 저지 법안이 상정되면서, 유가 상승폭이 커져 브렌트유가 107달러를 되찾았다"),
  it("드미트리예프 '러 국부펀드, 경유 거래 대금 결제에 미국과 협력'", R, "2026-10-17", "https://www.reuters.com/world/dmitriev-says-russian-wealth-fund-will-work-with-us-payment-diesel-deal-2026-10-16/",
     "러시아 국부펀드 수장 드미트리예프가 경유 거래 대금 결제에서 미국과 협력하겠다고 밝히면서, 거래의 결제 경로가 마련되고 있다 (제목 기준)"),
  it("트럼프 경유 거래, 의회에서 새 입법 도전 직면", B, "2026-10-17", "https://www.bloomberg.com/news/articles/2026-10-16/trump-diesel-deal-faces-fresh-legislative-challenge-in-congress",
     "트럼프 대통령의 러시아 경유 거래가 의회의 새 입법 도전에 부딪히면서, 하원의원 22명의 일반면허 135호 철회 요구 등 거래 유지의 정치적 부담이 커졌다"),
  it("젤렌스키, 미·러 경유 거래 비판하며 유럽의 더 큰 역할 환영", R, "2026-10-17", "https://www.reuters.com/world/ukraines-zelenskiy-blasts-us-russian-diesel-deal-welcomes-bigger-european-role-2026-10-16/",
     "우크라이나 젤렌스키 대통령이 미·러 경유 거래를 비판하고 유럽의 역할 확대를 환영하면서, 거래를 둘러싼 우방 간 이견이 드러났다 (제목 기준)"),
  it("트럼프, 그레이엄법상 대러 에너지 관세·제재 면제", B, "2026-10-17", "https://www.bloomberg.com/news/articles/2026-10-17/trump-waives-russia-energy-tariffs-sanctions-in-graham-law",
     "트럼프 대통령이 그레이엄법에 따른 러시아 에너지 관세·제재를 면제하면서, 러시아 원유 상위 구매국에 최대 100% 관세가 붙을 위험이 미뤄졌다"),
  it("트럼프, 시행 앞둔 대러 제재·관세 다수 유예", R, "2026-10-17", "https://www.reuters.com/world/europe/trump-waives-many-russia-related-sanctions-tariffs-before-they-were-take-effect-2026-10-17/",
     "트럼프 대통령이 시행을 며칠 앞둔 대러 제재·관세 다수를 국익을 이유로 유예하고 의회에 확인서를 내면서, 대통령이나 국무장관이 달리 정할 때까지 효력이 멈췄다")
 ]
})

# G1-007
items.append({
 "cid": "G1-007", "attachTo": "n-rtr-0014",
 "title": "美 중부사령부 '봉쇄로 이란 원유 250억 달러 수출 막아'…이란은 유조선 공격·LPG 우회 수출",
 "one": "미 중부사령부가 해상 봉쇄로 이란의 원유 수출 최소 250억 달러어치를 막았다고 밝혔지만 이란이 유조선 공격과 LPG·항공유 우회 수출을 이어가고 트럼프가 곡괭이산 핵시설 타격 가능성을 내비치면서, 호르무즈 해협의 긴장이 이어지고 있다",
 "facts": [
  "무엇이: 브래드 쿠퍼 중부사령관은 10월 16일 해상 봉쇄로 이란이 최소 250억 달러어치 원유를 수출하지 못했고, 지난 1주일 동안 약 400척과 원유 1억 배럴 이상이 호르무즈 해협을 지났다고 밝혔다 [사실]",
  "금융: 미 당국은 이란 관련 암호화폐 약 3억 5,000만 달러를 동결했다 [사실]",
  "우회 수출: UANI 분석으로는 7월 중순 이후 이란산 LPG를 실은 가스선 최소 8척이 오만만을 떠났고 총량은 약 410만 배럴이며, 항공유 유조선 1척이 9월 미얀마에 도착했다 [사실]",
  "공격: 윈드워드 집계로 10월 14일까지 2주간 호르무즈와 인근 해역 상선 공격이 최소 23건이었고, 이란은 오만 인근에서 해협을 불법 통과한 유조선을 공격했다고 발표했다 [채널]",
  "트럼프: 트럼프 대통령은 핵무기와 지상군은 배제하면서 이란 곡괭이산 핵시설을 타격해야 할 수도 있다고 했다 [사실]"
 ],
 "basis": "verified",
 "check": "중부사령부 발표(250억 달러·400척·암호화폐 동결)와 LPG·항공유 우회 수출은 검색 결과 요약으로 확인, 곡괭이산 발언은 출처 1곳. 이란군 500km 작전, 유조선 공격 발표, 텔아비브 방공호, 트럼프의 '지나쳤을 수도' 발언은 채널 전언",
 "src": [
  {"o": "The Hill", "d": "2026-10-16", "u": "https://thehill.com/newsletters/defense-national-security/6155474-centcom-commander-says-naval-blockade-cost-iran-25b-in-oil-revenue/"},
  {"o": "Al Arabiya", "d": "2026-10-16", "u": "https://english.alarabiya.net/News/middle-east/2026/10/16/us-military-aids-financial-chokehold-on-iran-blocking-25-billion-in-oil-exports"},
  {"o": "gCaptain", "d": "2026-10-16", "u": "https://gcaptain.com/iran-ships-some-lpg-jet-fuel-despite-us-blockade-data-shows/"},
  {"o": "Sunday Guardian", "d": "2026-10-16", "u": "https://sundayguardianlive.com/world/us-israel-iran-war-latest-live-news-trump-signals-possible-us-strike-on-irans-pickaxe-mountain-nuclear-site-rules-out-nuclear-weapons-and-ground-troops-deployment-306996/"}
 ],
 "inds": ["macro", "oil", "shipping"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "oil", "node": "opec", "f": "공급", "dir": "down", "k": "실제", "t": "美 봉쇄로 이란 원유 250억 달러어치 수출 차단"},
  {"ind": "shipping", "node": "routes", "f": "공급", "dir": "down", "k": "예상", "t": "호르무즈 상선 공격 2주간 최소 23건"}
 ],
 "added": "이번 로이터 2건과 텔레그램 5건으로 중부사령부의 이란 원유 250억 달러 수출 차단 발표, 이란의 LPG·항공유 우회 수출과 유조선 공격, 곡괭이산 타격 가능성이 추가됐다",
 "items": [
  it("이란, 美 봉쇄에도 LPG·항공유 일부 선적…데이터로 확인", R, "2026-10-16", "https://www.reuters.com/business/energy/iran-ships-some-lpg-jet-fuel-despite-us-blockade-data-shows-2026-10-16/",
     "이란이 미국의 해상 봉쇄 속에서도 오만 앞바다 선박 간 환적으로 LPG 약 410만 배럴과 항공유 일부를 실어 내보내면서, 봉쇄에 빈틈이 있다는 분석이 나왔다"),
  it("트럼프 '이란 곡괭이산 타격해야 할 수도'", R, "2026-10-16", "https://www.reuters.com/world/trump-says-us-may-need-strike-irans-pickaxe-mountain-2026-10-16/",
     "트럼프 대통령이 이란의 곡괭이산 핵시설을 타격해야 할 수도 있다고 말하면서, 핵무기·지상군을 뺀 추가 공습 가능성을 열어뒀다"),
  it("이란군 '며칠 안에 미 해군 500km 밖으로 밀어낼 공세 작전'", "텔레그램 트릴리온", "2026-10-16", "https://t.me/Trillion_labs/10640",
     "이란군이 해안에서 500km 떨어진 미 해군을 더 밀어내는 공세 작전을 며칠 안에 벌이겠다고 밝히면서, 걸프 해역의 군사 충돌 위험이 높아졌다"),
  it("이란, 호르무즈 불법 통과 유조선 오만 인근서 공격했다고 발표", "텔레그램 트릴리온", "2026-10-16", "https://t.me/Trillion_labs/10641",
     "이란이 오만 인근 해역에서 호르무즈 해협을 불법 통과한 유조선을 공격했다고 발표하면서, 해협을 지나는 상선의 안전 위험이 커졌다"),
  it("텔아비브 이동식 방공호 배치…이란, 헤즈볼라에 최고 경계령", "텔레그램 트릴리온", "2026-10-17", "https://t.me/Trillion_labs/10668",
     "이스라엘이 텔아비브에 이동식 방공호를 배치하고 이란이 헤즈볼라에 최고 경계 태세를 내렸다는 전언이 나오면서, 이스라엘·이란 간 추가 공격 가능성이 거론됐다"),
  it("중부사령부 '봉쇄로 이란 석유 수출 250억 달러 차단, 해상 수출입 중단'", "텔레그램 미국 주식 인사이더", "2026-10-17", "https://t.me/insidertracking/66498",
     "쿠퍼 중부사령관이 봉쇄로 이란 석유 수출 최소 250억 달러를 막고 인도적 지원 외 해상 수출입을 멈췄다고 밝히면서, 이란의 외화 수입이 크게 줄었다"),
  it("트럼프 '이란 지도부에 지나쳤을 수도…대화할 상대 없어'", "텔레그램 하나증권 중국전략", "2026-10-17", "https://t.me/HANAchina/70545",
     "트럼프 대통령이 이란 지도부에 지나치게 했을 수 있다며 대화할 상대가 없다고 말하면서, 협상을 통한 긴장 완화 통로가 막혀 있음을 드러냈다")
 ]
})

# G1-015
items.append({
 "cid": "G1-015", "attachTo": "n-tg-0118",
 "title": "CXMT 1~3분기 순이익 1,310억 위안대 흑자 전환…'내년 1분기 HBM 80~100% 인상' 전망",
 "one": "중국 CXMT가 D램 가격 급등에 1~9월 순이익 1,310억~1,325억 위안의 흑자 전환을 예고하고 키뱅크가 내년 1분기 HBM 가격 80~100% 인상을 내다보면서, 데이터센터로 생산이 쏠린 PC·스마트폰용 메모리 공급은 내년 20~30% 줄어들 전망이다",
 "facts": [
  "무엇이: CXMT는 10월 16일 2026년 1~9월 지배주주 순이익이 1,310억~1,325억 위안으로 전년 동기 52억 8,000만 위안 순손실에서 흑자로 돌아설 것이라고 예고했다 [사실]",
  "매출: 같은 기간 매출은 2,650억~2,700억 위안(전년 321억 위안)으로 예상되며, 회사는 AI 연산 수요에 따른 D램 공급 부족과 가격 상승을 이유로 들었다 [사실]",
  "3분기: 3분기 단독 순이익은 약 534억~549억 위안으로 계산되며, 주주밍 회장은 A주 자사주 매입을 제안했지만 규모는 최대 20억 위안과 100억~200억 위안으로 보도가 엇갈린다 [사실]",
  "전망: 키뱅크는 메모리 업체들이 생산능력을 데이터센터로 돌려 내년 PC·스마트폰용 메모리 공급이 20~30% 줄고, 4분기 D램·낸드 가격이 15% 넘게 오르며 내년 1분기 HBM 가격이 80~100% 오를 것으로 봤다 [채널]",
  "장기계약: HP·델은 메모리 공급계약을 2031년까지 늘렸고 구글은 2035년까지 적용되는 장기계약을 협상 중이라는 전언이다 [채널]"
 ],
 "basis": "verified",
 "check": "CXMT 실적 예고(순이익·매출·전년 손실)와 3분기 추정치는 검색 결과 요약으로 확인, 자사주 매입 규모는 출처마다 엇갈림. 키뱅크 전망과 HP·델·구글 장기계약은 채널 전언",
 "src": [
  {"o": "SCMP", "d": "2026-10-16", "u": "https://www.scmp.com/tech/tech-trends/article/3353988/cxmts-blowout-earnings-outlook-fuels-rally-chinese-memory-chip-stocks"},
  {"o": "TechFlow", "d": "2026-10-16", "u": "https://www.techflowpost.com/en-US/newsletter/140275"},
  {"o": "BigGo Finance", "d": "2026-10-16", "u": "https://finance.biggo.com/news/09ccf926-1af4-4bb1-9ace-fe1a44ed99fa"}
 ],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "vc": [
  {"ind": "semis", "node": "memory", "f": "가격", "dir": "up", "k": "실제", "t": "D램 가격 급등에 CXMT 흑자 전환"},
  {"ind": "semis", "node": "memory", "f": "공급", "dir": "down", "k": "예상", "t": "내년 PC·스마트폰용 메모리 공급 20~30% 감소 전망"}
 ],
 "added": "이번 블룸버그 1건과 텔레그램 3건으로 CXMT의 1~3분기 순이익 1,310억 위안대 흑자 전환 예고와 키뱅크의 내년 1분기 HBM 가격 80~100% 인상 전망이 추가됐다",
 "items": [
  it("키뱅크 '내년 1분기 HBM 80~100% 인상, 메모리 장기계약 2035년까지'", "텔레그램 하나증권 중국전략", "2026-10-16", "https://t.me/HANAchina/70528",
     "키뱅크가 메모리 업체의 데이터센터 쏠림으로 내년 PC·스마트폰용 메모리 공급이 20~30% 줄고 4분기 D램·낸드 가격이 15% 넘게 오를 것으로 내다봤다"),
  it("중국 CXMT, 메모리 칩 가격 급등에 흑자 전환", B, "2026-10-17", "https://www.bloomberg.com/news/articles/2026-10-16/china-s-cxmt-swings-to-profit-after-memory-chip-prices-surge",
     "중국 CXMT가 메모리 칩 가격 급등에 힘입어 흑자로 돌아서면서, 중국 D램 업체가 세계 메모리 가격 상승의 수익을 크게 누리고 있다"),
  it("CXMT 1~9월 순이익 최대 1,325억 위안 전망…매출 8배 넘게 급증", "텔레그램 미국 주식 인사이더", "2026-10-17", "https://t.me/insidertracking/66483",
     "CXMT가 1~9월 순이익 1,310억~1,325억 위안과 매출 2,650억~2,700억 위안을 예상하면서, 이 소식이 나스닥 하락의 한 촉매가 됐다는 해석이 나왔다"),
  it("CXMT 3분기 단독 순이익 534억~549억 위안…자사주 매입 추진", "텔레그램 하나증권 중국전략", "2026-10-17", "https://t.me/HANAchina/70542",
     "CXMT가 3분기 단독 순이익 534억~549억 위안을 예상하고 회장이 A주 자사주 매입을 제안했지만, 연간 순이익 컨센서스 2,000억 위안대는 어렵다는 평가가 나왔다")
 ]
})

# G1-020
items.append({
 "cid": "G1-020", "attachTo": "n-bbg-0319",
 "title": "IMF '은행세 인상 최선 아냐'…英 힐리 은행세 구상에 베일리와 마찰 우려",
 "one": "존 힐리 재무장관이 10월 28일 예산안에서 은행 추가세율을 3%에서 8%로 되돌리는 안을 검토하는 가운데 IMF가 은행세 인상은 첫 선택이 아니라며 재산세 개편과 복지 지출 조정을 권하면서, 은행권 세 부담을 둘러싼 논쟁이 커지고 있다",
 "facts": [
  "무엇이: IMF 유럽국 헬게 베르거 부국장은 10월 16일 은행세 인상은 선택지일 수 있지만 첫 선택은 아니라며, 재산세 개편·판매세 확대·복지 지출 조정을 권했다 [사실]",
  "방안: 힐리 재무장관은 은행 추가세율을 8%에서 3%로 낮췄던 조치를 되돌리는 안을 검토 중이며, UK파이낸스는 경쟁력과 투자를 해친다며 반대했다 [사실]",
  "중앙은행: 블룸버그는 은행세 계획이 힐리 장관과 베일리 영란은행 총재의 마찰을 부를 수 있다고 전했다 [제목]",
  "비자: 힐리 재무장관은 부유한 외국인을 위한 새 투자자 비자를 검토하고 있다 [제목]",
  "기존: 보도 뒤 16일 바클레이스·로이즈·냇웨스트 주가가 장 초반 0.2~1.8% 내렸고, TUC는 8% 환원 시 연 22억 5,000만 파운드가 걷힐 것으로 추산했다 [사실]"
 ],
 "basis": "partial",
 "check": "IMF 발언과 추가세율 환원 검토는 검색 결과 요약으로 확인. 베일리 총재와의 마찰, 투자자 비자 검토, 은행세가 미끼라는 분석은 확인 못 함(제목 기준)",
 "src": [
  {"o": "Eastern Eye", "d": "2026-10-16", "u": "https://www.easterneye.biz/imf-warns-uk-against-higher-bank-taxes-ahead-of-october-budget/"},
  {"o": "AOL", "d": "2026-10-16", "u": "https://www.aol.co.uk/articles/cut-public-spending-rather-raising-173751000.html"}
 ],
 "inds": ["fin", "macro"], "nodes": ["macro/fiscal"],
 "vc": [
  {"ind": "fin", "node": "banks", "f": "가격", "dir": "down", "k": "실제", "t": "은행세 인상 검토에 영국 은행주 하락"},
  {"ind": "macro", "node": "fiscal", "f": "-", "dir": "flat", "k": "예상", "t": "IMF가 은행세 대신 재산세·복지 조정 권고"}
 ],
 "added": "이번 블룸버그 3건과 로이터 1건으로 IMF의 은행세 인상 신중 권고와 힐리·베일리 마찰 가능성, 부유층 외국인 투자자 비자 검토가 추가됐다",
 "items": [
  it("英 은행세 계획, 힐리와 베일리 영란은행 총재 마찰 부를 수도", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/uk-bank-tax-plan-risks-putting-healey-at-odds-with-boe-s-bailey",
     "힐리 재무장관의 은행세 인상 계획이 베일리 영란은행 총재와 부딪힐 수 있다는 분석이 나오면서, 재정당국과 중앙은행 간 마찰 위험이 부각됐다 (제목 기준)"),
  it("IMF '은행세 인상은 英 예산안의 최선 아냐'", R, "2026-10-16", "https://www.reuters.com/world/uk/raising-bank-tax-is-not-best-choice-uk-budget-imf-says-2026-10-16/",
     "IMF가 은행세 인상은 영국 예산안의 첫 선택이 아니라며 재산세 개편과 복지 지출 조정을 권하면서, 힐리 재무장관의 은행세 인상 구상에 부담이 생겼다"),
  it("힐리, 부유한 외국인 위한 새 투자자 비자 검토", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/healey-considers-new-uk-investor-visa-for-wealthy-foreigners",
     "힐리 재무장관이 부유한 외국인을 겨냥한 새 투자자 비자를 검토하면서, 영국이 해외 부유층 자금 유치에 다시 나설 수 있다 (제목 기준)"),
  it("예산안이 또 은행가를 겨냥했다…미끼일까", B, "2026-10-17", "https://www.bloomberg.com/news/newsletters/2026-10-16/the-budget-targets-bankers-again-is-it-a-decoy",
     "블룸버그 뉴스레터가 이번 예산안의 은행 겨냥이 미끼일 수 있다는 의문을 던지면서, 은행세 인상이 실제 핵심 조치인지에 물음표가 붙었다 (제목 기준)")
 ]
})

# G1-026
items.append({
 "cid": "G1-026", "attachTo": "n-bbg-0052",
 "title": "미 9월 수입물가 1.1%↑·전년비 8.1% 4년여 최대…BofA '10월 인상' 전망 유지",
 "one": "미국 9월 수입물가가 연료 4.8% 급등에 전월 대비 1.1%, 전년 대비 8.1% 올라 2022년 7월 이후 최대폭을 기록하고 비연료 물가도 0.7% 오르면서, CPI 3.7%에 이어 물가 확산이 확인되자 BofA가 10월 인상 전망을 유지했다",
 "facts": [
  "무엇이: 미 노동통계국 발표로 9월 수입물가는 전월 대비 1.1%(예상 0.8%) 올랐고 전년 대비 8.1% 상승해 2022년 7월 이후 최대폭이었다 [사실]",
  "연료: 수입 연료 가격은 한 달 새 4.8%, 1년 새 34.5% 올랐고 수입 천연가스는 1년 새 96.5% 뛰었다 [사실]",
  "확산: 비연료 수입물가도 전월 대비 0.7%, 전년 대비 6.0% 올랐다 [사실]",
  "BofA: BofA는 근원 CPI 항목 가운데 최근 3개월 연율 2.5%를 넘는 비중이 55%로 고점 수준에 이르렀다며 10월 인상 전망을 유지하고, 연준의 비둘기파 신호는 이해하기 어렵다고 했다 [채널]",
  "기존: 9월 CPI는 전년 대비 3.7%, PPI는 6.3% 올랐고, 보우먼·데일리 등의 발언 뒤 10월 27~28일 동결 확률이 73%로 높아졌다 [사실]"
 ],
 "basis": "verified",
 "check": "수입물가 수치(1.1%·8.1%·연료 4.8%·비연료 0.7%)는 노동통계국 발표의 검색 결과 요약으로 확인. BofA 전망과 자본재 가격 0.9% 상승은 채널 전언",
 "src": [
  {"o": "미 노동통계국", "d": "2026-10-16", "u": "https://www.bls.gov/news.release/archives/ximpim_10162026.htm"},
  {"o": "ANI", "d": "2026-10-16", "u": "https://aninews.in/news/business/us-import-prices-surge-81-in-12-months-highest-rise-since-july-202220261016193539/"}
 ],
 "inds": ["macro"], "nodes": ["macro/inflation", "macro/cb"],
 "vc": [
  {"ind": "macro", "node": "inflation", "f": "가격", "dir": "up", "k": "실제", "t": "9월 수입물가 전년비 8.1% 상승"},
  {"ind": "macro", "node": "cb", "f": "가격", "dir": "up", "k": "예상", "t": "BofA 연준 10월 금리 인상 전망 유지"}
 ],
 "fed": [
  {"k": "", "who": "연준", "role": "BofA의 10월 인상 전망", "kind": "관련 뉴스", "stance": "매파", "t": "BofA가 물가 확산을 들어 연준의 10월 금리 인상 예상을 유지했다", "d": "2026-10-16", "u": "https://t.me/HANAchina/70527"}
 ],
 "added": "이번 로이터 1건과 텔레그램 2건으로 9월 수입물가 전년비 8.1% 상승과 근원 수입물가·자본재 가격 동반 상승, BofA의 10월 인상 전망 유지가 추가됐다",
 "items": [
  it("BofA '여전히 10월 금리 인상 예상'…연준 중시 물가 지표 전망 상향", "텔레그램 하나증권 중국전략", "2026-10-16", "https://t.me/HANAchina/70527",
     "BofA가 근원 CPI 항목 중 3개월 연율 2.5% 초과 비중이 55%로 반등했다며, 연준의 10월 금리 인상 예상을 유지하고 물가 전망을 높였다"),
  it("미 9월 수입물가, 예상보다 큰 폭 상승", R, "2026-10-17", "https://www.reuters.com/business/us-import-prices-increase-more-than-expected-september-2026-10-16/",
     "미국 9월 수입물가가 전월 대비 1.1% 올라 예상 0.8%를 웃돌면서, 전년 대비 상승률이 8.1%로 2022년 7월 이후 가장 커졌다"),
  it("미 9월 근원 수입물가·자본재 가격 동반 상승…물가 확산 확인", "텔레그램 하나증권 중국전략", "2026-10-17", "https://t.me/HANAchina/70556",
     "미국 9월 수입물가에서 연료가 4.8% 오른 데 더해 근원 수입물가 0.7%, 자본재 0.9%가 함께 오르면서, 인플레이션이 경제 전반으로 번지고 있다")
 ]
})

# G1-032
items.append({
 "cid": "G1-032", "attachTo": "",
 "title": "英 CMA, MS 업무용 SW에 전략적 시장지위 지정 제안…클라우드는 자율 개선 택해",
 "one": "영국 경쟁시장청(CMA)이 마이크로소프트의 윈도·오피스 등 업무용 소프트웨어에 전략적 시장지위 지정을 제안하고 클라우드는 AWS·MS의 자율 개선 약속을 택하면서, MS의 경쟁 클라우드 대상 라이선스 조건과 데이터 반출 수수료가 손질될 전망이다",
 "facts": [
  "무엇이: CMA는 10월 16일 마이크로소프트의 업무용 소프트웨어 생태계를 전략적 시장지위(SMS)로 지정하자고 제안하고 의견 수렴에 들어갔으며, 지정이 위법 행위를 뜻하지는 않는다고 했다 [사실]",
  "범위: 윈도·오피스·보안·서버 소프트웨어·데이터베이스가 대상이고 영국 기업·공공기관 100만 곳 이상이 쓰며, 초기 초점은 경쟁 클라우드 업체에 대한 라이선스와 코파일럿 외 AI 도구 선택권이다 [사실]",
  "클라우드: AWS와 마이크로소프트는 데이터 반출(이그레스) 수수료를 없애거나 줄이고 멀티클라우드 상호운용성을 높이기로 했고, CMA 이사회는 6개월 뒤 진척을 점검한다 [사실]",
  "반응: 마이크로소프트는 업무용 소프트웨어 제안에 동의하지 않는다면서도 클라우드 지정이 필요 없다는 판단은 반겼다 [사실]"
 ],
 "basis": "verified",
 "check": "CMA의 SMS 지정 제안, 대상 제품, 클라우드 자율 개선과 6개월 점검은 검색 결과 요약으로 확인",
 "src": [
  {"o": "Wired-Gov(CMA 보도자료)", "d": "2026-10-16", "u": "https://wired-gov.net/wg/news.nsf/articles/CMA+takes+first+steps+to+ensure+choice+in+business+software+16102026162000?open="},
  {"o": "Tech Policy Press", "d": "2026-10-16", "u": "https://www.techpolicy.press/uk-cloud-regulator-opts-for-voluntary-commitments-launches-microsoft-investigation/"},
  {"o": "The Next Web", "d": "2026-10-16", "u": "https://thenextweb.com/news/cma-aws-microsoft-cloud-switching-barriers"}
 ],
 "inds": ["tech"], "nodes": [],
 "vc": [
  {"ind": "tech", "node": "software", "f": "가격", "dir": "down", "k": "예상", "t": "CMA, MS의 경쟁 클라우드 대상 라이선스 손질 추진"},
  {"ind": "tech", "node": "cloud", "f": "가격", "dir": "down", "k": "예상", "t": "AWS·MS 데이터 반출 수수료 폐지·인하 약속"}
 ],
 "added": "이번 로이터 2건으로 CMA가 MS의 업무용 소프트웨어 장악력을 겨냥하고 AWS·MS에 클라우드 전환 장벽을 더 낮추라고 요구한 내용이 추가됐다",
 "items": [
  it("英 규제당국, MS 소프트웨어에 대한 감독 강화 제안", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/uk-watchdog-proposes-tougher-scrutiny-of-microsoft-software",
     "영국 CMA가 마이크로소프트 업무용 소프트웨어를 전략적 시장지위로 지정하자고 제안하면서, 윈도·오피스 라이선스 관행에 더 강한 감독이 붙을 전망이다"),
  it("英 경쟁당국, MS의 업무용 소프트웨어 장악력 겨냥", R, "2026-10-16", "https://www.reuters.com/legal/litigation/uk-competition-regulator-targets-microsofts-business-software-grip-2026-10-16/",
     "CMA가 경쟁 클라우드 업체에 대한 MS의 라이선스 방식과 코파일럿 외 AI 도구 선택권을 먼저 살피기로 하면서, MS 업무용 소프트웨어 판매 방식에 제약이 생길 수 있다"),
  it("英 경쟁당국 'AWS·MS, 클라우드 장벽 해소에 더 나설 수 있어'", R, "2026-10-17", "https://www.reuters.com/legal/litigation/aws-microsoft-can-do-more-address-cloud-services-barriers-uk-competition-2026-10-16/",
     "CMA가 AWS·MS에 클라우드 전환 장벽을 더 낮추라고 하면서, 두 회사가 데이터 반출 수수료 인하와 상호운용성 개선을 약속하고 6개월 뒤 점검을 받는다")
 ]
})

# G1-038
items.append({
 "cid": "G1-038", "attachTo": "",
 "title": "FAA·관제사 노조, 2.8% 임금 인상 합의…출입 기록·근무 개편 함께 도입",
 "one": "미 연방항공청(FAA)과 관제사 노조 NATCA가 1월로 소급한 2.8% 임금 인상에 합의하고 출입 기록·업무량 기반 근무표 등 인력 개편을 함께 도입하면서, 인력난이 심한 시설로 재배치가 이뤄지는 등 관제 인력 운영 방식이 바뀐다",
 "facts": [
  "무엇이: FAA와 NATCA는 10월 16일 관제사 임금을 2.8% 올리는 데 합의했고, 인상은 10월 18일 시행돼 1월 1일로 소급된다 [사실]",
  "수치: 묶음의 로이터 주소에는 '28 pay rise'로 적혀 있지만 검색된 보도는 모두 2.8%로 전했다 [사실]",
  "조건: 의회가 승인한 인상분 가운데 1%만 먼저 지급되고 나머지는 인력 개편을 조건으로 묶여 있었으며, 관제사는 출입 기록을 남기고 근무표는 예상 업무량에 맞춰 짠다 [사실]",
  "배경: 많은 관제사가 의무 초과근무와 주 6일 근무를 하고 있고, 반복된 정부 셧다운의 부담을 떠안아 왔다 [사실]"
 ],
 "basis": "verified",
 "check": "2.8% 인상·시행일·소급·인력 개편 조건은 검색 결과 요약으로 확인. 묶음 주소의 '28'은 소수점이 빠진 표기로 판단",
 "src": [
  {"o": "Spokesman-Review", "d": "2026-10-16", "u": "https://www.spokesman.com/stories/2026/oct/16/faa-air-traffic-controllers-union-reach-agreement-/"},
  {"o": "EIN Presswire", "d": "2026-10-16", "u": "https://www.einnews.com/pr_news/950281318/trump-s-transportation-department-air-traffic-controller-union-announce-2-8-pay-increase-deal"},
  {"o": "The Aviation Hub", "d": "2026-10-16", "u": "https://theaviationhub.co.uk/faa-air-traffic-controllers-pay-deal/"}
 ],
 "inds": ["aero"], "nodes": [],
 "vc": [
  {"ind": "aero", "node": "airports", "f": "가격", "dir": "up", "k": "실제", "t": "미 관제사 임금 2.8% 인상 합의"},
  {"ind": "aero", "node": "airports", "f": "공급", "dir": "up", "k": "예상", "t": "인력난 시설 중심 관제사 재배치"}
 ],
 "added": "이번 로이터 후속 1건으로 노조 확인을 거친 2.8% 인상이 1월로 소급되고 10월 18일부터 시행된다는 점이 추가됐다",
 "items": [
  it("미 관제사, FAA와 2.8% 임금 인상 합의…WSJ 보도", R, "2026-10-17", "https://www.reuters.com/business/world-at-work/us-air-traffic-controllers-reach-deal-with-faa-28-pay-rise-wsj-reports-2026-10-16/",
     "WSJ 보도로 미 관제사 노조가 FAA와 2.8% 임금 인상에 합의했다고 알려지면서, 지연됐던 의회 승인 인상분의 지급 길이 열렸다"),
  it("FAA·관제사 노조, 임금 인상에 합의", B, "2026-10-17", "https://www.bloomberg.com/news/articles/2026-10-16/faa-air-traffic-controllers-union-reach-agreement-on-pay-bump",
     "FAA와 관제사 노조 NATCA가 임금 인상에 합의하면서, 출입 기록과 업무량 기반 근무표 같은 인력 개편도 함께 시행된다"),
  it("미 관제사, FAA 합의로 2.8% 임금 인상 받는다", R, "2026-10-17", "https://www.reuters.com/business/world-at-work/us-air-traffic-controllers-get-28-pay-raise-under-faa-deal-2026-10-16/",
     "미 관제사들이 FAA 합의에 따라 1월로 소급된 2.8% 임금 인상을 10월 18일부터 받게 되면서, 초과근무에 시달려 온 인력의 불만이 일부 풀릴 수 있다")
 ]
})

# G1-047
items.append({
 "cid": "G1-047", "attachTo": "n-rtr-0295",
 "title": "킴벌리클라크, 켄뷰 인수 앞두고 채권 발행 준비…켄뷰 타이레놀 소송 재심리 요청 기각",
 "one": "킴벌리클라크가 켄뷰 인수를 앞두고 채권 발행을 준비하는 가운데 미 2순회 항소법원이 타이레놀 자폐 소송 수백 건을 되살린 판결의 재심리 요청을 기각하면서, EU 조건부 승인을 받은 인수에 소송 부담이 따라붙게 됐다",
 "facts": [
  "무엇이: 미 2순회 항소법원은 10월 16일 타이레놀이 자폐를 일으킬 수 있다는 켄뷰 상대 소송 수백 건을 되살린 판결에 대해 켄뷰의 재심리·전원합의체 심리 요청을 기각했다 [사실]",
  "의미: 7월 판결은 원고 측 전문가 증언 배제가 지나쳤다고 본 것으로 타이레놀이 자폐를 일으킨다고 판단한 것은 아니며, 켄뷰는 연방대법원 상고에 나설 수 있다 [사실]",
  "채권: 킴벌리클라크는 켄뷰 인수를 앞두고 채권 발행을 준비하고 있다 [제목]",
  "기존: EU 집행위원회는 10월 13일 유럽경제지역 여성위생 사업을 딜렉 그룹에 판다는 조건으로 인수를 승인했고, 인수 규모는 보도에 따라 400억 달러 또는 487억 달러다 [사실]"
 ],
 "basis": "partial",
 "check": "재심리 요청 기각과 7월 판결 내용은 검색 결과 요약으로 확인. 킴벌리클라크 채권 발행 준비는 확인 못 함(제목 기준)",
 "src": [
  {"o": "The Globe and Mail", "d": "2026-07", "u": "https://www.theglobeandmail.com/business/international-business/us-business/article-us-appeals-court-kenvue-lawsuits-tylenol-autism-claims/"},
  {"o": "Baptista Research", "d": "2026-10", "u": "https://baptistaresearch.com/kenvue-tylenol-lawsuits-kimberly-clark-deal/"}
 ],
 "inds": ["consumer"], "nodes": [],
 "vc": [
  {"ind": "consumer", "node": "household", "f": "공급", "dir": "down", "k": "예상", "t": "켄뷰 인수 앞두고 킴벌리클라크 채권 발행 준비"}
 ],
 "added": "이번 블룸버그·로이터 2건으로 킴벌리클라크의 인수 전 채권 발행 준비와 켄뷰의 타이레놀 자폐 소송 재심리 요청 기각이 추가됐다",
 "items": [
  it("킴벌리클라크, 타이레놀 제조사 인수 앞두고 채권 발행 준비", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/kimberly-clark-preps-bond-sale-ahead-of-tylenol-maker-purchase",
     "킴벌리클라크가 타이레놀 제조사 켄뷰 인수를 앞두고 채권 발행을 준비하면서, 인수 마무리를 위한 자금 조달에 들어갔다 (제목 기준)"),
  it("켄뷰, 타이레놀 자폐 소송 부활 뒤 재심리 요청 기각당해", R, "2026-10-17", "https://www.reuters.com/legal/litigation/kenvue-loses-bid-rehearing-after-tylenol-autism-lawsuits-revived-2026-10-16/",
     "미 2순회 항소법원이 켄뷰의 재심리 요청을 기각하면서, 타이레놀 자폐 소송 수백 건이 1심으로 돌아가고 켄뷰의 법적 부담이 이어진다")
 ]
})

# G1-053
items.append({
 "cid": "G1-053", "attachTo": "n-rtr-0323",
 "title": "중국, 미국산 대두 10~13척 추가 구매…이번 주 최대 150만 톤",
 "one": "중국 국영 무역회사들이 13일 8~10척에 이어 16일 미국산 대두 10~13척을 12~3월 선적분으로 더 사들이면서, 이번 주 구매량이 120만~150만 톤에 이르고 누적 매입이 약 1,500만 톤으로 2026/27년 목표 2,500만 톤에 다가섰다",
 "facts": [
  "무엇이: 중국 국영 무역회사들이 10월 16일 미국산 대두 10~13척을 추가로 샀고 선적은 12월~3월이다 [사실]",
  "규모: 13일 8~10척을 합친 이번 주 구매량은 120만~150만 톤으로 추산되며, 블룸버그는 최소 20척, 약 130만 톤으로 전했다 [사실]",
  "누적: 중국의 미국산 대두 누적 매입은 약 1,500만 톤으로 2026/27년 목표 2,500만 톤에 가까워졌다 [사실]",
  "한계: 미국산 대두는 13% 관세(브라질산 3%)를 물어 민간 구매자에게 가격 경쟁력이 없고, 구매는 국영 기업이 주도한다 [사실]"
 ],
 "basis": "verified",
 "check": "16일 10~13척 추가 구매, 주간 120만~150만 톤, 누적 약 1,500만 톤, 관세 차이는 검색 결과 요약으로 확인",
 "src": [
  {"o": "KXEL", "d": "2026-10-16", "u": "https://kxel.com/2026/10/16/chinese-buyers-book-another-large-round-of-u-s-soybeans/"},
  {"o": "Farm Policy News", "d": "2026-10", "u": "https://farmpolicynews.illinois.edu/2026/10/china-buys-first-us-soybeans-since-trump-xi-meeting/"}
 ],
 "inds": ["agri"], "nodes": [],
 "vc": [
  {"ind": "agri", "node": "demand", "f": "수요", "dir": "up", "k": "실제", "t": "중국 국영사 미국산 대두 10~13척 추가 구매"}
 ],
 "added": "이번 블룸버그·로이터 2건으로 16일 10~13척 추가 구매와 이번 주 120만~150만 톤, 누적 약 1,500만 톤 매입이 추가됐다",
 "items": [
  it("중국, 미국산 대두 추가 구매…구매 행렬 속도 붙어", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/china-buys-more-us-soybeans-as-purchasing-spree-gathers-pace",
     "중국 국영 기업들이 미국산 대두를 최소 20척, 약 130만 톤 사들이면서, 미·중 정상회담 뒤 구매 속도가 빨라지고 있다"),
  it("중국 국영 구매자, 정상회담 뒤 미국산 대두 추가 확보", R, "2026-10-16", "https://www.reuters.com/world/asia-pacific/china-state-buyers-snap-up-more-us-soybeans-latest-post-summit-purchases-2026-10-16/",
     "중국 국영 구매자들이 12~3월 선적분 미국산 대두 10~13척을 더 사면서, 누적 매입이 약 1,500만 톤으로 목표 2,500만 톤에 가까워졌다")
 ]
})

# G1-059
items.append({
 "cid": "G1-059", "attachTo": "",
 "title": "ASML 하이브리드 본딩 장비 개발 보도에 베시 주가 약 3% 하락",
 "one": "세미애널리시스가 ASML이 경쟁 하이브리드 본딩 장비를 개발 중이라고 보도하면서, 이 장비를 양산 공급하는 유일한 업체인 베시 주가가 약 3% 내리고 첨단 패키징 장비 경쟁이 거세질 전망이다",
 "facts": [
  "무엇이: 10월 16일 세미애널리시스는 2022년 12월~2024년 11월 출원된 ASML 특허 27개 계열을 분석해 ASML이 다이-투-웨이퍼 하이브리드 본딩 장비를 개발 중이라고 보도했다 [사실]",
  "주가: 암스테르담 장 초반 베시는 약 2.7% 내린 159.05유로, ASML은 1.1% 오른 1,480유로였다 [사실]",
  "경쟁: 현재 하이브리드 본딩 장비를 양산 공급하는 곳은 베시뿐이며, 보고서는 첨단 로직 고객이 ASML 장비를 먼저 채택할 것으로 봤다 [사실]",
  "HBM: 보고서는 HBM의 다이-투-웨이퍼 채택이 2029년 이후로 밀릴 것으로 봤고, ASML은 보도에 논평하지 않았다 [사실]"
 ],
 "basis": "verified",
 "check": "세미애널리시스 보고서 내용, 베시·ASML 주가, ASML 무논평은 검색 결과 요약으로 확인",
 "src": [
  {"o": "BigGo Finance", "d": "2026-10-16", "u": "https://finance.biggo.com/news/aeeb7ea9-2962-419e-813f-c8347c958ab4"},
  {"o": "Finimize", "d": "2026-10-16", "u": "https://finimize.com/content/besi-stumbled-after-a-report-linked-asml-to-hybrid-bonding"}
 ],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "vc": [
  {"ind": "semis", "node": "equipment", "f": "공급", "dir": "up", "k": "예상", "t": "ASML 하이브리드 본딩 진출로 장비 공급자 증가"}
 ],
 "items": [
  it("ASML 경쟁 하이브리드 본딩 제품 개발 보도에 베시 주가 하락", R, "2026-10-16", "https://www.reuters.com/business/besi-shares-fall-report-asml-is-working-rival-hybrid-bonding-product-2026-10-16/")
 ]
})

# G1-061
items.append({
 "cid": "G1-061", "attachTo": "n-rtr-0043",
 "title": "美 지역은행도 3분기 대출 견조…대형은행 이어 경기 탄탄 신호",
 "one": "미 지역은행들이 3분기 실적에서 대출이 견조하다는 신호를 내며 대형은행에 이어 경기가 버티고 있음을 보여 줬고, 리전스는 조정 주당순이익 0.73달러로 예상을 넘기고 기업 대출 중심으로 평균 대출이 0.5% 늘었다",
 "facts": [
  "무엇이: 미 지역은행들이 3분기 실적에서 대출이 견조하다는 신호를 내며 대형은행들과 함께 경제가 탄탄하다는 신호를 보냈다 [제목]",
  "리전스: 리전스 파이낸셜의 3분기 조정 주당순이익은 0.73달러로 예상 0.66달러를 넘었고, 매출은 19억 7,000만 달러로 예상을 조금 밑돌았다 [사실]",
  "대출: 리전스의 평균 대출은 전 분기 대비 0.5% 늘었고 증가는 주로 기업·산업(C&I) 대출에서 나왔으며, 순상각률은 평균 대출의 0.29%로 내렸다 [사실]",
  "기존: 대형은행에서는 모건스탠리가 예상을 넘은 반면 뱅크오브아메리카는 12억 달러 자금세탁 방지 위반 벌금에 순이익이 17% 줄었다 [사실]"
 ],
 "basis": "partial",
 "check": "리전스 실적은 회사 발표·검색 결과 요약으로 확인. 지역은행 전반의 대출 견조는 다른 은행 수치를 확인하지 못해 제목 기준",
 "src": [
  {"o": "리전스 파이낸셜 IR", "d": "2026-10-16", "u": "https://ir.regions.com/news-events/press-releases/news-details/2026/Regions-Reports-Earnings-of-611-Million-and-EPS-of-0-71-in-3Q-2026/default.aspx"},
  {"o": "SEC 8-K", "d": "2026-10-16", "u": "https://www.sec.gov/Archives/edgar/data/0001281761/000128176126000063/rf-2026930xexhibit991.htm"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "banks", "f": "수요", "dir": "up", "k": "실제", "t": "지역은행 3분기 기업 대출 견조"}
 ],
 "added": "이번 로이터 1건으로 지역은행들도 3분기 대출이 견조해 대형은행과 함께 경기 탄탄 신호를 보냈다는 점과 리전스의 예상 웃돈 이익이 추가됐다",
 "items": [
  it("美 지역은행, 대출 견조로 대형은행과 함께 경기 탄탄 신호", R, "2026-10-17", "https://www.reuters.com/markets/us/us-regional-banks-join-bigger-peers-signaling-resilient-economy-lending-holds-2026-10-16/",
     "미 지역은행들이 3분기 대출이 견조하다고 밝히면서, 대형은행에 이어 미국 경기가 버티고 있다는 신호가 더해졌다")
 ]
})

# G1-067
items.append({
 "cid": "G1-067", "attachTo": "n-bbg-0225",
 "title": "폴란드 중앙은행 이사회 마비 위기…대통령, 교착 해법 모색",
 "one": "폴란드 대통령실이 정부의 중앙은행 이사 지명 부서 거부로 11월 5일부터 이사회가 법정 최소 인원에 못 미칠 수 있다고 경고하고 대통령이 교착 해법을 찾으면서, 글라핀스키 총재 국사재판소 회부 공방과 겹쳐 통화정책 기구 운영이 흔들리고 있다",
 "facts": [
  "무엇이: 폴란드 대통령실은 정부가 중앙은행 이사 지명에 부서를 거부해 새 지명이 없으면 지도부가 5명으로 줄어 법정 최소 인원에 못 미치고, 11월 5일부터 기능이 멈출 수 있다고 밝혔다 [사실]",
  "정부: 슈와프카 정부 대변인은 정부 부서 없는 대통령 임명은 법적으로 무효라고 맞섰다 [사실]",
  "대통령: 블룸버그는 폴란드 대통령이 중앙은행 교착을 벗어날 길을 찾고 있다고 전했다 [제목]",
  "기존: 하원 헌법책임위원회는 10월 9일 글라핀스키 총재를 국사재판소에 회부하자는 보고서를 채택했고, 하원 표결은 빨라야 10월 말이다 [사실]"
 ],
 "basis": "partial",
 "check": "이사회 정족수 미달 우려(11월 5일)와 부서 공방은 검색 결과 요약(폴란드 매체)으로 확인. 대통령의 구체적 해법은 확인 못 함(제목 기준)",
 "src": [
  {"o": "wPolityce", "d": "2026-10-16", "u": "https://wpolityce.pl/gospodarka/paraliz-w-nbp-od-listopada-prezydent-nawrocki-rzuca-wyzwanie-tuskowi-,278560"},
  {"o": "Archyde", "d": "2026-10", "u": "https://www.archyde.com/nbp-resubmits-board-appointments-to-president-nawrocki-amid-tensions-with-government/"},
  {"o": "Poland Insight", "d": "2026-10", "u": "https://polandinsight.com/glapinski-state-tribunal-nbp-zloty-market-reaction-october-2026/"}
 ],
 "inds": ["macro"], "nodes": ["macro/cb"],
 "vc": [
  {"ind": "macro", "node": "cb", "f": "-", "dir": "flat", "k": "예상", "t": "중앙은행 이사회 정족수 미달 우려로 교착"}
 ],
 "added": "이번 블룸버그 1건으로 이사 지명 부서 공방에 따른 중앙은행 이사회 정족수 미달 우려와 대통령의 교착 해법 모색이 추가됐다",
 "items": [
  it("폴란드 대통령, 중앙은행 이사회 교착 벗어날 길 모색", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/polish-president-seeks-way-out-of-deadlock-at-the-central-bank",
     "폴란드 대통령이 중앙은행 이사회 교착을 풀 방법을 찾으면서, 11월 5일 이후 정족수 미달로 기능이 멈출 수 있다는 우려에 대응하고 있다")
 ]
})

# G1-073
items.append({
 "cid": "G1-073", "attachTo": "n-rtr-0284",
 "title": "앙골라 올해 연료보조금 약 40억 달러로 두 배…신흥국 연료비 부담 확산",
 "one": "앙골라 재무 당국자가 올해 연료보조금 지출이 최대 3조 8,000억 콴자(약 41억 6,000만 달러)로 당초 예상의 두 배 가까이 늘 것으로 내다보면서, 발리 연료 부족·케냐 휘발유값 인상에 이어 신흥국의 연료비발 재정 압박이 커지고 있다",
 "facts": [
  "무엇이: 앙골라 재무부 고위 당국자는 올해 연료보조금 지출이 최대 3조 8,000억 콴자(약 41억 6,000만 달러)로 당초 예상인 2조 콴자 미만의 두 배 가까이 될 수 있다고 밝혔다 [사실]",
  "유가 가정: 그는 연말까지 유가가 배럴당 평균 약 90달러로 2026년 예산 기준 61달러를 크게 웃돌 것으로 봤다 [사실]",
  "개혁: 정부는 경제·사회적 충격을 우려해 보조금 축소를 천천히 이어가고 있으며, 베라 다베스 재무장관은 보조금 지출이 GDP의 2.48%(예산 0.9%)에 이를 수 있다고 했다 [사실]",
  "기존: 인도네시아 발리주는 연료 부족으로 10월 15~17일 재택근무를 명령했고, 케냐는 나이로비 휘발유 상한가를 리터당 226.96실링으로 올렸다 [사실]"
 ],
 "basis": "verified",
 "check": "보조금 3조 8,000억 콴자(약 41억 6,000만 달러)와 유가 가정은 검색 결과 요약으로 확인, GDP 2.48%는 루사 인터뷰 기준으로 출처마다 추정이 다름",
 "src": [
  {"o": "Devdiscourse", "d": "2026-10-16", "u": "https://www.devdiscourse.com/article/international/3993849-angolas-fuel-subsidies-spending-projected-to-hit-4-billion-in-2026-official-says"},
  {"o": "Macau Business", "d": "2026", "u": "https://macaubusiness.com/angola-spending-on-fuel-subsidies-set-to-rise-to-2-48-gdp-in-2026-minister/"}
 ],
 "inds": ["macro", "oil"], "nodes": ["macro/fiscal"],
 "vc": [
  {"ind": "macro", "node": "fiscal", "f": "수요", "dir": "up", "k": "예상", "t": "앙골라 연료보조금 지출 약 41억 달러로 증가 전망"}
 ],
 "added": "이번 로이터 1건으로 앙골라의 올해 연료보조금 지출이 약 40억 달러로 당초 예상의 두 배 가까이 늘 전망이라는 점이 추가됐다",
 "items": [
  it("앙골라 올해 연료보조금 지출 40억 달러 달할 전망…당국자", R, "2026-10-17", "https://www.reuters.com/business/energy/angolas-fuel-subsidies-spending-projected-hit-4-billion-2026-official-says-2026-10-16/",
     "앙골라 재무 당국자가 고유가로 올해 연료보조금 지출이 약 40억 달러에 이를 것으로 내다보면서, 예산 대비 재정 부담이 크게 늘게 됐다")
 ]
})

# G1-079
items.append({
 "cid": "G1-079", "attachTo": "n-rtr-0078",
 "title": "악조노벨·액설타, EU에 차량 보수용 도료 매각 시정안 제출…심사 기한 연장",
 "one": "악조노벨과 액설타가 250억 달러 합병의 EU 승인을 위해 악조노벨 차량 보수용 도료 사업 매각 시정안을 10월 15일 내면서, 집행위 심사 기한이 영업일 10일 늘어 11월로 넘어가고 경쟁사·고객 검증을 거쳐 승인 여부가 정해질 전망이다",
 "facts": [
  "무엇이: 악조노벨과 액설타는 10월 15일 약 250억 달러 합병의 EU 승인을 얻기 위한 시정안을 냈다 [사실]",
  "시정안: 시정안은 악조노벨의 유럽 차량 보수용 도료 사업 매각이며, 분체도료 중복 우려는 앞서 해소됐다 [사실]",
  "일정: 시정안 제출로 집행위 심사 기한이 영업일 10일 자동 연장돼 11월로 넘어갔고, 집행위는 경쟁사·고객을 상대로 시정안을 시험한 뒤 승인·추가 수정 요구·본조사 개시 가운데 하나를 정한다 [사실]",
  "기존: 합병 완료는 2026년 말~2027년 초로 예상됐다 [사실]"
 ],
 "basis": "verified",
 "check": "10월 15일 시정안 제출, 차량 보수용 도료 매각, 기한 연장은 검색 결과 요약으로 확인",
 "src": [
  {"o": "MLex", "d": "2026-10-16", "u": "https://www.mlex.com/mlex/mergers-acquisitions/articles/2538287"},
  {"o": "European Coatings", "d": "2026-10", "u": "https://www.european-coatings.com/news/markets-companies/akzo-nobel-axalta-merger-eu-approval-may-hinge-on-sale-of-akzonobels-vehicle-refinish-business/"},
  {"o": "Traders Union", "d": "2026-10-16", "u": "https://tradersunion.com/news/companies/show/3848182-akzonobel-axalta-eu-merger-review/"}
 ],
 "inds": ["industrial"], "nodes": [],
 "vc": [
  {"ind": "industrial", "node": "materials", "f": "공급", "dir": "down", "k": "예상", "t": "악조노벨·액설타 합병으로 코팅 공급자 감소"}
 ],
 "added": "이번 로이터 1건으로 두 회사가 차량 보수용 도료 사업 매각 시정안을 실제로 제출해 EU 심사 기한이 연장됐다는 점이 추가됐다",
 "items": [
  it("악조노벨·액설타, 250억 달러 합병 EU 승인 위해 시정안 제출", R, "2026-10-17", "https://www.reuters.com/business/akzonobel-axalta-offer-remedies-bid-eu-approval-25-billion-deal-2026-10-16/",
     "악조노벨과 액설타가 EU에 차량 보수용 도료 사업 매각 시정안을 내면서, 합병 심사 기한이 영업일 10일 늘어 11월로 넘어갔다")
 ]
})

# G1-085
items.append({
 "cid": "G1-085", "attachTo": "",
 "title": "멕시코, 125억 달러 규모 재생에너지 사업 승인 앞둬…8.2GW 추가",
 "one": "멕시코 국영 전력사 CFE 이사회가 20일 풍력·태양광 위주 60여 개 민관 합작 사업 승인을 표결할 예정이면서, 약 125억 달러를 들여 8.2GW의 발전 설비가 더해질 전망이다",
 "facts": [
  "무엇이: CFE 이사회는 10월 20일 60개가 넘는 재생에너지 사업 승인을 표결할 예정이라고 소식통이 전했다 [사실]",
  "규모: 사업은 주로 풍력·태양광으로 약 8.2GW를 더하며, 송전 투자에 따라 달라지는 비용은 약 125억 달러로 추정된다 [사실]",
  "구조: 셰인바움 대통령의 민간·CFE 협력 계획의 일부이며, 멕시코 법은 모든 발전소에서 국가 지분 54% 이상을 요구한다 [사실]",
  "변수: 다른 소식통은 최종 승인 사업 수가 더 적을 수 있다고 했다 [사실]"
 ],
 "basis": "partial",
 "check": "표결일·사업 수·8.2GW·125억 달러는 블룸버그 리네아(블룸버그 계열 스페인어 매체) 기사의 검색 결과 요약으로 확인해 독립 출처 확인은 아님",
 "src": [
  {"o": "Bloomberg Línea", "d": "2026-10-16", "u": "https://bloomberglinea.com/latinoamerica/mexico/mexico-perfila-aprobar-proyectos-de-energia-renovable-por-us12500-millones"}
 ],
 "inds": ["power"], "nodes": ["power/developers"],
 "vc": [
  {"ind": "power", "node": "developers", "f": "공급", "dir": "up", "k": "예상", "t": "멕시코 8.2GW 재생에너지 사업 승인 표결 앞둬"}
 ],
 "items": [
  it("멕시코, 125억 달러 규모 재생에너지 발전 사업 승인 예정", B, "2026-10-17", "https://www.bloomberg.com/news/articles/2026-10-16/mexico-set-to-approve-12-5-billion-in-renewable-power-projects")
 ]
})

d = {"agent": "W3", "searches_used": 16, "fetches_used": 0, "items": items, "skipped": []}

# checks
tail = re.compile(r' \((제목 기준|채널 전언)\)$')
bad = []
for x in items:
    multi = len(x["items"]) > 1 or x["attachTo"]
    n = len(tail.sub('', x["one"]))
    lo, hi = (90, 160) if multi else (80, 130)
    if not (lo <= n <= hi): bad.append((x["cid"], "one", n))
    if not (20 <= len(x["title"]) <= 50): bad.append((x["cid"], "title", len(x["title"])))
    if not (2 <= len(x["facts"]) <= 5): bad.append((x["cid"], "facts", len(x["facts"])))
    if multi:
        a = len(tail.sub('', x.get("added", "")))
        if not (60 <= a <= 140): bad.append((x["cid"], "added", a))
    for i in x["items"]:
        if not (25 <= len(i["t"]) <= 60): bad.append((x["cid"], "t", len(i["t"]), i["t"]))
        if multi:
            s = len(tail.sub('', i.get("s", "")))
            if not (45 <= s <= 110): bad.append((x["cid"], "s", s, i["s"][:30]))
        elif "s" in i: bad.append((x["cid"], "s-not-allowed"))
    for v in x["vc"]:
        if not (12 <= len(v["t"]) <= 45): bad.append((x["cid"], "vc", len(v["t"])))
    for f in x.get("fed", []):
        if not (20 <= len(f["t"]) <= 70): bad.append((x["cid"], "fed", len(f["t"])))
    blob = json.dumps(x, ensure_ascii=False)
    if "{{" in blob or "**" in blob: bad.append((x["cid"], "markup"))
    for fa in x["facts"]:
        if "|" in fa: bad.append((x["cid"], "pipe"))
for b in bad: print(b)
json.dump(d, open(OUT, "w"), ensure_ascii=False, indent=1)
print("written", len(items))
