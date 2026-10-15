import json

B, R = "블룸버그", "로이터"
def I(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s: x["s"] = s
    return x

items = []

# G1-008
items.append({
 "cid": "G1-008", "attachTo": "n-tg-0201",
 "title": "英 예산안 앞 IMF '건전화 가속 불필요·국방비 재원 설명하라'…힐리 '적자 감축 고수'",
 "one": "IMF가 영국에 재정건전화를 서두를 필요는 없지만 국방비 재원을 위한 지출 삭감안을 설명하라고 주문하고 힐리 재무장관이 추가 차입 없이 적자 감축 경로를 지키겠다고 밝히면서, 10월 28일 예산안에서 감세·지원책을 넓힐 여지가 좁아질 전망이다",
 "facts": [
  "무엇이: IMF 재정국장 로드리고 발데스는 영국에 재정건전화 속도를 높이라는 것이 아니라 기존 경로를 지키라고 권고했고, 국방비 지출 압력이 재정 전망을 흔들 수 있다고 경고했다 [사실]",
  "차입: FT는 힐리 재무장관이 새 예산 조치의 재원을 마련해 2029/30년 기준 차입을 늘리지 않을 것이라고 보도했다 [사실]",
  "생계비 지원: IMF는 생계비 대책이 광범위한 연료 보조금, 일반 감세, 가격 통제를 피하고 좁게 겨냥돼야 한다고 했다 [사실]",
  "세수·여력: 임금 상승이 예산에 90억 파운드를 보탤 수 있다는 분석이 나왔고, 로이터 설문에서는 재정 여력을 약 150억~160억 파운드로 다시 쌓아야 한다는 의견이 나왔다 [제목]",
  "기존 흐름: 힐리는 자본이득세를 소득세 수준으로 올리지 않을 것이라는 FT 보도가 나왔고, 영국 식료품 물가 상승률은 2.5%로 빨라졌다 [사실]"
 ],
 "basis": "verified",
 "check": "IMF의 '건전화 가속 아님·기존 경로 유지' 권고, 국방비 압력 경고, FT의 추가 차입 없는 예산 보도는 검색 결과 요약으로 확인. 90억 파운드 임금 세수, 150억~160억 파운드 여력 설문, 힐리 '경로 고수' 발언, 영국 증시 상승은 제목 기준",
 "src": [
  {"o": "The National", "d": "2026-10-13", "u": "https://www.thenationalnews.com/business/economy/2026/10/13/imf-urges-uk-to-stay-course-on-deficit-reduction/"},
  {"o": "IndexBox", "d": "2026-10-14", "u": "https://www.indexbox.io/blog/imf-warns-uk-to-stay-on-deficit-reduction-path-ahead-of-healeys-budget/"}
 ],
 "inds": ["macro"], "nodes": ["macro/fiscal"],
 "vc": [{"ind": "macro", "node": "fiscal", "f": "수요", "dir": "down", "k": "예상", "t": "IMF·힐리 추가 차입 없는 적자 감축 경로 유지"}],
 "added": "이번 블룸버그·로이터 9건으로 IMF의 건전화 가속 불필요·국방비 재원 설명 주문과 힐리의 추가 차입 없는 예산·적자 감축 고수 방침, 90억 파운드 임금 세수 분석이 추가됐다",
 "items": [
  I("IMF '영국, 국방력 증강 재원 마련하려면 지출 삭감해야'", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/uk-needs-to-slash-spending-to-fund-defense-buildup-imf-warns",
    "IMF가 영국에 국방비 증액 재원을 위해 다른 지출을 줄여야 한다고 경고하면서, 예산안의 지출 배분 부담이 커지고 있다"),
  I("IMF '영국에 재정건전화 가속을 권고하는 것 아니다'", R, "2026-10-14", "https://www.reuters.com/world/europe/imf-says-it-is-not-recommending-faster-uk-fiscal-consolidation-2026-10-14/",
    "IMF 발데스 재정국장이 영국에 건전화 속도를 높이라는 게 아니라 기존 경로를 지키라는 뜻이라고 밝히면서, 예산안이 급격한 긴축보다 계획 유지에 무게를 둘 수 있다"),
  I("FT '힐리 재무장관, 추가 차입 없이 예산 조치 재원 마련'", R, "2026-10-14", "https://www.reuters.com/business/finance/uk-finance-minister-healey-set-pay-budget-measures-without-more-borrowing-ft-2026-10-14/",
    "힐리 재무장관이 새 예산 조치의 재원을 마련해 2029/30년 기준 차입을 늘리지 않을 계획이라고 FT가 전하면서, 지원책 확대에는 증세나 지출 조정이 따라야 할 전망이다"),
  I("IMF '영국은 국방비 재원을 위한 지출 삭감안을 설명해야'", B, "2026-10-14", "https://www.bloomberg.com/news/newsletters/2026-10-14/imf-says-the-uk-must-explain-spending-cuts-needed-to-fund-defence",
    "IMF가 영국 정부에 국방비 재원을 위해 어떤 지출을 줄일지 설명하라고 요구하면서, 예산안의 지출 우선순위가 쟁점으로 떠올랐다 (제목 기준)"),
  I("임금 상승, 힐리의 예산에 90억 파운드 보탬 가능", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/wages-may-deliver-a-9-billion-boost-for-healey-at-uk-budget",
    "임금 상승이 힐리 재무장관의 예산에 90억 파운드를 보태 줄 수 있다는 분석이 나오면서, 재정 여력 확보 부담이 일부 덜어질 수 있다 (제목 기준)"),
  I("英 재무장관, 예산안 앞두고 무성한 추측 진화", B, "2026-10-15", "https://www.bloomberg.com/news/newsletters/2026-10-14/uk-chancellor-tamps-down-pre-budget-speculation",
    "힐리 재무장관이 예산안 발표를 앞두고 쏟아지는 추측을 누그러뜨리고 나서면서, 10월 28일 발표 전 시장 기대를 관리하려 하고 있다 (제목 기준)"),
  I("필수소비재·방산 강세에 英 증시 상승…예산 차입 보도로 심리 개선", R, "2026-10-15", "https://www.reuters.com/world/uk/uk-stocks-gain-consumer-staples-defence-budget-borrowing-report-lifts-sentiment-2026-10-14/",
    "필수소비재·방산주가 오르고 예산 조치를 추가 차입 없이 메운다는 보도가 투자심리를 끌어올리면서, 영국 증시가 상승했다 (제목 기준)"),
  I("英 힐리 재무장관 '적자 감축 경로 그대로 지키겠다'", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/uk-s-healey-says-he-will-stay-the-path-on-deficit-reduction",
    "힐리 재무장관이 적자 감축 경로를 그대로 지키겠다고 밝히면서, 예산안에서 차입을 늘리는 대규모 부양책이 나올 가능성이 낮아졌다 (제목 기준)"),
  I("로이터 설문 '힐리, 재정 여력 약 150억~160억 파운드로 다시 쌓아야'", R, "2026-10-15", "https://www.reuters.com/world/uk/uks-healey-should-rebuild-fiscal-headroom-about-15-16-billion-reuters-poll-shows-2026-10-15/",
    "로이터 설문 응답자들이 힐리 재무장관이 재정 여력을 약 150억~160억 파운드로 다시 쌓아야 한다고 보면서, 예산안의 증세·지출 조정 폭이 커질 수 있다 (제목 기준)")
 ]
})

# G1-011
items.append({
 "cid": "G1-011", "attachTo": "n-tg-0132",
 "title": "EU, 대중 수입 쿼터 화학·기계로 확대 검토…中 하이브리드차 상한 수용에도 갈등 확산",
 "one": "중국이 하이브리드차 연 35만 대 수입 상한을 받아들인 뒤 독일이 화학·기계 등으로 쿼터 확대를 밀고 EU 집행위가 추가 업종 평가에 착수하면서, EU-중국 무역 갈등이 자동차 밖 제조업 전반으로 번질 수 있다",
 "facts": [
  "무엇이: 독일은 집행위에 연말까지 화학·기계, 경우에 따라 제약까지 대중 수입 쿼터안을 마련하라고 요구했고, 집행위는 수입 급증을 가려내는 무역 데이터 평가에 착수했다 [사실]",
  "수단: 독일·프랑스는 회원국 가중다수결로 반대하지 않으면 집행위가 신속히 대응 조치를 발동하는 수단을 제안했고, 쿼터는 반덤핑과 달리 수입 급증만으로 근거가 된다 [사실]",
  "중국 양보: WSJ는 중국이 하이브리드차 수입 상한을 받아들이며 한발 물러섰다고 전했고, 9월 중국의 EU향 수출은 달러 기준 전년 대비 25.3% 늘었다 [채널]",
  "중국 반응: 중국 측 논평가들은 하이브리드차 합의가 다른 업종의 선례가 되지 않는다며 더 압박하면 반격할 수밖에 없다고 경고했다 [사실]",
  "주변: 프랑스 화장품 업계는 중국 통관 지연을 호소했고, EU 일부 국가는 PET 수입 제한을 요청했다 [제목]"
 ],
 "basis": "verified",
 "check": "독일의 쿼터 확대 요구 업종, 집행위의 추가 업종 평가, 독·불 신속 대응 수단, 하이브리드차 연 35만 대 상한은 검색 결과 요약으로 확인. 9월 대EU 수출 25.3% 증가는 채널 전언, 화장품 통관 지연·PET 수입 제한 요청은 제목 기준",
 "src": [
  {"o": "Türkiye Today", "d": "2026-10-14", "u": "https://www.turkiyetoday.com/business/germany-seeks-broader-eu-import-quotas-on-chinese-goods-beyond-evs-report-3230311"},
  {"o": "Dragonometry", "d": "2026-10-15", "u": "https://dragonometry.substack.com/p/china-exports-faster-europe-builds"}
 ],
 "inds": ["macro", "auto", "beauty"], "nodes": ["macro/geo", "beauty/exports"],
 "vc": [
  {"ind": "macro", "node": "geo", "f": "공급", "dir": "down", "k": "예상", "t": "EU 대중 수입 쿼터 화학·기계로 확대 검토"},
  {"ind": "beauty", "node": "exports", "f": "공급", "dir": "down", "k": "실제", "t": "프랑스 화장품 중국 통관 지연"}
 ],
 "added": "이번 블룸버그·로이터·텔레그램 14건으로 독일의 화학·기계 쿼터 확대 요구, 집행위의 추가 업종 평가 착수, 독·불의 신속 대응 수단 제안과 중국 9월 대EU 수출 25.3% 증가가 추가됐다",
 "items": [
  I("중국 'EU와 협력해 무역관계 안정 높일 용의'", R, "2026-10-14", "https://www.reuters.com/world/china/china-says-it-is-willing-work-with-eu-boost-stability-trade-ties-2026-10-14/",
    "중국이 EU와 협력해 무역관계의 안정성을 높일 용의가 있다고 밝히면서, 하이브리드차 합의 뒤 갈등 확대를 피하려는 신호를 보냈다 (제목 기준)"),
  I("국내 압박 받는 EU 정상들, 대중 무역 조치 저울질", R, "2026-10-14", "https://www.reuters.com/world/china/pressured-home-eu-leaders-weigh-china-trade-steps-2026-10-14/",
    "자국 압박을 받는 EU 정상들이 대중 무역 조치를 저울질하면서, 정상회의에서 추가 규제 논의가 커질 수 있다 (제목 기준)"),
  I("독일, EU에 더 많은 중국산 수입품 상한 부과 압박", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/germany-to-push-eu-to-impose-caps-on-additional-chinese-imports",
    "독일이 화학·기계 등 더 많은 중국산 수입품에 상한을 두자고 EU를 압박하면서, 쿼터가 자동차 밖 업종으로 넓어질 수 있다"),
  I("돔브로우스키스 '하이브리드차 합의 뒤 다른 업종도 대중 무역 재균형 필요'", R, "2026-10-14", "https://www.reuters.com/business/autos-transportation/after-hybrid-car-deal-eu-needs-rebalance-china-trade-other-sectors-dombrovskis-2026-10-14/",
    "돔브로우스키스 집행위원이 하이브리드차 합의 이후 다른 업종에서도 대중 무역 재균형이 필요하다고 밝히면서, 연 3,600억 유로 적자 축소 압박이 이어졌다"),
  I("독일, 브뤼셀 정상회의 앞두고 대중 쿼터 확대 촉구", B, "2026-10-14", "https://www.bloomberg.com/news/newsletters/2026-10-14/germany-pushes-for-more-eu-quotas-on-china-ahead-of-brussels-summit",
    "독일이 브뤼셀 정상회의를 앞두고 대중 수입 쿼터 확대를 촉구하면서, 정상들의 중국 무역 논의 수위가 높아졌다"),
  I("프랑스 화장품, 중국 통관 지연 겪어…업계 단체", R, "2026-10-14", "https://www.reuters.com/business/retail-consumer/french-cosmetics-facing-delays-clearing-china-customs-says-industry-association-2026-10-14/",
    "프랑스 화장품 업계 단체가 중국 세관 통관이 늦어지고 있다고 밝히면서, 프랑스 화장품의 중국 수출에 차질이 생기고 있다 (제목 기준)"),
  I("EU 국가들, PET 수입 제한 요청 제출…변호사들", R, "2026-10-14", "https://www.reuters.com/world/asia-pacific/eu-countries-file-request-curb-pet-imports-lawyers-say-2026-10-14/",
    "EU 일부 국가가 PET 수입 제한을 요청했다고 변호사들이 전하면서, 수입 방어 조치가 다른 품목으로도 번질 수 있다 (제목 기준)"),
  I("EU, 규제 확대 계획으로 중국과 더 큰 무역 충돌 위험", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-14/china-and-eu-risk-new-trade-clash-over-what-comes-after-car-deal",
    "EU가 대중 수입 규제 확대를 추진하면서, 하이브리드차 합의 뒤 중국과의 무역 충돌이 더 커질 위험이 생겼다"),
  I("EU 정상들, 정상회의서 중국 수출·에너지값·예산 논의", R, "2026-10-15", "https://www.reuters.com/world/china/eu-leaders-tackle-china-exports-energy-prices-budget-summit-2026-10-15/",
    "EU 정상들이 10월 15일 정상회의에서 중국 수출과 에너지값, 예산을 다루면서, 대중 무역 조치의 정치적 방향이 정해질 전망이다"),
  I("EU, 대중 무역 쿼터 적용할 추가 업종 평가 착수", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/eu-begins-assessing-additional-sectors-for-china-trade-quotas",
    "EU 집행위가 무역 데이터를 분석해 수입 급증 업종을 가려내는 평가에 착수하면서, 하이브리드차식 쿼터가 다른 업종에 적용될 수 있다"),
  I("中, EU 하이브리드차 상한 수용…EU는 301조식 무역수단 추진", "텔레그램 상상인 김진범", "2026-10-16", "https://t.me/PipeBeom/6718",
    "중국이 EU의 하이브리드차 연 35만 대 수입 상한을 받아들인 가운데 독·불이 301조와 비슷한 폭넓은 관세 수단을 추진하면서, 규제가 화학 등 다른 제조업으로 번질 수 있다"),
  I("EU, 대중 무역 쿼터 적용 대상 업종 추가로 검토", B, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-15/eu-assesses-more-sectors-in-china-trade-for-quotas",
    "EU가 쿼터를 적용할 대중 교역 업종을 더 살피면서, 화학·기계 등 중국산 제품의 유럽 수출 여건이 빡빡해질 수 있다"),
  I("EU, 중국산 수입 차단 권한 담은 무역 무기 강화", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/eu-prepares-trade-tool-that-could-block-china-from-single-market",
    "EU가 중국산 수입을 단일시장에서 막을 수 있는 권한을 담은 무역 수단을 준비하면서, 중국 기업의 유럽 시장 접근이 위협받게 됐다 (제목 기준)"),
  I("EU, 더 넓은 무역 수단으로 중국 겨냥 계획", B, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-15/eu-is-said-to-target-china-with-broader-trade-tool",
    "EU가 더 폭넓은 무역 수단으로 중국을 겨냥하려 한다는 보도가 나오면서, 독·불이 제안한 신속 대응 수단이 힘을 얻고 있다")
 ]
})

# G1-026
items.append({
 "cid": "G1-026", "attachTo": "n-rtr-0282",
 "title": "美, 그림자 선단 제재 완화 검토…원유 운임 배럴당 30달러로 치솟아",
 "one": "원유 운임이 1년 전 배럴당 4달러에서 30달러로 치솟자 미국이 제재 유조선에 비제재 원유 수송을 허용하는 그림자 선단 제재 완화를 검토하면서, 운임 하락 기대가 생겼지만 분석가들은 새로 풀리는 유조선이 많지 않을 것으로 본다",
 "facts": [
  "무엇이: 미국은 제재 대상이던 유조선이 미국 제재를 받지 않는 원유·제품을 나르도록 허용하는 방안을 논의 중이며, 기업은 재무부에 선박 사용을 신청해야 하고 러시아·이란산 원유 제재는 유지된다 [사실]",
  "목적: 크리스 라이트 에너지장관은 사상 최고 운임이 미국산 원유 수요를 깎았다며 걸프 지역 원유 수송을 늘리려는 논의라고 설명했다 [사실]",
  "운임: 골드만삭스는 세계 평균 원유 운송료가 1년 전 배럴당 4달러에서 30달러로, 중동 항로는 35달러로 올랐고 무르반·바스라 가격차가 2월 2달러에서 43달러로 벌어졌다고 분석했다 [채널]",
  "회의론: 에너지 애스펙츠는 러시아·베네수엘라 연계 제재 선박 대부분이 최근 3개월간 이미 운항 중이라 효과가 작다고 봤고, 선박 보험사가 EU·영국 규정에 묶여 운임이 크게 내리긴 어렵다는 지적도 나왔다 [사실]",
  "반대 압박: 영국 재무장관은 러시아 해운 제재를 강화하라고 촉구했고, 앞서 프랑스는 그림자 선단 유조선 DF피크를 나포했다 [제목]"
 ],
 "basis": "verified",
 "check": "미국의 제재 완화 논의 내용·목적, 에너지 애스펙츠의 효과 제한 평가는 검색 결과 요약으로 확인. 골드만삭스 운임 수치는 채널 전언, 영국 재무장관의 제재 강화 촉구와 운임발 소비자 물가 상승은 제목 기준",
 "src": [
  {"o": "BOE Report", "d": "2026-10-14", "u": "https://boereport.com/2026/10/14/us-considers-easing-sanctions-on-shadow-fleet-vessels-to-cut-freight-rates-official-says/"},
  {"o": "Meduza", "d": "2026-10-15", "u": "https://meduza.io/en/news/2026/10/15/us-weighs-easing-sanctions-on-shadow-fleet-tankers"},
  {"o": "investingLive", "d": "2026-10-15", "u": "https://investinglive.com/commodities/us-weighs-easing-shadow-fleet-sanctions-to-cut-record-tanker-freight-rates/"}
 ],
 "inds": ["oil", "shipping", "macro"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "shipping", "node": "tankers", "f": "가격", "dir": "up", "k": "실제", "t": "원유 운임 1년 새 배럴당 4달러서 30달러로"},
  {"ind": "oil", "node": "policy", "f": "공급", "dir": "up", "k": "예상", "t": "미국 그림자 선단 제재 완화 검토"}
 ],
 "added": "이번 텔레그램 5건·블룸버그·로이터 5건으로 미국의 그림자 선단 제재 완화 검토와 원유 운임 배럴당 30달러 급등, 분석가들의 효과 제한 평가가 추가됐다",
 "items": [
  I("골드만 '원유 운송료 배럴당 30달러…무르반-바스라 가격차 43달러'", "텔레그램 트릴리온", "2026-10-14", "https://t.me/Trillion_labs/10442",
    "골드만삭스가 세계 원유 운송료가 1년 전 배럴당 4달러에서 30달러로 올랐다고 분석하면서, 호르무즈 안팎 원유 등급 간 가격차가 43달러로 벌어졌다"),
  I("치솟는 원유 운임, 연료 공급을 위협하는 위험으로 부상", B, "2026-10-14", "https://www.bloomberg.com/news/newsletters/2026-10-14/soaring-oil-freight-is-becoming-a-risk-to-fuel-supply",
    "원유 운임 급등이 연료 공급을 위협하는 요인으로 떠오르면서, 수입국의 석유제품 조달 차질 우려가 커지고 있다 (제목 기준)"),
  I("美, 운임 낮추려 그림자 선단 일부 제재 해제 논의…로이터", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66315",
    "미국이 글로벌 운임을 낮추고 중동 원유 흐름을 늘리려 그림자 선단 일부 선박의 제재 해제를 논의한다는 영문 속보가 나오면서, 유조선 공급 확대 기대가 생겼다"),
  I("美, 운임 인하 위해 그림자 함대 일부 선박 제재 완화 논의", "텔레그램 미국 주식 인사이더", "2026-10-15", "https://t.me/insidertracking/66319",
    "미국 정부가 중동 석유 수송을 살리려 그림자 함대 일부 선박의 제재 완화를 논의 중이라는 관계자 발언이 한국어로 전해지면서, 운임 하락 가능성이 거론됐다"),
  I("美, 불법 선박 제재 완화 검토…채널 '새 카드'", "텔레그램 트릴리온", "2026-10-15", "https://t.me/Trillion_labs/10531",
    "미국이 불법 선박 제재 완화를 검토한다는 소식을 채널이 운임 대응을 위한 새 카드로 평가하면서, 그림자 선단 규제 완화 가능성에 관심이 쏠렸다"),
  I("英 재무장관, 러시아 해운에 대한 제재 강화 촉구", R, "2026-10-15", "https://www.reuters.com/world/uk/uk-finance-minister-calls-tighter-russian-shipping-sanctions-2026-10-15/",
    "영국 재무장관이 러시아 해운 제재를 더 조여야 한다고 촉구하면서, 미국의 완화 검토와 반대 방향의 압박이 나왔다 (제목 기준)"),
  I("트럼프 행정부, 러·이란·베네수엘라 원유 나른 유조선단 제재 완화 계획", "텔레그램 트릴리온", "2026-10-15", "https://t.me/Trillion_labs/10548",
    "트럼프 행정부가 러시아·이란·베네수엘라 석유를 실어 온 유조선단의 제재 완화를 계획한다고 채널이 전하면서, 사상 최고 운임을 낮추려는 대응이 구체화되고 있다"),
  I("원유 운송비 급등에 주유소 기름값·식료품 값까지 상승", R, "2026-10-15", "https://www.reuters.com/business/energy/oil-shipping-costs-spike-lifting-prices-pump-grocery-2026-10-15/",
    "원유 운송비가 급등해 주유소 기름값과 식료품 가격까지 끌어올리면서, 운임 부담이 소비자 물가로 번지고 있다 (제목 기준)"),
  I("분석가들 '美 그림자 선단 제재 완화로 풀리는 유조선 많지 않을 것'", R, "2026-10-16", "https://www.reuters.com/business/energy/us-plan-ease-shadow-fleet-sanctions-unlikely-free-up-many-tankers-analysts-say-2026-10-15/",
    "분석가들이 제재 선박 대부분이 이미 운항 중이고 보험사가 EU·영국 규정에 묶여 있다고 지적하면서, 미국의 완화가 운임을 크게 낮추기 어렵다고 봤다"),
  I("美 관리 '운임 낮추려 그림자 선단 선박 제재 완화 검토'", R, "2026-10-16", "https://www.reuters.com/legal/government/us-considers-easing-sanctions-shadow-fleet-vessels-cut-freight-rates-official-2026-10-15/",
    "미국 관리가 제재 유조선이 비제재 원유를 나르도록 허용해 운임을 낮추는 방안을 검토 중이라고 밝히면서, 기업들이 재무부 신청을 거쳐 해당 선박을 쓸 수 있게 될 전망이다")
 ]
})

