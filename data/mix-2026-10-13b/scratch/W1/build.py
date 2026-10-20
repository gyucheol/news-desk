import json, re, sys

OUT = '/home/user/news-desk/data/mix-2026-10-13b/out2/W1.json'
TP = '텔레그램 '
def it(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s: x["s"] = s
    return x

B = []

B.append({"cid": "C002", "attachTo": "n-tg-0157",
 "title": "{{이란 봉쇄 걸프 전역 확대}} 경고…VLCC 1항차 8천만 달러, 日 {{운송비 지원}}",
 "one": "{{이란 혁명수비대}}가 봉쇄 대상을 호르무즈 너머 걸프 전역으로 넓히고 미군도 봉쇄 돌파 화물선을 타격하는 가운데 선박 피격이 이어지면서, 미 걸프-중국 {{VLCC 1항차 운임}}이 약 8천만 달러로 치솟아 {{일본 정부}}가 우회 수입 운송비 지원에 나섰다",
 "facts": [
  "무엇이: 혁명수비대는 10월 9~10일 허가받지 않은 선박을 호르무즈 해협 밖 역내 어디서든 추적·처벌하겠다고 경고했고, 10월 11일에는 UAE 라스알카이마 앞 정박 선박에 두바이 정박지로 옮기라고 했다 [채널]",
  "봉쇄 집행: 미 중부사령부는 10월 10일 오만만에서 이란 봉쇄를 돌파하려던 파나마 선적 화물선 오션 몰리카호를 정밀유도무기로 타격해 멈춰 세웠고, 7월 14일 봉쇄 재개 뒤 상선 4척 무력화·135척 회항을 밝혔다 [채널]",
  "운임: 10월 9일 발틱거래소 기준 미 걸프-중국(TD22) VLCC 1항차 운임은 약 7,961만 달러였고, 미국발 한 계약은 배럴당 41달러로 WTI 선물 가격의 약 45%에 달했다 [채널]",
  "일본: 일본 내각은 10월 13일 호르무즈를 우회하는 원유·연료 수입의 추가 운송비를 보전하는 보조금과, 외국 재보험사가 거부할 때 선박 보험금 일부를 정부가 떠안는 방안 등 법안 3건을 승인했다 [사실]",
  "피격: 10월 9일 UAE 알자지라 서쪽 13해리 해상에서 선박이 정체불명 발사체에 맞아 불이 났고, 10월 13일에는 UKMTO가 24시간 새 최소 4건의 직접 피격을 보고했다는 전언이 나왔다 [채널]"],
 "basis": "partial",
 "check": "일본 내각의 우회 수입 운송비 보조·선박 보험 법안 승인은 검색 결과 요약으로 확인. 이란의 걸프 전역 봉쇄 경고, 미군의 화물선 타격 세부, VLCC 1항차 운임 수치는 독립 출처로 확인 못 함(미군 타격은 로이터 제목과 일치)",
 "src": [{"o": "Rallies(일본 내각 운송비 지원 법안)", "d": "2026-10-13", "u": "https://rallies.ai/news/japan-cabinet-backs-plan-to-help-oil-importers-pay-higher-transport-costs-d00537f8ad2c85aa"},
         {"o": "Red Hot Singapore", "d": "2026-10-13", "u": "https://www.redhot.sg/japan-cabinet-backs-plan-to-help-oil-importers-pay-for-higher-transport-costs-727266.html"}],
 "inds": ["macro", "gas"], "nodes": ["macro/geo", "macro/commodity", "gas/shipping"],
 "added": "이번 텔레그램·로이터 20건으로 {{이란의 걸프 전역 봉쇄 경고}}와 미군의 봉쇄 돌파 화물선 타격, VLCC 1항차 8천만 달러 운임, {{일본 운송비 지원 법안}} 승인이 추가됐다",
 "items": [
  it("미국-극동 VLCC 운임, WTI 원유 가격 대비 25% 할증 수준", TP+"Polaristimes", "2026-10-09", "https://t.me/The_MariTimes/63621",
     "{{미국-극동 VLCC 운임}}이 WTI 가격 대비 크게 오르면서, 미국산 원유를 수입하면 원유값에 약 {{25% 할증}}이 붙는 셈이 됐다"),
  it("선박 공격 급증 속 UAE 앞바다서 선박이 정체불명 발사체에 피격", "로이터", "2026-10-09", "https://www.reuters.com/world/middle-east/vessel-struck-by-unknown-projectile-off-uae-coast-amid-surge-attacks-ukmto-says-2026-10-09/",
     "{{UAE 앞바다}}에서 선박이 정체불명 발사체에 맞으면서, 걸프 해역의 선박 공격이 {{급증}}하는 흐름이 이어졌다 (제목 기준)"),
  it("이란, 페르시아만 전역 완전 봉쇄 발표…무허가 선박 공격 경고", TP+"트릴리온", "2026-10-10", "https://t.me/Trillion_labs/10231",
     "{{이란}}이 페르시아만 전역 완전 봉쇄를 발표하면서, 허가받지 않은 선박은 {{호르무즈 밖}}에서도 공격 대상이 될 수 있게 됐다"),
  it("호르무즈 해협 오만 측 항로서 기뢰 피격 의심 폭발 보도", TP+"Polaristimes", "2026-10-10", "https://t.me/The_MariTimes/63632",
     "호르무즈 해협 {{오만 측 항로}}에서 기뢰 피격으로 의심되는 강한 폭발이 보도되면서, 우회 항로도 안전하지 않다는 {{우려}}가 커졌다"),
  it("미 멕시코만-중국 VLCC 운항비 8천만 달러…로켓 발사비보다 비싸", TP+"트릴리온", "2026-10-10", "https://t.me/Trillion_labs/10242",
     "유가 위기 속 {{미 멕시코만-중국 VLCC}} 운항 비용이 {{8천만 달러}}에 이르면서, 유조선 소유주들이 막대한 돈을 벌어들이고 있다"),
  it("러시아·이란, 카스피해 화물선 127척→211척 늘려 미 봉쇄 대응", TP+"트릴리온", "2026-10-10", "https://t.me/Trillion_labs/10254",
     "{{러시아와 이란}}이 카스피해 화물선을 127척에서 211척으로 늘리면서, 이란 수입품의 {{30% 이상}}이 카스피해 북부 항구를 거치게 됐다"),
  it("혁명수비대 해군, 규정 위반 선박 역내 전역서 추적·처벌 경고", TP+"미국 주식 인사이더", "2026-10-10", "https://t.me/insidertracking/65845",
     "{{혁명수비대 해군}}이 위반 선박 대응을 호르무즈에 국한하지 않겠다고 밝히면서, 무허가 항로 선박이 {{역내 전역}}에서 추적·처벌 대상이 됐다"),
  it("UKMTO \"UAE 알자지라 서쪽 해상서 선박 발사체 피격·화재\"", TP+"미국 주식 인사이더", "2026-10-10", "https://t.me/insidertracking/65846",
     "UKMTO가 10월 9일 {{UAE 알자지라 서쪽 13해리}} 해상에서 선박이 발사체에 맞아 불이 났다고 밝히면서, 인근 통과 선박에 {{주의}}를 당부했다"),
  it("유조선 운임 60년 만에 최고…미국-중국 원유 운송비가 로켓 발사비 넘어", TP+"하나증권 중국전략", "2026-10-10", "https://t.me/HANAchina/70176",
     "호르무즈 운송력 부족과 환적 증가로 {{배럴당 운송비}}가 41달러까지 뛰면서, 정유사 이익이 잠식되고 {{중고 유조선 값}}이 신조선을 웃돌았다"),
  it("서아프리카-중국 VLCC 운임 배럴당 32.89달러…연초 2.5달러서 폭등", TP+"트릴리온", "2026-10-11", "https://t.me/Trillion_labs/10306",
     "{{서아프리카-중국 VLCC 운임}}이 연초 배럴당 2.5달러에서 10월 9일 {{32.89달러}}로 뛰면서, 200만 배럴 한 척 운임만 약 6,578만 달러가 됐다"),
  it("혁명수비대, UAE 라스알카이마 정박 선박에 두바이 이동 경고", TP+"트릴리온", "2026-10-11", "https://t.me/Trillion_labs/10311",
     "{{혁명수비대}}가 UAE {{라스알카이마}} 앞 정박 선박에 두바이 정박지로 옮기지 않으면 공격하겠다고 경고하면서, 호르무즈 인근 정박도 위험해졌다"),
  it("혁명수비대 \"무허가 항로 이탈 VLCC, 기뢰 충돌로 폭발·화재\"", TP+"미국 주식 인사이더", "2026-10-11", "https://t.me/insidertracking/65937",
     "{{혁명수비대}}가 위치추적을 끈 채 무허가 항로로 빠져나가던 VLCC가 {{기뢰}}에 부딪혀 불탔다고 밝히면서, 위반 유조선에 같은 결과를 경고했다"),
  it("미군, 오만만서 이란 봉쇄 돌파 시도 화물선 정밀타격으로 무력화", TP+"미국 주식 인사이더", "2026-10-11", "https://t.me/insidertracking/65938",
     "{{미 중부사령부}}가 봉쇄를 돌파하려던 화물선 오션 몰리카호를 정밀유도무기로 멈춰 세우면서, 7월 이후 {{상선 4척 무력화}}와 135척 회항 실적을 밝혔다"),
  it("사우디 원유 200만 배럴 실은 VLCC GEM NO.2, UAE 앞바다서 피격", TP+"트릴리온", "2026-10-11", "https://t.me/Trillion_labs/10315",
     "사우디 원유 200만 배럴을 실은 {{GEM NO.2호}}가 호르무즈 밖 UAE 해안에서 피격되면서, 이란 항로를 피한 {{우회 해역}}도 안전하지 않음이 드러났다"),
  it("미군, 이란 봉쇄를 돌파하려던 화물선을 무력화했다고 밝혀", "로이터", "2026-10-11", "https://www.reuters.com/world/us-military-says-it-disabled-cargo-vessel-trying-run-iran-blockade-2026-10-11/",
     "{{미군}}이 이란 봉쇄를 뚫으려던 화물선을 무력화했다고 밝히면서, 미국의 대이란 {{해상 봉쇄}}가 실제 무력 집행으로 이어졌다 (제목 기준)"),
  it("미-중 VLCC 운임 8천만 달러, 팰컨9 발사비 7,400만 달러 넘어", TP+"TNBfolio", "2026-10-11", "https://t.me/TNBfolio/71495",
     "미국발 아시아행 {{VLCC 운임}}이 배럴당 41달러로 WTI의 약 45%까지 오르면서, 정제마진이 10월 {{배럴당 약 15달러}}로 줄어든 것으로 추정됐다"),
  it("UKMTO \"오만만서 유조선·군 병력 연루 사건 보고 접수\"", TP+"미국 주식 인사이더", "2026-10-11", "https://t.me/insidertracking/65945",
     "UKMTO가 10월 10일 {{오만만}}에서 유조선과 군 병력이 연루된 사건을 접수하면서, 인근 선박에 최신 보안 정보 확인과 {{경계 유지}}를 권고했다"),
  it("미군, 한 달여 만에 상선 첫 공격…이란은 유조선 기뢰 폭발 주장", TP+"하나증권 중국전략", "2026-10-11", "https://t.me/HANAchina/70217",
     "{{미군}}이 한 달여 만에 처음 상선을 타격하고 이란이 같은 날 유조선 {{기뢰 폭발}}을 발표하면서, 호르무즈 해협 긴장이 다시 높아졌다"),
  it("이란, 미 해군 호위 선박 겨냥 대함미사일 공격 재개", TP+"트릴리온", "2026-10-13", "https://t.me/Trillion_labs/10390",
     "{{이란}}이 미 해군 호위 선박을 겨냥한 대함미사일 공격을 재개한 것으로 전해지면서, 24시간 새 {{최소 4건}}의 선박 직접 피격이 보고됐다"),
  it("일본 내각, 원유 수입업체의 늘어난 운송비 지원 방안 승인", "로이터", "2026-10-13", "https://www.reuters.com/legal/litigation/japan-cabinet-backs-plan-help-oil-importers-pay-higher-transport-costs-2026-10-13/",
     "{{일본 내각}}이 호르무즈 우회 수입의 추가 운송비를 보전하는 보조금 법안을 승인하면서, {{원유 수입업체}}의 운송비 부담이 줄어들 전망이다"),
 ]})

B.append({"cid": "C020", "attachTo": "n-bbg-0052",
 "title": "9월 CPI {{0.56% 상승}} 전망…맥쿼리 \"{{10월 연준 인상}} 가능성 낮아\"",
 "one": "휘발유 급등으로 {{9월 미국 CPI}}가 전월 대비 0.56%, 전년 대비 3.6%로 뛸 전망이지만 근원 물가는 둔화가 예상되고 {{맥쿼리}}가 이번 지표로 10월 인상 결정이 바뀌지 않을 것으로 보면서, 시장의 {{10월 인상 확률}}은 약 19%에 머물고 있다",
 "facts": [
  "무엇이: 10월 14일 발표될 9월 CPI는 헤드라인 전월비 0.56%(UBS·블룸버그 컨센서스), 전년비 3.62%로 8월 3.40%에서 오를 것으로 UBS가 전망했다 [채널]",
  "근원: 바클레이즈·모건스탠리는 근원 CPI 전월비가 8월 0.29%에서 0.24%로 둔화할 것으로, UBS는 0.19%로 봤다 [채널]",
  "휘발유: 9월 휘발유 평균값은 갤런당 4.33달러로 9월 기준 최고였고, 헤드라인 상승분 대부분은 에너지에서 나온다 [사실]",
  "연준: 맥쿼리 위즈먼은 9월 CPI가 가속해도 이달 말 인상 결정을 바꾸지 않을 것이라 했고, 시장은 10월 28일 인상 확률을 약 19%로 반영한다 [사실]",
  "12월: 한 채널 집계는 10월 동결 83.5%, 12월 25bp 인상 74.5%를 제시했다 [채널]"],
 "basis": "verified",
 "check": "맥쿼리 전망, 10월 인상 확률 약 19%, 헤드라인 3.6% 안팎·휘발유 4.33달러는 검색 결과 요약으로 확인. UBS 세부 전망과 바클레이즈·모건스탠리 근원 수치는 채널 전언",
 "src": [{"o": "ChainCatcher(맥쿼리 전망)", "d": "2026-10-13", "u": "https://www.chaincatcher.com/en/article/2295859"},
         {"o": "Admiral Markets", "d": "2026-10", "u": "https://admiralmarkets.com/analytics/traders-blog/us-cpi-september-2026-scenarios-fed-october"}],
 "inds": ["macro"], "nodes": ["macro/inflation", "macro/cb", "macro/rates"],
 "added": "이번 텔레그램·블룸버그 5건으로 {{9월 CPI 0.56% 상승}} 전망과 근원 물가 둔화 예상, {{맥쿼리의 10월 인상 회의론}}이 기존 연준 경로 논의에 추가됐다",
 "items": [
  it("다음 주 미국 CPI의 의미: 연준, 10월 금리 동결할까", TP+"하나증권 중국전략", "2026-10-09", "https://t.me/HANAchina/70137",
     "{{바클레이즈·모건스탠리}}가 9월 근원 CPI 상승률이 0.24%로 둔화할 것으로 보면서, 연준의 {{10월 동결}} 근거가 될 수 있다는 분석이 나왔다"),
  it("연준 금리 전망: 10월 동결 83.5%, 12월 25bp 인상 74.5%", TP+"미국 주식 인사이더", "2026-10-10", "https://t.me/insidertracking/65892",
     "시장이 10월 동결 확률을 83.5%로 보는 대신 {{12월 25bp 인상}} 확률을 74.5%로 반영하면서, {{연내 1회 인상}} 경로가 유력해졌다"),
  it("미국 CPI, 휘발유 가격 상승에 전체 물가 상승 보여줄 전망", "블룸버그", "2026-10-11", "https://www.bloomberg.com/news/articles/2026-10-10/us-cpi-to-show-overall-inflation-boosted-by-higher-gasoline-prices",
     "{{휘발유 가격}} 상승이 9월 미국 CPI를 끌어올리면서, 전체 물가 상승률이 높게 나올 것으로 {{블룸버그}}가 전망했다"),
  it("UBS 9월 CPI 프리뷰: 헤드라인 0.56%, 근원 0.19% 전망", TP+"KK Kontemporaries", "2026-10-11", "https://t.me/kkkontemp/2731",
     "{{UBS}}가 9월 헤드라인 CPI를 0.56%로 보면서도 근원은 {{0.19%}}로 컨센서스보다 낮게 전망해, 에너지발 물가와 근원 둔화가 엇갈릴 것으로 봤다"),
  it("맥쿼리 \"9월 CPI 가속해도 연준 10월 인상 가능성 낮아\"", TP+"미국 주식 인사이더", "2026-10-13", "https://t.me/insidertracking/66111",
     "{{맥쿼리}}가 9월 CPI가 가속하더라도 이달 말 인상 결정을 바꾸지 않을 것으로 보면서, 시장의 10월 인상 확률은 {{약 19%}}에 그쳤다"),
 ]})

B.append({"cid": "C029", "attachTo": "n-tg-0233",
 "title": "{{ASML}}, 한국향 노광장비 부품값 일괄 10% 인상…킹보드 적층판 15%↑",
 "one": "{{ASML}}이 삼성전자·SK하이닉스에 공급하는 EUV·DUV 부품값을 2027년 1월부터 일괄 {{10%}} 올리고 킹보드도 박형 유리섬유 적층판 값을 15% 올리면서, 인텔·AMD 칩값 인상에 이어 {{반도체 공급망 전반}}의 원가 부담이 커지고 있다",
 "facts": [
  "무엇이: ASML이 한국에 공급한 EUV·DUV 장비의 소모품부터 핵심 부품까지 교체 부품값을 2027년 1월부터 일괄 10% 올리기로 했고 삼성전자·SK하이닉스가 수용했다는 보도가 나왔다 [사실]",
  "배경: 그간 개별 부품만 조정해 온 ASML의 일괄 인상은 이례적이며, 대체 공급처가 없어 고객사의 협상 여지가 작았다는 분석이 나왔다 [사실]",
  "확산: 어플라이드 머티어리얼즈·도쿄일렉트론도 가격 인상에 나섰다고 전해졌다 [채널]",
  "기판: 킹보드는 10월 13일 2116 규격 이하 박형 유리섬유 원단을 쓰는 적층판·프리프레그 판매가를 15% 올린다고 공지했다 [채널]"],
 "basis": "verified",
 "check": "ASML 부품값 10% 인상과 삼성·SK하이닉스 수용은 검색 결과 요약으로 확인(시행 시점은 2027년 1월로 보도, 일부 채널은 2026년 1월로 표기). ASML 공식 발표는 없음. 킹보드 15% 인상은 확인 못 함",
 "src": [{"o": "TrendForce", "d": "2026-10-12", "u": "https://www.trendforce.com/news/2026/10/12/news-asml-reportedly-plans-10-parts-price-hike-in-south-korea-starting-jan-2027-equipment-prices-may-also-rise/"},
         {"o": "Tech Times", "d": "2026-10-12", "u": "https://www.techtimes.com/articles/328933/20261012/asml-forces-first-ever-blanket-parts-hike-samsung-sk-hynix-january.htm"}],
 "inds": ["macro"], "nodes": ["macro/semis", "macro/inflation"],
 "added": "이번 텔레그램 5건으로 삼성전자·SK하이닉스가 수용한 {{ASML 부품값 10% 인상}}과 킹보드의 {{박형 적층판 15% 인상}}이 기존 칩·부품 가격 인상 흐름에 추가됐다",
 "items": [
  it("ASML, 한국 공급 장비 교체 부품값 일괄 10% 인상…내년 1월 적용", TP+"TNBfolio", "2026-10-10", "https://t.me/TNBfolio/71491",
     "{{ASML}}이 한국향 노광장비 부품값을 일괄 10% 올리면서, 반도체 공급망의 {{가격 결정권}}이 고객사에서 장비업체로 넘어가고 있다는 평가가 나왔다"),
  it("ASML, 장비 부품값 10% 인상…삼성전자·SK하이닉스 수용", TP+"하나증권 중국전략", "2026-10-10", "https://t.me/HANAchina/70181",
     "{{삼성전자·SK하이닉스}}가 ASML의 부품값 10% 인상을 받아들이면서, 동시 증설로 빠듯한 {{소모품 분야}}까지 공급 부족이 넓어질 전망이다"),
  it("ASML 전 부품 10% 인상에 반도체 장비 시장 전반으로 가격 압박 확산", TP+"부의 나침반", "2026-10-11", "https://t.me/w_compass/7231",
     "ASML에 이어 {{어플라이드머티리얼즈}} 같은 대형 장비업체도 값을 올리면서, {{웨이퍼 제조업체}}의 가격 협상력이 약해지고 있다"),
  it("ASML, EUV·DUV 전체 부품 10% 인상 확정…광학·광원 등 포함", TP+"미국 주식 인사이더", "2026-10-11", "https://t.me/insidertracking/65952",
     "ASML이 지난달 초 한국 법인을 통해 통보한 인상안을 협의 끝에 확정하면서, {{광학 시스템·광원}} 등 노광장비 {{전 부품}}의 값이 오르게 됐다"),
  it("킹보드, 박형 유리섬유 적층판·프리프레그 가격 15% 인상 공지", TP+"트릴리온", "2026-10-13", "https://t.me/Trillion_labs/10396",
     "{{킹보드}}가 박형 유리섬유 원단 부족을 이유로 2116 규격 이하 적층판·프리프레그 값을 {{15%}} 올리면서, 전자기판 원가 부담이 커지게 됐다"),
 ]})

B.append({"cid": "C043", "attachTo": "n-tg-0122",
 "title": "日 {{공작기계 수주 2,232억 엔}} 사상 최대…대만 기계 수출·포모사 이익도 급증",
 "one": "AI·반도체 장비 수요로 {{일본 9월 공작기계 수주}}가 60% 늘어 월간 최대를 기록하고 {{대만 기계 수출}}도 1~3분기 20% 늘었으며 {{포모사 4사}} 3분기 순이익이 4.8배로 뛰면서, 대만 상장사 사상 최대 매출에 이어 AI발 호황이 장비·소재 업종으로 번지고 있다",
 "facts": [
  "무엇이: 일본공작기계공업회 속보치로 9월 공작기계 수주는 2,232억 엔으로 60.4% 늘어 월간 최고였고 15개월 연속 증가했으며, 외수가 1,592억 엔으로 66.8% 늘었다 [사실]",
  "잔고: 8월 말 일본 공작기계 미출하 수주 잔액이 1조 엔을 넘어 사상 최고였고, 시바우라기계 등이 증산에 나섰다 [사실]",
  "대만 기계: 1~3분기 기계 수출액은 279억 8천만 달러로 20.3% 늘었고 9월은 29.9% 늘어 20개월 연속 증가했지만, 공구기계 완성품 수출은 1.9% 줄었다 [채널]",
  "포모사: 포모사 4사의 3분기 세후 순이익은 762억 7,900만 대만달러로 4.8배 넘게 늘었고 9월 합산 매출은 51.9% 늘었다 [채널]",
  "기존: 대만 상장사 9월 매출은 6조 5,900억 대만달러로 월간 최고였다 [채널]"],
 "basis": "verified",
 "check": "일본 9월 공작기계 수주 2,232억 엔(60.4% 증가, 사상 최고)과 미출하 잔액 1조 엔 돌파는 검색 결과 요약으로 확인. 대만 기계 수출과 포모사 4사 실적은 확인 못 함(채널 전언)",
 "src": [{"o": "RTTNews", "d": "2026-10-09", "u": "https://www.rttnews.com/story.aspx?Id=3697823"},
         {"o": "Nikkei Asia", "d": "2026-10", "u": "https://asia.nikkei.com/business/business-trends/japan-machine-tool-order-backlog-hits-all-time-high-on-ai-demand"},
         {"o": "産機通信(kikai-news)", "d": "2026-10-09", "u": "https://note.com/sankituushin/n/n6497c7b3d771?hl=en"}],
 "inds": ["macro", "petchem"], "nodes": ["macro/semis", "macro/growth", "petchem/commodity"],
 "added": "이번 텔레그램 3건으로 {{일본 공작기계 수주}} 사상 최대와 대만 기계 수출 20% 증가, {{포모사 4사 순이익 4.8배}} 급증이 기존 대만 매출 호조에 추가됐다",
 "items": [
  it("AI 수요에 일본 공작기계 미출하 수주 잔액 1조 엔 돌파", TP+"하나증권 중국전략", "2026-10-10", "https://t.me/HANAchina/70178",
     "AI 관련 수요로 {{일본 공작기계 미출하 잔액}}이 1조 엔을 넘고 9월 수주가 60% 늘면서, {{시바우라기계}} 등 제조업체가 증산에 속도를 내고 있다"),
  it("대만 1~3분기 기계 수출 279억 8천만 달러로 20.3% 증가", TP+"하나증권 중국전략", "2026-10-13", "https://t.me/HANAchina/70320",
     "AI·반도체 장비 수요로 {{대만 기계 수출}}이 1~3분기 20.3% 늘면서, 연간 목표 {{380억 달러}} 달성과 사상 최대 경신이 전망된다"),
  it("포모사 4사 3분기 순이익 4.8배 급증…1~3분기 흑자 전환", TP+"하나증권 중국전략", "2026-10-13", "https://t.me/HANAchina/70323",
     "AI 열풍으로 {{포모사 4사}} 3분기 순이익이 762억 7,900만 대만달러로 4.8배 넘게 늘면서, {{난야플라스틱}} 등이 사상 최대 이익을 냈다"),
 ]})

B.append({"cid": "C053", "attachTo": "",
 "title": "골드만 {{월드론}} 차기 CEO 부상…판궁성 인민은행 총재와 회동",
 "one": "{{골드만삭스}} 이사회가 존 월드론 사장 겸 COO를 차기 CEO로, 데이비드 솔로몬을 의장으로 두는 방안을 논의하는 가운데 월드론이 {{판궁성 인민은행 총재}}와 만나면서, 골드만 {{후계 구도}}와 다른 임원 거취에 관심이 쏠리고 있다",
 "facts": [
  "무엇이: 골드만삭스 이사회가 월드론을 차기 CEO로, 솔로몬을 1~2년간 의장으로 두는 방안을 논의 중이라는 보도가 나왔고 회사는 공식 확인하지 않았다 [사실]",
  "시기: 교체 시기는 내년 말~2028년 초 등 보도마다 다르며, 회사 대변인은 시기 관측을 추측이라고 했다 [사실]",
  "파장: 월드론의 부상이 사내에서 다른 임원들의 후계 계획에 연쇄 영향을 준다는 이야기가 나온다 [제목]",
  "회동: 판궁성 인민은행 총재가 10월 9일 월드론 COO와 만나 거시 현안을 논의했다 [채널]"],
 "basis": "verified",
 "check": "월드론 차기 CEO·솔로몬 의장 논의 보도는 검색 결과 요약으로 확인(이사회 승인·공식 발표는 없음). 판궁성 총재 회동은 확인 못 함",
 "src": [{"o": "Fortune", "d": "2026-10-01", "u": "https://fortune.com/2026/10/01/john-waldron-goldman-sachs-next-ceo-wall-street-succession/"},
         {"o": "RIABiz", "d": "2026-10-09", "u": "https://riabiz.com/a/2026/10/9/david-solomon-eyeing-near-term-goldman-sachs-ceo-exit-reports-say-and-his-heir-apparent-looks-ria-friendly-dfa-search-for-ma-partner-went-quiet-and-complex-factors-could-prolong-the-process"}],
 "inds": ["fin"], "nodes": [],
 "added": "이번 텔레그램 1건으로 차기 CEO로 거론되는 {{월드론 COO}}가 10월 9일 {{판궁성 인민은행 총재}}와 만나 거시 현안을 논의한 사실이 추가됐다",
 "items": [
  it("월드론 부상 예상에 골드만 내부 술렁…후계 계획에 연쇄 영향", "로이터", "2026-10-09", "https://www.reuters.com/legal/transactional/waldrons-expected-rise-stirs-talk-inside-goldman-knock-on-succession-plans-2026-10-09/",
     "{{월드론}}의 CEO 승진이 예상되면서, 골드만 내부에서 다른 임원들의 {{후계 계획}}에 미칠 연쇄 영향을 두고 말이 나오고 있다 (제목 기준)"),
  it("골드만 차기 CEO 후보 월드론, 판궁성 인민은행 총재와 회동", TP+"Polaristimes", "2026-10-09", "https://t.me/The_MariTimes/63625",
     "차기 CEO로 거론되는 {{월드론 COO}}가 {{판궁성 인민은행 총재}}를 만나 거시 현안을 논의하면서, 후계 부상과 맞물린 회동 시점이 주목받았다"),
 ]})

B.append({"cid": "C060", "attachTo": "n-bbg-0133",
 "title": "{{인포시스}} \"美 영주권 노동인증 중단, 실질적 영향 없어\"…인도 반발 속 진화",
 "one": "미국이 인포시스·TCS·마이크로소프트 등의 {{영주권 노동인증(PERM)}} 신청을 중단해 인도 정부가 반발한 가운데 {{인포시스}}가 미국 내 현지 인력과 기술 거점을 들어 {{실질적 영향}}이 없을 것이라고 밝히면서, 인도 IT 기업의 실적 타격 우려가 줄어들 수 있다",
 "facts": [
  "무엇이: 인포시스는 10월 10일 거래소 공시에서 미국 정부의 PERM 신청 중단이 실질적 영향을 주지 않을 것으로 본다고 밝혔다 [사실]",
  "근거: 인포시스는 미국 내 탄탄한 현지 인력과 기술·혁신 허브를 이유로 들었고, 필요하면 추가 공시하겠다고 했다 [사실]",
  "기존: 인도 외교부는 10월 9일 미국 조치가 양국 공동 목표에 도움이 되지 않는다고 반발했고, PERM 중단은 기존 H-1B 소지자 신분에는 영향이 없다 [사실]",
  "구글: 한 채널은 비자 규제로 인도 인력을 미국에 데려오기 어려워지자 구글이 인도 내 사업장을 넓히고 있다고 주장했다 [채널]"],
 "basis": "verified",
 "check": "인포시스의 '실질적 영향 없음' 공시는 검색 결과 요약으로 확인. 구글의 인도 사업장 확대 주장은 확인 못 함",
 "src": [{"o": "The Hans India", "d": "2026-10-10", "u": "https://www.thehansindia.com/tech/infosys-doesnt-see-material-impact-from-us-governments-perm-suspension-1131249"},
         {"o": "Zee Business", "d": "2026-10-10", "u": "https://www.zeebiz.com/companies/news-infosys-responds-to-us-perm-suspension-says-operations-unlikely-to-be-hit-403734"}],
 "inds": ["tech"], "nodes": [],
 "added": "이번 텔레그램·로이터 2건으로 {{인포시스의 영향 제한}} 공시와 비자 규제에 맞선 {{구글의 인도 사업장 확대}} 주장이 기존 인도 정부 반발에 추가됐다",
 "items": [
  it("구글, 미국 H-1B 비자 개혁에 인도 내 사업장 확대 시도", TP+"Polaristimes", "2026-10-09", "https://t.me/The_MariTimes/63610",
     "미국의 {{H-1B 비자}} 개혁으로 인도 인력을 데려오기 어려워지면서, {{구글}}이 아예 인도 내 사업장을 넓히는 쪽으로 움직인다는 주장이 나왔다"),
  it("인도 인포시스 \"미국 PERM 중단, 실질적 영향 없을 것\"", "로이터", "2026-10-11", "https://www.reuters.com/world/us/indias-infosys-does-not-expect-material-impact-us-perm-suspension-2026-10-10/",
     "{{인포시스}}가 미국의 PERM 신청 중단에도 {{실질적 영향}}이 없을 것으로 본다고 밝히면서, 현지 인력 중심 운영으로 충격을 흡수할 수 있다는 입장을 냈다"),
 ]})

B.append({"cid": "C069", "attachTo": "n-bbg-0103",
 "title": "BofA \"{{스타링크 모바일}}, 애플에 위협\"…가입자 10% 이탈 시 매출 60억 달러↓",
 "one": "{{스페이스X}}가 800MHz 저주파 대역을 확보해 위성·지상망을 합친 스타링크 모바일로 미 3대 통신사와 경쟁에 나서고 {{BofA}}가 후불 가입자 10%가 옮기면 {{애플 매출 약 60억 달러}}가 줄 수 있다고 추산하면서, 통신사에 이어 아이폰 보조금 판매 구조도 흔들릴 수 있다",
 "facts": [
  "무엇이: BofA는 미 3대 통신사 후불 가입자의 10%가 스페이스X로 옮기면 아이폰 판매가 약 500만 대, 애플 매출이 약 60억 달러 줄 수 있다고 추산했다 [사실]",
  "경로: 3대 통신사를 통해 연간 약 5,300만 대의 아이폰이 대당 약 800달러 프로모션과 함께 팔리는데, 스타링크로 옮기는 가입자는 이 혜택을 잃는다 [사실]",
  "한계: BofA는 단기 실적 위험은 제한적이고 실제 영향은 2028회계연도 이후로 봤으며, 스페이스X는 단말기를 발표하지 않았다 [사실]",
  "스페이스X: 800MHz 대역에서 최대 14MHz 쌍방향 폭을 확보했고, FCC는 2세대 스타링크 모바일 위성 1만 5,000기 배치를 승인했다 [채널]"],
 "basis": "verified",
 "check": "BofA의 아이폰 500만 대·매출 60억 달러 추산과 보조금 경로는 검색 결과 요약으로 확인. 800MHz 14MHz 폭·V2 위성 1만 5,000기 승인은 확인 못 함",
 "src": [{"o": "Yahoo Finance(BofA 분석 보도)", "d": "2026-10", "u": "https://finance.yahoo.com/technology/article/spacexs-starlink-could-pose-3-big-risks-to-apple-bofa-warns-175500290.html"},
         {"o": "BigGo Finance", "d": "2026-10", "u": "https://finance.biggo.com/news/bb116a77-9698-45bc-93ec-5a89946a9d39"}],
 "inds": ["tech"], "nodes": [],
 "added": "이번 텔레그램 2건으로 스타링크 모바일의 {{위성·지상망 통합}} 계획과 FCC의 2세대 위성 승인, {{애플 매출 60억 달러 감소}} 가능성을 짚은 BofA 분석이 추가됐다",
 "items": [
  it("스페이스X, 스타링크 모바일로 위성·지상망 통합…미 이통 3사에 도전", TP+"미국 주식 인사이더", "2026-10-10", "https://t.me/insidertracking/65838",
     "{{스페이스X}}가 800MHz 저주파 대역을 확보해 위성·지상망 통합을 추진하면서, {{T모바일·AT&T·버라이즌}}과 직접 경쟁할 기반을 마련했다"),
  it("BofA \"스타링크 모바일, 세 가지 측면에서 애플에 위협\"", TP+"미국 주식 인사이더", "2026-10-13", "https://t.me/insidertracking/66100",
     "{{BofA}}가 스타링크 이동이 통신사 보조금 모델을 흔들 수 있다고 분석하면서, 후불 가입자 10% 이탈 시 {{아이폰 500만 대}} 감소를 추산했다"),
 ]})

B.append({"cid": "C077", "attachTo": "n-tg-0212",
 "title": "골드만 \"{{위안화 20~25% 저평가}}…1년 뒤 달러당 6.40위안\"",
 "one": "중국의 주담대 보조·인프라 지원이 내수와 부동산을 되살리기엔 약하다는 평가 속에서도 {{골드만삭스}}가 위안화가 {{20~25% 저평가}}됐다며 1년 뒤 {{달러당 6.40위안}}을 전망하면서, 2022년 이후 최강인 위안화의 추가 강세 가능성이 부각되고 있다",
 "facts": [
  "무엇이: 골드만삭스는 시장이 위안화 상승 폭을 과소평가한다며, 위안화가 약 20~25% 저평가됐고 1년 뒤 달러당 6.40위안까지 오를 것으로 전망했다 [사실]",
  "위험: 이란 전쟁발 유가 급등이 연준을 매파로 붙잡아 달러를 떠받치면 위안화 절상 속도가 늦어질 수 있다 [사실]",
  "부양: 생애 첫 주택 구매자 주담대 금리 1%p 보조는 1년간 120㎡ 미만·22.3만 달러 미만 주택에 한정돼, 모건스탠리는 신규 주택 판매의 12%만 혜택을 볼 것으로 추정했다 [채널]",
  "성장: 2분기 GDP 성장률은 4.3%로 3년여 만에 최저였고, 9월에는 8개 은행·보험사에 540억 달러 자본 투입이 발표됐다 [채널]",
  "기존: 역외 위안화는 10월 12일 달러당 6.6906위안으로 2022년 이후 가장 강했다 [채널]"],
 "basis": "verified",
 "check": "골드만의 20~25% 저평가·1년 뒤 6.40위안 전망은 검색 결과 요약으로 확인. WSJ 인용 중국 부양책 세부는 채널 전언",
 "src": [{"o": "investingLive", "d": "2026-10-12", "u": "https://investinglive.com/forex/goldman-sachs-says-yuan-undervalued-by-up-to-25-and-markets-underestimate-how-far-it-can-rise/"},
         {"o": "Briefs", "d": "2026-10-12", "u": "https://www.briefs.co/news/goldman-says-markets-are-missing-the-odds-of-a-stronger-yuan/"}],
 "inds": ["macro"], "nodes": ["macro/fx", "macro/fiscal", "macro/growth"],
 "added": "이번 텔레그램·블룸버그 2건으로 {{중국 부양책의 제한적 규모}} 평가와 위안화 1년 뒤 6.40위안을 내다본 {{골드만의 강세 전망}}이 추가됐다",
 "items": [
  it("WSJ \"중국, 커지는 경제 문제에 반쪽 대책만 내놔\"", TP+"상상인 김진범", "2026-10-10", "https://t.me/PipeBeom/6648",
     "{{중국 정부}}가 주담대 보조·금융기관 자본 확충·인프라 지원을 내놨지만 규모가 제한적이어서, {{내수와 부동산}} 회복엔 역부족이라는 평가가 나왔다"),
  it("골드만 \"시장은 위안화가 얼마나 오를 수 있는지 과소평가\"", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-12/goldman-says-markets-are-underestimating-how-far-yuan-can-rise",
     "{{골드만삭스}}가 위안화 상승 여력을 시장이 과소평가한다고 보면서, 1년 뒤 {{달러당 6.40위안}}까지 절상될 수 있다고 전망했다"),
 ]})

B.append({"cid": "C095", "attachTo": "",
 "title": "美 농무부, 농가 태양광 보조금 문턱 높여…{{농지 지상형 설치}} 배제",
 "one": "{{미 농무부}}가 농촌에너지지원(REAP) 규정을 바꿔 12개월 가동 실적을 낸 뒤에야 보조금을 신청하게 하고 {{농지 지상형 태양광}}과 중국산 부품 설비를 배제하면서, {{농가 재생에너지 사업}}의 자금 조달이 어려워진다",
 "facts": [
  "무엇이: 농무부가 10월 1일 확정한 REAP 개정 규정이 10월 16일 시행되며, 설비를 먼저 완공·가동한 뒤 12개월 실측 자료로 신청해야 한다 [사실]",
  "제한: 인증 농지의 지상형 태양광·풍력과 중국 등 적대국산 부품을 쓴 설비가 배제되고, 지붕형은 농지 금지 대상에서 빠진다 [사실]",
  "지원 축소: 사업비 자기부담이 75% 이상으로 높아졌고, 재생에너지 설비 보조금 상한은 50만 달러다 [사실]",
  "반발: 환경단체들이 새 자격 기준의 무효화를 요구하는 소송을 냈다 [사실]"],
 "basis": "verified",
 "check": "REAP 개정 규정의 시행일·사후 신청·농지 지상형 배제·적대국 부품 배제는 검색 결과 요약으로 확인(일부 출처는 태양광 업계 블로그)",
 "src": [{"o": "Solar Power World", "d": "2026-10", "u": "https://www.solarpowerworldonline.com/2026/10/reap-grant-update-makes-solar-projects-on-farmland-ineligible/"},
         {"o": "IndexBox", "d": "2026-10", "u": "https://www.indexbox.io/blog/usda-revises-rural-energy-for-america-program-stricter-rules-for-solar-grants/"}],
 "inds": ["power"], "nodes": ["power/developers", "power/modules"],
 "items": [
  it("트럼프 새 규정, 농가의 연방 에너지 사업 자금 접근 어렵게 만들어", "로이터", "2026-10-09", "https://www.reuters.com/legal/litigation/new-trump-rules-will-make-it-harder-farmers-access-us-funds-energy-projects-2026-10-09/"),
 ]})

B.append({"cid": "C103", "attachTo": "",
 "title": "EU 재무장관, {{자본시장 감독 통합}} 축소 타협…도이체뵈르제 제외",
 "one": "{{EU 재무장관들}}이 대형 거래소·청산소 감독을 ESMA로 옮기는 안을 독일 요구대로 {{도이체뵈르제}}를 빼는 등 축소해 합의하면서, 자본시장 통합의 {{야심이 낮아졌다}}는 집행위원회와 ECB의 비판이 나왔다",
 "facts": [
  "무엇이: EU 재무장관들은 10월 9일 룩셈부르크에서 시장통합·감독 패키지의 축소 타협안에 합의했다 [사실]",
  "범위: ESMA는 가장 중요한 국경 간 거래소와 중앙예탁기관·청산소만 감독하며, 독일 요구로 도이체뵈르제와 SIX 그룹 등이 빠졌다 [사실]",
  "가상자산: EU 내 약 360개 가상자산 사업자 가운데 10~15곳만 ESMA 감독을 받는다 [사실]",
  "다음: 이는 이사회 협상안이며 유럽의회 안과 조율해야 한다 [사실]"],
 "basis": "verified",
 "check": "10월 9일 축소 타협, 도이체뵈르제 제외, 가상자산 10~15곳, 집행위 비판은 검색 결과 요약으로 확인",
 "src": [{"o": "Eunews", "d": "2026-10-09", "u": "https://www.eunews.it/en/2026/10/09/financial-markets-ecofin-curbs-esmas-supervisory-powers-drawing-criticism-from-the-european-commission-and-the-ecb/"},
         {"o": "MLex", "d": "2026-10-09", "u": "https://www.mlex.com/mlex/financial-services/articles/2536311"}],
 "inds": ["fin"], "nodes": [],
 "items": [
  it("EU 재무장관, 자본시장 감독 중앙집중화에 후퇴한 타협안 합의", "로이터", "2026-10-09", "https://www.reuters.com/legal/government/eu-ministers-reach-watered-down-compromise-centralised-cap-markets-supervision-2026-10-09/"),
 ]})

B.append({"cid": "C111", "attachTo": "",
 "title": "케냐, 케냐항공에 {{3억 5천만 달러}} 주주 금융 승인…부채 자본화도 추진",
 "one": "{{케냐 내각}}이 케냐항공에 {{3억 5천만 달러}} 주주 금융을 승인하고 정부 대출 약 9억 4,100만 달러의 자본 전환도 추진하면서, 정비 지연으로 멈춘 {{여객기 운항 재개}}에 자금이 투입된다",
 "facts": [
  "무엇이: 케냐 내각은 10월 9일 케냐항공에 3억 5천만 달러(약 454억 실링) 주주 금융을 승인했고, 재무부 감독 아래 분할 지급하며 최장 10년에 걸쳐 상환한다 [사실]",
  "부채: 기존 정부 대출 약 1,220억 실링(약 9억 4,100만 달러)을 자본으로 인정되는 거래 가능 상품으로 바꾸는 방안도 승인했지만 새 현금은 아니며 추가 승인이 필요하다 [사실]",
  "실적: 상반기 세전손실은 159억 2천만 실링으로 1년 전 121억 7천만 실링보다 커졌고 연료비가 72% 늘었다 [사실]"],
 "basis": "verified",
 "check": "3억 5천만 달러 주주 금융 승인과 상환 조건, 부채 전환안은 검색 결과 요약으로 확인",
 "src": [{"o": "CNBC Africa", "d": "2026-10-09", "u": "https://www.cnbcafrica.com/2026/kenya-approves-350-million-shareholder-financing-for-kenya-airways"},
         {"o": "ChimpReports", "d": "2026-10", "u": "https://chimpreports.com/kenya-approves-350-million-for-kenya-airways-rescue/"}],
 "inds": ["aero"], "nodes": [],
 "items": [
  it("케냐, 케냐항공에 3억 5천만 달러 규모 주주 금융 승인", "로이터", "2026-10-09", "https://www.reuters.com/world/africa/kenya-approves-350-million-shareholder-financing-kenya-airways-2026-10-09/"),
 ]})

B.append({"cid": "C127", "attachTo": "",
 "title": "{{퀄컴·암}} 계약 위반 분쟁, 델라웨어 배심 평결 앞둬",
 "one": "{{퀄컴}}이 암이 계약상 제공물을 주지 않고 최저가 보장 조항을 어겼다며 낸 소송에서 {{델라웨어 배심}}이 첫 심의에서 결론을 못 내면서, 차세대 아키텍처 {{라이선스 협상}}을 둘러싼 양사 분쟁의 향방이 평결에 걸렸다",
 "facts": [
  "무엇이: 퀄컴이 암을 상대로 낸 계약 위반 소송의 배심이 델라웨어 윌밍턴에서 금요일 약 4시간 심의했지만 결론을 내지 못했고 화요일 다시 모인다 [사실]",
  "쟁점: 퀄컴은 암이 칩 테스트 도구 등 제공물을 주지 않고 해지 위협을 흘려 메타와의 협상을 해쳤으며, 최저가 대비 10% 이내 가격 조항을 어겼다고 주장한다 [사실]",
  "반론: 암은 퀄컴이 금전 피해를 보지 않았고 소송이 라이선스 조건 다툼의 지렛대라고 본다 [사실]",
  "미확인: 배심 교착으로 재판이 끝났다는 보도 제목도 있어 최종 평결 여부는 확인하지 못했다 [미확인]"],
 "basis": "partial",
 "check": "배심 심의 교착과 화요일 재개, 양측 주장은 검색 결과 요약으로 확인. 최종 평결 여부는 확인 못 함",
 "src": [{"o": "Yahoo Finance", "d": "2026-10", "u": "https://finance.yahoo.com/markets/stocks/articles/qualcomm-arm-trial-ends-hung-130049760.html"},
         {"o": "Hoodline", "d": "2026-10", "u": "https://hoodline.com/2026/10/qualcomm-arm-return-to-delaware-court-over-billions-in-royalty-fight/"}],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "items": [
  it("퀄컴과 암, 계약 위반 분쟁에서 배심 평결 받을 예정", "로이터", "2026-10-10", "https://www.reuters.com/business/media-telecom/qualcomm-arm-set-jury-verdict-contract-breach-feud-2026-10-09/"),
 ]})

B.append({"cid": "C135", "attachTo": "",
 "title": "中 1~9월 도시 일자리 {{1,052만 개}}…서비스업 고용 정책 예고",
 "one": "{{중국}}이 1~9월 도시 일자리 {{1,052만 개}}를 만들어 연간 목표의 87.7%를 채우고 {{서비스업 고용 정책}} 문서를 준비하면서, 부진한 내수 속 고용 방어의 축이 서비스업으로 옮겨갈 전망이다",
 "facts": [
  "무엇이: 중국 인력자원사회보장부는 1~9월 도시 신규 일자리가 1,052만 개로 연간 목표의 87.7%라고 밝혔다 [사실]",
  "정책: 서비스업이 고용 흡수의 주 경로가 되도록 관계 부처와 서비스업 고용 문서를 마련 중이며, 세부 내용은 아직 공개되지 않았다 [사실]",
  "실업: 1~8월 도시 조사실업률은 평균 5.2%였다 [사실]"],
 "basis": "verified",
 "check": "1,052만 개·목표 대비 87.7%·서비스업 고용 문서 준비는 검색 결과 요약으로 확인",
 "src": [{"o": "SCIO(국무원 신문판공실)", "d": "2026-10-10", "u": "http://english.scio.gov.cn/pressroom/2026-10/10/content_118728380.html"},
         {"o": "Business Recorder", "d": "2026-10-10", "u": "https://www.brecorder.com/news/40443581/china-adds-1052m-urban-jobs-in-jan-sept-to-roll-out-services-jobs-policy"}],
 "inds": ["macro"], "nodes": ["macro/growth"],
 "items": [
  it("중국, 1~9월 도시 일자리 1,052만 개 창출…서비스업 고용 정책 내놓는다", "로이터", "2026-10-10", "https://www.reuters.com/world/asia-pacific/china-adds-1052-million-urban-jobs-jan-sept-roll-out-services-jobs-policy-2026-10-10/"),
 ]})

B.append({"cid": "C143", "attachTo": "",
 "title": "{{로사톰}} \"핀란드 원전 분쟁 중재 승소\"…순차액은 로사톰 측이 지급",
 "one": "{{로사톰}}이 국제상업회의소 중재에서 핀란드 {{펜노보이마}}의 2022년 한히키비-1 원전 계약 해지가 불법으로 판단됐다고 밝혔지만 순차액은 로사톰 자회사가 내야 하는 것으로 알려지면서, {{양측 모두}} 승리를 주장하고 있다",
 "facts": [
  "무엇이: 로사톰은 10월 10일 ICC 중재판정부가 펜노보이마의 2022년 한히키비-1 계약 해지를 불법으로 판단했다고 밝혔다 [사실]",
  "지급: 판정은 로사톰 자회사들이 펜노보이마에 순차액을 지급해야 한다고 인정했고, 펜노보이마는 자신이 낼 순지급액은 없다고 밝혔다 [사실]",
  "미공개: 판정문은 공개되지 않았고 ICC는 논평하지 않았으며, 리하초프 사장은 최종 승리가 아니라며 추가 소송을 예고했다 [사실]"],
 "basis": "verified",
 "check": "10월 10일 ICC 판정에 대한 로사톰 발표와 순차액 지급 인정, 양측 승리 주장은 검색 결과 요약으로 확인. 판정문은 비공개",
 "src": [{"o": "The Moscow Times", "d": "2026-10-10", "u": "https://www.themoscowtimes.com/2026/10/10/rosatom-says-it-wins-tribunal-ruling-in-finnish-nuclear-plant-dispute-a93939"},
         {"o": "Energynews.pro", "d": "2026-10", "u": "https://energynews.pro/en/hanhikivi-icc-rules-termination-unlawful-but-orders-rosatom-subsidiaries-to-pay-net-sum"}],
 "inds": ["uranium"], "nodes": ["uranium/build", "uranium/policy"],
 "items": [
  it("로사톰 \"핀란드 원전 분쟁 중재판정에서 승소했다\"", "로이터", "2026-10-11", "https://www.reuters.com/business/energy/rosatom-says-it-wins-tribunal-ruling-finnish-nuclear-plant-dispute-2026-10-10/"),
 ]})

B.append({"cid": "C151", "attachTo": "",
 "title": "{{북유럽}}, 러시아 위협에 국방비 늘리고 징병 확대",
 "one": "{{북유럽 국가들}}이 러시아 위협과 미국 안보 지원 불확실성에 국방비를 늘리고 {{스웨덴 징집 인원}}을 9,000명으로, 덴마크 복무를 11개월로 늘리면서, {{방산·결제망 자립}}에 돈을 쏟고 있다 (채널 전언)",
 "facts": [
  "무엇이: 지난해 덴마크·노르웨이의 GDP 대비 국방비 비중이 미국을 웃돌았다는 WSJ 보도를 채널이 전했다 [채널]",
  "징병: 스웨덴은 올해 징집 인원을 9,000명으로 2018년 3,500명보다 늘렸고, 덴마크는 여성도 징집하며 복무를 4개월에서 11개월로 늘렸다 [채널]",
  "자립: 덴마크는 우크라이나 기술로 드론 생산을 키우고, 스웨덴은 미국 카드망을 우회하는 스위시 오프라인 결제를 추진한다 [채널]",
  "부담: 덴마크 중앙은행은 국방 지출 확대가 다른 분야의 지출 여력을 줄인다고 경고했다 [채널]"],
 "basis": "channel",
 "check": "검색 한도로 독립 확인 안 함. WSJ 기사를 요약한 채널 글에만 근거",
 "src": [],
 "inds": ["macro"], "nodes": ["macro/geo", "macro/fiscal"],
 "items": [
  it("WSJ \"북유럽, 국방비 확대·징병 강화로 위험한 세계에 대응\"", TP+"상상인 김진범", "2026-10-11", "https://t.me/PipeBeom/6657"),
 ]})

B.append({"cid": "C159", "attachTo": "n-bbg-0070",
 "title": "리사 수 \"AMD {{공급 훨씬 더 필요}}\"…서버 CPU 부족 장기화 시각",
 "one": "{{리사 수}} AMD CEO가 대만·한국 방문에서 삼성·SK하이닉스에 장기 협력을 제안한 데 이어 공급이 훨씬 더 필요하다고 인정한 것으로 전해지면서, 에이전틱 AI발 {{서버 CPU 공급 부족}}이 길어져 {{인텔·AMD}}의 가격 결정력이 커질 수 있다 (채널 전언)",
 "facts": [
  "무엇이: 리사 수 CEO가 10월 대만·한국 방문에서 AMD에 훨씬 더 많은 공급이 필요하다고 처음 인정했다고 전해졌다 [채널]",
  "공급: TSMC는 신주 Fab 20·가오슝 Fab 22 등 2nm 팹 5곳을 동시에 늘리고 있고, 초기 생산능력은 3nm 같은 시점보다 약 45% 높다는 분석이다 [채널]",
  "영향: CPU 부족이 이어지면 인텔·AMD 모두 가격 결정력이 커지고 물량 확보용 장기계약이 늘 수 있다는 관측이다 [추론]",
  "기존: 리사 수는 10월 7일 방한해 삼성·SK하이닉스에 3~5년 이상 협력을 제안하고 SK하이닉스 HBM4 채택을 밝혔다 [사실]"],
 "basis": "channel",
 "check": "검색 한도로 이번 글의 '공급 훨씬 더 필요' 발언과 TSMC 2nm 증설 수치는 독립 확인 못 함. 방한 내용은 기존 문서 근거",
 "src": [],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "added": "이번 텔레그램 1건으로 리사 수가 AMD의 {{공급 부족}}을 인정했다는 전언과 {{TSMC 2nm 팹 5곳}} 동시 증설 현황이 기존 방한 협력 소식에 추가됐다",
 "items": [
  it("리사 수 \"AMD 공급 훨씬 더 필요\"…CPU 공급 부족 장기화 시각 부각", TP+"나쁜양파", "2026-10-11", "https://t.me/Badonions/7743",
     "{{리사 수}}가 AMD에 공급이 훨씬 더 필요하다고 인정한 것으로 전해지면서, GPU에 이어 {{서버 CPU}}까지 공급 부족이 길어질 수 있다는 시각이 부각됐다"),
 ]})

B.append({"cid": "C175", "attachTo": "",
 "title": "호주 경쟁당국, {{서니퀸 등 계란업체 12곳}} 담합 혐의로 제소",
 "one": "{{호주 경쟁소비자위원회}}가 서니퀸 등 {{계란 생산·공급업체 12곳}}이 2020년부터 생산량·출하·살처분을 조율했다며 연방법원에 제소하면서, 업체들이 {{과징금}}과 금지명령을 받을 수 있다",
 "facts": [
  "무엇이: 호주 경쟁소비자위원회(ACCC)는 10월 13일 서니퀸 등 계란 생산·공급업체 12곳을 상대로 연방법원에 민사소송을 냈다 [사실]",
  "혐의: 적어도 2020년 10월부터 공급 과잉을 관리하려고 생산량·유통·확장 계획·살처분을 조율했다는 혐의다 [사실]",
  "경쟁 제한: 서니퀸이 경쟁사 킨로스의 판매량을 제한하고 콜스·울워스 등 대형 유통사 납품을 막았다는 혐의도 있다 [사실]",
  "대응: 2017년 도입된 공동행위 금지 조항을 적용한 첫 사건이며, 서니퀸은 모든 혐의를 부인했다 [사실]"],
 "basis": "verified",
 "check": "ACCC의 10월 13일 제소, 12개 업체, 혐의 내용, 서니퀸 부인은 검색 결과 요약으로 확인",
 "src": [{"o": "ABC News", "d": "2026-10-13", "u": "https://www.abc.net.au/news/2026-10-13/accc-consumer-watchdog-court-egg-cartel-sunny-queen/107260004"},
         {"o": "Inside FMCG", "d": "2026-10-13", "u": "https://insidefmcg.com.au/2026/10/13/sunny-queen-11-other-egg-producers-sued-for-alleged-collusion/"}],
 "inds": ["agri"], "nodes": [],
 "items": [
  it("호주 주요 계란 생산업체들, 반경쟁 행위 혐의로 고발당해", "블룸버그", "2026-10-13", "https://www.bloomberg.com/news/articles/2026-10-13/top-australian-egg-producers-accused-of-anti-competitive-conduct"),
 ]})

B.append({"cid": "C192", "attachTo": "n-rtr-0021",
 "title": "{{우간다 외환보유고 56% 급증}}…실링 약세 속 67억 달러",
 "one": "{{우간다 중앙은행}}이 6월까지 1년간 외환보유고가 {{56%}} 늘어 약 67억 달러에 이르렀다고 밝혔지만 실링은 현지 채권 기피로 최약세 통화가 되고 콩고가 프랑 결제 의무화에 나서면서, {{아프리카 통화}} 정책 부담이 이어지고 있다",
 "facts": [
  "무엇이: 우간다 중앙은행은 6월까지 1년간 외환보유고가 56% 늘어 약 67억 달러가 됐다고 밝혔다 [사실]",
  "한계: 보유고는 수입 3.7개월분으로 중앙은행 목표인 4개월에 못 미치며, 실링은 사상 최저 수준으로 밀렸다 [사실]",
  "실링: 투자자들의 현지 채권 기피로 우간다 실링이 가장 부진한 통화가 됐다 [제목]",
  "기존: 케냐 중앙은행은 10월 7일 기준금리를 8.75%로 동결했고, 콩고는 프랑화 결제 의무화를 계획한다 [제목]"],
 "basis": "verified",
 "check": "외환보유고 56% 증가·약 67억 달러·수입 3.7개월분은 검색 결과 요약으로 확인(56%는 Finimize 보도, 6월 보유고 수준은 통계 사이트와 일치). 실링 최약세와 콩고 계획은 제목 근거",
 "src": [{"o": "Finimize", "d": "2026-10-13", "u": "https://finimize.com/content/ugandas-fx-reserves-jumped-56-as-the-shilling-slid"},
         {"o": "Trading Economics", "d": "2026-10", "u": "https://tradingeconomics.com/uganda/foreign-exchange-reserves"}],
 "inds": ["macro"], "nodes": ["macro/fx"],
 "added": "이번 로이터 1건으로 {{우간다 외환보유고}}가 6월까지 1년간 56% 늘어 약 67억 달러에 이르렀지만 {{수입 3.7개월분}}으로 목표에 못 미친다는 사실이 추가됐다",
 "items": [
  it("우간다 중앙은행 \"6월까지 1년간 외환보유고 56% 급증\"", "로이터", "2026-10-13", "https://www.reuters.com/world/africa/ugandas-fx-reserves-surged-56-year-ended-june-central-bank-says-2026-10-13/",
     "{{우간다 중앙은행}}이 6월까지 1년간 외환보유고가 {{56%}} 급증했다고 밝히면서, 실링 약세 속에도 대외 완충 여력이 커졌다"),
 ]})

skipped = [
 {"cid": "C085", "reason": "범위 밖(미국 규제 가정 시나리오와 종목 나열뿐, 새 구체 사실 없음)"},
 {"cid": "C119", "reason": "이미 다룸(n-bbg-0259)"},
 {"cid": "C167", "reason": "이미 다룸(n-rtr-0062)"},
 {"cid": "C184", "reason": "범위 밖(유로 가입 가능성 해설 기사 제목뿐, 구체 사실 없음)"},
]

d = {"agent": "W1", "searches_used": 16, "fetches_used": 0, "items": B, "skipped": skipped}

# checks
def L(x):
    return len(re.sub(r' \((제목 기준|채널 전언)\)$', '', x).replace('{{', '').replace('}}', ''))
def hl(x):
    return re.findall(r'\{\{(.*?)\}\}', x)
bad = []
for b in B:
    multi = len(b['items']) > 1 or b['attachTo']
    lo, hi = (90, 160) if multi else (80, 130)
    if not (20 <= L(b['title']) <= 50) or not (1 <= len(hl(b['title'])) <= 2): bad.append((b['cid'], 'title', L(b['title']), len(hl(b['title']))))
    if not (lo <= L(b['one']) <= hi) or not (2 <= len(hl(b['one'])) <= 4): bad.append((b['cid'], 'one', L(b['one']), len(hl(b['one']))))
    for h in hl(b['title']) + hl(b['one']) + hl(b.get('added', '')) + sum([hl(i.get('s', '')) for i in b['items']], []):
        if not (2 <= len(h) <= 20): bad.append((b['cid'], 'hl', h))
    if not (2 <= len(b['facts']) <= 5): bad.append((b['cid'], 'nfacts'))
    for f in b['facts']:
        if '{{' in f or '|' in f or '**' in f: bad.append((b['cid'], 'fact char'))
    if multi:
        a = b.get('added', '')
        if not (60 <= L(a) <= 140) or not (1 <= len(hl(a)) <= 3): bad.append((b['cid'], 'added', L(a), len(hl(a))))
        for i in b['items']:
            s = i.get('s', '')
            if not (45 <= L(s) <= 110) or not (1 <= len(hl(s)) <= 2) or not s.rstrip(' (제목 기준)').endswith('다'): bad.append((b['cid'], 's', L(s), len(hl(s)), s[:30]))
    else:
        if 'added' in b or any('s' in i for i in b['items']): bad.append((b['cid'], 'single has s/added'))
    for i in b['items']:
        if not (25 <= len(i['t']) <= 60): bad.append((b['cid'], 't', len(i['t']), i['t']))
    ds = [i['d'] for i in b['items']]
    if ds != sorted(ds): bad.append((b['cid'], 'order'))
print('BAD:', *bad, sep='\n')
json.dump(d, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('saved', len(B))
