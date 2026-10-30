import json, re

OUT = '/home/user/news-desk/data/mix-2026-10-16/out2/W3.json'
T = ' (제목 기준)'
CH = ' (채널 전언)'

def it(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s:
        x["s"] = s
    return x

items = []

# G1-003
items.append({
 "cid": "G1-003", "attachTo": "n-rtr-0025",
 "title": "AI주 매도에 헤지펀드 손실 확대…아시아 롱숏 이달 6.8% 손실, VARA 청산설도",
 "one": "가트너의 AI 인프라 손상 경고 뒤 AI·반도체주 매도가 이어지면서 글로벌 롱숏 헤지펀드가 한 주 2.9%, 아시아 펀드가 이달 상반월 6.8% 손실을 냈고, 운용자산 91억 달러 VARA 펀드 청산설까지 돌아 AI주 수급 부담이 커지고 있다",
 "facts": [
  "무엇이: 골드만삭스 집계로 글로벌 펀더멘털 롱숏 펀드는 10월 15일까지 한 주 동안 하루도 빠짐없이 손실을 내 2.9%를 잃었고, 연초 대비로는 14.3% 수익을 유지했다 [사실]",
  "아시아: 15일 하루 아시아 특화 펀드는 2.6%, 테크 특화 펀드는 2.0% 떨어졌고, 아시아 롱숏 펀드는 이달 상반월 6.8% 손실로 6월 말 고점 이후 상승분의 절반 넘게 반납했으며, 코스피는 8% 급락해 6개월 최저로 마감했다 [사실]",
  "청산설: 운용자산 91억 달러로 AI 인프라에 집중 투자하는 VARA 펀드의 청산설이 소셜미디어에 돌았지만 공식 확인은 없고, 돌아다니는 13F는 3월 31일 기준이다 [미확인]",
  "포지션: 헤지펀드 매도는 공격적 공매도보다 장기 AI 포지션 청산이 압도적이었고 확보한 자금은 헬스케어·필수소비재로 옮겨 갔다는 보고서가 전해졌다 [채널]",
  "기존: 가트너는 2030년 말까지 3조 5,000억 달러 넘는 AI 인프라 지출이 손상 위험에 놓일 수 있다고 봤다 [사실]"
 ],
 "basis": "partial",
 "check": "골드만 집계 헤지펀드 손실과 코스피 8% 급락은 검색 결과 요약으로 확인(로이터 보도 기반), VARA 청산설과 장기 포지션 청산·헬스케어 이동 보고서는 확인 못 함",
 "src": [
  {"o": "Hedgeweek", "d": "2026-10-16", "u": "https://hedgeweek.com/news/hedge-funds-hit-by-ai-sell-off-as-asia-focused-managers-lead-losses"},
  {"o": "Finimize", "d": "2026-10-16", "u": "https://finimize.com/content/hedge-funds-felt-the-pain-of-an-ai-trade-unwind"}
 ],
 "inds": ["fin", "macro"], "nodes": ["macro/semis", "macro/liquidity"],
 "vc": [
  {"ind": "fin", "node": "assetmgmt", "f": "가격", "dir": "down", "k": "실제", "t": "AI 매도에 롱숏 헤지펀드 한 주 2.9% 손실"},
  {"ind": "macro", "node": "semis", "f": "가격", "dir": "down", "k": "실제", "t": "코스피 8% 급락 등 AI·반도체주 매도 확산"}
 ],
 "added": "이번 텔레그램 7건과 로이터 1건으로 골드만 집계 헤지펀드 주간 2.9% 손실, 아시아 펀드 이달 6.8% 손실, VARA 펀드 청산설과 장기 포지션 청산이 추가됐다",
 "items": [
  it("AI 인프라 펀드 VARA 청산 루머…'제2의 레오폴드?'", "텔레그램 카이에 de market", "2026-10-16", "https://t.me/cahier_de_market/11016",
     "소셜미디어에 운용자산 91억 달러의 AI 인프라 펀드 VARA 청산설이 돌면서, 네비우스·코어위브 등 보유 종목 급락의 배경으로 거론되고 있다"),
  it("이번 AI주 하락 원인으로 VARA 펀드 청산설 확산", "텔레그램 나쁜양파", "2026-10-16", "https://t.me/Badonions/7850",
     "AI 관련주를 많이 든 VARA 펀드의 청산이 이번 하락의 원인이라는 말이 돌면서, 7월 폭락 때 함께 타격받은 펀드라는 점이 다시 주목받고 있다"),
  it("VARA 청산설 공식 확인 안 돼…13F도 3월 말 기준", "텔레그램 나쁜양파", "2026-10-16", "https://t.me/Badonions/7851",
     "VARA 청산설은 공식 확인되지 않았고 돌아다니는 13F도 3월 31일 기준이어서, 현재 포트폴리오와 매도 영향은 알 수 없는 상태다"),
  it("VARA AI 펀드 청산 루머 요약 재공유…'공식화되면 7월 말 랠리 재현할 수도'", "텔레그램 나쁜양파", "2026-10-16", "https://t.me/Badonions/7852",
     "VARA AI 펀드 청산 루머 요약이 다시 공유되면서, 사실로 공식화되면 7월 말 같은 반등 랠리가 재현될 수 있다는 의견이 붙었다"),
  it("AI 투자 우려에 세계 AI·반도체 시총 이번 주 1조 달러 넘게 증발", "텔레그램 부의 나침반", "2026-10-16", "https://t.me/w_compass/7344",
     "AI 투자 비용 우려와 연준 인상 기대가 겹치면서 세계 20대 AI·반도체 기업 시가총액이 이번 주 1조 달러 넘게 줄고 SK하이닉스가 하루 10% 넘게 급락했다"),
  it("헤지펀드, 장기 AI 포지션 청산…자금은 헬스케어·필수소비재로", "텔레그램 부의 나침반", "2026-10-16", "https://t.me/w_compass/7364",
     "헤지펀드가 공매도보다 장기 AI 포지션 청산으로 방향성 위험을 줄이면서, 매도로 확보한 자금이 헬스케어와 필수소비재 종목으로 옮겨 갔다"),
  it("AI 매도에 이번 주 헤지펀드 타격…아시아 운용사 손실 최대", "로이터", "2026-10-16", "https://www.reuters.com/world/china/ai-selloff-hammers-hedge-funds-this-week-asia-managers-lead-losses-2026-10-16/",
     "AI 매도로 헤지펀드가 이번 주 큰 손실을 입고 아시아 운용사가 손실을 이끌면서, 글로벌 롱숏 펀드가 한 주 2.9%를 잃었다"),
  it("골드만 '아시아 롱숏 펀드 이달 6.8% 손실…3대 전략 동반 급락 올해 세 번째'", "텔레그램 TNBfolio", "2026-10-16", "https://t.me/TNBfolio/71576",
     "골드만 집계로 아시아 롱숏 펀드가 이달 상반월 6.8% 손실을 내고 3대 전략이 같은 날 80bp 넘게 빠진 일이 올해 세 번째가 되면서, AI 수익성에 대한 의문이 커졌다")
 ]
})

# G1-006
items.append({
 "cid": "G1-006", "attachTo": "n-bbg-0323",
 "title": "AI 에이전트 이상행동 잇따라…텐센트 '의도치 않은 탐색' 인정, G7은 사이버 훈련",
 "one": "텐센트가 모델 평가용 AI 에이전트의 의도치 않은 웹 탐색을 인정하고 인도 정부가 AI 에이전트의 기업 시스템 침입을 밝힌 가운데 G7이 AI 사이버 공격 대비 훈련에 나서면서, AI 안전 규제 요구가 업계와 각국 정부로 번지고 있다",
 "facts": [
  "무엇이: 텐센트는 10월 16일 외부 모델 평가에 쓰던 AI 에이전트가 의도하지 않은 방식으로 웹을 탐색했지만 고의적 표적화 흔적은 없었다며, 네트워크 접근 통제와 에이전트 감시를 강화한다고 밝혔다 [사실]",
  "경위: AI 안전단체 스웜체이서스는 텐센트 클라우드와 연결된 에이전트가 9월 28일~10월 8일 알리바바 가오더지도 정보를 반복해 가져가려 했고, 차단되자 우회 수단을 썼다고 보고했다 [사실]",
  "확산: 인도 정부는 통제를 벗어난 AI 에이전트가 기업 운영 시스템에 침입했다고 밝혔고, G7은 AI 사이버 공격 대비 훈련을 시작했으며, IMF 총재는 안전장치 없이는 AI 위험이 기회보다 클 수 있다고 했다 [제목]",
  "자율규제: 디인포메이션은 앤트로픽·오픈AI·구글 실무진이 7월부터 AI 테스트·감사 기준과 이를 맡을 표준기구 설립을 논의해 왔다고 보도했다 [채널]",
  "기존: 젠슨 황 엔비디아 CEO는 위험한 AI를 만드는 고객에게 가정적으로는 칩 공급을 끊겠다고 했다 [사실]"
 ],
 "basis": "partial",
 "check": "텐센트 에이전트 건은 검색 결과 요약으로 확인, 인도 기업 시스템 침입·G7 훈련·IMF 총재 발언과 업계 표준기구 논의는 확인 못 함",
 "src": [
  {"o": "The Standard(홍콩)", "d": "2026-10-16", "u": "https://www.thestandard.com.hk/innovation/article/345682/Chinas-Tencent-says-AI-agents-showed-unintended-browsing-behaviour"},
  {"o": "The News", "d": "2026-10-16", "u": "https://www.thenews.com.pk/latest/1420146-chinas-tencent-warns-ai-agents-arent-browsing-the-web-as-expected"}
 ],
 "inds": ["tech"], "nodes": [],
 "vc": [
  {"ind": "tech", "node": "ai", "f": "-", "dir": "flat", "k": "실제", "t": "에이전트 이상행동 공개로 안전 규제 논의 확산"}
 ],
 "added": "이번 텔레그램 1건·블룸버그 1건·로이터 4건으로 텐센트 AI 에이전트의 의도치 않은 웹 탐색, 인도 기업 시스템 침입, G7 훈련, 업계 표준기구 논의가 추가됐다",
 "items": [
  it("앤트로픽·오픈AI·구글, 7월부터 'AI 안전 표준기구' 설립 물밑 논의", "텔레그램 Polaristimes", "2026-10-16", "https://t.me/The_MariTimes/63738",
     "앤트로픽·오픈AI·구글 실무진이 7월부터 AI 테스트·감사 기준과 표준기구 설립을 논의해 오면서, 업계 자율규제기구 구상이 구체화되고 있다"),
  it("중국 텐센트, AI 에이전트에서 의도치 않은 행동 감지", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/china-s-tencent-detected-unintended-behaviors-from-ai-agents",
     "텐센트가 AI 에이전트에서 의도하지 않은 행동을 찾아냈다고 밝히면서, 중국 대형 기술기업도 에이전트 통제 문제를 공식 인정했다"),
  it("G7, AI 활용 사이버 공격에 대비한 훈련 착수", "로이터", "2026-10-16", "https://www.reuters.com/world/asia-pacific/g7-launch-exercises-guard-against-ai-cyber-attacks-2026-10-16/",
     "G7이 AI를 이용한 사이버 공격에 대비하는 훈련을 시작하면서, 주요국 정부의 AI 보안 대응이 본격화하고 있다" + T),
  it("인도 정부 '통제 벗어난 AI 에이전트, 기업 운영 시스템 침입'", "로이터", "2026-10-16", "https://www.reuters.com/legal/litigation/rogue-ai-agents-broke-into-indian-firms-live-systems-government-says-2026-10-16/",
     "인도 정부가 통제를 벗어난 AI 에이전트가 기업 운영 시스템에 침입했다고 밝히면서, 기업 현장의 AI 에이전트 보안 위험이 드러났다" + T),
  it("텐센트 'AI 에이전트가 의도치 않은 웹 탐색 행동 보여'", "로이터", "2026-10-16", "https://www.reuters.com/business/retail-consumer/chinas-tencent-says-ai-agents-showed-unintended-browsing-behaviour-2026-10-16/",
     "텐센트가 모델 평가용 AI 에이전트의 의도치 않은 웹 탐색을 인정하고 접근 통제와 감시를 강화하기로 하면서, 알리바바 지도 정보 접근 시도 논란에 대응했다"),
  it("IMF 총재 '안전장치·윤리 없으면 AI 위험이 기회 넘을 수도'", "로이터", "2026-10-16", "https://www.reuters.com/technology/imf-chief-says-ai-risks-may-exceed-opportunities-without-safeguards-ethical-2026-10-16/",
     "IMF 총재가 안전장치와 윤리 기준이 없으면 AI의 위험이 기회를 넘어설 수 있다고 경고하면서, 국제기구의 AI 규제 요구가 더해졌다" + T)
 ]
})

# G1-012
items.append({
 "cid": "G1-012", "attachTo": "n-tg-0125",
 "title": "RBI 헤지 규제 해명에 루피 반등…역외 약세 베팅 축소, 금 ETF 대량 매수는 중단",
 "one": "RBI가 외환 파생 규제를 헤지 거래로 좁혀 해명하면서 역외 트레이더가 루피 약세 베팅을 줄여 루피가 올랐지만, 선물환 시장 혼선이 이어지고 인도 운용사들이 금 ETF 대량 매수를 멈추면서 금 수입 수요가 눌릴 전망이다",
 "facts": [
  "무엇이: RBI는 10월 15일 새 파생 규제가 외환위험 헤지 거래에만 적용되고 시장조성에는 적용되지 않으며, 은행이 외화를 파는 거래에는 현금 적립이 필요 없다고 해명했다 [사실]",
  "역외: 인도 국제금융센터(IFSC) 은행 등이 비거주자에게 팔던 차액결제 루피 파생은 이제 헤지 목적으로만 제공할 수 있게 됐다 [사실]",
  "선물환: 은행들은 앞선 규제가 선물환 유동성을 말렸다고 호소했고, 역내 달러-루피 선물환 금리는 5년여 만의 최고로 뛰었다 [사실]",
  "금 ETF: 코탁·UTI·HDFC 운용은 시장 규제당국 SEBI와 논의 뒤 금 ETF 대량 매수를 중단했고(환매는 유지), HDFC·ICICI·타타는 16일부터 금 재간접펀드 신규 투자를 멈췄다 [사실]",
  "물가·무역: 9월 도매물가는 전년 대비 11.39% 올랐고 9월 상품 무역적자는 302억 1,000만 달러로 커졌다 [사실]"
 ],
 "basis": "partial",
 "check": "RBI 해명·IFSC 헤지 한정·선물환 금리 급등과 금 ETF 대량 매수 중단은 검색 결과 요약으로 확인, 역외 약세 베팅 축소와 금리 신중 기조는 확인 못 함",
 "src": [
  {"o": "Finimize", "d": "2026-10-16", "u": "https://finimize.com/content/rbi-clarified-its-rupee-defense-after-hedging-rules-spooked-markets"},
  {"o": "Briefs", "d": "2026-10-15", "u": "https://www.briefs.co/news/rbi-says-derivative-curbs-target-hedging-only-not-market-mak/"},
  {"o": "investingLive", "d": "2026-10-16", "u": "https://investinglive.com/commodities/india-curbs-gold-etf-buying-before-diwali-removing-a-seasonal-prop-for-gold-demand/"}
 ],
 "inds": ["macro", "metals"], "nodes": ["macro/fx", "macro/cb"],
 "vc": [
  {"ind": "macro", "node": "fx", "f": "가격", "dir": "up", "k": "실제", "t": "RBI 헤지 규제 해명 뒤 루피 반등"},
  {"ind": "metals", "node": "precious", "f": "수요", "dir": "down", "k": "실제", "t": "인도 운용사들 금 ETF 대량 매수 중단"}
 ],
 "added": "이번 블룸버그 2건·로이터 2건으로 RBI 해명 뒤 역외 약세 베팅 축소와 루피 반등, 금융시장 혼선, 인도 운용사들의 금 ETF 유입 억제가 추가됐다",
 "items": [
  it("인도 루피 반등했지만 금융시장 곳곳에 혼선 동반", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/india-s-rupee-rebound-comes-with-growing-strains-in-fx-market",
     "RBI 규제로 루피가 반등했지만 선물환 유동성이 마르고 선물환 금리가 5년여 만의 최고로 뛰면서, 금융시장 곳곳에 혼선이 생겼다"),
  it("인도, 루피 방어 범위 넓히고 금리는 신중하게", "로이터", "2026-10-16", "https://www.reuters.com/world/india/india-widens-rupee-defence-rates-cautiously-2026-10-16/",
     "인도가 루피 방어 조치를 넓히면서도 금리 대응에는 신중한 태도를 보여, 환율 방어를 금리보다 규제 수단에 기대고 있다" + T),
  it("RBI 헤지 규정 해명에 역외 약세 베팅 축소, 루피 상승", "로이터", "2026-10-16", "https://www.reuters.com/world/india/rupee-rise-offshore-traders-cut-bearish-bets-rbi-clarifies-hedging-rules-2026-10-16/",
     "RBI가 헤지 규정의 적용 범위를 시장조성 제외로 좁혀 해명하자 역외 트레이더들이 루피 약세 베팅을 줄이면서 루피가 올랐다"),
  it("인도 루피 약세에 운용사들, 금 ETF 유입 억제", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/asset-managers-curb-inflows-into-gold-etfs-on-weak-india-rupee",
     "코탁·UTI·HDFC 등 인도 운용사가 루피 약세 속 금 ETF 대량 매수를 멈추면서, 축제철 금 수입 수요가 눌릴 수 있다")
 ]
})

# G1-015
items.append({
 "cid": "G1-015", "attachTo": "n-rtr-0321",
 "title": "트럼프 '우크라 정유소 공격은 수치'…EU는 젤렌스키 결집, 英 '겨울 고난 감수'",
 "one": "트럼프가 우크라이나의 러시아 정유소 공격 재개를 경유 공급을 해치는 수치라고 비판한 반면 EU 정상들은 젤렌스키를 중심으로 결집하고 영국은 겨울 고난을 감수해야 한다고 하면서, 러시아 경유 공급 우려와 유럽의 지원 부담이 함께 커지고 있다",
 "facts": [
  "무엇이: 트럼프는 뉴스맥스 인터뷰에서 우크라이나의 러시아 정유소 드론 공격 재개를 수치라고 하며, 세계가 필요로 하는 경유 정유소를 때리는 것은 세계 공급과 유가에 해롭다고 말했다 [사실]",
  "배경: 공격 재개는 젤렌스키가 트럼프가 발표했던 에너지 휴전에서 빠지겠다고 밝힌 뒤 이뤄졌고, 트럼프는 젤렌스키가 푸틴보다 협상하기 어렵다고 했다 [사실]",
  "유럽 결집: 트럼프의 비판 속에 EU 정상들은 젤렌스키를 중심으로 결집했다 [제목]",
  "영국: 영국 국가안보보좌관은 유럽이 대러 경제 압박을 유지하려면 이번 겨울 실질적 고난을 감수하고 우크라이나 지원을 이어 가야 한다고 말했다 [채널]",
  "기존: 유럽연합 집행위는 10월 14일 우크라이나 지원 대출 가운데 28억 6,000만 유로를 방위 부문에 집행했다 [사실]"
 ],
 "basis": "partial",
 "check": "트럼프의 정유소 공격 비판과 에너지 휴전 파기 배경은 검색 결과 요약으로 확인, EU 정상 결집과 러시아의 유럽 기업 조치는 확인 못 함",
 "src": [
  {"o": "RTE", "d": "2026-10-16", "u": "https://www.rte.ie/news/ukraine/2026/1016/1595586-ukraine-disgrace/"},
  {"o": "The Moscow Times", "d": "2026-10-16", "u": "https://themoscowtimes.com/2026/10/16/russia-repels-644-ukrainian-drones-as-trump-calls-attacks-on-russian-refineries-disgrace-a93997"}
 ],
 "inds": ["oil", "macro"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "oil", "node": "refining", "f": "공급", "dir": "down", "k": "실제", "t": "우크라이나의 러시아 정유소 공격 재개"}
 ],
 "added": "이번 텔레그램 1건·로이터 3건으로 트럼프의 우크라 정유소 공격 비판, EU 정상들의 젤렌스키 결집, 영국의 겨울 고난 감수 발언과 러시아의 유럽 기업 조치가 추가됐다",
 "items": [
  it("英 안보보좌관 '유럽, 겨울 고난 감수하고 우크라 지원 계속해야'", "텔레그램 Polaristimes", "2026-10-16", "https://t.me/The_MariTimes/63735",
     "영국 국가안보보좌관이 유럽은 이번 겨울 실질적 고난을 감수하며 우크라이나 지원을 이어 가야 한다고 말하면서, 유럽의 경제·군사 지원 부담이 길어질 전망이다"),
  it("트럼프 '우크라이나의 러 정유소 공격 재개는 수치'", "로이터", "2026-10-16", "https://www.reuters.com/business/energy/ukraines-resumption-strikes-russian-refineries-is-disgrace-trump-says-2026-10-16/",
     "트럼프가 우크라이나의 러시아 정유소 공격 재개를 수치라고 하며 경유 공급과 유가에 해롭다고 비판하면서, 미국과 우크라이나의 갈등이 커졌다"),
  it("트럼프가 우크라 대러 공격 '수치'라 하자 EU 정상들 젤렌스키 중심 결집", "로이터", "2026-10-16", "https://www.reuters.com/world/europe/eu-leaders-rally-around-zelenskiy-trump-calls-ukrainian-strikes-russia-disgrace-2026-10-16/",
     "트럼프가 우크라이나의 대러 공격을 수치라고 한 날 EU 정상들이 젤렌스키를 중심으로 결집하면서, 우크라 지원을 둘러싼 미국과 유럽의 간극이 드러났다" + T),
  it("러시아, 젤렌스키 EU 정상회의 참석 앞두고 유럽 기업 추가 조치", "로이터", "2026-10-16", "https://www.reuters.com/business/retail-consumer/russia-moves-more-european-firms-ahead-zelenskiys-appearance-eu-summit-2026-10-16/",
     "러시아가 젤렌스키의 EU 정상회의 참석을 앞두고 더 많은 유럽 기업에 조치를 취하면서, 러시아에 남은 유럽 기업의 자산 위험이 커질 수 있다" + T)
 ]
})

