import json, re

BB = "블룸버그"; RT = "로이터"
TR = "텔레그램 트릴리온"; INS = "텔레그램 미국 주식 인사이더"; POL = "텔레그램 Polaristimes"; HANA = "텔레그램 하나증권 중국전략"

def it(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s is not None:
        x["s"] = s
    return x

items = []

# G1-006
items.append({
 "cid": "G1-006", "attachTo": "n-rtr-0181",
 "title": "MSCI 경고 확산…인니 벌금·튀르키예 증시 급락, 스트래티지도 퇴출 위기",
 "one": "MSCI가 인도네시아 강등 경고와 튀르키예 지수 변경 동결에 이어 비영업 기업을 지수에서 빼는 규칙을 확정하면서, 인니 당국이 1억 1,700만 달러 벌금을 내고 튀르키예 증시가 3% 넘게 빠졌으며 스트래티지는 약 28억 달러 패시브 매도 위험에 놓였다",
 "facts": [
  "무엇이: MSCI는 10월 15일 투자회사처럼 움직이는 비영업 기업을 11월 30일 장 마감 뒤 글로벌 투자가능지수에서 빼는 규칙을 확정했고, 스트래티지·메타플래닛이 삭제 후보에 올랐으며 최종 명단은 11월 11일 나온다 [사실]",
  "스트래티지: JP모건은 편출 시 패시브 펀드에서 약 28억 달러 매도가 나올 수 있다고 봤고, 스트래티지 주가는 16일 한때 4.2% 떨어졌다 [사실]",
  "인도네시아: MSCI 경고 뒤 당국이 1억 1,700만 달러 벌금을 발표했고, 루피아 압박 속에 금리 인상 베팅이 커졌다 [제목]",
  "튀르키예: MSCI의 일부 지수 변경 동결 뒤 튀르키예 증시가 3% 넘게 떨어졌다 [제목]",
  "기존: 자카르타종합지수는 10월 16일 한때 11% 넘게 빠져 1998년 1월 이후 최대 하루 낙폭을 향했고, 루피아는 달러당 18,070까지 밀렸다 [사실]"
 ],
 "basis": "partial",
 "check": "스트래티지 편출 규칙·일정·약 28억 달러 패시브 매도 추정·주가 4.2% 하락은 검색 결과 요약으로 확인. 인니 벌금 1억 1,700만 달러·금리 인상 베팅·튀르키예 증시 3% 하락은 제목 기준으로 독립 출처 확인 못 함",
 "src": [
  {"o": "Invezz", "d": "2026-10-16", "u": "https://invezz.com/news/2026/10/16/strategy-stock-mstr-falls-as-msci-index-exclusion-threatens-passive-investments/"},
  {"o": "Cryptopolitan", "d": "2026-10-16", "u": "https://www.cryptopolitan.com/msci-rules-could-eject-strategy-metaplanet/"}
 ],
 "inds": ["fin", "macro"], "nodes": ["macro/liquidity"],
 "vc": [
  {"ind": "macro", "node": "liquidity", "f": "공급", "dir": "down", "k": "실제", "t": "MSCI 경고에 인니·튀르키예 증시 자금 이탈"},
  {"ind": "fin", "node": "payments", "f": "수요", "dir": "down", "k": "예상", "t": "MSCI 편출 시 스트래티지 패시브 매도 약 28억 달러"}
 ],
 "added": "이번 블룸버그·로이터·텔레그램 8건으로 인니 당국의 1억 1,700만 달러 벌금, 튀르키예 증시 3% 넘는 하락, MSCI 새 규칙에 따른 스트래티지 편출 위험이 추가됐다",
 "items": [
  it("인도네시아, 예상 밖 MSCI 강등 경고에 허를 찔려", BB, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-16/indonesia-caught-off-guard-by-surprise-msci-downgrade-warning",
     "MSCI가 예고 없이 강등 경고를 내놓으면서 인도네시아 정부와 시장이 대응 준비 없이 충격을 받았다 (제목 기준)"),
  it("MSCI 경보에 루피아 압박…인도네시아 금리 인상 베팅 커져", BB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/indonesia-rate-hike-bets-grow-as-msci-alarm-pressures-rupiah",
     "MSCI 경보가 루피아를 짓누르면서 인도네시아 중앙은행이 금리를 올릴 것이라는 시장 베팅이 커졌다 (제목 기준)"),
  it("수개월 경고 끝에 MSCI가 인도네시아 시장 심판에 불붙여", BB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/msci-ignites-indonesia-market-reckoning-after-months-of-warnings",
     "수개월 이어진 경고 끝에 MSCI가 행동에 나서면서 인도네시아 증시의 구조 문제가 한꺼번에 드러나고 있다 (제목 기준)"),
  it("인도네시아, MSCI 경고 뒤 1억 1,700만 달러 벌금 발표", BB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/indonesia-unveils-117-million-in-fines-after-msci-warning",
     "인도네시아 당국이 MSCI 경고 직후 1억 1,700만 달러 규모의 벌금을 발표하면서 시장 규율 강화에 나섰다 (제목 기준)"),
  it("MSCI의 일부 지수 변경 동결에 튀르키예 증시 3% 넘게 하락", RT, "2026-10-16", "https://www.reuters.com/world/middle-east/turkish-stocks-drop-more-than-3-after-msci-freezes-certain-index-changes-2026-10-16/",
     "MSCI가 튀르키예 지수의 일부 변경을 동결하면서 튀르키예 증시가 하루 새 3% 넘게 떨어졌다 (제목 기준)"),
  it("인도네시아, 글로벌 자본 끊길 수 있는 이례적 MSCI 제외 위기", RT, "2026-10-17", "https://www.reuters.com/world/asia-pacific/indonesia-faces-rare-msci-exclusion-that-could-cut-it-off-global-capital-2026-10-16/",
     "MSCI 지수 제외라는 드문 조치가 거론되면서 인도네시아가 글로벌 지수 자금에서 끊길 위험에 놓였다 (제목 기준)"),
  it("주가조작 스캔들에 튀르키예 기업들 글로벌 지수 제외 위기", TR, "2026-10-17", "https://t.me/Trillion_labs/10681",
     "MSCI가 유동주식 안정성 우려로 튀르키예 지수 변경을 동결하고 2027년 6월까지 진전이 없으면 강등 협의를 하겠다고 하면서, 튀르키예 기업들이 지수에서 빠질 위기에 놓였다"),
  it("스트래티지, 새 규칙에 MSCI 퇴출 위기…수십억 달러 패시브 보유분 위험", RT, "2026-10-17", "https://www.reuters.com/world/asia-pacific/strategy-faces-msci-ouster-under-new-rules-billions-passive-holdings-risk-2026-10-16/",
     "MSCI가 비영업 기업을 11월 30일 이후 지수에서 빼는 규칙을 확정하면서 스트래티지가 약 28억 달러 패시브 매도 위험에 놓였다")
 ]})

# G1-010
items.append({
 "cid": "G1-010", "attachTo": "n-rtr-0201",
 "title": "유럽 가스값 두 배에 EU 정상회의 격론…이탈리아 가스 부담 완화 합의, 석탄발전 횡재",
 "one": "유럽 가스값이 연초보다 두 배 넘게 오르면서 EU 정상회의에서 배출권거래제 완화를 두고 격론이 벌어지고 이탈리아가 집행위와 가스값의 전기요금 전가를 줄이는 조치에 원칙 합의했으며, 남은 석탄발전소는 가스 급등의 횡재를 누리고 있다",
 "facts": [
  "무엇이: 이탈리아는 집행위와 가스값이 전기요금에 번지는 것을 줄이는 조치에 원칙 합의했고, 국가보조 규정에 맞는다며 정식 통보하기로 했지만 최종 승인은 아니다 [사실]",
  "쟁점: 이탈리아·폴란드·헝가리·슬로바키아·체코 등은 배출권거래제를 완화하고 건물·운송 적용을 2028년에서 2030년으로 미루자고 했고, 독일·프랑스·스페인·북유럽은 가격 신호 약화에 반대했다 [채널]",
  "배경: 유럽 가스값은 주로 미국·이스라엘의 이란 전쟁 탓에 연초보다 두 배 넘게 올랐다 [채널]",
  "석탄: 가스값 급등에 유럽의 줄어든 석탄발전소들이 횡재를 누리고 있다 [제목]",
  "기존: 영국 오프젬은 공급사를 도매가 급변동에서 보호할 시장안정 부담금을 이르면 11월 재가동하는 방안을 협의하고 있다 [사실]"
 ],
 "basis": "partial",
 "check": "이탈리아·EU 원칙 합의와 정식 통보 절차는 검색 결과 요약으로 확인(상한 방식·수준은 보도마다 달라 쓰지 않음). ETS 완화 논쟁·가스값 두 배는 채널 전언, 석탄발전 횡재·영국 재생에너지 우위는 제목 기준",
 "src": [
  {"o": "Montel News", "d": "2026-10-16", "u": "https://montelnews.com/news/4b1e7e0f-fb2e-4e2e-9e90-97ca48851020/ec-italy-near-power-market-reform-deal-to-curb-gas-costs"},
  {"o": "Eunews", "d": "2026-10-14", "u": "https://www.eunews.it/en/2026/10/14/brussels-is-open-to-melonis-energy-bill-decree-broad-agreement-reached-between-italy-and-the-eu-technical-issues-remain/"},
  {"o": "Il Sole 24 Ore", "d": "2026-10-16", "u": "https://en.ilsole24ore.com/art/electricity-prices-the-eu-italia-agreement-ets-neutralisation-AJqKpejB"}
 ],
 "inds": ["power", "gas", "coal"], "nodes": ["power/market", "gas/trade", "coal/power"],
 "vc": [
  {"ind": "gas", "node": "trade", "f": "가격", "dir": "up", "k": "실제", "t": "유럽 가스값 연초 대비 두 배 넘게 상승"},
  {"ind": "power", "node": "market", "f": "가격", "dir": "down", "k": "예상", "t": "이탈리아·EU, 가스값의 전기요금 전가 억제 합의"},
  {"ind": "coal", "node": "power", "f": "수요", "dir": "up", "k": "실제", "t": "가스값 급등에 유럽 석탄발전 횡재"}
 ],
 "added": "이번 블룸버그·로이터·텔레그램 5건으로 이탈리아·EU의 가스값 전가 억제 원칙 합의, 정상회의의 배출권거래제 완화 격론, 석탄발전 횡재가 추가됐다",
 "items": [
  it("가스값 급등에 유럽의 줄어든 석탄발전소들이 횡재", BB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/dwindling-coal-fleet-in-europe-reaps-windfall-from-gas-rally",
     "유럽 가스값이 치솟으면서 줄어든 석탄발전소들이 전력 판매에서 큰 이익을 거두고 있다 (제목 기준)"),
  it("EU, 이탈리아 주도 배출권거래제 완화 시도에 저항…정상회의 에너지값 격론", TR, "2026-10-16", "https://t.me/Trillion_labs/10631",
     "이탈리아 등 5개국이 배출권거래제 완화와 건물·운송 적용 연기를 밀었지만 독일·프랑스 등이 가격 신호 약화에 반대하면서, EU 기후정책 후퇴 여부가 쟁점이 됐다"),
  it("에너지 가격 부담, EU 정상회의 전반을 짓눌러", RT, "2026-10-16", "https://www.reuters.com/sustainability/energy-prices-loom-over-eu-summit-2026-10-16/",
     "에너지 가격 부담이 EU 정상회의 전반을 짓누르면서 정상들이 가계·기업 비용 대책 마련 압박을 받았다 (제목 기준)"),
  it("이탈리아, 가스값의 전기요금 영향 줄이는 조치로 EU와 합의", RT, "2026-10-17", "https://www.reuters.com/business/italy-clinches-deal-with-eu-over-measures-limit-impact-gas-prices-electricity-2026-10-16/",
     "이탈리아가 발전용 가스값이 전기요금에 번지는 것을 막는 조치에 집행위와 원칙 합의하면서, 정식 통보 뒤 우선 심사를 받게 됐다"),
  it("겨울 대비하는 유럽 속 영국은 재생에너지 우위", BB, "2026-10-17", "https://www.bloomberg.com/news/newsletters/2026-10-16/britain-has-a-renewable-energy-edge-as-europe-braces-for-winter",
     "유럽이 겨울 에너지 부담에 대비하는 가운데 영국은 재생에너지 덕에 상대적으로 유리한 위치에 있다 (제목 기준)")
 ]})

# G1-013
items.append({
 "cid": "G1-013", "attachTo": "n-bbg-0317",
 "title": "美 열연 톤당 1,255달러 4년 최고…캐나다는 스텔코 국유화 검토",
 "one": "트럼프 관세로 미국 열연코일 가격이 1년 새 52% 올라 숏톤당 1,255달러로 2022년 5월 이후 최고를 찍은 가운데 캐나다 정부가 감원을 강행하는 스텔코의 국유화까지 검토하면서, 클리블랜드클리프스의 캐나다 자산이 강제 매각 압박을 받고 있다",
 "facts": [
  "무엇이: 미국 열연코일 가격이 10월 16일 숏톤당 1,255달러로 1년 새 52% 올라 2022년 5월 이후 최고를 기록했다 [사실]",
  "수입·공급: 섹션 232 관세는 2025년 3월 25%에서 6월 50%로 올랐고 1~9월 완제 철강 수입은 약 14% 줄었으며, 9~12월 정비로 100만 톤 넘는 생산이 빠질 전망이다 [사실]",
  "캐나다: 졸리 산업장관은 투자캐나다법 40조의 법원 절차를 통한 스텔코 국유화를 포함해 모든 방안을 검토한다고 했고, 곤살베스 클리블랜드클리프스 CEO는 국유화 구상을 일축했다 [사실]",
  "내수: 캐나다 철강사들은 국내 수요로 미국 관세 타격을 일부 상쇄하고 있다 [제목]",
  "기존: 스텔코는 미국 관세를 이유로 해밀턴 공장 냉연·도금 공정을 무기한 멈춰 최대 500명이 영향을 받는다 [사실]"
 ],
 "basis": "verified",
 "check": "열연 1,255달러·52%·관세·수입 감소·정비 감산 전망은 검색 결과 요약(쿼츠·서울경제)으로 확인, 스텔코 국유화 검토와 곤살베스 반응은 검색 결과 요약(글로브앤메일·CBC)으로 확인. 캐나다 철강사 내수 상쇄는 제목 기준",
 "src": [
  {"o": "Quartz", "d": "2026-10-16", "u": "https://qz.com/us-steel-prices-four-year-high-tariffs-imports-101626"},
  {"o": "서울경제", "d": "2026-10-17", "u": "https://en.sedaily.com/international/2026/10/17/us-steel-prices-hit-four-year-high-on-trump-tariffs"},
  {"o": "The Globe and Mail", "d": "2026-10-16", "u": "https://www.theglobeandmail.com/business/article-cleveland-cliffs-dismisses-nationalizing-stelco-ottawa-jobs/"},
  {"o": "CBC", "d": "2026-10-16", "u": "https://www.cbc.ca/news/canada/hamilton/stelco-nationalize-9.7376461"}
 ],
 "inds": ["metals"], "nodes": [],
 "vc": [
  {"ind": "metals", "node": "steel", "f": "가격", "dir": "up", "k": "실제", "t": "관세에 美 열연 톤당 1,255달러 4년 최고"},
  {"ind": "metals", "node": "steel", "f": "공급", "dir": "down", "k": "예상", "t": "정비로 美 철강 100만 톤 넘는 생산 감소 전망"}
 ],
 "added": "이번 블룸버그·로이터·텔레그램 5건으로 미국 열연 가격 4년 최고와 캐나다 정부의 스텔코 국유화 검토, 캐나다 철강사의 내수 상쇄가 추가됐다",
 "items": [
  it("트럼프 관세 효과에 미국 철강 가격 4년 만의 최고", BB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/us-steel-prices-climb-to-four-year-high-as-trump-s-tariffs-bite",
     "트럼프 관세가 수입을 막으면서 미국 철강 가격이 4년 만의 최고로 올라 미국 제조업체의 원가 부담이 커졌다"),
  it("캐나다 철강사, 내수로 미국 관세 타격 일부 상쇄", RT, "2026-10-16", "https://www.reuters.com/business/canadian-steelmakers-offset-some-us-tariff-pain-with-domestic-demand-2026-10-16/",
     "캐나다 철강사들이 국내 수요로 판로를 돌리면서 미국 관세로 잃은 물량 일부를 메우고 있다 (제목 기준)"),
  it("美 열연 톤당 1,255달러로 1년 새 52% 올라 2022년 5월 이후 최고", TR, "2026-10-17", "https://t.me/Trillion_labs/10648",
     "관세로 미국 열연코일 가격이 1년 새 52% 올라 톤당 1,255달러가 되면서, 미국 생산업체엔 호재지만 제조업체 생산비는 올랐다"),
  it("캐나다 산업장관 '스텔코 국유화 방안 검토 중'", RT, "2026-10-17", "https://www.reuters.com/business/canada-exploring-stelco-nationalization-industry-minister-says-2026-10-16/",
     "졸리 산업장관이 투자캐나다법상 법원 절차를 통한 스텔코 국유화를 검토한다고 하면서 클리블랜드클리프스와의 감원 다툼이 커졌다"),
  it("클리블랜드클리프스, 스텔코 감원 문제로 강제 매각 위협 직면", BB, "2026-10-17", "https://www.bloomberg.com/news/newsletters/2026-10-16/cleveland-cliffs-faces-forced-sale-threat-over-stelco-layoffs",
     "캐나다 정부가 스텔코 감원을 문제 삼아 강제 매각까지 거론하면서 클리블랜드클리프스가 캐나다 자산을 잃을 위험에 놓였다")
 ]})

# G1-019
items.append({
 "cid": "G1-019", "attachTo": "n-bbg-0111",
 "title": "IMF '佛 금리 상승 아직 감당 가능'…정치 위기가 부채 위기로 번질 우려",
 "one": "프랑스 정치 위기가 부채 위기로 번진다는 우려 속에 IMF가 국채 금리 상승은 지금은 감당 가능하지만 금리가 높게 머물면 2027년 예산을 넘는 중기 재정 건전화 계획이 필요하다고 하면서, 프랑스 예산 협상에 대한 압박이 커질 수 있다",
 "facts": [
  "무엇이: IMF 유럽국장 마테우시 슈체레크는 프랑스 차입 비용 상승이 단기적으로 감당 가능하지만, 금리가 높게 유지되면 2027년 예산을 넘는 신뢰할 만한 중기 건전화 계획이 필요하다고 했다 [사실]",
  "근거: 그는 시장 유동성, 긴 만기 구조, 다양한 투자자층, 높은 은행 유동성을 단기 위험이 제한된 이유로 들었다 [사실]",
  "시장: 프랑스 10년물 금리는 10월 16일 4.82%로 10월 초 5% 가까이에서 내려왔고, 독일 국채와의 금리차는 약 137bp다 [사실]",
  "시각: 블룸버그는 정치 위기가 부채 위기로 번지고 있다고 짚었고, 사모 자본은 위기의 프랑스에 여전히 신뢰를 보인다고 전했다 [제목]",
  "기존: 레스퀴르 재무장관은 시장이 더 비싼 값에 프랑스에 돈을 빌려준다며 경고 신호라고 했고, 국가부채는 6월 말 GDP의 119%로 사상 최대다 [사실]"
 ],
 "basis": "partial",
 "check": "IMF 슈체레크 발언은 로이터 전재 기사 검색 결과 요약으로만 보여 독립 출처는 확인 못 함, 10년물 4.82%·금리차 137bp는 트레이딩이코노믹스 검색 결과 요약으로 확인. 부채 위기·사모 자본·시위 관련 블룸버그 3건은 제목 기준",
 "src": [
  {"o": "Trading Economics", "d": "2026-10-16", "u": "https://tradingeconomics.com/france/government-bond-yield"},
  {"o": "CNBC", "d": "2026-10-15", "u": "https://www.cnbc.com/amp/2026/10/15/france-budget-deficit-moulin-protests.html"}
 ],
 "inds": ["macro"], "nodes": ["macro/fiscal", "macro/rates"],
 "vc": [
  {"ind": "macro", "node": "rates", "f": "가격", "dir": "up", "k": "실제", "t": "정치 위기에 프랑스 10년물 4.8%대로 상승"},
  {"ind": "macro", "node": "fiscal", "f": "수요", "dir": "down", "k": "예상", "t": "IMF, 佛 중기 재정 건전화 압박 커질 수 있다 경고"}
 ],
 "added": "이번 블룸버그·로이터 4건으로 IMF의 금리 상승은 감당 가능하나 건전화 압박이 커질 수 있다는 평가와 사모 자본의 프랑스 신뢰가 추가됐다",
 "items": [
  it("프랑스 정치 위기, 국가 부채 위기로 번지는 중", BB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/the-french-political-crisis-that-s-turning-into-a-debt-crisis",
     "프랑스의 정치 교착이 길어지면서 국채 시장 부담이 커져 정치 위기가 부채 위기로 번지고 있다 (제목 기준)"),
  it("IMF '佛 국채 금리 상승 지금은 감당 가능, 건전화 압박 커질 수도'", RT, "2026-10-16", "https://www.reuters.com/business/rise-french-yields-is-manageable-now-consolidation-pressure-might-grow-imf-says-2026-10-16/",
     "IMF가 프랑스 금리 상승은 시장 유동성과 긴 만기 구조 덕에 당장은 감당 가능하지만 금리가 높게 머물면 중기 건전화 계획이 필요하다고 했다"),
  it("사모 자본, 위기에 빠진 프랑스에 여전히 신뢰 유지", BB, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-16/private-capital-keeps-faith-in-crisis-hit-france",
     "정치·재정 위기에도 사모 자본이 프랑스 투자를 이어가면서 민간 자금 흐름은 아직 흔들리지 않고 있다 (제목 기준)"),
  it("프랑스 시위와 '돈으로 달래는 정치' 시대의 종말", BB, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-16/french-protests-and-the-end-of-checkbook-politics",
     "재정 여력이 줄면서 프랑스 정부가 시위를 재정 지출로 달래던 방식이 더는 통하지 않게 됐다 (제목 기준)")
 ]})

# G1-025 fed
items.append({
 "cid": "G1-025", "attachTo": "",
 "title": "워시 '회의별 결정 예단 안 해'…가이던스 없자 연준 동결 베팅 커져",
 "one": "워시 연준 의장이 IMF 대담에서 남은 회의 결정을 예단하지 않겠다며 포워드 가이던스를 내놓지 않고 AI가 공급보다 수요에 먼저 작용한다고 말하면서, 시장에서는 연준이 금리를 동결할 것이라는 베팅이 커졌다",
 "facts": [
  "무엇이: 워시 의장은 IMF·세계은행 연차총회 대담에서 물가 안정을 이루겠다면서도 회의별 결정을 예단하지 않겠다고 했다 [사실]",
  "시장: 블룸버그는 워시가 하지 않은 말이 연준 금리 동결 베팅을 키웠다고 전했다 [제목]",
  "AI: 워시는 AI가 경제의 공급 측보다 수요 측에 먼저 작용할 것이라 했고, 연준이 한 달 뒤 샌프란시스코에서 AI 청문회를 연다고 했다 [채널]",
  "조직: 워시는 연준 직원의 약 75%가 통화정책을 다루지 않는다고 했고, 볼커·그린스펀·버냉키가 연준에 제도적 신뢰를 더한 것을 자랑스럽게 여긴다고 했다 [사실]",
  "금융 안정: 워시는 금융위기의 상처를 언급하면서도 연준이 정책당국이 대응할 수 있는 꼬리 위험과 금융 안정 위험을 생각해야 한다고 했다 [채널]"
 ],
 "basis": "partial",
 "check": "회의 예단 안 함·직원 75%·볼커 등 전임 의장 언급·금융위기 상처 표현은 검색 결과 요약으로 확인. AI 청문회·꼬리 위험 발언은 채널 전언, 동결 베팅은 제목 기준. 같은 대담은 n-bbg-0311에서 이미 다뤘고 이번 묶음은 조직·전임 의장 언급 등 세부를 더함",
 "src": [
  {"o": "The Nation Thailand", "d": "2026-10-16", "u": "https://www.nationthailand.com/business/economy/40072363"}
 ],
 "inds": ["macro"], "nodes": ["macro/cb"],
 "vc": [
  {"ind": "macro", "node": "cb", "f": "-", "dir": "flat", "k": "예상", "t": "워시 가이던스 없어 연준 동결 베팅 확대"}
 ],
 "fed": [
  {"k": "", "who": "연준", "role": "워시 발언 뒤 시장 반응", "kind": "관련 뉴스", "stance": "", "t": "워시가 금리 경로 단서를 주지 않자 연준 동결 베팅이 커졌다", "d": "2026-10-16", "u": "https://www.bloomberg.com/news/newsletters/2026-10-16/warsh-s-missing-words-fuel-bets-fed-will-hold-rates"},
  {"k": "Warsh", "who": "케빈 워시", "role": "연준 의장", "kind": "발언", "stance": "중립", "t": "남은 회의 결정을 예단하지 않겠다며 AI는 수요에 먼저 작용한다고 했다", "d": "2026-10-16", "u": "https://t.me/insidertracking/66454"}
 ],
 "added": "이번 폴라리스타임스 글로 워시의 금융위기 상처 언급, 연준 직원 75%의 비통화정책 업무, 한 달 뒤 AI 청문회, 꼬리 위험 대비 발언이 추가됐다",
 "items": [
  it("워시가 하지 않은 말, 연준 금리 동결 베팅 키워", BB, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-16/warsh-s-missing-words-fuel-bets-fed-will-hold-rates",
     "워시 의장이 향후 금리 경로에 대한 단서를 내놓지 않으면서 연준이 금리를 동결할 것이라는 시장 베팅이 커졌다 (제목 기준)"),
  it("글로벌 브리핑: 워시 '남은 FOMC 결정 예측에 회의적'", INS, "2026-10-16", "https://t.me/insidertracking/66454",
     "워시 의장이 남은 FOMC 회의 결정을 미리 예측하는 데 회의적이라고 하면서 통화정책 사전 확약을 경계하는 신중한 태도를 드러냈다"),
  it("워시 'AI는 수요 측에 먼저 작용…연준, 한 달 뒤 AI 청문회'", POL, "2026-10-16", "https://t.me/The_MariTimes/63748",
     "워시 의장이 회의별 결정을 예단하지 않으면서 AI가 수요에 먼저 작용하고 연준이 꼬리 위험을 생각해야 한다고 해, 가이던스 없는 기조를 이어갔다")
 ]})

# G1-031
items.append({
 "cid": "G1-031", "attachTo": "n-rtr-0349",
 "title": "메르츠 '내연차 금지는 과거 일'…佛·獨, 2035년 90% 감축 차 배출 협정 합의",
 "one": "독일과 프랑스가 2035년 신차 CO2 감축 목표를 90%로 낮추고 독일이 프랑스의 메이드 인 유럽 요구를 지지하는 자동차 협정에 합의하고 메르츠 총리가 내연차 퇴출은 과거 일이 됐다고 하면서, 유럽 완성차의 내연기관 판매 기한이 늘어날 수 있다",
 "facts": [
  "무엇이: 메르츠 총리와 마크롱 대통령은 2035년부터 완성차 평균 배출을 90%만 줄이고 나머지 10%는 상쇄하지 않아도 되게 하는 데 원칙 합의했고, 독일은 그 대가로 프랑스의 바이 유러피언 요구를 지지한다 [사실]",
  "중간 목표: 양국은 2030년 55% 감축 목표를 집행위안의 3년이 아닌 5년에 걸쳐 달성하는 방안도 제안했다 [사실]",
  "발언: 메르츠는 정상회의 뒤 내연기관 퇴출은 이제 과거 일이라며 합의를 EU 규정으로 옮겨야 한다고 했다 [사실]",
  "영국: 협정은 영국에 특별 지위를 주는 내용을 담았다 [제목]",
  "절차: 유럽의회와 회원국 승인을 거쳐야 효력이 생긴다 [사실]"
 ],
 "basis": "verified",
 "check": "90% 감축·바이 유러피언 맞교환·2030년 5년 달성안·메르츠 발언·승인 절차는 검색 결과 요약(클린에너지와이어·라프레세)으로 확인. 영국 특별 지위는 보도로만 나와 제목 기준",
 "src": [
  {"o": "Clean Energy Wire", "d": "2026-10-16", "u": "https://www.cleanenergywire.org/news/france-and-germany-strike-deal-further-weaken-eu-combustion-engine-phaseout-media"},
  {"o": "LaPresse", "d": "2026-10-16", "u": "https://uk.lapresse.it/world-en/2026/10/16/eu-merz-the-end-of-combustion-engines-is-a-thing-of-the-past-yes-to-biofuels"}
 ],
 "inds": ["auto"], "nodes": [],
 "vc": [
  {"ind": "auto", "node": "policy", "f": "공급", "dir": "up", "k": "예상", "t": "佛·獨, 2035년 CO2 감축 90%로 완화 합의"}
 ],
 "added": "이번 블룸버그·로이터 3건으로 양국의 협정 합의와 메르츠의 내연차 금지는 과거 일이라는 선언, 영국 특별 지위와 각계 반응이 추가됐다",
 "items": [
  it("메르츠 '프랑스와 합의로 EU 내연차 금지는 과거 일'", BB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/france-germany-reach-deal-on-future-of-european-auto-industry",
     "메르츠 총리가 프랑스와의 합의로 EU의 2035년 내연차 금지가 사라졌다고 선언하면서 유럽 완성차의 내연기관 판매 길이 열릴 수 있다"),
  it("'운전자와 일자리에 좋은 날'…독일·프랑스 자동차 협정 반응", RT, "2026-10-17", "https://www.reuters.com/business/a-good-day-motorists-jobs-reactions-germany-france-car-deal-2026-10-16/",
     "독일·프랑스 자동차 협정을 두고 운전자와 일자리에 좋은 날이라는 반응이 나오는 등 각계 평가가 이어졌다 (제목 기준)"),
  it("프랑스·독일, 차 배출 규제 협정 합의…영국엔 특별 지위", RT, "2026-10-17", "https://www.reuters.com/business/france-germany-agree-deal-car-emissions-uk-special-status-2026-10-16/",
     "프랑스와 독일이 차 배출 규제 완화에 합의하면서 영국에는 메이드 인 유럽 혜택을 받을 수 있는 특별 지위를 주기로 했다 (제목 기준)")
 ]})

# G1-037
items.append({
 "cid": "G1-037", "attachTo": "n-rtr-0282",
 "title": "초대형 유조선 운임 사상 최고서 하락…美 원유 유럽 도착 13% 감소 전망",
 "one": "그림자 선단 제재 완화 검토와 걸프 수출 감소로 오만만~중국 초대형 유조선 운임이 WS 841에서 776으로 내렸지만, 미국 걸프~북서유럽 아프라막스 운임이 한 달 새 약 4.2배 뛰면서 미국산 원유의 유럽 도착이 약 13% 줄 전망이다",
 "facts": [
  "무엇이: 발틱거래소 자료로 오만만~중국 초대형 유조선 운임은 WS 약 776으로, 지수 출범 이후 최고였던 지난주 841에서 내렸다 [사실]",
  "원인: 케플러는 걸프 운임 상승과 수출 감소로 해당 항로 수요가 줄었다고 했고, 스파르타 코모디티스는 트럼프 정부의 그림자 선단 제재 해제 언급이 운임을 끌어내렸다고 봤다 [사실]",
  "유럽: 미국 걸프~북서유럽 아프라막스 운임지수가 한 달 만에 약 4.2배 뛰면서 미국산 원유의 유럽 도착량이 약 13% 줄 전망이다 [채널]",
  "기존: 미국은 제재 유조선이 비제재 원유·제품을 나르도록 허용하는 방안을 논의 중이며, 세계 평균 원유 운송료는 1년 전 배럴당 4달러에서 30달러로 올랐다 [사실]"
 ],
 "basis": "partial",
 "check": "초대형 유조선 운임 WS 841→776과 하락 원인은 검색 결과 요약(인덱스박스)으로 확인. 아프라막스 4.2배·미국산 원유 유럽 도착 13% 감소는 확인 못 해 채널 전언",
 "src": [
  {"o": "IndexBox", "d": "2026-10-16", "u": "https://www.indexbox.io/blog/supertanker-freight-rates-fall-from-record-highs-as-middle-east-tensions-ease/"}
 ],
 "inds": ["shipping", "oil"], "nodes": [],
 "vc": [
  {"ind": "shipping", "node": "tankers", "f": "가격", "dir": "down", "k": "실제", "t": "초대형 유조선 운임 WS 841에서 776으로 하락"},
  {"ind": "oil", "node": "transport", "f": "공급", "dir": "down", "k": "예상", "t": "운임 급등에 미국산 원유 유럽 도착 13% 감소 전망"}
 ],
 "added": "이번 텔레그램·로이터 3건으로 초대형 유조선 운임의 사상 최고치 대비 하락과 아프라막스 운임 급등에 따른 미국산 원유 유럽 도착 감소 전망이 추가됐다",
 "items": [
  it("美 원유 유럽 도착 13% 감소 전망…아프라막스 운임 한 달 새 4.2배", TR, "2026-10-16", "https://t.me/Trillion_labs/10642",
     "미국 걸프~북서유럽 아프라막스 운임이 한 달 새 약 4.2배 뛰면서 차익거래가 막혀 미국산 원유의 유럽 도착이 약 13% 줄 전망이다"),
  it("초대형 유조선(VLCC) 운임, 사상 최고치에서 하락", RT, "2026-10-16", "https://www.reuters.com/business/energy/supertanker-rates-fall-record-highs-2026-10-16/",
     "걸프 수출 감소와 그림자 선단 제재 완화 언급에 오만만~중국 초대형 유조선 운임이 WS 841에서 776으로 내렸다"),
  it("트럼프 정부, 탱커 운임 낮추려 그림자 선단 제재 완화 검토", POL, "2026-10-17", "https://t.me/The_MariTimes/63773",
     "트럼프 정부가 러시아·이란·베네수엘라 원유를 나르던 그림자 선단 제재 완화를 검토하면서 치솟은 탱커 운임을 끌어내리려 한다")
 ]})

# G1-045
items.append({
 "cid": "G1-045", "attachTo": "",
 "title": "홍콩거래소, 2028년 하반기 T+1 결제 전환 목표…의견 109건 대부분 찬성",
 "one": "홍콩거래소가 결제 주기 단축 자문 결과를 내고 시장 준비와 당국 승인을 전제로 2028년 하반기까지 주식 현물시장을 T+1 결제로 바꾸기로 하면서, 증권사·수탁기관의 결제 위험과 자본 부담이 줄어들 전망이다",
 "facts": [
  "무엇이: 홍콩거래소는 10월 16일 결제 주기 단축 자문 결과를 내고 2028년 하반기, 목표 시점 2028년 9월의 T+1 전환을 계획했다 [사실]",
  "일정: 4월 자문안의 2027년 4분기 예시 일정보다 늦춰졌고, 시장 준비와 규제당국 승인이 전제다 [사실]",
  "의견: 브로커·수탁기관·운용사 등에서 중복 제외 109건의 의견을 받았고, 응답자들은 효율 개선·결제 위험 감소·자본 효율 개선을 들어 찬성했다 [사실]",
  "후속: 홍콩거래소는 상장규정·청산소 규정을 고치고 3단계 이행 체계를 도입한다 [사실]"
 ],
 "basis": "verified",
 "check": "2028년 하반기(9월 목표) 전환·109건 의견·4월안 대비 일정 변경·규정 개정은 검색 결과 요약(파이넥스트라·FX뉴스그룹)으로 확인",
 "src": [
  {"o": "Finextra", "d": "2026-10-16", "u": "https://www.finextra.com/pressarticle/111318/hkex-sets-t1-transition-roadmap"},
  {"o": "FX News Group", "d": "2026-10-16", "u": "https://fxnewsgroup.com/forex-news/exchanges/hkex-outlines-roadmap-for-t1-transition-in-securities-market/"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "markets", "f": "가격", "dir": "down", "k": "예상", "t": "T+1 전환으로 결제 위험·자본 부담 감소 전망"}
 ],
 "added": "이번 로이터 1건으로 홍콩거래소의 T+1 결제 출범 시점이 2028년 하반기라는 점이 해외 통신 보도로도 전해졌다는 사실이 추가됐다 (제목 기준)",
 "items": [
  it("홍콩거래소, 2028년 하반기 T+1 결제 전환 목표", HANA, "2026-10-16", "https://t.me/HANAchina/70529",
     "홍콩거래소가 자문 결과 보고서에서 2028년 하반기까지 T+1 전환을 끝내겠다고 하면서 결제 위험과 자본 부담을 낮추려 한다"),
  it("홍콩, 2028년 하반기 하루 결제(T+1) 도입", RT, "2026-10-16", "https://www.reuters.com/world/asia-pacific/hong-kong-launch-one-day-settlement-second-half-2028-2026-10-16/",
     "홍콩이 2028년 하반기부터 주식 결제를 거래 하루 뒤로 앞당기기로 하면서 현물시장 결제 주기가 짧아진다 (제목 기준)")
 ]})

# G1-051
items.append({
 "cid": "G1-051", "attachTo": "n-rtr-0315",
 "title": "아시아 채권 외국인 82억 달러 유출, 2020년 3월 이후 최대…대만달러 2개월 최저",
 "one": "외국인이 9월 한국·태국·인도 등 아시아 5개국 채권을 82억 1,000만 달러 순매도해 2020년 3월 이후 최대 유출을 기록하고 대만 증시에서도 하루 3,025억 대만달러를 팔면서, 대만달러가 2개월여 최저로 밀리는 등 아시아 통화 약세가 넓어지고 있다",
 "facts": [
  "무엇이: 외국인은 9월 인도·인도네시아·말레이시아·한국·태국 채권을 82억 1,000만 달러 순매도해 2020년 3월(172억 8,000만 달러) 이후 최대 월간 유출을 기록했다 [사실]",
  "나라별: 한국이 약 63억 달러로 가장 많이 빠졌고 태국 8억 2,200만, 인도 5억 4,800만, 말레이시아 4억 3,600만, 인도네시아 1억 달러 순이었다 [사실]",
  "대만: 외국인은 10월 15일 대만 증시에서 사상 최대인 3,025억 대만달러를 순매도했고, 대만달러는 장중 32.452까지 밀렸다 [사실]",
  "대만달러: 대만달러는 금요일 0.67% 내린 32.481로 2개월여 최저를 기록했고, 국영은행 개입으로 낙폭이 줄었다 [채널]",
  "기존: 필리핀 페소는 10월 15일 달러당 63.06페소로 처음 63페소 선을 넘었다 [사실]"
 ],
 "basis": "verified",
 "check": "아시아 채권 9월 82억 1,000만 달러 순유출·나라별 규모는 로이터 전재(더스타) 검색 결과 요약으로 확인, 대만 외국인 3,025억 대만달러 순매도·장중 32.452는 중앙통신·ETtoday 검색 결과 요약으로 확인. 금요일 32.481 종가는 확인 못 해 채널 전언",
 "src": [
  {"o": "The Star", "d": "2026-10-16", "u": "https://www.thestar.com.my/business/business-news/2026/10/16/asian-bonds-record-biggest-monthly-foreign-outflow-since-march-2020"},
  {"o": "중앙통신(CNA)", "d": "2026-10-15", "u": "https://www.cna.com.tw/news/afe/202610150182.aspx"},
  {"o": "ETtoday", "d": "2026-10-15", "u": "https://finance.ettoday.net/news/3255213"}
 ],
 "inds": ["macro"], "nodes": ["macro/liquidity", "macro/fx"],
 "vc": [
  {"ind": "macro", "node": "liquidity", "f": "공급", "dir": "down", "k": "실제", "t": "아시아 채권 9월 외국인 82억 달러 순유출"},
  {"ind": "macro", "node": "fx", "f": "가격", "dir": "down", "k": "실제", "t": "외국인 매도에 대만달러 2개월여 최저"}
 ],
 "added": "이번 로이터·텔레그램 2건으로 9월 아시아 채권의 2020년 3월 이후 최대 외국인 유출과 대만 증시 사상 최대 외국인 순매도, 대만달러 2개월여 최저가 추가됐다",
 "items": [
  it("아시아 채권, 2020년 3월 이후 최대 월간 외국인 유출", RT, "2026-10-16", "https://www.reuters.com/world/asia-pacific/asian-bonds-record-biggest-monthly-foreign-outflow-since-march-2020-2026-10-16/",
     "미 국채 금리 급등과 연준 긴축 재개에 외국인이 9월 아시아 5개국 채권을 82억 1,000만 달러 순매도해 2020년 3월 이후 최대 유출을 기록했다"),
  it("대만달러 2개월여 최저…TSMC 호실적에도 외국인 자금 유출", HANA, "2026-10-17", "https://t.me/HANAchina/70551",
     "TSMC 호실적에도 AI 투자 지속성 우려로 외국인이 이번 주 5,400억 대만달러를 순매도하면서 대만달러가 32.481로 2개월여 최저로 밀렸다")
 ]})

# G1-057
items.append({
 "cid": "G1-057", "attachTo": "n-rtr-0054",
 "title": "伊 재무장관 '은행은 사냥꾼 돼야'…MPS 10대 주주 골드스톤, 인테사 인수 지지",
 "one": "조르제티 재무장관이 이탈리아 은행은 인수합병 물결에서 먹잇감이 아닌 사냥꾼이 돼야 한다고 하고 MPS 10대 주주 골드스톤이 인테사 인수안 지지를 밝히면서, 10월 29일 MPS 주총의 방어안 표 대결이 인테사 쪽으로 기울 수 있다",
 "facts": [
  "무엇이: 조르제티 재무장관은 이탈리아·독일 은행권을 바꾸는 인수합병 물결에서 이탈리아 은행이 표적이 아닌 인수자가 돼야 하고, 인수자는 이탈리아 은행이 낫다고 했다 [사실]",
  "주주: MPS 상위 10대 주주인 골드스톤이 인테사의 인수 제안을 지지했다 [제목]",
  "기존: ISS와 글래스루이스는 MPS의 방코BPM·방카제네랄리 인수안과 40억 유로 특별배당에 반대를 권고했다 [사실]",
  "기존: 인테사는 MPS 주주가 방어안을 부결할 때만 현금 8억 유로를 얹겠다고 했고, 주총은 10월 29일 열린다 [사실]"
 ],
 "basis": "partial",
 "check": "조르제티 발언은 검색 결과 요약(피니마이즈)으로 확인. 골드스톤의 인테사 지지는 검색에서 찾지 못해 제목 기준",
 "src": [
  {"o": "Finimize", "d": "2026-10-16", "u": "https://finimize.com/content/italys-finance-minister-wants-banks-hunting-not-being-hunted"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "banks", "f": "공급", "dir": "down", "k": "예상", "t": "MPS 주주 인테사 지지로 은행 통합 가능성 커져"}
 ],
 "added": "이번 로이터·블룸버그 2건으로 조르제티 재무장관의 은행은 사냥꾼이 돼야 한다는 발언과 MPS 10대 주주 골드스톤의 인테사 인수안 지지가 추가됐다",
 "items": [
  it("伊 재무장관 '인수합병 물결 속 이탈리아 은행은 먹잇감 아닌 사냥꾼 돼야'", RT, "2026-10-16", "https://www.reuters.com/legal/transactional/italian-banks-should-be-predators-not-prey-ma-wave-economy-minister-says-2026-10-16/",
     "조르제티 재무장관이 이탈리아 은행이 인수합병 물결에서 인수자가 돼야 한다고 하면서 해외 은행의 국내 은행 인수에 거리를 뒀다"),
  it("MPS 10대 주주 골드스톤, 인테사 인수 제안 지지", BB, "2026-10-17", "https://www.bloomberg.com/news/articles/2026-10-16/paschi-top-10-investor-goldstone-backs-intesa-takeover-bid",
     "MPS 상위 10대 주주인 골드스톤이 인테사의 인수 제안을 지지하면서 MPS 경영진의 방어안이 주주 지지를 잃을 수 있다 (제목 기준)")
 ]})

# G1-064
items.append({
 "cid": "G1-064", "attachTo": "n-rtr-0056",
 "title": "튀르키예 펀드 위기 여파, 1조 리라 회사채 시장으로 번져",
 "one": "튀르키예 펀드 위기로 환매가 몰리자 운용사들이 팔기 쉬운 자산부터 처분해 1조 리라가 넘는 리라화 회사채 시장에 거래가 어려운 채권이 쌓이고 테라 야트름 은행이 원리금 60억 5,000만 리라를 못 갚으면서, 중소 발행사의 자금 조달이 막힐 수 있다",
 "facts": [
  "무엇이: 리라화 회사채 시장은 9월 말 1조 리라를 넘었고 뮤추얼펀드가 약 3분의 1을 갖고 있으며, 환매가 몰리자 운용사들이 팔기 쉬운 자산부터 팔아 거래가 어려운 회사채 비중이 커졌다 [사실]",
  "부도: 테라 야트름 은행은 10월 5일 60억 5,000만 리라의 원리금을 갚지 못했고, 위기 기업과 얽힌 채권 약 350억 리라가 남아 있다 [사실]",
  "발행: 가란티 BBVA 계열사는 10월 리라화 채권을 팔았고 투르크셀·악방크는 사모로 자금을 조달해, 대형 발행사는 시장 접근을 유지하고 있다 [사실]",
  "기존: 자본시장위원회는 운용사 7곳의 펀드 131개(자산 약 183억 달러) 청산을 명령했고, 중앙은행은 금융 시스템 전염 위험은 없다고 했다 [사실]"
 ],
 "basis": "partial",
 "check": "회사채 시장 1조 리라·펀드 보유 3분의 1·테라 원리금 미지급·대형사 발행은 검색 결과 요약(브리프스, 블룸버그 기사 요약)으로 확인했으나 독립 보도는 찾지 못함",
 "src": [
  {"o": "Briefs", "d": "2026-10-16", "u": "https://www.briefs.co/news/turkey-s-fund-turmoil-puts-corporate-bonds-and-small-issuers/"}
 ],
 "inds": ["fin", "macro"], "nodes": ["macro/liquidity"],
 "vc": [
  {"ind": "macro", "node": "liquidity", "f": "공급", "dir": "down", "k": "실제", "t": "펀드 위기에 튀르키예 회사채 유동성 위축"}
 ],
 "added": "이번 블룸버그 1건으로 펀드 위기가 1조 리라 규모 리라화 회사채 시장으로 번져 테라 야트름 은행 원리금 미지급과 중소 발행사 조달난이 드러난 점이 추가됐다",
 "items": [
  it("급성장한 튀르키예 회사채 시장, 펀드 위기 여파와 씨름", BB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/turkey-s-fast-growing-corporate-bond-market-grapples-with-funds-crisis-fallout",
     "펀드 환매 사태가 회사채로 번지면서 급성장한 튀르키예 회사채 시장이 유동성 부족과 발행사 부도 여파에 시달리고 있다")
 ]})

# G1-070
items.append({
 "cid": "G1-070", "attachTo": "n-bbg-0124",
 "title": "발레 '고비용에 철광석 시장 10% 적자'…2년 최저 가격 속 감산 압박",
 "one": "철광석값이 2년 만의 최저로 떨어진 가운데 발레가 중동 분쟁발 에너지·운임 비용 상승으로 해상 철광석 공급의 약 10%인 1억 6,000만 톤이 적자이고 1,500만 톤은 이미 멈췄다고 밝히면서, 고원가 광산의 감산이 가격을 받칠 수 있다",
 "facts": [
  "무엇이: 구스타보 피멘타 발레 CEO는 10월 16일 에너지·운임 비용 상승으로 해상 철광석 공급의 약 10%인 1억 6,000만 톤이 수익을 내지 못한다고 했다 [사실]",
  "감산: 약 1,500만 톤은 비용 상승으로 이미 생산이 멈췄고, 피멘타는 고원가 생산자 감산으로 가격이 회복되고 중국 수요는 견조하다고 봤다 [사실]",
  "가격: 싱가포르 철광석 선물은 이번 주 2년 만에 처음 톤당 90달러 밑으로 내려 올해 약 15% 떨어졌고, 16일에는 약 1.1% 올라 90.85달러였다 [사실]",
  "기존: 중국 성수기 철강 수요 약세와 기니 시만두 공급 증가 우려가 하락 요인으로 꼽혔다 [사실]"
 ],
 "basis": "verified",
 "check": "피멘타 CEO의 10%·1억 6,000만 톤·1,500만 톤 중단 발언과 철광석 가격은 검색 결과 요약(마이닝위클리·마이닝닷컴·리오타임스)으로 확인",
 "src": [
  {"o": "Mining.com", "d": "2026-10-16", "u": "https://www.mining.com/vale-says-soaring-costs-put-10-of-iron-ore-in-the-red/"},
  {"o": "Mining Weekly", "d": "2026-10-16", "u": "https://www.miningweekly.com/article/vale-says-high-costs-making-10-of-iron-ore-market-lose-money-2026-10-16"},
  {"o": "Rio Times", "d": "2026-10-16", "u": "https://www.riotimesonline.com/iron-ore-markets-latam-friday-october-16-2026"}
 ],
 "inds": ["metals"], "nodes": [],
 "vc": [
  {"ind": "metals", "node": "ironore", "f": "공급", "dir": "down", "k": "실제", "t": "고비용에 철광석 1,500만 톤 생산 중단"},
  {"ind": "metals", "node": "ironore", "f": "가격", "dir": "down", "k": "실제", "t": "싱가포르 철광석 2년 만에 90달러 밑으로"}
 ],
 "added": "이번 블룸버그 1건으로 발레가 고비용 탓에 해상 철광석 시장의 약 10%가 적자이고 1,500만 톤이 이미 멈췄다고 밝힌 점이 추가됐다",
 "items": [
  it("발레 '고비용 탓에 철광석 시장의 10%가 적자'", BB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/vale-says-high-costs-making-10-of-iron-ore-market-lose-money",
     "발레가 에너지·운임 비용 상승으로 해상 철광석 공급의 약 10%가 적자라고 하면서 고원가 광산의 감산이 늘어날 수 있다고 봤다")
 ]})

# G1-076
items.append({
 "cid": "G1-076", "attachTo": "n-rtr-0159",
 "title": "나이지리아거래소 CEO '단고테 IPO가 신규 상장 물꼬'…에너지·기술·국영사 대기",
 "one": "단고테 정유가 16억 달러 IPO 청약을 10월 27일까지 늘리고 이집트 예탁증서까지 논의하는 가운데 포폴라 나이지리아거래소 CEO가 이번 상장이 에너지·기술·국영 기업의 신규 상장을 부를 것이라고 하면서, 나이지리아 증시 상장이 내년부터 늘어날 수 있다",
 "facts": [
  "무엇이: 테미 포폴라 나이지리아거래소 CEO는 여러 기업과 비공개 협의 중이며 내년부터 좋은 상장이 나올 수 있다고 했다 [사실]",
  "후보: 거래소는 에너지·기술·국영 기업 상장을 추진하고 있고, NNPC CEO는 10월 13일 상장 계획을 진행한다고 했다 [사실]",
  "한계: 포폴라는 거래 한 건이 시장 깊이·유동성·외환 송금 같은 구조 문제를 고치지는 못한다고 했다 [사실]",
  "기존: 단고테는 41억 주를 주당 525나이라에 팔아 약 16억 달러를 조달하며, 청약 마감은 10월 27일로 연장됐다 [사실]"
 ],
 "basis": "verified",
 "check": "포폴라 CEO의 신규 상장 기대·후보 업종·구조 문제 언급은 검색 결과 요약(네어라메트릭스·뉴스크로니클)으로 확인",
 "src": [
  {"o": "Nairametrics", "d": "2026-10-08", "u": "https://nairametrics.com/2026/10/08/dangote-refinery-ipo-could-trigger-a-new-wave-of-listings-ngx-ceo/"},
  {"o": "The News Chronicle", "d": "2026-10-16", "u": "https://thenews-chronicle.com/dangote-ipo-could-spark-new-wave-of-ngx-listings-ngx-ceo/"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "markets", "f": "공급", "dir": "up", "k": "예상", "t": "단고테 IPO 뒤 나이지리아 신규 상장 확대 전망"}
 ],
 "added": "이번 블룸버그 1건으로 나이지리아거래소 CEO가 단고테 IPO를 계기로 에너지·기술·국영 기업의 신규 상장을 기대한다고 밝힌 점이 추가됐다",
 "items": [
  it("나이지리아거래소 CEO '단고테 IPO가 신규 상장 이끌 것'", BB, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/nigeria-bourse-sees-new-listings-spurred-by-record-dangote-ipo",
     "포폴라 나이지리아거래소 CEO가 단고테 IPO가 신규 상장을 이끌 것이라고 하면서 내년부터 에너지·기술 기업 상장이 늘어날 수 있다고 봤다")
 ]})

# G1-082
items.append({
 "cid": "G1-082", "attachTo": "n-rtr-0034",
 "title": "EU, 대러 제재 우회 3명·9곳 추가 제재…병행수입 무버스 그룹·그림자 선단 겨냥",
 "one": "EU 이사회가 10월 15일 병행수입으로 제재 물품을 러시아에 들여온 무버스 그룹과 그림자 선단·인도행 원유 공급에 얽힌 업체 등 3명·9곳을 추가 제재하면서, 12일 1,600건 가까운 지정에 이어 러시아의 물품 조달과 원유 수출 경로가 더 좁아지고 있다",
 "facts": [
  "무엇이: EU 이사회는 10월 15일 제재 우회에 관여한 개인 3명·법인 9곳을 지정했고, 병행수입으로 제재 물품을 러시아에 들여온 무버스 그룹과 그 대표 드미트리 추돕스키가 포함됐다 [사실]",
  "원유: 그림자 선단이나 인도행 원유 공급과 얽힌 DIS 로지스틱스 DMCC, 비고르 마린 서비스, 시바 시핑, 후루스 트레이드도 지정됐다 [사실]",
  "기타: 러시아 통관 중개업체 DT 이니에르와 튀르키예의 베글레르 테크스틸·메드세 그룹도 포함됐고, 자산 동결과 개인 여행 금지가 적용된다 [사실]",
  "기존: EU는 10월 12일 개인 743명·법인 826곳 등 약 1,600건의 대러 제재 명단을 채택했다 [사실]"
 ],
 "basis": "verified",
 "check": "10월 15일 3명·9곳 지정과 무버스 그룹·원유 관련 업체 명단은 검색 결과 요약(EU 이사회 보도자료·소피아글로브)으로 확인",
 "src": [
  {"o": "EU 이사회", "d": "2026-10-15", "u": "https://www.consilium.europa.eu/en/press/press-releases/2026/10/15/closing-loopholes-council-lists-individuals-and-entities-for-circumventing-eu-sanctions/"},
  {"o": "Sofia Globe", "d": "2026-10-16", "u": "https://sofiaglobe.com/2026/10/16/eu-announces-sanctions-on-individuals-and-firms-for-circumventing-eu-sanctions/"}
 ],
 "inds": ["macro", "oil"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "macro", "node": "geo", "f": "공급", "dir": "down", "k": "실제", "t": "EU, 병행수입 무버스 그룹 등 우회 제재"},
  {"ind": "oil", "node": "policy", "f": "공급", "dir": "down", "k": "실제", "t": "그림자 선단·인도행 원유 공급 업체 제재"}
 ],
 "added": "이번 텔레그램 1건으로 EU가 병행수입 업체 무버스 그룹을 중심으로 제재 우회를 도운 금융·물류 기업을 추가 제재한 점이 추가됐다",
 "items": [
  it("EU, 무버스 그룹 등 대러 제재 우회 기업·개인 추가 제재", INS, "2026-10-17", "https://t.me/insidertracking/66494",
     "EU가 대체 수입 경로를 제공한 무버스 그룹 등 제재 우회 기업·개인을 추가 제재하면서 러시아의 물품 조달 통로가 좁아지고 있다")
 ]})

