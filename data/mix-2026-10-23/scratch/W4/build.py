import json
D = "2026-10-23"
BB, RT = "블룸버그", "로이터"
HANA, TRIL, INS, PIPE = "텔레그램 하나증권 중국전략", "텔레그램 트릴리온", "텔레그램 미국 주식 인사이더", "텔레그램 상상인 김진범"

def it(t, o, u, s=None):
    x = {"t": t, "o": o, "d": D, "u": u}
    if s: x["s"] = s
    return x

def vc(ind, node, f, d, k, t):
    return {"ind": ind, "node": node, "f": f, "dir": d, "k": k, "t": t}

def src(o, d, u):
    return {"o": o, "d": d, "u": u}

items = []
A = items.append

A({"cid": "G1-003", "attachTo": "",
 "title": "구찌 3분기 매출 6% 감소에 케링 주가 11% 급락…유럽 명품 밸류에이션 10년 만의 최저",
 "one": "\n".join([
  "구찌 3분기 매출이 중국 부진으로 비교 기준 6% 줄면서 케링 주가가 11% 넘게 급락했다.",
  "· 구찌 3분기 매출은 12.9억 유로로 보고 기준 4%, 비교 기준 6% 줄어 예상치 약 5.4% 감소보다 나빴다.",
  "· 구찌 직영 매장 동일 매장 매출은 9% 줄었고, 케링은 9개월간 105개 매장을 순폐점했다.",
  "· LVMH·에르메스 등 유럽 명품 대기업의 밸류에이션은 10년 만의 최저로 떨어졌다.",
  "· 에르메스·까르띠에를 떠받치던 중국 부유층 고객도 지출을 줄이고 있다.",
  "· LVMH 소속 시계 브랜드 제니스는 고가 시장으로 옮기며 인력을 줄이는 것으로 전해졌다."]),
 "facts": [
  "무엇이: 구찌 3분기 매출은 12.9억 유로로 보고 기준 4%, 비교 기준 6% 줄어 예상치(약 5.4% 감소)를 밑돌았고 케링 그룹 매출은 33.5억 유로였다 [사실]",
  "주가: 케링 주가는 실적 발표 뒤 11% 넘게 떨어졌다(ADR 약 11.9% 하락) [사실]",
  "매장: 구찌 직영 매장 동일 매장 매출은 9% 줄었고, 케링은 올해 9개월간 105개 매장을 순폐점했다 [사실]",
  "회사 전망: CFO는 올해 그룹 매출 증가 여부에 답을 피했고, 경상 영업이익률은 지난해보다 높을 것이라는 전망을 유지했다 [채널]",
  "업계: 유럽 명품 대기업 밸류에이션은 10년 만의 최저이고, 에르메스·까르띠에의 중국 부유층 고객이 지출을 줄이며, LVMH 제니스는 고가화하며 인력을 줄인다 [제목]"],
 "basis": "partial",
 "check": "구찌·케링 수치와 주가 하락은 검색 결과 요약으로 확인; 명품 밸류에이션 10년 최저, 에르메스·까르띠에 중국 고객 이탈, 제니스 인력 감축은 제목만 근거",
 "src": [src("Investing.com", "2026-10-22", "https://www.investing.com/news/transcripts/earnings-call-transcript-kering-q3-2026-shares-sink-as-gucci-recovery-lags-93CH-4967112"),
         src("BusinessDay", "2026-10-22", "https://www.businessday.co.za/world/international-companies/2026-10-22-kering-faces-setback-as-gucci-revenue-falls-in-china/"),
         src("Yahoo Finance", "2026-10-22", "https://sg.finance.yahoo.com/news/kering-slides-gucci-sales-fall-163516532.html")],
 "inds": ["consumer"], "nodes": [],
 "vc": [vc("consumer", "apparel", "수요", "down", "실제", "중국 수요 부진에 구찌 3분기 매출 6% 감소"),
        vc("consumer", "apparel", "가격", "down", "실제", "케링 주가 11% 급락, 명품 밸류에이션 10년 최저")],
 "items": [
  it("구찌, 중국 부진에 매출 실망…턴어라운드 흔들", BB, "https://www.bloomberg.com/news/articles/2026-10-22/gucci-sales-trail-estimates-on-china-slump-as-turnaround-falters",
     "구찌가 중국 수요 부진으로 3분기 매출이 시장 예상에 못 미치면서 케링이 추진해 온 구찌 회생 계획이 흔들리고 있다"),
  it("구찌 3분기 매출 5% 감소…중국 수요 약세에 회복 기대 꺾여", RT, "https://www.reuters.com/business/retail-consumer/guccis-sales-drop-5-third-quarter-weak-chinese-demand-dampens-turnaround-hopes-2026-10-22/",
     "구찌가 중국 수요 약세로 3분기 매출이 감소했다고 밝히면서 직영 매장 매출이 9% 줄고 케링의 회복 기대가 꺾였다"),
  it("구찌 3분기 매출 6% 감소, 예상의 두 배…케링 105개 순폐점", HANA, "https://t.me/HANAchina/70869",
     "하나증권은 구찌 3분기 비교 기준 매출 감소 폭이 예상의 거의 두 배였고 케링이 9개월간 105개 매장을 순폐점했다고 전했다"),
  it("유럽 명품 대기업들, 10년 만의 최저 밸류에이션", BB, "https://www.bloomberg.com/news/articles/2026-10-23/europe-luxury-lvmh-hermes-trade-at-lowest-valuations-decade",
     "LVMH·에르메스 등 유럽 명품 대기업의 밸류에이션이 10년 만의 최저로 떨어지면서 명품주 전반의 평가가 낮아졌다 (제목 기준)"),
  it("에르메스·까르띠에의 마지막 믿을 고객, 중국서 이탈", BB, "https://www.bloomberg.com/news/articles/2026-10-23/hermes-cartier-s-last-reliable-shoppers-are-retreating-in-china",
     "에르메스·까르띠에를 떠받치던 중국 부유층 고객마저 지출을 줄이면서 최상위 명품 브랜드의 중국 매출도 흔들리고 있다 (제목 기준)"),
  it("케링 주가 11% 급락…구찌 매출 감소 여파", RT, "https://www.reuters.com/business/retail-consumer/kering-shares-drop-11-gucci-sales-slide-2026-10-23/",
     "케링 주가가 구찌 3분기 매출 감소 발표 뒤 11% 급락하면서 구찌 회생 계획에 대한 시장의 의구심이 드러났다"),
  it("LVMH 시계 브랜드 제니스, 고가화하며 인력 감축…소식통", RT, "https://www.reuters.com/business/retail-consumer/lvhm-owned-watchmaker-zenith-cut-jobs-shift-upmarket-source-says-2026-10-23/",
     "LVMH 소속 시계 브랜드 제니스가 고가 시장으로 옮기면서 인력을 줄이는 것으로 전해져 명품 시계 부문의 비용 감축이 이어지고 있다 (제목 기준)")]})

