import json, re
B = "https://www.bloomberg.com/news/"
R = "https://www.reuters.com/"
def it(t, o, d, u): return {"t": t, "o": o, "d": d, "u": u}
H = "텔레그램 하나증권 중국전략"
items = []

items.append({"cid": "C008", "attachTo": "",
 "title": "NATO 사령관, 대러 '승리 이론' 공개…드론 방벽·후방 타격으로 침공 저지",
 "one": "그륀케비치 NATO 최고연합군사령관이 10월 12일 바르샤바에서 초기 공격 차단과 후방 지휘망 타격을 담은 '승리 이론'을 공개하고 체코·독일 당국이 러시아의 그림자 전쟁 확대를 경고하면서, 유럽의 국방비와 탄약·무인체계 생산능력 확대가 억제력의 관건으로 떠올랐다",
 "facts": [
  "무엇이: 그륀케비치 사령관이 10월 12일 바르샤바 안보포럼에서 초기 공격을 막고, 지속되면 진격을 둔화시키고, 필요하면 적의 전력과 작전 체계를 무너뜨린다는 '승리 이론'을 발표하며 분쟁이 임박했다고 보지는 않는다고 언급 [사실]",
  "수단: 드론·인공지능과 러시아 후방 깊숙한 미사일 타격이 계획에 포함되고, 사보타주·사이버 공격 같은 하이브리드 위협과 불필요한 확전 회피도 다룸 [사실]",
  "구상: 저비용 드론·지상 로봇의 자율 방어구역, 칼리닌그라드·벨라루스 지휘시설 타격, 동맹 표적 정보를 실시간 공유하는 데이터 백본을 묶어 동부 전선 억제 이니셔티브로 명명, 2만 명 이상 모의훈련 중 [채널]",
  "제약: 미국이 이란 전쟁에 군수물자를 집중하면서 유럽 내 PAC-3·ATACMS 재고 부족이 심화됐고 미 국방부는 유럽 주둔 미군 감축 가능성도 검토 [채널]",
  "주변: NATO 관계자는 러시아 사상자가 지난달 5만 명이라고 했고, 체코 정보수장과 독일 내무장관은 러시아의 더 위험한 공작과 그림자 전쟁을 경고 [제목]"],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 10월 12일 바르샤바 안보포럼 발표, 차단·둔화·격파 3단계, 드론·AI·후방 미사일 타격(발칸인사이트·메두자·유라시아리뷰). 동부 전선 억제 이니셔티브 명칭, 2만 명 훈련, 탄약 재고 부족은 확인 못 함",
 "src": [{"o": "Balkan Insight", "d": "2026-10-12", "u": "https://balkaninsight.com/2026/10/12/natos-top-commander-unveils-plan-for-victory-against-russia/rd/"},
         {"o": "Meduza", "d": "2026-10-12", "u": "https://meduza.io/en/feature/2026/10/12/how-would-nato-defeat-a-russian-invasion-its-top-commander-envisions-a-wall-of-drones-a-counteroffensive-and-missile-strikes-deep-behind-russian-lines"},
         {"o": "Eurasia Review", "d": "2026-10-12", "u": "https://www.eurasiareview.com/12102026-weve-got-this-nato-commander-unveils-theory-of-victory-against-russia/"}],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "items": [
  it("NATO 관계자 \"러시아, 지난달 사상자 5만 명 발생\"", "블룸버그", "2026-10-12", B+"articles/2026-10-11/russia-suffered-50-000-casualties-last-month-nato-official-says"),
  it("NATO 사령관 \"우크라이나 지원이 푸틴의 유럽 위협 억지할 것\"", "블룸버그", "2026-10-12", B+"articles/2026-10-11/nato-commander-says-ukraine-aid-will-deter-putin-s-europe-threat"),
  it("그륀케비치 NATO 사령관 \"러시아의 공격은 완전히 헛된 일\" 경고", "로이터", "2026-10-12", R+"world/nato-commander-grynkewich-warns-russia-attack-would-be-utterly-futile-2026-10-12/"),
  it("체코 정보수장 \"러시아, NATO 회원국에 더 위험한 공작 감행할 수도\"", "로이터", "2026-10-12", R+"world/czech-intelligence-chief-says-russia-could-resort-riskier-operations-nato-states-2026-10-12/"),
  it("독일 내무장관 \"냉전 위협을 넘어서는 그림자 전쟁에 직면\"", "로이터", "2026-10-12", R+"world/germany-faces-shadow-war-that-goes-beyond-cold-war-threats-interior-minister-2026-10-12/"),
  it("NATO 군사 수장, 우크라이나 높이 평가하며 대러 전략 제시", "블룸버그", "2026-10-12", B+"articles/2026-10-12/nato-military-chief-lauds-ukraine-lays-out-russia-strategy"),
  it("NATO 장군, 러시아의 '어리석은 공격'에 강경한 군사 대응 방침 제시", "로이터", "2026-10-12", R+"world/nato-general-sets-out-tough-military-response-any-foolish-russian-attack-2026-10-12/"),
  it("NATO, 드론·장거리 미사일 결합한 동부 전선 억제 전략 공개", "텔레그램 상상인 김진범", "2026-10-13", "https://t.me/PipeBeom/6679")]})