out = {"agent": "W6", "searches_used": 16, "fetches_used": 0, "items": items, "skipped": []}
json.dump(out, open("/home/user/news-desk/data/mix-2026-10-17/out2/W6.json", "w"), ensure_ascii=False, indent=1)

# checks
tail = re.compile(r' \((제목 기준|채널 전언)\)$')
def L(s): return len(tail.sub('', s))
for x in items:
    multi = len(x["items"]) > 1 or x["attachTo"]
    lo, hi = (90, 160) if multi else (80, 130)
    msgs = []
    if not (20 <= len(x["title"]) <= 50): msgs.append(f"title {len(x['title'])}")
    if not (lo <= L(x["one"]) <= hi): msgs.append(f"one {L(x['one'])}")
    if "added" in x and not (60 <= L(x["added"]) <= 140): msgs.append(f"added {L(x['added'])}")
    for i in x["items"]:
        if not (25 <= len(i["t"]) <= 60): msgs.append(f"t {len(i['t'])} {i['t']}")
        if "s" in i and not (45 <= L(i["s"]) <= 110): msgs.append(f"s {L(i['s'])} {i['s'][:30]}")
    for v in x["vc"]:
        if not (12 <= len(v["t"]) <= 45): msgs.append(f"vc {len(v['t'])} {v['t']}")
    for f in x.get("fed", []):
        if not (20 <= len(f["t"]) <= 70): msgs.append(f"fed {len(f['t'])}")
    for s in x["facts"]:
        if "|" in s or "**" in s or "{{" in s: msgs.append("bad char")
    print(x["cid"], msgs)