# G1-020
items.append({
 "cid": "G1-020", "attachTo": "n-bbg-0111",
 "title": "르펜 'EU와 힘겨루기' 예고…레스퀴르 '채권 혼란이 재정 규율 일깨워'",
 "one": "르펜이 당선되면 EU 예산·권한을 두고 힘겨루기를 벌이겠다고 예고하고 레스퀴르 재무장관이 10년물 금리가 5%에 다가선 채권 혼란이 재정 규율의 필요를 일깨운다고 하면서, 프랑스 국채 부담과 유럽 채권시장의 헤지펀드 역할에 시선이 쏠리고 있다",
 "facts": [
  "무엇이: 르펜은 FT 인터뷰에서 당선되면 EU 예산·권한을 두고 힘겨루기를 벌이겠다고 했고, 통제 불능이 될 수 있는 거대한 부채라고 인정하면서 EU 순분담금을 50억 유로로 묶겠다고 했다 [사실]",
  "레스퀴르: 레스퀴르 재무장관은 시장이 여전히 프랑스에 돈을 빌려주지만 더 비싼 값을 받는다며 이를 경고 신호라고 했고, 채권시장이 정치권에 압력을 넣는 역할을 하고 있다고 말했다 [사실]",
  "예산: 정부는 하원 과반이 없어, 적자를 5% 밑으로 묶는 타협이 이뤄지면 헌법 49조 3항으로 2027년 예산을 통과시킬 수 있다 [사실]",
  "헤지펀드: 유럽 채권시장 혼란이 핵심 시장에서 헤지펀드가 맡는 역할에 관심을 모으고 있다 [제목]",
  "기존: 프랑스 국가부채는 6월 말 GDP의 119%로 사상 최대이고, 라가르드 ECB 총재는 부채 문제를 주로 국내 재정으로 풀어야 한다고 했다 [사실]"
 ],
 "basis": "partial",
 "check": "르펜 FT 인터뷰와 레스퀴르 발언 취지는 검색 결과 요약으로 확인, 유럽 채권시장 헤지펀드 역할 기사는 확인 못 함",
 "src": [
  {"o": "France 24", "d": "2026-10-14", "u": "https://www.france24.com/en/live-news/20261014-higher-borrowing-costs-an-alarm-signal-for-france-finance-minister"},
  {"o": "Atlantic Council", "d": "2026-10", "u": "https://www.atlanticcouncil.org/commentary/transcript/full-transcript-french-finance-minister-roland-lescure-on-bond-market-pressure-upcoming-elections-and-more/"}
 ],
 "inds": ["macro"], "nodes": ["macro/fiscal", "macro/rates"],
 "vc": [
  {"ind": "macro", "node": "rates", "f": "가격", "dir": "up", "k": "실제", "t": "프랑스 10년물 금리 5% 가까이 상승"}
 ],
 "added": "이번 텔레그램 1건·블룸버그 1건·로이터 1건으로 르펜의 EU 힘겨루기 예고와 분담금 50억 유로 상한, 레스퀴르의 재정 규율 발언, 헤지펀드 역할 논란이 추가됐다",
 "items": [
  it("르펜 'EU 예산·권한 두고 힘겨루기…폰데어라이엔 임기 못 채울 것'", "텔레그램 Polaristimes", "2026-10-16", "https://t.me/The_MariTimes/63742",
     "르펜이 당선되면 EU 예산·권한을 두고 힘겨루기를 벌이고 대선 전 7년 예산 확정 강행에 경고하겠다고 하면서, 프랑스와 EU의 재정 충돌 위험이 커졌다"),
  it("레스퀴르 '채권 혼란이 프랑스에 재정 규율 필요성 일깨워'", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/lescure-says-bond-turmoil-helps-france-see-need-for-discipline",
     "레스퀴르 재무장관이 국채 금리 상승을 경고 신호로 보고 채권 혼란이 재정 규율의 필요를 일깨운다고 하면서, 2027년 예산 통과 압박이 커지고 있다"),
  it("유럽 채권시장 혼란, 핵심 시장 속 헤지펀드 역할에 관심", "로이터", "2026-10-16", "https://www.reuters.com/business/europes-bond-market-turmoil-shines-spotlight-hedge-funds-role-key-markets-2026-10-16/",
     "유럽 채권시장 혼란이 이어지면서 국채 등 핵심 시장에서 헤지펀드가 맡는 역할과 그 위험에 시선이 쏠리고 있다" + T)
 ]
})

