import json, re

H = "텔레그램 하나증권 중국전략"
B = "텔레그램 나쁜양파"
T = "텔레그램 TNBfolio"
items = []

items.append({"cid": "C004", "attachTo": "n-tg-0140",
 "title": "美 30년물 입찰 5.618%로 2000년 이후 최고…재정적자 2조 달러 육박",
 "one": "미 장기 국채 매도로 30년물 금리가 2002년 이후 최고권에 머문 가운데 10월 8일 30년물 입찰이 2000년 이후 최고인 5.618%에 낙찰되고 2026회계연도 재정적자도 1조 9,930억 달러로 불어나, 모기지 등 차입 비용 부담이 커지고 있다",
 "facts": [
  "무엇이: 미 재무부가 10월 8일 30년물 220억 달러를 5.618%에 낙찰해 2000년 8월 이후 최고였고, 9월 5.308%보다 0.31%p 높았습니다 [사실]",
  "수요: 응찰배율 2.54배로 최근 평균 2.41배를 웃돌고 간접입찰 비중이 72.3%여서 높은 금리에 수요는 견조했습니다 [사실]",
  "재정: CBO는 2026회계연도 재정적자를 1조 9,930억 달러로 추정했고, 순이자 지출이 1,150억 달러(11%) 늘어 적자 증가분의 절반 이상을 차지했습니다 [사실]",
  "기존: 30년물 금리는 10월 8일 5.69% 안팎으로 2002년 이후 최고, MBA 30년 고정 모기지 금리는 7.49%로 2023년 11월 이후 최고였습니다 [사실]",
  "시각 차: 모건스탠리자산운용 칸두자는 41억 달러 펀드 듀레이션을 6.07년으로 늘려 10여 년 만에 미 국채 강세로 돌아섰고, 반대로 재정적자와 대규모 회사채 발행이 자본을 다퉈 조달 비용이 구조적으로 오른다는 분석도 나왔습니다 [채널]"],
 "basis": "verified",
 "check": "30년물 입찰 결과(5.618%, 응찰배율 2.54배, 간접 72.3%)와 CBO 재정적자 1조 9,930억 달러·순이자 증가는 검색 결과 요약으로 확인. 채널의 '2001년 이후 최고'는 검색상 2000년 8월 이후로 바로잡음. 칸두자 듀레이션 전환은 미확인",
 "src": [
  {"o": "CNBC", "d": "2026-10-08", "u": "https://www.cnbc.com/2026/10/08/us-treasury-yields-30-year-bond-auction.html"},
  {"o": "TokenPost", "d": "2026-10-08", "u": "https://www.tokenpost.com/news/investing/28466"},
  {"o": "The Fiscal Times", "d": "2026-10-08", "u": "https://www.thefiscaltimes.com/2026/10/08/Deficit-Rose-2-Trillion-2026-Fiscal-Year-CBO"}],
 "inds": ["macro"], "nodes": ["macro/rates", "macro/fiscal"],
 "items": [
  {"t": "모건스탠리 베테랑 채권 운용역, 10년 만에 미 국채 강세로 전환", "o": H, "d": "2026-10-09", "u": "https://t.me/HANAchina/70092"},
  {"t": "미 2026회계연도 재정적자 1조 9,930억 달러…이자 지출 1조 1천억 달러 돌파", "o": H, "d": "2026-10-09", "u": "https://t.me/HANAchina/70103"},
  {"t": "미 30년물 입찰 5.618%에 낙찰, 응찰배율 2.54배로 수요는 평균 이상", "o": "텔레그램 부의 나침반", "d": "2026-10-09", "u": "https://t.me/w_compass/7228"},
  {"t": "정부 재정적자와 대규모 채권 발행이 자본 쟁탈전…채권시장 압박 이제 시작", "o": H, "d": "2026-10-09", "u": "https://t.me/HANAchina/70126"}]})

