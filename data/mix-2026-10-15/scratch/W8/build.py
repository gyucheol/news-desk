import json, re

OUT = "/home/user/news-desk/data/mix-2026-10-15/out2/W8.json"
TG_INS = "텔레그램 미국 주식 인사이더"
TG_HANA = "텔레그램 하나증권 중국전략"

items = []

# G2-012
items.append({
 "cid": "G2-012", "attachTo": "n-bbg-0230",
 "title": "러, 트럼프 거래 뒤 경유 수출 재개…美는 러 동결자산 최대 1000억 달러 해제 검토",
 "one": "트럼프와의 거래로 러시아가 프리모르스크항에서 경유 수출을 재개하고 미국이 최대 1000억 달러 러시아 동결자산 해제까지 검토한다는 보도가 나오면서, 공화당·유럽의 반발이 커지는 가운데 경유 도매가 하락 효과는 배럴당 1~2달러에 그칠 전망이다",
 "facts": [
  "무엇이: 크렘린은 10월 15일 트럼프와의 거래에 따라 러시아산 경유가 세계 시장에 나가기 시작했다고 밝혔고, 러시아는 10월 10일부터 경유 수출 금지를 일부 풀었다 [사실]",
  "선적: 발트해 프리모르스크항에서 경유 선적이 재개됐고 약 4만 톤을 실은 유조선 한 척이 모로코로 향했다 [사실]",
  "물량: 트럼프는 즉시 30만 톤 이상, 11월 50만 톤을 공급받기로 했다고 밝혔고, 노박 부총리는 연말까지 월 경유 수출을 350만 톤으로 되돌리겠다고 했다 [사실]",
  "효과: 골드만삭스는 초기 물량이 미 걸프만·유럽 경유 도매가를 배럴당 1~2달러 낮추는 데 그칠 것으로 추정했다 [사실]",
  "동결자산: FT 보도로는 위트코프·쿠슈너 특사가 에너지 시설 제한 휴전의 유인으로 최대 1000억 달러 러시아 동결자산 해제를 검토 중이고, EU 관계자들은 이를 거부했다 [채널]"
 ],
 "basis": "partial",
 "check": "경유 수출 재개·선적·물량·골드만 추정은 검색 결과 요약(모스크바타임스·CNBC)으로 확인. FT발 동결자산 해제 검토, 멜로니 총리·크렘린 특사 발언, 우크라이나 정보공유 중단 위협은 확인 못 함",
 "src": [
  {"o": "The Moscow Times", "d": "2026-10-15", "u": "https://www.themoscowtimes.com/2026/10/15/kremlin-says-russia-restarts-diesel-exports-after-deal-with-trump-a93977"},
  {"o": "CNBC", "d": "2026-10-13", "u": "https://www.cnbc.com/2026/10/13/trump-putin-zelenskyy-russia-ukraine-diesel-oil-price.html"}
 ],
 "inds": ["oil", "macro"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "oil", "node": "products", "f": "공급", "dir": "up", "k": "실제", "t": "러시아, 트럼프 거래 뒤 경유 수출 재개"},
  {"ind": "oil", "node": "price", "f": "가격", "dir": "down", "k": "예상", "t": "골드만, 경유 도매가 배럴당 1~2달러 하락 효과 추정"}
 ],
 "added": "이번 로이터 4건·텔레그램 5건으로 크렘린의 경유 수출 재개 확인, 미국의 최대 1000억 달러 러시아 동결자산 해제 검토, 멜로니 이탈리아 총리의 '매우 위험한 선택' 비판이 추가됐다",
 "items": [
  {"t": "멜로니 伊 총리 \"미·러 경유 거래는 매우 위험한 선택\"", "o": "로이터", "d": "2026-10-14", "u": "https://www.reuters.com/business/us-russia-deal-diesel-is-very-risky-choice-italy-pm-meloni-says-2026-10-14/",
   "s": "멜로니 이탈리아 총리가 미·러 경유 거래를 매우 위험한 선택이라고 비판하면서, 유럽 동맹의 반대 목소리가 하나 더 늘었다 (제목 기준)"},
  {"t": "크렘린 특사 \"경유 거래가 미·러 추가 협력의 길 열어\"", "o": "로이터", "d": "2026-10-14", "u": "https://www.reuters.com/business/diesel-deal-opens-way-more-russia-us-cooperation-kremlin-envoy-says-2026-10-14/",
   "s": "크렘린 특사가 경유 거래가 미·러 간 더 많은 협력의 길을 열었다고 말하면서, 러시아가 이 거래를 관계 개선의 발판으로 삼으려 하고 있다 (제목 기준)"},
  {"t": "트럼프 \"러, 경유 즉시 30만 톤·11월 50만 톤 공급 합의\"", "o": "텔레그램 Polaristimes", "d": "2026-10-15", "u": "https://t.me/The_MariTimes/63723",
   "s": "트럼프가 러시아가 즉시 30만 톤 이상, 11월 50만 톤, 이어 100만 톤의 경유를 공급하기로 했다고 밝히면서, 연료값 부담을 덜려는 조치로 풀이됐다"},
  {"t": "FT \"美, 러 동결자산 최대 1000억 달러 해제 검토\"…EU는 거부", "o": "텔레그램 트릴리온", "d": "2026-10-15", "u": "https://t.me/Trillion_labs/10520",
   "s": "미국 특사들이 에너지 시설 제한 휴전의 유인으로 최대 1000억 달러 러시아 동결자산 해제를 검토하면서, EU 관계자들이 단호히 반대하고 나섰다"},
  {"t": "美, 유럽 내 러 동결자산 일부를 미국 관리 특수기구로 이전 제안", "o": "텔레그램 Polaristimes", "d": "2026-10-15", "u": "https://t.me/The_MariTimes/63726",
   "s": "미국이 유럽이 가진 러시아 동결자산 일부를 풀어 미국이 관리하는 특수 금융기구로 옮기자고 제안하면서, 유럽의 자산 몰수 추진과 부딪치고 있다"},
  {"t": "FT \"美, 우크라 평화협상 재개 위해 러 자산 일부 해제 거론\"", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/world/europe/us-floats-unfreezing-some-russian-assets-restart-ukraine-peace-talks-ft-reports-2026-10-14/",
   "s": "미국이 우크라이나 평화협상을 다시 열기 위해 러시아 동결자산 일부 해제를 거론하면서, 제재 완화 범위가 경유에서 자산으로 넓어질 수 있다 (제목 기준)"},
  {"t": "크렘린 \"트럼프와 거래 뒤 러시아 경유 수출 재개\"", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/business/energy/kremlin-says-russia-restarts-diesel-exports-after-deal-with-trump-2026-10-15/",
   "s": "크렘린이 트럼프와의 거래 뒤 러시아산 경유 수출이 재개됐다고 확인하면서, 프리모르스크항에서 선적이 다시 시작돼 세계 경유 공급이 늘기 시작했다"},
  {"t": "크렘린, 러시아산 디젤 세계 시장 진출 개시 확인", "o": "텔레그램 트릴리온", "d": "2026-10-15", "u": "https://t.me/Trillion_labs/10606",
   "s": "크렘린이 러시아산 디젤의 세계 시장 진출 개시를 확인했지만, 채널은 러시아에 내보낼 물량 자체가 부족하다고 꼬집으며 실제 공급 여력에 의문을 제기했다"},
  {"t": "러시아 디젤 순수출 줄고 휘발유는 수입 중…공급 여력 의문", "o": "텔레그램 트릴리온", "d": "2026-10-15", "u": "https://t.me/Trillion_labs/10608",
   "s": "러시아의 디젤 순유출량이 줄고 휘발유는 수입하는 상황이라는 자료가 나오면서, 러시아가 약속한 경유 수출 물량을 실제로 댈 수 있을지 의문이 커졌다"}
 ]
})