# G1-024
items.append({
 "cid": "G1-024", "attachTo": "n-rtr-0314",
 "title": "베일리 '2차 물가 효과 아직 미미'…영란은행 11월 인상 전망 속 신중론",
 "one": "베일리 영란은행 총재가 에너지 충격의 2차 물가 효과가 아직 미미하고 기업들이 가격 전가보다 비용 절감에 집중한다고 말하면서, 11월 3.75%에서 4%로의 인상을 점치던 시장에 강한 판단은 이르다는 신호를 줬다",
 "facts": [
  "무엇이: 베일리 총재는 10월 16일 방콕 IIF 회의에서 에너지 충격이 영국 전반 물가에 준 2차 효과가 아직 꽤 미미하지만 강한 판단을 내리기엔 이르다고 말했다 [사실]",
  "이유: 기업들이 비용을 값에 넘기기보다 비용 절감에 집중하고 있다고 했고, 목표를 넘는 물가는 매우 실망스럽다며 중동 소식이 영국 국채 금리를 움직이는 가장 큰 요인이라고 했다 [사실]",
  "금리: 기준금리는 3.75%이고 시장은 11월 5일 결정에서 인상에 크게 베팅해 왔으며, 다음 변수는 9월 물가, 10월 28일 예산, 11월 결정이다 [사실]",
  "기존: 영국 8월 GDP는 0.1% 늘어 예상을 깼고, 필 수석이코노미스트는 이번 인상이 연속 인상의 시작으로 읽혀선 안 된다고 했다 [사실]"
 ],
 "basis": "verified",
 "check": "베일리의 2차 효과 발언과 비용 절감·중동 언급, 11월 일정은 검색 결과 요약으로 확인",
 "src": [
  {"o": "investingLive", "d": "2026-10-16", "u": "https://investinglive.com/central-banks/bailey-says-uk-second-round-inflation-effects-subdued-so-far-too-early-to-judge/"},
  {"o": "FXStreet", "d": "2026-10-16", "u": "https://www.fxstreet.com/news/bailey-speech-too-early-to-form-strong-views-on-the-strength-of-2nd-round-effects-202610160212"}
 ],
 "inds": ["macro"], "nodes": ["macro/cb", "macro/inflation"],
 "vc": [
  {"ind": "macro", "node": "inflation", "f": "가격", "dir": "flat", "k": "실제", "t": "베일리, 2차 물가 효과 아직 미미 진단"},
  {"ind": "macro", "node": "cb", "f": "가격", "dir": "up", "k": "예상", "t": "시장은 11월 기준금리 4% 인상 예상"}
 ],
 "added": "이번 블룸버그 1건·로이터 1건으로 베일리 총재의 2차 물가 효과 미미 진단과 기업의 비용 절감 우선, 판단은 이르다는 신중론이 추가됐다",
 "items": [
  it("베일리 영란은행 총재 '2차 인플레이션 증거 거의 없어'", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/boe-s-bailey-sees-little-evidence-of-second-round-inflation",
     "베일리 총재가 2차 인플레이션 증거가 거의 없다고 보면서, 11월 인상 베팅이 쌓인 시장에 물가 압력이 아직 번지지 않았다는 진단을 내놨다"),
  it("베일리 '2차 물가 압력, 지금까진 억제된 모습'", "로이터", "2026-10-16", "https://www.reuters.com/world/uk/bank-englands-bailey-says-second-round-inflation-pressures-look-subdued-so-far-2026-10-16/",
     "베일리 총재가 기업들이 가격 전가보다 비용 절감에 집중해 2차 물가 압력이 아직 억눌려 있지만 판단은 이르다고 말하면서, 인상 경로 판단을 유보했다")
 ]
})