items.append({"cid": "C006", "attachTo": "",
 "title": "애플, 수요 부진에 아이폰18 프로 부품 주문 15~20% 축소…메모리값발 가격 인상 역풍",
 "one": "애플이 메모리 칩 비용 급등으로 100달러 올린 아이폰18 프로·프로 맥스의 10월 부품 주문을 당초보다 15~20% 줄이면서, 공급망 물량 감소 우려에 애플 주가가 개장 전 1.9% 내렸지만 수출 지표상으로는 라인업 변화 효과라는 해석도 나온다",
 "facts": [
  "무엇이: 애플이 아이폰18 프로·프로 맥스의 10월 부품 주문을 당초 요청보다 15~20% 줄였다고 닛케이아시아가 보도했습니다 [사실]",
  "원인: 메모리 칩 비용 급등으로 시작가가 프로 1,199달러, 프로 맥스 1,299달러로 전작보다 100달러씩 올라 수요가 둔화됐다는 설명입니다 [사실]",
  "시장: 보도 뒤 애플 주가는 미국 개장 전 거래에서 1.9% 내렸습니다 [사실]",
  "업황: IDC는 2026년 세계 스마트폰 출하가 16.7% 줄고 평균판매가격은 27.6% 오를 것으로 봤습니다 [채널]",
  "반론: 한국 카메라모듈 수출은 9월 11억 3천만 달러로 30% 늘었고 OLED 패널 수출은 14% 줄어, 기본형이 내년 봄으로 빠진 라인업 변화 효과라는 해석도 있습니다 [채널]"],
 "basis": "verified",
 "check": "닛케이 보도 내용(10월 부품 주문 15~20% 축소, 가격 100달러 인상)과 주가 1.9% 하락은 검색 결과 요약으로 확인. IDC 전망과 수출 지표 해석은 채널 전언",
 "src": [
  {"o": "Nikkei Asia", "d": "2026-10-09", "u": "https://asia.nikkei.com/business/technology/exclusive-apple-cuts-iphone-18-pro-orders-due-to-soft-demand"},
  {"o": "BusinessToday", "d": "2026-10-09", "u": "https://businesstoday.in/technology/news/story/iphone-18-pro-apple-reportedly-cuts-orders-by-15-as-demand-for-its-latest-flagships-slows-560650-2026-10-09"}],
 "inds": ["tech"], "nodes": [],
 "items": [
  {"t": "애플, 수요 부진으로 아이폰18 프로 주문 축소 (닛케이)", "o": H, "d": "2026-10-09", "u": "https://t.me/HANAchina/70131"},
  {"t": "애플, 수요 부진에 아이폰18 프로 주문 축소…닛케이아시아 보도", "o": "로이터", "d": "2026-10-09", "u": "https://www.reuters.com/business/retail-consumer/apple-cuts-iphone-18-pro-orders-due-soft-demand-nikkei-asia-reports-2026-10-09/"},
  {"t": "아이폰18 프로·맥스 10월 부품 주문 15~20% 감소…메모리값에 가격 인상 역풍", "o": T, "d": "2026-10-09", "u": "https://t.me/TNBfolio/71487"},
  {"t": "아이폰18 프로 감산 보도 점검…카메라모듈 수출 강세, 패널 약세는 라인업 영향", "o": B, "d": "2026-10-09", "u": "https://t.me/Badonions/7734"}]})

items.append({"cid": "C011", "attachTo": "n-tg-0122",
 "title": "대만 9월 수출 872억 달러 사상 최대…반도체 46% 늘며 AI 장비 교역 견인",
 "one": "반도체·서버 등 AI 장비 교역 급증으로 WTO가 올해 상품교역 증가율 전망을 3.9%로 올린 가운데, 대만 9월 수출이 사상 최대인 872억 달러를 기록하고 집적회로 수출도 46.1% 늘어 후공정·전력설비까지 수출 호조가 번지고 있다",
 "facts": [
  "무엇이: 대만 9월 수출이 872억 2천만 달러로 60.9% 늘어 사상 최대를 기록했고 35개월 연속 증가했습니다 [사실]",
  "반도체: 9월 집적회로 수출이 전년보다 46.1%(93억 9천만 달러) 늘었고, 채널은 금액을 297억 4천만 달러, 1~9월 누적을 2,200억 달러(47.3%)로 전했습니다 [사실]",
  "확산: 컴퓨터·전자부품뿐 아니라 대형 변압기 등 전력설비, 진공펌프 등 공정 장비, 패키징·테스트(ASE 수출액 43.4% 증가)도 함께 늘었습니다 [채널]",
  "교역: WTO는 2026년 상품교역 증가율 전망을 1.9%에서 3.9%로 올렸고, AI 관련 상품이 상반기 교역 증가분의 47%를 차지했습니다 [사실]"],
 "basis": "verified",
 "check": "9월 수출 872억 2천만 달러(60.9%)·35개월 연속 증가·집적회로 46.1% 증가는 검색 결과 요약으로 확인. 297억 4천만 달러와 누적 2,200억 달러는 직접 확인 못 함(증가액으로 역산하면 근사). 품목별 세부는 채널 전언",
 "src": [
  {"o": "新頭殼 Newtalk", "d": "2026-10-08", "u": "https://newtalk.tw/news/view/2026-10-08/1064510"},
  {"o": "經濟日報", "d": "2026-10-09", "u": "https://money.udn.com/money/story/10869/9804113"}],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "items": [
  {"t": "대만 9월 수출 리뷰: 컴퓨터·전자부품·전력설비 동반 개선", "o": B, "d": "2026-10-09", "u": "https://t.me/Badonions/7730"},
  {"t": "ASE 관련 대만 패키징·테스트 9월 수출액 43.4% 증가", "o": B, "d": "2026-10-09", "u": "https://t.me/Badonions/7731"},
  {"t": "대만 9월 반도체 수출 297억 달러로 46.1% 증가, 1~9월 누적 2,200억 달러", "o": "텔레그램 카이에 de market", "d": "2026-10-09", "u": "https://t.me/cahier_de_market/10953"}]})