# G2-028
items.append({
 "cid": "G2-028", "attachTo": "n-tg-0226",
 "title": "北, 잠수함발사 전략순항미사일 2종 시험…탄도미사일 이틀 만에 또 발사",
 "one": "북한이 트럼프 대통령의 회동 거론 직후인 10월 14일 동해에서 잠수함발사 전략순항미사일 2종을 시험 발사해 12일 전술탄도미사일 발사에 이어 핵 억제력 과시를 이어가면서, 한반도 지정학 위험이 다시 부각되고 있다",
 "facts": [
  "무엇이: 조선중앙통신은 10월 15일 북한이 14일 잠수함에서 쏘는 전략순항미사일 2종을 시험 발사했다고 밝혔다 [사실]",
  "방식: 한국군은 한 종류는 수직발사관에서, 다른 하나는 어뢰발사관에서 발사됐다고 밝혔다 [사실]",
  "목적: 북한은 수중 전투체계의 준비태세 점검과 해군의 전략 임무 수행 능력 강화를 목적으로 들고 주변국 안보에는 영향이 없다고 했다 [사실]",
  "연속 발사: 이번 시험은 12일 평양 일대에서 동해상으로 전술탄도미사일을 쏜 지 이틀 만이다 [사실]",
  "외교: 블룸버그는 트럼프 대통령이 회동을 거론한 뒤 김정은이 시험을 했다고 전했다 [제목]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약(알자지라·NK뉴스·프랑스24)으로 2종 시험 발사와 발사 방식 확인",
 "src": [
  {"o": "Al Jazeera", "d": "2026-10-15", "u": "https://www.aljazeera.com/news/2026/10/15/north-korea-tests-two-submarine-launched-missiles-state-media-reports"},
  {"o": "NK News", "d": "2026-10-15", "u": "https://www.nknews.org/2026/10/north-korea-says-it-tested-submarine-launched-cruise-missiles/"},
  {"o": "France 24", "d": "2026-10-14", "u": "https://www.france24.com/en/asia-pacific/20261014-north-korea-test-fires-submarine-launched-cruise-missiles"}
 ],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "macro", "node": "geo", "f": "-", "dir": "flat", "k": "실제", "t": "북한 잠수함발사 순항미사일 시험, 수급 영향은 직접 없음"}
 ],
 "added": "이번 블룸버그·로이터·텔레그램 3건으로 북한이 10월 14일 잠수함발사 전략순항미사일 2종을 시험 발사했다는 사실이 추가됐다",
 "items": [
  {"t": "김정은, 트럼프 회동 거론 뒤 잠수함발사 미사일 시험", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/articles/2026-10-15/kim-tests-submarine-launched-missiles-after-trump-floats-meeting",
   "s": "김정은이 트럼프의 회동 거론 직후 잠수함발사 미사일을 시험하면서, 외교 신호 속에서도 군사 도발을 이어 가고 있다 (제목 기준)"},
  {"t": "北 \"잠수함발사 순항미사일 시험\"…조선중앙통신 보도", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/world/asia-pacific/north-korea-says-it-tested-submarine-launched-cruise-missiles-kcna-says-2026-10-14/",
   "s": "북한이 조선중앙통신을 통해 잠수함발사 순항미사일 시험을 발표하면서, 전술탄도미사일에 이어 해상 발사 능력까지 과시했다"},
  {"t": "AP \"北 잠수함용 전략순항미사일 2종 시험, 핵탑재 염두\"", "o": TG_INS, "d": "2026-10-15", "u": "https://t.me/insidertracking/66348",
   "s": "북한이 핵탄두 탑재를 염두에 둔 전략순항미사일 2종을 잠수함 발사용으로 시험하면서, 사전 탐지가 어려운 수중 발사 위협이 커졌다고 AP가 전했다"}
 ]
})