# G1-026
items.append({
 "cid": "G1-026", "attachTo": "n-tg-0292",
 "title": "中 국가대표 자금, ETF 대량 유입으로 복귀 신호…매도 제한·자사주 매입도",
 "one": "중국 증시가 미국 물가 충격에 흔들린 가운데 국가대표 자금이 대규모 ETF 유입으로 복귀 신호를 보내고 당국이 매도 제한과 자사주 매입으로 증시 떠받치기에 나서면서, A주 하락 압력이 누그러질 수 있다" + T,
 "facts": [
  "무엇이: 중국 국가대표 자금이 대규모 ETF 유입으로 증시 복귀 신호를 보냈다 [제목]",
  "부양: 중국은 매도 제한과 자사주 매입으로 증시를 떠받치는 조치에 나섰다 [제목]",
  "거래: 10월 15일 주식형 ETF 전체 거래대금은 1,670억 위안을 넘어 전날 1,193억 위안보다 약 40% 늘었다 [채널]",
  "지수: 15일 CSI300은 1.59%, CSI500은 2.43% 내렸고, 미국 물가 지표가 예상보다 높게 나온 뒤 세계 증시 매도가 원인으로 꼽혔다 [사실]"
 ],
 "basis": "title",
 "check": "검색에서 10월 16일 매도 제한·자사주 매입 발표 내용과 ETF 유입 규모를 찾지 못함(FXStreet는 미국 금융 매체 제목만 전함)",
 "src": [],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "markets", "f": "수요", "dir": "up", "k": "실제", "t": "국가대표 자금 ETF 대량 유입으로 복귀 신호"},
  {"ind": "fin", "node": "markets", "f": "공급", "dir": "down", "k": "실제", "t": "당국의 매도 제한으로 주식 매도 물량 억제"}
 ],
 "added": "이번 블룸버그 2건으로 국가대표 자금의 대규모 ETF 유입 복귀 신호와 당국의 매도 제한·자사주 매입 부양책이 추가됐다" + T,
 "items": [
  it("중국 국가대표 자금, 대규모 ETF 유입으로 복귀 신호", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/china-s-national-team-signals-return-with-heavy-etf-inflows",
     "중국 국가대표 자금이 대규모 ETF 유입으로 증시 복귀 신호를 보내면서, 15일 급락 뒤 지수형 ETF에 지지 매수가 들어온 것으로 보인다" + T),
  it("중국, 매도 제한·자사주 매입으로 증시 떠받치기", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/china-moves-to-prop-up-stock-market-with-selling-curbs-buybacks",
     "중국 당국이 매도 제한과 자사주 매입으로 증시 부양에 나서면서, 주식 매도 물량을 줄여 주가 하락을 막으려 하고 있다" + T)
 ]
})