items.append({"cid": "C016", "attachTo": "",
 "title": "트럼프, 8월 517건 증권거래 공시…메타 최대 2,500만 달러·스페이스X 채권 매수",
 "one": "트럼프 대통령이 8월 한 달 517건, 최대 2억 7,330만 달러 규모의 증권 거래를 신고했고 우주운송 정책 서명 이틀 전 스페이스X 채권을 사들인 사실이 드러나면서, 대통령 포트폴리오와 정책 결정이 겹친다는 이해충돌 논란이 커질 수 있다",
 "facts": [
  "무엇이: 트럼프 대통령의 8월 재산 공시에 매수·매도 517건, 총 7,430만~2억 7,330만 달러 규모의 거래가 담겼다고 CNBC가 분석했습니다 [사실]",
  "메타: 8월 21일 메타 주식을 500만~2,500만 달러어치 사들인 것이 최대 거래였고, 매수는 최소 4,420만 달러, 매도는 최소 3,010만 달러였습니다 [사실]",
  "스페이스X: 8월 18일 금리 5.35%, 2031년 7월 만기 선순위 무담보 채권을 100만~500만 달러어치 샀고, 이틀 뒤 상업 우주운송 확대 정책에 서명했습니다 [사실]",
  "매도: 같은 날 AMD·처치앤드와이트를 각 100만~500만 달러, 엔비디아·보잉·델을 각 50만~100만 달러어치 팔았습니다 [채널]",
  "해명: 백악관은 포트폴리오가 일임 계좌와 컴퓨터 모델로 운용돼 대통령 일가가 투자 결정에 관여할 수 없다고 밝혔습니다 [사실]"],
 "basis": "verified",
 "check": "517건·거래 규모 범위·메타 매수·스페이스X 채권 매수와 정책 서명 시점·백악관 해명은 검색 결과 요약(CNBC 보도와 인용 기사)으로 확인. 개별 매도 종목은 채널 전언",
 "src": [
  {"o": "CNBC", "d": "2026-10-08", "u": "https://www.cnbc.com/2026/10/08/trump-august-trades-meta-spacex-financial-disclosure.html"},
  {"o": "TipRanks", "d": "2026-10-08", "u": "https://www.tipranks.com/news/meta-and-spacex-among-517-transactions-trump-disclosed-for-august"}],
 "inds": ["fin"], "nodes": [],
 "items": [
  {"t": "트럼프, 8월 증권거래 최대 2억 7,300만 달러…메타 주식·스페이스X 채권 매수", "o": B, "d": "2026-10-08", "u": "https://t.me/Badonions/7726"},
  {"t": "트럼프, 8월 메타 주식 최대 2,500만 달러·스페이스X 채권 최대 500만 달러 매입 (CNBC)", "o": H, "d": "2026-10-08", "u": "https://t.me/HANAchina/70085"},
  {"t": "트럼프 8월 517건 거래 신고…스페이스X 채권 매수 이틀 뒤 우주운송 정책 서명", "o": T, "d": "2026-10-09", "u": "https://t.me/TNBfolio/71483"}]})

items.append({"cid": "C023", "attachTo": "",
 "title": "구글, 기업용 범용 AI 에이전트 공개…제미나이·클로드 골라 쓴다",
 "one": "구글 클라우드가 업무 계획부터 코딩·문서 작성까지 스스로 수행하고 제미나이와 앤스로픽 클로드를 작업별로 골라 쓰는 기업용 범용 에이전트를 내놓고 Gemini Enterprise 고객에 추가 비용 없이 주기로 하면서, 업무용 소프트웨어 시장의 에이전트 경쟁이 거세질 수 있다",
 "facts": [
  "무엇이: 구글 클라우드가 10월 8일 Gemini at Work 2026 행사에서 범용 업무 에이전트 'Gemini Agent'를 공개했고, 현재는 비공개 프리뷰 단계입니다 [사실]",
  "모델: 에이전트와 기반 모델을 분리해 제미나이와 앤스로픽 클로드 가운데 작업별로 고르며, 다른 폐쇄형·오픈 모델로 넓힐 계획입니다 [사실]",
  "연동: 웹·모바일·CLI·Google Workspace·Microsoft 365·Slack에서 쓰고 Salesforce·ServiceNow·Jira 등과 MCP로 연결되며, 자체 메일·드라이브를 가진 동료 에이전트도 만들 수 있습니다 [사실]",
  "가격: Gemini Enterprise를 쓸 수 있는 고객에게는 추가 비용 없이 제공하고, 프로젝트별 실시간 지출 한도를 둡니다 [사실]",
  "도입: 구글 클라우드 고객 약 80%가 AI 제품을 쓰고 포춘 100대 기업의 약 90%가 Gemini Enterprise를 쓴다고 구글이 밝혔습니다 [채널]"],
 "basis": "verified",
 "check": "발표 시점·멀티모델(클로드 포함)·연동 범위·추가 비용 없음·프리뷰 단계는 검색 결과 요약으로 확인. 도입 비율 수치는 채널 전언",
 "src": [
  {"o": "9to5Google", "d": "2026-10-08", "u": "https://9to5google.com/2026/10/08/gemini-agent-google-cloud/"},
  {"o": "VentureBeat", "d": "2026-10-08", "u": "https://venturebeat.com/orchestration/google-cloud-unveils-persistent-gemini-agents-for-long-running-tasks-and-they-get-their-own-gmail-calendar-and-drive-storage"}],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "items": [
  {"t": "구글 클라우드, 기업 업무용 범용 AI 에이전트 '제미나이 에이전트' 공개", "o": "텔레그램 미국 주식 인사이더", "d": "2026-10-08", "u": "https://t.me/insidertracking/65748"},
  {"t": "구글 Gemini Agent 세부: 멀티에이전트·멀티모델·기업 시스템 통합", "o": "텔레그램 카이에 de market", "d": "2026-10-08", "u": "https://t.me/cahier_de_market/10949"}]})

