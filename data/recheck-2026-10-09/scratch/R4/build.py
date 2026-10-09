import json
OUT = "/home/user/news-desk/data/recheck-2026-10-09/out/R4.json"
SEARCHES = 16
FETCHES = 0
docs = []

docs.append({
 "id": "n-rtr-0127", "changed": True, "basis": "verified",
 "title": "질랜드·로슈 비만 신약, 2상서 체중 최대 9.2% 감량",
 "one": "덴마크 질랜드파마와 로슈가 개발하는 비만 신약 페트렐린타이드가 2형 당뇨 환자 대상 2상에서 28주간 체중을 최대 9.2% 줄였다고 발표하면서, 이미 시작한 3상으로 비만약 후발 주자 경쟁을 이어갈 근거를 얻었다",
 "facts": [
  "무엇이: 질랜드·로슈의 아밀린 유사체 페트렐린타이드가 2상 ZUPREME-2에서 28주간 평균 체중을 최대 9.2% 줄였다(위약 2.0%) [사실]",
  "대상: 과체중·비만이면서 2형 당뇨가 있는 미국 성인 220명, 주 1회 3개 용량군에서 감량 폭 7.4~9.2% [사실]",
  "안전성: 위장관 이상반응은 대체로 경미했고 이로 인한 투약 중단은 1.9%(위약 1.7%) [사실]",
  "다음 단계: 두 회사는 ZUPREME-1·2 결과를 바탕으로 3상 3건을 시작했다 [사실]",
  "평가: 혈당(HbA1c) 개선 폭은 위약 대비 0.61~0.88%포인트로 작아 분석가 반응이 엇갈렸다 [사실]"
 ],
 "check": "질랜드 공시(GlobeNewswire)와 BioSpace·Fierce Biotech 보도의 검색 결과 요약으로 확인. 9.2%는 실제 발표 수치와 일치",
 "src_add": [
  {"o": "질랜드파마 공시(GlobeNewswire)", "d": "2026-10-07", "u": "https://www.globenewswire.com/news-release/2026/10/07/3376750/0/en/zealand-pharma-announces-positive-phase-2-zupreme-2-topline-results-for-amylin-analog-petrelintide-in-people-with-overweight-or-obesity-and-type-2-diabetes.html"},
  {"o": "BioSpace", "d": "2026-10-07", "u": "https://www.biospace.com/drug-development/despite-zealand-assets-intriguing-weight-loss-analysts-underwhelmed-by-blood-sugar-numbers"}
 ],
 "note": "9.2% 맞음 확인, 약물명·대상·위약 수치 추가, 3상 이미 시작으로 한줄 보정, 꼬리 뗌"
})