A({"cid": "G1-012", "attachTo": "n-tg-0121",
 "title": "러 정유시설 공격 재개 뒤 로스네프트 올해 114차례 피격…복구 고의 지연·23일 대규모 드론 공습",
 "one": "\n".join([
  "젤렌스키가 15일 정유시설 공격 재개를 선언한 뒤 러시아 정유 피해가 로스네프트 복구 지연으로 번지고 있다.",
  "· 젤렌스키는 전력망 공격과 미국의 정보 공유 철회·스타링크 약화에 반발해 트럼프의 11일 정유시설 휴전을 깼다.",
  "· 블룸버그 집계로 우크라는 올해 러시아 정유시설을 최소 114차례 공격해 지난해 같은 기간의 두 배를 넘었다.",
  "· 로스네프트는 복구한 설비가 다시 피격되자 며칠이면 끝날 정유소 복구를 몇 달로 늦추고 있다.",
  "· 랴잔 정유소는 5월 첫 피격 뒤 절반 넘는 기간 멈췄고, 투압세는 4월부터 가동이 중단됐다.",
  "· 우크라이나는 23일 새벽 러시아 서부를 겨냥한 대규모 드론 공습을 벌였다."]),
 "facts": [
  "무엇이: 젤렌스키 대통령은 15일 FT 인터뷰에서 러시아 정유시설 공격 재개를 선언해 트럼프가 11일 발표한 정유시설 에너지 휴전을 깼고, 이후 러시아 정유 부문 피해가 커지고 있다 [사실]",
  "이유·조건: 젤렌스키는 러시아의 전력망 공격과 미국의 정보 공유 철회·스타링크 속도 저하에 반발했고, 패트리엇 지원을 공격 재중단 조건으로 걸었다 [채널]",
  "피해 규모: 블룸버그 집계로 우크라이나는 올해 러시아 정유시설을 최소 114차례 공격해 지난해 같은 기간의 두 배를 넘었고, 로스네프트 12개 정유소는 러시아 정제능력의 약 3분의 1이며 랴잔은 5월 첫 피격 뒤 절반 넘는 기간 멈췄고 투압세는 4월부터 멈췄다 [사실]",
  "로스네프트: 복구한 설비가 재피격되자 복구를 며칠에서 몇 주~몇 달로 늦추고 있고, 서방 부품 대체가 더디며, 상반기 순이익은 약 5분의 1 줄어 2,000억 루블이었다 [사실]",
  "맞공격·정치: 러시아는 우크라이나 전력망·연료 저장소 공격을 이어 갔고, 우크라이나는 23일 새벽 러시아 서부에 대규모 드론 공습을 벌였으며, 미·러는 러시아산 디젤 수출 관련 제재 완화를 논의해 왔다 [채널]"],
 "basis": "partial",
 "check": "로스네프트 복구 지연·114차례·랴잔·투압세·순이익은 검색 결과 요약(우크린폼·NV·investinglive)으로 확인; 23일 새벽 드론 공습과 푸틴의 공격 완화 모색은 확인 못 함",
 "src": [src("Ukrinform", "2026-10-22", "https://www.ukrinform.net/rubric-economy/4177209-rosneft-fears-longterm-damage-from-prolonged-war-in-ukraine-bloomberg.html"),
         src("NV", "2026-10-22", "https://english.nv.ua/russian-war/rosneft-delays-refinery-repairs-as-costs-mount-50652630.html"),
         src("investingLive", "2026-10-22", "https://investinglive.com/commodities/rosneft-stretches-refinery-repairs-from-days-to-months-as-ukraine-strikes-bite/")],
 "inds": ["oil", "macro"], "nodes": ["macro/geo"],
 "vc": [vc("oil", "refining", "공급", "down", "실제", "로스네프트 정유소 114차례 피격·복구 지연"),
        vc("macro", "geo", "공급", "down", "실제", "우크라 23일 러 서부 대규모 드론 공습")],
 "added": "텔레그램 4건 — 로스네프트 올해 114차례 피격·정유소 복구 고의 지연, 랴잔 절반 이상 가동 중단, 23일 러 서부 대규모 드론 공습 내용이 추가됨",
 "items": [
  it("로스네프트, 반복 피격에 정유소 복구 고의 지연", TRIL, "https://t.me/Trillion_labs/11162",
     "트릴리온은 블룸버그를 인용해 로스네프트가 복구 직후 재피격이 반복되자 정유소 복구를 며칠에서 몇 달로 늦추고 있다고 전했다"),
  it("우크라, 올해 러 정유시설 114차례 공격…로스네프트 압박", TRIL, "https://t.me/Trillion_labs/11163",
     "트릴리온은 우크라이나가 올해 러시아 정유시설을 최소 114차례 공격했고 랴잔 정유소는 5월 이후 절반 넘게 멈췄다고 전했다"),
  it("우크라 드론, 러시아 서부에 대규모 공격 진행", TRIL, "https://t.me/Trillion_labs/11176",
     "트릴리온은 23일 우크라이나 드론의 대규모 공격이 러시아 서부 지역에서 진행 중이라고 속보로 전해 공습이 다시 거세졌음을 알렸다"),
  it("우크라, 23일 새벽 러시아 서부 대규모 드론 공습", INS, "https://t.me/insidertracking/67083",
     "미국 주식 인사이더는 우크라이나가 23일 새벽 러시아 서부를 겨냥한 대규모 드론 공습을 벌이고 있다고 전해 같은 날 공습 소식을 뒷받침했다")]})

A({"cid": "G1-019", "attachTo": "",
 "title": "AI발 금속 수요에 광산 투자 부족…리튬 2050년 700만 톤·신규 광산 134개 필요",
 "one": "\n".join([
  "우드맥켄지와 벤치마크가 AI·전기차발 금속 수요를 광산 공급이 따라가지 못한다고 경고했다.",
  "· 우드맥켄지는 AI 전력 수요 급증에도 인허가·개발비 부담으로 신규 광산 승인이 부족하다고 봤다.",
  "· 우드맥켄지는 미국 외 시장에서 정제 구리 약 45만 톤 부족을 예상했다.",
  "· 벤치마크는 리튬 수요가 올해 211만 톤에서 2050년 약 700만 톤으로 늘어 신규 광산 134개가 필요하다고 봤다.",
  "· BHP는 구리 생산 기업 인수 비용이 급등해 광산을 직접 짓는 편이 더 싸다고 지적했다.",
  "· 코달은 서아프리카 리튬 사업 확장을 계획하고 있다고 CEO가 밝혔다 (채널 전언)"]),
 "facts": [
  "무엇이: 우드맥켄지는 AI 전력 수요 급증으로 금속 수요가 커지지만 광산 투자가 따라가지 못한다고 지적했다 [채널]",
  "구리: 미국 외 지역 구리 재고는 수요 48일분(미국 170일분 이상)에 그쳐 약 45만 톤의 정제 구리 부족이 예상되고, 향후 10년간 매년 약 85만 톤 신규 생산능력이 필요하다 [채널]",
  "리튬: 벤치마크는 리튬 수요가 올해 211만 톤에서 2050년 약 700만 톤(LCE)으로 늘어 3만 6,000톤 규모 신규 광산 134개와 1,000억 달러 이상 투자가 필요하다고 봤다 [채널]",
  "광산 인수: BHP는 구리값 상승으로 생산 기업 인수 비용이 급등해 직접 건설이 더 싸다고 지적했다 [채널]",
  "확장: 코달은 서아프리카 리튬 사업 확장을 계획하고 있다고 CEO가 밝혔다 [제목]"],
 "basis": "channel",
 "check": "mining.com 원문 2건 열람이 403으로 실패했고 검색 한도로 따로 확인 못 함; 텔레그램 요약과 로이터 제목 기준",
 "src": [],
 "inds": ["metals"], "nodes": [],
 "vc": [vc("metals", "copper", "공급", "down", "예상", "미국 외 정제 구리 약 45만 톤 부족 예상"),
        vc("metals", "battery", "수요", "up", "예상", "리튬 수요 2050년 약 700만 톤으로 증가 전망")],
 "items": [
  it("BHP '구리 광산, 인수보다 직접 건설이 더 싸다'", TRIL, "https://t.me/Trillion_labs/11132",
     "트릴리온은 구리값 상승으로 생산 기업 인수 비용이 급등해 BHP가 광산을 사기보다 직접 짓는 편이 싸다고 지적했다고 전했다"),
  it("벤치마크 '리튬 2050년 700만 톤, 신규 광산 134개 필요'", PIPE, "https://t.me/PipeBeom/6832",
     "벤치마크는 리튬 수요가 2050년 약 700만 톤으로 3배 넘게 늘어 신규 광산 134개와 1,000억 달러 이상 투자가 필요하다고 봤다"),
  it("우드맥 'AI발 금속 수요를 광산 투자가 못 따라가'", PIPE, "https://t.me/PipeBeom/6834",
     "우드맥켄지는 AI 전력 수요로 금속 수요가 커지는데 광산 승인이 부족해 미국 외 시장에서 정제 구리 약 45만 톤 부족을 예상했다"),
  it("코달, 서아프리카 리튬 사업 확장 계획…CEO", RT, "https://www.reuters.com/world/africa/kodal-plans-west-africa-lithium-expansion-ceo-says-2026-10-23/",
     "코달이 서아프리카 리튬 사업 확장 계획을 밝히면서 아프리카에서 새 리튬 공급원을 넓히려는 움직임이 이어지고 있다 (제목 기준)")]})