items.append({"cid": "C028", "attachTo": "n-bbg-0052",
 "title": "연준 '연내 추가 인상' 기류 속 뉴욕연준 '관세가 상품물가 2.9%p 끌어올려'",
 "one": "연준이 9월 0.25%p 인상 뒤 의사록에서 대다수 위원이 연내 추가 인상을 지지한 가운데, 뉴욕연준 연구진이 관세가 없었다면 2월 기준 상품 물가가 오히려 약 0.9% 내렸을 것이라고 분석해, 관세가 물가를 떠받친다는 근거가 더해지고 있다",
 "facts": [
  "무엇이: 뉴욕연준 연구진이 10월 6일 관세 때문에 67개 상품군 물가가 2월 기준 2.9%p 더 올랐다고 분석했습니다 [사실]",
  "반사실: 관세가 없었다면 해당 상품 물가는 약 0.9% 내렸을 것으로 추정됐고, 가계 소비 전체로 넓히면 영향은 약 0.6%p로 계산됩니다 [사실]",
  "연준: 9월 기준금리를 3.75~4.00%로 올렸고 의사록에서 대다수 위원이 연내 추가 인상이 적절하다고 봤습니다 [사실]",
  "시장: 10월 인상 확률은 약 24%로 낮아져 10월 동결·12월 인상 쪽으로 기대가 옮겨갔습니다 [사실]",
  "반박: 백악관은 관세 비용을 결국 외국 수출업체가 부담할 것이라고 반박했습니다 [사실]"],
 "basis": "verified",
 "check": "뉴욕연준 분석(10월 6일, 67개 상품군 2.9%p, 반사실 약 -0.9%)은 검색 결과 요약으로 확인. 채널의 '-2.9% 추가 하락해 디플레이션'은 2.9%p 기여도와 -0.9% 반사실을 섞은 표현으로 보여 확인된 수치로 씀",
 "src": [
  {"o": "CNBC", "d": "2026-10-08", "u": "https://www.cnbc.com/2026/10/08/inflation-tariffs-trump-fed-consumer-goods.html"},
  {"o": "Washington Post", "d": "2026-10-07", "u": "https://www.washingtonpost.com/business/2026/10/07/tariffs-drove-up-prices-consumer-goods-study-finds/"},
  {"o": "Daybreak Wire", "d": "2026-10-08", "u": "https://daybreakwire.com/business/ny-fed-tariffs-2-9-points-goods-inflation/"}],
 "inds": ["macro"], "nodes": ["macro/inflation", "macro/cb"],
 "items": [
  {"t": "뉴욕연준 '관세 없었다면 2월 물가 하락해 디플레이션 영역'", "o": "텔레그램 Polaristimes", "d": "2026-10-09", "u": "https://t.me/The_MariTimes/63607"}]})

items.append({"cid": "C031", "attachTo": "n-tg-0187",
 "title": "허리케인 이사야스 멕시코만 상륙 임박…원유 63% 중단 속 정유설비 14%도 경로에",
 "one": "2등급 허리케인 이사야스가 미 멕시코만 북부 상륙을 앞두고 원유 생산 약 63%(하루 128만 배럴)를 멈춰 세운 데 이어, 경로 인근에 미 정유능력의 14%인 하루 270만 배럴이 몰려 있어 차질이 정유 부문까지 번질 수 있다",
 "facts": [
  "무엇이: 미 국립기상청은 이사야스가 금~토요일 멕시코만 북부 해안에 큰 폭풍해일·강풍·홍수를 일으키고 남동부 내륙까지 영향을 줄 것으로 예보했습니다 [채널]",
  "생산: 10월 8일 기준 멕시코만 원유 생산 약 62.9%(하루 128만 배럴)와 가스 57.4%가 중단됐고, 유인 플랫폼 371곳 중 121곳이 대피했습니다 [사실]",
  "정유: 미 정유능력의 약 14%인 하루 270만 배럴이 예상 경로 안팎에 있고, 1등급이라도 정상화에 약 1주일이 걸릴 수 있다는 분석입니다 [사실]",
  "경로: 뉴올리언스 동쪽 상륙이 예상돼 핵심 에너지 설비 일부는 비켜갈 수 있고, 피해가 없으면 점검 뒤 생산 재개는 빠를 수 있습니다 [사실]"],
 "basis": "partial",
 "check": "생산 중단 비율·대피 플랫폼·정유능력 노출(CNN, 리포 오일)·상륙 예상 위치는 검색 결과 요약으로 확인. 국립기상청 예보 세부와 실제 상륙 여부는 확인 못 함",
 "src": [
  {"o": "CNN", "d": "2026-10-08", "u": "https://www.cnn.com/2026/10/08/economy/isaias-oil-refineries-gulf-coast-hurricanes"},
  {"o": "gCaptain", "d": "2026-10-08", "u": "https://gcaptain.com/hurricane-isaias-shuts-down-nearly-two-thirds-of-gulf-oil-production/"}],
 "inds": ["macro", "gas"], "nodes": ["macro/commodity", "gas/upstream"],
 "items": [
  {"t": "미 기상청 '허리케인 이사야스, 멕시코만 북부에 폭풍해일·강풍·홍수'", "o": "텔레그램 미국 주식 인사이더", "d": "2026-10-09", "u": "https://t.me/insidertracking/65801"}]})