docs.append({
 "id": "n-bbg-0100", "changed": True, "basis": "verified",
 "title": "셸, 3분기 정제 마진 75% 급등 예고에 가스 생산 전망도 상향",
 "one": "셸이 3분기 정제 마진 지표를 배럴당 24달러에서 42달러로 높여 안내한 데 이어 통합가스 부문 생산 전망도 올리면서, 정유·가스 부문 이익은 늘지만 화학 마진은 톤당 208달러로 떨어져 석유화학 부진은 이어질 전망이다",
 "facts": [
  "무엇이: 셸이 3분기 통합가스 생산 전망을 하루 74만~78만 배럴(석유환산)로 제시, 2분기 63만1000배럴보다 높다 [사실]",
  "정제: 3분기 정제 마진 지표를 2분기 24달러에서 배럴당 42달러로 높여 안내 [사실]",
  "화학: 화학 마진은 톤당 270달러에서 208달러로 하락 [사실]",
  "주의: 이전 3분기 전망(57만~63만 배럴)은 ARC리소시스·카타르 물량을 뺀 수치라 직접 비교는 어렵다 [사실]",
  "기타: 정제 가동률 93~97%로 하락(라인강 수위), 독일 배출권 관련 약 25억 달러 현금 유출 예상 [사실]"
 ],
 "check": "셸 3분기 안내문을 다룬 StockTitan·DirectorsTalk 등의 검색 결과 요약으로 가스 생산 전망 수치까지 확인",
 "src_add": [
  {"o": "StockTitan(셸 안내문)", "d": "2026-10-07", "u": "https://www.stocktitan.net/news/SHEL/shell-third-quarter-2026-update-ip8be8zrdsz6.html"},
  {"o": "DirectorsTalk", "d": "2026-10-07", "u": "https://www.directorstalkinterviews.com/shell-raises-q3-integrated-gas-outlook-as-refining-margins-improve/4121265558"}
 ],
 "note": "가스 생산 전망 수치(74만~78만 boe/d) 추가, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0020", "changed": True, "basis": "verified",
 "title": "독일 환경단체 이어 주정부 장관도 '러시아 원자로용 링겐 핵연료 공장 막아야'",
 "one": "독일 환경단체 분트가 로사톰 면허로 러시아형 원전 연료를 만들려는 프라마톰 링겐 공장 허가의 임시 정지를 법원에 신청한 데 이어 주정부 장관까지 공장을 막아야 한다고 나서면서, 불가리아 등 유럽 5개국의 러시아산 연료 대체 일정이 늦어질 수 있다",
 "facts": [
  "무엇이: 니더작센주 환경장관 크리스티안 마이어가 링겐 공장이 러시아 면허로 불가리아 등 유럽 5개국용 핵연료를 만들어선 안 된다고 말했다 [사실]",
  "기존: 환경단체 분트가 프라마톰 링겐 공장이 로사톰 면허로 러시아형 원전 연료를 만들도록 한 허가를 법원에서 임시로 멈추려 한다 [사실]",
  "배경: 마이어의 부처가 허가 당국이며, 법적 거부 근거가 없어 허가는 내줬다는 입장이다 [사실]",
  "영향: 불가리아 등 유럽 5개국이 러시아산을 대신할 연료를 공급받는 일정이 늦어질 수 있다 [추론]",
  "남은 점: 법원의 정지 신청 결정 시점은 확인하지 못했다 [미확인]"
 ],
 "check": "불가리아 BNews(10월 7일)와 관련 보도의 검색 결과 요약으로 발언 장관(니더작센 환경장관 마이어)과 분트의 정지 신청 확인. 법원 결정은 못 찾음",
 "src_add": [
  {"o": "BNews 불가리아", "d": "2026-10-07", "u": "https://balgarianovinite.com/en/lower-saxony-minister-opposes-nuclear-fuel-pro/"}
 ],
 "note": "장관 소속(니더작센 환경장관 마이어) 확인해 facts 보강, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0074", "changed": True, "basis": "verified",
 "title": "아젠엑스, 쇼그렌증후군 비브가트 임상 중단…주가 급락",
 "one": "벨기에 바이오기업 아젠엑스가 대표 약물 비브가트의 쇼그렌증후군 임상시험을 중단하면서 주가가 급락했고, 비브가트의 적응증 확대 기대가 줄어들 수 있다",
 "facts": [
  "무엇이: 아젠엑스가 데이터모니터링위원회의 무익성 판단에 따라 쇼그렌증후군 대상 비브가트 3상(UNITY)을 중단 [사실]",
  "시장: 10월 8일 주가가 약 13~16% 떨어져 시가총액 약 85억 유로가 줄었다 [사실]",
  "안전성: 새로운 안전성 문제는 없었고 기존 승인 적응증에는 영향 없음 [사실]",
  "영향: 분석가들이 기대한 쇼그렌 적응증(윌리엄블레어 최대 매출 추정 14억 달러) 확대가 무산 [사실]"
 ],
 "check": "BioSpace·Fierce Pharma·Endpoints 보도의 검색 결과 요약으로 중단 사유와 주가 하락 확인",
 "src_add": [
  {"o": "BioSpace", "d": "2026-10-08", "u": "https://www.biospace.com/drug-development/argenx-shutters-sjogrens-study-losing-blockbuster-expansion-opportunity-for-vyvgart"},
  {"o": "Fierce Pharma", "d": "2026-10-08", "u": "https://www.fiercepharma.com/pharma/argenx-walks-away-vyvgart-sjogrens-disease-trial-after-futility-flag"}
 ],
 "note": "3상 UNITY 무익성 중단·하락폭 확인해 facts 보강, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0083", "changed": True, "basis": "verified",
 "title": "트레비 \"웨빌드 상향 인수가는 적정가치 범위 하단\"",
 "one": "이탈리아 지반공사업체 트레비가 웨빌드의 상향된 인수 제안가를 자사 적정가치 범위의 하단에 해당한다고 평가하면서, 웨빌드의 제안가가 트레비가 보는 적정가치 범위 안에 들어오게 됐다",
 "facts": [
  "무엇이: 트레비 이사회가 웨빌드의 상향 제안가(주당 5.165유로)가 자체 적정가치 범위(주당 5.1~6.1유로)의 하단이라고 평가 [사실]",
  "상향: 웨빌드는 현금 인수가를 주당 4.50유로에서 5.165유로로 올렸다 [사실]",
  "입장: 이사회 평가는 응모 권고나 거부가 아니라고 트레비가 밝혔다 [사실]",
  "경쟁: 경쟁 입찰자 ICOP도 주식 교환 방식으로 주당 5.165유로를 제시했으나 이사회는 재무적으로 적정하지 않다고 봤다 [사실]",
  "의미: 제안가가 범위 안에 들어 거래 성사 가능성은 열려 있지만 높은 가격이라는 평가는 아님 [추론]"
 ],
 "check": "Global Banking and Finance·일솔레24오레 보도의 검색 결과 요약으로 적정가치 범위와 상향 제안가 확인",
 "src_add": [
  {"o": "Global Banking and Finance Review", "d": "2026-10-08", "u": "https://www.globalbankingandfinance.com/trevi-webuilds-sweetened-bid-low-end-fair-value-range/"},
  {"o": "Il Sole 24 Ore", "d": "2026-10-06", "u": "https://en.ilsole24ore.com/art/trevi-makes-a-move-webuild-raises-takeover-bid-price-AJl3KRZB"}
 ],
 "note": "제안가 5.165유로·범위 5.1~6.1유로 확인해 facts 보강, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0091", "changed": True, "basis": "verified",
 "title": "아람코, 유전서비스업체 NESR과 사우디 리튬 사업 공동 개발 합의",
 "one": "사우디 아람코와 중동 유전서비스업체 NESR이 연 2000톤 규모 리튬 직접추출 시범 사업을 함께 개발하기로 합의하면서, 석유 기업이 배터리 원료 공급망에 들어서는 사우디의 리튬 확보 시도가 구체화되고 있다",
 "facts": [
  "무엇이: NESR과 아람코가 사우디아라비아에서 리튬 시범 사업(Aramco 2027 Lithium Demonstration Project)을 개발하기로 합의했다 [사실]",
  "규모: 배터리급 탄산리튬 연 2000톤 생산 목표, 2027년 말 가동·생산 시작 예정 [사실]",
  "방식: NESR의 LiThara 플랫폼으로 염수 전처리·리튬 직접추출(DLE)·탄산화를 하고 아람코는 지하자원 전문성을 제공 [사실]",
  "계약: 5년 약 2억 달러 규모라는 보도가 있으나 일부 보도에만 나온다 [사실]",
  "의미: 산유국이 배터리 원료 공급망에 들어오면 중장기 리튬 공급원이 다변화될 수 있다 [추론]"
 ],
 "check": "Benzinga·AGBI·Mining.com.au 보도의 검색 결과 요약으로 규모(연 2000톤)·일정·방식 확인. 2억 달러 계약액은 Benzinga·AGBI에만 나옴",
 "src_add": [
  {"o": "AGBI", "d": "2026-10-08", "u": "https://www.agbi.com/mining/2026/10/saudi-aramco-targets-first-lithium-extraction-next-year/"},
  {"o": "Mining.com.au", "d": "2026-10-08", "u": "https://mining.com.au/nesr-aramco-agree-to-develop-lithium-project-in-saudi-arabia/"}
 ],
 "note": "규모·방식 미확인을 사실로 채움(연 2000톤, DLE, 2027년 말), 한줄에 규모 반영, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0096", "changed": True, "basis": "verified",
 "title": "폴스타 분기 판매 소폭 증가…미국 판매 금지 임박",
 "one": "스웨덴·중국계 전기차업체 폴스타의 3분기 소매 판매가 1만4371대로 1% 늘었지만 2027년형부터 미국 판매가 금지되면서, 폴스타의 미국 시장 판매가 막혀 유럽 중심 실적 회복이 더뎌질 수 있다",
 "facts": [
  "무엇이: 폴스타의 3분기 글로벌 소매 판매가 1만4371대로 전년보다 약 1% 증가 [사실]",
  "세부: 미국을 뺀 판매는 8% 감소했다 [사실]",
  "위험: 미 상무부의 중국 연계 커넥티드카 차단 규정으로 2027년형부터 미국 판매가 금지된다(최대주주 지리홀딩) [사실]",
  "대응: 미국에서는 남은 2026년형 폴스타 3·4 재고를 팔고 서비스망은 유지한다 [사실]"
 ],
 "check": "폴스타 발표(BusinessWire)와 Investing.com 자체 기사의 검색 결과 요약으로 판매 대수와 금지 근거 확인",
 "src_add": [
  {"o": "폴스타 발표(BusinessWire)", "d": "2026-10-08", "u": "https://www.businesswire.com/news/home/20261008797091/en/Polestar-Reports-Record-Nine-Month-Retail-Sales-and-Its-Strongest-Third-Quarter"},
  {"o": "Investing.com", "d": "2026-10-08", "u": "https://www.investing.com/news/company-news/polestar-reports-q3-retail-sales-up-1-to-14371-vehicles-93CH-4938555"}
 ],
 "note": "판매 대수(1만4371대, +1%)·금지 근거(상무부 규정, 2027년형부터) 확인해 한줄·facts 보강, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0102", "changed": True, "basis": "verified",
 "title": "전 RBA 인사 \"AI 붐, 금리 올라도 호주 물가 자극할 것\"",
 "one": "호주중앙은행(RBA) 전직 인사가 AI 붐이 금리 인상에도 불구하고 호주 인플레이션을 부추길 것이라고 밝히면서, RBA의 긴축이 길어지거나 추가 인상 압력이 생길 수 있다",
 "facts": [
  "무엇이: RBA 출신 조너선 컨스 챌린저 수석이코노미스트가 AI 투자 붐이 높아진 금리에도 단기적으로 호주 물가를 끌어올릴 것이라고 말했다 [사실]",
  "근거: 초기 기술·인프라 투자가 국내 물가를 밀어 올리는 반면 생산성 효과는 천천히 나타나고, 물가가 4~5년째 목표를 웃돌아 RBA가 이를 넘겨 볼 여지가 적다고 봤다 [사실]",
  "완충: 데이터센터 지출의 약 4분의 3이 수입 장비라 물가 영향이 일부 줄어든다고 추정 [사실]",
  "전망: 컨스는 RBA가 올해 한 차례 더 금리를 올릴 것으로 예상, RBA는 9월 올해 네 번째 인상으로 기준금리를 4.6%로 올렸다 [사실]",
  "의미: 긴축 부담이 가계·환율·비AI 기업 투자에 더 쏠릴 수 있다 [사실]"
 ],
 "check": "Capital Brief·IndexBox 보도의 검색 결과 요약으로 발언자(조너선 컨스)와 주장 내용 확인",
 "src_add": [
  {"o": "Capital Brief", "d": "2026-10-08", "u": "https://www.capitalbrief.com/briefing/ex-rba-official-says-australias-ai-boom-will-fuel-short-term-inflation-9cb438cf-6783-460a-bf27-74e7933034e6/"},
  {"o": "IndexBox", "d": "2026-10-08", "u": "https://www.indexbox.io/blog/australias-ai-investment-boom-to-push-inflation-higher-says-former-rba-official/"}
 ],
 "note": "발언자·근거·추가 인상 전망 확인해 facts 보강, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0110", "changed": True, "basis": "verified",
 "title": "화이자, 이탈리아 시칠리아 공장서 약 330명 감원…비용 절감 이어가",
 "one": "화이자가 이탈리아 시칠리아 카타니아 공장에서 페니실린 부서를 닫고 약 330명을 줄이기로 하면서, 공장 인력의 약 60%가 줄어 이탈리아 정부·노조와의 협상이 이어지게 됐다",
 "facts": [
  "무엇이: 화이자가 이탈리아 시칠리아 카타니아 공장에서 약 330명을 감원한다고 노조가 밝혔다 [사실]",
  "대상: 페니실린 부서 폐쇄를 포함한 구조조정으로, 노조 기준 현 인력 약 550명 가운데 약 60%다 [사실]",
  "협상: 로마에서 열린 산업부 중재 협의가 결론 없이 끝났고 우르소 산업장관이 10월 23일 공장을 찾고 11월 10일 추가 협의가 잡혔다 [사실]",
  "배경: 화이자가 진행해 온 전사 비용 절감 계획의 연장선일 수 있다 [추론]"
 ],
 "check": "Global Banking and Finance·Seeking Alpha·GuruFocus 보도의 검색 결과 요약으로 감원 규모와 사업장(카타니아) 확인. 공장 인력 규모는 출처마다 다름",
 "src_add": [
  {"o": "Global Banking and Finance Review", "d": "2026-10-07", "u": "https://www.globalbankingandfinance.com/pfizer-cut-around-330-jobs-italy/"},
  {"o": "Seeking Alpha", "d": "2026-10-07", "u": "https://seekingalpha.com/news/4651244-pfizer-to-close-penicillin-unit-cut-around-330-jobs-in-italy"}
 ],
 "note": "감원 사업장(시칠리아 카타니아, 페니실린 부서) 확인해 제목·한줄·facts 보강, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0118", "changed": True, "basis": "verified",
 "title": "미국, 미얀마 군부와 직접 대화 개시…수년간의 고립 정책 뒤집어",
 "one": "미국이 수년간 유지해 온 미얀마 군부 고립 정책을 뒤집고 군 장성들과 직접 대화를 시작하면서, 서방 제재로 막혀 있던 미얀마와의 외교·경제 관계에 변화가 생길 수 있다",
 "facts": [
  "무엇이: 미국이 2021년 쿠데타 이후의 고립 정책을 뒤집고 미얀마 군부와 직접 대화를 시작 [사실]",
  "일시·참석: 마이클 밴스 국무부 정보조사담당 차관보가 9월 15~16일 네피도에서 민아웅흘라잉과 회담 [사실]",
  "계기: 미국인 사업가 억류 석방 협상에서 시작됐고 사기 단지 단속이 주된 의제다 [사실]",
  "자원: 중희토류 접근도 논의됐으나 주요 매장지는 군부와 싸우는 소수민족 무장단체 지역에 있다 [사실]",
  "영향: 민아웅흘라잉은 여전히 미국 제재 대상이며 제재·투자 환경 변화는 지켜봐야 한다 [추론]"
 ],
 "check": "Bangkok Post·Japan Times·Modern Diplomacy 보도의 검색 결과 요약으로 대화 일시·참석자·의제 확인",
 "src_add": [
  {"o": "Bangkok Post", "d": "2026-10-08", "u": "https://www.bangkokpost.com/world/3333614/us-opens-direct-talks-with-myanmar"},
  {"o": "Modern Diplomacy", "d": "2026-10-08", "u": "https://moderndiplomacy.eu/2026/10/08/why-is-washington-talking-directly-to-myanmars-military-government/"}
 ],
 "note": "대화 일시·참석자·의제(희토류 포함) 확인해 facts 보강, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0123", "changed": True, "basis": "verified",
 "title": "웨불 주가 급락…\"美 하원 위원회, 중국 연계 문제 제기\" CNBC 보도",
 "one": "미 하원 위원회가 온라인 증권사 웨불의 중국 연계를 문제 삼았다는 CNBC 보도가 나오면서 웨불 주가가 급락해, 중국 연계 핀테크 기업에 대한 미국 의회의 규제·안보 압박이 주가 위험으로 번지고 있다",
 "facts": [
  "무엇이: CNBC가 미 하원 중국특별위원회(초당적)가 웨불이 중국 정부와 구조적으로 연계돼 있다고 결론 냈다고 보도 [사실]",
  "시장: 10월 7일 웨불 주가가 보도 시점에 따라 19~32% 급락, 로빈후드·인터랙티브브로커스도 2~3% 하락 [사실]",
  "반박: 웨불은 보고서에 중대한 오류와 근거 없는 결론이 있다며 미국 고객 데이터는 미국에 저장한다고 밝혔다 [사실]",
  "한계: 위원회 보고서 자체로는 제재·영업 금지 같은 강제 조치가 따르지 않는다 [사실]",
  "영향: 중국 연계 미국 상장 핀테크에 대한 의회 감시 강화 가능성 [추론]"
 ],
 "check": "24/7 Wall St.·Crowdfund Insider 보도의 검색 결과 요약으로 위원회 명칭과 하락폭(출처별 19~32%) 확인",
 "src_add": [
  {"o": "24/7 Wall St.", "d": "2026-10-07", "u": "https://247wallst.com/investing/2026/10/07/webull-sinks-29-as-house-panel-calls-its-china-ties-a-national-security-risk-robinhood-drops-3-interactive-brokers-slips/"},
  {"o": "Crowdfund Insider", "d": "2026-10-07", "u": "https://www.crowdfundinsider.com/2026/10/316397-webull-shares-plummet-as-house-select-committee-on-china-declares-national-security-risk-and-ties-to-china/"}
 ],
 "note": "위원회 명칭·하락폭·회사 반박 확인해 facts 보강, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0129", "changed": True, "basis": "verified",
 "title": "미 FDA, 노바티스 두드러기약 랩시도 피부묘기증으로 적응증 확대",
 "one": "미 FDA가 노바티스의 만성 두드러기약 랩시도(레미브루티닙)를 항히스타민제로 조절되지 않는 성인 증상성 피부묘기증에 쓰도록 승인하면서, 노바티스가 이 약의 처방 대상을 넓히게 됐다",
 "facts": [
  "무엇이: 미 FDA가 노바티스 랩시도(레미브루티닙)의 사용을 성인 증상성 피부묘기증(만성 두드러기의 한 형태)으로 확대 승인 [사실]",
  "대상: 항히스타민제로 증상이 충분히 조절되지 않는 성인, 이 질환 전용 첫 FDA 승인 치료제 [사실]",
  "근거: 3상 RemIND에서 12주 뒤 두드러기 완전 소실 비율이 29.3%로 위약 14%보다 높았다 [사실]",
  "기존: 이 약은 이미 미국에서 만성 자발성 두드러기에 승인돼 있다 [사실]"
 ],
 "check": "PharmTech·AJMC 보도의 검색 결과 요약으로 약 이름(레미브루티닙)과 질환(증상성 피부묘기증) 확인",
 "src_add": [
  {"o": "PharmTech", "d": "2026-10-07", "u": "https://www.pharmtech.com/view/symptomatic-dermographism-novartis-lands-remibrutinib-label-expansion"},
  {"o": "AJMC", "d": "2026-10-07", "u": "https://www.ajmc.com/view/fda-approves-first-symptomatic-dermographism-treatment"}
 ],
 "note": "약 이름(랩시도·레미브루티닙)·질환(피부묘기증) 확인해 제목·한줄·facts 구체화, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0134", "changed": True, "basis": "verified",
 "title": "英 바닥재 유통사 헤드램, 법정관리 들어가며 상장폐지",
 "one": "영국 바닥재 유통업체 헤드램이 법정관리 끝에 핵심 자산을 1490만 파운드에 라이크와이즈에 넘기고 런던 증시 상장폐지를 추진하면서, 기존 주주가 투자금을 돌려받을 가능성이 거의 사라졌다",
 "facts": [
  "무엇이: 헤드램 관리인이 FCA에 상장 취소를 신청할 계획이며 시행일은 아직 정해지지 않았다 [사실]",
  "경과: 헤드램은 9월 8일 법정관리에 들어갔고 주식은 9월 초부터 거래 정지 상태다 [사실]",
  "매각: 라이크와이즈가 대참 물류센터와 브랜드 등 일부 자산을 1490만 파운드에 인수해 10월 6일 완료, 약 110개 일자리 유지 [사실]",
  "영향: 회사는 주주에게 자본이 돌아갈 가능성이 낮다고 밝혔다 [사실]"
 ],
 "check": "헤드램 공시를 다룬 TipRanks·AskTraders·TradersUnion의 검색 결과 요약으로 법정관리·자산 매각·상장 취소 계획 확인. 상장폐지 시행일은 미정",
 "src_add": [
  {"o": "TipRanks(헤드램 공시)", "d": "2026-10-07", "u": "https://www.tipranks.com/news/company-announcements/headlam-sells-core-assets-to-likewise-and-plans-london-listing-cancellation"},
  {"o": "AskTraders", "d": "2026-10-07", "u": "https://www.asktraders.com/analysis/headlam-shares-face-delisting-after-14-9m-asset-sale-to-likewise/"}
 ],
 "note": "상장폐지는 '추진'(시행일 미정)으로 한줄 보정, 자산 매각 1490만 파운드 추가, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0139", "changed": True, "basis": "verified",
 "title": "로사톰, 델로 지분 100% 확보…러시아 최대 물류그룹 탄생",
 "one": "러시아 국영 원자력기업 로사톰이 창업자 지분 51%를 사들여 물류그룹 델로를 완전히 소유하고 FESCO와 묶기로 하면서, 러시아 항만·컨테이너 운송에서 국영기업의 영향력이 커지게 됐다",
 "facts": [
  "무엇이: 로사톰이 창업자 세르게이 시시카료프의 델로 지분 51%를 사들여 지분 100%를 확보했다(기존 49%) [사실]",
  "금액: 인수가는 공개되지 않았고 시시카료프는 자기 지분 가치를 770억 루블로 제시했다 [사실]",
  "재편: 로사톰은 델로를 해운사 FESCO 등과 묶어 공동 관리센터를 세울 계획이다 [사실]",
  "규모: 로사톰의 러시아 컨테이너 환적 시장 점유율은 50%, 철도 컨테이너 운송 점유율은 44%에 이르렀다 [사실]",
  "영향: 국영기업 중심의 물류 재편 [추론]"
 ],
 "check": "Moscow Times·Splash247·Baird Maritime 보도의 검색 결과 요약으로 지분 구조와 통합 계획 확인. 실제 인수 금액은 비공개",
 "src_add": [
  {"o": "The Moscow Times", "d": "2026-10-07", "u": "https://www.themoscowtimes.com/2026/10/07/rosatom-takes-full-control-of-delo-group-in-900m-buyout-a93906"},
  {"o": "Splash247", "d": "2026-10-08", "u": "https://splash247.com/rosatom-folds-delo-into-expanding-logistics-platform/"}
 ],
 "note": "기존 지분율(49%)·인수 지분(51%)·FESCO 통합 확인해 한줄·facts 보강, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0146", "changed": True, "basis": "partial",
 "title": "인도 NSE, 수요 몰린 해외 ETF 고평가 경고",
 "one": "인도국립증권거래소(NSE)가 해외 주식 ETF로 수요가 몰려 일부 상품 가격이 비싸지자 투자자들에게 주의를 당부하면서, 해외 주식에 쏠린 인도 개인 투자자들이 고평가된 가격에 사들이는 손실 위험이 부각됐다",
 "facts": [
  "무엇이: NSE가 일부 해외 ETF가 순자산가치(NAV)보다 크게 비싸게 거래된다며 투자자 주의 촉구 [사실]",
  "원인: 뮤추얼펀드의 해외 투자 한도가 소진돼 새 ETF 단위를 만들 수 없어 수요가 가격을 밀어 올렸다 [사실]",
  "세부: 모틸랄오스왈 나스닥 Q50 ETF의 프리미엄은 9월 18일 235%까지 치솟았다가 9월 28일 57%로 내려간 뒤 다시 반등했다 [사실]",
  "참고: BSE도 비슷한 경고를 냈다 [사실]"
 ],
 "check": "Value Research·Whalesbook 보도의 검색 결과 요약으로 해외 ETF 프리미엄과 BSE 경고는 확인. NSE 경고 원문은 로이터 계열 글에서만 보여 독립 출처로는 확인 못 함",
 "src_add": [
  {"o": "Value Research", "d": "2026-10-07", "u": "https://valueresearchonline.com/stories/229882/nasdaq-q50-etf-premium-international-funds-open"},
  {"o": "Whalesbook", "d": "2026-10-07", "u": "https://www.whalesbook.com/news/English/sebiexchange/BSE-Warns-Investors-On-International-ETF-Price-Premiums/6ab6baed5aacb956d080c3f0"}
 ],
 "note": "프리미엄 원인·규모 확인해 facts 보강, NSE 경고 자체는 독립 출처 미확인이라 partial, 꼬리 뗌"
})

