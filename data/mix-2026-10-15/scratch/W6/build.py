import json

def I(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s is not None:
        x["s"] = s
    return x

TB = "블룸버그"; TR = "로이터"
items = []

# G1-004
items.append({
 "cid": "G1-004", "attachTo": "n-tg-0140",
 "title": "美 10년물 5.08%로 3주 최저…월가는 베선트 장기물 발행 축소 신호 주시",
 "one": "기술주 급락에 안전자산 매수가 몰려 미 10년물 금리가 5.08% 안팎 3주 최저로 내려왔지만, 라보뱅크가 재정 부채를 금리 상승의 가장 지속적 요인으로 꼽고 월가가 베선트 재무부의 장기물 발행 축소 신호를 기다리면서 금리 방향이 국채 공급 결정에 달리게 됐다",
 "facts": [
  "무엇이: 10월 15일 미 10년물 금리는 기술·AI주 매도에 국채로 돈이 몰리며 5.08~5.09% 안팎으로 내려 9월 25일 이후 3주 만의 최저를 기록했습니다 [사실]",
  "진단: 라보뱅크는 연준 인상 기대가 10년물을 5%로, 사상 최악 수준의 입찰 결과에 따른 기간 프리미엄 상승이 5.31%로 끌어올렸다며 공공부채가 수년간 가장 지속적인 상승 요인이 될 것이라고 봤습니다 [채널]",
  "발행: 금요일 프라이머리 딜러 설문을 앞두고 씨티는 장기물 발행 축소나 20년물 발행 취소 가능성을, 모건스탠리는 중간선거 직후인 11월 차환 발행 발표의 중요성을 짚었습니다 [채널]",
  "시각: BNY 로빈 빈스 CEO는 약 5.25%의 10년물 금리가 역사적으로 이례적이지 않다며 경제 강세와 AI 구축용 부채 발행 증가를 상승 요인으로 꼽았습니다 [사실]",
  "칠레: 미 금리 하락에 건 칠레 AFP의 약 77억 달러 평가손실에 앞서 위험 경고가 나왔지만 받아들여지지 않았다는 보도가 나왔습니다 [제목]"
 ],
 "basis": "partial",
 "check": "10년물 3주 최저(5.08~5.09%)와 BNY CEO 발언은 검색 결과 요약으로 확인. 프라이머리 딜러 설문·씨티 20년물 취소 전망, 라보뱅크 진단, 헤지펀드 공매도 수치는 채널 전언으로 독립 확인 못 함. L&G 헤지·캐나다 보유 증가·칠레 경고는 제목 기준",
 "src": [
  {"o": "Economies.com", "d": "2026-10-15", "u": "https://www.economies.com/markets/americas-news/us-10-year-treasury-yields-fall-to-three-week-low-as-fed-remarks-ease-rate-hike-bets-50140"},
  {"o": "FXStreet", "d": "2026-10-15", "u": "https://www.fxstreet.com/news/japanese-yen-holds-firm-despite-hotter-than-expected-us-producer-inflation-202610151418"},
  {"o": "Traders Union", "d": "2026-10-15", "u": "https://tradersunion.com/news/institutions/show/3825451-bny-ceo-10-year-yield-normalization/"}
 ],
 "inds": ["macro"], "nodes": ["macro/rates", "macro/fiscal"],
 "vc": [
  {"ind": "macro", "node": "rates", "f": "가격", "dir": "down", "k": "실제", "t": "기술주 급락에 10년물 금리 3주 최저로 하락"},
  {"ind": "macro", "node": "fiscal", "f": "공급", "dir": "down", "k": "예상", "t": "장기물 발행 축소와 20년물 발행 취소 가능성"}
 ],
 "added": "이번 텔레그램 6건·블룸버그 7건·로이터 1건으로 10년물의 3주 최저 하락, 라보뱅크의 재정 부채 경고, 베선트 재무부의 장기물 발행 축소 가능성, 헤지펀드 공매도 36% 쏠림이 추가됐다",
 "items": [
  I("라보뱅크 '美 10년물 5.31%는 연준 아닌 재정 부채가 밀어 올려'", "텔레그램 하나증권 중국전략", "2026-10-14", "https://t.me/HANAchina/70403",
    "라보뱅크가 10년물 상승을 연준발 5%와 입찰 부진·기간 프리미엄발 5.31%의 두 단계로 나누면서, 공공부채가 수년간 금리를 밀어 올릴 가장 지속적 요인이라고 경고했다"),
  I("L&G, 매도세 위험에 대비해 채권 매입분 헤지", TB, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/l-g-is-hedging-its-bond-purchases-against-risk-of-selloff",
    "영국 L&G가 채권을 사들이면서도 매입분을 매도세 위험에 대비해 헤지하면서, 채권 매수와 금리 급등 방어를 함께 택했다 (제목 기준)"),
  I("래리 핑크 '50년 경력에 처음 보는 진정한 자본 부족'", "텔레그램 TNBfolio", "2026-10-15", "https://t.me/TNBfolio/71549",
    "래리 핑크 블랙록 회장이 40조 달러로 불어난 미 국가부채와 급증한 민간 자본 수요가 겹쳐 자본 부족이 시작됐다고 하면서, 커지는 국채 입찰이 신용 수요를 압박한다고 짚었다"),
  I("기술주 급락이 성장 위협하자 미 국채 강세", TB, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/treasuries-extend-gains-as-equities-selloff-dents-risk-sentiment",
    "기술·AI주 급락이 성장 우려를 키우면서 투자자들이 미 국채로 몰려 국채 가격이 오르고 금리가 내려왔다"),
  I("美 10년물 5.089%·30년물 5.431%로 나란히 3주 만에 최저", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66352",
    "미 10년물 금리가 5.089%, 30년물이 5.431%로 내려 3주 만의 최저를 기록하고 독일 10년물도 3.386%로 2주 최저까지 밀리면서 선진국 장기금리가 함께 내렸다"),
  I("AI·금리 공포 맞물리며 시장의 평온 깨져", TB, "2026-10-15", "https://www.bloomberg.com/news/newsletters/2026-10-15/market-calm-shatters-as-ai-rate-fears-collide",
    "AI 우려와 금리 공포가 한꺼번에 부딪히면서 그동안 이어지던 금융시장의 평온이 깨졌다 (제목 기준)"),
  I("월가, 베선트 재무장관의 국채 금리 대응 재개에 촉각", TB, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/wall-street-on-alert-for-treasury-s-scott-bessent-to-act-on-bond-yields-again",
    "월가가 베선트 재무장관이 다시 국채 금리에 손을 댈 가능성에 대비하면서, 재무부 발행 정책이 장기금리의 변수로 떠올랐다 (제목 기준)"),
  I("BNY CEO '美 10년물 금리 수준, 전례 없는 일 아냐'", TR, "2026-10-16", "https://www.reuters.com/business/finance/us-10-year-treasury-yield-levels-not-unprecedented-bny-ceo-says-2026-10-15/",
    "BNY 로빈 빈스 CEO가 약 5.25%의 10년물 금리는 역사적으로 이례적이지 않은 정상화라고 하면서, 경제 강세와 AI 구축용 부채 발행 증가를 상승 요인으로 꼽았다"),
  I("美 금리 베팅이 수십억 달러 날리기 전 칠레에선 경고가 무시됐다", TB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/before-us-rate-bets-wiped-out-billions-warnings-were-ignored-in-chile",
    "칠레 연기금의 미 금리 하락 베팅이 수십억 달러 손실로 번지기 전에 위험 경고가 나왔지만 받아들여지지 않았다는 보도가 나왔다 (제목 기준)"),
  I("칠레 AFP, 파생상품 늘리는 동안 위험 경고 있었다", TB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/afp-de-chile-advirtieron-riesgos-mientras-aumentaban-derivados-mv9vmy1r",
    "칠레 AFP들이 위험 경고가 나오던 시기에도 파생상품 규모를 늘려 온 것으로 전해지면서, 미 금리 베팅 손실의 경위가 드러났다 (제목 기준)"),
  I("FT '美 국채 평균 만기 5.9년, 주요 선진국 중 가장 짧아'", "텔레그램 미국 주식 인사이더", "2026-10-16", "https://t.me/insidertracking/66396",
    "FT 집계에서 미국 정부 부채의 평균 만기가 5.9년으로 주요 선진국 중 가장 짧고 단기 국채 비중도 가장 높게 나타나, 미 재무부의 단기물 의존이 드러났다"),
  I("캐나다의 美 국채·채권 보유 증가 뒤엔 중국이 있을 수도", TB, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-15/china-may-be-behind-canada-s-growing-us-treasury-bond-holdings",
    "캐나다의 미 국채·채권 보유가 늘어나는 배경에 중국 자금이 있을 수 있다는 분석이 나오면서, 미 국채 해외 수요의 실제 주인이 관심사가 됐다 (제목 기준)"),
  I("헤지펀드 美 10년물 국채 공매도 204만 계약, 시장의 36%", "텔레그램 카이에 de market", "2026-10-16", "https://t.me/cahier_de_market/11014",
    "웰링턴 전략가 제임스 손이 헤지펀드의 10년물 국채 공매도가 204만 계약으로 시장의 36%에 이르렀다고 짚으면서, 국채 공매도의 주도권이 헤지펀드로 넘어갔다고 봤다"),
  I("씨티 '딜러 설문, 장기물 축소·20년물 발행 취소 시사할 수도'", "텔레그램 하나증권 중국전략", "2026-10-16", "https://t.me/HANAchina/70492",
    "월가가 금요일 프라이머리 딜러 설문에서 베선트 재무부의 금리 억제 단서를 찾는 가운데, 씨티가 장기물 발행 축소나 20년물 발행 취소 가능성을 제시했다"),
 ]})

# G1-013
items.append({
 "cid": "G1-013", "attachTo": "n-rtr-0021",
 "title": "우간다, 기준금리 9.75%→12% 긴급 인상…실링 이틀째 급반등",
 "one": "실링이 사상 최저로 밀리자 우간다 중앙은행이 10월 14일 긴급회의에서 기준금리를 9.75%에서 12%로 225bp 올리면서 실링이 이틀 연속 반등했지만, 물가 전망은 7~7.5%로 높아지고 성장률 전망은 6~6.5%로 낮아졌다",
 "facts": [
  "무엇이: 우간다 중앙은행이 10월 14일 긴급 통화정책회의에서 기준금리를 9.75%에서 12%로 225bp 올렸고, 11월 12일 정례회의를 앞당긴 결정입니다 [사실]",
  "배경: 아팅기에고 총재는 실링 약세가 물가로 번질 수 있다고 경고했고, 고유가에 따른 석유 수입업체의 달러 수요와 자금 유입 감소를 압력으로 들었습니다. 9월 물가는 4.6%, 향후 12개월 전망은 7~7.5%입니다 [사실]",
  "실링: 중앙은행 고시 중간환율은 결정 당일 달러당 약 4,130실링에서 약 3,951실링으로 강해졌고, 실링은 이틀째 올랐습니다 [사실]",
  "성장: 중앙은행은 2026/27 회계연도 성장률 전망을 7~7.5%에서 6~6.5%로 낮췄고, JP모건은 압력이 이어지면 추가 인상이 있을 수 있다고 봤습니다 [사실]",
  "주변국: 남아공 크가냐고 총재는 물가 상방 위험을 짚었고 무디스는 남아공이 등급 상향 궤도에 있다고 봤으며, IMF는 아프리카의 회복력이 물가 위협과 취약한 완충력을 가린다고 경고했습니다 [제목]"
 ],
 "basis": "verified",
 "check": "우간다 금리 12% 인상, 인상 폭, 환율 변화, 물가·성장 전망은 검색 결과 요약으로 확인. 남아공·IMF·나이지리아 글은 제목 기준",
 "src": [
  {"o": "BusinessDay", "d": "2026-10-14", "u": "https://www.businessday.co.za/world/africa/2026-10-14-uganda-lifts-interest-rate-to-12-at-emergency-meeting/"},
  {"o": "CNBC Africa", "d": "2026-10-14", "u": "https://www.cnbcafrica.com/2026/uganda-central-bank-hikes-key-lending-rate-by-225-basis-points"},
  {"o": "Rio Times", "d": "2026-10-14", "u": "https://www.riotimesonline.com/bank-of-uganda-rate-hike-12-2026/"}
 ],
 "inds": ["macro"], "nodes": ["macro/cb", "macro/fx"],
 "vc": [
  {"ind": "macro", "node": "cb", "f": "가격", "dir": "up", "k": "실제", "t": "우간다 기준금리 9.75%에서 12%로 긴급 인상"},
  {"ind": "macro", "node": "fx", "f": "가격", "dir": "up", "k": "실제", "t": "금리 인상 뒤 우간다 실링 이틀째 반등"}
 ],
 "added": "이번 블룸버그 3건·로이터 5건으로 우간다의 기준금리 12% 긴급 인상과 실링 이틀 연속 반등, 남아공 총재의 물가 상방 위험 경고, IMF의 아프리카 물가 경고가 추가됐다",
 "items": [
  I("무디스 '남아공, 신용등급 상향 궤도에 올라'", TB, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/moody-s-says-south-africa-is-on-right-track-for-rating-upgrade",
    "무디스가 남아공이 신용등급 상향으로 가는 올바른 궤도에 있다고 평가하면서, 남아공 국가신용의 개선 가능성이 부각됐다 (제목 기준)"),
  I("우간다 대폭 금리 인상 뒤 실링, 세계 최고 성과 통화로", TB, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/uganda-announces-jumbo-interest-rate-hike-to-defend-shilling",
    "우간다 중앙은행이 기준금리를 9.75%에서 12%로 225bp 올리면서 사상 최저로 밀렸던 실링이 세계에서 가장 많이 오른 통화로 돌아섰다"),
  I("남아공 랜드 소폭 강세…다음 주 중기 예산안에 관심", TR, "2026-10-15", "https://www.reuters.com/world/africa/south-african-rand-edges-up-next-weeks-medium-term-budget-draws-focus-2026-10-15/",
    "남아공 랜드가 소폭 오른 가운데 시장의 관심이 다음 주 중기 예산안으로 옮겨 가면서, 재정 계획이 랜드 방향의 변수가 됐다 (제목 기준)"),
  I("크가냐고 남아공 중앙은행 총재 '물가에 상방 위험'", TR, "2026-10-15", "https://www.reuters.com/world/africa/south-africas-central-bank-governor-kganyago-sees-upside-risks-inflation-2026-10-15/",
    "남아공 중앙은행 크가냐고 총재가 물가에 상방 위험이 있다고 짚으면서, 우간다에 이어 남아공 통화당국도 물가 경계를 드러냈다 (제목 기준)"),
  I("IMF '아프리카 경제 회복력, 커지는 물가 위협·취약한 완충력 가려'", TR, "2026-10-15", "https://www.reuters.com/world/africa/africas-economic-resilience-masks-rising-inflation-threat-fragile-buffers-imf-2026-10-15/",
    "IMF가 아프리카 경제의 회복력 뒤에 커지는 물가 위협과 취약한 완충력이 숨어 있다고 경고하면서, 역내 통화·물가 불안을 짚었다 (제목 기준)"),
  I("아프리카 외환: 케냐·우간다 통화 압박 받아", TR, "2026-10-15", "https://www.reuters.com/world/africa/africa-fx-kenyan-ugandan-currencies-under-strain-2026-10-15/",
    "로이터 주간 아프리카 외환 전망에서 케냐·우간다 통화가 압박을 받는 것으로 나타나면서, 금리 인상 뒤에도 동아프리카 통화 부담이 남았다 (제목 기준)"),
  I("나이지리아 9월 물가 상승률 소폭 둔화", TR, "2026-10-15", "https://www.reuters.com/world/africa/nigerias-inflation-rate-eases-slightly-september-data-shows-2026-10-15/",
    "나이지리아의 9월 물가 상승률이 소폭 낮아지면서, 아프리카 역내 물가 흐름이 나라마다 엇갈렸다 (제목 기준)"),
  I("우간다 실링, 대폭 금리 인상 뒤 이틀째 반등", TB, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/ugandan-shilling-rallies-for-second-day-after-jumbo-rate-hike",
    "우간다의 225bp 금리 인상 뒤 실링이 이틀 연속 오르면서, 중앙은행의 환율 방어 효과가 이어졌다 (제목 기준)"),
 ]})

# G1-034
items.append({
 "cid": "G1-034", "attachTo": "",
 "title": "우크라이나 의회, EU·IMF 자금 풀 법안 통과…해외 소포 부가세 신설",
 "one": "우크라이나 의회가 해외 소포 과세·전자상거래 투명성·정치인 금융감시 법안을 통과시키면서, EU 거시금융지원 2차분 37억 유로와 IMF 3차분 약 7억 달러의 집행 조건 일부를 채워 전시 재정 자금줄이 이어질 전망이다",
 "facts": [
  "무엇이: 우크라이나 의회가 10월 15일 해외 소포 과세, 전자상거래 투명성 강화, 정치인 금융감시 규정 개정 등 EU·IMF 요구 법안 묶음을 통과시켰습니다 [사실]",
  "소포세: 소포 과세 법안은 찬성 252표로 최종 통과했고, 해외 소포에 대한 20% 부가가치세는 2027년 7월 이후 시행됩니다 [사실]",
  "자금: 이 법과 관세법 개정은 IMF 3차분 약 7억 달러와 EU 거시금융지원 2차분 37억 유로를 받는 조건입니다 [사실]",
  "규모: 블룸버그는 이번 법안으로 43억 유로 규모의 EU 자금 트랜치가 풀린다고 전했습니다 [제목]",
  "남은 과제: 총리는 채권단 요구를 다 맞추려면 할 일이 많다고 했고, EU 기준에 맞춘 SEPA 법안은 지지 부족으로 1차 독회 표결에서 빠졌습니다 [사실]"
 ],
 "basis": "partial",
 "check": "법안 통과·표결 수·EU 37억 유로·IMF 약 7억 달러 조건은 검색 결과 요약으로 확인. 블룸버그 제목의 43억 유로 수치는 독립 출처에서 확인 못 함. 돔브로우스키스 발언은 제목 기준",
 "src": [
  {"o": "Kyiv Independent", "d": "2026-10-15", "u": "https://kyivindependent.com/ukrainian-parliament-passes-key-bill-on-international-parcel-taxes/"},
  {"o": "Interfax-Ukraine", "d": "2026-10-15", "u": "https://en.interfax.com.ua/news/economic/1220641.html"},
  {"o": "RBC-Ukraine", "d": "2026-10-15", "u": "https://newsukraine.rbc.ua/news/ukraine-parliament-passes-key-decisions-for-1775585939.html"}
 ],
 "inds": ["macro"], "nodes": ["macro/fiscal"],
 "vc": [
  {"ind": "macro", "node": "fiscal", "f": "공급", "dir": "up", "k": "예상", "t": "법안 통과로 EU·IMF 지원금 집행 길 열려"}
 ],
 "added": "이번 블룸버그·로이터 10월 15일 2건으로 의회의 소포 과세·금융감시 법안 통과와 EU 37억 유로·IMF 약 7억 달러 지원 조건 충족이 추가됐다",
 "items": [
  I("돔브로우스키스 'EU, IMF·G7 회의서 우크라이나 자금 마련 모색'", TR, "2026-10-14", "https://www.reuters.com/world/americas/eu-seeks-raise-cash-ukraine-imf-g7-meetings-dombrovskis-says-2026-10-14/",
    "돔브로우스키스 EU 집행위원이 IMF·G7 회의에서 우크라이나 지원 자금을 더 모으겠다고 밝히면서, 우크라이나 외부 재원 확보가 국제회의 의제에 올랐다 (제목 기준)"),
  I("우크라이나 의회, EU 자금 43억 유로 트랜치 풀 법안 무더기 통과", TB, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/ukraine-s-parliament-passes-new-raft-of-laws-to-unlock-4-3b-tranche-of-eu-funds",
    "우크라이나 의회가 새 법안 묶음을 통과시키면서 43억 유로 규모 EU 자금 트랜치를 받을 길을 열었다 (제목 기준)"),
  I("우크라이나, EU·IMF 수십억 달러 지원 풀 핵심 법안 통과", TR, "2026-10-15", "https://www.reuters.com/world/ukraine-passes-key-laws-help-unlock-billions-aid-eu-imf-2026-10-15/",
    "우크라이나가 해외 소포 과세와 정치인 금융감시 개정 등 핵심 법안을 통과시키면서, IMF 3차분 약 7억 달러와 EU 37억 유로 지원 조건을 채워 나갔다"),
 ]})

# G3-007
items.append({
 "cid": "G3-007", "attachTo": "",
 "title": "페어팩스, 인도 IDBI은행 지분 60.72% 56억 달러에 인수…주가 하락",
 "one": "인도 정부가 IDBI은행 지분 60.72%를 페어팩스에 주당 81루피, 약 56억 달러에 넘기기로 승인하면서 할인된 인수가에 IDBI 주가가 7% 안팎 떨어졌고, 페어팩스는 고디지트·IIFL캐피털을 IDBI은행으로 합칠 계획이다",
 "facts": [
  "무엇이: 인도 내각 경제위원회가 10월 14일 페어팩스의 IDBI은행 지분 60.72% 인수를 승인했고 인수가는 약 5,288억 루피(약 56억 달러)입니다 [사실]",
  "가격: 주당 81루피로 직전 종가 90.44루피보다 약 10% 낮아 IDBI 주가는 장 초반 약 7% 떨어졌습니다 [사실]",
  "지분: 정부 지분은 45.5%에서 15%로, LIC는 49.2%에서 19%로 줄고, 페어팩스 의결권은 26%로 제한되며 15년 안에 지분을 26%로 낮춰야 합니다 [사실]",
  "남은 절차: 구속력 있는 최종 계약은 아직 없고 RBI·SEBI·IRDAI 승인이 필요하며, 페어팩스는 단일 대주주 규정에 맞추려 고디지트·IIFL캐피털을 IDBI은행에 합칠 계획입니다 [사실]",
  "의미: 블룸버그는 이번 지분 매각이 유가 100달러 상황에서 인도 재정에 완충재가 된다고 짚었습니다 [제목]"
 ],
 "basis": "verified",
 "check": "내각 승인, 지분율, 인수가·주가 하락, 지분 제한, 계열사 통합 계획은 검색 결과 요약으로 확인. 유가 100달러 완충 해석은 제목 기준",
 "src": [
  {"o": "The Globe and Mail", "d": "2026-10-15", "u": "https://www.theglobeandmail.com/business/article-fairfax-financial-buys-majority-stake-in-indias-idbi-bank-for-556/"},
  {"o": "Business Standard", "d": "2026-10-15", "u": "https://www.business-standard.com/companies/news/idbi-bank-fairfax-deal-what-rbi-rules-say-on-foreign-ownership-and-control-126101500482_1.html"},
  {"o": "INDmoney", "d": "2026-10-15", "u": "https://www.indmoney.com/blog/stocks/idbi-bank-shares-fall-fairfax-stake-sale"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "banks", "f": "가격", "dir": "down", "k": "실제", "t": "인수가 10% 할인에 IDBI 주가 약 7% 하락"}
 ],
 "added": "이번 로이터 10월 16일 글로 페어팩스가 고디지트 보험·IIFL캐피털 등 인도 금융 계열사를 IDBI은행에 합쳐 단일 대주주 규정에 맞추려는 계획이 추가됐다",
 "items": [
  I("인도 정부, IDBI은행 구조조정 승인", TR, "2026-10-14", "https://www.reuters.com/world/india/indian-government-approves-restructuring-idbi-bank-2026-10-14/",
    "인도 정부가 IDBI은행 구조조정안을 승인하면서, 정부와 LIC가 가진 지분 60.72%를 민간에 넘기는 매각이 본궤도에 올랐다"),
  I("페어팩스의 60억 달러 은행 인수, 인도 자산 향한 열의 보여줘", TB, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/fairfax-s-6-billion-bank-deal-signals-zest-for-indian-assets",
    "페어팩스가 약 60억 달러에 인도 IDBI은행 경영권을 사들이면서, 해외 금융자본의 인도 자산 선호가 드러났다 (제목 기준)"),
  I("IDBI 지분 매각, 유가 100달러 앞 인도에 때맞춘 완충재", TB, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/india-s-idbi-stake-sale-brings-timely-buffer-against-100-oil",
    "인도 정부가 IDBI 지분 매각으로 대규모 매각 대금을 확보하면서, 유가 100달러에 따른 재정 부담을 덜 완충재를 얻었다 (제목 기준)"),
  I("페어팩스 55억 6천만 달러 경영권 인수에 IDBI은행 주가 하락", TR, "2026-10-15", "https://www.reuters.com/world/india/idbi-bank-drops-after-fairfax-buys-controlling-stake-556-billion-2026-10-15/",
    "페어팩스가 IDBI은행 경영권을 55억 6,000만 달러에 사기로 했지만 인수가가 직전 종가보다 약 10% 낮아, IDBI 주가가 장중 약 7% 떨어졌다"),
  I("페어팩스, 인도 금융 계열사들을 IDBI은행에 통합 계획", TR, "2026-10-16", "https://www.reuters.com/world/india/fairfax-plans-fold-indian-financial-holdings-into-idbi-bank-2026-10-15/",
    "페어팩스가 고디지트 보험·IIFL캐피털 등 인도 금융 계열사를 IDBI은행 아래로 합칠 계획을 밝히면서, RBI의 단일 대주주 규정에 맞추려 한다"),
 ]})

# G3-010
items.append({
 "cid": "G3-010", "attachTo": "",
 "title": "블랙록 3분기 순유입 2,050억 달러·운용자산 15.5조 달러…英 운용사도 유입",
 "one": "블랙록이 3분기 ETF 1,350억 달러를 포함한 2,050억 달러 순유입으로 운용자산을 약 15조 5,000억 달러로 늘리고 조정 주당순이익 15.93달러로 예상을 넘었고, 영국 애시모어·주피터도 자금 유입이 늘면서 운용사 수수료 수입이 불어나고 있다",
 "facts": [
  "무엇이: 블랙록의 3분기 말 운용자산은 약 15조 5,000억 달러로 1년 전 13조 5,000억 달러보다 15% 늘었고, 분기 순유입은 2,050억 달러였습니다 [사실]",
  "유입 구성: 장기 순유입 1,750억 달러 중 ETF가 1,350억 달러였고 채권 782억 달러, 주식 524억 달러, 대체 242억 달러, 디지털자산 79억 달러가 들어왔습니다 [사실]",
  "실적: 매출은 19% 늘어 77억 5,000만 달러, 조정 주당순이익은 15.93달러로 시장 예상 14.30달러를 웃돌았습니다 [사실]",
  "영국: 애시모어는 신흥시장 회복력에 회계연도 1분기 유입이 예상을 넘었고, 주피터는 3분기 유입이 늘며 운용자산이 사상 최대를 기록했습니다 [제목]"
 ],
 "basis": "verified",
 "check": "블랙록 운용자산·순유입·유입 구성·매출·주당순이익은 검색 결과 요약으로 확인(채널의 15조 4,900억 달러는 약 15조 5,000억 달러로 확인). 애시모어·주피터는 제목 기준",
 "src": [
  {"o": "Pulse 2.0", "d": "2026-10-14", "u": "https://pulse2.com/blackrock-q3-2026-results/"},
  {"o": "SEC 8-K(블랙록 실적 자료)", "d": "2026-10-14", "u": "https://www.sec.gov/Archives/edgar/data/0002012383/000119312526420979/blk-ex99_2.htm"},
  {"o": "TipRanks", "d": "2026-10-14", "u": "https://www.tipranks.com/news/company-announcements/blackrock-posts-strong-q3-2026-earnings-and-inflows"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "assetmgmt", "f": "수요", "dir": "up", "k": "실제", "t": "블랙록 3분기 순유입 2,050억 달러"}
 ],
 "added": "이번 로이터 10월 15일 글들로 블랙록의 매출 19% 증가·조정 주당순이익 15.93달러와 주피터의 3분기 유입 증가·운용자산 사상 최대가 추가됐다",
 "items": [
  I("애시모어, 신흥시장 회복력에 1분기 자금 유입 예상 웃돌아", TR, "2026-10-14", "https://www.reuters.com/business/finance/uks-ashmore-first-quarter-inflows-beat-expectations-emerging-market-resilience-2026-10-14/",
    "영국 신흥시장 운용사 애시모어의 회계연도 1분기 자금 유입이 예상을 넘으면서, 신흥시장 자산으로 돈이 돌아오고 있음을 보여 줬다 (제목 기준)"),
  I("블랙록 3분기 실적 예상 상회, 운용자산 15조 4,900억 달러 돌파", "텔레그램 미국 주식 인사이더", "2026-10-14", "https://t.me/insidertracking/66217",
    "블랙록이 3분기 시장 예상을 웃도는 실적을 내고 운용자산이 15조 4,900억 달러를 넘어서면서, ETF로 자금이 빠르게 몰리고 있음을 보여 줬다"),
  I("블랙록 순이익 급증…견조한 시장이 수수료 끌어올려", TR, "2026-10-15", "https://www.reuters.com/business/blackrock-profit-jumps-resilient-markets-boost-fees-2026-10-14/",
    "견조한 시장 덕에 운용 수수료가 불어나면서 블랙록의 3분기 매출이 19% 늘고 조정 주당순이익이 15.93달러로 예상을 넘었다"),
  I("주피터, 3분기 자금 유입 늘고 운용자산 사상 최대", TR, "2026-10-15", "https://www.reuters.com/business/jupiter-fund-management-reports-higher-third-quarter-inflows-assets-hit-record-2026-10-15/",
    "영국 주피터 펀드매니지먼트의 3분기 자금 유입이 늘고 운용자산이 사상 최대를 기록하면서, 영국 운용사로도 돈이 들어오고 있다 (제목 기준)"),
 ]})

# G3-020
items.append({
 "cid": "G3-020", "attachTo": "",
 "title": "홍콩, IPO 조작 의혹 바이차 거래정지·자산 동결…美 펌프앤덤프 단속도",
 "one": "홍콩 증권선물위원회가 IPO 수요 부풀리기 의혹으로 차판다 운영사 바이차바이다오 거래를 멈추고 브로커 6곳의 고객자산 최대 약 44억 홍콩달러를 묶은 데 이어 미국도 해외 소형주 펌프앤덤프 단속에 나서면서, 소형 IPO에 대한 규제가 양쪽 시장에서 조여지고 있다",
 "facts": [
  "무엇이: 홍콩 SFC가 10월 13일 오전 9시부터 차판다 운영사 쓰촨 바이차바이다오(2555)의 거래를 정지시켰고, IPO가 수요를 부풀리도록 조작됐을 수 있다는 심각한 우려를 이유로 들었습니다 [사실]",
  "동결: SFC는 쑨란과 관련 회사 8곳이 얽힌 조직과 관련해 브로커 6곳에 최대 43억 7,946만 홍콩달러의 고객자산 처분을 제한했고, 이 조직은 클라우드브레이크 파마와 바이차 IPO에 연루된 혐의를 받습니다 [사실]",
  "수법: SFC는 미공개 약정으로 IPO 조달금 일부가 신규 상장사 밖으로 빠져나갔을 수 있다고 봤고, 또 다른 조직은 톈쥐디허 상장과 관련돼 있습니다 [사실]",
  "바이차: 바이차는 2024년 4월 상장 첫날 27% 떨어진 뒤 공모가를 넘은 적이 없고, 회사는 사업이 정상 운영 중이며 조사에 협조한다고 밝혔습니다 [사실]",
  "미국: 해외를 겨냥한 미국의 펌프앤덤프 단속은 미국 내 반발에 부딪혔습니다 [제목]"
 ],
 "basis": "verified",
 "check": "바이차 거래정지·자산 동결 규모·연루 IPO는 검색 결과 요약으로 확인. 미국 펌프앤덤프 단속과 홍콩 IPO 위험 신호 기사는 제목 기준",
 "src": [
  {"o": "The Standard", "d": "2026-10-14", "u": "https://www.thestandard.com.hk/finance/article/345349/HKs-SFC-cracks-down-on-suspected-IPO-rigging-syndicates-with-46b-frozen-after-ChaPanda-trading-halt"},
  {"o": "Dimsum Daily", "d": "2026-10-13", "u": "https://www.dimsumdaily.hk/sfc-suspends-baicha-trading-as-probe-targets-suspected-ipo%E2%80%91rigging-syndicates/"},
  {"o": "China Daily HK", "d": "2026-10-13", "u": "https://www.chinadailyhk.com/hk/article/641028"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "regulation", "f": "-", "dir": "flat", "k": "실제", "t": "IPO 조작 단속은 수급보다 규제 강화 신호"}
 ],
 "added": "이번 로이터·블룸버그 10월 15일 글로 바이차의 거래정지 공시와 해외 소형주를 겨냥한 미국 펌프앤덤프 단속에 대한 미국 내 반발이 추가됐다",
 "items": [
  I("홍콩 IPO 위험 신호…갑작스러운 대출·비밀 약정", TB, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/hong-kong-ipo-red-flags-include-sudden-loans-secret-handshakes",
    "블룸버그가 홍콩 IPO 조작의 위험 신호로 상장 무렵의 갑작스러운 대출과 비밀 약정을 꼽으면서, 소형 상장 심사의 허점이 부각됐다 (제목 기준)"),
  I("바이차바이다오, 홍콩 당국의 IPO 조작 관련 거래정지 공시", TR, "2026-10-15", "https://www.reuters.com/legal/government/baicha-baidao-notes-hong-kong-regulators-trading-suspension-over-ipo-rigging-2026-10-14/",
    "차판다 운영사 바이차바이다오가 홍콩 SFC의 IPO 조작 의혹에 따른 거래정지를 공시하면서, 조사 협조와 사업 정상 운영을 함께 밝혔다"),
  I("해외 겨냥한 美 펌프앤덤프 단속, 국내 반발에 직면", TB, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/us-pump-and-dump-crackdown-aimed-abroad-meets-homegrown-protests",
    "미국 당국이 해외 소형주를 겨냥한 펌프앤덤프 단속을 벌이자 미국 안에서 반발이 나오면서, 단속 범위를 둘러싼 갈등이 생겼다 (제목 기준)"),
 ]})

# G3-029
items.append({
 "cid": "G3-029", "attachTo": "",
 "title": "이글힐스, 시리아에 최대 170억 달러 개발 계획…두바이는 14억 달러 금융지구",
 "one": "UAE 개발사 이글힐스의 알아바르 회장이 다마스쿠스·라타키아 두 개발사업에 최대 170억 달러를 넣겠다고 밝히고 두바이도 14억 달러 규모 새 금융지구 개발에 나서면서, 걸프 자본이 역내 대형 부동산 개발 물량을 늘리고 있다",
 "facts": [
  "무엇이: 이글힐스의 무함마드 알아바르 회장이 10월 14일 시리아에 160억~170억 달러를 투자할 계획이라고 밝혔고, 이는 서명된 계약 금액이 아닌 계획입니다 [사실]",
  "사업: 다마스쿠스의 타다문 타워 개발과 라타키아의 마리나를 낀 주거·관광 사업 에코 라이프 두 곳이며, 10월 5일 알샤라 대통령이 참석한 가운데 기본협약을 맺었습니다 [사실]",
  "규모: 두 사업은 4만 개 넘는 일자리를 만들 것으로 예상되지만, 당국은 사업 금액과 완공 시점을 밝히지 않았습니다 [사실]",
  "두바이: 두바이는 14억 달러를 들인 새 지구로 금융센터를 키웁니다 [제목]"
 ],
 "basis": "partial",
 "check": "이글힐스 투자 계획·사업 내용·협약 시점은 검색 결과 요약으로 확인. 두바이 14억 달러 금융지구는 확인 못 함(제목 기준)",
 "src": [
  {"o": "The National", "d": "2026-10-05", "u": "https://www.thenationalnews.com/business/property/2026/10/05/abu-dhabis-eagle-hills-to-develop-residential-and-tourism-projects-in-syria/"},
  {"o": "AGBI", "d": "2026-10", "u": "https://www.agbi.com/real-estate/2026/10/eagle-hills-to-start-work-on-two-projects-in-syria/"},
  {"o": "LBCI", "d": "2026-10-14", "u": "https://www.lbcgroup.tv/news/middleeastnews/962809/eagle-hills-plans-up-to-17-billion-investment-in-syria-chairman-says/en"}
 ],
 "inds": ["realestate"], "nodes": [],
 "vc": [
  {"ind": "realestate", "node": "develop", "f": "공급", "dir": "up", "k": "예상", "t": "이글힐스 시리아 개발 최대 170억 달러 계획"}
 ],
 "added": "이번 블룸버그 10월 15일 글로 두바이가 14억 달러 규모 새 지구를 지어 금융센터를 키운다는 계획이 추가됐다 (제목 기준)",
 "items": [
  I("이글힐스 회장 '시리아에 최대 170억 달러 투자 계획'", TR, "2026-10-14", "https://www.reuters.com/world/middle-east/eagle-hills-plans-up-17-billion-investment-syria-chairman-says-2026-10-14/",
    "이글힐스 알아바르 회장이 시리아 다마스쿠스·라타키아 개발에 최대 170억 달러를 넣겠다고 밝히면서, 전후 시리아 재건에 걸프 부동산 자본이 들어가게 됐다"),
  I("두바이, 14억 달러 새 지구로 금융센터 확장", TB, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/dubai-builds-up-financial-center-with-new-1-4-billion-district",
    "두바이가 14억 달러 규모 새 지구를 지어 금융센터를 키우기로 하면서, 금융권 업무 공간 공급이 늘어날 전망이다 (제목 기준)"),
 ]})

# G3-048
items.append({
 "cid": "G3-048", "attachTo": "",
 "title": "노르웨이 국부펀드 윤리 규정 대수술 권고…윤리위 투자배제 권한 없애",
 "one": "노르웨이 정부위원회가 미국의 캐터필러 매각 항의 뒤 국부펀드 윤리 규정 개편안을 내고 윤리위원회의 투자배제 권고 권한을 없애자고 하면서, 핵무기 배제가 풀리면 방산기업에 수백억 달러가 투자될 수 있다",
 "facts": [
  "무엇이: 노르웨이 국부펀드 윤리 규정을 검토한 위원회가 10월 15일 보고서에서 대대적인 개편을 권고했고, 정부는 2027년 봄 백서에서 자체안을 낼 예정입니다 [사실]",
  "배경: 트럼프 행정부가 가자지구·서안에서 쓰인 불도저를 이유로 한 국부펀드의 캐터필러 지분 매각에 항의한 뒤 윤리 규정 적용이 멈췄고, 정부는 미국을 의식한 조치라는 해석을 부인했습니다 [사실]",
  "윤리위: 윤리위원회는 위험 평가 역할은 유지하지만 투자배제 권고 권한을 잃고 노르웨이 중앙은행 투자관리(NBIM)가 대응을 정하며, 보고서도 자동 공개되지 않습니다 [사실]",
  "방산: 핵무기 배제 기준이 바뀌면 방산기업에 수백억 달러가 투자될 수 있지만, 노르웨이 적십자와 국제앰네스티는 반대하고 있습니다 [사실]"
 ],
 "basis": "verified",
 "check": "위원회 보고서 공개일, 윤리위 권한 변경, 캐터필러 배경, 핵무기 배제 변경 영향은 검색 결과 요약으로 확인",
 "src": [
  {"o": "Amnesty International", "d": "2026-10-15", "u": "https://www.amnesty.org/en/latest/news/2026/10/norway-investment-fund-human-rights-safeguards-weakened/"},
  {"o": "ArcticToday", "d": "2026-10-15", "u": "https://www.arctictoday.com/norways-sovereign-wealth-fund-should-invest-in-major-defence-groups-commission-concludes/"},
  {"o": "MyJoyOnline", "d": "2026-10-15", "u": "https://www.myjoyonline.com/norways-wealth-fund-set-to-overhaul-ethical-rules-after-us-scrutiny/"}
 ],
 "inds": ["fin", "aero"], "nodes": [],
 "vc": [
  {"ind": "aero", "node": "defspend", "f": "수요", "dir": "up", "k": "예상", "t": "핵무기 배제 해제 시 방산주에 수백억 달러 투자 가능"}
 ],
 "items": [
  I("노르웨이 국부펀드, 미국 압박 뒤 윤리 규정 대폭 개편 예정", TR, "2026-10-15", "https://www.reuters.com/legal/government/norways-wealth-fund-set-overhaul-ethical-rules-after-us-scrutiny-2026-10-15/"),
 ]})

# G4-005
items.append({
 "cid": "G4-005", "attachTo": "",
 "title": "코어위브 신용불안에 젠슨 황 '지원 필요 없다'…채권·주가 반등",
 "one": "코어위브가 520억 달러 부채·리스 부담 속에 주가 15% 급락과 채권 부실화 우려를 겪자 엔비디아 젠슨 황 CEO가 재무가 나아지고 있어 지원이 필요 없다고 밝히면서, 2031년물 채권이 80센트대로 반등하고 신용 스프레드가 좁혀졌다",
 "facts": [
  "무엇이: 코어위브 주가가 10월 14일 15% 급락했고 2032년 만기 무담보채가 액면 1달러당 80센트 아래, 수익률 15% 이상에서 거래되며 약 520억 달러 부채·리스 의무가 부각됐습니다 [채널]",
  "황 발언: 젠슨 황 엔비디아 CEO는 10월 15일 스톡홀름에서 코어위브가 재무적으로 강해지고 있고 자본비용도 내려가고 있어 엔비디아가 뒷받침할 필요가 없다고 말했습니다 [사실]",
  "반등: 발언 뒤 2031년 10월물은 달러당 81~83센트, 2030년 6월물은 87~91센트로 올랐지만 모두 액면가를 밑돌았고, 5년물 CDS는 1,100~1,190bp대로 사상 최고권이었습니다 [사실]",
  "엮임: 엔비디아는 코어위브의 주주이자 GPU 공급사이며 2032년 4월까지 코어위브의 팔리지 않은 컴퓨팅 용량을 사들일 의무가 있어 구제 압박 논란이 일었습니다 [사실]",
  "반론: 인트레이터 CEO는 약 1,040억 달러 수주잔고가 부채 상환 의무를 충분히 뒷받침한다고 주장했습니다 [채널]"
 ],
 "basis": "verified",
 "check": "황 발언, 채권 반등 폭, CDS, 엔비디아 미판매 용량 구매 의무는 검색 결과 요약으로 확인(출처별 채권·CDS 수치가 달라 범위로 씀). 520억 달러 부채·1,040억 달러 수주잔고·파산 확률 17%는 채널 전언",
 "src": [
  {"o": "Benzinga", "d": "2026-10-15", "u": "https://www.benzinga.com/trading-ideas/movers/26/10/62396966/coreweave-stock-snaps-back-as-nvidia-ceo-signals-support"},
  {"o": "TheNextWeb", "d": "2026-10-15", "u": "https://thenextweb.com/news/huang-coreweave-backstop-stockholm"},
  {"o": "TradingKey", "d": "2026-10-15", "u": "https://www.tradingkey.com/analysis/stocks/us-stocks/262219232-coreweave-stock-credit-risk-cds-bond-yield-deutsche-bank-buy-nvidia-jensen-huang-tradingkey"}
 ],
 "inds": ["macro", "tech"], "nodes": ["macro/semis"],
 "vc": [
  {"ind": "tech", "node": "cloud", "f": "가격", "dir": "mixed", "k": "실제", "t": "주가 15% 급락 뒤 황 발언에 채권·주가 반등"},
  {"ind": "macro", "node": "semis", "f": "수요", "dir": "down", "k": "예상", "t": "코어위브 유동성 악화 시 GPU 구매 수요 타격 우려"}
 ],
 "added": "이번 10월 16일 블룸버그·로이터·텔레그램 글로 젠슨 황의 지원 불필요 발언 뒤 31년물 스프레드가 970bp로 줄고 주가가 반등했으며, 도이체방크의 긍정 평가와 대주단 노출 해설이 추가됐다",
 "items": [
  I("코어위브 '시장이 비이성적으로 반응'…사업모델 고수", TB, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-14/coreweave-s-ceo-blames-rout-on-market-acting-irrationally",
    "코어위브가 주가 급락을 두고 시장이 비이성적으로 움직인다며 기존 사업모델을 고수하겠다고 밝히면서, 회사와 시장의 신용 판단이 엇갈렸다 (제목 기준)"),
  I("QTR '코어위브 흔들리면 엔비디아 구제 압박 받을 수도'", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66263",
    "QTR 리서치가 엔비디아의 20억 달러 추가 투자와 63억 달러 미판매 용량 구매 약정을 들어, 코어위브 유동성이 악화되면 엔비디아가 구제 압박을 받을 수 있다고 경고했다"),
  I("코어위브 CEO, 메모로 탄탄한 수주잔고 강조하며 직원 안심시켜", TR, "2026-10-15", "https://www.reuters.com/business/coreweave-ceo-notes-strong-backlog-memo-reassure-staff-over-market-scrutiny-2026-10-14/",
    "코어위브 인트레이터 CEO가 직원 메모에서 탄탄한 수주잔고를 강조하면서, 시장의 신용 우려 속에 내부 동요를 막으려 했다 (제목 기준)"),
  I("코어위브 주가 15% 폭락, 채권은 부실채권 수준으로", "텔레그램 하나증권 중국전략", "2026-10-15", "https://t.me/HANAchina/70438",
    "코어위브가 약 9% 금리로 조달해 5%도 안 되는 투자수익을 낸다는 지적 속에 주가가 15% 폭락하면서, 예측시장의 2027년 전 파산 확률이 17%에 이르렀다"),
  I("엔비디아의 코어위브 딜레마: 구제냐 방치냐", "텔레그램 하나증권 중국전략", "2026-10-15", "https://t.me/HANAchina/70446",
    "엔비디아가 코어위브를 도우면 최종 보증자 기대가 굳어지고 방치하면 GPU 수요와 지분 가치가 함께 깎이는 딜레마에 놓였다는 분석이 나왔다"),
  I("코어위브 채권 급반등…31년물 82.8센트·30년물 91.3센트", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66367",
    "매도세 뒤 매수세가 돌아오면서 코어위브 2031년 10월물이 82.8센트, 2030년 6월물이 91.3센트로 올라 신용 압박이 다소 누그러졌다"),
  I("엔비디아 CEO, 코어위브 우려 일축…주가 떠받쳐", TB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/nvidia-ceo-huang-says-coreweave-improving-no-backstop-needed",
    "젠슨 황 엔비디아 CEO가 코어위브 재무가 나아지고 있어 뒷받침이 필요 없다고 하면서, 장 초반 9.5% 빠졌던 코어위브 주가가 반등했다"),
  I("젠슨 황 발언 뒤 코어위브 31년물 스프레드 1,122→970bp", "텔레그램 나쁜양파", "2026-10-16", "https://t.me/Badonions/7849",
    "젠슨 황 발언 이후 코어위브 31년물 스프레드가 1,122bp에서 970bp로 줄고 주가가 61.3달러에서 63.6달러로 오르면서, 주식과 채권이 함께 회복했다"),
  I("도이체방크 '코어위브 매도세는 매수 기회'", TB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/coreweave-s-selloff-is-buying-opportunity-deutsche-bank-says",
    "도이체방크가 코어위브 주가 급락을 긍정적으로 평가하면서, 신용 불안 속에서도 증권사들의 시각이 엇갈리기 시작했다"),
  I("코어위브의 AI 계약과 증설 자금을 댄 대주단", TR, "2026-10-16", "https://www.reuters.com/legal/transactional/coreweaves-ai-contracts-lenders-financing-its-build-out-2026-10-15/",
    "코어위브의 AI 고객 계약과 증설 자금을 댄 대주단이 함께 조명되면서, 코어위브 신용 불안이 대출 기관 노출 문제로 번졌다 (제목 기준)"),
  I("코어위브의 곤경이 AI 붐을 흔드는 이유", TR, "2026-10-16", "https://www.reuters.com/legal/transactional/why-coreweaves-troubles-are-rattling-ai-boom-2026-10-15/",
    "코어위브의 재무 곤경이 왜 AI 붐 전체를 흔드는지 짚은 해설이 나오면서, 한 기업의 신용 문제가 AI 업계 전반의 우려로 번졌다 (제목 기준)"),
 ]})

# G4-012
items.append({
 "cid": "G4-012", "attachTo": "n-rtr-0023",
 "title": "美 8개 주 오픈AI 제소·FTC 오픈AI·앤트로픽 조사…AI 규제 압박 확대",
 "one": "백악관의 AI 사고 보고 의무화와 오픈AI 아동정보 집단소송에 이어 미국 8개 주가 챗GPT의 아동 피해를 들어 오픈AI를 제소하고 FTC가 오픈AI·앤트로픽에 보안 사고·안전장치 자료를 요구하면서, AI 기업의 소송·규제 부담이 주와 연방 양쪽에서 커지고 있다",
 "facts": [
  "무엇이: 아칸소·애리조나·아이오와·아이다호·캔자스·몬태나·네브래스카·웨스트버지니아 8개 주가 10월 14일 챗GPT가 아동에게 해롭고 안전성을 허위로 설명했다며 각 주 법원에 오픈AI를 제소했습니다 [사실]",
  "요구: 주들은 이익 환수, 제품 변경, 벌금과 피해 배상을 요구했고, 오픈AI는 다른 AI 제품에 없는 연령별 보호 장치를 갖췄다고 반박했습니다 [사실]",
  "FTC: FTC는 오픈AI와 앤트로픽에 보안 사고·안전장치·마케팅 자료·개인정보 정책에 관한 각 50쪽 넘는 민사조사 요구서를 보냈고, 다른 AI 조직에도 뒤따를 예정입니다 [사실]",
  "기존: 백악관은 프런티어 AI 기업에 보안 사고 보고를 의무화했고, 10월 13일에는 오픈AI가 미성년자 데이터 무단 수집으로 집단소송을 당했습니다 [사실]",
  "그 밖: 미국 주들은 캐릭터AI 파산 절차에서 아동 데이터 보호를 요구했고, 오픈AI·메타는 미국 사법부에 딥페이크 증거 위험을 경고했습니다 [제목]"
 ],
 "basis": "verified",
 "check": "8개 주 제소와 요구 내용, 오픈AI 반박, FTC 민사조사 요구서 범위는 검색 결과 요약으로 확인. 캐릭터AI 파산 절차·딥페이크 증거 경고는 제목 기준",
 "src": [
  {"o": "CNBC", "d": "2026-10-14", "u": "https://www.cnbc.com/2026/10/14/openai-sued-by-8-states-over-chatgpt-safety-concerns-.html"},
  {"o": "Fortune", "d": "2026-10-15", "u": "https://fortune.com/2026/10/15/eight-states-sue-openai-saying-chatgpt-hurt-kids-and-lied-to-adults/"},
  {"o": "Runtime Wire", "d": "2026-10-15", "u": "https://runtimewire.com/article/ftc-anthropic-openai-ai-safety-investigation"}
 ],
 "inds": ["tech"], "nodes": [],
 "vc": [
  {"ind": "tech", "node": "ai", "f": "-", "dir": "flat", "k": "실제", "t": "8개 주 소송과 FTC 조사로 규제 부담 확대"}
 ],
 "added": "이번 텔레그램 2건·로이터 4건으로 미국 8개 주의 오픈AI 제소와 FTC의 오픈AI·앤트로픽 민사조사 요구서 발부, 캐릭터AI 파산 절차의 아동 데이터 보호 요구가 추가됐다",
 "items": [
  I("美 8개 주 법무장관 '챗GPT가 청소년 자해 조장' 오픈AI 제소", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66301",
    "미국 8개 주 법무장관이 오픈AI가 챗GPT 안전성을 허위로 설명하고 보호 장치 없이 출시를 서둘렀다며 제소하면서, 안전 운영 변경과 피해 배상을 요구했다"),
  I("美 주들, 캐릭터AI 파산 절차서 아동 데이터 보호 요구", TR, "2026-10-15", "https://www.reuters.com/business/us-states-seek-childrens-data-protections-characterai-bankruptcy-2026-10-14/",
    "미국 주들이 캐릭터AI 파산 절차에서 아동 데이터 보호를 요구하면서, 파산한 AI 기업이 가진 이용자 데이터 처리가 쟁점이 됐다 (제목 기준)"),
  I("美 8개 주, '챗GPT가 아동에 해롭다'며 오픈AI 제소", TR, "2026-10-15", "https://www.reuters.com/world/eight-us-states-sue-openai-claiming-chatgpt-harms-children-2026-10-14/",
    "미국 8개 주가 각 주 법원에 챗GPT가 아동에게 해롭다며 오픈AI를 제소하면서, 이익 환수와 제품 변경, 벌금 부과를 요구했다"),
  I("악시오스 'FTC, 앤트로픽·오픈AI에 민사조사 요구서 발부'", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66355",
    "FTC가 앤트로픽과 오픈AI에 민사조사 요구서를 보내 관련 문서 확보에 나서면서, 연방 당국의 AI 기업 조사가 본격화했다"),
  I("악시오스 'FTC, 소비자 피해 놓고 오픈AI·앤트로픽 소환'", TR, "2026-10-15", "https://www.reuters.com/business/us-ftc-subpoenas-openai-anthropic-over-consumer-harms-axios-reports-2026-10-15/",
    "FTC가 소비자 피해 여부를 따지려 오픈AI·앤트로픽에 보안 사고와 안전장치, 마케팅 자료를 요구하면서, 다른 AI 조직에도 요구서가 뒤따를 예정이다"),
  I("오픈AI·메타, 美 사법부에 딥페이크 증거 위험 경고", TR, "2026-10-16", "https://www.reuters.com/legal/government/openai-meta-caution-us-judiciary-about-risk-deepfake-evidence-2026-10-15/",
    "오픈AI와 메타가 미국 사법부에 딥페이크 증거의 위험을 경고하면서, AI가 만든 증거를 법정에서 어떻게 다룰지가 과제로 떠올랐다 (제목 기준)"),
 ]})

# G4-037
items.append({
 "cid": "G4-037", "attachTo": "",
 "title": "췌장암 RAS 표적약 진전…다락손라십 EU 승인 권고, 버라스템 반응률 50%",
 "one": "EMA의 CHMP가 레볼루션 메디슨의 다락손라십을 기존 치료 뒤 전이성 췌장암 단독요법으로 승인 권고하고 버라스템의 KRAS G12D 억제제 VS-7375가 2차 췌장암에서 반응률 50%를 내면서, 췌장암 RAS 표적치료 경쟁이 커질 전망이다",
 "facts": [
  "무엇이: EMA 약물사용자문위원회(CHMP)가 10월 15일 레볼루션 메디슨의 다락손라십(제품명 라손크)을 전신치료 경험이 있는 성인 전이성 췌장선암 단독요법으로 EU 판매 승인하라고 권고했습니다 [사실]",
  "근거: 3상 RASolute 302에서 전체생존기간 중앙값은 13.2개월로 항암화학요법 6.7개월보다 길었고(위험비 0.40), 미 FDA는 8월 26일 이미 승인했습니다 [사실]",
  "버라스템: VS-7375는 900mg 단독요법에서 2차 이상 환자 22명의 확정 반응률 41%, 2차 췌장암 8명에서 50%를 보였습니다 [사실]",
  "버라스템 자금: 2억 5,000만 달러 투자 유치와 CEO 사임 소식이 함께 전해졌습니다 [채널]",
  "레볼루션: 유럽 승인 추진은 레볼루션이 이 항암제를 단독 출시하려는 의지를 보여 준다는 분석이 나왔습니다 [제목]"
 ],
 "basis": "partial",
 "check": "CHMP 승인 권고와 3상 수치, FDA 승인일, VS-7375 반응률은 검색 결과 요약으로 확인. 버라스템 2억 5,000만 달러 조달과 CEO 사임은 확인 못 함(채널 전언). 단독 출시 해석은 제목 기준",
 "src": [
  {"o": "GlobeNewswire(레볼루션 메디슨 보도자료)", "d": "2026-10-15", "u": "https://www.globenewswire.com/news-release/2026/10/15/3381786/0/en/revolution-medicines-rasonque-daraxonrasib-receives-positive-chmp-opinion-recommending-marketing-authorization-in-european-union-for-metastatic-pancreatic-cancer.html"},
  {"o": "OncLive", "d": "2026-10-15", "u": "https://www.onclive.com/view/chmp-recommends-approval-of-daraxonrasib-for-previously-treated-metastatic-pancreatic-cancer"},
  {"o": "OncLive", "d": "2026-10", "u": "https://www.onclive.com/view/vs-7375-elicits-responses-in-kras-g12d-mutated-pancreatic-cancer"}
 ],
 "inds": ["pharma"], "nodes": [],
 "vc": [
  {"ind": "pharma", "node": "regulatory", "f": "공급", "dir": "up", "k": "예상", "t": "다락손라십 EU 승인 권고로 유럽 출시 앞둬"}
 ],
 "added": "이번 로이터 10월 16일 글로 레볼루션 메디슨이 유럽 승인을 직접 밀어붙이며 다락손라십을 단독 출시하려 한다는 해석이 추가됐다 (제목 기준)",
 "items": [
  I("버라스템 VS-7375, 2차 췌장암 반응률 50%…2억 5천만 달러 조달", "텔레그램 트릴리온", "2026-10-14", "https://t.me/Trillion_labs/10476",
    "버라스템의 KRAS G12D 억제제 VS-7375가 2차 췌관선암에서 반응률 50%와 완전관해 2건을 내는 가운데, 회사는 2억 5,000만 달러를 조달하고 CEO가 물러났다"),
  I("EMA, 레볼루션 췌장암 신약 승인 권고", TR, "2026-10-15", "https://www.reuters.com/business/healthcare-pharmaceuticals/ema-recommends-approval-revolutions-pancreatic-cancer-drug-2026-10-15/",
    "EMA가 레볼루션 메디슨의 다락손라십을 기존 치료 뒤 전이성 췌장암 치료제로 승인 권고하면서, 유럽연합 집행위원회의 최종 결정만 남았다"),
  I("레볼루션 메디슨의 유럽 행보, 항암제 단독 출시 야심 시사", TR, "2026-10-16", "https://www.reuters.com/legal/litigation/revolution-medicines-europe-efforts-signal-solo-launch-ambitions-cancer-drug-2026-10-15/",
    "레볼루션 메디슨이 유럽 승인을 스스로 밀어붙이면서, 협력사 없이 췌장암 신약을 단독으로 출시하려는 의지가 드러났다 (제목 기준)"),
 ]})

# G4-051
items.append({
 "cid": "G4-051", "attachTo": "",
 "title": "에릭슨, 네트워크 수요에 3분기 이익 예상 상회…주가 최대 11% 급등",
 "one": "에릭슨이 3분기 매출 595억 크로나(유기 성장 7%)와 조정 EBITA 101억 크로나로 예상치 79억 3,000만 크로나를 웃돌고 네트워크 부문 이익이 90억 크로나로 늘면서 주가가 최대 11% 올랐지만, 부품 비용 상승이 마진을 압박할 전망이다",
 "facts": [
  "무엇이: 에릭슨의 3분기 조정 EBITA는 101억 크로나(마진 17.0%)로 블룸버그 집계 예상치 79억 3,000만 크로나를 웃돌았고, 전년 76억 크로나 매각 차익을 빼면 늘었습니다 [사실]",
  "매출: 순매출은 595억 크로나로 6% 늘었고 유기 성장률은 7%였습니다 [사실]",
  "부문: 네트워크 부문 조정 EBITA는 72억에서 90억 크로나로 늘어 마진 23.1%였고, 기업 부문은 아이코넥티브 매각 여파로 5억 크로나 적자였습니다 [사실]",
  "위험: 경영진은 부품 비용이 올라 마진을 계속 압박할 것이라고 경고했고, 인수·매각 전 잉여현금흐름은 26% 줄어 약 49억 크로나였습니다 [사실]"
 ],
 "basis": "verified",
 "check": "조정 EBITA·매출·부문 이익·주가 상승 폭·부품 비용 경고는 검색 결과 요약(에릭슨 보도자료 포함)으로 확인",
 "src": [
  {"o": "에릭슨 보도자료", "d": "2026-10-15", "u": "https://www.ericsson.com/en/press-releases/2026/10/ericsson-reports-third-quarter-results-2026"},
  {"o": "Quartz", "d": "2026-10-15", "u": "https://qz.com/ericsson-stock-earnings-beat-network-demand-101526"}
 ],
 "inds": ["tech"], "nodes": [],
 "vc": [
  {"ind": "tech", "node": "telecom", "f": "수요", "dir": "up", "k": "실제", "t": "모바일 네트워크 장비 수요로 네트워크 이익 증가"}
 ],
 "added": "이번 블룸버그·로이터 2건으로 네트워크 수요에 따른 3분기 이익 예상 상회와 전년 매각 차익을 뺀 조정 EBITA 증가, 주가 최대 11% 급등이 추가됐다",
 "items": [
  I("모바일 네트워크 수요가 이익 끌어올려…에릭슨 주가 급등", TB, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/ericsson-earnings-beat-forecast-on-solid-mobile-network-demand",
    "모바일 네트워크 장비 수요가 3분기 이익을 끌어올리면서 에릭슨 주가가 스톡홀름에서 장중 최대 11% 뛰었다"),
  I("에릭슨 3분기 핵심이익, 예상보다 덜 줄어", TR, "2026-10-15", "https://www.reuters.com/business/ericssons-third-quarter-core-profit-falls-less-than-expected-2026-10-15/",
    "에릭슨의 3분기 조정 EBITA가 전년 매각 차익 효과로 101억 크로나로 줄었지만 감소 폭이 예상보다 작아, 네트워크 본업의 이익 개선이 드러났다"),
 ]})

# G4-064
items.append({
 "cid": "G4-064", "attachTo": "",
 "title": "애플, 택션 특허 57억 달러 배상 평결 파기·재심 요청",
 "one": "애플이 탭틱 엔진 특허 침해로 택션에 57억 달러를 물라는 배심 평결에 대해 손해액이 추측에 근거했다며 파기나 재심을 요청하면서, 기록적 특허 배상금의 확정 여부가 법원 판단에 달리게 됐다",
 "facts": [
  "무엇이: 애플이 10월 13일(미국 시간) 남부 캘리포니아 연방법원에 택션 테크놀로지 특허 소송의 57억 달러 배상 평결을 뒤집거나 재심을 열어 달라고 요청했습니다 [사실]",
  "배경: 배심은 9월 25일 애플이 탭틱 엔진 관련 택션 특허 2건을 침해했다고 봤지만 고의 침해는 인정하지 않았습니다 [사실]",
  "논리: 애플은 택션이 특허 기술의 가치를 입증하지 못했고 손해 산정 전문가도 재판 전 배제됐다며 배상액이 추측에 기댔다고 주장했습니다 [사실]",
  "상태: 판사는 아직 평결 파기나 재심 여부를 결정하지 않았습니다 [사실]"
 ],
 "basis": "verified",
 "check": "배상액 57억 달러, 요청 내용, 평결일·고의성 판단, 미결 상태는 검색 결과 요약으로 확인",
 "src": [
  {"o": "9to5Mac", "d": "2026-10-13", "u": "https://9to5mac.com/2026/10/13/apple-challenges-tactions-5-7b-patent-verdict-says-damages-were-based-on-guesswork/"},
  {"o": "PYMNTS", "d": "2026-10-14", "u": "https://www.pymnts.com/cpi-posts/apple-seeks-to-overturn-record-5-7-billion-patent-verdict/"}
 ],
 "inds": ["tech"], "nodes": [],
 "vc": [
  {"ind": "tech", "node": "devices", "f": "-", "dir": "flat", "k": "예상", "t": "특허 배상 다툼은 수급보다 법적 비용 문제"}
 ],
 "items": [
  I("애플, 美 법원에 57억 달러 기록적 특허 배상 평결 파기 요청", TR, "2026-10-15", "https://www.reuters.com/legal/litigation/apple-asks-us-court-overturn-landmark-57-billion-patent-verdict-2026-10-14/"),
 ]})

out = {"agent": "W6", "searches_used": 16, "fetches_used": 0, "items": items,
       "skipped": [
         {"cid": "G2-016", "reason": "AI 투자 증액"},
         {"cid": "G3-032", "reason": "이미 다룸(n-bbg-0205)"}
       ]}
json.dump(out, open("/home/user/news-desk/data/mix-2026-10-15/out2/W6.json", "w"), ensure_ascii=False, indent=1)
print("ok")