items.append({"cid": "C036", "attachTo": "n-tg-0132",
 "title": "셰프초비치 EU 집행위원 방중 무역협의…中, 하이브리드차 수출 자율제한은 거부",
 "one": "셰프초비치 EU 무역 집행위원이 베이징에서 왕원타오 상무부장과 대중 무역적자와 희토류 수출통제를 협의하는 가운데 중국이 하이브리드차 수출 자율제한 요구를 거부해, EU의 세이프가드 도입과 유럽 완성차의 가격 경쟁 부담이 커질 수 있다",
 "facts": [
  "무엇이: 셰프초비치 EU 무역·경제안보 집행위원이 10월 8일 베이징에서 왕원타오 중국 상무부장과 회담하며 이틀간 무역투자이사회 협의를 시작했습니다 [사실]",
  "의제: EU는 2022년 이후 최대인 대중 무역적자를 '지속 불가능'하다고 보고 희토류 수출통제 완화도 요구했으나, 다음 주 EU 정상회의 전 돌파구는 어렵다는 관측이 많습니다 [사실]",
  "하이브리드: 중국 상무부는 EU의 하이브리드차 수출 자율제한(시장의 약 15%) 요구를 WTO 규칙 위반이라며 거부했습니다 [사실]",
  "대안: EU 집행위는 일정 물량 초과분에 관세를 매기는 한시 세이프가드를 검토하고 있습니다 [사실]",
  "중국차 공세: 10월 12~18일 파리모터쇼에 중국 브랜드 20여 개가 하이브리드를 앞세워 참가합니다 [사실]"],
 "basis": "verified",
 "check": "셰프초비치-왕원타오 회담(10월 8일)과 무역적자·희토류 의제, 돌파구 기대 낮음은 검색 결과 요약으로 확인. 하이브리드·세이프가드·파리모터쇼는 기존 문서 근거",
 "src": [
  {"o": "CGTN", "d": "2026-10-08", "u": "https://news.cgtn.com/news/2026-10-08/Chinese-commerce-minister-meets-with-EU-trade-chief-in-Beijing-1R4VxG03528/p.html"},
  {"o": "Al Jazeera", "d": "2026-10-07", "u": "https://www.aljazeera.com/economy/2026/10/7/eu-china-trade-talks-begin-in-beijing-amid-escalating-pressure"}],
 "inds": ["macro", "auto"], "nodes": ["macro/geo"],
 "items": [
  {"t": "셰프초비치 EU 무역 집행위원, 이번 주 방중해 왕원타오 상무부장과 회담", "o": "텔레그램 Polaristimes", "d": "2026-10-08", "u": "https://t.me/The_MariTimes/63596"}]})

items.append({"cid": "C046", "attachTo": "",
 "title": "애플, 10월 27일께 첫 터치스크린 OLED 맥북 프로·OLED 아이패드 미니 공개 예정",
 "one": "애플이 10월 27일 전후 행사에서 첫 터치스크린 OLED 맥북 프로와 OLED 아이패드 미니, M6 칩 아이맥 등을 내놓을 계획이어서, 맥 제품군에 OLED 디스플레이 채택이 처음으로 넓어질 전망이다",
 "facts": [
  "무엇이: 애플이 10월 27일 전후 행사에서 14·16인치 터치스크린 OLED 맥북 프로를 처음 공개할 계획이라고 보도됐습니다 [사실]",
  "사양: 새 맥북 프로는 다이내믹 아일랜드를 처음 넣고 더 가벼워지며 M5 프로·맥스 칩을 쓸 것으로 알려졌습니다 [사실]",
  "동반 제품: OLED 아이패드 미니와 M6 칩을 단 보급형 14인치 맥북 프로·아이맥도 함께 나올 예정입니다 [사실]",
  "일정: 10월 13일에는 스마트홈 허브 등 홈 제품 발표가 먼저 있고, 애플은 아직 일정을 확인하지 않았습니다 [사실]"],
 "basis": "verified",
 "check": "10월 27일 전후 출시 계획과 제품 구성은 검색 결과 요약(MacRumors·9to5Mac 등 블룸버그 보도 인용)으로 확인. 애플 공식 확인은 없음",
 "src": [
  {"o": "MacRumors", "d": "2026-10-08", "u": "https://www.macrumors.com/2026/10/08/apple-october-27-macbook-pro/"},
  {"o": "9to5Mac", "d": "2026-10-08", "u": "https://9to5mac.com/2026/10/08/apple-to-launch-touchscreen-macbook-pro-and-more-on-october-27-report/"}],
 "inds": ["tech"], "nodes": [],
 "items": [
  {"t": "애플, 10월 말 첫 터치스크린 맥북·신형 아이패드 미니 출시 예정 보도", "o": H, "d": "2026-10-09", "u": "https://t.me/HANAchina/70096"}]})

items.append({"cid": "C051", "attachTo": "",
 "title": "인도네시아, 中 자금 고속철 운영사 지분 60% 정부 이전…9월 시한 넘겨도 추진",
 "one": "인도네시아가 9월 시한을 넘겼지만 중국 자금으로 지은 73억 달러 규모 고속철 운영사의 지분 60%를 재무부 등으로 옮기는 작업을 이어가면서, 국영기업이 떠안던 고속철 부채가 국가 재정으로 넘어가게 된다",
 "facts": [
  "무엇이: 인도네시아 재무부 고위 관계자가 9월 시한을 넘겼지만 고속철 운영사 KCIC 지분 이전을 계속 추진한다고 밝혔습니다 [사실]",
  "구조: 국영기업 컨소시엄 PSBI가 KCIC 지분 60%를, 중국 컨소시엄이 40%를 갖고 있으며, 재무부가 다난타라로부터 지분을 넘겨받아 향후 부채 상환을 맡는 방식입니다 [사실]",
  "부채: 연 약 1조 루피아(약 5,670만 달러)씩 80년에 걸쳐 갚는 구조조정안이 거론됩니다 [사실]",
  "변수: 재무장관이 교체됐지만 다난타라는 이전 절차가 예정대로라고 밝혔고, 경제학자들은 기술 역량이 부족한 재무 조직이 맡는 데 우려를 나타냈습니다 [사실]"],
 "basis": "partial",
 "check": "지분 60% 구조, 재무부 인수·80년 분할 상환안, 재무장관 교체는 검색 결과 요약으로 확인. 이전 완료 시점은 확인 못 함",
 "src": [
  {"o": "ANTARA", "d": "2026-08", "u": "https://en.antaranews.com/news/431864/finance-ministry-to-acquire-60-percent-stake-in-whoosh-train-operator"},
  {"o": "Jakarta Globe", "d": "2026-10", "u": "https://jakartaglobe.id/business/indonesia-china-discuss-whoosh-train-debt-by-video-calls-says-rosan"},
  {"o": "China Global South Project", "d": "2026-10-09", "u": "https://chinaglobalsouth.com/2026/10/09/indonesia-whoosh-railway-stake-transfer/"}],
 "inds": ["industrial"], "nodes": [],
 "items": [
  {"t": "인도네시아, 지연에도 中 자금 고속철 지분 인수 계획 순항", "o": "로이터", "d": "2026-10-09", "u": "https://www.reuters.com/world/asia-pacific/indonesia-plan-stake-china-funded-bullet-train-track-despite-delay-2026-10-09/"}]})