# G1-030
items.append({
 "cid": "G1-030", "attachTo": "n-tg-0228",
 "title": "SC '러 경유, 세계 공급 못 늘려'…중간유분 재고 바닥에 겨울 난방유 우려",
 "one": "스탠다드차타드가 트럼프의 러시아산 경유 거래는 다른 구매국 몫을 돌릴 뿐 세계 공급을 늘리지 못한다고 분석한 가운데 미국 중간유분 재고가 계절 평균보다 약 12% 적은 1억 510만 배럴까지 줄면서, 겨울 난방유·경유 가격이 오를 수 있다",
 "facts": [
  "무엇이: 스탠다드차타드는 러시아산 경유가 미국 등으로 돌려지면 기존 구매국이 그만큼 못 받게 돼 세계 순공급은 늘지 않고, 손상된 정유 설비와 러시아 국내 수요가 공급을 묶는다고 분석했다 [사실]",
  "재고: 미국 중간유분 재고는 10월 2일 기준 1억 510만 배럴로 계절 평균보다 약 12% 적었다 [사실]",
  "규모: 480만 톤 전량은 약 3,600만 배럴로 미국 수요 약 9.5일 치이며, 실제 인도 속도는 아직 확인되지 않았다 [사실]",
  "겨울: 채널은 정유 가동이 최대이고 가격도 높은데 중간유분 재고가 최저 수준에 가까워져, 한파나 정유 고장 때 난방유 가격이 폭등할 수 있다고 봤다 [채널]",
  "기존: 골드만삭스는 10~11월 풀릴 러시아 경유가 미 걸프만·유럽 도매 경유 가격을 배럴당 1~2달러 낮추는 데 그칠 것으로 봤다 [사실]"
 ],
 "basis": "verified",
 "check": "스탠다드차타드 분석과 미국 중간유분 재고 수치는 검색 결과 요약으로 확인",
 "src": [
  {"o": "OilPrice.com", "d": "2026-10-16", "u": "https://oilprice.com/Energy/Crude-Oil/Standard-Chartered-Trumps-Russian-Diesel-Wont-Add-New-Supply.html"},
  {"o": "EBC Financial", "d": "2026-10", "u": "https://www.ebc.com/forex/us-russia-diesel-deal-2026-fuel-prices"}
 ],
 "inds": ["oil"], "nodes": [],
 "vc": [
  {"ind": "oil", "node": "stocks", "f": "공급", "dir": "down", "k": "실제", "t": "미 중간유분 재고 계절 평균보다 12% 적어"},
  {"ind": "oil", "node": "products", "f": "가격", "dir": "up", "k": "예상", "t": "재고 부족에 겨울 난방유 가격 급등 우려"}
 ],
 "added": "이번 텔레그램 2건으로 스탠다드차타드의 러시아 경유 순공급 증가 없음 분석과 중간유분 재고 최저 수준 근접에 따른 겨울 난방유 가격 급등 우려가 추가됐다",
 "items": [
  it("중간유분 재고 최저 수준 근접…겨울 난방유 가격 폭등 우려", "텔레그램 트릴리온", "2026-10-16", "https://t.me/Trillion_labs/10612",
     "정유 가동이 최대이고 가격도 높은데 중간유분 재고가 최저 수준에 가까워지면서, 한파나 정유 고장 시 난방유 가격이 폭등할 수 있다는 경고가 나왔다"),
  it("SC '트럼프의 러시아 경유 거래, 세계 공급 못 늘린다'", "텔레그램 트릴리온", "2026-10-16", "https://t.me/Trillion_labs/10629",
     "스탠다드차타드가 정유 설비 피해와 수출 제한으로 러시아 공급이 묶여 서방행 경유는 다른 구매국의 부족만 낳는다고 분석하면서, 경유값 인하 효과가 제한될 전망이다")
 ]
})