A({"cid": "G1-031", "attachTo": "",
 "title": "호주 스노위 2.0 수력 비용 최대 250억 호주달러로 폭증…당초 추정의 11배·완공 2029년",
 "one": "\n".join([
  "호주 대표 수력 사업 스노위 2.0의 비용이 최대 250억 호주달러(180억 달러)로 불어났다.",
  "· 블룸버그는 비용이 당초 추정의 11배가 됐다고 전했고, 당초 예산은 20억 호주달러였다.",
  "· 스노위 하이드로는 재산정 목표 비용을 222억 호주달러로 잡고 250억 호주달러 시나리오도 대비한다.",
  "· 완공 시점은 2029년 말로 밀렸고, 회사는 설계 변경·지질 악조건·인건비 상승을 원인으로 꼽았다."]),
 "facts": [
  "무엇이: 스노위 2.0 비용이 최대 250억 호주달러(약 180억 달러)로 불어나 당초 추정의 11배(로이터 기준 약 12배)가 됐다 [사실]",
  "재산정: 시공사 재산정 뒤 목표 비용은 222억 호주달러이고 250억 호주달러 시나리오를 대비하며, 회사는 222억 호주달러 전부를 납세자가 대는 것은 아니라고 밝혔다 [사실]",
  "일정·원인: 당초 20억 호주달러에 2021년 가동 예정이었으나 완공은 2029년 말로 밀렸고, 설계 변경·지질 악조건·시장·인건비 상승이 원인으로 꼽혔다 [사실]",
  "효과: GHD 연구는 이 사업이 2075년까지 도매 전력비를 70억 호주달러 넘게 낮출 것으로 봤다 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약(스노위 하이드로 발표·ABC·Proactive)으로 확인; core의 '180억 호주달러'는 미 달러 환산액이라 글에 맞춰 '최대 250억 호주달러(180억 달러)'로 고침",
 "src": [src("Snowy Hydro", "2026-10-22", "https://www.snowyhydro.com.au/news/snowy-2-0-cost-reassessment-complete/"),
         src("ABC News", "2026-10-22", "https://www.abc.net.au/news/2026-10-22/cost-of-snowy-hydro-expansion-doubles/107276162"),
         src("Proactive Investors", "2026-10-22", "https://www.proactiveinvestors.com.au/a/defdacc4/snowy-2-0-cost-blows-out-to-as-much-as-a-25-billion-as-completion-slips-")],
 "inds": ["power"], "nodes": ["power/storage"],
 "vc": [vc("power", "storage", "가격", "up", "실제", "스노위 2.0 비용 최대 250억 호주달러로 폭증"),
        vc("power", "storage", "공급", "down", "예상", "스노위 2.0 완공 2029년 말로 지연")],
 "items": [
  it("호주 대표 수력 사업, 비용이 당초 추정의 11배로", BB, "https://www.bloomberg.com/news/articles/2026-10-22/australia-s-flagship-hydro-project-now-costs-11-times-original-estimate",
     "호주 스노위 2.0 수력 사업 비용이 당초 추정의 11배로 불어나면서 정부 주도 에너지 사업의 비용 부담이 크게 늘었다"),
  it("호주 스노위 수력 사업 비용 폭증…추정 180억 달러", RT, "https://www.reuters.com/business/energy/australias-snowy-hydro-project-cost-blows-out-estimated-18-billion-2026-10-23/",
     "스노위 하이드로가 사업비를 최대 250억 호주달러(180억 달러)로 재산정하고 완공을 2029년 말로 미루면서 비용 초과가 굳어졌다")]})

A({"cid": "G1-034", "attachTo": "n-bbg-0613",
 "title": "트럼프 80억 달러 농가 디젤 지원, 선거 뒤 연말께 지급…디젤값 완화책 비용 눈덩이",
 "one": "\n".join([
  "트럼프 대통령이 발표한 80억 달러 농가 디젤 지원이 11월 3일 선거 뒤에야 지급될 전망이다.",
  "· 트럼프는 10월 19일 캔자스 유세에서 수확기 디젤 비용을 보전하는 80억 달러 지원을 발표했다.",
  "· 농무부는 상품신용공사 재원으로 2026년 작부 추정 손실에 비례해 일회성으로 지급한다.",
  "· 농무부 관리는 지급이 연말에 가까울 것이라며 정확한 시점은 아직 정해지지 않았다고 밝혔다.",
  "· 경유 전국 평균 가격은 갤런당 약 6.32달러로 9월 사상 최고 뒤에도 높은 수준이다.",
  "· 선거가 다가오면서 트럼프의 디젤값 완화책 비용은 갈수록 불어나고 있다."]),
 "facts": [
  "무엇이: 트럼프 대통령이 10월 19일 캔자스 유세에서 발표한 80억 달러 농가 디젤 지원은 11월 3일 선거 뒤, 연말께 지급될 전망이다 [사실]",
  "방식: 농무부 농업서비스청이 상품신용공사 재원으로 2026년 작부 추정 손실에 비례한 일회성 지급을 하며, 품목별 단가는 11월 발표 예정이고 작물보험 가입은 조건이 아니다 [사실]",
  "시점: 농무부 리처드 포다이스는 지급이 연말에 가까울 것이라면서도 정확한 시점은 아직 불분명하다고 밝혔다 [사실]",
  "배경: 디젤 전국 평균 가격은 갤런당 약 6.32달러로 9월 사상 최고 뒤에도 높았고, 앞서 농가 가교 지원으로 120억 달러가 지급됐다 [사실]",
  "비용: 선거가 다가오며 트럼프의 디젤값 완화책 비용이 불어나고 있다 [제목]"],
 "basis": "partial",
 "check": "선거 뒤·연말께 지급과 포다이스 발언은 검색 결과 요약으로 확인; 디젤값 완화책 비용 증가는 제목만 근거",
 "src": [src("Rallies", "2026-10-23", "https://rallies.ai/news/trump-administrations-8-billion-diesel-aid-for-farmers-will-arrive-after-election-official-says-81d0dac63053e83f"),
         src("The Hill", "2026-10-20", "https://thehill.com/homenews/administration/6159427-trump-announces-8-billion-harvest-relief/")],
 "inds": ["macro", "agri"], "nodes": ["macro/fiscal"],
 "vc": [vc("macro", "fiscal", "수요", "up", "예상", "80억 달러 농가 디젤 지원 선거 뒤 지급 전망")],
 "added": "로이터 2건 — 80억 달러 디젤 지원이 11월 3일 선거 뒤 연말께 지급될 전망, 선거 앞 디젤값 완화책 비용 증가 내용이 추가됨",
 "items": [
  it("선거 앞두고 트럼프 디젤값 완화책 비용 눈덩이", RT, "https://www.reuters.com/business/energy/trumps-diesel-price-relief-efforts-grow-costlier-election-nears-2026-10-23/",
     "선거가 다가오면서 트럼프 행정부의 디젤값 완화책 비용이 갈수록 불어나 연료값 대책의 재정 부담이 커지고 있다 (제목 기준)"),
  it("트럼프 행정부 80억 달러 농가 디젤 지원, 선거 뒤 지급…관리", RT, "https://www.reuters.com/business/energy/trump-administrations-8-billion-diesel-aid-farmers-will-arrive-after-election-2026-10-23/",
     "농무부 관리가 80억 달러 농가 디젤 지원이 11월 3일 선거 뒤 연말께 지급될 것이라고 밝히면서 농가의 비용 보전이 늦어지게 됐다")]})

A({"cid": "G1-044", "attachTo": "",
 "title": "체리, 해외 생산 차량 수출 50% 돌파 전망…캐나다 생산 검토로 미국 인접 공략",
 "one": "\n".join([
  "중국 체리자동차가 수출 차량 가운데 해외 현지 생산 비중을 올해 말 절반 넘게로 높일 전망이다.",
  "· 장구이빙 부사장은 해외 생산 차량이 올해 말 수출의 50%를 넘고 내년 60%, 2030년 70%에 이를 것으로 봤다.",
  "· 올해 수출 물량 가운데 해외 생산 비중은 약 48%다.",
  "· 체리는 중국 완성차들이 미국을 노리는 가운데 캐나다 생산을 검토하고 있다."]),
 "facts": [
  "무엇이: 체리는 해외 생산 차량이 올해 말 수출의 50%를 넘고 내년 60%, 2030년 70%에 이를 것으로 전망했다 [사실]",
  "현재: 올해 수출 물량 중 해외 생산 비중은 약 48%이며, 체리는 현지 공장이 일자리를 만들고 현지 기술 파트너와 협력할 수 있게 한다고 설명했다 [사실]",
  "캐나다: 체리는 중국 완성차들이 미국 시장을 노리는 가운데 캐나다 생산을 검토하고 있다 [제목]"],
 "basis": "partial",
 "check": "50%·60%·70%·48%는 검색 결과 요약(TimesLIVE·Finimize)으로 확인; 캐나다 생산 검토는 확인 못 함",
 "src": [src("TimesLIVE", "2026-10-23", "https://www.timeslive.co.za/motoring/2026-10-23-chery-expects-more-than-half-its-exports-to-be-built-overseas-by-year-end/"),
         src("Finimize", "2026-10-23", "https://finimize.com/content/chery-wants-most-of-its-export-cars-built-abroad")],
 "inds": ["auto"], "nodes": [],
 "vc": [vc("auto", "chinaoem", "공급", "up", "예상", "체리 해외 생산 차량 수출의 50% 돌파 전망")],
 "items": [
  it("체리, 캐나다 생산 검토…중국차 미국 주변 공략", BB, "https://www.bloomberg.com/news/articles/2026-10-23/chery-eyes-canada-production-as-chinese-carmakers-circle-the-us",
     "체리가 캐나다 생산을 검토하면서 중국 완성차들이 미국 시장과 맞닿은 지역으로 생산 거점을 넓히려 하고 있다 (제목 기준)"),
  it("중국 체리 '해외 생산 차량이 수출의 50% 넘을 것'", RT, "https://www.reuters.com/business/autos-transportation/chinas-chery-expects-overseas-manufactured-vehicles-top-50-exports-exec-says-2026-10-23/",
     "체리 경영진이 해외 생산 차량 비중이 수출의 50%를 넘을 것이라고 밝히면서 중국차 수출이 현지 생산으로 옮겨 가고 있다")]})

A({"cid": "G1-054", "attachTo": "",
 "title": "데이터센터발 설비 수요…웰스펀 美 가스관 5.8억 달러 수주·렉셀 연간 전망 재상향",
 "one": "\n".join([
  "미국 데이터센터 수요가 인도 웰스펀의 가스관 수주와 프랑스 렉셀의 실적 전망 상향으로 이어졌다.",
  "· 웰스펀 미국 법인은 퍼미안 분지 가스관용 강관을 공급하는 약 5.8억 달러 주문을 따냈다.",
  "· 이 가스관은 대형 기술기업의 데이터센터 단지로 가스를 보내며, 웰스펀 수주잔고는 52.5억 달러로 최대다.",
  "· 렉셀은 3분기 같은 영업일 기준 매출이 11.4% 늘었고 미국 데이터센터 매출은 3배 넘게 늘었다.",
  "· 렉셀은 연간 같은 영업일 매출 증가율 전망을 약 5%에서 약 7%로 다시 올렸다."]),
 "facts": [
  "무엇이: 웰스펀 미국 법인 웰스펀 튜블러는 데이터센터 단지에 가스를 보낼 퍼미안 분지 가스관용 코팅 강관 약 5.8억 달러(약 5,500크로르 루피) 주문을 따냈다 [사실]",
  "웰스펀: 강관은 미국 공장에서 만들어 2029 회계연도에 납품하며, 수주잔고는 약 52.5억 달러로 최대가 됐다 [사실]",
  "렉셀 실적: 3분기 매출은 약 54.5억 유로로 같은 영업일 기준 11.4% 늘었고, 미국 데이터센터 매출은 3배 넘게 늘어 미국 매출의 약 13%를 차지했다 [사실]",
  "렉셀 전망: 2026년 같은 영업일 매출 증가율 전망을 약 5%에서 약 7%로, 조정 EBITA 마진 하한을 6.2%에서 6.4%로 올렸지만 4분기 증가율은 약 6.5%로 둔화를 예상했다 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약(Tradebrains·Angel One, 렉셀 발표·Investing.com)으로 확인",
 "src": [src("Trade Brains", "2026-10-23", "https://tradebrains.in/indian-markets/welspun-corp-bags-5500-crore-us-gas-pipeline-order-global-order-book-hits-record-525-billion-12740320"),
         src("Rexel", "2026-10-22", "https://www.rexel.com/en/q3-2026-sales"),
         src("Investing.com", "2026-10-22", "https://www.investing.com/news/stock-market-news/rexel-sales-up-on-data-center-demand-guidance-raised-4968374")],
 "inds": ["gas", "industrial"], "nodes": ["gas/midstream"],
 "vc": [vc("gas", "midstream", "수요", "up", "실제", "웰스펀 데이터센터용 가스관 5.8억 달러 수주"),
        vc("industrial", "electrical", "수요", "up", "실제", "렉셀 미국 데이터센터 매출 3배 증가")],
 "items": [
  it("인도 웰스펀, 데이터센터 연계 美 가스관 5.8억 달러 수주", RT, "https://www.reuters.com/business/energy/indias-welspun-bags-580-million-us-gas-pipeline-order-tied-data-centre-buildout-2026-10-23/",
     "웰스펀이 데이터센터 단지로 가스를 보낼 미국 퍼미안 가스관용 강관 5.8억 달러 주문을 따내면서 수주잔고가 최대로 늘었다"),
  it("렉셀, 美 데이터센터·유럽 전기화 수요에 전망 재상향", RT, "https://www.reuters.com/business/rexel-raises-outlook-again-us-data-centre-demand-european-electrification-drive-2026-10-22/",
     "렉셀이 미국 데이터센터 매출 급증과 유럽 전기화 수요로 연간 매출 증가율 전망을 약 7%로 다시 올리면서 전기 자재 수요 강세가 드러났다")]})

A({"cid": "G1-058", "attachTo": "n-rtr-0631",
 "title": "CATL, 배터리 교환망 확대…트럭 교환소 연말 900곳·BAIC와 교환 차량 100만 대 목표",
 "one": "\n".join([
  "CATL이 대형트럭에 이어 승용차까지 배터리 교환망을 넓히며 중국 전기차 시장 공략을 서두르고 있다.",
  "· CATL은 새 대형트럭 배터리를 내놓고 교환소를 연말 900곳, 2027년 2,000곳으로 늘리겠다고 밝혔다.",
  "· CATL은 교환 시스템이 트럭 배터리를 약 5분 만에 바꿔 고속 충전보다 낫다고 봤다.",
  "· CATL과 BAIC는 22일 전략 협약을 맺고 배터리 교환 차량 100만 대를 목표로 내걸었다.",
  "· BAIC는 여러 브랜드 차량을 CATL 초콜릿 교환망에 넣고 딜러망으로 교환소 건설을 돕는다.",
  "· 폭스바겐 계열 스카니아는 운전자들이 디젤을 떠나자 중국 전기트럭 사업을 서두르고 있다."]),
 "facts": [
  "무엇이: CATL은 20일 새 대형트럭 배터리를 내놓고 대형트럭 교환소를 연말 900곳, 2027년 2,000곳, 장기적으로 1만 곳으로 늘리겠다고 밝혔다 [사실]",
  "제품: 장거리용 톈싱 II는 760kWh 배터리팩에 주행거리 600km 이상이고, 교환 시스템은 약 5분 만에 배터리를 바꾸며, 세계 대형트럭 전기화율은 아직 10% 미만이다 [사실]",
  "BAIC 협력: CATL과 BAIC는 22일 베이징에서 전략 협약을 맺고 배터리 교환 차량 100만 대를 목표로 했으며, BAIC는 여러 브랜드 차량을 초콜릿 교환망에 넣고 딜러망으로 교환소 건설을 지원한다 [사실]",
  "교환망 현황: CATL은 중국 200개 도시에서 교환소 약 2,500곳을 운영하고 장기 목표는 3만 곳이지만, 이번 협약에는 일정·교환소 수가 제시되지 않았다 [사실]",
  "경쟁: 폭스바겐의 스카니아는 운전자들의 디젤 이탈에 중국 전기트럭 사업을 서두르고 있다 [제목]"],
 "basis": "verified",
 "check": "BAIC 협약(22일, 100만 대, 초콜릿 교환망, 교환소 약 2,500곳)은 검색 결과 요약(CarNewsChina·CnEVPost·electrive)으로 확인",
 "src": [src("CarNewsChina", "2026-10-23", "https://carnewschina.com/2026/10/23/catl-and-baic-forge-strategic-partnership-to-target-1-million-battery-swapping-evs/"),
         src("CnEVPost", "2026-10-22", "https://cnevpost.com/2026/10/22/catl-battery-swap-baic-adoption/"),
         src("electrive", "2026-10-23", "https://www.electrive.com/2026/10/23/baic-and-catl-aim-to-accelerate-battery-swap-approach/")],
 "inds": ["auto"], "nodes": [],
 "vc": [vc("auto", "battery", "공급", "up", "예상", "CATL·BAIC 배터리 교환 차량 100만 대 목표")],
 "added": "블룸버그 1건 — CATL·BAIC가 배터리 교환 차량 100만 대를 목표로 승용차 교환망 협력에 나선 내용이 추가됨",
 "items": [
  it("CATL·BAIC, 새 배터리 교환망으로 차량 100만 대 목표", BB, "https://www.bloomberg.com/news/articles/2026-10-23/catl-baic-target-1-million-cars-with-new-battery-swap-network",
     "CATL과 BAIC가 새 배터리 교환망으로 차량 100만 대를 목표로 내걸면서 CATL의 교환 사업이 트럭에서 승용차로 넓어졌다")]})

A({"cid": "G1-068", "attachTo": "",
 "title": "법원, 큐리그 커피포드 독점·끼워팔기 혐의 소송 진행 판단…2027년 재판 전망",
 "one": "\n".join([
  "미국 연방법원이 커피포드 독점 혐의 소송을 끝내 달라는 큐리그의 요청을 받아들이지 않았다.",
  "· 판사는 큐리그가 커피 머신과 포드를 불법으로 끼워 팔았다는 원고 주장을 재판에서 다툴 수 있다고 봤다.",
  "· 원고 측은 50억 달러 넘는 배상을 청구하고 있어 2027년 재판이 열릴 수 있다."]),
 "facts": [
  "무엇이: 뉴욕남부연방지법 버넌 브로데릭 판사는 큐리그의 약식판결 요청을 기각해 커피 머신 시장 독점력·경쟁 침해·배타적 계약 쟁점을 배심 재판에 넘겼다 [사실]",
  "쟁점: 판사는 원고가 머신과 포드의 불법 끼워팔기를 입증할 수 있다고 봤고, 경쟁 포드에 대한 큐리그의 일부 발언은 명백히 거짓이라고 판단했다 [사실]",
  "규모: 원고 측은 50억 달러 넘는 배상을 청구해 2027년 재판이 예상되며, 큐리그는 기각된 청구들을 들어 결정에 만족한다고 밝혔다 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약(Capitol Forum·FoodBev·PYMNTS)으로 확인; 결정문은 9월 18일자로 10월에 공개됨",
 "src": [src("Capitol Forum", "2026-10", "https://thecapitolforum.com/judge-allows-monopolization-tying-claims-against-keurig-to-move-forward-setting-stage-for-2027-trial-over-5-billion-in-damages-claims/"),
         src("FoodBev", "2026-10", "https://www.foodbev.com/news/keurig-faces-jury-trial-in-long-running-coffee-pod-antitrust-case")],
 "inds": ["consumer"], "nodes": [],
 "vc": [vc("consumer", "food", "-", "flat", "예상", "큐리그 커피포드 독점 혐의 배심 재판행")],
 "items": [
  it("법원 '큐리그, 커피포드 독점 혐의 소송 받아야'", BB, "https://www.bloomberg.com/news/articles/2026-10-22/keurig-must-face-coffee-pod-monopoly-allegations-judge-says")]})

A({"cid": "G1-078", "attachTo": "",
 "title": "中 희토류 영구자석 월간 수출 올해 최고…주요 희토류 기업 3분기 실적 양호 전망",
 "one": "\n".join([
  "중신증권은 중국 희토류 영구자석 월간 수출이 올해 최고를 기록해 업황 개선이 이어질 수 있다고 봤다.",
  "· Northern Rare Earth·JL MAG 등 주요 기업의 3분기 실적 전망이 양호하고, Shenghe는 제련·분리 지분 양도 계획을 냈다.",
  "· 중국·유럽 무역 협상의 긍정 신호와 4분기 성수기·로봇 수요가 겹쳐 수급이 빡빡해질 수 있다 (채널 전언)"]),
 "facts": [
  "무엇이: 중국 희토류 영구자석 월간 수출량이 올해 들어 최고치를 기록했다 [채널]",
  "기업: Northern Rare Earth·JL MAG 등 주요 기업의 3분기 실적 전망이 양호하고, Shenghe Resources는 제련·분리 사업 지분 양도 계획을 발표해 상류 집중도가 높아질 전망이다 [채널]",
  "수요: 중국·유럽 무역 협상의 긍정 신호, 4분기 전통 성수기, 로봇 등 신흥 분야 수요 증가가 겹쳤다 [채널]"],
 "basis": "channel",
 "check": "중신증권 의견을 전한 하나증권 텔레그램 1건; 검색 한도로 따로 확인하지 않음",
 "src": [],
 "inds": ["metals"], "nodes": [],
 "vc": [vc("metals", "critical", "수요", "up", "실제", "희토류 영구자석 월간 수출 올해 최고")],
 "items": [
  it("中 희토류 영구자석 수출 올해 최고…업황 개선 기대", HANA, "https://t.me/HANAchina/70880")]})

A({"cid": "G1-088", "attachTo": "",
 "title": "SGS 3분기 매출 14.6% 늘어 19.8억 스위스프랑…유기적 성장 5.7%·연간 전망 유지",
 "one": "\n".join([
  "스위스 검사·인증 기업 SGS의 3분기 매출이 14.6% 늘어 19.82억 스위스프랑을 기록했다.",
  "· 유기적 성장률은 5.7%로 2분기 5.9%보다 조금 낮아졌고, 인수 효과가 6.9%를 보탰다.",
  "· SGS는 올해 유기적 매출 성장 5~7%와 조정 영업이익률 16% 전망을 유지했다."]),
 "facts": [
  "무엇이: SGS 3분기 매출은 19.82억 스위스프랑으로 14.6% 늘었고 유기적 성장 5.7%, 인수 효과 6.9%, 환율 효과 2%였다 [사실]",
  "지역: 아시아태평양은 유기적으로 9.3% 늘었지만 유럽은 2.4%에 그쳤고, 일부 유럽 산업 시장 약세와 중동 변동성이 언급됐다 [사실]",
  "전망: 2026년 유기적 매출 성장 5~7%, 조정 영업이익률 16% 목표를 유지하고 예상 인수 효과는 높였다 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약(RTTNews·Yahoo Finance·Investing.com 콜 전문)으로 확인",
 "src": [src("RTTNews", "2026-10-23", "https://www.rttnews.com/3702153/sgs-q3-sales-rise.aspx"),
         src("Yahoo Finance", "2026-10-23", "https://finance.yahoo.com/markets/stocks/articles/sgs-beats-q3-revenue-estimates-060308898.html")],
 "inds": ["industrial"], "nodes": [],
 "vc": [vc("industrial", "services", "수요", "up", "실제", "SGS 3분기 유기적 성장 5.7%, 연간 전망 유지")],
 "items": [
  it("검사기업 SGS, 3분기 매출 증가…연간 전망 유지", RT, "https://www.reuters.com/business/testing-firm-sgs-posts-higher-q3-sales-confirms-outlook-2026-10-23/")]})

A({"cid": "G1-098", "attachTo": "",
 "title": "폭스바겐, JSW와 파트너 협상 중 인도 전기차 투자 동결…저가 EV 플랫폼은 대기",
 "one": "\n".join([
  "폭스바겐그룹이 인도 JSW그룹과 제휴 협상이 이어지는 동안 인도 전기차 사업 추가 투자를 멈췄다.",
  "· 폭스바겐은 설계 작업을 마쳐 협상이 진전되면 기존 저가 전기차 플랫폼으로 빠르게 추진할 수 있다.",
  "· 인도 법인은 지난해 11월 전기차 플랫폼 비용을 10억 달러에서 약 7억 달러로 줄였다."]),
 "facts": [
  "무엇이: 폭스바겐그룹은 인도 JSW그룹의 구체적 제휴안을 기다리며 인도 전기차 사업 추가 투자를 멈췄다 [사실]",
  "준비: 관련 설계 작업은 끝났고, 협상이 진전되면 앞서 개발한 저가 전기차 플랫폼으로 빠르게 추진할 수 있다 [사실]",
  "배경: 인도 법인은 2025년 11월 전기차 플랫폼 비용을 10억 달러에서 약 7억 달러로 줄였고, 앞서 마힌드라와의 협상은 결렬됐다 [사실]"],
 "basis": "partial",
 "check": "투자 동결과 JSW 협상은 블룸버그를 인용한 KuCoin 요약 등 검색 결과 요약으로 확인(2차 인용); 비용 축소는 electrive·Business Standard 요약으로 확인",
 "src": [src("KuCoin News", "2026-10-23", "https://www.kucoin.com/news/flash/volkswagen-pauses-india-ev-investment-amid-jsw-partnership-talks"),
         src("Business Standard", "2025-11-19", "https://www.business-standard.com/industry/auto/volkswagen-pares-india-ev-development-costs-amid-hunt-for-partner-125111900085_1.html")],
 "inds": ["auto"], "nodes": [],
 "vc": [vc("auto", "oem", "공급", "down", "예상", "폭스바겐 인도 전기차 추가 투자 동결")],
 "items": [
  it("폭스바겐, 파트너 협상 이어지며 인도 전기차 투자 동결", BB, "https://www.bloomberg.com/news/articles/2026-10-23/volkswagen-freezes-india-ev-investment-as-partner-talks-continue")]})

A({"cid": "G1-108", "attachTo": "",
 "title": "中 에너지국, 석유·가스 기업에 증산·전략 공급기지 구축 지시…투자·탐사 확대 촉구",
 "one": "\n".join([
  "중국 국가에너지국이 석유·가스 기업에 생산능력 확대와 국가 전략 공급기지 구축을 주문했다.",
  "· 국가에너지국은 투자·탐사를 늘려 원유는 꾸준히, 천연가스는 빠르게 늘리라고 요구했다.",
  "· 중국 원유 생산은 지난해 2.16억 톤으로 최대였고, 2030년 석유·가스 공급 하한은 4.4억 톤이다."]),
 "facts": [
  "무엇이: 중국 국가에너지국은 석유·가스 기업에 투자·탐사를 늘려 생산능력을 키우고 국가 전략 석유·가스 공급기지 조성을 서두르라고 주문했다 [사실]",
  "목표: 원유 생산은 꾸준히, 천연가스 생산은 빠르게 늘리는 것이 목표다 [사실]",
  "배경: 중국 원유 생산은 지난해 2.16억 톤으로 최대였고, 2030년 국내 석유·가스 공급 하한은 석유환산 4.4억 톤(2025년 4.2억 톤)이며, 성숙 유전 감산과 신규 개발비 상승 압박이 있다 [사실]"],
 "basis": "verified",
 "check": "지시 내용은 검색 결과 요약(로이터 전재 요약 포함)으로, 배경 수치는 SCMP·Mysteel·megaproject 요약으로 확인",
 "src": [src("SCMP", "2026", "https://www.scmp.com/economy/china-economy/article/3361437/china-hits-record-oil-and-gas-output-so-why-it-warning-dual-squeeze"),
         src("Mysteel", "2026", "https://www.mysteel.net/analysis/5143249-chinas-first-standalone-oil-and-gas-five-year-plan-shifts-the-focus-from-volume-to-security-and-transition")],
 "inds": ["oil", "gas"], "nodes": ["gas/upstream"],
 "vc": [vc("oil", "nonopec", "공급", "up", "예상", "중국 석유·가스 증산·전략 공급기지 구축 지시"),
        vc("gas", "upstream", "공급", "up", "예상", "중국 천연가스 생산 빠른 증가 목표")],
 "items": [
  it("中, 석유·가스 기업에 증산·전략 공급기지 구축 촉구", RT, "https://www.reuters.com/business/energy/china-calls-oil-gas-firms-boost-output-build-strategic-supply-bases-2026-10-23/")]})

A({"cid": "G2-010", "attachTo": "",
 "title": "메타, 사기 광고 소송·새 약관 반발 잇따라…로드아일랜드 제소·뉴멕시코 변호인 최대 12.7억 달러",
 "one": "\n".join([
  "메타가 미국 주정부 소송과 유럽 광고업계 반발 등 법적·규제 압박에 잇따라 부딪혔다.",
  "· 출판·광고업계는 EU·영국 경쟁 당국에 메타 새 상업 약관 중단을 요청했고, 메타는 시행을 미뤘다.",
  "· 로드아일랜드주는 메타가 사기 광고를 방치했다며 미국 주 가운데 처음으로 제소했다.",
  "· 뉴멕시코주의 메타 소송을 맡은 외부 변호인들은 최대 12.7억 달러의 보수를 받을 수 있다.",
  "· 메타는 AI 사업이 커지는 가운데 의결권 없는 새 주식 클래스를 만들고 있다.",
  "· 메타는 23일 개인 AI 에이전트 Muse를 북미 밖 첫 시장인 일본에 내놨다."]),
 "facts": [
  "무엇이: 출판·광고업계는 EU·영국 경쟁 당국에 메타의 새 상업 약관 중단을 요청했고, 메타는 비판받은 새 약관 시행을 미뤘다 [제목]",
  "로드아일랜드: 22일 주 법원에 사기 광고 방치 혐의로 메타를 제소했고, 소장은 메타가 매일 고위험 사기 광고 약 150억 건을 노출한다고 주장했으며 메타는 지난 1년간 사기 광고 1.59억 건 넘게 지웠다며 반박했다 [사실]",
  "뉴멕시코·주식: 뉴멕시코주 메타 소송의 외부 변호인은 최대 12.7억 달러 보수를 받을 수 있고, 메타는 AI 성장 속 무의결권 신주 클래스를 만든다 [제목]",
  "Muse: 메타는 10월 23일 일본에서 AI 에이전트 Muse를 iOS·안드로이드·웹으로 내놨고, 기본 기능은 무료이며 메르카리·머니포워드 ME·티켓피아와 연동한다 [사실]"],
 "basis": "partial",
 "check": "로드아일랜드 제소는 검색 결과 요약(보스턴글로브·Engadget), Muse 일본 출시는 메타 일본 뉴스룸 열람으로 확인; 뉴멕시코 변호인 보수·무의결권주·약관 시행 연기는 제목만 근거",
 "src": [src("Boston Globe", "2026-10-22", "https://www.bostonglobe.com/2026/10/22/metro/rhode-island-lawsuit-meta-facebook-instagram-false-advertising/"),
         src("Engadget", "2026-10-22", "https://www.engadget.com/2294778/rhode-island-sues-meta-over-its-approach-to-scam-ads/"),
         src("Meta 뉴스룸(일본)", "2026-10-23", "https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan")],
 "inds": ["tech"], "nodes": [],
 "vc": [vc("tech", "platforms", "-", "flat", "예상", "메타 사기 광고 제소·새 약관 시행 연기"),
        vc("tech", "ai", "공급", "up", "실제", "메타 AI 에이전트 Muse 일본 출시")],
 "items": [
  it("출판·광고업계, EU·영국 경쟁당국에 메타 새 약관 중단 요청", RT, "https://www.reuters.com/legal/litigation/publishers-advertisers-call-eu-uk-antitrust-regulators-suspend-metas-new-2026-10-22/",
     "출판·광고업계가 EU·영국 경쟁 당국에 메타의 새 상업 약관을 멈춰 달라고 요청하면서 메타 광고 거래 조건이 규제 심사대에 올랐다 (제목 기준)"),
  it("로드아일랜드주, 사기 광고 방치 혐의로 메타 제소", RT, "https://www.reuters.com/world/rhode-island-sues-meta-over-alleged-tolerance-scam-advertising-2026-10-22/",
     "로드아일랜드주가 사기 광고 방치 혐의로 미국 주 가운데 처음 메타를 제소하면서 메타 광고 사업의 법적 위험이 커졌다"),
  it("메타 AI 에이전트 Muse 일본 출시…북미 외 첫 시장", INS, "https://t.me/insidertracking/67078",
     "메타가 개인 AI 에이전트 Muse를 일본에 내놓고 메르카리·티켓피아 등과 연동하면서 서비스를 북미 밖으로 처음 넓혔다"),
  it("뉴멕시코 메타 소송 외부 변호인, 최대 12.7억 달러 보수 가능", RT, "https://www.reuters.com/world/new-mexicos-outside-lawyers-could-collect-up-127-billion-meta-case-2026-10-23/",
     "뉴멕시코주의 메타 소송을 맡은 외부 변호인들이 최대 12.7억 달러를 받을 수 있게 되면서 주정부 소송의 규모가 드러났다 (제목 기준)"),
  it("메타는 왜 AI 성장 속 무의결권 신주 클래스를 만드나", RT, "https://www.reuters.com/business/why-is-meta-creating-new-class-non-voting-shares-amid-its-ai-growth-2026-10-23/",
     "메타가 AI 사업 성장 속에 의결권 없는 새 주식 클래스를 만들면서 주주 의결권 구조 변화에 관심이 쏠렸다 (제목 기준)"),
  it("메타, 출판·광고업계 비판 받은 새 상업 약관 시행 연기", RT, "https://www.reuters.com/business/media-telecom/meta-delay-new-commercial-terms-criticised-by-publishers-advertisers-2026-10-23/",
     "메타가 출판·광고업계의 비판을 받은 새 상업 약관 시행을 미루면서 EU·영국 규제 압박에 일단 물러섰다 (제목 기준)")]})

A({"cid": "G2-026", "attachTo": "",
 "title": "신용시장 균열…나비엔트 CDS 8년 만에 최대 확대·정크 급락에 아리니 손실·AT1 매력 하락",
 "one": "\n".join([
  "신용시장에서 나비엔트 CDS 급등과 정크 급락, 은행 AT1 매력 하락이 한꺼번에 나타났다.",
  "· 나비엔트 CDS는 채권자들이 거래에서 배제되면서 8년 만에 가장 크게 벌어졌다.",
  "· 정크 채권 급락으로 아리니의 손실이 커졌고 소나는 그동안의 수익을 반납했다.",
  "· 투자자들이 까다로워지면서 AT1의 쉬운 수익 시기가 끝나고 은행 조달비용이 올랐다.",
  "· 사모펀드의 늦은 자산 평가는 공정성·신뢰 논쟁을 키우고 있다 (제목 기준)"]),
 "facts": [
  "무엇이: 나비엔트 CDS가 채권자들이 배제되면서 8년 만에 가장 크게 확대됐다 [제목]",
  "정크: 정크 채권 급락으로 아리니의 손실이 불어났고 소나는 수익을 모두 반납했다 [제목]",
  "AT1: 투자자들이 선별적으로 바뀌면서 은행 최고위험 증권의 쉬운 수익 시기가 끝나고 은행이 더 비싼 값을 치르고 있다 [제목]",
  "사모펀드: 오래된 자산 평가가 공정성·신뢰 논쟁을 키우고 있다 [제목]"],
 "basis": "title",
 "check": "나비엔트 CDS를 검색했으나 관련 결과가 없어 블룸버그 제목 기준으로 씀",
 "src": [],
 "inds": ["fin"], "nodes": [],
 "vc": [vc("fin", "assetmgmt", "가격", "down", "실제", "정크 급락에 아리니 손실 확대·소나 수익 반납"),
        vc("fin", "banks", "가격", "up", "실제", "AT1 투자자 선별에 은행 조달비용 상승")],
 "items": [
  it("나비엔트 CDS 8년 만에 최대 확대…채권자 배제 여파", BB, "https://www.bloomberg.com/news/articles/2026-10-22/navient-cds-widen-by-most-in-eight-years-as-debtholders-left-out",
     "나비엔트 CDS가 채권자들이 거래에서 빠지면서 8년 만에 가장 크게 벌어져 회사채 보유자의 손실 우려가 커졌다 (제목 기준)"),
  it("정크 급락에 아리니 손실 확대·소나 수익 반납", BB, "https://www.bloomberg.com/news/articles/2026-10-22/rapid-junk-rout-amplifies-arini-s-losses-and-erases-sona-s-gains",
     "정크 채권이 빠르게 급락하면서 운용사 아리니의 손실이 커지고 소나는 그동안 쌓은 수익을 모두 잃었다 (제목 기준)"),
  it("은행 최고위험 증권 AT1, 투자자 선별에 매력 하락", BB, "https://www.bloomberg.com/news/articles/2026-10-23/at1s-easy-money-run-fades-as-banks-pay-up-for-riskiest-debt",
     "투자자들이 AT1 같은 은행 최고위험 증권을 가려 사기 시작하면서 쉬운 수익 시기가 끝나고 은행 조달비용이 올라갔다 (제목 기준)"),
  it("사모펀드 평가 지연, 공정성·신뢰 논쟁 키워", BB, "https://www.bloomberg.com/news/newsletters/2026-10-23/private-equity-s-stale-marks-fuel-debate-over-fairness-trust",
     "사모펀드가 자산 가치를 늦게 고쳐 매기면서 투자자 간 공정성과 평가 신뢰를 둘러싼 논쟁이 커지고 있다 (제목 기준)")]})

A({"cid": "G2-045", "attachTo": "",
 "title": "유니트리 상장 후 첫 상한가…이번 주 46% 상승·창업자 '로봇 돌파구 2028년 가능'",
 "one": "\n".join([
  "중국 로봇 기업 유니트리가 상장 뒤 처음 상한가를 기록하며 이번 주에만 46% 넘게 올랐다.",
  "· 23일 주가는 20% 상한가였고, 기관 순매수는 2.41억 위안이었다.",
  "· 테슬라 옵티머스 양산 가속과 엔비디아 로봇 플랫폼 확대 소식이 휴머노이드 업종 강세를 이끌었다.",
  "· 창업자는 로봇 기술의 돌파구가 이르면 2028년에 올 수 있다고 봤다 (채널 전언)"]),
 "facts": [
  "무엇이: 유니트리는 23일 상장 후 처음 20% 상한가를 기록해 이번 주 누적 46.14% 올랐고 기관 순매수는 2.41억 위안이었다 [채널]",
  "배경: 중국 로봇 완제품 생산 증가, 테슬라 옵티머스 양산 가속, 엔비디아 로봇 개발 플랫폼 확대 소식이 호재로 꼽혔다 [채널]",
  "전망: 유니트리 창업자는 로봇 돌파구가 이르면 2028년 올 수 있다고 내다봤다 [제목]"],
 "basis": "channel",
 "check": "검색 한도로 따로 확인하지 않음; 하나증권 텔레그램 원문과 블룸버그 제목 기준",
 "src": [],
 "inds": ["industrial"], "nodes": [],
 "vc": [vc("industrial", "robotics", "가격", "up", "실제", "유니트리 상장 후 첫 상한가, 주간 46% 상승")],
 "items": [
  it("유니트리 창업자 '로봇 돌파구 이르면 2028년'", BB, "https://www.bloomberg.com/news/articles/2026-10-23/unitree-founder-now-expects-robots-breakthrough-as-soon-as-2028",
     "유니트리 창업자가 로봇 기술 돌파구 시점을 이르면 2028년으로 내다보면서 휴머노이드 상용화 시점에 대한 기대가 앞당겨졌다 (제목 기준)"),
  it("유니트리 상장 후 첫 상한가…이번 주 46% 상승", HANA, "https://t.me/HANAchina/70919",
     "유니트리가 23일 상장 후 첫 20% 상한가를 기록해 이번 주 46.14% 오르는 동안 기관 순매수가 2.41억 위안 들어왔다")]})

A({"cid": "G2-055", "attachTo": "",
 "title": "호주 Zip, 미국 사기 사건 비용 공개에 주가 장중 50% 폭락…종가 29.5% 하락",
 "one": "\n".join([
  "호주 후불결제 기업 Zip이 미국 사기 사건 비용을 공개하자 주가가 장중 50% 넘게 폭락했다.",
  "· Zip은 1분기 미국에서 정상 인증정보로 계좌를 연 조직적 사기로 720만 달러 비용이 들었다고 밝혔다.",
  "· 그룹 순대손율은 거래액의 1.97%로 1년 전 1.65%에서 올랐다.",
  "· 주가는 2년 반 만의 최저인 1.025호주달러까지 떨어졌다가 29.5% 내린 1.46호주달러에 마감했다."]),
 "facts": [
  "무엇이: Zip 주가는 23일 미국 사기 사건 공개 뒤 장중 50.5% 떨어져 1.025호주달러까지 밀렸다가 29.5% 내린 1.46호주달러에 마감했다 [사실]",
  "사건: 조직적 사기범들이 정상 인증정보로 새 계좌를 열어 대금을 갚지 않았고, 7~8월 거래액·신규 고객 증가가 둔화됐으며 현금 영업비용 720만 달러(1,010만 호주달러)가 들었다 [사실]",
  "건전성: 그룹 순대손율은 거래액의 1.97%(1년 전 1.65%), 미국은 1.93%였다 [사실]",
  "전망: Zip은 2027 회계연도 현금 EBTDA 가이던스 3.4억 호주달러를 유지했고, 9월 미국 거래액은 41% 늘었다 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약(Rask Media·The420·Traders Union)으로 확인",
 "src": [src("Rask Media", "2026-10-23", "https://www.raskmedia.com.au/2026/10/23/zip-asxzip-share-price-sinks-29-on-weak-fy27-first-quarter-fraud-event/"),
         src("The420.in", "2026-10-23", "https://the420.in/zip-shares-plunge-us-fraud-bad-debt/")],
 "inds": ["fin"], "nodes": [],
 "vc": [vc("fin", "payments", "가격", "down", "실제", "Zip 주가 미국 사기 사건에 장중 50% 폭락")],
 "items": [
  it("Zip, 미국 사기 사건 비용 경고에 주가 급락", BB, "https://www.bloomberg.com/news/articles/2026-10-23/zip-shares-slide-50-after-flagging-costs-tied-to-us-fraud-event",
     "Zip이 미국 사기 사건 관련 비용을 공개하자 주가가 장중 50% 넘게 떨어지면서 후불결제 업체의 고객 심사 통제에 대한 우려가 커졌다"),
  it("호주 Zip, 사기 사건에 1분기 고객 증가 타격…주가 50% 급락", RT, "https://www.reuters.com/legal/government/australias-zip-tumbles-50-after-fraud-incident-dents-first-quarter-customer-2026-10-23/",
     "Zip은 미국 사기 사건이 1분기 거래액과 신규 고객 증가를 깎았다고 밝혔고, 주가는 2년 반 만의 최저로 떨어졌다")]})

A({"cid": "G2-072", "attachTo": "n-bbg-0542",
 "title": "뉴질랜드, 선거 전 금리 인상 유력…3분기 CPI 3.7%·10월 28일 3%로 인상 전망",
 "one": "\n".join([
  "뉴질랜드 물가 압력이 커지면서 11월 7일 총선을 앞둔 10월 28일 기준금리 인상이 유력해졌다.",
  "· 뉴질랜드 2분기 물가 상승률은 4.1%였고, 3분기 CPI는 3.7%로 중앙은행 예상보다 낮았다.",
  "· 이코노미스트 다수는 10월 28일 기준금리를 0.25%p 올려 3%로 만들고 12월 추가 인상을 예상한다.",
  "· ASB는 4분기 물가 상승률 전망을 4.7%로 높였고, 시장의 10월 인상 확률은 81%로 올랐다.",
  "· 3분기 CPI는 약세를 이어 온 뉴질랜드달러의 방향을 가를 시험대로 꼽혔다."]),
 "facts": [
  "무엇이: 이코노미스트들은 뉴질랜드중앙은행이 11월 7일 총선 10일 전인 10월 28일 기준금리를 0.25%p 올려 3%로 만들 가능성이 크다고 봤다 [사실]",
  "물가: 2분기 물가 상승률은 4.1%, 3분기는 3.7%로 중앙은행 예상보다 낮았지만 ASB는 4분기 4.7%를 전망했다 [사실]",
  "시장·이견: 10월 인상 확률은 지난주 초 56%에서 81%로 올랐고, 웨스트팩은 10월 동결 뒤 12월 인상 전망에서 10월 인상으로 돌아섰으며 ANZ는 선거 시점이 고려 대상이 아니라고 봤다 [사실]",
  "환율: 3분기 CPI 결과가 약세를 이어 온 뉴질랜드달러의 방향을 가를 시험대로 꼽혔다 [제목]"],
 "basis": "verified",
 "check": "검색 결과 요약(interest.co.nz·ING·FXStreet)으로 확인",
 "src": [src("interest.co.nz", "2026-10", "https://www.interest.co.nz/economy/140789/temporary-reprieve-37-september-year-cpi-inflation-doesnt-see-economists-pull-back"),
         src("ING Think", "2026-10", "https://think.ing.com/articles/rbnz-to-hike-next-week-as-inflation-risks-mount"),
         src("FXStreet", "2026-10-23", "https://www.fxstreet.com/news/new-zealand-dollar-gains-ground-to-near-05700-on-rbnz-rate-hike-prospects-202610230235")],
 "inds": ["macro"], "nodes": ["macro/cb", "macro/rates"],
 "vc": [vc("macro", "cb", "가격", "up", "예상", "뉴질랜드 10월 28일 기준금리 3%로 인상 전망")],
 "added": "블룸버그 1건 — 이코노미스트들이 11월 7일 총선 전인 10월 28일 뉴질랜드 금리 인상을 유력하게 본 내용이 추가됨",
 "items": [
  it("뉴질랜드, 선거 전 금리 인상 유력…이코노미스트", BB, "https://www.bloomberg.com/news/articles/2026-10-22/new-zealand-likely-facing-pre-election-rate-hike-economists-say",
     "이코노미스트들이 뉴질랜드중앙은행의 총선 전 금리 인상을 유력하게 보면서 10월 28일 기준금리 3% 인상 가능성이 커졌다")]})

A({"cid": "G2-082", "attachTo": "",
 "title": "한국 3분기 성장률 0.7% 예상…9월 반도체 수출 262.8% 급증에 개선 전망",
 "one": "\n".join([
  "로이터 조사에서 한국 3분기 성장률이 반도체 수출에 힘입어 전 분기보다 높아졌을 것으로 예상됐다.",
  "· 이코노미스트 16명은 3분기 전기 대비 0.7% 성장을 예상해 2분기 0.6%보다 조금 높게 봤다.",
  "· 9월 수출은 반도체가 262.8% 늘어난 데 힘입어 84% 급증한 1,209억 달러로 최대였다."]),
 "facts": [
  "무엇이: 로이터 조사에서 이코노미스트 16명은 한국 3분기 성장률을 전기 대비 0.7%로 예상해 2분기 0.6%보다 높게 봤다(전망 범위 0.5~1.6%) [사실]",
  "전년 대비: 3분기 성장률은 3.0%로 2분기 3.7%보다 둔화할 것으로 예상됐다 [사실]",
  "수출: 9월 수출은 1,209억 달러로 84% 늘어 최대였고, 반도체 수출은 262.8% 늘어난 603억 달러였다 [사실]",
  "발표: 3분기 GDP 속보치는 10월 27일 나온다 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약(로이터 조사를 전한 US News·Yahoo 요약)으로 확인",
 "src": [src("Yahoo Finance", "2026-10-23", "https://finance.yahoo.com/economy/articles/south-korean-economys-growth-likely-054144476.html")],
 "inds": ["macro"], "nodes": ["macro/growth"],
 "vc": [vc("macro", "growth", "수요", "up", "예상", "한국 3분기 성장률 0.7%로 개선 전망")],
 "items": [
  it("한국 경제, 반도체 수출에 3분기 성장 개선 전망", RT, "https://www.reuters.com/world/asia-pacific/south-korean-economys-growth-likely-picked-up-q3-chip-exports-2026-10-23/")]})

A({"cid": "G2-092", "attachTo": "",
 "title": "뮌헨리, 3분기 순이익 17억 유로로 예상 상회…연간 이익 전망 66억 유로로 상향",
 "one": "\n".join([
  "뮌헨리가 3분기 호실적에 힘입어 올해 순이익 전망을 63억 유로에서 66억 유로로 올렸다.",
  "· 3분기 잠정 순이익은 약 17억 유로로 시장 예상 14.79억 유로를 웃돌았다.",
  "· 재보험 대형 손실이 예상보다 적었고 재보험 투자 수익이 강해 실적을 끌어올렸다."]),
 "facts": [
  "무엇이: 뮌헨리는 23일 2026년 순이익 전망을 63억 유로에서 66억 유로로 올렸다 [사실]",
  "3분기: 잠정 순이익은 약 17억 유로로 예상 14.79억 유로를 웃돌았고, 9개월 누적 순이익은 57억 유로다 [사실]",
  "요인·향후: 재보험 손해보험 대형 손실이 평균 예상보다 적고 투자 수익이 강했으며, 4분기에는 대형 손실 추이에 따라 준비금을 더 쌓을 계획이고 전체 3분기 보고서는 11월 12일 나온다 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약(Artemis·Reinsurance News·The Insurer)으로 확인",
 "src": [src("Artemis", "2026-10-23", "https://www.artemis.bm/news/munich-re-raises-full-year-2026-profit-target-as-q3-result-well-above-consensus/"),
         src("Reinsurance News", "2026-10-23", "https://www.reinsurancene.ws/munich-re-raises-2026-profit-guidance-to-e6-6bn-on-strong-preliminary-q3-results/")],
 "inds": ["fin"], "nodes": [],
 "vc": [vc("fin", "insurance", "가격", "up", "실제", "뮌헨리 연간 이익 전망 66억 유로로 상향")],
 "items": [
  it("뮌헨리, 예상 웃돈 3분기에 연간 이익 전망 상향", RT, "https://www.reuters.com/business/munich-re-raises-full-year-profit-guidance-after-stronger-than-expected-quarter-2026-10-23/")]})

out = {"agent": "W4", "searches_used": 18, "fetches_used": 3, "items": items,
       "skipped": [{"cid": "G2-028", "reason": "AI 투자 증액(스페이스X AI 칩 담보 400억 달러 부채 조달 2건 제외 시 테슬라 합병 승인 제목 1건만 남아 구체 사실 없음)"}]}
json.dump(out, open("/home/user/news-desk/data/mix-2026-10-23/out2/W4.json", "w"), ensure_ascii=False, indent=1)

# 자체 길이 점검
for x in items:
    if not 20 <= len(x["title"]) <= 70: print(x["cid"], "title", len(x["title"]))
    for i in x["items"]:
        if not 25 <= len(i["t"]) <= 60: print(x["cid"], "t", len(i["t"]), i["t"])
        s = i.get("s", "").replace(" (제목 기준)", "")
        if s and not 45 <= len(s) <= 110: print(x["cid"], "s", len(s), s)
    if x.get("added") and not 40 <= len(x["added"]) <= 140: print(x["cid"], "added", len(x["added"]))
    for v in x["vc"]:
        if not 12 <= len(v["t"]) <= 45: print(x["cid"], "vc", len(v["t"]))
    L = x["one"].split("\n")
    for k, l in enumerate(L):
        ll = l.replace(" (채널 전언)", "").replace(" (제목 기준)", "")
        if k == 0 and not 40 <= len(ll) <= 90: print(x["cid"], "line0", len(ll))
        if k > 0 and not 25 <= len(ll) <= 90: print(x["cid"], "line", k, len(ll))