# G2-038
items.append({
 "cid": "G2-038", "attachTo": "",
 "title": "카니 총리, 10월 19일 앨버타 분리 투표 앞두고 현지서 잔류 호소",
 "one": "카니 캐나다 총리가 10월 19일 앨버타 분리 주민투표를 며칠 앞두고 캘거리·에드먼턴 집회에 나서 잔류를 호소하면서, 분리 지지율이 22% 안팎인 가운데 산유 주의 이탈 논란이 투표 결과에 쏠리고 있다",
 "facts": [
  "무엇이: 카니 총리는 10월 19일 앨버타 주민투표를 앞두고 캘거리(목요일)·에드먼턴(금요일)에서 열리는 잔류 집회에 참석한다 [사실]",
  "투표 성격: 이번 투표는 독립을 바로 정하지 않고, 두 번째 구속력 있는 분리 투표를 위한 헌법 절차를 밟을지를 묻는다 [사실]",
  "여론: 스미스 앨버타 주총리는 최근 여론조사에서 분리 지지가 약 22%라고 밝혔다 [사실]",
  "카니 발언: 카니는 이민·헌법 개정을 다룬 9개 문항에도 반대표를 던지라고 촉구했다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약(CBC·ABC 뉴스)으로 일정과 투표 성격 확인",
 "src": [
  {"o": "CBC", "d": "2026-10-14", "u": "https://www.cbc.ca/news/canada/edmonton/carney-alberta-rallies-canadian-unity-9.7379637"},
  {"o": "CBC", "d": "2026-10-15", "u": "https://www.cbc.ca/news/canada/calgary/mark-carney-no-to-the-nine-alberta-referendum-9.7382226"}
 ],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "vc": [
  {"ind": "macro", "node": "geo", "f": "-", "dir": "flat", "k": "예상", "t": "앨버타 분리 투표 앞둬, 수급 영향은 아직 판단 어려움"}
 ],
 "items": [
  {"t": "카니 총리, 캐나다 분리 투표 며칠 앞두고 앨버타行", "o": "블룸버그", "d": "2026-10-14", "u": "https://www.bloomberg.com/news/articles/2026-10-13/carney-heads-to-alberta-days-before-canada-separation-vote"}
 ]
})

# G3-002
items.append({
 "cid": "G3-002", "attachTo": "n-rtr-0043",
 "title": "美 대형은행 3분기 희비…모건스탠리 예상 상회, BofA는 벌금에 이익 17%↓",
 "one": "미 대형은행 3분기 실적에서 주식 트레이딩 급증이 채권 부진을 메우며 골드만삭스·모건스탠리가 예상을 넘은 반면 뱅크오브아메리카는 12억 달러 자금세탁 방지 위반 벌금에 순이익이 17% 줄어, 은행별 희비 속에 월가는 딜 파이프라인이 견고하다고 봤다",
 "facts": [
  "무엇이: 뱅크오브아메리카의 3분기 순이익은 69억 3,000만 달러(주당 0.91달러)로 17% 줄었고, 12억 달러 자금세탁 방지 위반 벌금을 빼면 주당 1.08달러였다 [사실]",
  "벌금: 규제당국은 BofA가 수년간 50억 달러 넘는 의심 거래를 보고하지 않았다고 밝혔고, 벌금은 세금 공제가 되지 않으며 주가는 하루 약 5% 내렸다 [사실]",
  "모건스탠리: 3분기 매출 203억 4,000만 달러, 주당순이익 3.03달러로 예상을 넘었고 CET1 비율은 14.9%였다 [채널]",
  "BofA 이자이익: 순이자이익은 166억 달러로 8% 늘었고, 경영진은 2027년에도 8% 이상 성장을 예상했다 [채널]",
  "딜 전망: 솔로몬 골드만삭스 CEO는 일부 상장 철회에도 IPO 시장이 양호하고 투자은행 백로그가 매우 견고하다고 말했다 [채널]"
 ],
 "basis": "verified",
 "check": "BofA 벌금·순이익·주가는 검색 결과 요약(CNN·CNBC·SEC 8-K)으로 확인, 모건스탠리 매출 203억 4,000만 달러는 단일 매체 요약으로만 확인, BofA 컨퍼런스콜 수치와 솔로몬 발언은 채널 전언",
 "src": [
  {"o": "CNBC", "d": "2026-10-14", "u": "https://www.cnbc.com/2026/10/14/bank-of-america-bac-q3-2026-earnings.html"},
  {"o": "CNN", "d": "2026-10-13", "u": "https://www.cnn.com/2026/10/13/investing/bank-of-america-billion-dollar-fine"},
  {"o": "SEC 8-K", "d": "2026-10-14", "u": "https://www.sec.gov/Archives/edgar/data/0000070858/000007085826000481/bac09302026ex991.htm"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "ib", "f": "수요", "dir": "mixed", "k": "실제", "t": "주식 트레이딩 급증, 채권 트레이딩은 부진"},
  {"ind": "fin", "node": "banks", "f": "가격", "dir": "down", "k": "실제", "t": "BofA, 12억 달러 벌금에 순이익 17% 감소"}
 ],
 "added": "이번 텔레그램 6건·로이터 5건·블룸버그 2건으로 BofA의 12억 달러 벌금과 순이익 17% 감소, 모건스탠리의 예상 상회 실적, 월가의 견고한 딜 파이프라인 평가가 추가됐다",
 "items": [
  {"t": "JP모건 3분기 순이익 153억 달러…주식 트레이딩 49% 급증", "o": TG_INS, "d": "2026-10-14", "u": "https://t.me/insidertracking/66173",
   "s": "JP모건이 매출 509억 달러, 순이익 153억 달러를 냈지만 영업비용이 12% 늘고 CET1 비율이 13.9%로 내려가면서, 비용·자본 부담도 함께 드러났다"},
  {"t": "골드만삭스 3분기 EPS 17.01달러…M&A 자문 수익 사상 최대", "o": TG_INS, "d": "2026-10-14", "u": "https://t.me/insidertracking/66174",
   "s": "골드만삭스가 M&A 자문 수익 17억 달러로 분기 최대를 쓰고 주식 매출이 72% 늘면서, 역대 두 번째 분기 순매출 187억 달러를 기록했다"},
  {"t": "뱅크오브아메리카 3분기 조정 매출·EPS 예상 하회", "o": TG_INS, "d": "2026-10-14", "u": "https://t.me/insidertracking/66225",
   "s": "뱅크오브아메리카의 조정 매출 301억 2,000만 달러와 조정 EPS 1.08달러가 예상을 밑돌고 순이익이 17% 줄면서, 대형은행 가운데 부진한 성적을 냈다"},
  {"t": "모건스탠리 3분기 매출 203억 달러·EPS 3.03달러로 예상 상회", "o": TG_INS, "d": "2026-10-14", "u": "https://t.me/insidertracking/66232",
   "s": "모건스탠리가 매출 203억 4,000만 달러, EPS 3.03달러로 예상을 넘고 자사주 15억 4,000만 달러를 사들이면서, 주주환원을 이어 갔다"},
  {"t": "솔로몬 골드만 CEO \"IPO 시장 양호, 투자은행 백로그 견고\"", "o": "텔레그램 TNBfolio", "d": "2026-10-15", "u": "https://t.me/TNBfolio/71548",
   "s": "솔로몬 골드만삭스 CEO가 IPO 시장과 딜 백로그가 견고하다면서도 데이터센터 자금 조달 위험은 선별적으로 떠안겠다고 밝혀, 인수 위험 관리에 신중함을 보였다"},
  {"t": "모건스탠리, 주식 트레이딩 호조에 힘입어 3분기 이익 증가", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/business/finance/morgan-stanley-profit-rises-equity-trading-strength-2026-10-14/",
   "s": "모건스탠리가 주식 트레이딩 호조에 힘입어 이익을 늘리면서, 대형은행 실적에서 주식 부문 강세가 다시 확인됐다 (제목 기준)"},
  {"t": "JP모건·골드만 실적에 드러난 연준 금리 상승의 영향", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/newsletters/2026-10-14/jpmorgan-goldman-sachs-bank-earnings-show-effects-of-higher-fed-rates",
   "s": "JP모건·골드만삭스 실적에 연준 금리 상승의 효과가 드러나면서, 금리 환경이 은행 수익 구조를 바꾸고 있다는 분석이 나왔다 (제목 기준)"},
  {"t": "뱅크오브아메리카, 12억 달러 자금세탁 방지 벌금에 이익 타격", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/business/finance/bank-america-profit-hurt-by-12-billion-fine-over-anti-money-laundering-2026-10-14/",
   "s": "뱅크오브아메리카가 의심 거래 미보고에 따른 12억 달러 벌금을 반영하면서, 3분기 순이익이 69억 3,000만 달러로 17% 줄었다"},
  {"t": "골드만삭스, 3분기 주식 발행 주선 수익에서 경쟁사 앞서", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/articles/2026-10-14/goldman-sachs-leads-rivals-in-third-quarter-share-sale-revenue",
   "s": "골드만삭스가 3분기 주식 발행 주선 수익에서 경쟁사를 앞서면서, 주식 자본시장 회복의 몫을 가장 많이 가져갔다 (제목 기준)"},
  {"t": "월가 은행들 \"시장 변동성에도 딜 파이프라인 견고\"", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/legal/transactional/wall-street-banks-see-robust-deal-pipeline-despite-market-volatility-2026-10-14/",
   "s": "월가 은행들이 시장 변동성에도 딜 파이프라인이 견고하다고 밝히면서, 4분기 투자은행 수수료가 이어질 수 있다는 기대를 내비쳤다 (제목 기준)"},
  {"t": "BofA 어닝콜 \"2026년 순이자이익 8% 성장, 2027년도 8% 이상\"", "o": TG_INS, "d": "2026-10-15", "u": "https://t.me/insidertracking/66276",
   "s": "뱅크오브아메리카가 순이자이익 166억 달러로 8% 늘고 2027년에도 8% 이상 성장을 예상했지만, CET1 비율은 10.9%로 내려가 자본 여력이 줄었다"},
  {"t": "금리 변동성에 美 은행들 채권 트레이딩 실적 약세", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/business/finance/bond-trading-weakens-us-banks-interest-rate-volatility-affects-investors-2026-10-14/",
   "s": "금리 변동성이 투자자에 영향을 주면서 미 은행들의 채권 트레이딩이 약해져, 주식 부문과 대비되는 부진을 보였다 (제목 기준)"},
  {"t": "상반기 호조 뒤 자본시장 소강에 빠진 월가 은행들", "o": "로이터", "d": "2026-10-16", "u": "https://www.reuters.com/business/finance/wall-st-banks-caught-capital-markets-lull-after-strong-first-half-2026-2026-10-15/",
   "s": "2026년 상반기 강세 뒤 자본시장이 소강 국면에 들어서면서, 월가 은행들의 인수·발행 관련 수익 흐름이 둔해지고 있다 (제목 기준)"}
 ]
})

# G3-003
items.append({
 "cid": "G3-003", "attachTo": "n-rtr-0217",
 "title": "인도 금융사 9월 분기 이익 대체로 증가…지오파이낸셜만 감소, 은행 예금은 사상 최대",
 "one": "인도 증권사 그로우·엔젤원이 고객 증가로, HDFC생명·ICICI롬바드가 보험료 수입과 세제 혜택으로 분기 이익을 늘리고 9월 은행 예금도 달러 예금 덕에 사상 최대를 기록하면서, RBL은행에 이어 인도 금융사 실적이 대체로 개선됐지만 지오파이낸셜은 이익이 줄었다",
 "facts": [
  "무엇이: 엔젤원의 9월 분기 순이익은 334.9크로르 루피로 늘었고 매출은 약 17.8% 증가한 1,426.9크로르 루피였다 [사실]",
  "지오파이낸셜: 분기 매출은 약 1,699크로르 루피로 1년 전 1,002크로르보다 늘었지만 로이터는 분기 이익 감소를 전했다 [사실]",
  "보험: HDFC생명은 보험료 수입 증가로, ICICI롬바드는 세제 혜택에 힘입은 자동차·건강보험 호조로 분기 이익이 늘었다 [제목]",
  "증권·여신: 그로우는 고객 증가 속에 이익이 늘었고, HDB파이낸셜은 대출 수요 둔화에도 분기 이익이 늘었다 [제목]",
  "예금: 인도 은행 예금이 9월 달러 예금 증가에 힘입어 사상 최대인 3조 규모를 기록했다 [제목]"
 ],
 "basis": "partial",
 "check": "엔젤원 이익·매출과 지오파이낸셜 매출은 검색 결과 요약으로 확인. 그로우·HDB·ICICI롬바드·HDFC생명 실적과 9월 예금 기록(3조의 단위 포함)은 확인 못 함",
 "src": [
  {"o": "NewsBytes", "d": "2026-10-15", "u": "https://www.newsbytesapp.com/news/business/angel-one-posts-strong-september-quarter-rs3349cr-profit-interim-dividend/tldr"},
  {"o": "Upstox", "d": "2026-10-15", "u": "https://upstox.com/news/market-news/earnings/q2-results-live-updates-wipro-nestle-india-tech-mahindra-polycab-jio-financial-hdfc-life-irfc-hdfc-amc-angel-one-others-to-declare-earnings-oct015/liveblog-201887/"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "banks", "f": "공급", "dir": "up", "k": "실제", "t": "인도 9월 은행 예금 사상 최대, 달러 예금이 견인"},
  {"ind": "fin", "node": "markets", "f": "수요", "dir": "up", "k": "실제", "t": "그로우·엔젤원 고객 증가에 분기 이익 늘어"}
 ],
 "added": "이번 로이터 7건으로 그로우·엔젤원·HDFC생명·ICICI롬바드·HDB파이낸셜의 이익 증가, 지오파이낸셜의 이익 감소, 9월 은행 예금 사상 최대 기록이 추가됐다",
 "items": [
  {"t": "인도 증권사 그로우, 고객 증가 속 이익 증가", "o": "로이터", "d": "2026-10-14", "u": "https://www.reuters.com/world/india/indian-brokerage-groww-posts-higher-profit-customer-rises-2026-10-14/",
   "s": "인도 온라인 증권사 그로우가 고객 수 증가에 힘입어 이익을 늘리면서, 개인 투자자의 주식 거래 수요가 이어지고 있다 (제목 기준)"},
  {"t": "인도 HDB파이낸셜, 대출 수요 둔화에도 분기 이익 증가", "o": "로이터", "d": "2026-10-14", "u": "https://www.reuters.com/world/india/indias-hdb-financial-services-posts-quarterly-profit-rise-loan-demand-lower-2026-10-14/",
   "s": "HDFC은행 계열 여신사 HDB파이낸셜이 대출 수요가 줄었는데도 분기 이익을 늘리면서, 성장보다 수익성 관리가 실적을 받쳤다 (제목 기준)"},
  {"t": "인도 ICICI롬바드, 세제 혜택에 자동차·건강보험 호조로 이익 증가", "o": "로이터", "d": "2026-10-14", "u": "https://www.reuters.com/legal/litigation/indias-icici-lombard-posts-higher-profit-tax-breaks-lift-motor-health-insurance-2026-10-14/",
   "s": "손해보험사 ICICI롬바드가 세제 혜택으로 자동차·건강보험 판매가 늘면서 이익을 키워, 감세가 보험 수요를 끌어올리고 있다 (제목 기준)"},
  {"t": "인도 은행 예금, 달러 예금 힘입어 9월 사상 최대 3조 기록", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/world/india/indian-bank-deposits-hit-record-3-trillion-september-boosted-by-dollar-deposits-2026-10-15/",
   "s": "인도 은행 예금이 달러 예금 증가에 힘입어 9월 3조 규모로 사상 최대를 기록하면서, 은행의 대출 재원이 넉넉해졌다 (제목 기준)"},
  {"t": "인도 증권사 엔젤원, 고객 수 증가에 분기 이익 증가", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/world/india/indian-brokerage-angel-one-posts-higher-quarterly-profit-customer-numbers-climb-2026-10-15/",
   "s": "엔젤원이 고객 수 증가로 9월 분기 순이익을 334.9크로르 루피로 늘리고 매출도 약 17.8% 키우면서, 증권 중개 수요 회복을 보여 줬다"},
  {"t": "인도 HDFC생명, 보험료 수입 늘어 분기 이익 증가", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/world/india/indias-hdfc-life-posts-quarterly-profit-rise-higher-premium-income-2026-10-15/",
   "s": "생명보험사 HDFC생명이 보험료 수입 증가에 힘입어 분기 이익을 늘리면서, 인도 생명보험 수요가 이어지고 있다 (제목 기준)"},
  {"t": "릴라이언스 계열 인도 지오파이낸셜, 9월 분기 이익 감소", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/world/india/indias-jio-financial-posts-drop-quarterly-profit-2026-10-15/",
   "s": "릴라이언스 계열 지오파이낸셜이 매출은 약 1,699크로르 루피로 늘었지만 분기 이익이 줄면서, 인도 금융사 가운데 드물게 부진했다"}
 ]
})

# G3-009
items.append({
 "cid": "G3-009", "attachTo": "",
 "title": "리플, 90억 달러 실물자산 무기한 선물 붐 월가에 개방…하이퍼리퀴드는 美 규제 요구",
 "one": "리플 프라임이 하이퍼리퀴드에 상장된 100여 개 실물자산 무기한 선물을 참조하는 스와프를 기관 고객에 열고 하이퍼리퀴드 창업자 제프 얀이 블록체인이 아닌 시장 운영자를 규제해 달라고 요구하면서, 비트코인 너머로 번진 암호화폐 레버리지 거래가 월가로 들어오고 있다",
 "facts": [
  "무엇이: 리플의 프라임 브로커리지 리플 프라임이 Trade.xyz가 하이퍼리퀴드에 만든 무기한 선물을 참조하는 실물자산(RWA) 무기한 스와프를 기관 고객에 출시했고, 버투가 첫 거래 고객에 포함됐다 [사실]",
  "규모: 실물자산 무기한 선물의 미결제약정은 약 90억 달러에 이르렀다 [사실]",
  "구조: 고객이 기초 주식·원자재를 사지 않는 장외 상품으로, 리플 프라임이 거래 당사자가 되고 고객은 RLUSD를 담보로 낼 수 있다 [사실]",
  "규제: 제프 얀은 미국 규제당국이 네트워크가 아니라 그 위에 시장을 만드는 업체를 감독해야 한다고 했고, 하이퍼리퀴드 자체 무기한 선물 시장은 미국 고객에게 닫혀 있다 [사실]",
  "바이낸스US: 사업 확장을 위해 1억 달러 조달을 추진한다 [제목]"
 ],
 "basis": "verified",
 "check": "리플 프라임 출시·90억 달러·얀 발언은 검색 결과 요약(더블록·파이낸스피즈·코인데스크)으로 확인, 바이낸스US 1억 달러 조달과 레버리지 확산 기사 내용은 제목 기준",
 "src": [
  {"o": "The Block", "d": "2026-10-15", "u": "https://www.theblock.co/news/business/2026-10-15-ripple-prime-rwa-swaps-perpetual-futures-hyperliquid-418681"},
  {"o": "FinanceFeeds", "d": "2026-10-15", "u": "https://financefeeds.com/ripple-prime-adds-rwa-perpetual-swaps-across-more-than-100-markets/"},
  {"o": "CoinDesk", "d": "2026-10-15", "u": "https://www.coindesk.com/policy/2026/10/15/hyperliquid-founder-wants-u-s-oversight-of-trading-platforms-not-his-blockchain"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "payments", "f": "수요", "dir": "up", "k": "실제", "t": "실물자산 무기한 선물 미결제약정 약 90억 달러로 확대"}
 ],
 "added": "이번 블룸버그 1건으로 바이낸스US가 미국 내 암호화폐 사업 확장을 위해 1억 달러 조달에 나선다는 소식이 추가됐다 (제목 기준)",
 "items": [
  {"t": "암호화폐 레버리지 기계, 비트코인 베팅 너머에서 새 활로", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/articles/2026-10-14/crypto-s-leverage-machine-finds-new-life-beyond-bitcoin-bets",
   "s": "암호화폐 레버리지 거래가 비트코인 베팅을 넘어 다른 자산으로 번지면서, 무기한 선물 같은 파생상품 시장이 다시 커지고 있다 (제목 기준)"},
  {"t": "하이퍼리퀴드 창업자 얀, 블록체인은 빼는 美 규제 요구", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/articles/2026-10-15/hyperliquid-founder-yan-seeks-us-rules-that-spare-its-blockchain",
   "s": "제프 얀이 미국 규제당국에 하이퍼리퀴드 블록체인이 아니라 그 위에서 시장을 만드는 업체를 감독하라고 요구하면서, 탈중앙 거래소 규제 범위 논쟁에 불을 붙였다"},
  {"t": "제프 얀, 금융산업 전체를 하이퍼리퀴드 위로 옮기려는 구상", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/articles/2026-10-15/jeff-yan-s-plan-to-bring-the-entire-financial-industry-onto-hyperliquid",
   "s": "제프 얀이 금융산업 전체를 하이퍼리퀴드로 끌어들이겠다는 구상을 밝히면서, 전통 금융 상품의 블록체인 거래 확대를 노리고 있다 (제목 기준)"},
  {"t": "리플, 90억 달러 무기한 선물 붐을 월가 고객에 개방", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/articles/2026-10-15/ripple-opens-9-billion-perp-trading-boom-to-wall-street-clients",
   "s": "리플 프라임이 하이퍼리퀴드 무기한 선물을 참조하는 실물자산 스와프를 기관에 열면서, 미결제약정 약 90억 달러 시장에 월가 자금이 들어올 길이 생겼다"},
  {"t": "바이낸스US, 사업 확장 위해 1억 달러 조달 추진", "o": "블룸버그", "d": "2026-10-16", "u": "https://www.bloomberg.com/news/articles/2026-10-15/binance-us-seeks-100-million-to-expand-its-crypto-business",
   "s": "바이낸스US가 암호화폐 사업 확장을 위해 1억 달러 조달에 나서면서, 미국 내 거래소 경쟁에 다시 힘을 싣고 있다 (제목 기준)"}
 ]
})

# G3-012
items.append({
 "cid": "G3-012", "attachTo": "n-bbg-0116",
 "title": "사모신용 균열 확산…무디스 'PIK가 부실 가려', 은행들 호주 펀드 대출 축소",
 "one": "무디스가 미국 사모신용 차입자 부도율이 PIK·만기연장을 포함하면 4%에서 5.8%로 높아진다고 지적하고 골드만삭스·UBS 등 은행이 호주 사모신용 펀드 대출을 줄이면서, 호주 ASIC의 판매 중지에 이어 사모신용 시장의 유동성 부담이 커지고 있다",
 "facts": [
  "무엇이: 무디스는 평가한 차입자 607곳의 6월까지 12개월 부도율이 4%지만, 부실 차입자의 PIK 변경·만기 연장을 포함하면 5.8%로 오른다고 밝혔다 [사실]",
  "PIK 비중: 상장 BDC의 총투자수익에서 PIK가 차지하는 비중은 약 8%로 2021년 약 5.5%에서 높아졌다 [사실]",
  "은행 후퇴: 골드만삭스·UBS 등이 호주 사모신용 펀드 대출에 더 까다로워졌고 승인권이 있으면 딜을 막기도 하지만, 기존 약정은 대체로 유지되고 있다 [사실]",
  "부동산 노출: 약 2,000억 호주달러 규모 호주 사모신용 시장의 약 절반이 부동산과 연계돼 있고, 바슬라 그룹은 8월 약 34억 호주달러 부채를 안고 파산했다 [사실]",
  "자금 모집: 사모신용은 자금 모집이 사상 최대인 반면 돈을 집행할 곳은 부족해지고 있다 [제목]"
 ],
 "basis": "verified",
 "check": "무디스 부도율·PIK 비중과 은행들의 호주 펀드 대출 축소는 검색 결과 요약(프라이빗에쿼티와이어)으로 확인, 무디스 원보고서는 직접 보지 못함, 로이터 자금 모집 기사는 제목 기준",
 "src": [
  {"o": "Private Equity Wire", "d": "2026-10-14", "u": "https://www.privateequitywire.co.uk/pik-amendments-mask-us-private-credit-stress-moodys-warns/"},
  {"o": "Private Equity Wire", "d": "2026-10-15", "u": "https://www.privateequitywire.co.uk/banks-tighten-financing-for-australian-private-credit-funds/"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "pcredit", "f": "공급", "dir": "down", "k": "실제", "t": "골드만·UBS 등 호주 사모신용 펀드 대출 축소"}
 ],
 "added": "이번 블룸버그 2건·텔레그램 1건·로이터 1건으로 무디스의 PIK에 가려진 부도율 5.8% 분석과 골드만·UBS 등 은행의 호주 사모신용 펀드 대출 축소가 추가됐다",
 "items": [
  {"t": "무디스 \"늘어난 PIK가 美 사모신용 스트레스 가려\"", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/articles/2026-10-14/us-private-credit-stress-masked-by-growing-pik-use-moody-s-says",
   "s": "무디스가 PIK와 만기 연장을 넣으면 사모신용 차입자 부도율이 4%에서 5.8%로 오른다고 밝히면서, 표면 지표보다 큰 부실이 숨어 있다고 경고했다"},
  {"t": "글로벌 은행들, 호주 사모신용 펀드 대출에서 발 빼", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/articles/2026-10-14/banks-pull-back-from-financing-australian-private-credit-funds",
   "s": "글로벌 은행들이 호주 사모신용 펀드에 대한 대출을 줄이면서, 부동산 비중이 큰 소형 운용사부터 자금줄이 좁아지고 있다"},
  {"t": "골드만·UBS, 호주 사모신용 펀드 특화 대출 의지 잃어", "o": "텔레그램 TNBfolio", "d": "2026-10-15", "u": "https://t.me/TNBfolio/71551",
   "s": "골드만삭스·UBS 등이 딜 집행과 환매 대응용 특화 대출을 꺼리면서, 절반이 부동산에 묶인 2,000억 호주달러 시장의 유동성이 더 빠질 수 있다"},
  {"t": "사모신용, 자금 모집 사상 최대에도 집행처 부족", "o": "로이터", "d": "2026-10-16", "u": "https://www.reuters.com/legal/transactional/private-credit-faces-deployment-squeeze-fundraising-hits-record-2026-10-15/",
   "s": "사모신용 자금 모집이 사상 최대를 기록했지만 돈을 집행할 곳이 모자라면서, 대출 경쟁과 조건 완화 압력이 커질 수 있다 (제목 기준)"}
 ]
})

# G3-022
items.append({
 "cid": "G3-022", "attachTo": "",
 "title": "美 연말 쇼핑 매출 4.2% 증가 전망…관세·이란 전쟁에 장난감값은 급등",
 "one": "전미소매협회(NRF)가 11~12월 연말 매출이 4.2% 늘어 약 1조 130억 달러에 이를 것으로 내다봤지만 증가분의 절반가량은 가격 상승 몫이고 관세·이란 전쟁 여파로 장난감값도 급등하면서, 부유층 소비가 연말 매출을 떠받칠 전망이다",
 "facts": [
  "무엇이: NRF는 10월 15일 11~12월 연말 매출이 전년보다 4.2% 늘어 약 1조 130억 달러에 이를 것으로 전망했다(지난해 9,720억 달러, 3.1% 증가) [사실]",
  "물가 몫: 매슈스 NRF 수석 이코노미스트는 증가분의 약 절반은 실질 소비, 나머지는 가격 상승에서 나온다고 봤다 [사실]",
  "비용: 경유값 상승이 운송비를, 메모리 칩 가격 상승이 전자제품 원가를 밀어 올리고 있다 [사실]",
  "장난감: 관세와 이란 전쟁 여파로 연말 쇼핑 시즌을 앞두고 미국 장난감값이 급등했다 [제목]",
  "소비층: 부유층 소비가 연말 소매 판매 증가를 이끌 것으로 예상된다 [제목]"
 ],
 "basis": "partial",
 "check": "NRF 전망치와 물가 몫은 검색 결과 요약(UPI·리테일터치포인츠)으로 확인, 장난감값 급등 폭과 부유층 소비 분석은 확인 못 함",
 "src": [
  {"o": "UPI", "d": "2026-10-15", "u": "https://www.upi.com/Top_News/US/2026/10/15/national-retail-federation-holiday-spending-projection-2026/7911792092453"},
  {"o": "Retail TouchPoints", "d": "2026-10-15", "u": "https://www.retailtouchpoints.com/news/will-2026-holiday-sales-reach-1-trillion-nrf-says-yes/621759"}
 ],
 "inds": ["consumer"], "nodes": [],
 "vc": [
  {"ind": "consumer", "node": "demand", "f": "수요", "dir": "up", "k": "예상", "t": "NRF, 연말 매출 4.2% 늘어 1조 달러 넘을 전망"},
  {"ind": "consumer", "node": "retail", "f": "가격", "dir": "up", "k": "실제", "t": "관세·이란 전쟁 여파로 장난감값 급등"}
 ],
 "added": "이번 로이터·블룸버그 2건으로 NRF의 연말 매출 4.2% 증가·1조 달러 돌파 전망과 부유층 소비가 이를 이끌 것이라는 분석이 추가됐다",
 "items": [
  {"t": "관세·이란 전쟁 여파에 연말 앞두고 美 장난감값 급등", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/business/retail-consumer/us-toy-prices-surge-ahead-holiday-shopping-season-tariffs-iran-war-bite-2026-10-15/",
   "s": "관세와 이란 전쟁 여파가 겹치면서 연말 쇼핑 시즌을 앞둔 미국 장난감값이 급등해, 선물 수요가 큰 품목의 소비자 부담이 커졌다 (제목 기준)"},
  {"t": "NRF \"소비자 버텨 연말 매출 증가세 빨라질 것\"", "o": "로이터", "d": "2026-10-16", "u": "https://www.reuters.com/business/retail-consumer/us-holiday-sales-growth-speed-up-shoppers-stay-resilient-nrf-forecasts-2026-10-15/",
   "s": "NRF가 연말 매출이 4.2% 늘어 약 1조 130억 달러에 이를 것으로 내다보면서, 지난해(3.1%)보다 소비 증가세가 빨라질 것으로 봤다"},
  {"t": "부유층 소비가 美 연말 소매 판매 증가 이끌 전망", "o": "블룸버그", "d": "2026-10-16", "u": "https://www.bloomberg.com/news/articles/2026-10-15/wealthy-shoppers-expected-to-fuel-faster-us-holiday-retail-sales",
   "s": "부유층 소비자가 연말 소매 판매 증가를 이끌 것으로 예상되면서, 소득 계층별 소비 격차가 연말 실적을 가를 수 있다 (제목 기준)"}
 ]
})

# G3-031
items.append({
 "cid": "G3-031", "attachTo": "",
 "title": "핀테크 램프, 18억 5,000만 달러 조달…기업가치 600억 달러로 36% 올라",
 "one": "지출관리 핀테크 램프가 드래고니어 주도로 18억 5,000만 달러를 조달하며 기업가치 600억 달러를 인정받고 연환산 매출이 20억 달러를 넘었다고 밝히면서, 4개월 전 440억 달러였던 몸값이 약 36% 뛰었다",
 "facts": [
  "무엇이: 램프는 10월 15일 드래고니어 주도로 18억 5,000만 달러 신주 투자를 받아 기업가치 600억 달러를 인정받았고, 스라이브캐피털·파운더스펀드 등이 공동 주도했다 [사실]",
  "매출: 연환산 매출이 20억 달러를 넘어 6월 약 15억 달러에서 늘었다 [사실]",
  "가치: 6월 7억 5,000만 달러를 440억 달러 가치에 조달한 뒤 약 4개월 만에 가치가 약 36% 올랐고, 600억 달러는 투자 전 가치다 [사실]",
  "누적: 이번 조달로 누적 지분 투자액은 약 50억 달러가 됐다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약(램프 보도자료·테크크런치)으로 조달액·가치·매출 확인",
 "src": [
  {"o": "PR Newswire(램프 보도자료)", "d": "2026-10-15", "u": "https://www.prnewswire.com/news-releases/ramp-reaches-60-billion-valuation-as-annualized-revenue-tops-2-billion-302909315.html"},
  {"o": "TechCrunch", "d": "2026-10-15", "u": "https://techcrunch.com/2026/10/15/ramp-reaches-60b-valuation-as-it-pushes-deeper-into-ai/"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "payments", "f": "가격", "dir": "up", "k": "실제", "t": "램프 기업가치 440억에서 600억 달러로 상승"}
 ],
 "added": "이번 로이터 1건으로 램프의 이번 조달 규모가 18억 5,000만 달러이고 기업가치가 600억 달러라는 점이 추가됐다",
 "items": [
  {"t": "램프, 매출 급증 속 600억 달러 가치로 투자 유치 완료", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/articles/2026-10-15/ramp-completes-funding-at-60-billion-value-as-revenue-surges",
   "s": "램프가 연환산 매출이 20억 달러를 넘는 급성장 속에 600억 달러 가치로 투자 유치를 마치면서, 핀테크 비상장사 몸값을 끌어올렸다"},
  {"t": "핀테크 램프, 600억 달러 가치에 18억 5,000만 달러 조달", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/technology/fintech-firm-ramp-raises-185-billion-60-billion-valuation-2026-10-15/",
   "s": "램프가 드래고니어 주도로 18억 5,000만 달러를 조달하면서, 6월 440억 달러였던 기업가치가 600억 달러로 약 36% 뛰었다"}
 ]
})

# G3-034
items.append({
 "cid": "G3-034", "attachTo": "n-rtr-0054",
 "title": "ISS·글래스루이스 'MPS 쌍둥이 인수안·특별배당 반대'…인테사 인수에 무게",
 "one": "의결권 자문사 ISS와 글래스루이스가 MPS의 방코BPM·방카제네랄리 인수안과 40억 유로 특별배당에 반대를 권고하고 델핀·칼타지로네 등 주요 주주도 반대하면서, 10월 29일 주총에서 3분의 2 찬성이 필요한 MPS 방어안이 부결되고 인테사 제안이 힘을 얻을 수 있다",
 "facts": [
  "무엇이: ISS는 MPS 주주들에게 10월 29일 주총에서 방코BPM·방카제네랄리 인수안과 40억 유로 특별배당에 반대하라고 권고했다 [사실]",
  "단서: ISS는 메디오방카 합병은 지지했고, 반대 권고가 인테사 제안 지지를 뜻하지는 않으며 인테사 안에도 약점이 있다고 했다 [사실]",
  "글래스루이스: 글래스루이스도 두 인수안과 특별배당에 반대를 권고했다 [사실]",
  "인테사: 인테사는 MPS 주주가 방어안을 부결할 때만 현금 8억 유로를 얹고, 둘 중 하나라도 통과되면 제안을 철회하겠다고 했다 [사실]",
  "표 대결: MPS 지분 3.74%를 가진 방코BPM은 10월 27일 입장을 정한다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약(ANSA·일솔레24오레)으로 ISS·글래스루이스 권고와 인테사 조건 확인",
 "src": [
  {"o": "ANSA", "d": "2026-10-13", "u": "https://ansa.it/sito/notizie/topnews/2026/10/13/iss-bocciare-le-offerte-di-mps-e-la-cedola-da-4-miliardi_ae0a92f2-8299-44c1-8a9a-ba687062b27d.html"},
  {"o": "Il Sole 24 Ore", "d": "2026-10-14", "u": "https://en.ilsole24ore.com/art/mps-iss-versus-bpm-ops-and-banca-generali-AJy1YpiB"}
 ],
 "inds": ["fin"], "nodes": [],
 "vc": [
  {"ind": "fin", "node": "banks", "f": "공급", "dir": "down", "k": "예상", "t": "자문사 부결 권고로 인테사의 MPS 인수에 무게"}
 ],
 "added": "이번 로이터 1건으로 의결권 자문사 ISS가 MPS의 두 인수안과 40억 유로 특별배당에 반대표를 권고했다는 사실이 추가됐다",
 "items": [
  {"t": "ISS \"MPS 주주, 쌍둥이 인수안·특별배당 거부해야\"", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/business/finance/mps-investors-should-reject-twin-bids-special-dividend-proxy-adviser-iss-says-2026-10-14/",
   "s": "의결권 자문사 ISS가 MPS의 방코BPM·방카제네랄리 인수안과 40억 유로 특별배당에 반대를 권고하면서, MPS 방어안 통과가 더 어려워졌다"}
 ]
})

# G4-004
items.append({
 "cid": "G4-004", "attachTo": "n-bbg-0287",
 "title": "ASML, 연매출 전망 440억~450억 유로로 상향…'2028년까지 수요가 공급 앞서'",
 "one": "ASML이 3분기 순이익 50억 유로·매출총이익률 57.5%로 예상을 넘고 2026년 매출 전망 하단을 440억 유로로 높이며 2028년까지 수요가 장비 공급을 넘을 수 있다고 밝히면서, 흔들리던 반도체주 신뢰를 받치고 유럽 증시 기술주 상승을 이끌었다",
 "facts": [
  "무엇이: ASML의 3분기 매출은 116억 6,000만 유로로 예상(약 117억 유로)에 부합했고, 순이익 50억 유로와 매출총이익률 57.5%는 예상을 웃돌았다 [사실]",
  "전망: 4분기 매출을 142억~152억 유로로 제시하고 2026년 연간 매출 전망을 기존 430억~450억 유로에서 440억~450억 유로로 높였다 [사실]",
  "수급: 경영진은 2028년까지 수요가 계획된 장비 공급을 넘을 수 있다고 밝혔다 [사실]",
  "주주환원: 3분기에 자사주 약 41억 유로를 사들였고 주당 1.88유로 중간배당을 정했다 [채널]",
  "시장: ASML의 AI 수요 전망에 유럽 증시 기술주가 오르며 지수가 소폭 상승했다 [제목]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약(SEC 6-K 보도자료·야후파이낸스 콜 요약)으로 3분기 실적·전망·공급 부족 발언 확인, 자사주·배당은 채널 전언",
 "src": [
  {"o": "SEC 6-K(ASML 보도자료)", "d": "2026-10-14", "u": "https://www.sec.gov/Archives/edgar/data/0000937966/000162828026065813/pressreleasefinancialresul.htm"},
  {"o": "Yahoo Finance", "d": "2026-10-14", "u": "https://finance.yahoo.com/markets/stocks/articles/asml-q3-earnings-call-highlights-150000926.html"}
 ],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "vc": [
  {"ind": "semis", "node": "equipment", "f": "수요", "dir": "up", "k": "실제", "t": "연간 매출 전망 상향, 2028년까지 수요가 공급 초과"}
 ],
 "added": "이번 텔레그램 8건·블룸버그 1건·로이터 2건으로 3분기 실적(매출 116억 6,000만 유로·순이익 50억 유로), 연간 전망 하단 상향, 2028년까지 공급 부족 전망이 추가됐다",
 "items": [
  {"t": "ASML, 연간 매출 전망 440억~450억 유로…추정치 웃돌아", "o": "텔레그램 나쁜양파", "d": "2026-10-14", "u": "https://t.me/Badonions/7772",
   "s": "ASML이 연간 매출 전망을 440억~450억 유로로 내고 3분기 매출총이익률 57.5%로 예상(56.1%)을 넘기면서, 시장 추정치보다 강한 가이던스를 제시했다"},
  {"t": "ASML 4분기 매출 전망 142억~152억 유로, 추정치 상회", "o": TG_INS, "d": "2026-10-14", "u": "https://t.me/insidertracking/66194",
   "s": "ASML이 4분기 매출 전망을 142억~152억 유로로 제시해 추정치(141억 8,900만 유로)를 넘기면서, 연말 장비 출하가 늘어날 것을 예고했다"},
  {"t": "ASML 3분기 순매출 116억 6,000만 유로, 예상 소폭 하회", "o": TG_INS, "d": "2026-10-14", "u": "https://t.me/insidertracking/66195",
   "s": "ASML의 3분기 순매출이 116억 6,000만 유로로 예상(117억 유로)을 조금 밑돌면서, 매출보다 이익과 전망이 실적의 초점이 됐다"},
  {"t": "ASML 3분기 EPS 12.95유로로 예상 크게 상회", "o": "텔레그램 카이에 de market", "d": "2026-10-14", "u": "https://t.me/cahier_de_market/10988",
   "s": "ASML이 EPS 12.95유로, 순이익 50억 유로로 예상을 크게 넘고 2027~2028년 공급으로 고객 수요를 다 채우지 못한다고 밝히면서, 장비 품귀를 시사했다"},
  {"t": "ASML, 연간 매출총이익률 전망 56%로 상향", "o": TG_HANA, "d": "2026-10-14", "u": "https://t.me/HANAchina/70404",
   "s": "ASML이 연간 매출총이익률 전망을 56%로 높이고 올해 EUV 사업이 45% 이상 성장한다고 밝히면서, 고가 노광장비 판매 호조가 이익률을 끌어올렸다"},
  {"t": "ASML 3분기 매출 부합·EPS 21.5% 상회", "o": "텔레그램 양파농장", "d": "2026-10-14", "u": "https://t.me/Onionfarmer/18086",
   "s": "ASML의 3분기 매출이 전년보다 55.2% 늘어 예상에 부합하고 EPS는 21.5% 웃돌면서, 설치 기반 관리 매출도 32억 8,900만 유로로 늘었다"},
  {"t": "ASML, 3분기 연속 가이던스 상향…고객은 2030년 물량까지 주문 의사", "o": "텔레그램 TNBfolio", "d": "2026-10-14", "u": "https://t.me/TNBfolio/71539",
   "s": "ASML이 연간 매출 전망 하단을 높여 3분기 연속 가이던스를 올리고 일부 고객이 2029~2030년 물량 주문 의사를 보이면서, 칩 제조사 장비 수요가 길게 이어지고 있다"},
  {"t": "ASML, 전망 상향…향후 수년간 수요가 공급 앞설 것", "o": "블룸버그", "d": "2026-10-14", "u": "https://www.bloomberg.com/news/newsletters/2026-10-14/asml-raises-outlook-sees-demand-outstripping-supply-in-coming-years",
   "s": "ASML이 전망을 올리고 향후 수년간 수요가 공급을 앞설 것으로 보면서, 노광장비 부족이 이어질 수 있다는 신호를 줬다"},
  {"t": "ASML AI 수요 전망에 유럽 증시 기술주 상승", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/markets/europe/european-shares-edge-higher-asmls-ai-demand-outlook-boosts-tech-2026-10-14/",
   "s": "ASML의 AI 수요 전망이 기술주를 밀어 올리면서 유럽 증시가 소폭 올라, 반도체주 투자심리가 일부 회복됐다 (제목 기준)"},
  {"t": "ASML 어닝콜 \"3분기 매출 사상 최대, 잉여현금흐름 114억 유로\"", "o": TG_INS, "d": "2026-10-15", "u": "https://t.me/insidertracking/66275",
   "s": "ASML이 3분기 장비 매출 84억 유로, 잉여현금흐름 114억 유로를 내고 차세대 EUV 장비를 2027년 초부터 소량 출하한다고 밝히면서, 기술 우위를 강조했다"},
  {"t": "ASML, AI 칩 수요에 4분기 매출 예상 웃돌 것으로 전망", "o": "로이터", "d": "2026-10-15", "u": "https://www.reuters.com/business/asml-forecasts-q4-sales-above-expectations-ai-chip-demand-2026-10-14/",
   "s": "ASML이 AI 칩 수요를 근거로 4분기 매출이 예상을 웃돌 것으로 내다보면서, 142억~152억 유로의 매출 전망을 내놨다"}
 ]
})

# G4-014
items.append({
 "cid": "G4-014", "attachTo": "n-tg-0118",
 "title": "씨티 'CXMT D램 우려 과도, 2028년 전 양산 난망'…CXMT 시총 3조 위안 붕괴",
 "one": "중국 CXMT의 4F² 서버 D램 출시 소식에 메모리주가 흔들린 가운데 씨티가 CXMT가 선두보다 4세대 뒤처져 2028년 전 양산이 어렵다며 우려가 과도하다고 평가했지만, YMTC가 낸드 출하량 세계 3위로 올라서면서 중국발 메모리 공급 압력 논쟁은 이어지고 있다",
 "facts": [
  "무엇이: 씨티는 CXMT 4F² D램의 세계 공급 영향이 제한적이며, 기존 1y 나노 공정 기반이라 2028년 이전 양산 가능성이 낮다고 봤다 [사실]",
  "근거: 씨티는 CXMT가 선두 업체보다 4세대 뒤처져 있고 EUV 접근 제한으로 제조 비용이 10~20% 높을 수 있다고 지적했다 [사실]",
  "CXMT 계획: CXMT는 연말까지 4F² 구조 서버용 DDR5 RDIMM을 내놓겠다고 했지만 생산능력·성능·양산 일정은 공개하지 않았다 [사실]",
  "주가: CXMT는 10월 15일 오전 장중 5% 넘게 내려 시가총액 3조 위안이 무너졌고 A주 시총 1위를 공상은행에 내줬다 [채널]",
  "YMTC: 카운터포인트 집계로 YMTC는 2026년 2분기 낸드 출하량 세계 3위에 올라 키옥시아·마이크론을 앞섰다 [채널]"
 ],
 "basis": "verified",
 "check": "씨티 평가와 CXMT 출시 계획은 검색 결과 요약(서울경제·트렌드포스·집계 사이트)으로 확인, 씨티 원보고서는 직접 보지 못함, CXMT 시총·YMTC 순위는 채널 전언",
 "src": [
  {"o": "Seoul Economic Daily", "d": "2026-10-15", "u": "https://en.sedaily.com/society/2026/10/15/chinas-cxmt-to-unveil-4f2-dram-this-year-mass-output-seen"},
  {"o": "TrendForce", "d": "2026-10-12", "u": "https://www.trendforce.com/news/2026/10/12/news-cxmt-accelerates-4f%C2%B2-dram-push-eyes-year-end-server-ddr5-rdimm-launch/"}
 ],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "vc": [
  {"ind": "semis", "node": "memory", "f": "공급", "dir": "up", "k": "예상", "t": "CXMT 4F² 서버 D램 출시 계획, 양산은 2028년 이후"},
  {"ind": "semis", "node": "memory", "f": "가격", "dir": "down", "k": "실제", "t": "CXMT 주가 하락에 시가총액 3조 위안 붕괴"}
 ],
 "added": "이번 텔레그램 6건으로 씨티의 'CXMT 영향은 2028년 전 제한적' 평가, CXMT 시총 3조 위안 붕괴, YMTC 낸드 출하량 세계 3위 상승 소식이 추가됐다",
 "items": [
  {"t": "난야 최고 실적에도 CXMT 4F² 소문에 메모리주 매도", "o": TG_HANA, "d": "2026-10-14", "u": "https://t.me/HANAchina/70374",
   "s": "CXMT가 연말 전 4F² 구조 서버용 DDR5를 낸다는 소문이 돌면서, 난야가 사상 최고 3분기 순이익을 냈는데도 대만 메모리주가 강하게 팔렸다"},
  {"t": "\"중국 내에선 CXMT 4F² 소식 특별할 것 없어\"", "o": TG_HANA, "d": "2026-10-15", "u": "https://t.me/HANAchina/70444",
   "s": "중국 시장에서는 CXMT 4F² 소식이 예상된 일이라 큰 이슈가 아니었고, 메모리 기술주 열기가 식으며 고배당주로 자금이 옮겨 가고 있다는 전언이 나왔다"},
  {"t": "하나증권 \"CXMT 상장이 中 지방정부 모방 투자 불씨\"", "o": TG_HANA, "d": "2026-10-15", "u": "https://t.me/HANAchina/70453",
   "s": "하나증권이 CXMT 상장 성공과 허페이시 모델이 지방 재정난 속 중국 지방정부의 모방 투자를 부를 수 있다고 짚으면서, 반도체 과잉투자 위험을 제기했다"},
  {"t": "YMTC, 2분기 글로벌 낸드 출하량 3위로 상승", "o": TG_HANA, "d": "2026-10-15", "u": "https://t.me/HANAchina/70462",
   "s": "YMTC가 2분기 낸드 출하량 세계 3위로 올라 키옥시아·마이크론을 앞서고 매출 점유율도 9%에서 14%로 높이면서, 중국 낸드 공급이 빠르게 늘고 있다"},
  {"t": "CXMT 시총 3조 위안 붕괴…A주 1위 공상은행에 내줘", "o": TG_HANA, "d": "2026-10-15", "u": "https://t.me/HANAchina/70468",
   "s": "CXMT 주가가 장중 5% 넘게 빠져 시가총액 3조 위안이 무너지면서, 상장 두 달 반 만에 A주 시총 1위 자리를 공상은행에 넘겨줬다"},
  {"t": "씨티 \"CXMT의 D램 공급 영향 우려 과도, 2028년 전 제한적\"", "o": TG_INS, "d": "2026-10-15", "u": "https://t.me/insidertracking/66353",
   "s": "씨티가 CXMT가 선두보다 4세대 뒤처지고 제조 비용이 10~20% 높다며 2028년 전 영향이 제한적이라고 평가하면서, 메모리주 매도가 과도하다고 봤다"}
 ]
})

# G4-039
items.append({
 "cid": "G4-039", "attachTo": "n-rtr-0267",
 "title": "GTCR·엘리엇, CCC 인수 확정…프루프포인트는 바로니스 63억 달러 현금 인수",
 "one": "GTCR와 엘리엇이 막바지 협상 끝에 소프트웨어 기업 CCC 인텔리전트 솔루션즈 인수에 합의하고 토마브라보 계열 프루프포인트가 바로니스를 63억 달러 전액 현금으로 사기로 하면서, 사모펀드 자본의 기업용 소프트웨어 인수가 잇따르고 있다",
 "facts": [
  "무엇이: 토마브라보 소유 프루프포인트가 바로니스 시스템즈를 약 63억 달러 전액 현금으로 인수하기로 10월 15일 합의했다 [사실]",
  "조건: 바로니스 주주는 주당 49.75달러를 받고, 거래는 2027년 상반기에 마무리될 예정이다 [사실]",
  "CCC: GTCR와 엘리엇이 CCC 인텔리전트 솔루션즈 인수에 합의했고, 규모는 블룸버그 제목이 46억 달러, 로이터 제목이 61억 달러로 전했다 [제목]",
  "기존: 앞서 두 회사가 CCC 인수를 위한 막바지 협상을 벌이고 있다는 보도가 나왔다 [제목]"
 ],
 "basis": "partial",
 "check": "프루프포인트의 바로니스 인수는 검색 결과 요약(칼칼리스트·KSL)으로 확인, CCC 인수 규모(46억·61억 달러 차이)는 확인 못 함",
 "src": [
  {"o": "Calcalist", "d": "2026-10-15", "u": "https://www.calcalistech.com/ctechnews/article/gzk6vlon8"}
 ],
 "inds": ["tech"], "nodes": [],
 "vc": [
  {"ind": "tech", "node": "software", "f": "공급", "dir": "down", "k": "실제", "t": "바로니스·CCC, 사모펀드 계열에 인수 합의"}
 ],
 "added": "이번 블룸버그 1건·로이터 2건으로 GTCR·엘리엇의 CCC 인수 합의(46억~61억 달러)와 프루프포인트의 바로니스 63억 달러 현금 인수가 추가됐다",
 "items": [
  {"t": "GTCR·엘리엇, 소프트웨어 기업 CCC 46억 달러에 인수", "o": "블룸버그", "d": "2026-10-15", "u": "https://www.bloomberg.com/news/articles/2026-10-15/gtcr-elliott-acquire-software-firm-ccc-for-4-6-billion",
   "s": "GTCR와 엘리엇이 소프트웨어 기업 CCC를 46억 달러에 사들이기로 하면서, 막바지 협상이 인수 합의로 마무리됐다 (제목 기준)"},
  {"t": "GTCR·엘리엇, 61억 달러 규모 CCC 인텔리전트 솔루션즈 인수", "o": "로이터", "d": "2026-10-16", "u": "https://www.reuters.com/legal/transactional/gtcr-elliott-buy-ccc-intelligent-solutions-61-billion-deal-2026-10-15/",
   "s": "로이터는 GTCR·엘리엇의 CCC 인텔리전트 솔루션즈 인수 규모를 61억 달러로 전하면서, 블룸버그 제목의 46억 달러와 다른 수치를 제시했다 (제목 기준)"},
  {"t": "프루프포인트, 바로니스 시스템즈 63억 달러 전액 현금 인수", "o": "로이터", "d": "2026-10-16", "u": "https://www.reuters.com/legal/transactional/proofpoint-buy-varonis-systems-63-billion-all-cash-deal-2026-10-15/",
   "s": "토마브라보 계열 프루프포인트가 바로니스를 주당 49.75달러, 총 63억 달러 현금에 사기로 하면서, 데이터 보안 소프트웨어 업계 통합이 진행됐다"}
 ]
})

# G4-053
items.append({
 "cid": "G4-053", "attachTo": "",
 "title": "인텔 이스라엘 키르얏갓 공장 폭발로 2명 사망…독성가스 NF3 누출",
 "one": "이스라엘 키르얏갓의 인텔 반도체 공장에서 10월 14일 가스 실린더 오작동으로 추정되는 폭발이 일어나 근로자 2명이 숨지고 독성가스 삼불화질소가 새면서, 당국이 원인 조사와 현장 위험 점검에 나섰다",
 "facts": [
  "무엇이: 10월 14일 이스라엘 키르얏갓 인텔 공장에서 폭발이 일어나 근로자 2명이 숨지고 1명이 중상을 입었다 [사실]",
  "가스: 폭발로 불이 나며 반도체 장비 세정에 쓰는 독성 가스 삼불화질소(NF3)가 샜고, 화재는 진압됐다 [사실]",
  "원인: 경찰은 탱크로리 교체 중 가스 실린더 오작동을 의심하며 범죄·과실 혐의는 없다고 봤고, 인텔은 조사에 협조하고 있다 [사실]",
  "시설: 이 단지에는 Fab 28이 있고, 인접한 Fab 38 건설은 2024년 중반부터 멈춰 있다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약(타임스오브이스라엘·톰스하드웨어·DCD)으로 사상자·가스·원인 추정 확인, 생산 차질 여부는 보도 없음",
 "src": [
  {"o": "Times of Israel", "d": "2026-10-14", "u": "https://www.timesofisrael.com/3-workers-seriously-hurt-in-apparent-gas-explosion-at-intel-plant-in-southern-israel/"},
  {"o": "Tom's Hardware", "d": "2026-10-15", "u": "https://www.tomshardware.com/tech-industry/semiconductors/two-killed-one-seriously-hurt-in-explosion-at-intels-chip-plant-in-israel-police-suspect-a-gas-cylinder-malfunction-and-the-fire-involved-a-toxic-gas-used-to-clean-chipmaking-tools"},
  {"o": "DCD", "d": "2026-10-15", "u": "https://www.datacenterdynamics.com/en/news/two-workers-killed-third-injured-in-explosion-at-intels-kiryat-gat-fab-in-israel/"}
 ],
 "inds": ["macro"], "nodes": ["macro/semis"],
 "vc": [
  {"ind": "semis", "node": "foundry", "f": "-", "dir": "flat", "k": "실제", "t": "키르얏갓 공장 가스 폭발, 생산 영향은 알려지지 않음"}
 ],
 "items": [
  {"t": "이스라엘 인텔 키르얏갓 공장 폭발 현장 공개…NF3 처리 중", "o": "텔레그램 트릴리온", "d": "2026-10-14", "u": "https://t.me/Trillion_labs/10489"}
 ]
})

# G4-066
items.append({
 "cid": "G4-066", "attachTo": "n-tg-0273",
 "title": "中 태양광 5대 기업, 지난해 4만 명 추가 감원…감산·가격 하한선 합의 이어 구조조정",
 "one": "론지·트리나·징코·JA솔라·통웨이 등 중국 태양광 5대 기업이 과잉설비 속에 지난해 인력을 4만 명 넘게(21%) 줄인 데 이어 항저우 회의에서 자율 감산과 폴리실리콘·모듈 가격 하한선까지 정하면서, 공급 과잉에 빠진 태양광 공급망의 구조조정이 이어지고 있다",
 "facts": [
  "무엇이: 론지·트리나·징코·JA솔라·통웨이 5개사의 2025년 말 직원 수는 15만 4,061명으로 1년 새 4만 589명(21%) 줄었다 [사실]",
  "누적: 앞선 해에도 약 31%를 줄여 2년 새 인력이 절반가량 사라졌다 [사실]",
  "배경: 세계 폴리실리콘 설비가 연간 수요를 크게 웃돌아 공장 가동률이 낮고, 분석가들은 과잉설비가 2027년까지 이어질 것으로 본다 [사실]",
  "기존: 통웨이·GCL 등은 10월 11일 항저우 비공개 회의에서 수요에 맞춘 자율 감산 실행안과 폴리실리콘·모듈 가격 하한선을 정했다 [사실]"
 ],
 "basis": "verified",
 "check": "검색 결과 요약(차이나글로벌사우스·에너지뉴스)으로 감원 규모와 직원 수 확인",
 "src": [
  {"o": "China Global South", "d": "2026-10-14", "u": "https://chinaglobalsouth.com/2026/10/14/china-solar-giants-cut-40000-jobs-overcapacity-crisis/"},
  {"o": "energynews.pro", "d": "2026-10-14", "u": "https://energynews.pro/en/chinas-five-largest-solar-panel-makers-cut-their-workforces-again"}
 ],
 "inds": ["power"], "nodes": ["power/modules", "power/polysilicon"],
 "vc": [
  {"ind": "power", "node": "modules", "f": "공급", "dir": "down", "k": "실제", "t": "중국 태양광 5대 기업 지난해 인력 4만 명 감축"}
 ],
 "added": "이번 로이터 1건으로 중국 태양광 5대 기업이 지난해 인력을 4만 589명(21%) 줄였다는 사실이 추가됐다",
 "items": [
  {"t": "中 태양광 대기업, 과잉설비 지속에 지난해 4만 명 추가 감원", "o": "로이터", "d": "2026-10-14", "u": "https://www.reuters.com/business/world-at-work/china-solar-giants-shed-another-40000-jobs-last-year-overcapacity-persists-2026-10-14/",
   "s": "중국 태양광 5대 기업이 과잉설비 속에 지난해 인력을 4만 589명(21%) 줄이면서, 2년 새 인력이 절반가량 사라지는 구조조정이 이어졌다"}
 ]
})

out = {"agent": "W8", "searches_used": 16, "fetches_used": 1,
       "items": items,
       "skipped": [{"cid": "G1-043", "reason": "이미 다룸(n-rtr-0232)"}]}

json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)

TAIL = re.compile(r" \((제목 기준|채널 전언)\)$")
for x in items:
    multi = len(x["items"]) > 1 or x["attachTo"]
    lo, hi = (90, 160) if multi else (80, 130)
    n = len(TAIL.sub("", x["one"]))
    flag = "" if lo <= n <= hi else "  <-- one"
    print(x["cid"], "title", len(x["title"]), "one", n, flag)
    if not (20 <= len(x["title"]) <= 50): print("   title len!")
    if "added" in x:
        a = len(TAIL.sub("", x["added"]))
        if not (60 <= a <= 140): print("   added", a)
    for it in x["items"]:
        if not (25 <= len(it["t"]) <= 60): print("   t", len(it["t"]), it["t"])
        if "s" in it:
            s = len(TAIL.sub("", it["s"]))
            if not (45 <= s <= 110): print("   s", s, it["s"][:30])
    for v in x["vc"]:
        if not (12 <= len(v["t"]) <= 45): print("   vc t", len(v["t"]))
    for f in x["facts"]:
        if "|" in f or "**" in f or "{{" in f: print("   bad char")