items.append({"cid": "C010", "attachTo": "n-rtr-0025",
 "title": "AI 거품 경고 확산…브로드컴 탄 \"투자자 다수가 도박꾼\", 제프리스 \"2008년 모먼트\"",
 "one": "혹 탄 브로드컴 CEO가 AI 투자자 다수를 카지노 도박꾼에 비유하며 자본이 AI 성장의 최대 제약이 됐다고 말하고 제프리스가 하이퍼스케일러 수주잔고의 OpenAI·앤트로픽 쏠림을 2008년 위기에 견주면서, AI 인프라 자금줄에 대한 경계가 커지고 있다",
 "facts": [
  "무엇이: 혹 탄 CEO가 10월 12일 싱가포르 DBS 행사에서 많은 AI 투자자가 무엇에 투자하는지 모르는 도박꾼 같다며, 자본이 칩·메모리·전력 부족을 대신해 AI 발전의 최대 병목이 되고 있다고 발언 [사실]",
  "신용 집중: 제프리스 크리스 우드는 OpenAI·앤트로픽이 아마존 수주잔고의 45~50%, 구글의 약 40%를 차지한다며 서브프라임 위기에 비유하고, 신용시장이 자금을 거두는 순간 AI 거래가 무너질 수 있다고 경고 [사실]",
  "자금 시장: 엔비디아가 지원하는 호주 데이터센터 기업 퍼머스 그리드가 55억 달러 IPO를 철회했고, 탄은 OpenAI가 9월 연환산 매출 500억 달러에도 적자라고 지적 [사실]",
  "기업 지출: CFO들이 AI 지출 고삐를 죄고 있고 틱톡 추 CEO와 MS 알트호프도 AI 과열을 경고 [제목]",
  "기존: 웡 싱가포르 총리가 10월 8일 AI 기술 랠리가 결국 조정을 맞을 것이라고 경고 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 탄의 도박꾼 비유·자본 병목 발언, 퍼머스 그리드 IPO 철회, OpenAI 연환산 매출 500억 달러(트레이딩피디아·푸투). 제프리스 수주잔고 집중은 회사별 비중으로 확인(합계 2조 3,400억 달러 중 절반 수치는 확인 못 함). CFO 지출 긴축은 제목뿐",
 "src": [{"o": "Tradingpedia", "d": "2026-10-12", "u": "https://www.tradingpedia.com/2026/10/12/broadcom-chief-flags-casino-like-speculation-in-ai-stocks/"},
         {"o": "Futu News", "d": "2026-10-12", "u": "https://news.futunn.com/en/post/1000898139/broadcom-ceo-many-ai-investors-are-like-casino-gamblers-capital"},
         {"o": "Tiger Brokers", "d": "2026-10-12", "u": "https://www.itiger.com/news/1179263540"}],
 "inds": ["macro"], "nodes": ["macro/semis", "macro/liquidity"],
 "items": [
  it("CFO들, AI 지출에 지갑 끈 조인다(WK·WRBY·MTCH·PICS)", "블룸버그", "2026-10-12", B+"newsletters/2026-10-11/cfos-tighten-the-purse-strings-on-ai-wk-wrby-mtch-pics"),
  it("제프리스 \"2008년 모먼트\" 경고…AI 하이퍼스케일러 수주잔고 절반이 OpenAI·앤트로픽", H, "2026-10-12", "https://t.me/HANAchina/70247"),
  it("틱톡 추 CEO·MS 알트호프, 걷잡을 수 없는 AI 과열 경고", "블룸버그", "2026-10-12", B+"articles/2026-10-12/tiktok-s-chew-and-microsoft-s-althoff-warn-about-runaway-ai-hype"),
  it("브로드컴 CEO \"AI 기술 성장의 최대 장애물은 메모리가 아닌 자본\"", "로이터", "2026-10-12", R+"world/asia-pacific/broadcom-ceo-says-biggest-hurdle-ai-fuelled-tech-growth-is-capital-not-memory-2026-10-12/"),
  it("브로드컴 혹 탄 \"AI 최대 제약은 메모리 아닌 자본\"…웨이퍼 부족은 극복 중", "텔레그램 TNBfolio", "2026-10-12", "https://t.me/TNBfolio/71501"),
  it("브로드컴 CEO, 많은 AI 투자자를 카지노 도박꾼에 비유", "블룸버그", "2026-10-12", B+"articles/2026-10-12/broadcom-ceo-likens-many-ai-investors-to-casino-gamblers"),
  it("브로드컴 CEO \"AI 투자자는 카지노 도박꾼\"…인텔 립부 탄도 자금 조달 비용 우려", H, "2026-10-12", "https://t.me/HANAchina/70301"),
  it("혹 탄, 적자 AI 연구소 경제성에 의문…퍼머스 그리드 55억 달러 IPO 철회", "텔레그램 TNBfolio", "2026-10-13", "https://t.me/TNBfolio/71509")]})

items.append({"cid": "C016", "attachTo": "",
 "title": "인도 주식형 펀드 9월 유입 31% 급증…IPO 붐에 월가 인도 베팅 확대",
 "one": "인도 주식형 뮤추얼펀드에 9월 3만 8,307크로르 루피가 들어와 전월보다 31% 늘고 제트웍이 5억 1,800만 달러 규모 IPO 공모가 범위를 정하는 등 상장 붐이 이어지면서, 니프티 약세 속에서도 인도 증시로 자금이 계속 몰리고 있다",
 "facts": [
  "무엇이: 9월 인도 주식형 뮤추얼펀드 순유입이 3만 8,307크로르 루피로 8월 2만 9,329크로르 루피보다 약 31% 늘었고 소형주·중형주 펀드가 유입을 주도 [사실]",
  "적립식: SIP 납입액이 3만 2,490크로르 루피로 사상 최대였지만 채권형 환매로 업계 전체 운용자산은 82.64라크크로르 루피로 5.1% 감소 [사실]",
  "상장: 제트웍이 5억 1,800만 달러 IPO 공모가를 주당 143~151루피로 정했고, IPO 붐이 월가의 인도 베팅을 부추기고 있음 [제목]",
  "전망: 아문디 계열사는 이란 전쟁 종료가 인도의 전환점이 될 것이라 했고, 모디의 자유무역 추진으로 GDP가 1,400억 달러 늘 수 있다는 분석이 나옴 [제목]"],
 "basis": "partial",
 "check": "검색 결과 요약으로 확인: 9월 주식형 펀드 유입 3만 8,307크로르 루피·31% 증가, SIP 최대, 운용자산 5.1% 감소(업스톡스·아웃룩머니). 5개월 최고 표현과 제트웍 공모가는 확인 못 함",
 "src": [{"o": "Upstox", "d": "2026-10-12", "u": "https://upstox.com/news/personal-finance/mutual-funds/amfi-september-2026-data-equity-inflows-jump-31-small-mid-caps-lead-gold-and-silver-et-fs-gain/article-201686/"},
         {"o": "Outlook Money", "d": "2026-10-12", "u": "https://www.outlookmoney.com/invest/amfi-data-september-2026-equity-mf-inflows-38307-crore-rupees"}],
 "inds": ["fin"], "nodes": [],
 "items": [
  it("위험에도 IPO 붐이 월가의 인도 베팅을 부추긴다", "블룸버그", "2026-10-12", B+"articles/2026-10-12/ipo-boom-fuels-wall-street-s-india-bets-despite-risks"),
  it("아문디 계열사 \"이란 전쟁 종료가 인도의 전환점 될 것\"", "블룸버그", "2026-10-12", B+"articles/2026-10-12/iran-war-s-end-will-be-turning-point-for-india-amundi-arm-says"),
  it("저가 매수에 인도 주식형 펀드로 자금 유입 확대", "블룸버그", "2026-10-12", B+"articles/2026-10-12/india-equity-fund-flows-draw-more-cash-as-investors-buy-the-dip"),
  it("니프티 부진에도 인도 주식형 펀드 9월 유입 5개월 만에 최대", "로이터", "2026-10-12", R+"world/india/india-equity-mutual-fund-inflows-hit-5-month-high-september-despite-nifty-slump-2026-10-12/"),
  it("인도 제트웍, 5억 1,800만 달러 IPO 공모가 주당 143~151루피로 확정", "로이터", "2026-10-12", R+"world/india/indias-zetwerk-sets-price-band-143-151-rupees-per-share-518-million-ipo-2026-10-12/"),
  it("성장 야망이 뉴델리 논의의 중심 무대에 오르다", "블룸버그", "2026-10-12", B+"newsletters/2026-10-12/growth-ambitions-take-center-stage-in-new-delhi"),
  it("모디의 자유무역 추진, 인도 GDP 1,400억 달러 늘릴 수 있어", "블룸버그", "2026-10-13", B+"articles/2026-10-12/modi-s-free-trade-push-could-lead-to-140-billion-gdp-gain-for-india")]})

items.append({"cid": "C023", "attachTo": "",
 "title": "中 탄산리튬 선물 하루 11% 급락해 10개월 최저…EU 하이브리드 합의·광산 재가동 우려",
 "one": "중국 탄산리튬 선물이 10월 12일 EU와의 하이브리드차 수출 감축 합의에 따른 수요 우려와 장터전기 첸컹 광산 설계 승인 등 공급 확대 우려가 겹쳐 11.8% 급락해 10개월 만의 최저로 내려가면서, 리튬 생산업체 주가도 함께 떨어졌다",
 "facts": [
  "무엇이: 광저우 주력 탄산리튬 선물이 10월 12일 주간 거래를 11.8% 내린 톤당 10만 4,740위안에 마쳐 3월 이후 최대 일일 낙폭과 약 10개월 만의 최저를 기록 [사실]",
  "흐름: 5월 13일 고점 20만 9,880위안의 절반 수준이며 톈치리튬·간펑리튬 주가가 각각 5.1%, 3.9% 하락 [사실]",
  "공급: 장터전기 첸컹 광산(연 원광 300만 톤, 이론 생산능력 약 1만 5,000톤 LCE)의 안전시설 설계가 10월 11일 국가광산안전국 심사를 통과했고 CATL 젠샤워 광산 재가동 관측도 부담 [채널]",
  "수요: 상하이스틸연합 조사상 LFP 생산계획 전월 대비 증가율이 9월 4.74%에서 10월 3.61%로 둔화, 짐바브웨의 2027년 1월 리튬정광 수출금지는 반등 변수 [채널]",
  "계약: 에너지X가 트라피구라와 20억 달러 규모 구속력 있는 리튬 공급계약 체결 [제목]"],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 11.8% 급락·10만 4,740위안, EU 하이브리드 수출 합의, CATL 젠샤워 재가동 관측, 5월 고점, 톈치·간펑 주가(마이닝위클리). 장터전기 첸컹 승인과 LFP 생산계획 수치는 확인 못 함",
 "src": [{"o": "Mining Weekly", "d": "2026-10-12", "u": "https://www.miningweekly.com/article/chinese-lithium-prices-tumble-to-nearly-10-month-low-on-demand-concerns-2026-10-12"},
         {"o": "Finimize", "d": "2026-10-12", "u": "https://finimize.com/content/chinas-lithium-futures-tumbled-after-an-eu-hybrid-export-deal"}],
 "inds": ["metals"], "nodes": [],
 "items": [
  it("탄산리튬 선물 개장 직후 4%대 급락, 톤당 11만 위안대 위협", H, "2026-10-12", "https://t.me/HANAchina/70248"),
  it("탄산리튬 선물 낙폭 8%로 확대, 하한가 근접", H, "2026-10-12", "https://t.me/HANAchina/70274"),
  it("탄산리튬 선물 연중 최저…중국 운모 광산 진전에 공급 우려, 수요도 둔화", "텔레그램 상상인 김진범", "2026-10-12", "https://t.me/PipeBeom/6672"),
  it("장터전기 첸컹 리튬 광산, 연 300만 톤 채굴 설계 심사 통과", "텔레그램 상상인 김진범", "2026-10-12", "https://t.me/PipeBeom/6673"),
  it("EU 합의로 하이브리드 수출 줄자 중국 리튬 10% 급락", "블룸버그", "2026-10-12", B+"articles/2026-10-12/chinese-lithium-slumps-10-after-eu-deal-slashes-hybrid-exports"),
  it("에너지X, 트라피구라와 20억 달러 규모 구속력 있는 리튬 공급계약", "로이터", "2026-10-12", R+"business/energy/energyx-signs-binding-2-billion-lithium-supply-deal-with-trafigura-2026-10-12/")]})

items.append({"cid": "C030", "attachTo": "n-bbg-0093",
 "title": "IMF 총재 \"AI는 느린 쓰나미\"…부채·선진국 국채 매도도 방콕 총회 화두",
 "one": "게오르기에바 IMF 총재가 방콕 연차총회에서 AI를 일자리와 세수를 위협하는 '느린 쓰나미'로 규정하고 영국 재무장관이 주요국에 차입 통제를 촉구하면서, 고유가·고부채에 선진국 국채 매도까지 겹친 재정 위험이 회의의 핵심 의제로 떠올랐다",
 "facts": [
  "무엇이: 게오르기에바 총재가 10월 12일 방콕 IMF·세계은행 연차총회에서 AI가 반복 업무 수요를 줄이고 소득을 노동에서 자본으로 옮겨 세수를 압박할 수 있다며 '느린 쓰나미'라고 경고 [사실]",
  "규모: IMF는 세계 일자리의 약 40%가 AI로 보완·격하·소멸될 것으로 보며, AI 도입이 아시아 선진국 성장률을 0.5~1%포인트, 신흥 아시아를 0.2~0.8%포인트 높일 수 있다고 봄 [사실]",
  "부채: 영국 재무장관이 대형 경제국의 차입 통제를 촉구했고 선진국 국채 매도로 선진국 재정이 IMF의 관심 대상이 됨 [제목]",
  "성장: IMF는 AI 투자가 세계 성장률을 3% 안팎으로 지탱하며 아시아가 큰 혜택을 본다고 평가 [제목]",
  "기존: 10월 7일 총재가 유가 100달러 안팎의 에너지 충격, 2030년 전 GDP 100%를 넘을 공공부채, AI 실적 실망 위험이 겹쳤다며 재정 건전화를 촉구 [사실]"],
 "basis": "partial",
 "check": "검색 결과 요약으로 확인: 느린 쓰나미 발언, 일자리 40%, 세수 압박, 아시아 성장 효과(아이리시타임스·CNBC). 영국 재무장관 발언, 국채 매도, 세계 성장 3% 평가는 제목만으로 확인 못 함",
 "src": [{"o": "Irish Times", "d": "2026-10-12", "u": "https://www.irishtimes.com/business/work/2026/10/12/imf-chief-alarmed-at-slow-moving-tsunami-of-ai-for-jobs-taxes/"},
         {"o": "CNBC", "d": "2026-10-12", "u": "https://www.cnbc.com/2026/10/12/imf-world-bank-ai-jobs-inflation-.html"}],
 "inds": ["macro"], "nodes": ["macro/fiscal", "macro/growth", "macro/rates"],
 "items": [
  it("IMF 총재, AI가 일자리·세수에 미칠 '느린 쓰나미'에 경각심", "블룸버그", "2026-10-12", B+"articles/2026-10-12/imf-chief-alarmed-at-slow-moving-tsunami-of-ai-for-jobs-taxes"),
  it("영국 재무장관, IMF에서 대형 경제국에 차입 통제 촉구", "로이터", "2026-10-12", R+"world/uk/uk-finance-minister-call-big-economies-get-borrowing-under-control-imf-2026-10-11/"),
  it("IMF \"AI 생산성 향상이 아시아 고령화 문제 상쇄할 수 있어\"", "로이터", "2026-10-12", R+"world/asia-pacific/productivity-gains-ai-could-help-offset-asias-ageing-population-problem-imf-says-2026-10-12/"),
  it("선진국 국채 매도로 선진 경제가 IMF의 주목 대상에", "블룸버그", "2026-10-12", B+"newsletters/2026-10-12/rich-world-bond-selloff-puts-advanced-economies-in-imf-spotlight"),
  it("IMF \"AI 투자가 세계 성장 3% 안팎 지탱…아시아 혜택 커\"", "로이터", "2026-10-12", R+"world/china/imf-says-ai-investment-keeps-global-growth-around-3-with-major-asia-benefits-2026-10-12/")]})

items.append({"cid": "C037", "attachTo": "n-tg-0220",
 "title": "TSMC·GF 인터포저 계약 뒤 UMC·PSMC 증설 경쟁…패키징 소재도 확충",
 "one": "글로벌파운드리스가 TSMC의 20억 달러 규모 실리콘 인터포저 5년 계약을 따내 뉴욕에서 생산하기로 한 가운데 UMC가 인터포저 월 생산능력을 3,000장에서 6,000장으로 늘리고 스미토모 베이클라이트도 패키징 소재를 증설하면서, AI 칩 첨단 패키징 공급망 경쟁이 넓어지고 있다",
 "facts": [
  "무엇이: 글로벌파운드리스가 TSMC와 약 20억 달러 규모 5년 계약을 맺고 뉴욕주 몰타 공장에서 CoWoS용 실리콘 인터포저를 생산하며, 2028년 상반기부터 물량을 늘림 [사실]",
  "대만: UMC가 인터포저 월 생산능력을 3,000장에서 6,000장으로 두 배 늘리고 딥 트렌치 커패시터를 적용한 2.5D 솔루션을 확대 [사실]",
  "PSMC: 기존 공장 자원을 활용해 인터포저·고밀도 실리콘 커패시터·3D 웨이퍼 적층을 결합해 첨단 패키징에 진입 [채널]",
  "소재: 스미토모 베이클라이트가 쑤저우·싱가포르에서 패키징용 몰드 언더필 생산능력을 2배, 압축 성형용 과립 소재를 3배로 늘릴 계획 [채널]"],
 "basis": "partial",
 "check": "검색 결과 요약으로 확인: UMC 월 3,000장에서 6,000장 확대, TSMC·GF 20억 달러 5년 계약과 2028년 상반기 증산(테크소다·트렌드포스, 단 UMC 기존 능력 수치는 출처마다 다름). 스미토모 베이클라이트 증설과 PSMC 세부는 확인 못 함",
 "src": [{"o": "Techsoda", "d": "2026-10-12", "u": "https://techsoda.substack.com/p/global-market-watch-tsmc-is-localizing"}],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "items": [
  it("스미토모 베이클라이트, 쑤저우·싱가포르서 첨단 패키징 소재 증설", "텔레그램 미국 주식 인사이더", "2026-10-12", "https://t.me/insidertracking/65982"),
  it("TSMC 인터포저 GF 위탁에 대만 UMC·PSMC도 인터포저 사업 확대", H, "2026-10-12", "https://t.me/HANAchina/70239"),
  it("TSMC·GF 20억 달러 인터포저 계약, UMC 월 생산능력 6,000장으로 확대", "텔레그램 트릴리온", "2026-10-12", "https://t.me/Trillion_labs/10359"),
  it("TSMC, CoWoS 핵심 부품 실리콘 인터포저 첫 미국 생산을 GF에 맡겨", H, "2026-10-12", "https://t.me/HANAchina/70267")]})

items.append({"cid": "C045", "attachTo": "",
 "title": "MS 'Maia 300' 공개로 탈엔비디아 가속…AMD·엔비디아·마벨도 AI 인프라 신제품",
 "one": "마이크로소프트가 랙당 토큰 처리량을 최대 7배 늘린 3세대 자체 AI 칩 Maia 300을 공개하고 추론 작업을 주로 자체 칩에 맡기기로 한 가운데 AMD·엔비디아-시스코·마벨도 랙·광모듈·메모리 확장기를 내놓으면서, AI 추론 인프라의 엔비디아 GPU 의존이 줄어들 수 있다",
 "facts": [
  "무엇이: 마이크로소프트가 10월 12일 Maia 300을 공개, 167kW 랙에 가속기 96개(Maia 200의 2배)를 넣어 랙 단위 토큰 처리량을 최대 7배 높이고 메가와트당 토큰은 GPU 시스템보다 약 40% 많을 것으로 제시 [사실]",
  "일정·용도: 2027년부터 생산 배치되며 주로 추론에 쓰이고 당분간 외부에 임대하지 않아, 성능은 아직 회사 주장일 뿐 독립 검증이 없음 [사실]",
  "비중: 에버코어 ISI는 2027년 1분기까지 Maia가 마이크로소프트 AI 칩 지출의 약 10%를 차지할 것으로 추정 [채널]",
  "경쟁 제품: AMD가 최대 3만 2,000개 CPU 코어의 에이전틱 AI 랙 Helion을 11월 출시하고, 엔비디아·시스코는 단일 채널 400Gb/s 플러그형 광모듈 표준 USFP를, 마벨은 최대 9TB DDR4를 지원하는 CXL 메모리 확장기를 발표 [채널]"],
 "basis": "partial",
 "check": "검색 결과 요약으로 확인: Maia 300 랙당 96개·167kW·7배·GPU 대비 40%·2027년 생산·내부 전용(애저 블로그·CNBC). 에버코어 추정, AMD·엔비디아-시스코·마벨 신제품은 확인 못 함",
 "src": [{"o": "Microsoft Azure Blog", "d": "2026-10-12", "u": "https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/"},
         {"o": "CNBC", "d": "2026-10-12", "u": "https://www.cnbc.com/2026/10/12/microsoft-will-mainly-use-its-maia-chips-for-ai-inference.html"}],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "items": [
  it("마벨, 최대 9TB DDR4 지원 2세대 CXL 메모리 확장기 Structera X 출시", H, "2026-10-12", "https://t.me/HANAchina/70302"),
  it("마이크로소프트, 3세대 자체 AI 칩 Maia 300 공개…추론은 자체 칩 중심으로", "텔레그램 TNBfolio", "2026-10-12", "https://t.me/TNBfolio/71506"),
  it("엔비디아·시스코, 단일 채널 400Gb/s 플러그형 광모듈 첫 공개", H, "2026-10-13", "https://t.me/HANAchina/70309"),
  it("AMD, 최대 3만 2,000 CPU 코어 에이전틱 AI 랙 Helion 출시", H, "2026-10-13", "https://t.me/HANAchina/70317")]})

items.append({"cid": "C061", "attachTo": "",
 "title": "유럽 에너지값 대책 분주…獨 전기세 EU 최저로, EU는 석유·가스 횡재세 검토",
 "one": "메르츠 독일 총리가 모든 소비자의 전기세를 EU 최저 수준으로 낮추겠다고 약속하고 EU 집행위가 석유·가스 기업 횡재세 검토 작업반을 꾸리면서, 이란 전쟁발 에너지값 급등의 부담 일부가 에너지 기업 이익 쪽으로 옮겨갈 수 있다",
 "facts": [
  "무엇이: 메르츠 총리가 10월 12일 지난해 재원 부족으로 접었던 전 소비자 전기세 인하를 EU 최저 수준으로 다시 약속, 현재 세율은 kWh당 2.05센트이고 EU 최저는 0.05센트 [사실]",
  "재원: 성장 전망 개선으로 연방 세수가 필요액인 약 50억 유로 늘 수 있다고 설명 [사실]",
  "EU: 훅스트라 세제 담당 집행위원이 석유·가스 기업 횡재세의 득실을 따질 작업반을 꾸리고 있으며, 2022년에는 초과이익에 최소 33%를 부과해 약 290억 유로를 거뒀음 [사실]",
  "영국: 송전망 운영사가 공급 확보를 위해 프랑스에 긴급 전력을 요청 [제목]"],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 메르츠 전기세 인하 약속과 세율·50억 유로, EU 횡재세 작업반과 2022년 33%·290억 유로(인베스팅닷컴 자체 기사·글로벌뱅킹앤파이낸스). 영국 프랑스 긴급 전력 요청은 제목만",
 "src": [{"o": "Global Banking & Finance Review", "d": "2026-10-12", "u": "https://www.globalbankingandfinance.com/eu-looking-oil-gas-windfall-profit-tax-energy-prices-soar/"},
         {"o": "Global Banking & Finance Review", "d": "2026-10-12", "u": "https://www.globalbankingandfinance.com/merz-vows-electricity-tax-cut-consumers-close-credibility/"}],
 "inds": ["power", "gas"], "nodes": ["power/market", "gas/demand"],
 "items": [
  it("메르츠, 신뢰 격차 해소 위해 모든 소비자 전기세 인하 약속", "로이터", "2026-10-13", R+"business/merz-vows-electricity-tax-cut-all-consumers-close-credibility-gap-2026-10-12/"),
  it("영국 송전망, 공급 확보 위해 프랑스에 긴급 전력 요청", "블룸버그", "2026-10-13", B+"articles/2026-10-12/uk-grid-seeks-emergency-french-power-to-secure-supplies"),
  it("에너지 가격 급등에 EU, 석유·가스 횡재세 검토", "로이터", "2026-10-13", R+"business/energy/eu-looking-oil-gas-windfall-profit-tax-energy-prices-soar-2026-10-12/")]})

items.append({"cid": "C070", "attachTo": "",
 "title": "단종된 포드 F-150 라이트닝, 中古 시장서 깜짝 인기…평균 20일 만에 팔려",
 "one": "포드가 지난해 12월 생산을 멈춘 전기 픽업 F-150 라이트닝이 미국 중고차 시장에서 평균 20일 만에 팔리고 값도 연초보다 4% 오른 약 5만 달러에 이르면서, 신차 정가의 절반 수준으로 내려온 전기 픽업에 수요가 몰리고 있다",
 "facts": [
  "무엇이: 중고 F-150 라이트닝이 미국에서 평균 약 20일 만에 팔려 일반 중고차 평균 44일의 절반에 못 미치고, 가격은 연초 대비 4% 오른 약 5만 달러 [사실]",
  "가격: 중고가는 신차 정가의 50~60% 수준이며, 출시 첫해 실제 평균 거래가는 7만 9,000달러였음 [사실]",
  "판매: 포드는 휘발유 F-150을 좋은 해에 약 90만 대 팔지만 라이트닝은 4년 남짓 동안 10만 대를 조금 넘게 판매 [사실]",
  "다음 수: 포드는 내년 시작가 약 2만 8,000달러의 전기 픽업 패덤으로 연 10만 대를 노리지만 새 EV 플랫폼 대량 생산은 아직 궤도에 오르지 못함, 이란 전쟁발 고유가가 수요를 자극 [채널]"],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 20일 대 44일, 4% 상승 약 5만 달러, 정가의 50~60%, 첫해 평균 7만 9,000달러, 누적 10만 대 남짓(일렉트렉·디트로이트뉴스). 패덤 가격·목표는 확인 못 함",
 "src": [{"o": "Electrek", "d": "2026-10-12", "u": "https://electrek.co/2026/10/12/fords-electric-pickup-selling-like-hotcakes-50-off-used/"},
         {"o": "Detroit News", "d": "2026-10-11", "u": "https://www.detroitnews.com/story/business/autos/2026/10/11/ford-electric-truck-sales-surge-f-150-lightning-used/92207829007/"}],
 "inds": ["auto"], "nodes": [],
 "items": [
  it("단종된 포드 F-150 라이트닝, 중고차 시장 인기 차종으로 부상", "텔레그램 TNBfolio", "2026-10-12", "https://t.me/TNBfolio/71498"),
  it("포드가 단종한 F-150 라이트닝, 중고차 시장서 뜻밖의 인기", "블룸버그", "2026-10-12", B+"newsletters/2026-10-12/ford-s-axed-f-150-lightning-is-a-surprise-hit-in-the-used-market")]})

items.append({"cid": "C078", "attachTo": "n-rtr-0034",
 "title": "EU, 대러 제재 명단 약 1600건 공식 채택…침공 이후 최대 확대",
 "one": "EU 외교장관들이 10월 12일 탄도미사일 공급망을 중심으로 약 1,600건의 대러 제재 명단을 공식 채택하고 영국도 그림자 선단 유조선 등 38건을 추가 제재하면서, 러시아의 군수 조달과 원유 수출·결제 경로에 대한 압박이 커지고 있다",
 "facts": [
  "무엇이: EU 외교이사회가 10월 12일 약 1,600건의 대러 제재 명단을 채택했고, 칼라스 외교안보 고위대표는 전면 침공 이후 최대 규모 확대이며 절반 이상이 탄도미사일 생산 사슬과 관련됐다고 밝힘 [사실]",
  "구성: 개인 743명·법인 826곳 등 1,569건에 점령지 두마 선거 관련 77건을 더해 대사들이 합의한 1,646건이 됨 [사실]",
  "영국: 10월 8일 38건 지정, 유조선 12척 추가로 그림자 선단 제재 선박이 600척을 넘었고 우회 결제업체와 석유사도 포함 [사실]",
  "후속: 네덜란드 국방장관이 동맹국에 대러 제재 유지를 촉구 [제목]"],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 10월 12일 채택, 최대 규모, 탄도미사일 관련 절반 이상, 1,569건과 77건 구성(메두자·모스크바타임스·라트비아 외교부). 영국 제재는 기존 문서 근거",
 "src": [{"o": "Meduza", "d": "2026-10-12", "u": "https://meduza.io/en/news/2026/10/12/eu-approves-largest-expansion-of-sanctions-list-against-russia"},
         {"o": "The Moscow Times", "d": "2026-10-12", "u": "https://www.themoscowtimes.com/2026/10/12/eu-adopts-record-sanctions-expansion-targeting-16k-russian-defense-firms-and-executives-a93952"},
         {"o": "라트비아 외교부", "d": "2026-10-12", "u": "https://www.mfa.gov.lv/en/article/eu-foreign-affairs-council-adopts-largest-ever-package-sanctions-listings-against-russia"}],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "items": [
  it("EU, 러시아 겨냥 제재 명단 약 1,600건 신규 채택", "로이터", "2026-10-12", R+"world/europe/eu-adopts-nearly-1600-new-sanctions-listings-targeting-russia-2026-10-12/"),
  it("네덜란드 국방장관, 동맹국에 대러 제재 유지 촉구", "블룸버그", "2026-10-12", B+"articles/2026-10-12/dutch-defense-minister-urges-russia-sanctions-to-remain-in-place")]})

items.append({"cid": "C086", "attachTo": "",
 "title": "DJI·인스타360, 휴대용 스마트카메라 시장 90% 장악…고프로는 사업 축소",
 "one": "중국 DJI와 인스타360이 IDC 기준 글로벌 휴대용 스마트카메라 시장 합산 점유율 90%를 넘기면서, 지난달 매각된 미국 고프로가 핵심 액션카메라 사업에서 일부 철수를 시사하는 등 서방 업체가 밀려나고 있다 (채널 전언)",
 "facts": [
  "무엇이: IDC에 따르면 중국 선전의 DJI와 인스타360이 글로벌 휴대용 스마트카메라 시장 합산 점유율 90%를 돌파 [채널]",
  "고프로: 2023년까지 매출 기준 선두였으나 지난달 새 소유주에게 매각된 뒤 핵심 사업에서 적어도 일부 철수할 방침을 시사 [채널]",
  "유사 사례: 로봇청소기 시장 개척자 룸바 제조사도 중국 업체와의 경쟁에 밀려 지난해 파산 신청 [채널]"],
 "basis": "channel",
 "check": "검색 한도 안에서 따로 확인하지 못함, 채널 원문 기준",
 "src": [],
 "inds": ["consumer"], "nodes": [],
 "items": [
  it("고프로 몰락 속 DJI·인스타360, 휴대용 스마트카메라 시장 90% 이상 장악", "텔레그램 미국 주식 인사이더", "2026-10-12", "https://t.me/insidertracking/65981")]})

items.append({"cid": "C094", "attachTo": "",
 "title": "中 PCB 업체 둥산정밀, 최대 30억 달러 홍콩 상장 수요 조사",
 "one": "중국 PCB 업체 둥산정밀이 증감회 승인과 홍콩거래소 상장 심사를 통과한 뒤 최대 30억 달러 규모 홍콩 상장의 수요 조사에 나서면서, 4분기 홍콩 대형 IPO 물량이 늘어날 전망이다",
 "facts": [
  "무엇이: 선전 상장사 둥산정밀이 최대 30억 달러 규모 홍콩 상장을 앞두고 투자 수요를 타진 [사실]",
  "절차: 중국 증감회가 최대 2억 3,400만 주 발행을 승인했고 홍콩거래소 상장 심사도 통과, 공동 주관사는 UBS·궈타이하이퉁·광파증권·중신증권 [사실]",
  "규모·일정: IFR은 조달액을 20억~30억 달러로 전했고 일정이 다소 밀릴 수 있으나 연내 상장 예정 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 최대 30억 달러, 증감회 승인 2억 3,400만 주, 상장 심사 통과, 주관사(SCMP·인덱스박스)",
 "src": [{"o": "SCMP", "d": "2026-10", "u": "https://www.scmp.com/business/banking-finance/article/3369299/mainland-chinas-pcb-giant-wins-hong-kong-approval-planned-us3b-listing-sources"},
         {"o": "IndexBox", "d": "2026-10", "u": "https://www.indexbox.io/blog/suzhou-dongshan-precision-clears-final-hurdle-for-hong-kong-ipo/"}],
 "inds": ["fin"], "nodes": [],
 "items": [
  it("둥산정밀, 최대 30억 달러 상장 위한 수요 타진 중…소식통", "블룸버그", "2026-10-12", B+"articles/2026-10-12/dongshan-said-to-gauge-demand-for-up-to-3-billion-hk-listing")]})

items.append({"cid": "C102", "attachTo": "",
 "title": "퀄컴 CEO \"2028년 폰서 1000억 매개변수 모델 구동\"…머스크 \"관건은 메모리\"",
 "one": "퀄컴 CEO가 일부 선두 AI 기업이 2028년까지 스마트폰에서 1,000억 매개변수 모델을 상시 구동하길 요구한다고 밝히고 머스크가 관건은 RAM 공급이라고 답하면서, 온디바이스 AI가 모바일 메모리 수요를 키울 수 있다 (채널 전언)",
 "facts": [
  "무엇이: 퀄컴 CEO가 10일 인터뷰에서 AI 최전선 기업들이 2028년까지 스마트폰에서 최소 1개의 1,000억 매개변수 모델을 거의 항상 실행할 능력을 요구하고 있다고 발언 [채널]",
  "단말: 일부 AI 기업이 스마트폰을 개발하고 있다는 점도 확인했으나 기업명은 밝히지 않음 [채널]",
  "메모리: 머스크가 10월 11일 X에 핵심은 RAM 공급이라고 게시 [채널]"],
 "basis": "channel",
 "check": "검색 한도 안에서 따로 확인하지 못함, 채널 원문(중국 언론 인용) 기준",
 "src": [],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "items": [
  it("퀄컴 CEO \"2028년 스마트폰서 1,000억 매개변수 모델 실행\"…머스크 \"핵심은 메모리\"", H, "2026-10-12", "https://t.me/HANAchina/70273")]})

items.append({"cid": "C110", "attachTo": "",
 "title": "싱가포르, 아시아 채권선물 새 거래 창구 열어 해외 트레이더 유치",
 "one": "싱가포르가 아시아 채권선물에 새로운 거래 시간 창구를 열어 역외 트레이더 유치에 나서면서, 해외 투자자가 아시아 채권 금리 위험을 거래할 수 있는 시간대가 넓어질 수 있다 (제목 기준)",
 "facts": [
  "무엇이: 싱가포르가 새 아시아 채권선물 거래 창구로 역외 트레이더를 끌어들이려 함 [제목]",
  "의미: 역외 투자자의 아시아 채권 헤지·거래 접근성이 높아질 수 있음 [추론]"],
 "basis": "title",
 "check": "검색 한도 안에서 확인하지 못함, 블룸버그 제목 기준",
 "src": [],
 "inds": ["fin"], "nodes": [],
 "items": [
  it("싱가포르, 새 아시아 채권선물 거래 창구로 역외 트레이더 유치", "블룸버그", "2026-10-12", B+"articles/2026-10-12/singapore-woos-offshore-traders-with-new-asian-bond-futures-window")]})

items.append({"cid": "C118", "attachTo": "n-bbg-0112",
 "title": "폭스바겐 3분기 인도 14% 감소…중국 38% 급감에 4년여 만의 최대 낙폭",
 "one": "폭스바겐그룹의 3분기 인도량이 중국 38.5% 급감 여파로 14.3% 줄어든 약 189만 대에 그쳐 4년여 만의 최대 낙폭을 기록하고 포르쉐도 1~9월 16% 감소하면서, 중국발 판매 부진이 그룹 전 브랜드로 번지고 있다",
 "facts": [
  "무엇이: 폭스바겐그룹의 3분기 글로벌 인도량이 약 189만 대로 전년보다 14.3% 줄어 2022년 2분기 이후 가장 큰 분기 감소 [사실]",
  "지역: 중국이 40만 5,800대로 38.5% 급감했고 북미 5.8%, 서유럽 2.8% 줄었으며 중동부 유럽만 1.4% 증가 [사실]",
  "브랜드: 폭스바겐 승용차 19.3%, 아우디 19.7%, 포르쉐 15% 감소, 1~9월 누적은 약 601만 대로 9% 줄고 중국은 30.2% 감소 [사실]",
  "포르쉐: 1~9월 인도 17만 8,532대로 16% 줄었고 최상위 모델 가격 약 20% 인상 등 가치 중심 전략을 내놓음 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 14.3% 감소·약 189만 대, 중국 38.5%, 지역·브랜드별 수치, 9개월 누적(RTE·쿼츠·RTT뉴스)",
 "src": [{"o": "RTE", "d": "2026-10-12", "u": "https://www.rte.ie/news/business/2026/1012/1594972-volkswagen-quarterly-deliveries/"},
         {"o": "Quartz", "d": "2026-10-12", "u": "https://qz.com/volkswagen-deliveries-decline-china-sales-third-quarter-101226"},
         {"o": "RTTNews", "d": "2026-10-12", "u": "https://www.rttnews.com/3698112/volkswagen-q3-deliveries-fall-14-3.aspx"}],
 "inds": ["auto"], "nodes": [],
 "items": [
  it("폭스바겐그룹, 3분기 차량 인도량 14% 감소 발표", "로이터", "2026-10-12", R+"business/volkswagen-reports-14-drop-third-quarter-deliveries-2026-10-12/")]})

items.append({"cid": "C126", "attachTo": "",
 "title": "인니 중앙은행 새 총재 \"금리 결정 자율권 완전히 보유\"",
 "one": "데스트리 다마얀티 인도네시아 중앙은행 신임 총재가 정부와 협력하면서도 금리 결정에는 완전한 자율권이 있다고 밝히면서, 독립성 우려로 흔들린 루피아와 국채 투자자 신뢰를 되찾으려 하고 있다",
 "facts": [
  "무엇이: 데스트리 다마얀티 총재가 인터뷰에서 정부와 시너지를 내면서도 정책금리에 대한 완전한 자율권을 갖고 있다고 발언 [사실]",
  "우려 배경: 정부 관료가 월례 정책회의 일부에 참석하고, 의회가 성장 비중을 높이도록 권한을 넓혔으며, 프라보워 대통령의 조카가 고위직에 임명됨 [사실]",
  "금리: 9월 첫 회의에서 기준금리를 5.75%로 동결하고 대신 루피아 채권 외국인 투자자 헤지 비용 할인을 확대, 다음 회의는 10월 21일 [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 신임 총재의 자율권 발언과 독립성 우려 배경, 9월 5.75% 동결(파이니마이즈·트레이딩이코노믹스). 날짜 표기가 출처마다 일부 불일치",
 "src": [{"o": "Finimize", "d": "2026-10-12", "u": "https://finimize.com/content/bank-indonesias-new-governor-tries-to-calm-independence-fears"},
         {"o": "Trading Economics", "d": "2026-10", "u": "https://tradingeconomics.com/indonesia/interest-rate"}],
 "inds": ["macro"], "nodes": ["macro/cb", "macro/fx"],
 "items": [
  it("인도네시아 중앙은행 새 총재 \"금리에 대한 완전한 자율권 보유\"", "로이터", "2026-10-12", R+"world/asia-pacific/indonesia-central-bank-has-full-autonomy-over-interest-rates-new-chief-says-2026-10-12/")]})

items.append({"cid": "C134", "attachTo": "",
 "title": "소프트뱅크 투자 나이지리아 핀테크 오페이, 뉴욕 상장으로 최대 5억 달러 조달 추진",
 "one": "소프트뱅크가 투자한 나이지리아 핀테크 오페이가 뉴욕증권거래소 상장과 스탠다드은행 사모 배정을 합쳐 약 5억 달러 조달을 추진하면서, 상반기 매출이 두 배 넘게 늘어난 아프리카 핀테크의 미국 증시 데뷔가 시험대에 오른다",
 "facts": [
  "무엇이: 오페이가 뉴욕증권거래소 IPO와 스탠다드은행 그룹 대상 동시 사모로 약 5억 달러 조달을 목표로 함, 스탠다드은행 지분은 상장 후 4.99% 이하 [사실]",
  "실적: 2026년 상반기 매출 4억 6,710만 달러로 전년 1억 9,750만 달러에서 급증, 순이익 9,090만 달러, 대손충당금은 3,810만 달러에서 1억 1,840만 달러로 증가 [사실]",
  "가치·일정: 기업가치 약 40억 달러가 거론되며 11월 중순 가격 결정 기대, 소프트뱅크 지분은 상장 전 6.6% [사실]"],
 "basis": "verified",
 "check": "검색 결과 요약으로 확인: 약 5억 달러 목표, 상반기 실적, 40억 달러 가치, 소프트뱅크 6.6%(세마포·핀테크 매체). 공모가 범위는 아직 미정",
 "src": [{"o": "Semafor", "d": "2026-10-12", "u": "https://www.semafor.com/article/10/12/2026/opay-readies-4b-new-york-ipo"},
         {"o": "BusinessDay", "d": "2026-10", "u": "https://businessday.ng/technology/article/softbank-joins-opays-500m-fundraise-ahead-of-nyse-debut/"}],
 "inds": ["fin"], "nodes": [],
 "items": [
  it("소프트뱅크 투자 오페이, 뉴욕 상장으로 최대 5억 달러 조달 노려", "블룸버그", "2026-10-12", B+"articles/2026-10-12/softbank-backed-opay-eyes-up-to-500-million-in-new-york-listing")]})

items.append({"cid": "C142", "attachTo": "",
 "title": "바슈롬 손더스 CEO 사임…아피오 이사회 의장이 임시 CEO 맡아",
 "one": "안과 기업 바슈롬의 손더스 CEO가 물러나고 아피오 이사회 의장이 임시 최고경영자로 선임되면서, 새 경영진 선임 전까지 회사 전략과 경영 방향에 변화가 생길 수 있다 (제목 기준)",
 "facts": [
  "무엇이: 바슈롬 손더스 CEO가 사임하고 아피오 의장이 임시 CEO로 선임 [제목]",
  "의미: 정식 후임 선임 전까지 리더십 공백 [추론]"],
 "basis": "title",
 "check": "검색 한도 안에서 확인하지 못함, 로이터 제목 기준",
 "src": [],
 "inds": ["pharma"], "nodes": [],
 "items": [
  it("바슈롬 손더스 CEO 사임, 아피오 의장 임시 최고경영자 선임", "로이터", "2026-10-13", R+"legal/transactional/bausch-lomb-ceo-saunders-steps-down-chairman-appio-appointed-interim-chief-2026-10-12/")]})

items.append({"cid": "C150", "attachTo": "",
 "title": "커맨더스 새 NFL 경기장 계획에 워싱턴DC, 지방채 발행 검토",
 "one": "워싱턴 커맨더스의 새 NFL 경기장 건설 계획을 계기로 워싱턴DC가 지방채 발행을 검토하면서, 경기장 재원을 공공 부채로 조달하는 지방채 공급이 늘어날 수 있다 (제목 기준)",
 "facts": [
  "무엇이: 커맨더스의 새 NFL 경기장 계획에 따라 워싱턴DC가 지방채 매각을 저울질 [제목]",
  "의미: 스포츠 시설 재원 조달에 공공 부채가 쓰일 수 있음 [추론]"],
 "basis": "title",
 "check": "검색 한도 안에서 확인하지 못함, 블룸버그 제목 기준",
 "src": [],
 "inds": ["fin"], "nodes": [],
 "items": [
  it("워싱턴 커맨더스 새 NFL 경기장 계획에 DC, 지방채 발행 검토", "블룸버그", "2026-10-13", B+"articles/2026-10-12/washington-commanders-new-nfl-stadium-plan-prompts-dc-to-weigh-muni-bond-sale")]})

items.append({"cid": "C166", "attachTo": "",
 "title": "中 공업박람회에 첫 반도체 전용관…화홍 \"2030년 특수공정 자급 40% 넘어\"",
 "one": "중국이 상하이 국제공업박람회에 처음으로 반도체 전용관을 열어 설계·장비·소재 국산 공급망을 선보이고 화홍반도체가 2030년 특수공정 자급률 40% 이상을 내다봤지만, 핵심인 DUV 노광장비는 공개하지 않았다 (채널 전언)",
 "facts": [
  "무엇이: 10월 12일 상하이에서 개막한 제26회 중국국제공업박람회가 처음으로 집적회로 전용관을 마련해 설계·제조·패키징·장비·소재 전 산업망을 전시 [채널]",
  "전망: 화홍반도체 회장은 중국 특수공정 파운드리의 글로벌 ASP 비중이 2024년 66%에서 2030년 76%로 오르고 분야별 자급 비중이 모두 40%를 넘을 것으로 예상 [채널]",
  "장비·EDA: AMEC은 고급 장비 54종을 개발했고, 화다주톈은 국산 EDA 커버리지가 30%에서 85%로 넓어졌다고 설명 [채널]",
  "한계: 상하이마이크로일렉트로닉스는 DUV 노광장비 실물을 전시하지 않고 인터뷰를 거부했으며, 대만계 장비업체는 중국 사업의 어려움을 토로 [채널]"],
 "basis": "channel",
 "check": "검색으로 박람회 일정(10월 12~16일)과 집적회로 전시 구역만 확인, 화홍·DUV 관련 내용은 확인 못 함",
 "src": [],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "items": [
  it("중국 공업박람회서 반도체 자립 과시…DUV 노광장비 실물은 미공개", H, "2026-10-13", "https://t.me/HANAchina/70315")]})

skipped = [
 {"cid": "C053", "reason": "AI 투자 증액"},
 {"cid": "C158", "reason": "범위 밖"}]

out = {"agent": "W8", "searches_used": 16, "fetches_used": 0, "items": items, "skipped": skipped}
p = "/home/user/news-desk/data/mix-2026-10-13/out2/W8.json"
json.dump(out, open(p, "w"), ensure_ascii=False, indent=1)
for x in items:
    n = len(re.sub(r' \((제목 기준|채널 전언)\)$', '', x['one']))
    single = len(x['items']) == 1 and not x['attachTo']
    lo, hi = (80, 130) if single else (90, 160)
    flag = "" if lo <= n <= hi else " <-- one"
    tl = len(x['title'])
    if not 20 <= tl <= 50: flag += f" title{tl}"
    for i in x['items']:
        if not 25 <= len(i['t']) <= 60: flag += f" t{len(i['t'])}:{i['t']}"
    for f in x['facts']:
        if '|' in f or '**' in f: flag += " badfact"
    print(x['cid'], n, flag)