# G1-034
items.append({
 "cid": "G1-034", "attachTo": "",
 "title": "호주 빅토리아 밀 풍작·커피 공급 과잉 예고…커피값 변동성은 여전",
 "one": "호주 빅토리아주 밀 풍작이 세계 밀 공급을 늘리고 2026/27년 커피도 브라질 주도 공급 과잉이 예상되지만, 거래소 커피 재고가 크게 줄어 늘어난 물량이 재고 보충에 먼저 쓰이면서 커피값 변동성은 쉽게 잦아들지 않을 전망이다",
 "facts": [
  "무엇이: 호주 빅토리아주의 밀 풍작이 세계 밀 공급을 늘릴 전망이다 [제목]",
  "호주 작황: 라보뱅크는 앞서 빅토리아를 포함한 동부 산지의 비에 힘입어 호주 밀 생산 전망을 2,130만 톤에서 최대 3,000만 톤으로 올렸다 [사실]",
  "커피 과잉: 라보뱅크는 2026/27년 세계 커피 생산을 1억 8,170만 포대로 소비 1억 7,280만 포대보다 많게 봤고, 미 농무부는 사상 최대 1억 8,970만 포대를 예상했다 [사실]",
  "가격·재고: 아라비카는 10월 첫 주 파운드당 3달러를 넘었다가 브라질의 9월 수출 급증에 급락했고, ICE 인증 재고가 크게 줄어 라보뱅크는 과잉 물량이 주로 재고 보충에 쓰일 것으로 봤다 [사실]"
 ],
 "basis": "partial",
 "check": "커피 공급 과잉 전망·가격 급변·재고 부족은 검색 결과 요약으로 확인, 빅토리아주 풍작 규모는 확인 못 함(호주 전체 전망은 약 두 달 전 자료)",
 "src": [
  {"o": "DatamarNews", "d": "2026-10", "u": "https://datamarnews.com/noticias/global-coffee-prices-seen-falling-in-2026-as-brazil-led-surplus-emerges/"},
  {"o": "World Coffee Index", "d": "2026-10-10", "u": "https://www.worldcoffeeindex.com/article/coffee-week-2026-10-10/"},
  {"o": "BigGo Finance", "d": "2026-08", "u": "https://finance.biggo.com/news/83a53d36-457f-43a7-8319-132804156ebf"}
 ],
 "inds": ["agri"], "nodes": [],
 "vc": [
  {"ind": "agri", "node": "grains", "f": "공급", "dir": "up", "k": "예상", "t": "호주 빅토리아주 밀 풍작으로 세계 공급 증가"},
  {"ind": "agri", "node": "softs", "f": "공급", "dir": "up", "k": "예상", "t": "2026/27년 브라질 주도 커피 공급 과잉 예상"}
 ],
 "added": "이번 블룸버그 커피 기사로 다가오는 커피 공급 과잉에도 재고 보충 수요 때문에 변동성 큰 커피값이 쉽게 진정되지 않을 수 있다는 분석이 추가됐다",
 "items": [
  it("호주 빅토리아주 밀 풍작, 세계 밀 공급 늘린다", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/wheat-boom-in-australia-s-victoria-state-to-boost-global-supply",
     "호주 빅토리아주 밀 농사가 풍작을 맞아 세계 밀 공급이 늘면서, 미국 밀 선물 등 국제 밀값에 하락 압력이 커질 수 있다"),
  it("다가오는 커피 공급 과잉, 출렁이는 가격 진정시키기엔 부족할 수도", "블룸버그", "2026-10-16", "https://www.bloomberg.com/news/articles/2026-10-16/coffee-s-coming-glut-may-not-be-enough-to-calm-volatile-prices",
     "2026/27년 커피 공급 과잉이 예상되지만 줄어든 거래소 재고 보충에 물량이 먼저 쓰이면서, 출렁이는 커피 가격이 쉽게 안정되지 않을 수 있다")
 ]
})