docs.append({
 "id": "n-rtr-0151", "changed": True, "basis": "verified",
 "title": "남아공, 배터리 저장장치·가스발전 사업 우선 추진",
 "one": "남아공 에너지부가 배터리 저장장치 4.6GW와 가스발전 5GW를 우선 조달하겠다고 밝히면서, 전력난을 겪는 남아공의 신규 발전 조달이 저장장치·가스 쪽으로 쏠리고 관련 사업자의 수주 기회가 늘 수 있다",
 "facts": [
  "무엇이: 남아공 람오콥파 전력·에너지 장관이 배터리 저장장치와 가스발전을 우선 조달한다고 10월 7일 발표 [사실]",
  "규모: 2026~2037년 대상 34조 결정으로 배터리 저장 4.6GW, 가스발전 5GW 등 총 9.6GW를 먼저 조달하고 풍력·태양광 배정은 뒤에 한다 [사실]",
  "방식: 독립발전사업자청(IPPO)이 시행하며 에스콤을 포함한 모든 사업자에 열려 있다 [사실]",
  "미정: 저장 용량(MWh)과 입찰 일정은 공개되지 않았다 [미확인]",
  "의미: 신규 발전 조달이 저장·가스로 이동 [추론]"
 ],
 "check": "남아공 정부 통신(SAnews)·Engineering News 보도의 검색 결과 요약으로 조달 규모(4.6GW·5GW) 확인",
 "src_add": [
  {"o": "SAnews(남아공 정부)", "d": "2026-10-07", "u": "https://www.sanews.gov.za/south-africa/south-africa-prioritises-gas-and-battery-storage"},
  {"o": "Engineering News", "d": "2026-10-07", "u": "https://www.engineeringnews.co.za/article/new-determination-opens-way-for-public-procurement-of-large-scale-battery-storage-and-gas-to-power-2026-10-07"}
 ],
 "note": "조달 규모(저장 4.6GW·가스 5GW) 확인해 한줄·facts 보강, 꼬리 뗌"
})

out = {"agent": "R4", "searches_used": SEARCHES, "fetches_used": FETCHES, "docs": docs}
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
print(len(docs))