# G1-035
items.append({
 "cid": "G1-035", "attachTo": "",
 "title": "美, 베네수엘라 국회의장 제재 해제…경제고문은 채무 지속가능성 분석 공개 추진",
 "one": "미국 재무부가 베네수엘라 국회의장 호르헤 로드리게스를 제재 명단에서 빼고 베네수엘라 최고 경제고문이 채무 지속가능성 분석 공개를 추진하면서, 외국 석유사 진입을 넓힐 석유법 개정과 채무 재조정 논의가 진전될 수 있다",
 "facts": [
  "무엇이: 미국 재무부 해외자산통제실은 10월 14일 베네수엘라 국회의장 호르헤 로드리게스를 제재 명단에서 삭제해 미국 관할 내 자산 동결을 풀었다 [사실]",
  "배경: 그는 델시 로드리게스 대통령 권한대행의 동생으로 2021년부터 의회를 이끌었고 2018년 9월 제재됐으며, 델시 로드리게스의 제재는 4월 해제됐다 [사실]",
  "석유법: 그는 외국 기업이 더 들어올 수 있도록 석유법 개정을 이끌 것으로 예상된다 [사실]",
  "채무: 베네수엘라 최고 경제고문은 채무 지속가능성 분석을 공개하려 한다고 밝혔다 [제목]"
 ],
 "basis": "partial",
 "check": "국회의장 제재 해제와 석유법 개정 역할은 검색 결과 요약으로 확인. 채무 지속가능성 분석 공개 계획은 확인 못 함(제목 기준)",
 "src": [
  {"o": "Anadolu/aNews", "d": "2026-10-14", "u": "https://www.anews.com.tr/americas/2026/10/14/us-removes-head-of-venezuelas-national-assembly-from-sanctions-list"},
  {"o": "Xinhua", "d": "2026-10-15", "u": "https://english.news.cn/20261015/1b9e0af2721c4f558a35045cfc1d0e68/c.html"},
  {"o": "Jerusalem Post", "d": "2026-10-15", "u": "http://www.jpost.com/international/article-911704"}
 ],
 "inds": ["oil", "macro"], "nodes": ["macro/geo"],
 "vc": [{"ind": "oil", "node": "policy", "f": "공급", "dir": "up", "k": "예상", "t": "미국 베네수엘라 국회의장 제재 해제"}],
 "added": "이번 10월 15일 로이터 보도로 제재가 풀린 인물이 2021년부터 의회를 이끈 국회의장 호르헤 로드리게스라는 점과 석유법 개정 역할이 추가됐다",
 "items": [
  I("베네수엘라 최고 경제고문 '채무 지속가능성 분석 공개 추진'", R, "2026-10-14", "https://www.reuters.com/world/americas/venezuelas-top-economic-adviser-says-aims-publish-debt-sustainability-analysis-2026-10-14/",
    "베네수엘라 최고 경제고문이 채무 지속가능성 분석을 공개하겠다고 밝히면서, 채권자들과의 채무 재조정 논의의 기초 자료가 나올 수 있다 (제목 기준)"),
  I("미국, 관계 해빙 속 베네수엘라 최고위 입법자 제재 해제", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/us-lifts-sanctions-on-venezuela-s-top-lawmaker-as-relations-thaw",
    "미국이 관계 해빙 속에 베네수엘라 국회의장의 제재를 해제하면서, 양국 관계 정상화가 한 걸음 더 나아갔다"),
  I("美 재무부, 베네수엘라 의회 수장에 대한 제재 해제", R, "2026-10-15", "https://www.reuters.com/business/energy/us-lifts-sanctions-head-venezuela-legislature-2026-10-14/",
    "미국 재무부가 베네수엘라 의회 수장의 미국 내 자산 동결을 풀면서, 외국 석유사 진입을 넓힐 석유법 개정 추진에 힘이 실릴 수 있다")
 ]
})