items.append({"cid": "C056", "attachTo": "",
 "title": "IMF 구제 30년 만에 태국 경제 새 시험대…저성장·가계부채 85%에 재정 여력 축소",
 "one": "태국이 IMF 구제금융 이후 30년 가까이 지나 5년 평균 2.34%의 저성장과 GDP 대비 85.2%인 가계부채에 묶인 가운데, 공공부채가 법정 상한 70%에 다가서 재정으로 경기를 떠받칠 여력도 줄고 있다",
 "facts": [
  "무엇이: 태국은 최근 5년 연평균 성장률이 2.34%에 그쳐 역내 국가보다 회복이 더디고, 다음 주 방콕에서 IMF·세계은행 연차총회를 엽니다 [사실]",
  "가계: 6월 말 가계부채는 GDP 대비 85.2%로 아시아 최고 수준이며, 태국 중앙은행은 성장을 잠재 수준 아래로 묶을 수 있다고 경고했습니다 [사실]",
  "재정: 공공부채는 2025회계연도 말 GDP 대비 65.08%로 법정 상한 70%에 다가섰고, 내각은 새 회계연도 약 1조 2,600억 바트 차입을 승인했습니다 [사실]",
  "전망: 재무장관은 3년 안에 3% 성장을 목표로 하지만 세계은행의 올해 전망은 약 2%에 그칩니다 [사실]"],
 "basis": "partial",
 "check": "성장률·가계부채·공공부채·차입 승인·세계은행 전망은 검색 결과 요약으로 확인. 로이터 기사 본문의 논지 전체는 확인 못 함",
 "src": [
  {"o": "Free Malaysia Today", "d": "2026-10-08", "u": "https://www.freemalaysiatoday.com/category/business/2026/10/08/thai-household-debt-trap-tests-growth-ambitions-as-bangkok-hosts-imf"},
  {"o": "Nation Thailand", "d": "2026", "u": "https://www.nationthailand.com/news/policy/40071657"},
  {"o": "Thai Examiner", "d": "2026-10-08", "u": "https://www.thaiexaminer.com/thai-news-foreigners/2026/10/08/thailand-still-struggles-economically-even-with-revised-world-bank-gdp-growth-for-2026-coming-at-2/"}],
 "inds": ["macro"], "nodes": ["macro/growth", "macro/fiscal"],
 "items": [
  {"t": "IMF 구제 30년 가까이 지나 새 경제 시험대에 선 태국", "o": "로이터", "d": "2026-10-09", "u": "https://www.reuters.com/world/asia-pacific/nearly-30-years-after-imf-rescue-thailand-faces-new-economic-test-2026-10-09/"}]})

items.append({"cid": "C061", "attachTo": "",
 "title": "英 건자재 유통 SIG, 재무책임자 케스터턴을 차기 CEO로 지명…주가 8.4% 상승",
 "one": "영국 건자재 유통업체 SIG가 재무책임자 사이먼 케스터턴을 2027년 5월 1일자 차기 최고경영자로 지명하면서, 현금 1억 파운드 창출 등 '비전 2030' 목표를 이어갈 체제가 정해지고 주가는 8.4% 올랐다",
 "facts": [
  "무엇이: SIG가 10월 9일 재무책임자 사이먼 케스터턴을 2027년 5월 1일부터 최고경영자로 선임한다고 밝혔습니다 [사실]",
  "승계: 현 최고경영자 핌 페르바트는 같은 날 비상임 의장으로 옮기며, 2025년 7월 예고한 승계 계획의 일부입니다 [사실]",
  "목표: 2027년 말까지 최소 1억 파운드 현금 창출, 2028년 중반까지 연 5천만 파운드 영업이익 개선 목표는 그대로입니다 [사실]",
  "시장: 발표 당일 SIG 주가는 8.4% 올랐고, 후임 재무책임자 선임 절차를 시작했습니다 [사실]"],
 "basis": "verified",
 "check": "선임 일자·승계 구조·비전 2030 목표·주가 반응은 검색 결과 요약으로 확인",
 "src": [
  {"o": "ADVFN", "d": "2026-10-09", "u": "https://uk.advfn.com/market-news/article/24363/sig-shares-rise-8-4-as-cfo-simon-kesterton-is-appointed-next-chief-executive"},
  {"o": "Building", "d": "2026-10-09", "u": "https://www.building.co.uk/news/former-kier-finance-chief-to-take-top-role-at-sig/5144555.article"}],
 "inds": ["industrial"], "nodes": [],
 "items": [
  {"t": "영국 SIG, 재무책임자 사이먼 케스터턴을 차기 CEO로 지명", "o": "로이터", "d": "2026-10-09", "u": "https://www.reuters.com/world/uk/uks-sig-names-finance-chief-simon-kesterton-next-ceo-2026-10-09/"}]})

