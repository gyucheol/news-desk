import json, re

T = "텔레그램 "
def it(t, o, d, u): return {"t": t, "o": o, "d": d, "u": u}

items = []

items.append({"cid": "C006", "attachTo": "n-rtr-0014",
 "title": "이란 \"美 호르무즈 답변 불충분\"…영국은 페어퍼드 기지 사건 IRGC 배후 지목",
 "one": "미국이 해상 봉쇄와 그림자 선단 제재를 이어가는 가운데 이란이 호르무즈 재개방 제안에 대한 미국 답변을 불충분하다고 하고 영국 총리는 페어퍼드 기지 사건 배후로 혁명수비대를 지목해, 해협 재개방과 원유 수출 정상화가 더 늦어질 수 있다",
 "facts": [
  "무엇이: 이란 측 레자에이는 10월 11일 카타르를 거쳐 온 미국 답변이 일부 조건만 받아들여 불충분하며 조건이 충족될 때까지 호르무즈 개방도 협상도 없다고 했습니다 [사실]",
  "제안 내용: 이란의 7일 제안은 해협 재개방·핵협상 재개를 미국 해상 봉쇄 해제, 원유 판매 제한 완화와 맞바꾸는 것이고, 우라늄 농축이 핵심 쟁점입니다 [사실]",
  "영국: 버넘 총리는 9월 27일 페어퍼드 기지 인근 체포 사건이 혁명수비대 지시였을 가능성이 크다고 의회에 밝혔고, 영국은 이란인 2명을 제재했으며 약 30개국이 이란의 혼합 공격을 규탄했습니다 [사실]",
  "기존 흐름: 미 재무부는 10월 8일 그림자 선단 유조선 17척을 추가 제재했고, 이란은 8월 25일 이후 원유 수출 선적이 없습니다 [사실]",
  "군사·외교: 이란 드론이 10월 12일 이라크 에르빌주 코야의 쿠르드민주당 캠프를 타격했고, 60개국이 해협 통행료 반대 선언을 지지했습니다 [채널]"],
 "basis": "verified",
 "check": "미국 답변 불충분 발언과 버넘 총리의 IRGC 지목은 검색 결과 요약으로 확인. 60개국 통행료 반대 선언과 코야 드론 공격은 확인 못 함(60개국은 로이터 제목, 드론은 채널).",
 "src": [{"o": "Shafaq News", "d": "2026-10-11", "u": "https://shafaq.com/en/World/Iran-deems-US-response-to-its-proposal-insufficient"},
         {"o": "SAFETY4SEA", "d": "2026-10-12", "u": "https://safety4sea.com/iran-says-us-response-to-its-7-day-proposal-to-reopen-hormuz-is-insufficient/"},
         {"o": "The Globe and Mail", "d": "2026-10-12", "u": "https://www.theglobeandmail.com/world/article-iran-irgc-raf-fairford-incident/"}],
 "inds": ["macro"], "nodes": ["macro/geo", "macro/commodity"],
 "items": [
  it("이란 외무부 \"美의 러시아 지원 요청은 호르무즈 위기 지속 증거\"", T+"미국 주식 인사이더", "2026-10-12", "https://t.me/insidertracking/66030"),
  it("이란 외무부 \"미국의 최신 반응 주시하며 대응할 것\"", T+"하나증권 중국전략", "2026-10-12", "https://t.me/HANAchina/70279"),
  it("이란 \"호르무즈 재개방 제안에 대한 미국 답변 불충분\"", "로이터", "2026-10-12", "https://www.reuters.com/world/middle-east/iran-says-us-response-its-proposal-reopen-hormuz-was-insufficient-2026-10-11/"),
  it("이란 샤헤드-136 드론, 이라크 에르빌주 코야의 쿠르드민주당 캠프 타격", T+"미국 주식 인사이더", "2026-10-12", "https://t.me/insidertracking/66042"),
  it("이란 \"검토 끝나면 호르무즈 제안 관련 미국 답변에 회신\"", "로이터", "2026-10-12", "https://www.reuters.com/world/middle-east/iran-says-it-will-reply-us-response-hormuz-proposal-once-review-over-2026-10-12/"),
  it("오스틴 전 美 국방장관 \"이란 전쟁에 쉬운 출구 없다\"", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/iran-war-has-no-easy-way-out-former-us-defense-secretary-says"),
  it("영국 \"미군 사용 공군기지 사건, 이란 혁명수비대가 지시\"", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-12/uk-says-iran-s-irgc-directed-incident-at-airbase-used-by-us"),
  it("60개국, 해협 통행료 부과에 반대하는 선언 지지", "로이터", "2026-10-13", "https://www.reuters.com/world/asia-pacific/sixty-countries-back-declaration-opposing-strait-tolls-2026-10-12/"),
  it("버넘 英 총리 \"RAF 페어퍼드 사건, 이란 혁명수비대 배후 가능성\"", "로이터", "2026-10-13", "https://www.reuters.com/world/uk/uk-pm-burnham-says-irans-irgc-likely-behind-raf-fairford-incident-2026-10-12/"),
 ]})

items.append({"cid": "C011", "attachTo": "",
 "title": "中 완성차 유럽 현지화 가속…BYD 인력 4만 명, 샤오펑 2030년 50만 대 목표",
 "one": "BYD가 유럽 인력을 2030년 4만 명 이상으로 늘리고 샤오펑이 2030년 유럽 연 50만 대 판매를 목표로 현지 생산 확대에 나서는 가운데 지리의 포드 스페인 인수도 승인돼, 유럽 완성차 업체와의 현지 경쟁이 거세질 전망이다",
 "facts": [
  "무엇이: BYD 스텔라 리 부사장은 유럽 인력을 현재 1만여 명에서 2030년 4만 명 넘게 늘리겠다고 했고, 헝가리 첫 공장은 4분기 본격 생산, 프랑스·스페인이 추가 공장 후보입니다 [사실]",
  "샤오펑: 허샤오펑 회장은 2030년 유럽 연 50만 대(글로벌 100만 대의 절반) 판매를 목표로, 오스트리아 그라츠 위탁생산사 마그나와 증산을 논의 중이며 생산능력을 최대 제약으로 꼽았습니다 [사실]",
  "비교: 포드의 지난해 유럽 판매는 42만 6천 대, 오펠은 40만 대로 샤오펑 목표가 이를 넘어섭니다 [채널]",
  "배경: EU·중국 간 하이브리드 수입 제한 합의 뒤 BYD·체리가 유럽 공장 건설을 서두를 것으로 예상되고, 중국은 지리의 포드 스페인 인수를 승인했습니다 [제목]"],
 "basis": "verified",
 "check": "BYD 4만 명·샤오펑 50만 대 목표는 검색 결과 요약으로 확인. 지리의 포드 스페인 인수 승인과 하이브리드 제한 회피 공장 가속은 기사 제목 기준.",
 "src": [{"o": "Quartz", "d": "2026-10-12", "u": "https://qz.com/byd-europe-workforce-40000-hiring-2030-101226"},
         {"o": "Briefs", "d": "2026-10-12", "u": "https://www.briefs.co/news/xpeng-targets-500-000-yearly-sales-in-europe-by-decade-end/"}],
 "inds": ["auto"], "nodes": [],
 "items": [
  it("BYD \"미국 시장 없이도 5년 내 토요타·폭스바겐 추월\"", T+"하나증권 중국전략", "2026-10-12", "https://t.me/HANAchina/70234"),
  it("中 BYD·체리, 하이브리드 제한 피하려 유럽 공장 건설 가속 전망", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/china-s-byd-chery-expected-to-speed-up-europe-factories-to-evade-hybrid-limit"),
  it("중국 당국, 지리자동차의 포드 스페인 법인 인수 승인", "로이터", "2026-10-12", "https://www.reuters.com/business/retail-consumer/china-approves-geely-acquisition-ford-espaa-2026-10-12/"),
  it("中 BYD, 프랑스 공장 계획 검토 중…임원 BFM 인터뷰", "로이터", "2026-10-12", "https://www.reuters.com/world/china/chinas-byd-studying-plans-factory-france-executive-tells-bfm-2026-10-12/"),
  it("BYD, 대규모 채용으로 유럽 인력 4만 명까지 확대 계획", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/byd-plans-hiring-spree-and-bolster-european-workforce-to-40-000"),
  it("中 샤오펑, 2030년까지 유럽에서 포드·오펠 추월 노려", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-12/china-s-xpeng-seeks-to-edge-past-ford-opel-in-europe-by-2030"),
  it("샤오펑, 2030년 말 유럽 연 50만 대 판매 목표…마그나와 증산 논의", T+"하나증권 중국전략", "2026-10-13", "https://t.me/HANAchina/70305"),
  it("샤오펑 임원 \"현지 경쟁 앞서 유럽 생산 확대할 것\"", "로이터", "2026-10-13", "https://www.reuters.com/world/china/xpeng-executive-says-ev-maker-will-expand-european-production-ahead-local-2026-10-12/"),
 ]})

items.append({"cid": "C017", "attachTo": "n-tg-0140",
 "title": "美 국채 매도에 30년물 입찰 5.6%대…월가는 20년물 발행 중단론 재점화",
 "one": "30년물 입찰 금리가 2000년 이후 최고로 치솟고 국채 금리가 2월 이후 120bp 오르며 채권시장이 사실상 긴축을 대신하자, 월가에서 재무부의 20년물 축소·폐지론이 다시 나와 11월 4일 차환 계획이 장기물 수급의 분수령이 될 전망이다",
 "facts": [
  "무엇이: 씨티는 재무부가 20년물·30년물 입찰을 회당 30억 달러씩 줄이고 단기채로 메우며 20년물을 폐지할 수도 있다고 봤고, 변경은 11월 4일 분기 차환 발표 때 나올 것으로 예상했습니다 [사실]",
  "반론: BNP파리바는 20년물 축소·폐지가 장기금리를 지속적으로 낮추지 못하고 공황 신호로 읽혀 조달 비용을 오히려 높일 수 있다고 경고했고, 재무부는 아직 변경을 확인하지 않았습니다 [사실]",
  "기존: 10월 8일 30년물 220억 달러가 5.618%로 2000년 8월 이후 최고에 낙찰됐고, 2026회계연도 재정적자는 1조 9,930억 달러로 추정됐습니다 [사실]",
  "시장 진단: 모건스탠리 윌슨은 2월 이후 국채 금리가 누적 120bp 올라 채권시장이 연준 대신 긴축 중이라 했고, 골드만은 유가와 채권의 연동이 약해졌다고 지적했습니다 [채널]",
  "파급: 금리 급등이 모기지 헤지 매도를 불러 채권시장 압력을 키우고 있다는 보도가 나왔습니다 [제목]"],
 "basis": "verified",
 "check": "20년물 축소·폐지론과 씨티·BNP 시각은 검색 결과 요약으로 확인. 120bp 상승, 모기지 헤지 매도는 채널·제목 기준.",
 "src": [{"o": "Bloomingbit", "d": "2026-10-12", "u": "https://en.bloomingbit.io/feed/news/121722"},
         {"o": "Futu News", "d": "2026-10-12", "u": "https://news.futunn.com/en/post/1000819010/citi-bessent-may-slash-long-term-debt-issuance-next-month"}],
 "inds": ["macro"], "nodes": ["macro/rates", "macro/fiscal"],
 "items": [
  it("BofA 하트넷 \"연준의 선제 금리 인상이 오히려 증시 최대 호재\"", T+"하나증권 중국전략", "2026-10-12", "https://t.me/HANAchina/70255"),
  it("모건스탠리 윌슨 \"채권시장이 연준 대신 금리 인상 중\"", T+"하나증권 중국전략", "2026-10-12", "https://t.me/HANAchina/70297"),
  it("골드만 \"국채 금리 급등에 유가·채권 연동 약화, 변동성 매도 청산 위험\"", T+"하나증권 중국전략", "2026-10-12", "https://t.me/HANAchina/70299"),
  it("美 금리 급등이 모기지 헤지 촉발해 채권시장 압력 가중", "로이터", "2026-10-12", "https://www.reuters.com/business/us-yield-surge-triggers-mortgage-hedging-adds-bond-market-pressure-2026-10-12/"),
  it("월가, 美 20년물 국채 발행 폐지론 다시 꺼내 들어", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-12/wall-street-revives-the-case-for-scrapping-the-us-20-year-bond"),
  it("월가 전략가들 \"채권 급락 뒤 듀레이션에 가치\"", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-12/wall-street-strategists-see-value-in-duration-after-bond-rout"),
  it("美 20년물 발행 중단 검토설…BNP \"공황 유발 우려\", 씨티 \"초과수익 전망\"", T+"하나증권 중국전략", "2026-10-13", "https://t.me/HANAchina/70316"),
 ]})

items.append({"cid": "C024", "attachTo": "n-bbg-0049",
 "title": "AI 금융 위험 재평가…DBS \"시장이 AI 대출 위험 다시 가격 매겨\", 순환 금융 경고",
 "one": "빅테크의 AI 차입이 채권시장을 포화시키고 오라클 CDS가 사상 최고권에 오른 가운데 DBS CEO가 시장이 AI 금융 위험을 다시 가격 매기고 있다고 밝히고 순환 금융 구조 경고가 이어져, 약한 차입자의 신용등급과 조달 비용이 악화될 수 있다",
 "facts": [
  "무엇이: DBS 탄수산 CEO는 투자자들이 AI 인프라 금융에 더 높은 수익과 구조 점검을 요구하며 위험을 재평가하고 있고, 약한 기업은 신용등급이 깎일 수 있다고 했습니다 [사실]",
  "DBS 노출: DBS는 올해 칩·데이터센터 위주로 약 250억 싱가포르달러의 AI 거래를 주선했으나 자체 장부에는 일부만 보유했습니다 [사실]",
  "현금흐름 격차: S&P 글로벌 집계로 5대 AI 반도체 기업 잉여현금흐름은 2026년 5,000억 달러를 넘는 반면, 5대 클라우드 기업 합계는 85억 달러 적자가 예상됩니다 [채널]",
  "기존: 스페이스X·브로드컴·오라클이 일주일도 안 돼 1,500억 달러 넘는 조달에 나섰고, 오라클 2066년물 수익률은 8.45%였습니다 [사실]",
  "구조 위험: AI를 떠받치는 세계적 순환 금융 고리와 AI 붐이 키우는 금융 위험을 다룬 분석이 나왔습니다 [제목]"],
 "basis": "verified",
 "check": "DBS CEO 발언과 250억 싱가포르달러 규모는 검색 결과 요약으로 확인. S&P 현금흐름 수치는 채널, 순환 금융 기사 내용은 제목 기준. 빅테크 AI 차입 해설 기사는 AI 자금 조달이라 items에서 뺌.",
 "src": [{"o": "Fintech Singapore", "d": "2026-10-12", "u": "https://fintechnews.sg/138858/ai/dbs-ai-financing-risk-repricing/"},
         {"o": "The Edge Singapore", "d": "2026-10-12", "u": "https://www.theedgesingapore.com/news/tech/dbs-ceo-tan-says-market-repricing-risks-ai-financing"}],
 "inds": ["macro"], "nodes": ["macro/semis", "macro/liquidity"],
 "items": [
  it("DBS CEO 탄 \"시장이 AI 금융 위험을 다시 가격 매기고 있다\"", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/dbs-ceo-tan-says-market-is-repricing-risks-on-ai-financing"),
  it("AI 반도체 현금흐름 5,000억 달러 급증, 클라우드 5사는 마이너스 전환 전망", T+"부의 나침반", "2026-10-12", "https://t.me/w_compass/7254"),
  it("AI 공급망 부담은 걱정거리 중 가장 작은 것일 수 있다", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/newsletters/2026-10-12/ai-supply-chain-strains-may-be-the-least-of-our-worries"),
  it("AI를 떠받치는 거대한 세계 순환 금융 고리의 내막", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-12/inside-the-giant-global-circular-financing-loop-driving-ai"),
  it("AI 붐은 어떻게 세계 금융 위험을 키우고 있나", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/features/2026-10-12/how-the-ai-boom-is-fueling-global-financial-risks"),
 ]})

items.append({"cid": "C031", "attachTo": "",
 "title": "골드만, 글로벌 주식 비중확대 상향…美 주식위험프리미엄은 24년 만에 마이너스",
 "one": "골드만삭스가 3분기 실적 기대와 낮아진 밸류에이션을 들어 글로벌 주식 3개월 전망을 비중확대로 올리고 2027년 자사주 매입 1.7조 달러를 예상했지만, 미국 주식위험프리미엄은 24년 만에 마이너스로 떨어져 주식의 국채 대비 기대 보상이 사라지고 있다",
 "facts": [
  "무엇이: 골드만삭스는 10월 12일 글로벌 주식 3개월 전망을 중립에서 비중확대로 올리고 12개월 비중확대를 유지했으며, S&P 500 3분기 이익 증가율을 약 27%로 봤습니다 [사실]",
  "밸류에이션: 골드만 기준 S&P 500 선행 PER은 19.1배로 연초 약 22배에서 낮아졌고, 미국·아시아 비중확대, 유럽 비중축소, 국채 12개월 비중확대를 제시했습니다 [사실]",
  "수급: 골드만은 2027년 미국 기업 자사주 매입을 사상 최대 1.7조 달러, 주식 발행을 6,000억 달러로 전망했고 올해 발행은 약 4,310억 달러로 98% 늘었습니다 [채널]",
  "위험 보상: 미국 주식위험프리미엄이 24년 만의 최저로 마이너스가 됐고, 30년물 물가연동국채 금리는 3.40%에 근접했습니다 [채널]",
  "남은 변수: 골드만은 금리·에너지 가격 상승과 중간선거 불확실성을 위험으로 꼽았고, 연말 랠리는 실적에 달렸다는 분석이 나왔습니다 [사실]"],
 "basis": "partial",
 "check": "골드만 상향과 27%·19.1배 수치는 검색 결과 요약으로 확인. 자사주 1.7조 달러 전망과 ERP 마이너스는 확인 못 함(채널).",
 "src": [{"o": "Unusual Whales", "d": "2026-10-12", "u": "https://unusualwhales.com/news/goldman-sachs-bullish-stocks-overweight-equities"},
         {"o": "KuCoin News", "d": "2026-10-12", "u": "https://www.kucoin.com/news/flash/goldman-sachs-upgrades-global-stocks-to-overweight-forecasts-27-q3-earnings-growth-for-s-p-500"}],
 "inds": ["macro"], "nodes": ["macro/liquidity", "macro/rates"],
 "items": [
  it("골드만 전략가들, 이익 개선에 글로벌 주식 투자의견 상향", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/goldman-strategists-upgrade-global-stocks-on-earnings-boost"),
  it("비틀거리는 주식 랠리, 연말 상승은 실적에 달려", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/stumbling-equity-rally-hinges-on-earnings-for-year-end-boost"),
  it("골드만, 실적 낙관에 글로벌 주식 투자의견 상향", "로이터", "2026-10-12", "https://www.reuters.com/business/goldman-upgrades-global-equities-earnings-optimism-2026-10-12/"),
  it("美 주식위험프리미엄 24년 만에 최저…마이너스 전환", T+"TNBfolio", "2026-10-13", "https://t.me/TNBfolio/71507"),
  it("골드만 \"美 기업 2027년 자사주 1.7조 달러 매입, 주식 공급 충격 완화\"", T+"하나증권 중국전략", "2026-10-13", "https://t.me/HANAchina/70306"),
 ]})

items.append({"cid": "C038", "attachTo": "n-rtr-0022",
 "title": "IMF 지원 받는 파키스탄, 4%대 성장·민영화 10억 달러 목표…차입국 협의체 의장 맡아",
 "one": "파키스탄이 IMF와 약 12억 달러 지원 실무합의를 맺은 데 이어 4% 넘는 성장과 국영기업 매각으로 10억 달러 이상 조달을 내걸고 차입국 협의체 의장을 맡으면서, 세네갈 등 고유가에 짓눌린 취약 신흥국의 부채 조정 논의가 커지고 있다",
 "facts": [
  "무엇이: 아우랑제브 파키스탄 재무장관은 고유가에도 이번 회계연도 성장률이 4%를 넘고, 국영기업 5~6곳 매각으로 10억 달러 넘게 조달할 수 있다고 했습니다 [사실]",
  "협의체: 파키스탄은 10월 12일 방콕에서 이집트로부터 개도국 차입국 플랫폼 운영위원회 의장직을 넘겨받았고, 회원국은 30개국이 넘습니다 [사실]",
  "기존: IMF는 10월 7일 파키스탄과 실무합의를 맺어 이사회 승인 시 약 12억 달러를 집행하며, 조건은 연료 지원 조기 폐지와 GDP 대비 2% 기초재정흑자입니다 [사실]",
  "다른 나라: 세네갈은 빈국 부채 해결을 위한 국제 논의의 초점이 됐고, 12월까지 채권단과 채무조정 합의를 목표로 합니다 [제목]",
  "신용: 파키스탄은 추가 신용등급 상향을 노리고 있습니다 [제목]"],
 "basis": "verified",
 "check": "4% 성장·10억 달러 민영화·차입국 플랫폼 의장 취임은 검색 결과 요약으로 확인. 세네갈과 등급 상향 목표는 제목 기준.",
 "src": [{"o": "Business Recorder", "d": "2026-10-12", "u": "https://www.brecorder.com/news/40443777/pakistan-sees-growth-above-4-looks-to-raise-more-than-1-billion-from-privatisation"},
         {"o": "Business Recorder", "d": "2026-10-12", "u": "https://www.brecorder.com/news/40443812/aurangzeb-assumes-chairmanship-of-borrowers-platform"}],
 "inds": ["macro"], "nodes": ["macro/fiscal", "macro/growth"],
 "items": [
  it("세네갈, 빈국 부채 해결 위한 국제적 노력의 초점으로", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/features/2026-10-11/senegal-puts-focus-on-global-bid-to-help-poor-countries-tackle-debt"),
  it("파키스탄 재무장관 \"추가 신용등급 상향 노린다\"", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/pakistan-targets-another-ratings-upgrade-says-finance-minister"),
  it("파키스탄, 4% 넘는 성장 전망…민영화로 10억 달러 이상 조달 추진", "로이터", "2026-10-12", "https://www.reuters.com/world/asia-pacific/pakistan-sees-growth-above-4-looks-raise-more-than-1-billion-from-privatisation-2026-10-12/"),
  it("파키스탄, '퍼펙트 스톰' 직면한 세계 차입국 협의체 의장 맡아", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/pakistan-to-chair-global-borrowers-group-facing-perfect-storm"),
 ]})

items.append({"cid": "C046", "attachTo": "",
 "title": "LVMH 3분기 패션·가죽 매출 5% 감소…중국 수요 10%대 중반 급감",
 "one": "LVMH가 3분기 그룹 매출을 1% 늘렸지만 매출 절반을 차지하는 패션·가죽 부문이 중국 수요 급감으로 5% 줄어 예상보다 크게 부진하면서, 2분기 반등 뒤 명품 업종 회복 기대가 꺾이고 있다",
 "facts": [
  "무엇이: LVMH 3분기 그룹 유기적 매출은 1% 늘었으나, 패션·가죽 부문은 시장 예상(약 1.6~1.8% 감소)보다 큰 5% 감소를 기록했습니다 [사실]",
  "지역: 아시아는 한 자릿수 중반 감소, 중국 수요는 10%대 중반 줄었고 미국은 5% 늘었습니다. CFO는 중국 소비심리 약화와 중동 정세를 부담으로 꼽았습니다 [사실]",
  "누적: 9개월 패션·가죽 매출은 264억 유로로 유기적 2% 감소했고, 2분기에 2년 만의 성장 전환을 이뤘으나 이어가지 못했습니다 [사실]",
  "요인: 분석가들은 중국의 부유층 세무 단속과 루이비통의 중국 차 브랜드 상표 분쟁을 영향으로 들었습니다 [사실]"],
 "basis": "verified",
 "check": "패션·가죽 5% 감소, 중국 10%대 중반 감소, 264억 유로는 검색 결과 요약으로 확인.",
 "src": [{"o": "WWD", "d": "2026-10-12", "u": "https://wwd.com/business-news/financial/lvmh-q3-sales-fashion-leather-goods-down-5-percent-1239342984/"},
         {"o": "FashionNetwork", "d": "2026-10-12", "u": "https://us.fashionnetwork.com/news/Lvmh-third-quarter-sales-dragged-down-by-weak-chinese-demand-for-flagship-brands,1875112.html"}],
 "inds": ["consumer"], "nodes": [],
 "items": [
  it("LVMH 핵심 사업부 매출, 中 수요 약화에 급감", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-12/lvmh-sales-at-key-unit-fall-as-china-woes-hurt-louis-vuitton"),
  it("LVMH 3분기 매출 예상 하회…패션·가죽 부문 축소", "로이터", "2026-10-13", "https://www.reuters.com/business/retail-consumer/lvmh-third-quarter-sales-below-expectations-fashion-leather-division-shrinks-2026-10-12/"),
  it("LVMH 핵심 사업부 매출, 中 수요 부진에 하락", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/newsletters/2026-10-12/lvmh-sales-at-key-unit-slide-on-weak-china-demand"),
  it("LVMH 3분기 핵심 패션·가죽 매출 5% 감소, 중국 부진에 예상 하회", T+"하나증권 중국전략", "2026-10-13", "https://t.me/HANAchina/70311"),
 ]})

items.append({"cid": "C056", "attachTo": "n-bbg-0216",
 "title": "와인 수요 부진 속 구조조정…TWE, 로즈마운트 등 3개 브랜드 오틀리 가문에 매각",
 "one": "캘리포니아 와인 공급 과잉으로 나파 고급 와인이 유통업체 상표로 헐값에 팔리는 가운데 펜폴즈 모회사 TWE가 76개 브랜드를 30개로 줄이려 로즈마운트 등 3개 브랜드를 매각하고 일부 와인업체는 아가베로 눈을 돌려, 와인 자산 정리가 이어지고 있다",
 "facts": [
  "무엇이: 트레저리 와인 에스테이트(TWE)가 로즈마운트·잉골드비·시크릿스톤 브랜드를 오틀리 가문의 A.G. 오틀리 와인즈에 팔기로 했고, 거래는 10월 23일 마무리 예정이며 가격은 공개되지 않았습니다 [사실]",
  "배경: TWE는 76개 브랜드를 30개 핵심 브랜드로 줄이는 중이며, 8월에 10억 8천만 호주달러의 법정 순손실을 냈습니다 [사실]",
  "기존: 캘리포니아 와인 공급 과잉으로 병당 150달러 수준 와인이 유통업체 상표로 30달러 미만에 팔리고 있습니다 [사실]",
  "대안: 와인 수요 부진에 캘리포니아 와인업체들이 아가베 재배에 베팅하고 있습니다 [제목]"],
 "basis": "verified",
 "check": "TWE 브랜드 매각과 10월 23일 완료, 76→30개 축소, 순손실은 검색 결과 요약으로 확인. 아가베 전환은 제목 기준.",
 "src": [{"o": "Winetitles", "d": "2026-10-12", "u": "https://winetitles.com.au/twe-announces-sale-of-rosemount-ingoldby-and-secret-stone-to-oatley-family/"},
         {"o": "Business News Australia", "d": "2026-10-12", "u": "https://www.businessnewsaustralia.com/articles/oatleys-buy-back-rosemount-as-treasury-wine-trims-stable-from-76-brands-to-30.html"}],
 "inds": ["consumer"], "nodes": [],
 "items": [
  it("호주 억만장자 가문, 펜폴즈 모회사에서 와인 브랜드 3개 인수", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/billionaire-australian-family-buys-three-wine-brands-from-penfolds-maker"),
  it("와인 수요 급감에 캘리포니아 와인업체들, 아가베에 베팅", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/features/2026-10-12/california-winemakers-bet-on-agave-as-wine-demand-slumps"),
  it("호주 트레저리 와인, 로즈마운트를 창업자 오틀리 가문에 되팔아", "로이터", "2026-10-12", "https://www.reuters.com/legal/transactional/australias-treasury-wine-sells-rosemount-back-founding-oatley-family-2026-10-12/"),
 ]})

items.append({"cid": "C064", "attachTo": "n-rtr-0054",
 "title": "인테사, MPS 인수가 상향에 주주 지지 확보…MPS \"상향안에도 불확실성 남아\"",
 "one": "칼타지로네·델핀 등 주요 주주가 MPS의 방어용 인수안에 반대하는 가운데 인테사가 현금 8억 유로를 얹어 350억 유로 안팎으로 제안을 높이자 MPS가 이사회를 열고 불확실성이 남는다고 반박해, 10월 29일 주총에서 방어안 통과가 어려워지고 있다",
 "facts": [
  "무엇이: 인테사는 MPS 주주가 방어안을 부결하는 경우에만 주는 현금 8억 유로를 더해, MPS 1주당 현금 1.25유로와 인테사 신주 1.6주를 제시했습니다 [사실]",
  "MPS 반응: MPS는 10월 12일 상향안이 주주를 여러 불확실성에 노출시키고 대안 계획을 포기하게 한다며, 기대 수익이 실현된다는 보장이 없다고 밝혔습니다 [사실]",
  "표 대결: 방어안은 10월 29일 주총 출석 3분의 2 찬성이 필요한데, 지분 약 3분의 1을 가진 주주들이 반대하고 인테사 제안을 받을 것으로 알려졌습니다 [사실]",
  "기존: 칼타지로네(10.26%)가 방코BPM·방카제네랄리 인수안에 반대하기로 했고, 최대주주 델핀(17.6%)은 인테사 제안을 지지합니다 [사실]"],
 "basis": "verified",
 "check": "인테사 상향 조건, MPS 불확실성 성명, 3분의 2 요건은 검색 결과 요약으로 확인. 거래 규모는 보도마다 340억~350억 유로로 다름.",
 "src": [{"o": "Global Banking & Finance Review", "d": "2026-10-12", "u": "https://www.globalbankingandfinance.com/italys-mps-question-marks-remain-over-higher-intesa-bid/"},
         {"o": "Retail Banker International", "d": "2026-10-12", "u": "https://www.retailbankerinternational.com/news/intesa-sweetens-monte-paschi-bid/"}],
 "inds": ["fin"], "nodes": [],
 "items": [
  it("몬테데이파스키, 월요일 이사회 열어 인수합병 상황 점검", "로이터", "2026-10-12", "https://www.reuters.com/business/finance/monte-dei-paschi-hold-board-meeting-ma-situation-monday-2026-10-11/"),
  it("伊 MPS \"인테사 상향 제안에도 의문 남아\"", "로이터", "2026-10-13", "https://www.reuters.com/business/finance/italys-mps-says-question-marks-remain-over-higher-intesa-bid-2026-10-12/"),
 ]})

items.append({"cid": "C068", "attachTo": "",
 "title": "애플 COO, 폭스콘 정저우 방문해 첫 폴더블 '아이폰 듀오' 양산 점검",
 "one": "사비 칸 애플 COO가 10월 23일 출시를 앞둔 첫 폴더블폰 아이폰 듀오의 생산 규모를 늘리고 있다고 밝히고 주문량 30% 증가 보도까지 나오면서, 독점 조립을 맡은 폭스콘의 4분기 실적이 개선될 수 있다",
 "facts": [
  "무엇이: 사비 칸 애플 COO가 허난성 정저우 폭스콘 공장을 찾아 아이폰 듀오 공정과 아이폰 18 프로 카메라 모듈 라인 등을 둘러보고, 품질 기준에 맞춰 생산 규모를 늘리고 있다고 했습니다 [사실]",
  "일정: 아이폰 듀오는 10월 16일 사전예약, 10월 23일 판매를 시작하며 중국 폭스콘 공장이 독점 조립합니다 [사실]",
  "주문: 모듈 두께를 20% 줄인 새 스퍼터링 공정이 도입됐고, 애플이 주문량을 30% 늘렸으며 올해 판매는 약 600만 대로 예상됩니다 [채널]",
  "시장: 애플의 가세로 세계 폴더블폰 출하량이 13% 늘 것이라는 전망이 나왔고, 가격은 역대 최고인 약 316만 원입니다 [채널]"],
 "basis": "partial",
 "check": "COO 방문·생산 확대 발언과 출시 일정은 검색 결과 요약으로 확인. 주문 30% 증가, 600만 대, 316만 원은 확인 못 함(채널).",
 "src": [{"o": "Global Times", "d": "2026-10-12", "u": "https://www.globaltimes.cn/page/202610/1372124.shtml"},
         {"o": "AASTOCKS", "d": "2026-10-12", "u": "https://www.aastocks.com/en/stocks/news/aafn-con/now.1548768/latest-news"}],
 "inds": ["tech"], "nodes": [],
 "items": [
  it("애플 COO 폭스콘 정저우 방문…아이폰 듀오 주문 30% 늘려", T+"하나증권 중국전략", "2026-10-12", "https://t.me/HANAchina/70240"),
  it("애플 COO \"아이폰 듀오 생산 규모 확대 중\"…사전예약 앞두고 폭스콘 방문", T+"하나증권 중국전략", "2026-10-12", "https://t.me/HANAchina/70272"),
 ]})

items.append({"cid": "C076", "attachTo": "n-rtr-0013",
 "title": "인도 석탄난에 공장 정전 확산…철강공장 하루 10~12시간 단전, 태양광은 버려져",
 "one": "인도 석탄발전소 절반 가까이의 연료 재고가 필요량의 4분의 1 밑으로 떨어지자 콜인디아가 발전사 공급을 우선하면서 자가발전 연료를 못 구한 철강·화학 공장이 하루 최대 12시간 정전을 겪어, 석탄난이 산업 생산 감소로 번지고 있다",
 "facts": [
  "무엇이: 인도 전력부 자료로 10월 10일 기준 석탄발전소 절반 가까이의 연료 재고가 필요량의 4분의 1 미만으로 떨어졌습니다 [사실]",
  "산업 피해: 차티스가르주 소형 철강공장은 하루 10~12시간 정전으로 감산 중이고, 금속 제련·화학·제지 업체는 콜인디아가 계통 발전사에 우선 공급해 자가발전 연료를 구하지 못하고 있습니다 [사실]",
  "가격·수급: 콜인디아 현물 경매 프리미엄은 9월 기준가 대비 94%로 8월 59%에서 뛰었고, 10월 첫 10일 전력망 부족분은 하루 평균 약 4GW였습니다 [사실]",
  "원인: 2015년 이후 가장 약한 몬순으로 수력 발전이 줄고 더위로 냉방·관개 수요가 늘었습니다 [사실]",
  "역설: 7~8월 전력난 속에서도 태양광 발전의 4%가 버려졌다는 보고서가 나왔습니다 [제목]"],
 "basis": "verified",
 "check": "재고 수준, 철강공장 정전, 경매 프리미엄 94%, 4GW 부족은 검색 결과 요약으로 확인. 태양광 4% 낭비는 로이터 제목 기준.",
 "src": [{"o": "OilPrice.com", "d": "2026-10-12", "u": "https://oilprice.com/Latest-Energy-News/World-News/Small-Indian-Factories-Face-Blackouts-as-Coal-Stocks-Plunge.html"},
         {"o": "Engineering News", "d": "2026-10-12", "u": "https://www.engineeringnews.co.za/article/blackouts-hit-indian-factories-as-coal-crunch-feeds-into-economy-2026-10-12"}],
 "inds": ["coal", "power"], "nodes": ["coal/thermal", "coal/power", "power/demand", "power/grid"],
 "items": [
  it("석탄난이 경제로 번지며 인도 공장들 정전 피해", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/blackouts-hit-indian-factories-as-coal-crunch-feeds-into-economy"),
  it("인도, 7~8월 전력난 속 태양광 발전 4% 버려져…보고서", "로이터", "2026-10-12", "https://www.reuters.com/business/energy/india-wastes-4-solar-power-amid-power-shortages-july-august-report-shows-2026-10-12/"),
 ]})

items.append({"cid": "C084", "attachTo": "n-bbg-0175",
 "title": "PG&E, 산불 위험에 예방 단전 실행…캘리포니아 북부 약 1만 가구 전력 끊겨",
 "one": "캘리포니아 최대 전력회사 PG&E가 건조한 강풍으로 산불 위험이 커지자 예고했던 공공안전 단전을 실제로 시행하면서, 주말 사이 북부 여러 카운티의 약 1만~1만 1천 고객이 전기를 쓰지 못하고 월요일에도 복구가 늦어지고 있다",
 "facts": [
  "무엇이: PG&E가 10월 9일 금요일부터 공공안전 단전을 시작해 10월 11일 콜루사·글렌·섀스타·테하마·욜로 카운티 일부 약 1만 410 고객으로 범위를 넓혔습니다 [사실]",
  "규모: 11일 늦게는 9개 카운티 일부 약 1만 1천 고객이 단전 상태였고, 12일에도 섀스타·테하마·글렌에서 약 1만 고객이 전기가 끊겨 있었습니다 [사실]",
  "복구: 남부·센트럴밸리 일부 고객은 10일 복구됐고, 나머지는 기상 호전 뒤 설비 점검을 거쳐 복구됩니다 [사실]",
  "기존: PG&E는 10월 8일 약 1만 2,200 고객, 17개 카운티 일부에 단전 가능성을 통보했습니다 [사실]"],
 "basis": "verified",
 "check": "단전 시작일, 1만 410·1만 1천 고객, 12일 약 1만 고객 단전은 PG&E 발표와 지역 보도 검색 결과 요약으로 확인.",
 "src": [{"o": "PG&E", "d": "2026-10-11", "u": "https://www.pge.com/en/newsroom/currents/safety/potential-public-safety-power-shutoff-could-impact-small-portion.html"},
         {"o": "KRCR", "d": "2026-10-12", "u": "https://krcrtv.com/news/local/pge-confirms-wind-driven-shutoffs-nearly-10000-northstate-customers-affected-monday"}],
 "inds": ["power"], "nodes": ["power/grid"],
 "items": [
  it("PG&E, 캘리포니아 산불 위험 커지자 예방 단전 시작", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-11/pg-e-begins-preemptive-power-cuts-as-california-fire-risk-rises"),
 ]})

items.append({"cid": "C092", "attachTo": "",
 "title": "바이트댄스 숏드라마 앱 파인드라마, 1년 안 돼 1억 다운로드…수익화는 과제",
 "one": "바이트댄스가 중국 무료 숏드라마 앱 홍궈 모델을 해외에 옮긴 파인드라마가 출시 1년도 안 돼 1억 다운로드를 넘기고 인도네시아·브라질에서 빠르게 크고 있지만, 광고 수익화 여부가 가장 큰 불확실성으로 남아 있다 (채널 전언)",
 "facts": [
  "무엇이: 바이트댄스의 독립 숏드라마 앱 파인드라마가 출시 1년이 안 돼 다운로드 1억 회를 넘었고, 일간 이용자는 700만 명에 육박합니다 [채널]",
  "전략: 중국 홍궈의 무료 숏드라마 모델을 해외에 적용해 틱톡 트래픽과 현지 오리지널 콘텐츠로 인도네시아·브라질에서 성장 중입니다 [채널]",
  "과제: 이용자는 빠르게 늘지만 광고로 수익을 낼 수 있을지는 불확실하다는 평가입니다 [채널]"],
 "basis": "channel",
 "check": "검색 한도로 확인하지 않음. 월스트리트견문 기사 요약 기준.",
 "src": [],
 "inds": ["tech"], "nodes": [],
 "items": [
  it("바이트댄스 파인드라마 다운로드 1억 돌파…해외판 홍궈 노려", T+"하나증권 중국전략", "2026-10-12", "https://t.me/HANAchina/70261"),
 ]})

items.append({"cid": "C100", "attachTo": "",
 "title": "남아공 식료품 체인 복서, 저가 전략으로 이익 증가…새 CEO 선임",
 "one": "남아프리카공화국 식료품 체인 복서가 저가 전략에 힘입어 이익을 늘린 가운데 새 최고경영자를 선임하면서, 가격에 민감한 남아공 소비 시장에서 경영진 교체가 이뤄졌다 (제목 기준)",
 "facts": [
  "무엇이: 남아공 식료품 체인 복서가 새 CEO를 선임했습니다 [제목]",
  "실적: 낮은 가격 전략이 이익 증가에 도움이 됐습니다 [제목]"],
 "basis": "title",
 "check": "검색 한도로 확인하지 않음. 새 CEO 이름과 이익 수치는 확인 못 함.",
 "src": [],
 "inds": ["consumer"], "nodes": [],
 "items": [
  it("복서, 저가 전략에 이익 늘며 새 CEO 선임", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/boxer-appoints-new-ceo-as-south-african-grocer-s-profit-rises"),
 ]})

items.append({"cid": "C108", "attachTo": "n-rtr-0181",
 "title": "인도네시아 증시 2.5% 급락해 석 달 최저…규제 벌금설·MSCI 강등 우려",
 "one": "국부펀드 다난타라가 급락 시 매수 가능성을 열어둔 가운데 인도네시아 증시가 10월 12일 규제 벌금 추측 속에 2.5% 넘게 떨어져 석 달 만의 최저로 밀리면서, MSCI 강등 우려 속 세계 최약체 시장의 하방 압력이 커지고 있다",
 "facts": [
  "무엇이: 자카르타종합지수가 10월 12일 약 2.5% 하락해 5,936 안팎에 마감했고, 하락 종목이 632개에 달했습니다 [사실]",
  "업종: 인프라·금융·농업 업종에서 낙폭이 컸습니다 [사실]",
  "원인: 블룸버그는 규제 벌금을 둘러싼 추측을 급락 원인으로 들었으나, 다른 보도에서는 벌금 관련 내용을 찾지 못했습니다 [제목]",
  "기존: 다난타라는 일시적 외부 충격으로 밸류에이션이 매력적이면 개입할 수 있다고 했고, 다음 달 MSCI 검토에서 강등 우려가 있습니다 [사실]"],
 "basis": "partial",
 "check": "지수 약 2.5% 하락·5,936 마감은 검색 결과 요약으로 확인. 규제 벌금 추측이라는 원인은 확인 못 함(제목만). 낙폭은 보도마다 2.47~2.59%로 다름.",
 "src": [{"o": "Rancak Media", "d": "2026-10-12", "u": "https://rancakmedia.com/finance/101920/ihsg-plunges-2-59-to-5936-ptro-cuan-dssa-shares-tumble"}],
 "inds": ["fin"], "nodes": [],
 "items": [
  it("인도네시아 증시, 규제 당국 벌금 추측에 급락", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/indonesian-stocks-plunge-sending-benchmark-to-three-month-low"),
 ]})

items.append({"cid": "C116", "attachTo": "",
 "title": "英 채용업체 헤이스 순수수료 3% 감소…美·아시아 성장에 예상은 웃돌아",
 "one": "영국 채용업체 헤이스의 1분기 순수수료가 3% 줄었지만 미국·아시아 성장 덕에 예상보다 선방했고, 정규직 채용 수수료는 7% 줄어 유럽 고용 시장의 약세가 이어지고 있다",
 "facts": [
  "무엇이: 헤이스의 9월 말까지 1분기 그룹 순수수료가 동일 기준 3% 줄어 시장 예상(4% 감소)보다 나았습니다 [사실]",
  "지역: 미국 순수수료는 약 8% 늘었고, 독일은 6%, 프랑스는 16% 줄었습니다 [사실]",
  "부문: 정규직 순수수료는 채용 건수 12% 감소로 7% 줄었고, 임시·계약직은 1% 줄었습니다 [사실]",
  "전망: 헤이스는 단기 시장 여건이 안정적일 것으로 보고, 벨기에·브라질·중화권 등 사업에 대한 선택지를 검토 중입니다 [사실]"],
 "basis": "verified",
 "check": "순수수료 3% 감소·예상 4% 감소, 지역·부문 수치는 검색 결과 요약으로 확인. 주가 낙폭은 보도마다 달라 넣지 않음.",
 "src": [{"o": "Finimize", "d": "2026-10-12", "u": "https://finimize.com/content/hays-fee-slide-hit-fourteen-quarters-but-the-us-held-up"},
         {"o": "Global Banking & Finance Review", "d": "2026-10-12", "u": "https://www.globalbankingandfinance.com/british-recruiter-hays-tops-quarterly-net-fee-forecasts/"}],
 "inds": ["macro"], "nodes": ["macro/growth"],
 "items": [
  it("英 채용업체 헤이스, 美·아시아 성장에 분기 순수수료 예상 상회", "로이터", "2026-10-12", "https://www.reuters.com/business/british-recruiter-hays-tops-quarterly-net-fee-forecasts-strong-us-asia-growth-2026-10-12/"),
 ]})

items.append({"cid": "C124", "attachTo": "n-bbg-0150",
 "title": "쿠바, 美가 압류한 쿠바행 연료 화물 관여 부인…봉쇄 속 전력난 지속",
 "one": "미국이 쿠바 국영 연료회사로 향하던 바이오디젤 90건을 압류하며 연료 봉쇄를 이어가자 쿠바 정부가 해당 화물과 무관하다고 부인하면서, 정전이 심해진 쿠바의 연료 조달 경로를 둘러싼 공방이 이어지고 있다",
 "facts": [
  "무엇이: 쿠바가 미국이 압류한 쿠바행 연료 화물에 관여하지 않았다고 부인했습니다 [제목]",
  "기존: 미 당국은 10월 7일 쿠바 국영 연료회사 ENETEC로 향하던 바이오디젤 90건, 280만 달러어치를 압류했다고 발표했습니다 [사실]",
  "영향: 연료 봉쇄로 쿠바의 정전·물 부족·물가 상승이 심해졌다는 보도가 있습니다 [사실]"],
 "basis": "title",
 "check": "이번 부인 발언은 검색 한도로 확인하지 않음(로이터 제목 기준). 기존 사실은 기존 문서 근거.",
 "src": [],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "items": [
  it("쿠바, 美가 압류한 쿠바행 연료 화물 관여 부인", "로이터", "2026-10-12", "https://www.reuters.com/business/energy/cuba-denies-involvement-with-island-bound-fuel-shipments-seized-by-us-2026-10-12/"),
 ]})

items.append({"cid": "C132", "attachTo": "",
 "title": "그래머시 지원 업체, 360억 달러 소송에서 축출 시도 막아내",
 "one": "헤지펀드 그래머시가 자금을 댄 업체가 360억 달러 규모 소송에서 자신을 배제하려는 시도를 막아내면서, 거액 소송의 주도권과 소송 금융 투자자의 회수 가능성이 유지됐다 (제목 기준)",
 "facts": [
  "무엇이: 그래머시가 지원하는 업체가 360억 달러 규모 소송에서 축출 시도를 막아냈습니다 [제목]",
  "의미: 소송을 계속 이끌 수 있게 돼 투자 회수 가능성이 유지됩니다 [추론]"],
 "basis": "title",
 "check": "검색 한도로 확인하지 않음. 소송 상대와 사건 내용은 확인 못 함.",
 "src": [],
 "inds": ["fin"], "nodes": [],
 "items": [
  it("그래머시 지원 업체, 360억 달러 소송에서 축출 시도 막아내", "블룸버그", "2026-10-12", "https://www.bloomberg.com/news/articles/2026-10-12/gramercy-backed-firm-fends-off-ouster-from-36-billion-lawsuit"),
 ]})

items.append({"cid": "C140", "attachTo": "",
 "title": "독일 국가부채 비율, 2030년 GDP 대비 78.25%로 상승 전망",
 "one": "독일 안정위원회가 인프라 기금과 국방비 차입 완화로 국가부채 비율이 2025년 62.8%에서 2030년 78.25%로 오를 것으로 내다보면서, 독일 국채 공급 증가와 재정 여력 축소가 이어질 전망이다",
 "facts": [
  "무엇이: 연방·주 재정을 조율하는 독일 안정위원회는 10월 12일 국가부채가 2030년 GDP 대비 78.25%에 이를 것으로 전망했습니다 [사실]",
  "추이: 2025년 부채비율은 62.8%였고, 재정적자는 지난해 2.9%에서 내년 5.25%로 늘고 2030년에도 4.5%로 예상됩니다 [사실]",
  "원인: 5,000억 유로 인프라 기금과 국방비 차입 규정 완화가 부채 증가 요인으로 꼽힙니다 [사실]",
  "기준: EU 기준(적자 3%, 부채 60%)을 크게 웃도는 수준입니다 [사실]"],
 "basis": "verified",
 "check": "78.25%, 62.8%, 적자 경로는 검색 결과 요약으로 확인(로이터 보도를 옮긴 여러 매체 기준).",
 "src": [{"o": "The Standard (HK)", "d": "2026-10-12", "u": "https://www.thestandard.com.hk/finance/article/345270/Germanys-debt-to-GDP-ratio-expected-to-rise-to-7825pc-in-2030"}],
 "inds": ["macro"], "nodes": ["macro/fiscal"],
 "items": [
  it("독일 부채비율, 2030년 78.25%로 상승 전망", "로이터", "2026-10-12", "https://www.reuters.com/business/germanys-debt-to-gdp-ratio-expected-rise-7825-2030-2026-10-12/"),
 ]})

items.append({"cid": "C148", "attachTo": "",
 "title": "라이너스, 브라질 정부 지원 받아 희토류 공장 추진…메테오릭 칼데이라와 연계",
 "one": "라이너스가 브라질 정부 지원을 받아 희토류 가공 공장을 추진하고 메테오릭의 칼데이라 광산이 연 1만 2,500톤 산화물 생산을 계획하면서, 브라질이 채굴을 넘어 분리·정제까지 공급망을 넓힐 수 있다 (채널 전언)",
 "facts": [
  "무엇이: 라이너스가 브라질 정부 지원을 받아 현지 희토류 공장을 계획하고 있고, 브라질은 선광·분리·정제까지 국내 산업망을 넓히려 합니다 [채널]",
  "광산: 메테오릭의 칼데이라 프로젝트는 연평균 약 1만 2,500톤의 희토류 산화물 생산, 광산 수명 23년을 계획하며 네오디뮴·프라세오디뮴과 디스프로슘·테르븀을 포함합니다 [채널]",
  "자원량: 광물자원량 16억 3,000만 톤(TREO 2,317ppm), 광석매장량 1억 5,100만 톤(3,524ppm)입니다 [채널]",
  "변수: 초기 개발비 약 4억 9,800만 달러에 별도 분리시설 비용은 빠져 있고, 공장 건설은 자금 조달·인허가·라이너스의 최종투자결정에 달려 있습니다 [채널]"],
 "basis": "channel",
 "check": "검색 한도로 확인하지 않음. 채널이 인용한 mining.com 기사 요약 기준.",
 "src": [],
 "inds": ["metals"], "nodes": [],
 "items": [
  it("라이너스, 브라질 정부 지원 희토류 공장 추진…칼데이라 연 1만 2,500톤 계획", T+"상상인 김진범", "2026-10-13", "https://t.me/PipeBeom/6681"),
 ]})

items.append({"cid": "C156", "attachTo": "",
 "title": "카빌라 前 콩고 대통령, M23 반군 대체할 새 조직 결성",
 "one": "조제프 카빌라 전 콩고민주공화국 대통령이 동부 반군 M23을 대신할 새 조직을 만들면서, 광물 산지인 콩고 동부의 분쟁 구도가 새로 짜일 수 있다 (제목 기준)",
 "facts": [
  "무엇이: 카빌라 전 콩고 대통령이 M23 반군을 대체할 새 조직을 결성했습니다 [제목]",
  "의미: 콩고 동부 분쟁 구도 변화로 광물 공급 지역의 정세 불안이 이어질 수 있습니다 [추론]"],
 "basis": "title",
 "check": "검색 한도로 확인하지 않음. 조직 이름과 규모는 확인 못 함.",
 "src": [],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "items": [
  it("카빌라 前 콩고 대통령, M23 반군 대체할 새 조직 결성", "로이터", "2026-10-13", "https://www.reuters.com/world/congos-former-president-kabila-forms-new-group-replace-m23-insurgency-2026-10-12/"),
 ]})

items.append({"cid": "C164", "attachTo": "",
 "title": "佛 슈퍼마켓 체인 앵테르마르셰 사이버공격…매장 150곳 표적",
 "one": "프랑스 슈퍼마켓 체인 앵테르마르셰가 사이버공격을 받아 매장 150곳이 표적이 되면서, 해당 매장들의 운영과 고객 정보 보호에 차질이 생길 수 있다 (제목 기준)",
 "facts": [
  "무엇이: 프랑스 슈퍼마켓 체인 앵테르마르셰가 사이버공격을 받았습니다 [제목]",
  "범위: 매장 150곳이 표적이 됐습니다 [제목]"],
 "basis": "title",
 "check": "검색 한도로 확인하지 않음. 피해 내용은 확인 못 함.",
 "src": [],
 "inds": ["consumer"], "nodes": [],
 "items": [
  it("佛 슈퍼마켓 체인 앵테르마르셰 사이버공격, 매장 150곳 표적", "로이터", "2026-10-13", "https://www.reuters.com/business/retail-consumer/french-supermarket-chain-intermarche-hit-by-cyberattack-150-stories-targeted-2026-10-12/"),
 ]})

out = {"agent": "W6", "searches_used": 16, "fetches_used": 0, "items": items, "skipped": []}
p = "/home/user/news-desk/data/mix-2026-10-13/out2/W6.json"
json.dump(out, open(p, "w"), ensure_ascii=False, indent=1)
for x in items:
    one = re.sub(r' \((제목 기준|채널 전언)\)$', '', x['one'])
    single = len(x['items']) == 1 and not x['attachTo']
    lo, hi = (80, 130) if single else (90, 160)
    flag = "" if lo <= len(one) <= hi else "  <-- one"
    tf = "" if 20 <= len(x['title']) <= 50 else "  <-- title"
    bad = [i['t'] for i in x['items'] if not 25 <= len(i['t']) <= 60]
    print(x['cid'], len(x['title']), len(one), flag, tf, bad)