# G2-017
items.append({
 "cid": "G2-017", "attachTo": "n-rtr-0201",
 "title": "EU 정상회의, 에너지값 급등 대응 고심…伊 가스 가격 상한·체코 정유 횡재세",
 "one": "EU 정상들이 정상회의에서 집행위에 에너지값 부담을 덜 단기 대책을 요구하고 이탈리아가 가스 가격 상한 합의에 다가선 가운데 체코가 정유업 횡재세를 추진하면서, 독일 가스 비축 부담금에 이어 겨울 에너지 비용이 소비자와 에너지 기업에 나뉘어 지워지고 있다",
 "facts": [
  "무엇이: 10월 15~16일 EU 정상회의에서 정상들은 집행위에 시민과 기업의 에너지값 부담을 덜 단기 대책을 요구했고, 초안 결론에는 메탄 규제 수정, 국가보조 임시 체계 연장, 정유사 단기 체계, 자발적 수요 결집이 담겼다 [사실]",
  "가스 상한·횡재세: 멜로니 총리는 이탈리아가 EU와 가스 가격 상한 합의에 근접했다고 말했고, 체코 하원은 정유업 횡재세를 1차 지지했다 [제목]",
  "정상회의 의제: 석유사 횡재세는 정상회의 논의 대상이 아닌 것으로 전해졌고, 이탈리아·그리스의 재정 규칙 추가 예외 요구를 집행위는 거부해 왔다 [사실]",
  "겨울 경고: 집행위는 높은 에너지 가격으로 매우 힘든 겨울이 될 것이라고 경고했다 [채널]",
  "수급: 독일 규제당국은 가스 저장량이 낮지만 공급 위험은 없다고 밝혔고, EDF는 가스 공급 불확실성으로 에디슨 지분 매각 계획을 멈췄다 [제목]"
 ],
 "basis": "partial",
 "check": "정상회의의 단기 대책 요구·초안 결론, 석유사 횡재세 비의제는 검색 결과 요약으로 확인. 멜로니의 가스 가격 상한 발언, 집행위 겨울 경고, 체코 횡재세, EDF·독일 저장량 소식은 확인 못 함",
 "src": [
  {"o": "Agence Europe", "d": "2026-10-15", "u": "https://agenceurope.eu/en/bulletin/article/13960/1/heads-of-state-meeting-in-brussels-count-on-european-commission-to-tackle-soaring-energy-prices"},
  {"o": "E3G", "d": "2026-10", "u": "https://www.e3g.org/news/euco-october2026-eu-leaders/"}
 ],
 "inds": ["gas", "oil"], "nodes": ["gas/trade", "gas/regas"],
 "vc": [
  {"ind": "gas", "node": "trade", "f": "가격", "dir": "down", "k": "예상", "t": "이탈리아 EU와 가스 가격 상한 합의 근접"},
  {"ind": "oil", "node": "refining", "f": "가격", "dir": "down", "k": "예상", "t": "체코 하원 정유업 횡재세 1차 지지"}
 ],
 "added": "이번 블룸버그·로이터 6건과 텔레그램 1건으로 EU 정상회의의 단기 에너지 대책 논의, 이탈리아의 가스 가격 상한 합의 근접, 체코 정유업 횡재세, 집행위의 힘든 겨울 경고가 추가됐다",
 "items": [
  I("체코 하원, 정유 부문 횡재세 법안에 1차 지지", R, "2026-10-14", "https://www.reuters.com/legal/transactional/czech-lower-house-gives-initial-backing-windfall-tax-refinery-sector-2026-10-14/",
    "체코 하원이 정유업 횡재세 법안을 1차로 지지하면서, 높은 에너지값 속 정유사 이익에 대한 과세가 현실화될 수 있다 (제목 기준)"),
  I("멜로니 '이탈리아, EU와 가스 가격 상한 합의 근접'", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/italy-is-nearing-deal-with-eu-on-gas-price-cap-meloni-says",
    "멜로니 총리가 이탈리아가 EU와 가스 가격 상한 합의에 다가섰다고 밝히면서, 가스값 급등에 상한을 두는 대응이 가시화될 수 있다 (제목 기준)"),
  I("EU 집행위 '높은 에너지 가격에 매우 힘든 겨울'", "텔레그램 미국 주식 인사이더", "2026-10-14", "https://t.me/insidertracking/66223",
    "EU 집행위원회가 높은 에너지 가격 탓에 매우 힘든 겨울이 될 것이라고 경고하면서, 가계와 기업의 난방·전력 비용 부담 우려가 커졌다"),
  I("EDF, 가스 공급 불확실성에 에디슨 지분 매각 계획 중단", R, "2026-10-15", "https://www.reuters.com/business/energy/edf-pauses-edison-stake-sale-plan-gas-supply-uncertainty-clouds-outlook-2026-10-14/",
    "EDF가 가스 공급 불확실성으로 전망이 흐려지자 에디슨 지분 매각 계획을 멈추면서, 에너지 자산 매각 일정이 늦춰졌다 (제목 기준)"),
  I("유럽 정상들, 전쟁발 에너지 충격 누그러뜨릴 수단 부족", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/europe-s-leaders-have-few-tools-to-ease-war-driven-energy-shock",
    "유럽 정상들이 전쟁으로 촉발된 에너지 충격을 누그러뜨릴 정책 수단을 마땅히 찾지 못하면서, 높은 에너지값이 겨울 내내 이어질 수 있다 (제목 기준)"),
  I("EU 정상회의서 에너지값 급등 논의…쉬운 해법 없어", B, "2026-10-15", "https://www.bloomberg.com/news/newsletters/2026-10-15/no-easy-solutions-as-eu-leaders-discuss-energy-price-surge-at-summit",
    "EU 정상들이 정상회의에서 집행위에 단기 대책을 요구하는 데 무게를 두면서, 메탄 규제 수정과 국가보조 체계 연장 같은 한정된 조치가 거론되고 있다"),
  I("독일 규제당국 '가스 저장량 낮지만 공급 위험은 없어'", R, "2026-10-16", "https://www.reuters.com/business/energy/germany-gas-storage-low-no-supply-risk-regulator-says-2026-10-15/",
    "독일 규제당국이 가스 저장량은 낮지만 공급 위험은 없다고 밝히면서, 겨울 가스 부족 우려를 진정시키려 했다 (제목 기준)")
 ]
})