items.append({"cid": "C066", "attachTo": "",
 "title": "英 옥스퍼드 메트릭스, 엔터 업계 지출 축소에 연간 적자 경고…주가 11년 만에 최저",
 "one": "영국 옥스퍼드 메트릭스가 영화·TV·게임 업계 지출 축소와 미국 연구비 제약으로 모션캡처 계약이 늦어지자 이번 회계연도 조정 영업손실을 예고하면서, 주가가 2015년 3월 이후 최저로 떨어졌다",
 "facts": [
  "무엇이: 옥스퍼드 메트릭스가 15개월로 늘린 이번 회계연도에 조정 영업손실 50만~390만 파운드를 예상해, 시장 예상 300만 파운드 이익을 밑돌 것이라고 밝혔습니다 [사실]",
  "원인: 영화·TV·게임 스튜디오 통합과 투자 축소, 미국 연구비 제약으로 비콘 모션캡처 대형 계약이 미뤄졌습니다 [사실]",
  "매출: 매출 전망은 4,700만~5,100만 파운드로 시장 예상 5,620만 파운드에 못 미칩니다 [사실]",
  "대응: 연 150만~200만 파운드 비용 절감, 무브AI 기술·인력 52만 5천 파운드 인수, 최대 300만 파운드 자사주 매입을 내놨고 로봇 업체 주문은 늘고 있습니다 [사실]"],
 "basis": "verified",
 "check": "손실 범위·매출 전망·원인·대응책과 주가 2015년 3월 이후 최저는 검색 결과 요약으로 확인",
 "src": [
  {"o": "The Market Reporter", "d": "2026-10-09", "u": "https://www.themarketreporter.co.uk/a/08c8ec7c/oxford-metrics-warns-of-full-year-loss-as-film-studios-and-researchers-c"},
  {"o": "UK Investor Magazine", "d": "2026-10-09", "u": "https://ukinvestormagazine.co.uk/oxford-metrics-shares-sink-on-profit-warning-as-entertainment-and-research-demand-weakens/"}],
 "inds": ["tech"], "nodes": [],
 "items": [
  {"t": "영국 옥스퍼드 메트릭스, 엔터 업계 지출 삭감에 연간 손실 경고", "o": "로이터", "d": "2026-10-09", "u": "https://www.reuters.com/world/uk/uks-oxford-metrics-warns-about-annual-loss-entertainment-industry-spending-cuts-2026-10-09/"}]})

items.append({"cid": "C071", "attachTo": "",
 "title": "유럽 석유 메이저 3분기도 이익 강세 전망…셸 정제마진 배럴당 42달러로 급등",
 "one": "유럽 석유 메이저의 3분기 이익이 강한 증가세를 이어갈 것으로 보이는 가운데, 셸이 3분기 지표 정제마진을 2분기 24달러에서 42달러로 제시하고 브렌트 분기 평균이 90달러를 넘어 정유·트레이딩 이익이 커질 전망이다",
 "facts": [
  "무엇이: 유럽 석유 메이저들의 강한 이익 증가세가 3분기에도 이어졌을 것으로 예상됩니다 [제목]",
  "셸: 3분기 지표 정제마진은 배럴당 42달러로 2분기 24달러에서 크게 뛰었고, 정제설비 가동률은 93~97%로 제시했습니다 [사실]",
  "반대 흐름: 셸의 지표 화학 마진은 톤당 270달러에서 208달러로 떨어졌고, 마케팅 이익도 2분기보다 낮을 전망입니다 [사실]",
  "BP: 3분기 생산은 중동 차질과 멕시코만 기상 영향을 반영해 하루 210만~225만 배럴(석유환산)로 제시했고, 정제마진은 높게 유지될 것으로 봤습니다 [사실]",
  "일정: 셸은 10월 29일 3분기 실적을 발표합니다 [사실]"],
 "basis": "partial",
 "check": "셸 3분기 업데이트(정제마진 42달러, 화학 마진 하락, 브렌트 90달러 이상)와 BP 가이던스는 검색 결과 요약으로 확인. 토탈에너지 등 다른 메이저의 3분기 전망은 확인 못 함",
 "src": [
  {"o": "Shell", "d": "2026-10-07", "u": "https://www.shell.com/news-and-insights/newsroom/news-and-media-releases/2026/shell-third-quarter-2026-update-note/_jcr_content/root/main/section/simple_copy/call_to_action/links/item0.stream/1791349231897/c8861121920e47d0e80c3ff047537e15e0580dae/q3-2026-quarterly-update-note.pdf"},
  {"o": "Rigzone", "d": "2026-10-07", "u": "https://www.rigzone.com/news/shell_expects_strong_trading_results_for_q3-07-oct-2026-184789-article"}],
 "inds": ["macro", "petchem"], "nodes": ["macro/commodity", "petchem/commodity"],
 "items": [
  {"t": "유럽 석유 메이저, 3분기에도 강한 이익 증가세 이어갔을 듯", "o": "로이터", "d": "2026-10-09", "u": "https://www.reuters.com/business/european-majors-strong-earnings-growth-expected-have-continued-q3-2026-10-09/"}]})