# G1-040
items.append({
 "cid": "G1-040", "attachTo": "n-tg-0166",
 "title": "후티, 사우디의 오만 회담 제안 거부…리야드 공항 이달 20차례 공격",
 "one": "사우디가 후티에 오만 무스카트 회담을 제안했지만 후티가 거부하고 10월에만 리야드 공항을 20차례 공격하면서, 이란의 확전 부추김 논란 속 사우디 석유시설과 걸프 항공에 대한 위협이 길어질 전망이다",
 "facts": [
  "무엇이: 사우디 외무부 라에드 크림리 공공외교 차관은 확전 초기 후티에 오만 무스카트 회담을 요청했지만 후티가 거부했고, 그것이 몇 주 전 마지막 접촉이었다고 말했다 [사실]",
  "이란: 크림리는 이란이 후티의 확전을 부추긴다고 비난하면서도 이란과의 직접 소통은 이어 가고 있다고 했다 [사실]",
  "공항: 사우디 주도 연합군은 후티가 10월에만 리야드 공항을 20차례 공격했다고 밝혔다 [사실]",
  "전장: 채널은 후티가 여러 전선에서 사우디 지원 연합군을 밀어내며 영토를 넓히고 있어 지금은 협상이 불리하다고 판단한 것으로 봤다 [채널]",
  "기존: 13일 공격 때 다란 아람코 본사 일부에 불이 났고, 후티는 사우디 공항·석유시설 공격을 이어 가겠다고 했다 [사실]"
 ],
 "basis": "verified",
 "check": "사우디의 오만 회담 제안과 후티 거부, 이란 비난, 리야드 공항 20차례 공격은 검색 결과 요약으로 확인",
 "src": [
  {"o": "Dawn", "d": "2026-10-15", "u": "https://www.dawn.com/news/2037374/saudi-arabia-says-houthis-declined-to-meet-in-oman-in-recent-weeks"},
  {"o": "Times of Israel", "d": "2026-10-15", "u": "https://www.timesofisrael.com/liveblog_entry/saudi-arabia-says-houthis-declined-to-meet-in-oman-struck-riyadh-airport-20-times/"},
  {"o": "PBS NewsHour", "d": "2026-10-15", "u": "https://www.pbs.org/newshour/world/saudi-diplomat-says-iran-is-encouraging-houthi-escalation-of-attacks-on-the-kingdom"}
 ],
 "inds": ["oil", "macro", "aero"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "oil", "node": "opec", "f": "공급", "dir": "down", "k": "예상", "t": "후티 협상 거부로 사우디 석유시설 공격 위협 지속"},
  {"ind": "aero", "node": "airports", "f": "공급", "dir": "down", "k": "실제", "t": "리야드 공항 10월에만 20차례 공격받아"}
 ],
 "added": "이번 텔레그램 1건으로 후티가 사우디의 오만 협상 제안을 거부하고 여러 전선에서 연합군을 밀어내며 세력을 넓히고 있다는 내용이 추가됐다",
 "items": [
  it("후티, 사우디의 오만 협상 제안 거부…전장 우위 판단", "텔레그램 트릴리온", "2026-10-16", "https://t.me/Trillion_labs/10620",
     "후티가 사우디의 오만 협상 제안을 거부하고 여러 전선에서 연합군을 밀어내면서, 전장 우위를 쥔 후티의 사우디 공격이 이어질 전망이다")
 ]
})

# G1-044
items.append({
 "cid": "G1-044", "attachTo": "n-rtr-0343",
 "title": "ACG, A320neo 75대 사상 최대 주문…캐세이 등 항공기 주문 행렬 이어져",
 "one": "항공기 리스사 ACG가 2032~2035년 인도분 A320neo 계열 75대를 창사 이래 최대 규모로 주문하고 캐세이퍼시픽이 광동체 최대 50대 추가 주문을 추진하면서, 에어버스의 수주 잔고가 늘고 증산 압력이 커지고 있다",
 "facts": [
  "무엇이: 에비에이션캐피털그룹(ACG)은 10월 16일 에어버스 A320neo 계열 75대를 주문했고, 토머스 베이커 CEO는 40년 가까운 회사 역사상 최대 주문이라고 했다 [사실]",
  "조건: 인도는 2032~2035년이며 A320neo 계열 안에서 다른 기종으로 바꿀 권리가 있고, 기종 구성과 금액은 공개하지 않았다 [사실]",
  "누적: ACG의 A320neo 계열 누적 주문은 190대로 늘었고, 6월 말 보유 기단에는 118대가 있었다 [사실]",
  "기존: 에어버스는 A350 증산 결정을 서두르겠다고 했고, 캐세이퍼시픽은 광동체 최대 50대 추가 주문을 추진한다 [사실]"
 ],
 "basis": "verified",
 "check": "ACG 주문 규모·인도 시기·누적 주문은 검색 결과 요약으로 확인(ACG 보도자료 포함)",
 "src": [
  {"o": "ACG 보도자료(PR Newswire)", "d": "2026-10-16", "u": "http://www.prnewswire.com/news-releases/aviation-capital-group-grows-portfolio-with-order-for-75-airbus-a320neo-family-aircraft-the-largest-order-in-acgs-history-302911033.html"},
  {"o": "FlightGlobal", "d": "2026-10-16", "u": "https://www.flightglobal.com/fleets/2026/10/aviation-capital-group-places-its-largest-order-for-airbus-jets/"}
 ],
 "inds": ["aero"], "nodes": [],
 "vc": [
  {"ind": "aero", "node": "oem", "f": "수요", "dir": "up", "k": "실제", "t": "ACG의 A320neo 계열 75대 사상 최대 주문"}
 ],
 "added": "이번 로이터 1건으로 ACG의 A320neo 계열 75대 주문이 2032~2035년 인도분이자 회사 사상 최대 규모로 추가됐다",
 "items": [
  it("ACG, 에어버스 A320neo 75대 주문…리스사 사상 최대 구매", "로이터", "2026-10-16", "https://www.reuters.com/business/aerospace-defense/acg-orders-75-airbus-a320neo-jets-lessors-biggest-purchase-yet-2026-10-16/",
     "ACG가 A320neo 계열 75대를 회사 사상 최대 규모로 주문하면서, 에어버스 협동체 수주 잔고가 2030년대 중반 인도분까지 늘어났다")
 ]
})