# G3-008
items.append({
 "cid": "G3-008", "attachTo": "",
 "title": "中 증시 급락 속 오후 지수형 ETF 거래 폭증…주식형 ETF 거래대금 40%↑",
 "one": "중국 증시가 미국 물가 충격에 밀린 10월 15일 오후 CSI300 등 지수형 ETF 거래가 몰려 주식형 ETF 거래대금이 1,670억 위안으로 40% 늘면서, 당국의 지지 매수 가능성이 거론됐지만 낙폭 축소는 제한적이었다",
 "facts": [
  "무엇이: 10월 15일 주식형 ETF 전체 거래대금이 1,670억 위안을 넘어 전날 1,193억 위안보다 약 40% 늘며 2개월 만에 최대였고, 직전 고점은 8월 19일 2,089억 위안이었다 [채널]",
  "대형 ETF: E펀드 CSI300 ETF 거래대금은 장 마감 무렵 급증해 수개월 만의 최대로 불었고, 집계는 150억~194억 위안으로 엇갈렸다 [사실]",
  "지수: 이날 CSI300은 1.59%, CSI500은 2.43% 내렸고, 미국 물가 지표가 예상보다 높게 나온 뒤 세계 증시 매도가 원인으로 꼽혔다 [사실]",
  "개입: 채널은 정부 개입을 추정했지만 이날 국가대표 자금의 매수는 확인되지 않았다 [미확인]",
  "수급: UBS는 A주 기술주의 공모펀드 초과 비중이 역사적 고점 18.5%에서 내려오고 거래 비중이 49.7%에서 37.2%로 떨어져 쏠림이 대부분 풀렸다고 봤고, 홍콩 강구퉁 거래 비중은 2년 만에 최저였다 [채널]"
 ],
 "basis": "partial",
 "check": "10월 15일 CSI300 ETF 거래 급증과 지수 하락은 검색 결과 요약으로 확인(거래대금 집계는 출처마다 다름). 주식형 ETF 전체 1,670억 위안, UBS 분석, 강구퉁 비중은 채널 전언, 정부 개입은 확인 못 함",
 "src": [
  {"o": "KuCoin News", "d": "2026-10-15", "u": "https://www.kucoin.com/news/flash/a-share-indices-fall-amid-global-market-downturn-etfs-see-strong-inflows"},
  {"o": "China Stock Crowd", "d": "2026-10-15", "u": "https://chinastockcrowd.substack.com/p/only-one-in-13-chinese-stocks-rose"}
 ],
 "inds": ["fin", "macro"], "nodes": ["macro/liquidity"],
 "vc": [
  {"ind": "fin", "node": "markets", "f": "수요", "dir": "up", "k": "실제", "t": "주식형 ETF 거래대금 40% 늘어 2개월 최고"},
  {"ind": "fin", "node": "markets", "f": "가격", "dir": "down", "k": "실제", "t": "CSI300 하루 1.59% 하락"}
 ],
 "added": "이번 10월 15일 텔레그램 3건으로 UBS의 기술주 쏠림 해소 평가와 오후 지수형 ETF 거래 급증, 주식형 ETF 거래대금 40% 증가가 추가됐다",
 "items": [
  I("홍콩 강구퉁 본토 거래 비중 2년래 최저…본토 자금 순유출", "텔레그램 하나증권 중국전략", "2026-10-14", "https://t.me/HANAchina/70375",
    "홍콩 증시에서 본토 투자자의 강구퉁 거래 비중이 2년 만에 최저로 떨어지면서, 본토 자금의 순유출이 이어지고 있다"),
  I("중국 주식 대 채권 투자 매력도…주식 우위 여전", "텔레그램 하나증권 중국전략", "2026-10-14", "https://t.me/HANAchina/70376",
    "하나증권 중국전략이 중국 주식과 채권의 투자 매력도를 비교하면서, 주식의 상대 매력이 여전히 압도적이라는 평가를 전했다"),
  I("UBS 'A주 기술주 쏠림 대폭 완화, 추가 하락 위험 제한적'", "텔레그램 하나증권 중국전략", "2026-10-15", "https://t.me/HANAchina/70460",
    "UBS가 A주 기술주의 공모펀드 초과 비중이 고점 18.5%에서 내려오고 거래 비중이 37.2%로 떨어졌다고 보면서, 시장의 추가 하락 위험이 제한적이라고 판단했다"),
  I("中 오후장 지수형 ETF 거래액 급증…정부 개입 추정", "텔레그램 하나증권 중국전략", "2026-10-15", "https://t.me/HANAchina/70474",
    "창업판·과창50·CSI300 ETF 거래액이 오후 들어 전날 하루치를 넘어서면서, 채널은 정부 개입을 추정했지만 낙폭 축소는 제한적이었다고 전했다"),
  I("주식형 ETF 거래대금 40% 급증해 2개월 최고", "텔레그램 하나증권 중국전략", "2026-10-15", "https://t.me/HANAchina/70478",
    "중국 주식형 ETF 거래대금이 1,670억 위안을 넘어 전날보다 약 40% 늘고 E펀드 CSI300 ETF는 전일의 14배로 불어나면서, 2개월 만에 최대 거래가 몰렸다")
 ]
})