items.append({"cid": "C076", "attachTo": "",
 "title": "홍콩 헤지펀드 세간티 내부자거래 재판 종결…판결은 2월 선고 예정",
 "one": "홍콩 헤지펀드 세간티와 창업자 사이먼 새들러의 에스프리 블록딜 내부자거래 재판이 마무리되고 판결이 2월로 잡히면서, 아시아 블록딜 시장을 흔든 사건의 법적 불확실성이 몇 달 더 이어지게 됐다",
 "facts": [
  "무엇이: 세간티 내부자거래 재판이 끝났고 판결은 2월에 나올 예정입니다 [제목]",
  "사건: 세간티와 사이먼 새들러, 전 트레이더 대니얼 라로카가 2017년 에스프리 블록딜 관련 내부자거래 혐의로 기소돼 2026년 5월 홍콩 지방법원 재판에서 무죄를 주장했습니다 [사실]",
  "쟁점: 검찰 측 전문가는 피고인들이 2017년 6월 14일 거래로 160만~170만 홍콩달러를 벌었다고 추산했습니다 [사실]",
  "처벌: 유죄 시 최대 징역 7년에 처해질 수 있습니다 [사실]"],
 "basis": "partial",
 "check": "기소 내용·재판 개시·최종변론 단계·최대 형량은 검색 결과 요약으로 확인. 재판 종결과 2월 선고 일정은 제목에만 근거",
 "src": [
  {"o": "Hedgeweek", "d": "2026", "u": "https://hedgeweek.com/news/segantii-insider-trading-trial-heads-towards-conclusion-in-hong-kong"},
  {"o": "The Standard", "d": "2026-05-04", "u": "https://www.thestandard.com.hk/finance/article/331037/Hong-Kongs-block-trade-king-pleads-not-guilty-as-Segantii-insider-trading-trial-begins"},
  {"o": "SCMP", "d": "2026", "u": "https://www.scmp.com/news/hong-kong/law-and-crime/article/3352518/hong-kong-block-trade-king-exploited-bank-lapse-make-hk17-million-court-told"}],
 "inds": ["fin"], "nodes": [],
 "items": [
  {"t": "세간티 내부자거래 재판 종결, 판결은 2월 예정", "o": "블룸버그", "d": "2026-10-09", "u": "https://www.bloomberg.com/news/articles/2026-10-09/segantii-insider-trading-trial-ends-with-verdict-due-february"}]})

items.append({"cid": "C081", "attachTo": "",
 "title": "벤딩스푼스 CEO, 'SaaS 종말론' 급락장에서 인수 기회 본다",
 "one": "소프트웨어 인수 기업 벤딩스푼스의 최고경영자가 SaaS 기업 가치가 한꺼번에 무너진 이른바 'SaaS 종말' 국면을 매수 기회로 보면서, 가치가 떨어진 소프트웨어 기업을 겨냥한 인수가 늘어날 수 있다",
 "facts": [
  "무엇이: 벤딩스푼스 최고경영자가 'SaaS 종말' 국면에서 매수 기회를 본다고 밝혔습니다 [제목]",
  "인수 기준: 루카 페라리 최고경영자는 5년 이상 실적 궤적을 예측할 수 있고 기술·제품으로 매출과 비용을 개선할 수 있는 기업을 고른다고 말해 왔습니다 [사실]",
  "금리: 그는 금리가 오르면 부채 비용보다 인수 가격 하락의 이득이 더 커 연쇄 인수자에게 유리할 수 있다고 봤습니다 [사실]",
  "경쟁: 소프트웨어 전문 사모펀드의 신규 자금 모집이 줄어 인수 경쟁이 약해질 수 있습니다 [추론]"],
 "basis": "partial",
 "check": "이번 발언 자체('SaaSpocalypse')는 확인 못 함. 페라리의 인수 기준과 금리 관련 기존 발언은 팟캐스트 요약 등 검색 결과로 확인",
 "src": [
  {"o": "BigGo Finance(Sourcery 요약)", "d": "2026", "u": "https://finance.biggo.com/news/203624e4a75db892"},
  {"o": "Blue|Pier Capital", "d": "2026", "u": "https://bluepiercapital.substack.com/p/the-salvors-premium-part-ii"}],
 "inds": ["tech"], "nodes": [],
 "items": [
  {"t": "벤딩스푼스 CEO, 'SaaS 종말' 국면에서 매수 기회 포착", "o": "블룸버그", "d": "2026-10-09", "u": "https://www.bloomberg.com/news/articles/2026-10-09/bending-spoons-ceo-sees-buying-opportunities-in-saaspocalypse"}]})

skipped = [{"cid": "C041", "reason": "범위 밖 (상반기 조선 통계는 7월 23일 공표된 사건의 재탕)"}]

out = {"agent": "W4", "searches_used": 18, "fetches_used": 0, "items": items, "skipped": skipped}
p = "/home/user/news-desk/data/mix-2026-10-09/out2/W4.json"
json.dump(out, open(p, "w"), ensure_ascii=False, indent=1)
for x in items:
    n = len(re.sub(r' \((제목 기준|채널 전언)\)$', '', x['one']))
    single = len(x['items']) == 1 and not x['attachTo']
    lo, hi = (80, 130) if single else (90, 160)
    flag = "" if lo <= n <= hi else "  <-- OUT"
    print(x['cid'], n, len(x['title']), [len(i['t']) for i in x['items']], flag)
    for f in x['facts']:
        assert '|' not in f and '**' not in f