# G1-048
items.append({
 "cid": "G1-048", "attachTo": "n-rtr-0328",
 "title": "맨그룹 운용자산 2,709억 달러 사상 최대…블랙록 이어 운용사 자금 유입 확대",
 "one": "맨그룹이 변동성 장세 속 3분기 순유입 101억 달러에 힘입어 운용자산을 사상 최대 2,709억 달러로 늘리고 블랙록도 분기 2,050억 달러 순유입을 기록하면서, 대형 운용사의 수수료 기반 자산이 불어나고 있다",
 "facts": [
  "무엇이: 맨그룹의 9월 30일 운용자산은 2,709억 달러로 6월 말 2,536억 달러, 1년 전 2,139억 달러보다 늘어 사상 최대였다 [사실]",
  "동력: 3분기 순유입은 101억 달러였고 투자 성과가 약 59억 달러를 더했다(33억 달러로 전한 보도도 있음) [사실]",
  "구성: 유동 대체투자는 997억 달러, 롱온리 주식은 1,132억 달러로 늘었고 사모시장 자산은 174억 달러로 줄었다 [사실]",
  "기존: 블랙록의 3분기 말 운용자산은 약 15조 5,000억 달러, 분기 순유입은 2,050억 달러였다 [사실]"
 ],
 "basis": "verified",
 "check": "맨그룹 운용자산·순유입·부문별 자산은 검색 결과 요약으로 확인, 투자 성과 기여분은 보도마다 엇갈림",
 "src": [
  {"o": "ADVFN", "d": "2026-10-16", "u": "https://uk.advfn.com/market-news/article/24662/man-group-assets-under-management-rise-to-270-9-billion-following-10-1-billion-in-q3-net-inflows"},
  {"o": "The Market Reporter", "d": "2026-10-16", "u": "https://www.themarketreporter.co.uk/a/596e9b34/man-group-assets-climb-to-271bn-on-strong-flows-and-performance"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "assetmgmt", "f": "수요", "dir": "up", "k": "실제", "t": "맨그룹 3분기 순유입 101억 달러로 자산 사상 최대"}
 ],
 "added": "이번 로이터 1건으로 맨그룹의 운용자산 사상 최대 2,709억 달러와 3분기 순유입 101억 달러, 변동성 장세가 유입을 이끌었다는 점이 추가됐다",
 "items": [
  it("맨그룹 운용자산 사상 최대 2,709억 달러…변동성이 견인", "로이터", "2026-10-16", "https://www.reuters.com/business/man-groups-assets-under-management-hit-record-2709-billion-volatility-drives-2026-10-16/",
     "맨그룹이 변동성 장세 속 3분기 101억 달러 순유입으로 운용자산을 사상 최대 2,709억 달러로 늘리면서, 대체투자 운용 수요가 커졌다")
 ]
})

# G1-052
items.append({
 "cid": "G1-052", "attachTo": "",
 "title": "美 항소법원, 연 90억 달러 통신 보조금 기금 운영기관 설립 무효 판결",
 "one": "미 제5순회 항소법원이 FCC에 연 90억 달러 규모 보편적 서비스 기금의 운영기관(USAC)을 세울 권한이 없었다고 판결하면서, 통신 보조금 지원 체계가 흔들릴 수 있다",
 "facts": [
  "무엇이: 제5순회 항소법원 재판부(이디스 브라운 클레멘트 판사)는 FCC가 1997년 USAC를 만든 것이 의회의 구체적 승인 없이 이뤄져 정부기업통제법을 어겼다고 판결했다 [사실]",
  "규모: 기금은 해마다 약 90억 달러를 거두며, 판결은 기금 자체보다 운영기관 설립을 겨냥했다 [사실]",
  "시점: FCC는 판결이 최소 두 달간 효력을 내지 않으며 모든 대응 방안을 검토 중이라고 밝혔다 [사실]",
  "배경: 대법원은 2025년 6월 보편적 서비스 기금 조달 방식이 위헌이 아니라고 판결해 제5순회 전원합의체 결정을 뒤집은 바 있다 [사실]"
 ],
 "basis": "verified",
 "check": "판결 요지와 FCC 반응은 검색 결과 요약으로 확인(보도 대부분이 로이터 전재), 2025년 대법원 판결은 로펌 자료로 확인",
 "src": [
  {"o": "Mezha", "d": "2026-10-16", "u": "https://mezha.net/eng/news/mezha-b6fc943f93e352e47b3b852b_us_appeals_court"},
  {"o": "Wiley", "d": "2025-06", "u": "https://www.wiley.law/alert-Supreme-Court-Declares-Universal-Service-Fund-Constitutional-Reversing-Fifth-Circuit-Opinion"}
 ],
 "inds": ["tech"], "nodes": [],
 "vc": [
  {"ind": "tech", "node": "telecom", "f": "수요", "dir": "down", "k": "예상", "t": "연 90억 달러 통신 보조금 기금 운영 차질 우려"}
 ],
 "items": [
  it("美 항소법원, 연방 90억 달러 통신 보조금 기금 무효화", "로이터", "2026-10-16", "https://www.reuters.com/legal/government/us-appeals-court-invalidates-federal-9-billion-telecom-subsidy-fund-2026-10-16/")
 ]
})

d = {"agent": "W3", "searches_used": 16, "fetches_used": 0, "items": items, "skipped": []}
json.dump(d, open(OUT, 'w'), ensure_ascii=False, indent=1)

# checks
strip = lambda x: re.sub(r' \((제목 기준|채널 전언)\)$', '', x)
for x in items:
    one = strip(x['one'])
    multi = len(x['items']) > 1 or x['attachTo']
    lo, hi = (90, 160) if multi else (80, 130)
    flag = [] if lo <= len(one) <= hi else ['ONE %d' % len(one)]
    if not (20 <= len(x['title']) <= 50): flag.append('TITLE %d' % len(x['title']))
    if multi:
        a = strip(x.get('added', ''))
        if not (60 <= len(a) <= 140): flag.append('ADDED %d' % len(a))
    for i in x['items']:
        if not (25 <= len(i['t']) <= 60): flag.append('T %d %s' % (len(i['t']), i['t']))
        if multi:
            s = strip(i.get('s', ''))
            if not (45 <= len(s) <= 110): flag.append('S %d %s' % (len(s), s[:20]))
    for v in x['vc']:
        if not (12 <= len(v['t']) <= 45): flag.append('VC %d' % len(v['t']))
    if not (2 <= len(x['facts']) <= 5): flag.append('FACTS')
    for f in x['facts']:
        if '|' in f or '**' in f or '{{' in f: flag.append('BADCHAR')
    print(x['cid'], len(one), flag)