# G3-011
items.append({
 "cid": "G3-011", "attachTo": "n-rtr-0193",
 "title": "UBS, 스위스 자본규제 강화 땐 본사 해외 이전 검토…美 금융사 인수·합병 거론",
 "one": "스위스가 해외 자회사 자본 보강 강화와 사실상 UBS만 내는 백스톱 수수료를 추진하는 가운데 UBS가 규제가 과도해지면 미국 금융사 인수 후 이전 등 본사를 해외로 옮기는 비상 계획을 검토하면서, 스위스 대표 은행의 이탈 가능성이 커지고 있다",
 "facts": [
  "무엇이: WSJ는 UBS가 의회가 자본 요건을 강화하면 미국 금융사 인수 후 이전, 유럽 경쟁사와 합병, 미국 은행에 매각 등 본사를 스위스 밖으로 옮기는 비상 계획을 준비 중이라고 보도했다 [사실]",
  "쟁점: 정부안은 해외 자회사를 CET1 자본으로 100% 뒷받침하게 해 UBS 추산 약 160억 달러의 추가 자본이 필요하고(현행 60%), 상원은 9월 23일 90% 안을 승인했다 [사실]",
  "UBS 입장: 에르모티 CEO는 스위스 잔류가 경제와 주주에 좋다고 했고, 켈러허 의장은 규제가 지나치면 재검토가 필요하다고 경고했다 [사실]",
  "주변: 한 경쟁 은행은 UBS 이탈이 스위스에 나쁠 것이라고 했고, 스위스 대법원은 크레디트스위스 보너스 삭감을 확정했다 [제목]",
  "기존: 스위스 상원 경제위원회는 사실상 UBS만 대상인 공적 유동성 백스톱 사전 수수료안을 지지했고, FSB는 스위스를 중대한 미준수로 평가했다 [사실]"
 ],
 "basis": "verified",
 "check": "WSJ의 UBS 본사 이전 비상 계획 보도와 자본규제 쟁점·경영진 입장은 검색 결과 요약으로 확인. 경쟁 은행 발언과 크레디트스위스 보너스 판결은 제목 기준",
 "src": [
  {"o": "Global Banking & Finance Review", "d": "2026-10-15", "u": "https://www.globalbankingandfinance.com/ubs-weighs-moving-headquarters-switzerland-if-capital-rules/"},
  {"o": "Investing.com", "d": "2026-10-15", "u": "https://www.investing.com/news/stock-market-news/ubs-considers-leaving-switzerland-over-capital-rule-plans-wsj-reports-93CH-4950453"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [{"ind": "fin", "node": "banks", "f": "공급", "dir": "down", "k": "예상", "t": "자본규제 강화 땐 UBS 본사 해외 이전 검토"}],
 "added": "이번 로이터 3건·블룸버그 1건으로 UBS의 본사 해외 이전 등 비상 계획 검토와 경쟁 은행의 이탈 우려, 스위스 대법원의 크레디트스위스 보너스 삭감 확정이 추가됐다",
 "items": [
  I("WSJ 'UBS, 자본규제 강화 시 본사 스위스 밖 이전 검토'", R, "2026-10-15", "https://www.reuters.com/business/finance/ubs-weighs-moving-headquarters-switzerland-if-capital-rules-tighten-wsj-reports-2026-10-15/",
    "UBS가 스위스 자본규제가 강화되면 본사를 해외로 옮기는 방안을 검토한다고 WSJ가 보도하면서, 의회의 규제 논의에 대한 압박이 커졌다"),
  I("UBS 경쟁 은행 'UBS 이탈은 스위스에 나쁜 일'", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/a-ubs-competitor-says-its-departure-would-be-bad-for-switzerland",
    "UBS의 한 경쟁 은행이 UBS가 떠나면 스위스에 해가 될 것이라고 밝히면서, 본사 이전 논란이 업계 전반의 쟁점으로 번졌다 (제목 기준)"),
  I("스위스 대법원, 크레디트스위스 보너스 삭감 확정", R, "2026-10-15", "https://www.reuters.com/legal/transactional/switzerlands-top-court-upholds-credit-suisse-bonus-cuts-2026-10-15/",
    "스위스 대법원이 크레디트스위스 보너스 삭감 조치를 유지하면서, 2023년 구제 이후 경영진 책임을 묻는 조치가 법적으로 굳어졌다 (제목 기준)"),
  I("소식통 'UBS, 스위스 규제 감당 못 할 경우 대비해 해외 선택지 모색'", R, "2026-10-16", "https://www.reuters.com/legal/transactional/ubs-exploring-options-abroad-case-swiss-rules-prove-intolerable-sources-say-2026-10-15/",
    "UBS가 스위스 규제를 견디기 어려워질 경우에 대비해 미국 금융사 인수·유럽 경쟁사 합병 등 해외 선택지를 살피면서, 본사 이전 가능성이 구체화되고 있다")
 ]
})

# G3-021
items.append({
 "cid": "G3-021", "attachTo": "n-rtr-0031",
 "title": "대만, 선거 베팅 의혹에 코인베이스·칼시 차단…SEC는 Cboe KPI 예측시장 승인",
 "one": "대만이 11월 28일 지방선거를 앞두고 선거 베팅 의혹으로 코인베이스·칼시 접속을 막은 가운데 미국 SEC가 로빈후드를 통한 Cboe의 KPI 예측시장 상품을 승인하고 중간선거 베팅이 급성장하면서, 예측시장이 확장과 규제 압박을 함께 받고 있다",
 "facts": [
  "무엇이: 대만 신베이 지방법원이 형사경찰국 요청을 받아들여 선거 베팅 의혹으로 코인베이스·칼시 웹사이트 접속 제한을 허용했고, 폴리마켓은 이미 대만에서 차단돼 있었다 [사실]",
  "처벌·일정: 선거 도박 참여자는 최대 징역 6개월, 운영자는 최대 5년에 처해질 수 있고, 조치는 11월 28일 지방선거를 앞두고 시행된다 [사실]",
  "미국: SEC가 로빈후드를 통한 Cboe의 KPI 예측시장 베팅을 승인했고, 미국 중간선거 베팅 시장이 급성장하고 있다 [제목]",
  "기존: 칼시는 백악관 대변인 지명 직전 수상한 베팅을 조사하고 있고, NFL은 39개 주와 함께 예측시장 스포츠 계약을 주 도박법으로 규제하게 해 달라고 대법원에 요청했다 [사실]"
 ],
 "basis": "partial",
 "check": "대만의 코인베이스·칼시 차단은 검색 결과 요약으로 확인. SEC의 Cboe KPI 예측시장 승인과 중간선거 베팅 시장 급성장은 확인 못 함(제목 기준)",
 "src": [
  {"o": "Taipei Times", "d": "2026-10-16", "u": "https://www.taipeitimes.com/News/taiwan/archives/2026/10/16/2003866062"},
  {"o": "Quartz", "d": "2026-10-15", "u": "https://qz.com/taiwan-blocks-coinbase-kalshi-election-betting-101526"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "regulation", "f": "공급", "dir": "down", "k": "실제", "t": "대만 선거 베팅 의혹에 코인베이스·칼시 차단"},
  {"ind": "fin", "node": "markets", "f": "공급", "dir": "up", "k": "실제", "t": "SEC 로빈후드 통한 Cboe KPI 예측시장 승인"}
 ],
 "added": "이번 블룸버그 2건·로이터 1건으로 SEC의 Cboe KPI 예측시장 승인, 미국 중간선거 베팅 시장 급성장, 대만의 코인베이스·칼시 차단이 추가됐다",
 "items": [
  I("SEC, 로빈후드 통한 Cboe의 KPI 예측시장 베팅 승인", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-14/sec-approves-cboe-s-kpi-prediction-market-bets-with-robinhood",
    "SEC가 로빈후드를 통해 거래되는 Cboe의 KPI 예측시장 상품을 승인하면서, 증권 규제 틀 안의 예측시장이 넓어질 전망이다 (제목 기준)"),
  I("급성장하는 미국 중간선거 베팅 시장의 내막 들여다보기", R, "2026-10-15", "https://www.reuters.com/legal/government/inside-booming-market-us-midterm-election-bets-2026-10-14/",
    "미국 중간선거를 겨냥한 베팅 시장이 급성장하면서, 선거 결과에 돈을 거는 예측시장 계약 거래가 크게 늘고 있다 (제목 기준)"),
  I("대만, 선거 베팅 의혹에 코인베이스·칼시 차단", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/taiwan-blocks-coinbase-kalshi-over-suspected-election-bets",
    "대만 법원이 선거 베팅 의혹으로 코인베이스·칼시 접속 제한을 허용하면서, 11월 28일 지방선거를 앞두고 해외 예측시장 이용이 막혔다")
 ]
})

# G3-030
items.append({
 "cid": "G3-030", "attachTo": "n-rtr-0181",
 "title": "MSCI, 인도네시아 신흥시장→독자시장 강등 협의 착수…내년 6월 결정",
 "one": "MSCI가 불투명한 지분 구조와 담합 거래 의혹이 풀리지 않았다며 인도네시아를 신흥시장에서 독자시장으로 낮추는 협의에 착수하면서, 올해 지수 시가총액이 55% 줄어든 인도네시아 증시에서 지수 추종 자금 이탈 압력이 커질 수 있다",
 "facts": [
  "무엇이: MSCI는 10월 15일 인도네시아를 신흥시장에서 독자시장으로 재분류하는 안에 대한 협의를 시작했고, 2027년 4월 30일까지 의견을 받아 6월 30일 이전에 결정한다 [사실]",
  "이유: MSCI는 불투명한 지분 구조와 담합 거래 의혹 등 투자 가능성 문제가 풀리지 않았고, 프런티어 시장 강등으로는 문제의 깊이를 반영하지 못한다고 봤다 [사실]",
  "규모: 1월 이후 MSCI 인도네시아 지수 시가총액은 55% 줄었고 신흥시장 지수 내 비중은 1.16%에서 0.43%로 떨어졌으며, 1월부터의 지수 동결은 계속된다 [사실]",
  "기존: 자카르타종합지수는 10월 12일 약 2.5% 떨어져 석 달 만의 최저를 기록했고, 국부펀드 다난타라는 개입 가능성을 열어 뒀다 [사실]"
 ],
 "basis": "verified",
 "check": "MSCI 협의 착수, 사유, 일정, 시가총액·비중 변화는 MSCI 보도자료 전재본과 검색 결과 요약으로 확인",
 "src": [
  {"o": "MSCI 보도자료(Business Wire 전재)", "d": "2026-10-15", "u": "https://www.financialcontent.com/article/bizwire-2026-10-15-msci-launches-a-consultation-on-a-proposal-to-reclassify-indonesia-from-emerging-market-to-standalone-market-status"},
  {"o": "Securities.io", "d": "2026-10-15", "u": "https://www.securities.io/msci-consults-on-moving-indonesia-indexes-to-standalone-market-status/"}
 ],
 "inds": ["fin", "macro"], "nodes": ["macro/liquidity"],
 "vc": [
  {"ind": "fin", "node": "markets", "f": "수요", "dir": "down", "k": "예상", "t": "MSCI 인도네시아 독자시장 강등 협의 착수"},
  {"ind": "macro", "node": "liquidity", "f": "공급", "dir": "down", "k": "실제", "t": "신흥지수 내 인도네시아 비중 0.43%로 축소"}
 ],
 "added": "이번 블룸버그·로이터 2건으로 MSCI의 인도네시아 독자시장 강등 협의 착수와 2027년 6월 결정 일정, 지수 시가총액 55% 감소가 추가됐다",
 "items": [
  I("MSCI '인도네시아 신흥시장 지위 협의 대상'", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/indonesia-s-emerging-market-status-under-consultation-msci-says",
    "MSCI가 인도네시아의 신흥시장 지위를 협의에 부치면서, 지분 투명성 개선이 없으면 내년 강등이 현실화될 수 있다"),
  I("MSCI, 인도네시아를 독자시장으로 강등하는 방안 검토", R, "2026-10-16", "https://www.reuters.com/world/asia-pacific/msci-weighs-downgrading-indonesia-standalone-market-status-2026-10-15/",
    "MSCI가 인도네시아를 프런티어가 아닌 독자시장으로 낮추는 방안을 검토하면서, 개혁 성과가 없으면 신흥시장 지수 추종 자금이 빠질 수 있다")
 ]
})

# G3-033
items.append({
 "cid": "G3-033", "attachTo": "n-rtr-0246",
 "title": "유니크레디트, 코메르츠방크 지배 ECB 승인…연말께 의결권 50% 확보 예상",
 "one": "유럽중앙은행이 유니크레디트에 코메르츠방크 지분 30% 초과 보유를 상한 없이 허용하면서, 지분 약 48%를 가진 유니크레디트가 11월 16일 시한의 EU 경쟁 심사를 거쳐 연말께 의결권 50%로 지배권을 확보할 전망이다",
 "facts": [
  "무엇이: 유니크레디트는 ECB가 코메르츠방크 지분 30% 초과를 승인하고 상한 없이 지분을 늘릴 수 있게 했다고 밝혔다 [사실]",
  "지분: 7월 마무리된 적대적 공개매수로 지분이 약 48%로 늘었고(보도별 47.6~48%), 남은 규제 절차와 조건을 마치면 연말께 의결권 약 50%로 지배권을 얻을 것으로 본다 [사실]",
  "남은 절차: EU 반독점 당국은 11월 16일까지 거래에 대한 판단을 내린다 [제목]",
  "독일 정부: 독일 정부는 코메르츠방크가 상장을 유지하고 프랑크푸르트에 본사를 두기를 원하며, 정부 지분은 9월 기준 약 12%였다 [사실]"
 ],
 "basis": "verified",
 "check": "ECB 승인, 지분율, 연말 지배권 확보 전망, 독일 정부 입장은 검색 결과 요약으로 확인. EU 경쟁 심사 시한은 기존 문서 제목 기준",
 "src": [
  {"o": "Euronews", "d": "2026-10-15", "u": "https://www.euronews.com/2026/10/15/unicredit-cleared-by-ecb-to-take-control-of-commerzbank"},
  {"o": "GuruFocus", "d": "2026-10-15", "u": "https://www.gurufocus.com/news/9126297/unicredit-gains-ecb-approval-to-boost-stake-in-commerzbank-crzby-beyond-30"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [{"ind": "fin", "node": "banks", "f": "공급", "dir": "down", "k": "예상", "t": "유니크레디트 코메르츠방크 지배 ECB 승인"}],
 "added": "이번 로이터 1건으로 ECB가 유니크레디트의 코메르츠방크 지분 30% 초과를 상한 없이 승인해 연말께 지배권 확보 길이 열렸다는 점이 추가됐다",
 "items": [
  I("유니크레디트, 독일 코메르츠방크 지배 ECB 승인 받아", R, "2026-10-16", "https://www.reuters.com/business/finance/italys-unicredit-wins-ecb-approval-control-germanys-commerzbank-2026-10-15/",
    "ECB가 유니크레디트의 코메르츠방크 지분 30% 초과를 승인하면서, 이탈리아 유니크레디트가 독일 코메르츠방크를 지배할 길이 열렸다")
 ]
})

# G3-049
items.append({
 "cid": "G3-049", "attachTo": "",
 "title": "韓 금융사 16곳 해킹 피해 확인…개인정보 약 10만 건 유출",
 "one": "금융위원회가 은행·저축은행·여신금융사·가상자산사업자 등 금융사 16곳에서 해킹으로 개인정보 약 10만 건이 새어 나간 사실을 확인하면서, 금융사 CEO·이사회의 보안 책임이 무거워질 전망이다",
 "facts": [
  "무엇이: 금융위원회는 10월 14일 금융사 16곳이 해킹 피해를 입어 약 10만 건의 개인정보가 유출됐다고 밝혔다 [사실]",
  "대상: 신한·KB국민·BNK부산·하나 등 은행 4곳, 저축은행 4곳, 현대캐피탈·KDB캐피탈 등 여신금융사, 가상자산사업자 스트리미 등이 포함됐다 [사실]",
  "유출 정보: 이름·연락처·주민등록번호가 포함됐으나 계좌·카드 번호 유출 정황은 아직 없다 [사실]",
  "점검·대응: 555개 금융사 점검에서 130곳이 보안 미흡을 보고했고, 금융위는 CEO·이사회의 보안 책임을 높이고 대형사에 연 2회 이상 취약점 점검을 요구할 계획이다 [사실]",
  "미확인: AI 에이전트를 활용한 공격이라는 의심이 제기됐으나 확인되지 않았고, 피해 회사 수는 더 늘 수 있다 [미확인]"
 ],
 "basis": "verified",
 "check": "피해 금융사 16곳, 약 10만 건 유출, 피해사 명단, 점검 결과와 대응책은 검색 결과 요약으로 확인. AI 활용 공격 여부는 출처마다 엇갈려 확인 못 함",
 "src": [
  {"o": "The Korea Times", "d": "2026-10-14", "u": "https://www.koreatimes.co.kr/business/banking-finance/20261014/ai-driven-cyberattacks-hit-16-financial-firms-expose-100000-records"},
  {"o": "Aju Press", "d": "2026-10-14", "u": "https://www.ajupress.com/view/20261014155603996"},
  {"o": "Digital Today", "d": "2026-10-14", "u": "https://www.digitaltoday.co.kr/en/view/114620/financial-sector-hacking-leaks-100000-records-fsc-tightens-ceo-security-accountability"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [{"ind": "fin", "node": "regulation", "f": "-", "dir": "flat", "k": "실제", "t": "금융사 16곳 해킹 피해로 보안 책임 강화 예고"}],
 "items": [
  I("한국, 해킹 피해 입은 금융사 총 16곳으로 확인", R, "2026-10-14", "https://www.reuters.com/world/south-korea-finds-hacking-incidents-total-16-financial-firms-2026-10-14/")
 ]
})

# G4-013
items.append({
 "cid": "G4-013", "attachTo": "",
 "title": "금리 상승에 AI 부채 경고등…코어위브 채권 수익률 15%, 데이터센터 IPO 줄줄이 연기",
 "one": "미국 물가 충격으로 금리가 오른 가운데 코어위브 주가가 15% 넘게 급락하고 채권 수익률이 15% 안팎으로 치솟은 데 이어 데이터센터 업체들의 상장이 철회·연기되면서, AI 인프라의 자금 조달 비용이 투자 속도를 늦출 수 있다",
 "facts": [
  "무엇이: 코어위브 주가가 10월 14일 약 15.5% 급락했고, 2032년 만기 채권 수익률은 14.8%, 2031년물은 약 14.9%로 뛰었다 [사실]",
  "신용: 코어위브는 S&P 등급 B+로 6월 말 기준 약 351억 달러의 부채를 졌고, 5년물 CDS는 자료에 따라 643bp에서 1,000bp 이상까지 엇갈렸다 [사실]",
  "상장: 최근 일주일 새 블랙스톤이 투자한 에어트렁크 리츠, 엔비디아가 투자한 퍼머스, 소프트뱅크가 투자한 SB에너지의 상장이 철회되거나 연기됐다 [채널]",
  "지연: 엔스케일은 노르웨이 주력 데이터센터가 6개월 늦어져 계획한 30MW 중 6.4MW만 가동 중이며, 약 350억 달러 가치를 노린 상장 계획이 흔들리고 있다 [사실]",
  "조달: 골드만삭스는 2027년 하이퍼스케일러 투자 지출의 최소 35%를 회사채로 메워야 하고, 자금 조달이 늦어지면 2027~2028년 반도체 공급망에 주문 공백이 생길 수 있다고 경고했다 [채널]"
 ],
 "basis": "verified",
 "check": "코어위브 주가·채권 수익률·CDS, 엔스케일 데이터센터 지연은 검색 결과 요약으로 확인(CDS 수치는 출처마다 다름). 에어트렁크·퍼머스·SB에너지 상장 철회·연기와 골드만삭스 분석은 채널 전언",
 "src": [
  {"o": "CNBC", "d": "2026-10-14", "u": "https://www.cnbc.com/2026/10/14/coreweave-stock-bond-yields-ai-debt.html"},
  {"o": "Startup Fortune", "d": "2026-10-15", "u": "https://startupfortune.com/nscales-35-billion-ipo-is-wobbling-because-its-data-centers-arent-ready/"}
 ],
 "inds": ["macro", "tech", "fin"], "nodes": ["macro/semis", "macro/liquidity"],
 "vc": [
  {"ind": "tech", "node": "cloud", "f": "가격", "dir": "up", "k": "실제", "t": "코어위브 채권 수익률 15% 안팎으로 급등"},
  {"ind": "realestate", "node": "datacenter", "f": "공급", "dir": "down", "k": "실제", "t": "데이터센터 업체 상장 철회·연기 잇따라"},
  {"ind": "macro", "node": "semis", "f": "수요", "dir": "down", "k": "예상", "t": "자금 지연 시 2027~2028년 반도체 주문 공백 위험"}
 ],
 "added": "이번 10월 16일 텔레그램·로이터·블룸버그 4건으로 에어트렁크·퍼머스·SB에너지의 상장 철회·연기와 엔스케일 데이터센터 지연에 따른 상장 차질이 추가됐다",
 "items": [
  I("골드만 'AI 회사채 발행 중단이 신용시장 지탱…앞으로 두 달이 마지막 평온기'", "텔레그램 하나증권 중국전략", "2026-10-14", "https://t.me/HANAchina/70417",
    "골드만삭스 트레이더들이 AI 대기업들의 채권 발행 중단이 회사채 시장의 평온을 만들었다고 경고하면서, 1,500억 달러 넘는 칩 금융 조달이 대기해 신용 부담이 커질 수 있다"),
  I("AI 최대 병목은 전력·칩 아닌 자금…코어위브 CDS 881bp", "텔레그램 하나증권 중국전략", "2026-10-15", "https://t.me/HANAchina/70464",
    "골드만삭스가 2027년 하이퍼스케일러 투자 지출의 35% 이상을 회사채로 메워야 한다고 분석한 가운데 코어위브 채권 수익률이 15%를 넘으면서, 조달 비용이 AI 투자의 제약으로 떠올랐다"),
  I("금리 상승에 데이터센터 평가 기준, 성장서 수익성·상환능력으로", "텔레그램 상상인 김진범", "2026-10-16", "https://t.me/PipeBeom/6723",
    "에어트렁크·퍼머스·SB에너지가 상장을 철회하거나 미루면서, 데이터센터 투자자들의 평가 기준이 성장 규모에서 수익성과 부채 상환 능력으로 옮겨가고 있다"),
  I("시장 매도세·금리 상승, AI 데이터센터 거래 붐 시험대", R, "2026-10-16", "https://www.reuters.com/business/finance/market-selloff-rising-rates-test-ai-data-centre-deal-boom-2026-10-15/",
    "시장 매도세와 금리 상승이 이어지면서, 활황이던 AI 데이터센터 거래와 상장이 자금 조달 시험대에 올랐다"),
  I("글로벌 시장 긴급: AI 관련 신용부도스와프(CDS)", R, "2026-10-16", "https://www.reuters.com/business/media-telecom/global-markets-cds-ai-urgent-2026-10-15/",
    "AI 관련 기업의 신용부도스와프가 시장의 긴급 관심사로 떠오르면서, AI 부채에 대한 신용 위험 경계가 커지고 있다 (제목 기준)"),
  I("엔스케일 350억 달러 IPO 계획, AI 데이터센터 지연에 혼선", B, "2026-10-16", "https://www.bloomberg.com/news/features/2026-10-15/nscale-s-35-billion-ipo-plans-muddied-by-ai-data-center-delays",
    "엔스케일의 노르웨이 데이터센터가 6개월 늦어져 30MW 중 6.4MW만 가동되면서, 약 350억 달러 가치를 노린 상장 계획이 흔들리고 있다")
 ]
})

# G4-038
items.append({
 "cid": "G4-038", "attachTo": "n-rtr-0253",
 "title": "넷플릭스, 인력 6%·약 1,000명 감원…2022년 이후 최대",
 "one": "넷플릭스가 성장 둔화 속에 10월 20일 3분기 실적 발표를 앞두고 전체 인력의 6%인 약 1,000명을 줄이기로 하면서, 감원 폭이 당초 알려진 5%보다 커졌고 제품·기술 부문에서 영화·TV 경영진까지 비용 조정이 번지고 있다",
 "facts": [
  "무엇이: 넷플릭스는 10월 14일 사내 공지로 전체 인력의 약 6%인 약 1,000명을 줄이기로 했고, WSJ가 공동 CEO 서랜도스·피터스의 내부 이메일을 인용해 처음 보도했다 [사실]",
  "대상: 감원은 주로 제품·기술·법무·인사 부문에 집중됐고, 2022년 이후 최대 규모다 [사실]",
  "배경: 서랜도스는 지난달 성장 속도가 원하는 만큼 빠르지 않다고 말했고, 넷플릭스는 워너브러더스디스커버리 스트리밍·스튜디오 인수전에서 파라마운트 스카이댄스에 졌다 [사실]",
  "일정·입장: 3분기 실적 발표는 10월 20일이며, 넷플릭스는 연간 전망 달성 궤도에 있다고 밝혔다 [사실]",
  "콘텐츠: 블룸버그는 영화·TV 경영진 감원이 프로그램 편성의 어려움을 시사한다고 봤다 [제목]"
 ],
 "basis": "verified",
 "check": "6%·약 1,000명 감원, 부문, 배경, 실적 일정은 검색 결과 요약으로 확인. 영화·TV 경영진 감원은 제목 기준",
 "src": [
  {"o": "CNBC", "d": "2026-10-14", "u": "https://www.cnbc.com/2026/10/14/netflix-layoffs.html"},
  {"o": "Deadline", "d": "2026-10-14", "u": "https://deadline.com/2026/10/netflix-layoffs-underway-1237156351/"},
  {"o": "TechCrunch", "d": "2026-10-14", "u": "https://techcrunch.com/2026/10/14/netflix-to-lay-off-1000-staff-amid-intensifying-competition-for-user-attention/"}
 ],
 "inds": ["tech"], "nodes": [],
 "vc": [{"ind": "tech", "node": "media", "f": "공급", "dir": "down", "k": "실제", "t": "넷플릭스 인력 6% 약 1,000명 감원"}],
 "added": "이번 블룸버그 2건·로이터 1건으로 감원 규모가 5%에서 6%, 약 1,000명으로 커졌다는 점과 제품·기술 부문 집중, 영화·TV 경영진 감원 소식이 추가됐다",
 "items": [
  I("넷플릭스, 성장 둔화에 인력 6%·약 1,000명 감원", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/netflix-to-cut-6-of-global-staff-about-1-000-jobs-wsj-says",
    "넷플릭스가 성장 둔화 속에 전체 인력의 6%인 약 1,000명을 줄이기로 하면서, 2022년 이후 최대 규모의 비용 조정에 나섰다"),
  I("WSJ '넷플릭스, 전체 일자리 약 6% 감축'", R, "2026-10-15", "https://www.reuters.com/business/world-at-work/netflix-cuts-about-6-jobs-wsj-reports-2026-10-14/",
    "WSJ가 넷플릭스의 약 6% 감원을 보도하면서, 감원이 제품·기술·법무·인사 부문에 집중된다는 점이 드러났다"),
  I("넷플릭스의 영화·TV 경영진 감원, 프로그램 편성 고민 시사", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-14/netflix-cuts-of-film-and-tv-executives-hint-at-programming-woes",
    "넷플릭스가 영화·TV 부문 경영진까지 줄이면서, 콘텐츠 편성 전략에 문제가 있다는 해석이 나오고 있다 (제목 기준)")
 ]
})

# G4-052
items.append({
 "cid": "G4-052", "attachTo": "n-tg-0217",
 "title": "메타, 오픈 웨이트 Muse Spark Open 공개…최고 모델은 비공개 유지",
 "one": "메타가 성인 대화 허용 논란을 부른 Muse Wonder에 이어 8,160억 매개변수의 오픈 웨이트 모델 Muse Spark Open을 코딩·에이전트용으로 공개하면서도 최고 모델은 닫아 두면서, 키미 K3 등과의 오픈 모델 경쟁에 다시 뛰어들었다",
 "facts": [
  "무엇이: 메타는 10월 15일 코딩과 AI 에이전트 작업용 오픈 웨이트 모델 Muse Spark Open을 공개했다 [사실]",
  "사양: 총 8,160억 개 매개변수 중 420억 개가 활성화되고 100만 토큰 문맥을 지원하며, 허깅페이스에서 내려받거나 오픈라우터·투게더AI로 쓸 수 있다 [사실]",
  "성능: 메타 자체 발표로 터미널벤치 2.1에서 76.4점을 받았지만, 키미 K3가 일부 코딩 시험에서 더 높은 점수를 냈다 [사실]",
  "전략: 블룸버그는 메타가 오픈 모델을 내놓으면서도 최고 기술은 비공개로 남겼다고 봤다 [제목]",
  "기존: 메타는 10월 12일 Muse Wonder를 공개했고, 와이어드 시험에서 노골적 성적 대화가 생성돼 성인 대화 허용 논란이 일었다 [사실]"
 ],
 "basis": "verified",
 "check": "Muse Spark Open 공개, 사양, 성능 수치는 메타 블로그·허깅페이스 블로그를 담은 검색 결과 요약으로 확인. 최고 모델 비공개 유지는 제목 기준",
 "src": [
  {"o": "Meta 리서치 블로그", "d": "2026-10-15", "u": "https://research.meta.ai/blog/muse-spark-open"},
  {"o": "Hugging Face 블로그", "d": "2026-10-15", "u": "https://huggingface.co/blog/meta-muse-spark-open"}
 ],
 "inds": ["tech"], "nodes": [],
 "vc": [{"ind": "tech", "node": "ai", "f": "공급", "dir": "up", "k": "실제", "t": "메타 오픈 웨이트 Muse Spark Open 공개"}],
 "added": "이번 블룸버그·로이터 2건으로 메타가 8,160억 매개변수의 코딩·에이전트용 오픈 웨이트 모델 Muse Spark Open을 공개하고 최고 모델은 비공개로 둔 점이 추가됐다",
 "items": [
  I("메타, 오픈 AI 모델 공개하면서 최고 기술은 비공개 유지", B, "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-15/meta-releases-open-ai-model-while-keeping-its-best-tech-closed",
    "메타가 오픈 웨이트 AI 모델을 공개하면서도 최고 성능 기술은 닫아 두면서, 개방형과 폐쇄형을 나눈 이원 전략을 택했다"),
  I("메타, 코딩·에이전트용 오픈 웨이트 Muse Spark 모델 공개", R, "2026-10-16", "https://www.reuters.com/business/meta-releases-open-weight-muse-spark-model-coding-agentic-tasks-2026-10-15/",
    "메타가 코딩과 AI 에이전트 작업용 오픈 웨이트 Muse Spark 모델을 내놓으면서, 개발자들이 허깅페이스에서 내려받아 직접 돌릴 수 있게 됐다")
 ]
})

# G4-065
items.append({
 "cid": "G4-065", "attachTo": "n-tg-0233",
 "title": "킹보드, 올해 8번째 CCL 값 인상…파나소닉 200% 이어 기판 소재 인상 확산",
 "one": "킹보드가 유리섬유 원단·원사 공급 부족을 이유로 박형 원단을 쓰는 CCL·프리프레그 값을 15% 올려 올해 8번째 인상에 나서고 파나소닉이 2027년 1월부터 일반 CCL 값을 200% 올리기로 하면서, PCB 업체들의 소재 원가 부담이 커지고 있다",
 "facts": [
  "무엇이: 킹보드 라미네이츠는 2116 이하 박형 유리섬유 원단을 쓰는 CCL과 프리프레그 값을 즉시 15% 올렸고, 올해 들어 8번째 인상이다 [사실]",
  "이유: 회사는 박형 원단 수요 증가와 전자용 유리섬유 원단·원사 공급 부족을 들었고, 씨티는 이번 인상이 모든 CCL이 아닌 고급 제품에만 적용된다고 봤다 [사실]",
  "앞선 인상: 킹보드는 8월 28일 일반 FR-4 값을 10%, 박형 프리프레그 값을 20% 올렸다 [사실]",
  "파나소닉: 파나소닉 인더스트리는 2027년 1월 출하분부터 일반 다층기판용 CCL 값을 200% 올린다고 고객사에 알렸다 [채널]",
  "기존 흐름: ASML은 한국향 EUV·DUV 교체 부품값을 2027년 1월부터 일괄 10% 올리기로 했다 [사실]"
 ],
 "basis": "partial",
 "check": "킹보드의 8번째 15% 인상과 이유, 8월 인상은 검색 결과 요약으로 확인. 파나소닉 CCL 200% 인상은 이번에 확인하지 못함(기존 채널 전언)",
 "src": [
  {"o": "DIGITIMES", "d": "2026-10-14", "u": "https://www.digitimes.com/news/a20261014PD200/kingboard-ccl-pcb-price-increase-2026.html"},
  {"o": "Futu News", "d": "2026-10-14", "u": "https://news.futunn.com/en/post/1001090124/hong-kong-stocks-movers-kingboard-laminates-01888-drops-over-6"}
 ],
 "inds": ["macro", "semis"], "nodes": ["macro/semis"],
 "vc": [
  {"ind": "semis", "node": "materials", "f": "가격", "dir": "up", "k": "실제", "t": "킹보드 박형 원단 CCL·프리프레그 15% 인상"},
  {"ind": "semis", "node": "materials", "f": "공급", "dir": "down", "k": "실제", "t": "전자용 유리섬유 원단·원사 공급 부족"}
 ],
 "added": "이번 텔레그램 1건으로 킹보드의 15% 인상이 올해 8번째이며 유리섬유 원단·원사 공급 부족 때문이라는 점과 회사의 인상 확인이 추가됐다",
 "items": [
  I("킹보드 라미네이츠, 올해 8번째 가격 인상…CCL·PP 15%", "텔레그램 하나증권 중국전략", "2026-10-14", "https://t.me/HANAchina/70407",
    "킹보드 라미네이츠가 유리섬유 원단·원사 공급 부족을 이유로 CCL과 PP 값을 15% 올리면서, 올해에만 8번째 인상으로 PCB 원가 부담이 커졌다")
 ]
})

out = {"agent": "W7", "searches_used": 16, "fetches_used": 1, "items": items, "skipped": []}
json.dump(out, open("/home/user/news-desk/data/mix-2026-10-15/out2/W7.json", "w"), ensure_ascii=False, indent=1)
print("ok", len(items))
