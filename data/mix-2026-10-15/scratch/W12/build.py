import json, re

def I(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s is not None:
        x["s"] = s
    return x

def V(ind, node, f, d, k, t):
    return {"ind": ind, "node": node, "f": f, "dir": d, "k": k, "t": t}

R, B = "로이터", "블룸버그"
items = []

# G1-039
items.append({
 "cid": "G1-039", "attachTo": "n-rtr-0240",
 "title": "EU 7년 예산 정상회의서 충돌…스웨덴 '수용 불가', 코스타가 협상 넘겨받아",
 "one": "아일랜드 의장국이 2028~34년 EU 예산을 8% 줄인 약 1조 6,220억 유로로 제시했지만 스웨덴이 순분담금 약 60% 증가를 들어 거부하고 독일·네덜란드도 부족하다고 하면서, 정상회의에서 빠른 합의가 보이지 않아 연내 타결이 늦어질 수 있다",
 "facts": [
  "무엇이: 아일랜드 의장국은 2028~34년 EU 예산을 집행위안보다 1,410억 유로(8%) 줄인 약 1조 6,220억 유로로 제안했습니다 [사실]",
  "반발: 크리스테르손 스웨덴 총리는 자국 순분담금이 약 60% 늘어난다며 거부했고, 메르츠 독일 총리는 옳은 방향이지만 여전히 크다고, 예텐 네덜란드 총리는 합의에 충분하지 않다고 했습니다 [사실]",
  "의회와 격차: 유럽의회는 1조 9,380억 유로를 요구해 아일랜드안보다 16% 많습니다 [사실]",
  "일정: 코스타 상임의장이 협상을 넘겨받아 11월 말 특별 회의를 추가했고, 결론 초안은 연내 합의 대신 적시 합의로 표현을 바꿨습니다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 스웨덴 거부 사유(순분담금 약 60% 증가), 독일·네덜란드 반응, 유럽의회 요구액, 코스타 협상 인계·11월 말 특별 회의",
 "src": [
  {"o": "France 24", "d": "2026-10-15", "u": "https://france24.com/en/europe/20261015-eu-leaders-head-for-showdown-over-bloc-budget"},
  {"o": "Euronews", "d": "2026-10-15", "u": "https://www.euronews.com/2026/10/15/eu-summit-leaders-seek-fast-solutions-to-spiralling-energy-prices"},
  {"o": "A News", "d": "2026-10-15", "u": "https://www.anews.com.tr/european-union/2026/10/15/eu-leaders-divided-over-blocs-next-long-term-budget-ahead-of-summit"}
 ],
 "inds": ["macro"], "nodes": ["macro/fiscal"],
 "vc": [V("macro", "fiscal", "수요", "down", "예상", "순기여국 반발로 EU 장기 예산 추가 삭감 압박")],
 "added": "이번 로이터 2건으로 정상회의에서 순기여국 반발이 이어지고 스웨덴이 순분담금 약 60% 증가를 들어 거부했으며 코스타 상임의장이 협상을 넘겨받은 점이 추가됐다",
 "items": [
  I("EU 정상들, 장기 예산 놓고 충돌…빠른 합의 안 보여", R, "2026-10-15", "https://www.reuters.com/business/eu-leaders-clash-over-long-term-budget-no-quick-deal-sight-2026-10-14/",
    "EU 정상들이 2028~34년 장기 예산 규모를 두고 맞서면서 아일랜드 의장국 삭감안으로도 빠른 합의가 보이지 않는다"),
  I("스웨덴, 아일랜드 의장국의 2028~34년 EU 예산안 거부", R, "2026-10-15", "https://www.reuters.com/world/europe/sweden-reject-irish-eu-presidency-proposal-2028-2034-budget-plan-2026-10-15/",
    "스웨덴이 순분담금이 약 60% 늘어난다며 아일랜드 의장국 예산안을 거부하면서 연내 합의 가능성에 의문이 커졌다"),
 ]})

# G2-003
items.append({
 "cid": "G2-003", "attachTo": "n-bbg-0085",
 "title": "에스콘디다 파업 피했지만 센티넬라는 교착…美 구리 재고 효과 약화",
 "one": "BHP가 에스콘디다 감독직 노조와 잠정합의해 파업을 피했지만 센티넬라 파업 협상은 진전이 없고 미국향 구리 차익이 톤당 약 310달러로 줄면서, 칠레 공급 불안 속에서도 구리값은 미국 물가 부담에 사흘째 내렸다",
 "facts": [
  "무엇이: BHP와 에스콘디다 감독직 노조는 정부 중재를 하루 연장해 잠정합의했고, 조합원 64%가 찬성해 36개월 계약으로 파업을 피했습니다 [사실]",
  "스펜스: BHP는 스펜스 구리광산 노조를 불법 생산 중단으로 약 860만 달러 규모 소송을 냈습니다 [사실]",
  "센티넬라: 709명이 파업 중인 안토파가스타 센티넬라의 노조는 15일 협상에서 돌파구가 없었다고 했습니다 [제목]",
  "미국 재고: 맥쿼리 추정 미국 구리 재고는 약 160만 톤, COMEX 재고는 71만 4천 톤 이상으로 세계 가시재고의 약 70%이며, 미국향 차익은 톤당 3,000달러 이상에서 약 310달러로 줄었습니다 [채널]",
  "가격: 구리값은 강한 미국 물가 지표에 사흘째 떨어졌습니다 [제목]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 에스콘디다 잠정합의·64% 찬성·36개월 계약, 스펜스 노조 제소 확인. 센티넬라 협상 결렬과 구리값 사흘째 하락은 제목, 미국 재고·차익 수치는 채널 전언",
 "src": [
  {"o": "Mining Weekly", "d": "2026-10-15", "u": "https://www.miningweekly.com/article/bhp-escondida-supervisors-reach-deal-to-avert-strike-at-chile-copper-mine-2026-10-15"},
  {"o": "MINING.COM", "d": "2026-10-14", "u": "https://www.mining.com/bhp-averts-strike-at-worlds-biggest-copper-mine-2"},
  {"o": "Discovery Alert", "d": "2026-10-15", "u": "https://discoveryalert.com/news/bhp-spence-copper-strike-lawsuit-october-2026/"}
 ],
 "inds": ["metals"], "nodes": [],
 "vc": [V("metals", "copper", "공급", "flat", "실제", "에스콘디다 잠정합의로 파업 피하고 정상 가동"),
        V("metals", "copper", "가격", "down", "실제", "미국 물가 강세에 구리값 사흘째 하락")],
 "added": "이번 텔레그램·블룸버그·로이터 12건으로 에스콘디다 잠정합의(조합원 64% 찬성)로 파업이 피해졌고 센티넬라 협상 교착, BHP의 스펜스 노조 제소, 미국향 구리 차익 축소가 추가됐다",
 "items": [
  I("에스콘디다, 협상 결렬 시 14일 파업 가능…센티넬라는 운행 트럭 급감 주장", "텔레그램 상상인 김진범", "2026-10-14", "https://t.me/PipeBeom/6697",
    "에스콘디다 노조가 1인당 약 2만 5,500달러 보너스가 부족하다며 추가 개선을 요구하면서 13일 중재 시한을 넘기면 1,000명 이상이 파업할 수 있었다"),
  I("BHP 에스콘디다 노동자들 합의안 승인, 구리 파업 피해", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/world-s-top-copper-mine-faces-strike-as-wage-talks-break-down",
    "에스콘디다 노조원들이 BHP 합의안을 승인하면서 세계 최대 구리 광산의 파업 위험이 사라졌다"),
  I("BHP 에스콘디다 감독직 노조, 계약 협상 실패로 파업 예고", R, "2026-10-14", "https://www.reuters.com/business/world-at-work/supervisors-bhps-escondida-mine-chile-strike-after-contract-talks-fail-2026-10-13/",
    "에스콘디다 감독직 노조가 계약 협상이 실패했다며 파업에 나서기로 하면서 구리 공급 차질 우려가 커졌다 (제목 기준)"),
  I("세계 최대 광산 파업 피하자 구리값 소폭 하락", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/copper-climbs-to-three-week-high-on-strike-threat-fed-comments",
    "세계 최대 구리 광산이 파업을 피하면서 공급 차질 우려가 줄어 구리값이 소폭 내렸다 (제목 기준)"),
  I("BHP-에스콘디다 감독직 노조 잠정합의…비준 위해 중재 하루 연장", "텔레그램 상상인 김진범", "2026-10-15", "https://t.me/PipeBeom/6708",
    "BHP와 감독직 노조가 처우 개선안에 잠정합의하고 비준 투표를 위해 중재를 하루 연장하면서 광산은 정상 운영을 이어갔다"),
  I("미국 구리 재고 160만 톤…관세 위협발 미국 쏠림 효과 약해져", "텔레그램 상상인 김진범", "2026-10-15", "https://t.me/PipeBeom/6709",
    "미국향 구리 차익이 톤당 3,000달러 이상에서 약 310달러로 줄면서 추가 유입 유인은 약해졌지만 쌓인 재고는 미국에 머물 수 있다"),
  I("트럼프 관세 위협이 쌓은 미국 구리 산, 효과 약해져", R, "2026-10-15", "https://www.reuters.com/world/asia-pacific/trump-tariff-threat-built-us-copper-mountain-effects-are-fading-2026-10-14/",
    "관세 위협으로 미국에 쌓인 구리가 세계 가시재고의 약 70%에 이르지만 차익 축소로 쏠림 효과가 약해지고 있다"),
  I("BHP 에스콘디다 감독직 노조, 잠정합의로 파업 피해", R, "2026-10-15", "https://www.reuters.com/business/world-at-work/bhps-escondida-supervisors-union-avert-strike-with-preliminary-agreement-2026-10-14/",
    "BHP와 에스콘디다 감독직 노조가 잠정합의에 이르면서 세계 최대 구리 광산의 파업이 회피됐다"),
  I("강한 미국 물가 지표에 매도세…구리값 사흘째 하락", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/copper-falls-for-third-day-as-strong-us-inflation-spurs-selloff",
    "미국 물가 지표가 예상보다 강하게 나오면서 금속 시장에 매도세가 이어져 구리값이 사흘째 떨어졌다 (제목 기준)"),
  I("LME 위크: 구리 공급난이 오래된 광산에 새 생명 불어넣어", R, "2026-10-15", "https://www.reuters.com/world/asia-pacific/lmeweek-copper-squeeze-breathes-new-life-into-old-mines-2026-10-15/",
    "구리 공급난과 높은 가격이 이어지면서 채산성이 낮던 오래된 광산들이 다시 살아나고 있다 (제목 기준)"),
  I("안토파가스타 센티넬라 파업 노조 '협상 돌파구 없어'", R, "2026-10-16", "https://www.reuters.com/business/world-at-work/no-breakthrough-talks-antofagastas-striking-centinela-copper-mine-unions-say-2026-10-15/",
    "센티넬라 파업 노조가 회사와의 협상에서 돌파구가 없었다고 밝히면서 칠레 구리 공급 차질이 길어질 수 있다 (제목 기준)"),
  I("BHP, 스펜스 구리광산 노조를 불법 생산 중단으로 제소", R, "2026-10-16", "https://www.reuters.com/legal/litigation/bhp-sues-union-spence-copper-mine-over-illegal-production-stoppages-lawsuit-2026-10-15/",
    "BHP가 스펜스 구리광산 노조를 불법 생산 중단 혐의로 제소하면서 칠레 광산 노사 갈등이 법정으로 번졌다"),
 ]})

# G2-004
T1 = "텔레그램 미국 주식 인사이더"
items.append({
 "cid": "G2-004", "attachTo": "n-tg-0157",
 "title": "호르무즈서 화물선 잇단 침몰…이란, 美 중간선거 앞 선박 공격 전술 전환",
 "one": "이란이 미국 중간선거를 앞두고 유가를 높게 묶어 두려 호르무즈 선박 공격을 늘리면서 싱가포르 선적 컨테이너선 GFS 프라이드가 피격 뒤 침몰하고 24시간 새 두 척이 가라앉아, 걸프 해상 운송과 원유 수출 위험이 다시 커지고 있다",
 "facts": [
  "무엇이: 싱가포르 해사항만청은 자국 선적 컨테이너선 GFS 프라이드가 정체불명 발사체에 맞아 불이 난 뒤 침몰했다고 밝혔고, 자매선 GFS 지젤도 선체가 손상됐지만 자력으로 피항했습니다 [사실]",
  "원인 공방: 이란 혁명수비대는 허가되지 않은 항로를 쓰다 기뢰에 부딪혔다고 주장했고, 해상보안 소식통은 발사체 공격으로 봤습니다 [사실]",
  "전술 전환: 이란 고위 관계자 2명은 유가를 높이고 11월 미국 중간선거에 영향을 주려 약 10일 전부터 공격 빈도·방식을 바꿨고 오만만까지 범위를 넓힐 계획이라고 했습니다 [채널]",
  "피해 규모: 최근 2주간 선박 24척이 피해를 입었고, 해양 당국은 24시간 동안 두 척이 각각 포탄에 맞아 침몰했다고 밝혔습니다 [채널]",
  "의미: GFS 프라이드는 이번 분쟁에서 두 번째로 확인된 대형 원양 선박 침몰로 보입니다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 GFS 프라이드 침몰·GFS 지젤 피격, 원인 공방, 선거 앞 공격 확대(CNN) 확인. 공격 전술 세부와 2주간 24척 피해는 채널 전언",
 "src": [
  {"o": "CNN", "d": "2026-10-15", "u": "https://www.cnn.com/2026/10/15/middleeast/strait-of-hormuz-ships-sunk-iran-intl-hnk"},
  {"o": "gCaptain", "d": "2026-10-15", "u": "https://gcaptain.com/containership-sinks-as-hormuz-attacks-spiral-out-of-control/"},
  {"o": "The National", "d": "2026-10-15", "u": "https://thenationalnews.com/news/gulf/2026/10/15/fire-sinking-and-reported-scramble-for-cargo-what-we-know-about-ship-lost-in-strait-of-hormuz"}
 ],
 "inds": ["shipping", "oil", "macro"], "nodes": ["macro/geo"],
 "vc": [V("shipping", "routes", "공급", "down", "실제", "호르무즈서 컨테이너선 피격 침몰 잇따라"),
        V("oil", "transport", "공급", "down", "예상", "이란 공격 확대로 걸프 원유 수송 차질 우려")],
 "added": "이번 텔레그램 7건·블룸버그 1건·로이터 3건으로 이란의 선거 앞 공격 전술 전환, 싱가포르 선적 GFS 프라이드 침몰, 24시간 새 두 척 침몰이 추가됐다",
 "items": [
  I("이란, 美 중간선거 앞두고 호르무즈 선박 공격 새 전술 도입", T1, "2026-10-14", "https://t.me/insidertracking/66186",
    "이란 지도부가 유가를 높이고 미국 중간선거에 영향을 주려 약 10일 전부터 선박 공격 빈도와 방식을 바꾸면서 오만만까지 작전을 넓히려 한다"),
  I("이란, 미국 선거 앞 선박 공격 강화로 전술 전환…관계자들", R, "2026-10-14", "https://www.reuters.com/world/middle-east/iran-shifting-tactics-step-up-attacks-shipping-before-us-vote-officials-say-2026-10-14/",
    "이란 관계자들이 미국 선거 전 선박 공격을 늘리는 쪽으로 전술을 바꿨다고 밝히면서 호르무즈 운항 위험이 커졌다"),
  I("혁명수비대 '컨테이너 2,500개 실은 화물선, 기뢰 충돌 뒤 침몰'", T1, "2026-10-14", "https://t.me/insidertracking/66216",
    "이란 혁명수비대가 허가되지 않은 항로를 쓴 화물선이 기뢰에 부딪혀 불이 나 가라앉았다고 주장하며 다른 선박에도 위험을 경고했다"),
  I("UKMTO '13일 호르무즈서 컨테이너선 2척 발사체 피격'", T1, "2026-10-14", "https://t.me/insidertracking/66221",
    "5만 톤급과 1만 9천 톤급 컨테이너선이 20분 간격으로 발사체에 맞았지만 피해가 경미해 항해를 이어갔고 당국이 조사에 나섰다"),
  I("호르무즈 2주간 선박 24척 피해…개전 뒤 가장 강도 높은 공격", T1, "2026-10-14", "https://t.me/insidertracking/66228",
    "최근 2주간 선박 24척이 피해를 입고 하루 최소 6척이 공격받으면서 석유 수출량이 전쟁 전의 절반 아래로 줄었다는 전언이 나왔다"),
  I("GFS 프라이드호 추정 컨테이너선 침몰 이미지 유포", "텔레그램 트릴리온", "2026-10-14", "https://t.me/Trillion_labs/10475",
    "GFS 프라이드호로 추정되는 컨테이너선이 실제로 가라앉는 이미지가 퍼지면서 기뢰 충돌이라는 이란 주장과 별개로 긴장 고조 신호가 됐다"),
  I("싱가포르 선적 선박 2척 호르무즈서 피격, 1척 침몰", R, "2026-10-14", "https://www.reuters.com/world/asia-pacific/two-singapore-registered-vessels-struck-strait-hormuz-one-sinks-2026-10-14/",
    "싱가포르 선적 GFS 프라이드와 GFS 지젤이 피격돼 프라이드는 불이 난 뒤 가라앉았고 지젤은 선체 손상 뒤 자력으로 피항했다"),
  I("WSJ '호르무즈서 UAE 화물선 2척 공격받아 침몰'", "텔레그램 상상인 김진범", "2026-10-15", "https://t.me/PipeBeom/6706",
    "호르무즈 해협에서 화물선 두 척이 공격을 받아 침몰했다는 보도가 나오면서 이란 공격 급증에 따른 해상 운송 위험이 커졌다"),
  I("공격 잦아지는 호르무즈 해협서 컨테이너선 침몰", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-14/cargo-ship-sinks-in-strait-of-hormuz-after-strike-triggers-fire",
    "호르무즈 해협 공격이 잦아지는 가운데 컨테이너선이 피격 뒤 화재로 가라앉으면서 선박 운항 위험이 높아졌다"),
  I("호르무즈 인근 24시간 새 컨테이너선·벌크선 2척 포탄 맞아 침몰", "텔레그램 트릴리온", "2026-10-15", "https://t.me/Trillion_labs/10573",
    "해양 당국이 24시간 새 컨테이너선과 벌크선이 각각 포탄에 맞아 침몰했다고 밝히면서 미국 봉쇄에 맞선 이란의 공격 강화가 드러났다"),
  I("컨테이너선, 호르무즈 인근서 발사체 맞고 침몰…소식통", R, "2026-10-15", "https://www.reuters.com/world/asia-pacific/container-ship-sinks-near-hormuz-after-being-hit-by-projectile-sources-say-2026-10-14/",
    "해상보안 소식통들이 컨테이너선 침몰을 발사체 공격 탓으로 보면서 기뢰 충돌이라는 이란 주장과 엇갈렸다"),
 ]})

# G2-031
items.append({
 "cid": "G2-031", "attachTo": "n-bbg-0078",
 "title": "러시아 10월 석유·가스 세수 10% 증가 전망…노바텍 3분기 가스 생산 4.9%↑",
 "one": "러시아의 10월 석유·가스 세수가 분기별 초과이익세 납부로 1년 전보다 약 10% 늘어난 약 1조 루블로 예상되고 노바텍의 3분기 가스 생산도 4.9% 늘었지만, 1~10월 세수는 14% 줄 전망이어서 9월 보조금발 세수 부진은 일부만 만회될 전망이다",
 "facts": [
  "무엇이: 로이터 계산으로 10월 러시아 연방 석유·가스 세수는 약 1조 루블(약 120억 달러)로 1년 전보다 약 10% 늘 전망이며, 분기마다 내는 초과이익세가 반영된 영향입니다 [사실]",
  "누계: 1~10월 석유·가스 세수는 6조 4,500억 루블로 1년 전보다 약 14% 줄 것으로 예상됩니다 [사실]",
  "기존: 9월 세수는 정유사 보조금이 3,055억 루블로 불어나 1년 전보다 22% 줄어든 4,524억 루블이었습니다 [사실]",
  "노바텍: 3분기 가스 생산은 211억 2천만 세제곱미터로 4.9% 늘었지만 가스 판매는 158억 세제곱미터로 3.1% 줄었습니다 [사실]",
  "선박: 노바텍이 쇄빙 가스선을 최소 2척 확보했다는 선박 자료가 나왔습니다 [제목]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 10월 세수 10% 증가·1~10월 14% 감소, 노바텍 3분기 가스 생산 4.9% 증가 확인. 묶음 제목의 '49%'는 주소에서 소수점이 빠진 것으로 4.9%가 맞음. 쇄빙 가스선 확보는 제목 기준",
 "src": [
  {"o": "The Moscow Times", "d": "2026-10-15", "u": "https://www.themoscowtimes.com/2026/10/15/russias-oil-and-gas-revenues-forecast-to-rise-10-year-on-year-in-october-to-12bln-a93992"},
  {"o": "LNG Prime", "d": "2026-10-14", "u": "https://lngprime.com/asia/novateks-gas-sales-down-in-q3/198412/"},
  {"o": "ChemAnalyst", "d": "2026-10-14", "u": "https://www.chemanalyst.com/NewsAndDeals/NewsDetails/novatek-output-surges-4-2-but-gas-sales-slip-as-liquids-gain-45003"}
 ],
 "inds": ["oil", "gas", "macro"], "nodes": ["gas/upstream", "gas/shipping", "macro/fiscal"],
 "vc": [V("gas", "upstream", "공급", "up", "실제", "노바텍 3분기 가스 생산 4.9% 증가"),
        V("gas", "shipping", "공급", "up", "실제", "노바텍 쇄빙 가스선 최소 2척 확보")],
 "added": "이번 로이터 3건으로 10월 석유·가스 세수 약 10% 증가 전망(1~10월은 14% 감소), 노바텍 3분기 가스 생산 4.9% 증가, 쇄빙 가스선 확보가 추가됐다",
 "items": [
  I("러시아 노바텍, 3분기 가스 생산 4.9% 증가", R, "2026-10-14", "https://www.reuters.com/business/energy/russias-novatek-says-q3-gas-output-up-49-2026-10-14/",
    "노바텍의 3분기 가스 생산이 1년 전보다 4.9% 늘었지만 가스 판매는 3.1% 줄면서 생산 증가가 판매로 이어지지 못했다"),
  I("러시아 노바텍, 쇄빙 가스선 최소 2척 확보…선박 자료", R, "2026-10-15", "https://www.reuters.com/business/energy/russias-novatek-acquires-least-two-ice-class-gas-carriers-data-shows-2026-10-14/",
    "노바텍이 쇄빙 가스선을 최소 2척 사들인 것으로 선박 자료에 나타나면서 북극 LNG 운송 능력이 늘 수 있다 (제목 기준)"),
  I("러시아 10월 석유·가스 세수 1년 전보다 10% 늘어 120억 달러 전망", R, "2026-10-15", "https://www.reuters.com/business/energy/russias-oil-gas-revenue-seen-up-10-yy-october-12-billion-2026-10-15/",
    "분기별 초과이익세 납부로 러시아 10월 석유·가스 세수가 약 1조 루블로 10% 늘 전망이지만 1~10월 누계는 14% 줄 것으로 보인다"),
 ]})

# G2-036
items.append({
 "cid": "G2-036", "attachTo": "n-bbg-0254",
 "title": "아시아 석탄값 2년여 만에 최고…中 9월 석탄 수입은 6% 감소",
 "one": "중국 탄광 안전점검 감산과 인도네시아 수출 제약 속에 아시아 발전사들이 겨울 재고 확보에 나서면서 뉴캐슬 발전용 석탄값이 2년여 만의 최고로 올랐지만, 재고가 넉넉한 중국의 9월 석탄 수입은 4,337만 톤으로 6% 줄었다",
 "facts": [
  "무엇이: 중국의 9월 석탄 수입은 4,337만 톤으로 1년 전보다 6% 줄었지만 8월 4,209만 톤보다는 늘었고, 1~9월 누계는 3억 5,354만 톤으로 2.2% 증가했습니다 [사실]",
  "원인: 해안 발전사 재고가 예년보다 많았고, 인도네시아 생산계획 조정과 칼리만탄 강 수위 저하가 수출 물량을 줄였습니다 [사실]",
  "국제 가격: 뉴캐슬 발전용 석탄값은 13일 2024년 8월 이후 최고로 올해 40% 넘게 올랐고, 모건스탠리는 장기 가격 전망을 4% 올린 톤당 125달러로 제시했습니다 [채널]",
  "중국 가격: 친황다오 발전용 석탄 현물은 9월 말 톤당 986위안으로 3년 만의 최고였습니다 [사실]"
 ],
 "basis": "partial",
 "check": "검색 결과 요약으로 중국 9월 수입 수치·원인 확인. 뉴캐슬 2년여 만의 최고와 모건스탠리 전망은 확인 못 함(채널 전언)",
 "src": [
  {"o": "Mining Weekly", "d": "2026-10-14", "u": "https://www.miningweekly.com/article/china-september-coal-imports-fall-6-on-high-inventories-indonesia-supply-constraints-2026-10-14"},
  {"o": "OilPrice.com", "d": "2026-10-14", "u": "https://oilprice.com/Latest-Energy-News/World-News/Chinas-Coal-Imports-Fall-6-as-Prices-Hit-Nearly-3-Year-High.html"}
 ],
 "inds": ["coal"], "nodes": ["coal/trade", "coal/thermal"],
 "vc": [V("coal", "trade", "가격", "up", "실제", "뉴캐슬 발전용 석탄값 2년여 만에 최고"),
        V("coal", "trade", "수요", "down", "실제", "중국 9월 석탄 수입 6% 감소")],
 "added": "이번 로이터·텔레그램 2건으로 중국 9월 석탄 수입 6% 감소(4,337만 톤)와 뉴캐슬 발전용 석탄값의 2년여 만 최고, 올해 40% 넘는 상승이 추가됐다",
 "items": [
  I("중국 9월 석탄 수입 6% 감소…높은 재고·인도네시아 공급 제약", R, "2026-10-14", "https://www.reuters.com/business/energy/china-september-coal-imports-fall-6-high-inventories-indonesia-supply-2026-10-14/",
    "중국 발전사 재고가 넉넉하고 인도네시아 수출 물량이 줄면서 9월 석탄 수입이 4,337만 톤으로 1년 전보다 6% 줄었다"),
  I("아시아 석탄값 2년여 만에 최고…올해 40% 넘게 급등", "텔레그램 하나증권 중국전략", "2026-10-14", "https://t.me/HANAchina/70431",
    "중국 감산·인도네시아 수출 제약에 겨울 재고 확보 수요가 겹치면서 뉴캐슬 발전용 석탄값이 2024년 8월 이후 최고로 올랐다"),
 ]})

# G3-015
items.append({
 "cid": "G3-015", "attachTo": "n-bbg-0237",
 "title": "쿠치넬리 연간 전망 상향·페르노리카 감소폭 축소…샤넬은 이사회 개편",
 "one": "브루넬로 쿠치넬리가 3분기 매출 13.5% 증가로 연간 성장 전망을 약 12%로 올리고 페르노리카의 1분기 매출 감소가 인도 덕에 0.9%에 그쳤지만, 미국·중국 주류 판매는 10%, 25% 줄어 유럽 명품·주류 수요의 지역별 차이가 커졌다",
 "facts": [
  "무엇이: 브루넬로 쿠치넬리의 3분기 매출은 고정환율 기준 13.5% 늘어난 3억 7,420만 유로로 예상을 조금 넘었고, 연간 매출 증가율 전망을 10~11%에서 약 12%로 올렸습니다 [사실]",
  "페르노리카: 1분기 매출은 22억 3,400만 유로로 0.9% 줄어 예상(1.7% 감소)보다 나았고, 인도는 19% 늘었지만 미국은 10%, 중국은 25% 줄었으며 연간 전망은 유지했습니다 [사실]",
  "샤넬: 패션 부문 대표 브뤼노 파블로프스키가 이사회에서 물러났지만 운영 역할은 유지하며, 이사회 독립성을 높이는 개편의 일환입니다 [사실]",
  "기존: 유럽 명품 기업 시가총액은 올해 약 3,500억 달러 줄었고 LVMH 주가는 40% 넘게 떨어졌습니다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 쿠치넬리 3분기 매출·전망 상향, 페르노리카 1분기 매출과 지역별 증감, 샤넬 파블로프스키 이사회 퇴임 확인",
 "src": [
  {"o": "FashionNetwork", "d": "2026-10-15", "u": "https://uk.fashionnetwork.com/news/Brunello-cucinelli-raises-2026-outlook-after-beating-q3-sales-forecasts,1876339.html"},
  {"o": "RTE", "d": "2026-10-15", "u": "https://www.rte.ie/news/business/2026/1015/1595486-pernod-ricard-quarterly-sales/"},
  {"o": "The Spirits Business", "d": "2026-10-15", "u": "https://www.thespiritsbusiness.com/2026/10/india-shines-for-pernod-ricard-in-q1-amid-china-us-woes/"},
  {"o": "FashionNetwork", "d": "2026-10-15", "u": "https://in.fashionnetwork.com/news/Chanel-overhaul-continues-as-fashion-head-pavlovsky-exits-board,1876116.html"}
 ],
 "inds": ["consumer"], "nodes": [],
 "vc": [V("consumer", "apparel", "수요", "up", "실제", "쿠치넬리 3분기 매출 13.5% 증가에 전망 상향"),
        V("consumer", "alcohol", "수요", "mixed", "실제", "페르노리카 인도 19% 증가 속 미국·중국 감소")],
 "added": "이번 블룸버그·로이터 4건으로 쿠치넬리의 연간 전망 상향(약 12%), 페르노리카 1분기 0.9% 감소와 인도 19% 증가, 샤넬 이사회 개편이 추가됐다",
 "items": [
  I("페르노리카 매출 감소, 인도 시장 강세로 감소폭 완화", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/pernod-ricard-sales-decline-softened-by-strength-in-india",
    "페르노리카의 1분기 매출이 0.9% 줄었지만 인도 매출이 19% 늘면서 미국·중국 부진을 일부 메웠다"),
  I("샤넬 개편 이어져…패션 대표 파블로프스키 이사회 떠나", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/chanel-overhaul-continues-as-fashion-head-pavlovsky-exits-board",
    "샤넬이 패션 대표 파블로프스키를 이사회에서 빼고 운영 역할은 유지하게 하면서 이사회 독립성 강화 개편을 이어갔다"),
  I("페르노리카 1분기 매출 예상보다 덜 줄어…중국엔 신중한 낙관", R, "2026-10-15", "https://www.reuters.com/world/china/pernod-ricard-first-quarter-sales-fall-less-than-expected-cautious-optimism-2026-10-15/",
    "페르노리카의 1분기 매출 감소가 예상보다 작았고 회사가 중국에 신중한 낙관을 보이면서 연간 전망을 유지했다"),
  I("브루넬로 쿠치넬리, 3분기 매출 예상 웃돌아 2026년 전망 상향", R, "2026-10-16", "https://www.reuters.com/business/retail-consumer/brunello-cucinelli-raises-2026-outlook-after-beating-q3-sales-forecasts-2026-10-15/",
    "쿠치넬리의 3분기 매출이 13.5% 늘어 예상을 웃돌면서 2026년 매출 증가율 전망이 약 12%로 올라갔다"),
 ]})

# G3-038
items.append({
 "cid": "G3-038", "attachTo": "n-bbg-0285",
 "title": "도미노, 주문 건수 늘었지만 객단가 하락…美 동일점포 0.3% 증가에 그쳐",
 "one": "도미노피자의 3분기 주문 건수는 늘었지만 주문당 품목 수가 줄어 미국 동일점포 매출이 0.3% 증가에 그쳤고 미국 순증 매장 목표도 125~150개로 낮아지면서, 압박받는 소비자가 외식 객단가를 줄이는 흐름이 배달 피자 수요를 누르고 있다",
 "facts": [
  "무엇이: 도미노의 3분기 미국 동일점포 매출은 0.3% 늘어 3분기 연속 1% 미만이었고, 주문 건수는 늘었지만 평균 객단가와 주문당 품목 수가 줄었습니다 [사실]",
  "글로벌: 글로벌 소매매출은 환율 제외 3.2% 늘었고, 3분기 순증 매장은 미국 26개·해외 149개였습니다 [사실]",
  "전망: 올해 미국 순증 매장 목표를 125~150개로 낮췄고, 미국 동일점포 매출은 낮은 한 자릿수 범위의 하단으로 봤습니다 [사실]",
  "수익성·환원: 환율·재프랜차이징 영향을 빼면 영업이익은 8.5% 늘었고, 3분기 가격 인상률은 1.2%, 연초 이후 자사주 매입은 약 3억 500만 달러였습니다 [채널]"
 ],
 "basis": "partial",
 "check": "검색 결과 요약으로 글로벌 소매매출 3.2%, 순증 매장 미국 26개·해외 149개, 미국 순증 목표 125~150개 확인. 영업이익 8.5%·가격 인상 1.2%·자사주 3억 500만 달러는 확인 못 함",
 "src": [
  {"o": "Motley Fool(어닝콜 녹취)", "d": "2026-10-13", "u": "https://www.fool.com/earnings/call-transcripts/2026/10/13/dominos-dpz-q3-2026-earnings-call-transcript/"},
  {"o": "Yahoo Finance(GuruFocus 요약)", "d": "2026-10-14", "u": "https://finance.yahoo.com/markets/stocks/articles/dominos-pizza-inc-dpz-q3-010024852.html"}
 ],
 "inds": ["consumer"], "nodes": [],
 "vc": [V("consumer", "dining", "수요", "mixed", "실제", "주문 건수 늘었지만 객단가 하락에 동일점포 0.3% 증가")],
 "added": "이번 텔레그램 1건으로 영업이익 8.5% 증가, 글로벌 소매매출 3.2% 증가, 미국 순증 매장 26개, 연초 이후 자사주 약 3억 500만 달러 매입이 추가됐다",
 "items": [
  I("도미노 3분기 어닝콜: 주문 건수 늘었지만 객단가 하락에 동일점포 둔화", T1, "2026-10-14", "https://t.me/insidertracking/66175",
    "도미노가 주문 건수 증가와 영업이익 8.5% 증가를 냈지만 주문당 구매량이 줄어 1.2% 가격 인상에도 동일점포 매출 성장이 제한됐다"),
 ]})

# G4-007
items.append({
 "cid": "G4-007", "attachTo": "",
 "title": "AI 안전 규제 요구 확산…게이츠·해리스 가세, 젠슨 황 '위험 AI엔 칩 중단'",
 "one": "젠슨 황 엔비디아 CEO가 위험한 AI를 만드는 고객에게 칩 공급을 끊을 수 있다고 하고 빌 게이츠가 규제 강화에 개인 자원 투입을 검토하는 등 AI 안전 요구가 커지면서, 완화된 규제를 선호하는 트럼프 행정부와 충돌할 가능성이 커지고 있다",
 "facts": [
  "무엇이: 젠슨 황은 블룸버그 인터뷰에서 위험한 AI를 만드는 고객에게 가정적으로는 칩 공급을 끊겠다면서도 먼저 대화가 필요하고 지금의 우려는 과도하다고 했습니다 [사실]",
  "게이츠: 빌 게이츠가 AI 규제 강화에 대규모 개인 자원 투입을 검토하며 아모데이 등과 논의했고, 자발적 협약을 선호하는 트럼프 행정부와 부딪힐 수 있다는 악시오스 보도가 전해졌습니다 [채널]",
  "확산: 해리스는 AI 안전장치를 마련할 시간이 줄고 있다며 미·중 협력을 촉구했고, 바이트댄스는 AI 안전팀을 꾸렸으며, 앤트로픽은 평가기관 METR에 직원 수준의 모델 접근권을 줬습니다 [제목]",
  "수급: 젠슨 황은 AI 인프라 수급 불균형이 수년간 이어질 것이라고 했습니다 [채널]"
 ],
 "basis": "partial",
 "check": "검색 결과 요약으로 젠슨 황 발언(조건부 공급 중단·대화 우선·우려 과도) 확인. 게이츠·해리스·해사비스·바이트댄스·앤트로픽 METR은 확인 못 함",
 "src": [
  {"o": "The Next Web", "d": "2026-10-14", "u": "https://thenextweb.com/news/huang-cut-off-unsafe-ai-customers"},
  {"o": "Quartz", "d": "2026-10-14", "u": "https://qz.com/nvidia-huang-cut-off-unsafe-ai-developers-chips-101426"}
 ],
 "inds": ["tech", "macro"], "nodes": ["macro/semis"],
 "vc": [V("tech", "ai", "-", "flat", "예상", "AI 안전 규제 요구 확산은 정책 논의 단계")],
 "added": "이번 10월 15~16일 텔레그램·로이터·블룸버그 4건으로 게이츠의 AI 규제 강화 자원 투입 검토, 바이트댄스 AI 안전팀 신설, 앤트로픽의 METR 접근권 부여가 추가됐다",
 "items": [
  I("재계 거물들, 위험 커지자 AI 규제 강화 목소리 키워", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/tycoons-amplify-calls-for-stronger-ai-rules-as-risks-mount",
    "재계 거물들이 AI 위험이 커진다며 더 강한 규제를 요구하면서 AI 업계에 대한 규제 압력이 높아지고 있다 (제목 기준)"),
  I("해리스 'AI 안전장치 마련할 시간 줄어'…미·중 협력 촉구", R, "2026-10-15", "https://www.reuters.com/legal/government/kamala-harris-warns-window-closing-ai-safeguards-urges-us-china-cooperation-2026-10-14/",
    "카멀라 해리스가 AI 안전장치를 마련할 시간이 줄고 있다며 미·중 협력을 촉구하면서 국제 규제 논의를 압박했다 (제목 기준)"),
  I("구글 딥마인드 해사비스 'AI 해킹은 초기 경고 사격'", R, "2026-10-15", "https://www.reuters.com/legal/litigation/google-deepminds-hassabis-calls-ai-hacks-early-warning-shots-2026-10-14/",
    "데미스 해사비스가 AI를 이용한 해킹을 초기 경고 신호로 규정하면서 AI 보안 위험에 대한 경각심을 높였다 (제목 기준)"),
  I("엔비디아 CEO '위험한 AI 만드는 고객엔 공급 끊겠다'", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-14/nvidia-ceo-says-he-would-cut-off-customers-who-build-unsafe-ai",
    "젠슨 황이 위험한 AI를 만드는 고객에게 칩 공급을 끊을 수 있다고 밝히면서 칩 공급사가 AI 안전에 관여할 여지를 내비쳤다"),
  I("젠슨 황 '위험 AI엔 칩 중단 가능…그래도 AI 개발은 가속해야'", T1, "2026-10-15", "https://t.me/insidertracking/66264",
    "젠슨 황이 공급 중단 전 협상이 먼저라며 AI 안전 우려를 성장통으로 보고 감시 기술을 위해 AI 개발을 더 가속해야 한다고 했다"),
  I("젠슨 황 'AI 인프라 부족 수년간 지속될 것'", "텔레그램 하나증권 중국전략", "2026-10-15", "https://t.me/HANAchina/70434",
    "젠슨 황이 위험 AI 고객에 칩 공급을 끊겠다면서도 AI 인프라 수급 불균형이 수년간 이어질 것이라고 해 공급 부족이 길어질 전망이다"),
  I("빌 게이츠, AI 규제 강화에 대규모 개인 자원 투입 검토", T1, "2026-10-15", "https://t.me/insidertracking/66356",
    "빌 게이츠가 AI 위험 통제를 생애 핵심 과제로 보고 규제 강화에 개인 자원을 쓰려 하면서 트럼프 행정부와 정책 충돌 가능성이 생겼다"),
  I("중국 바이트댄스, AI 안전팀 신설하고 글로벌 채용 나서", R, "2026-10-15", "https://www.reuters.com/business/media-telecom/chinas-bytedance-sets-up-ai-safety-team-launches-global-hiring-drive-2026-10-15/",
    "바이트댄스가 AI 안전팀을 만들고 세계 채용에 나서면서 중국 빅테크도 AI 안전 대응을 늘리고 있다 (제목 기준)"),
  I("앤트로픽, AI 평가기관 METR에 직원 수준 모델 접근권 부여", R, "2026-10-16", "https://www.reuters.com/business/anthropic-grants-ai-evaluator-metr-employee-level-access-its-models-2026-10-15/",
    "앤트로픽이 외부 평가기관 METR에 직원 수준의 모델 접근권을 주면서 외부 안전 검증의 범위가 넓어졌다 (제목 기준)"),
  I("속도 조절 요구 한 달 만에 AI 개발 경쟁 다시 가열", B, "2026-10-16", "https://www.bloomberg.com/news/newsletters/2026-10-15/ai-race-heats-up-again-a-month-after-calls-for-a-slowdown",
    "AI 개발 속도를 늦추자는 요구가 나온 지 한 달 만에 업계 경쟁이 다시 달아오르면서 안전 논의와 개발 경쟁이 엇갈리고 있다 (제목 기준)"),
 ]})

# G4-010
items.append({
 "cid": "G4-010", "attachTo": "",
 "title": "ASML, AI 수요 못 따라가…3분기 中 비중 23%, 美 대중 DUV 규제엔 반대",
 "one": "ASML이 고객 수요가 최소 2028년까지 공급을 웃돌 것이라고 하고 3분기 중국 비중이 23%로 높아진 가운데 CFO가 미국 MATCH 법안의 대중 DUV 판매 제한에 반대하면서, 노광장비 공급 부족과 대중 수출 규제가 실적 변수로 떠올랐다",
 "facts": [
  "무엇이: ASML의 3분기 매출은 사상 최대인 117억 유로(장비 84억 유로)였고, 고객들은 최소 2028년까지 수요가 공급을 웃돌 것이라고 했으며 일부는 2028년 주문을 냈습니다 [사실]",
  "중국: 3분기 장비 매출 중 중국 비중은 2분기 14%에서 23%로 높아졌지만 1년 전 42%보다는 낮고, 올해 전체 매출의 약 20%로 예상됩니다 [사실]",
  "규제: 로저 다센 CFO는 대중 DUV 판매를 제한하는 미국 MATCH 법안이 통과되면 중국의 자체 기술 개발만 앞당길 것이라며 반대했습니다 [사실]",
  "공급망: EU는 ASML 공급사를 살리려 중국 기업에 대한 제재를 풀 예정이라고 전해졌습니다 [제목]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 3분기 매출, 중국 비중 14%→23%, 2028년까지 수요 초과, CFO의 MATCH 법안 반대 확인. EU 제재 해제는 제목 기준. 테라팹이 2027년 이후 전망에 반영됐다는 텔레그램(HANAchina/70413)은 반도체 투자 증액이라 뺌",
 "src": [
  {"o": "TechWire Asia", "d": "2026-10-15", "u": "https://techwireasia.com/2026/10/asml-china-sales-q3-2026/"},
  {"o": "GuruFocus", "d": "2026-10-15", "u": "https://www.gurufocus.com/news/9124907/asml-holding-nv-asml-q3-2026-earnings-call-highlights-record-eur117-billion-sales-demand-outpacing-supply-through-2028"},
  {"o": "ASML 6-K(SEC)", "d": "2026-10-14", "u": "https://www.sec.gov/Archives/edgar/data/0000937966/000162828026065813/pressreleasefinancialresul.htm"}
 ],
 "inds": ["semis", "macro"], "nodes": ["macro/semis"],
 "vc": [V("semis", "equipment", "수요", "up", "예상", "고객 수요가 2028년까지 공급 웃돌 전망"),
        V("semis", "policy", "공급", "down", "예상", "미 MATCH 법안 대중 DUV 판매 제한 추진")],
 "added": "이번 10월 15~16일 텔레그램·로이터 3건으로 3분기 중국향 출하 109% 증가(비중 23%), EU의 ASML 공급사 관련 제재 완화 협상, 수요 너머를 보는 투자자 시각이 추가됐다",
 "items": [
  I("ASML, 폭발적 AI 수요 따라갈 생산능력 확대에 고전", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/asml-raises-full-year-sales-outlook-as-ai-boom-drives-demand",
    "ASML이 AI 수요 급증을 따라갈 만큼 생산능력을 늘리지 못하면서 고객 수요가 최소 2028년까지 공급을 웃돌 전망이다"),
  I("ASML CFO '대중 DUV 판매 제한하는 美 MATCH 법안은 역효과'", R, "2026-10-14", "https://www.reuters.com/technology/asml-cfo-says-us-match-act-limiting-duv-sales-china-would-be-counterproductive-2026-10-14/",
    "ASML CFO가 미국 MATCH 법안이 대중 DUV 판매를 막으면 중국의 자체 기술 개발만 앞당길 것이라며 반대 입장을 냈다"),
  I("EU, ASML 공급사 살리려 중국 기업 제재 해제 예정", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/eu-set-to-lift-sanction-on-chinese-firm-to-save-asml-supplier",
    "EU가 ASML 공급사를 지키려 중국 기업 제재를 풀기로 하면서 노광장비 공급망의 중국 의존 위험이 드러났다 (제목 기준)"),
  I("ASML 3분기 中 출하 전분기 대비 109% 급증…비중 23%", T1, "2026-10-15", "https://t.me/insidertracking/66266",
    "ASML의 3분기 중국향 장비 출하가 전 분기보다 109% 늘면서 장비 매출 중 중국 비중이 14%에서 23%로 올라갔다"),
  I("EU, ASML 공급사 위해 중국과 제재 완화 협상", "텔레그램 트릴리온", "2026-10-15", "https://t.me/Trillion_labs/10540",
    "중국 희토류에 기대는 ASML 공급사가 몇 달 안에 문을 닫을 위기에 놓이자 EU가 제재 완화를 위해 중국과 협상하고 있다는 전언이다"),
  I("ASML '완판' 전망에 투자자들, 수요 너머를 보기 시작", R, "2026-10-16", "https://www.reuters.com/business/retail-consumer/asmls-sold-out-outlook-forces-investors-look-beyond-demand-2026-10-15/",
    "ASML 장비가 사실상 다 팔렸다는 전망이 나오면서 투자자들이 수요보다 생산능력 같은 다른 변수에 주목하고 있다 (제목 기준)"),
 ]})

# G4-017
items.append({
 "cid": "G4-017", "attachTo": "",
 "title": "갈더마, ZO 15억 달러 인수…길리어드-비어·랩코프-옵코 등 헬스케어 거래 잇따라",
 "one": "갈더마가 ZO스킨헬스를 기업가치 15억 달러에 사들이고 길리어드가 비어와 최대 19억 달러 항암 제휴를, 랩코프가 옵코 자산을 최대 8억 7,200만 달러에 인수하기로 하면서, 피부·항암·진단 자산이 대형사로 모이고 있다",
 "facts": [
  "무엇이: 갈더마는 미국 피부관리 업체 ZO스킨헬스를 기업가치 15억 달러에 인수하기로 했습니다 [사실]",
  "길리어드-비어: 비어는 선급금 9천만 달러를 포함한 최대 18억 8천만 달러 규모로 이중 마스킹 T세포 인게이저 후보 3개를 길리어드와 함께 개발합니다 [사실]",
  "랩코프: 옵코헬스 사업부 일부 자산을 현금 7억 2,200만 달러와 전립선암 검사 매출에 연동한 최대 1억 5천만 달러에 사들입니다 [사실]",
  "랜시어스: 은행들이 랜시어스 거래를 뒷받침할 42억 5천만 달러 대출 주선을 두고 경쟁하고 있습니다 [제목]",
  "매도자: ZO스킨헬스를 판 곳은 블랙스톤입니다 [제목]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 갈더마 ZO 15억 달러, 길리어드-비어 최대 18억 8천만 달러(선급금 9천만 달러), 랩코프-옵코 7억 2,200만 달러+최대 1억 5천만 달러 확인. 블랙스톤 매도와 랜시어스 대출은 제목 기준",
 "src": [
  {"o": "Medical Dialogues", "d": "2026-10-14", "u": "https://medicaldialogues.in/news/industry/pharma/gilead-vir-biotechnology-sign-usd-188-billion-deal-to-develop-cancer-treatments-181355"},
  {"o": "Benzinga", "d": "2026-10-14", "u": "https://www.benzinga.com/markets/biotech/26/10/62362938/vir-biotechnology-gilead-strike-deal-for-novel-tumor-treatments"},
  {"o": "Quartz", "d": "2026-10-14", "u": "https://qz.com/gilead-vir-biotechnology-solid-tumor-cancer-deal-101526"}
 ],
 "inds": ["pharma"], "nodes": [],
 "vc": [V("pharma", "deals", "수요", "up", "실제", "갈더마 ZO 인수 등 헬스케어 인수합병 잇따라")],
 "added": "이번 10월 15일 로이터·블룸버그 3건으로 갈더마의 ZO 인수 공식 발표, 랜시어스 거래용 42억 5천만 달러 대출 경쟁, 랩코프의 옵코 자산 최대 8억 7,200만 달러 인수가 추가됐다",
 "items": [
  I("갈더마, ZO스킨헬스 약 15억 달러에 인수 합의…소식통", R, "2026-10-14", "https://www.reuters.com/world/galderma-agrees-buy-zo-skin-health-around-15-billion-sources-say-2026-10-13/",
    "갈더마가 ZO스킨헬스를 약 15억 달러에 사들이기로 하면서 미국 스킨케어 시장에서 몸집을 키운다"),
  I("블랙스톤, ZO스킨헬스를 갈더마에 15억 달러에 매각", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/galderma-expands-in-us-skincare-with-1-5-billion-purchase-of-zo",
    "블랙스톤이 ZO스킨헬스를 갈더마에 15억 달러에 팔면서 사모펀드가 피부관리 자산을 정리했다 (제목 기준)"),
  I("비어·길리어드, 고형암 치료제 최대 19억 달러 공동개발 계약", R, "2026-10-14", "https://www.reuters.com/legal/litigation/vir-gilead-team-up-solid-tumor-cancer-therapies-up-19-billion-deal-2026-10-14/",
    "길리어드가 비어에 선급금 9천만 달러를 주고 고형암 T세포 인게이저 3개를 함께 개발하기로 하면서 계약 규모가 최대 19억 달러가 됐다"),
  I("갈더마, 미국 ZO스킨헬스 15억 달러에 인수", R, "2026-10-15", "https://www.reuters.com/legal/transactional/galderma-buy-us-firm-zo-skin-health-15-billion-2026-10-14/",
    "갈더마가 ZO스킨헬스를 기업가치 15억 달러에 인수한다고 발표하면서 앞선 소식통 보도가 공식 확인됐다"),
  I("랜시어스 거래 뒷받침할 42억 5천만 달러 대출 두고 은행들 경쟁", B, "2026-10-15", "https://www.bloomberg.com/news/articles/2026-10-15/banks-vie-for-4-25-billion-debt-financing-to-back-lantheus-deal",
    "은행들이 랜시어스 거래에 쓸 42억 5천만 달러 대출 주선을 놓고 경쟁하면서 헬스케어 인수금융 수요가 드러났다 (제목 기준)"),
  I("랩코프, 옵코헬스 사업부 일부 자산 최대 8억 7,200만 달러에 인수", R, "2026-10-15", "https://www.reuters.com/legal/litigation/labcorp-buy-select-assets-opko-health-unit-up-872-million-2026-10-15/",
    "랩코프가 옵코헬스 사업부 자산을 현금 7억 2,200만 달러와 성과 연동 최대 1억 5천만 달러에 사들이면서 진단검사 사업을 넓힌다"),
 ]})

# G4-022
items.append({
 "cid": "G4-022", "attachTo": "",
 "title": "화웨이 기린 9050 양산·쿤펑 동남아 출하 최대…中 EUV 광원 국산화 90%",
 "one": "화웨이가 기린 9050 칩 양산을 공개하고 쿤펑 CPU의 동남아 출하가 1~8월 2,200개로 사상 최대를 기록한 데 이어 중국이 국산화율 90%의 EUV 광원 시제품을 내놓으면서, 미국 수출 통제 속 중국 반도체의 자체 공급이 넓어지고 있다",
 "facts": [
  "무엇이: 화웨이는 10월 13일 기린 9050 시리즈가 양산됐다고 밝혔고, 이 칩은 메이트 90 시리즈에 들어갔습니다 [사실]",
  "누적 출하: 2023년 이후 기린 칩 탑재 단말기 누적 출하는 1억 대를 넘었다고 화웨이 측이 밝혔습니다 [채널]",
  "쿤펑: 화웨이 쿤펑 CPU의 동남아 출하는 2026년 1~8월 2,200개로 2025년 연간 1,744개를 넘어섰고, 싱가포르 법인이 재수출 거점입니다 [채널]",
  "EUV 광원: 중국 랑다오수옌이 국산화율 90%의 EUV 광원 시제품을 공개했지만 양산까지는 3~5년이 걸릴 전망입니다 [채널]"
 ],
 "basis": "partial",
 "check": "검색 결과 요약으로 기린 9050 양산(글로벌타임스 10월 13일)·메이트 90 탑재 확인. 쿤펑 출하와 EUV 광원 시제품은 확인 못 함. 중국 반도체 장비 수입 급증 글(HANAchina/70384)은 반도체 투자 증액이라 뺌",
 "src": [
  {"o": "Global Times", "d": "2026-10-13", "u": "https://www.globaltimes.cn/page/202610/1372187.shtml"}
 ],
 "inds": ["semis", "macro"], "nodes": ["macro/semis"],
 "vc": [V("semis", "design", "공급", "up", "실제", "화웨이 기린 9050 양산·쿤펑 동남아 출하 최대"),
        V("semis", "equipment", "공급", "up", "예상", "중국 EUV 광원 시제품 국산화율 90%")],
 "added": "이번 10월 15일 텔레그램 1건으로 화웨이의 기린 9050 시리즈 양산 공개와 2023년 이후 기린 칩 단말기 누적 출하 1억 대 돌파가 추가됐다",
 "items": [
  I("화웨이 쿤펑 CPU 동남아 출하 1~8월 2,200개로 사상 최대", "텔레그램 TNBfolio", "2026-10-14", "https://t.me/TNBfolio/71532",
    "미국의 인텔 수출 허가 취소 뒤 화웨이 서버가 쿤펑 칩으로 바뀌면서 동남아 출하가 8개월 만에 지난해 연간치를 넘었다"),
  I("쿤펑 칩 동남아 출하, 8개월 만에 연간 최고치 경신", "텔레그램 카이에 de market", "2026-10-14", "https://t.me/cahier_de_market/10987",
    "쿤펑 칩의 동남아 출하가 1~8월 2,200개로 2023년 996개, 2025년 1,744개였던 연간 최고치를 8개월 만에 넘어섰다"),
  I("중국 EUV 광원 시제품 국산화율 90%…양산까지 3~5년", "텔레그램 하나증권 중국전략", "2026-10-14", "https://t.me/HANAchina/70420",
    "랑다오수옌이 핵심 부품 대부분을 자체 개발한 EUV 광원 시제품을 공개하면서 7nm 이하 공정 자립의 약한 고리가 좁혀질 수 있다"),
  I("화웨이, 기린 9050 시리즈 칩 양산 성공 공개", "텔레그램 하나증권 중국전략", "2026-10-15", "https://t.me/HANAchina/70440",
    "화웨이가 메이트 90 등에 들어간 기린 9050 칩 양산을 공개하면서 2023년 이후 기린 칩 단말기 누적 출하가 1억 대를 넘었다고 밝혔다"),
 ]})

# G4-030
items.append({
 "cid": "G4-030", "attachTo": "",
 "title": "오픈AI CFO '중국 AI 모델 쓰는 기업은 안전 위험 감수'",
 "one": "오픈AI의 최고재무책임자가 중국 AI 모델을 쓰는 기업들이 안전 위험을 떠안고 있다고 경고하면서, 기업 고객이 중국 AI 모델을 채택할 때 보안 검토 부담이 커질 수 있다 (제목 기준)",
 "facts": [
  "무엇이: 오픈AI 최고재무책임자가 중국 AI 모델을 쓰는 기업들이 안전 위험을 감수하고 있다고 말했습니다 [제목]",
  "배경: 앤트로픽은 9월 10일 위협 보고서에서 문샷(키미)과 딥시크가 사용자 요청을 몰래 클로드로 넘겼다고 주장했고, 중국 인터넷정보판공실은 두 회사를 조사하고 있습니다 [사실]"
 ],
 "basis": "title",
 "check": "오픈AI CFO 발언은 확인 못 해 제목 기준. 함께 묶인 텔레그램 2건(카이에 de market/11007, 나쁜양파/7829의 '오늘 클로드 보안 보고서')은 검색 결과 요약으로 9월 10일 앤트로픽 보고서의 재탕임을 확인해 items에서 뺌",
 "src": [
  {"o": "Cyber Kendra", "d": "2026-09", "u": "https://www.cyberkendra.com/2026/09/anthropic-says-kimi-users-were-secretly.html"},
  {"o": "Ynet News", "d": "2026-10", "u": "https://www.ynetnews.com/tech-and-digital/article/sjkfr8zcmg"}
 ],
 "inds": ["tech", "macro"], "nodes": ["macro/semis"],
 "vc": [V("tech", "ai", "수요", "down", "예상", "중국 AI 모델 쓰는 기업에 안전 위험 경고")],
 "items": [
  I("오픈AI CFO '중국 AI 모델 쓰는 기업은 안전 위험 감수'", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/openai-cfo-says-firms-using-chinese-ai-models-are-risking-safety"),
 ]})

# G4-045
items.append({
 "cid": "G4-045", "attachTo": "n-bbg-0222",
 "title": "미탈 '원웹이 인도 위성통신서 스타링크 앞서'…머스크·암바니 갈등 지속",
 "one": "미탈 바르티 회장이 원웹은 5년 전 신청해 지상망까지 갖췄다며 승인 순서에서 스타링크보다 앞선다고 주장하고 머스크·암바니 갈등도 이어지면서, 3사 모두 최종 승인을 기다리는 인도 위성통신 시장의 진입 순서가 정치 변수에 흔들릴 수 있다",
 "facts": [
  "무엇이: 수닐 미탈 바르티 회장은 원웹이 약 5년 전 신청했고 지상망은 3년 전부터 준비돼 있어 승인 순서에서 스타링크보다 앞서지만 아직 서비스 허가는 없다고 했습니다 [사실]",
  "현황: 스타링크·지오 위성·원웹 3곳이 위성통신 면허를 받았지만 주파수 배정과 보안 승인 등이 남아 상업 서비스는 시작하지 못했습니다 [사실]",
  "공방: 머스크는 특정 세력이 스타링크 진입을 막는다고 했고 통신부는 근거 없다고 반박했습니다 [사실]",
  "갈등: 스타링크 진입이 막히면서 머스크와 암바니가 맞서고 있다는 분석이 나왔고, 앞서 영향력 있는 힌두 단체가 스타링크 차단을 촉구했습니다 [제목]"
 ],
 "basis": "partial",
 "check": "검색 결과 요약으로 미탈 발언, 3사 면허·최종 승인 대기, 머스크 주장과 통신부 반박 확인. 머스크·암바니 갈등 분석은 제목 기준",
 "src": [
  {"o": "Forbes India", "d": "2026-10-14", "u": "https://www.forbesindia.com/article/news/bharti-significantly-ahead-of-musks-starlink-in-satcom-approvals-sunil-mittal/2999464/1"},
  {"o": "ThePrint", "d": "2026-10-14", "u": "https://theprint.in/economy/airtels-mittal-says-his-firm-ahead-of-musks-starlink-in-indias-satellite-internet-queue/3071968/"}
 ],
 "inds": ["tech"], "nodes": [],
 "vc": [V("tech", "telecom", "공급", "flat", "실제", "스타링크·지오·원웹 모두 인도 서비스 승인 대기")],
 "added": "이번 블룸버그 2건으로 원웹이 승인 순서에서 스타링크보다 앞선다는 미탈의 주장과, 스타링크 진입 지연이 머스크·암바니 갈등으로 번졌다는 분석이 추가됐다",
 "items": [
  I("억만장자 미탈 '인도 위성통신 경쟁서 원웹이 머스크 앞서'", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/ai-regulation-needed-now-before-accidents-occur-mittal-says",
    "미탈이 원웹은 5년 전 신청해 지상망까지 갖췄다며 승인 순서에서 스타링크를 앞선다고 주장하면서 인도 위성통신 선점 경쟁이 뜨거워졌다"),
  I("스타링크 진입 막히자 머스크, 인도 억만장자 암바니와 갈등", B, "2026-10-14", "https://www.bloomberg.com/news/newsletters/2026-10-14/starlink-lockout-has-elon-musk-feuding-with-indian-billionaire-mukesh-ambani",
    "스타링크의 인도 진입이 막히면서 머스크가 지오를 거느린 암바니와 맞서 인도 위성통신 승인 과정의 정치 부담이 커졌다 (제목 기준)"),
 ]})

# G4-057
items.append({
 "cid": "G4-057", "attachTo": "",
 "title": "올림푸스, FDA 6개 시설 경고장에 주가 13.6% 급락",
 "one": "미국 FDA가 품질관리 대응 미흡을 이유로 일본·독일·미국의 6개 시설에 경고장을 보내면서 올림푸스 주가가 13.6% 급락했지만, 회사는 생산·판매 제한이 없어 실적 영향도 없다고 밝혔다",
 "facts": [
  "무엇이: FDA는 10월 7일자 경고장에서 2025년 말 점검한 올림푸스 6개 시설의 Form 483 지적 사항 대응이 충분하지 않다고 했습니다 [사실]",
  "대상: 하치오지·히노데 등 일본 4곳과 독일 함부르크 올림푸스 윈터앤이베, 미국 미네소타 자이러스 ACMI입니다 [사실]",
  "영향: 회사는 생산·판매·유통 제한이나 리콜 요구가 없어 연결 실적 영향이 없다고 보고, 15영업일 안에 종합 답변을 내겠다고 했습니다 [사실]",
  "주가: 올림푸스 주가는 13.6% 내린 1,756엔을 기록했습니다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 경고장 날짜·대상 6개 시설, 생산·판매 제한 없음, 주가 13.6% 하락",
 "src": [
  {"o": "MassDevice", "d": "2026-10-13", "u": "https://www.massdevice.com/olympus-receives-fda-warning-letter-after-international-inspections/"},
  {"o": "Medical Device Network", "d": "2026-10-14", "u": "https://www.medicaldevice-network.com/news/olympus-shares-plunge-following-fda-warning-letter-over-manufacturing-failures/"}
 ],
 "inds": ["pharma"], "nodes": [],
 "vc": [V("pharma", "medtech", "가격", "down", "실제", "FDA 경고장에 올림푸스 주가 13.6% 급락"),
        V("pharma", "regulatory", "공급", "flat", "실제", "경고장에도 생산·판매 제한은 없어")],
 "items": [
  I("올림푸스 주가, FDA의 6개 시설 경고장에 급락", B, "2026-10-14", "https://www.bloomberg.com/news/articles/2026-10-14/olympus-shares-slump-on-fda-warning-letter-on-six-facilities"),
 ]})

out = {"agent": "W12", "searches_used": 16, "fetches_used": 0, "items": items,
       "skipped": [{"cid": "G2-042", "reason": "범위 밖(美 국방부의 베네수엘라 유전사 지분 35%는 8월 말~9월 초 발표된 사건의 재탕, n-tg-0051·n-tg-0060 계열)"}]}
json.dump(out, open("/home/user/news-desk/data/mix-2026-10-15/out2/W12.json", "w"), ensure_ascii=False, indent=1)

# checks
tail = re.compile(r" \((제목 기준|채널 전언)\)$")
for x in items:
    multi = len(x["items"]) > 1 or x["attachTo"]
    lo, hi = (90, 160) if multi else (80, 130)
    n = len(tail.sub("", x["one"]))
    flag = "" if lo <= n <= hi else " <-- one"
    tl = len(x["title"]); tf = "" if 20 <= tl <= 50 else " <-- title"
    print(x["cid"], "title", tl, tf, "one", n, flag)
    if "added" in x:
        a = len(tail.sub("", x["added"]))
        if not 60 <= a <= 140: print("   added", a)
    for it in x["items"]:
        if not 25 <= len(it["t"]) <= 60: print("   t", len(it["t"]), it["t"])
        if "s" in it:
            s = len(tail.sub("", it["s"]))
            if not 45 <= s <= 110: print("   s", s, it["s"][:30])
    for v in x["vc"]:
        if not 12 <= len(v["t"]) <= 45: print("   vc", len(v["t"]))
    for f in x["facts"]:
        if "|" in f or "**" in f or "{{" in f: print("   bad fact")
