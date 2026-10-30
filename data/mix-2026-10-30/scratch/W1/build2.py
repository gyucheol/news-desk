import json
BB = '블룸버그'
def it(t, o, d, u, s=None):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s: x["s"] = s
    return x
P1 = json.load(open('/home/user/news-desk/data/mix-2026-10-30/scratch/W1/part1.json'))
I = P1["items"]
B = 'https://www.bloomberg.com/news/'

# ---------- G2-001 ECB
I.append({
 "cid": "G2-001", "attachTo": "",
 "title": "ECB 예금금리 2.5% 동결·12월 인상 대비…라가르드 2월 7일 조기 사임, 후임 경쟁 시작",
 "one": "\n".join([
  "ECB가 예금금리를 2.5%로 동결한 날 라가르드 총재가 2027년 2월 7일 조기 사임을 발표했다.",
  "· 라가르드는 에너지 가격 급등의 간접 영향이 심화됐다면서도 물가 확산 위험은 낮게 봤다.",
  "· 유로존 9월 물가 상승률은 3.8%였고 유럽 가스값은 10월 들어 36% 급등했다.",
  "· ECB 위원들은 12월 금리 인상을 준비하고 있다.",
  "· 프랑스 10년물 금리는 5%로 2002년 이후 최고였고 라가르드 사임 발표에 프랑스 시장은 숨을 돌렸다.",
  "· EU는 당일 후임 선출에 착수했고 데코스와 크노트가 유력 후보로 거론된다.",
  "· 라가르드는 중립 의무를 벗고 정치에 뛰어들 가능성을 내비쳤다."]),
 "facts": [
  "무엇이: ECB는 10월 29일 9월 0.25%p 인상 뒤 예금금리를 2.5%로 동결했고, 라가르드 총재는 2027년 10월 임기 만료 약 9개월 전인 2027년 2월 7일 물러나겠다고 밝혔다 [사실]",
  "물가: 유로존 9월 물가 상승률은 3.8%로 2023년 9월 이후 최고이고, 라가르드는 에너지 가격 급등의 간접 영향이 심화됐다고 했다 [사실]",
  "12월: ECB 위원들이 12월 금리 인상을 준비하고 있고 시장도 12월 인상을 널리 예상한다 [사실]",
  "프랑스·가스: 프랑스 10년물 금리가 5%로 2002년 이후 최고를 기록해 인상에 부담이 되고, 유럽 가스값은 낮은 비축량에 10월 들어 36% 올랐다 [채널]",
  "후임: EU는 당일 후임 선출 절차에 착수했고 데코스·크노트가 유력 후보로 꼽히며, 라가르드는 중립을 벗고 정치에 참여할 가능성을 시사했다 [사실]"],
 "basis": "verified",
 "check": "Euronews·CNBC 검색 결과 요약으로 2.5% 동결·2027년 2월 7일 사임·물가 3.8%·12월 인상 예상·프랑스 10년물 5%·후임 후보 확인. 가스 36%는 채널(WSJ 인용) 기준",
 "src": [{"o": "Euronews", "d": "2026-10-29", "u": "https://www.euronews.com/2026/10/29/ecb-holds-rates-at-25-as-lagarde-announces-early-exit-with-inflation-near-double-the-targe"},
         {"o": "CNBC", "d": "2026-10-29", "u": "https://www.cnbc.com/2026/10/29/european-central-bank-interest-rates.html"}],
 "inds": ["macro"], "nodes": ["macro/cb", "macro/rates"],
 "vc": [{"ind": "macro", "node": "cb", "f": "가격", "dir": "flat", "k": "실제", "t": "ECB 예금금리 2.5% 동결·12월 인상 대비"},
        {"ind": "macro", "node": "rates", "f": "가격", "dir": "mixed", "k": "실제", "t": "프랑스 10년물 5% 뒤 라가르드 사임에 숨 돌려"}],
 "items": [
  it("ECB, 프랑스·에너지 위험 점검 위해 금리 동결할 듯", BB, "2026-10-29", B+"articles/2026-10-29/ecb-set-to-hold-rates-to-assess-france-and-energy-risks",
     "ECB가 프랑스 국채 불안과 에너지 위험을 따져 보려고 금리를 동결할 것으로 예상되면서 결정 전 시장의 관망이 이어졌다 (제목 기준)"),
  it("라가르드 ECB 조기 사임, 후임 경쟁 불붙어", BB, "2026-10-29", B+"articles/2026-10-29/lagarde-will-step-down-as-ecb-president-in-february",
     "라가르드 총재가 임기 만료 약 9개월 전인 2월 물러나기로 하면서 ECB 차기 총재를 둘러싼 경쟁이 본격화했다"),
  it("라가르드 ECB 총재, 2월 7일 조기 사임 계획", "텔레그램 미국 주식 인사이더", "2026-10-29", "https://t.me/insidertracking/67767",
     "라가르드 총재가 직원들에게 2월 7일 사임 계획을 알리면서 ECB 지도부 교체 일정이 앞당겨졌다"),
  it("코스타 'EU, 오늘 새 ECB 총재 물색 시작'", BB, "2026-10-29", B+"articles/2026-10-29/costa-says-eu-will-start-search-for-new-ecb-president-today",
     "코스타 EU 정상회의 상임의장이 당일부터 후임 ECB 총재 물색에 나선다고 밝히면서 인선 절차가 곧바로 시작됐다 (제목 기준)"),
  it("ECB 실시간: 라가르드 조기 사임, 금리 결정 앞둬", BB, "2026-10-29", B+"live-blog/2026-10-29/lagarde-steps-down-ecb-rate-decision-euro-live-updates",
     "라가르드 조기 사임 소식이 금리 결정 직전에 나오면서 유로화와 유럽 금리 시장이 두 사안을 함께 소화했다 (제목 기준)"),
  it("ECB 동결 속 라가르드, 물가 확산 위험 낮게 봐", BB, "2026-10-29", B+"articles/2026-10-29/ecb-holds-rates-as-lagarde-exit-compounds-alarm-over-oil-france",
     "ECB가 예금금리를 2.5%로 동결하면서 라가르드가 물가 상승의 확산 위험을 낮게 평가해 즉각 인상 기대를 눌렀다"),
  it("라가르드 물러나며 ECB 수장 자리 경쟁 시작", BB, "2026-10-29", B+"newsletters/2026-10-29/contest-to-lead-ecb-begins-as-lagarde-bows-out",
     "라가르드가 물러나기로 하면서 데코스·크노트 등이 거론되는 ECB 수장 경쟁이 막을 올렸다"),
  it("라가르드 '에너지 가격 급등의 간접 영향 심화'", "텔레그램 트릴리온", "2026-10-29", "https://t.me/Trillion_labs/11403",
     "라가르드 총재가 에너지 가격 급등의 간접 영향이 심화됐다고 밝히면서 유로존 물가 압력이 넓어지고 있음을 인정했다"),
  it("라가르드, 중립 벗고 정치판 뛰어들려 ECB 떠나", BB, "2026-10-30", B+"articles/2026-10-29/lagarde-quits-ecb-to-shed-neutrality-and-enter-political-fray-mvtp2d3u",
     "라가르드가 중앙은행 총재의 중립 의무를 벗고 정치에 뛰어들기 위해 ECB를 떠난다는 해석이 나오면서 프랑스 정치 변수와 엮였다 (제목 기준)"),
  it("라가르드 퇴장 일정 확정에 프랑스 시장 숨 돌려", BB, "2026-10-30", B+"newsletters/2026-10-29/lagarde-sets-exit-as-french-markets-get-a-breather",
     "라가르드가 퇴장 일정을 정하는 사이 10년물 금리 5%까지 밀렸던 프랑스 채권시장이 잠시 숨을 돌렸다"),
  it("ECB 위원들, 12월 금리 인상할 준비 갖춰", BB, "2026-10-30", B+"articles/2026-10-29/ecb-officials-are-ready-to-raise-interest-rates-in-december",
     "ECB 위원들이 12월 금리 인상에 나설 준비가 돼 있다고 보면서 이번 동결이 일시 정지에 그칠 가능성이 커졌다"),
  it("WSJ 'ECB 2.5% 동결, 에너지발 물가에 인상 압력'", "텔레그램 상상인 김진범", "2026-10-30", "https://t.me/PipeBeom/6922",
     "ECB가 예금금리를 2.5%로 동결했지만 9월 물가 3.8%와 가스값 36% 급등으로 인상 압력이 커지면서 프랑스 국채 불안이 인상 속도를 제약할 수 있다"),
  it("유럽 경제 압박 커지는 가운데 라가르드 물러나", BB, "2026-10-30", B+"newsletters/2026-10-29/ecb-s-lagarde-steps-aside-as-european-economic-pressure-builds",
     "에너지발 물가와 프랑스 금리 상승으로 유럽 경제 압박이 커지는 가운데 라가르드가 물러나면서 후임의 부담이 커졌다"),
  it("라가르드, 조기 사임 후 정치 참여 가능성 언급", "텔레그램 Polaristimes", "2026-10-30", "https://t.me/The_MariTimes/64103",
     "프랑스 재무장관 출신인 라가르드가 조기 사임 뒤 정계 복귀 가능성을 내비치면서 사임 이유가 본인의 정치적 야망으로 옮겨 갔다")]
})

# ---------- G2-024 엔비디아
I.append({
 "cid": "G2-024", "attachTo": "",
 "title": "젠슨 황, 중국 스파이 공작 표적 보도…대만선 엔비디아 직원 대중 칩 밀수 혐의 구속",
 "one": "\n".join([
  "엔비디아 젠슨 황 CEO가 중국 스파이 공작의 표적이 됐다는 보도가 나오며 대중 칩 유출 의혹이 커졌다.",
  "· 뉴욕타임스는 싱가포르 데이터센터 업체 메가스피드 임원이 중국을 위해 정보를 모았다고 보도했다.",
  "· 대만 검찰이 엔비디아 직원을 대중국 반도체 밀수 혐의로 구속했다는 소식도 전해졌다.",
  "· 젠슨 황은 스파이 수사 대상 회사와의 관계가 정상적이었다고 해명했다."]),
 "facts": [
  "무엇이: 뉴욕타임스는 10월 29일 미 정보당국이 메가스피드 임원 앨리스 황을 중국 정보 수집원으로 판단했고 그가 젠슨 황과 가까운 관계를 맺었다고 보도했다 [사실]",
  "한계: 보도는 젠슨 황이 알고 도왔다는 근거는 없다고 했고 아무도 기소되지 않았으며, 중국 대사관은 근거 없는 비방이라고 반박했다 [사실]",
  "대만 수사: 대만 검찰의 엔비디아 직원 구속은 7월 슈퍼마이크로 서버 약 50대 대중 밀수 수사 때 이미 보도됐고, 이번 '속보'가 새 구속인지는 확인하지 못했다 [미확인]",
  "해명: 젠슨 황은 스파이 수사 대상 회사와의 관계가 '정상적'이었다고 말했고, 엔비디아는 고객과의 만남은 CEO 업무의 일부라고 밝혔다 [제목]"],
 "basis": "partial",
 "check": "Yahoo Finance·Fox Business 검색 결과 요약으로 NYT 스파이 표적 보도 확인. 대만 엔비디아 직원 구금은 7월 보도만 찾아 이번 구속 시점은 미확인. 젠슨 황 '정상적' 발언은 제목 기준",
 "src": [{"o": "Yahoo Finance", "d": "2026-10-29", "u": "https://finance.yahoo.com/technology/ai/articles/nvidia-ceo-huang-caught-reported-135330027.html"},
         {"o": "Fox Business", "d": "2026-10-29", "u": "https://www.foxbusiness.com/business-leaders/suspected-chinese-intelligence-asset-gained-access-nvidia-ceo-jensen-huang-report"},
         {"o": "DCD", "d": "2026-07-28", "u": "https://www.datacenterdynamics.com/en/news/nvidia-employee-detained-in-taiwan-as-part-of-ongoing-chip-smuggling-investigation/"}],
 "inds": ["semis", "macro"], "nodes": ["macro/semis", "macro/geo"],
 "vc": [{"ind": "semis", "node": "policy", "f": "-", "dir": "flat", "k": "예상", "t": "엔비디아 대중 칩 밀수·스파이 의혹으로 수사 압박"}],
 "items": [
  it("젠슨 황, 중국 스파이 공작의 표적으로 지목돼", "텔레그램 미국 주식 인사이더", "2026-10-29", "https://t.me/insidertracking/67762",
     "젠슨 황 엔비디아 CEO가 중국 스파이 공작의 표적이 됐다는 보도가 나오면서 엔비디아의 대중 거래에 대한 의심이 커졌다"),
  it("대만 검찰, 엔비디아 직원 대중 반도체 밀수 혐의 구속", "텔레그램 Polaristimes", "2026-10-29", "https://t.me/The_MariTimes/64094",
     "대만 검찰이 엔비디아 직원을 대중국 반도체 밀수 혐의로 구속했다고 전해지면서 워싱턴에서 엔비디아의 발언권이 약해질 수 있다는 평가가 나왔다"),
  it("젠슨 황 '스파이 수사 대상 회사와 관계는 정상적'", BB, "2026-10-30", B+"articles/2026-10-29/nvidia-ceo-says-ties-to-company-under-spying-probe-were-normal",
     "젠슨 황이 스파이 수사 대상 회사와의 관계를 정상적인 거래라고 해명하면서 개인 연루 의혹 진화에 나섰다 (제목 기준)")]
})

# ---------- G2-033 ING·로이즈
I.append({
 "cid": "G2-033", "attachTo": "",
 "title": "ING 3분기 이익 18.5억 유로 예상 하회·400명 감원…로이즈는 이익 웃돌았지만 전망 유지",
 "one": "\n".join([
  "유럽 은행 실적이 엇갈린 가운데 ING는 이익이 예상에 못 미쳤고 로이즈는 금리 상승 속 전망을 유지했다.",
  "· ING 3분기 순이익은 18억 5,000만 유로로 3.5% 늘었지만 예상 19억 7,000만 유로에 못 미쳤다.",
  "· ING는 도매금융 재편으로 약 400명을 줄이고 16억 5,000만 유로 자사주 매입을 발표했다.",
  "· 로이즈는 이익이 예상을 웃돌았지만 연간 전망은 그대로 유지했다.",
  "· 로이즈는 높은 금리가 이어지면 자산 성장이 둔화할 수 있다고 밝혔다."]),
 "facts": [
  "무엇이: ING 3분기 순이익은 18억 5,000만 유로로 3.5% 늘었지만 예상 19억 7,000만 유로를 밑돌았고, 대손비용 증가와 수익 부진이 원인이었다 [사실]",
  "ING 감원·환원: 2027년 도매금융 재편으로 약 400명을 줄이고(3월 1,250명에 추가) 4분기 1억 7,500만 유로 구조조정 충당금을 쌓으며, 16억 5,000만 유로 자사주 매입과 2억 5,000만 유로 현금 배당을 발표했다 [사실]",
  "로이즈: 9개월 법정 세후이익은 48억 3,500만 파운드, 3분기 유형자기자본이익률은 19.5%였고 연간 순이자이익 149억 파운드 초과 등 전망을 유지했다 [사실]",
  "금리 부담: 로이즈는 높은 금리가 지속되면 자산 성장이 둔화하기 시작할 수 있다고 밝혔다 [사실]"],
 "basis": "verified",
 "check": "NL Times·Finimize 검색 결과 요약으로 ING 이익 18억 5,000만 유로·예상 19억 7,000만 유로·400명 감원 확인, 로이즈 3분기 IMS로 전망 유지·고금리 자산 성장 둔화 언급 확인",
 "src": [{"o": "NL Times", "d": "2026-10-29", "u": "https://nltimes.nl/2026/10/29/ing-planning-cut-hundreds-jobs-despite-eu19-billion-profit-last-quarter"},
         {"o": "Finimize", "d": "2026-10-29", "u": "https://finimize.com/content/ing-rolls-out-165-billion-buyback-even-as-profit-misses"},
         {"o": "로이즈 3분기 IMS", "d": "2026-10-29", "u": "https://www.lloydsbankinggroup.com/assets/pdfs/investors/financial-performance/lloyds-banking-group-plc/2026/q3/2026-lbg-q3-ims.pdf"}],
 "inds": ["fin"], "nodes": [],
 "vc": [{"ind": "fin", "node": "banks", "f": "수요", "dir": "down", "k": "예상", "t": "로이즈, 고금리 지속 시 자산 성장 둔화 경고"}],
 "items": [
  it("ING, 분기 이익 예상 하회 속 인력 감원 발표", BB, "2026-10-29", B+"articles/2026-10-29/ing-dutch-netherlands-job-cuts-quarterly-profit-misses-estimates",
     "ING가 대손비용 증가로 3분기 순이익이 예상에 못 미치면서 도매금융 재편으로 약 400명을 줄이기로 했다"),
  it("로이즈 이익 예상 상회, 금리 상승 속 전망 보합에 빛바래", BB, "2026-10-29", B+"articles/2026-10-29/lloyds-beats-estimates-on-rise-in-fees-and-interest-income",
     "로이즈가 수수료·이자이익 증가로 예상을 웃돌았지만 금리 상승 속에 연간 전망을 올리지 않으면서 주가 반응이 식었다")]
})

# ---------- G2-039 RBNZ (attach)
I.append({
 "cid": "G2-039", "attachTo": "n-bbg-0542",
 "title": "뉴질랜드중앙은행 2.75% 깜짝 동결 뒤 총재 '12월 인상 가능성 높아'…시장 77% 반영",
 "one": "\n".join([
  "뉴질랜드중앙은행이 10월 28일 금리를 2.75%로 깜짝 동결한 뒤 총재가 12월 인상 가능성을 높게 봤다.",
  "· 이코노미스트 다수는 11월 7일 총선 전 0.25%p 인상으로 3%를 예상했지만 표결은 4대 3 동결이었다.",
  "· 결정 전 시장의 10월 인상 확률은 81%였고, 동결 뒤 12월 인상 확률은 약 77%로 반영됐다.",
  "· 브레먼 총재는 위원 전원이 추가 인상 가능성에 동의한다며 다음 결정일은 12월 9일이다.",
  "· 2분기 물가는 4.1%, 3분기는 3.7%였고 ASB는 4분기 4.7%를 전망했다.",
  "· 3분기 CPI는 약세를 이어 온 뉴질랜드달러의 방향을 가를 시험대로 꼽혔다."]),
 "facts": [
  "무엇이: 뉴질랜드중앙은행은 11월 7일 총선 10일 전인 10월 28일 기준금리를 2.75%로 동결해 0.25%p 인상(3%)을 예상한 시장을 놀라게 했고, 표결은 4대 3이었다 [사실]",
  "12월 신호: 안나 브레먼 총재는 다음 날 12월 인상 가능성이 높다며 위원 전원이 추가 인상 가능성에 동의한다고 했고, 다음 결정은 12월 9일이다 [사실]",
  "시장·이견: 10월 인상 확률은 지난주 초 56%에서 81%로 올랐지만 동결됐고, 12월 인상 확률은 약 77%이며 웨스트팩은 12월 인상을, ANZ는 12월 동결을 점쳤다 [사실]",
  "물가: 2분기 물가 상승률은 4.1%, 3분기는 3.7%로 중앙은행 예상보다 낮았지만 ASB는 4분기 4.7%를 전망했다 [사실]",
  "환율: 3분기 CPI 결과가 약세를 이어 온 뉴질랜드달러의 방향을 가를 시험대로 꼽혔다 [제목]"],
 "basis": "verified",
 "check": "investinglive·Newsquawk·FXStreet 검색 결과 요약으로 10월 28일 2.75% 동결(4대 3)·브레먼 12월 인상 가능성 높음·12월 인상 확률 약 77%·12월 9일 결정 확인. 기존 문서의 10월 인상 전망은 빗나감",
 "src": [{"o": "investingLive", "d": "2026-10-29", "u": "https://investinglive.com/central-banks/rbnz-s-breman-says-chances-of-a-december-rate-hike-are-high-after-surprise-hold-at-2-75/"},
         {"o": "Newsquawk", "d": "2026-10-29", "u": "https://www.newsquawk.com/headlines/rbnz-governor-breman-says-chances-of-a-december-raye-hike-are-high"},
         {"o": "FXStreet", "d": "2026-10-28", "u": "https://www.fxstreet.com/news/what-can-we-expect-from-the-rbnz-monetary-policy-decision-202610272058"}],
 "inds": ["macro"], "nodes": ["macro/cb"],
 "vc": [{"ind": "macro", "node": "cb", "f": "가격", "dir": "up", "k": "예상", "t": "RBNZ 2.75% 동결 뒤 12월 인상 가능성 높아"}],
 "added": "블룸버그 1건 — 10월 28일 2.75% 깜짝 동결(4대 3) 뒤 브레먼 총재가 12월 인상 가능성을 높게 보고 시장이 약 77%를 반영한 내용이 추가됨",
 "items": [
  it("RBNZ 총재 '12월 금리 인상 가능성 높아'", BB, "2026-10-29", B+"articles/2026-10-29/rbnz-governor-sees-high-chance-of-december-interest-rate-hike",
     "브레먼 뉴질랜드중앙은행 총재가 2.75% 깜짝 동결 다음 날 12월 인상 가능성이 높다고 밝히면서 시장의 12월 인상 확률이 약 77%로 올랐다")]
})

# ---------- G2-046 연준 레포
I.append({
 "cid": "G2-046", "attachTo": "",
 "title": "연준 레포 기반 운영체계 전환, 익숙한 걸림돌에 막혀",
 "one": "\n".join([
  "연준이 레포 기반 운영체계로 옮겨 가는 길이 다시 익숙한 걸림돌에 부딪혔다.",
  "· 연준 이사회 논문은 상설 레포 운영 이용에 낙인 효과가 따른다고 지적했다 (제목 기준)"]),
 "facts": [
  "무엇이: 연준의 레포 기반 운영체계 전환이 익숙한 장애물에 부딪혔다 [제목]",
  "배경: 연준 이사회 FEDS 논문은 상설 레포 운영 이용에 낙인이 따르며 일상 도구로 알리는 소통이 중요하다고 지적했다 [사실]",
  "장애물: 기사가 말한 '익숙한 장애물'이 상설 레포 이용 낙인 문제인지는 확인하지 못했다 [추론]"],
 "basis": "title",
 "check": "기사 내용은 찾지 못함(제목 기준). 상설 레포 낙인 문제는 연준 이사회 FEDS 논문 검색 결과 요약으로 확인",
 "src": [{"o": "연준 이사회 FEDS 논문", "d": "2026", "u": "https://www.federalreserve.gov/econres/feds/files/2026019pap.pdf"}],
 "inds": ["macro"], "nodes": ["macro/cb", "macro/liquidity"],
 "vc": [{"ind": "macro", "node": "cb", "f": "-", "dir": "flat", "k": "예상", "t": "연준 레포 기반 운영체계 전환에 걸림돌"}],
 "fed": [{"k": "", "who": "연준", "role": "연방준비제도", "kind": "관련 뉴스", "stance": "",
          "t": "레포 기반 운영체계 전환이 익숙한 장애물에 부딪혔다", "d": "2026-10-30",
          "u": B+"articles/2026-10-29/fed-s-path-to-a-repo-based-framework-faces-a-familiar-roadblock"}],
 "items": [
  it("연준의 레포 기반 체계 전환, 익숙한 장애물에 직면", BB, "2026-10-30", B+"articles/2026-10-29/fed-s-path-to-a-repo-based-framework-faces-a-familiar-roadblock")]
})

# ---------- G2-053 옴디아
I.append({
 "cid": "G2-053", "attachTo": "",
 "title": "옴디아, 2026년 폴더블폰 AMOLED 출하 2,900만 장으로 44% 증가 전망",
 "one": "\n".join([
  "옴디아가 2026년 폴더블폰용 AMOLED 패널 출하량을 2,900만 장으로 내다봤다.",
  "· 출하량은 전년보다 44% 늘어나는 규모로 제시됐다 (채널 전언)"]),
 "facts": [
  "무엇이: 옴디아는 2026년 폴더블폰용 AMOLED 디스플레이 패널 출하량을 2,900만 장, 전년 대비 44% 증가로 전망했다 [채널]",
  "출처: 하나증권 중국전략이 옴디아 전망을 중국어 원문과 함께 전했다 [채널]"],
 "basis": "channel",
 "check": "1건짜리 구체 수치 텔레그램 글이라 검색 생략(채널 기준)",
 "src": [],
 "inds": ["tech"], "nodes": [],
 "vc": [{"ind": "tech", "node": "devices", "f": "수요", "dir": "up", "k": "예상", "t": "폴더블 AMOLED 출하 2,900만 장 44% 증가 전망"}],
 "items": [
  it("옴디아, 2026년 폴더블 AMOLED 출하 2,900만 장 44%↑ 전망", "텔레그램 하나증권 중국전략", "2026-10-29", "https://t.me/HANAchina/71210")]
})

# ---------- G2-060 말레이시아
I.append({
 "cid": "G2-060", "attachTo": "",
 "title": "말레이시아 2027년 예산안 하원 정책 단계 통과…안와르, 야당 의원 13명과 신임·공급 합의",
 "one": "\n".join([
  "안와르 총리가 야당 의원들과 합의한 뒤 2027년 예산안이 하원 정책 단계를 음성 표결로 통과했다.",
  "· 정부는 베르사투 의원 6명 등 13명과 신임·공급 협약을 맺어 임기 말까지 지지를 확보했다.",
  "· 예산안은 11월 2~26일 위원회 심의를 거쳐 3독회와 상원으로 넘어간다."]),
 "facts": [
  "무엇이: 10월 9일 제출된 2027년 예산안이 10월 29일 하원 정책 단계를 음성 표결로 통과했고, 지난해와 달리 야당의 기록 표결 요구가 없었다 [사실]",
  "합의: 정부는 베르사투 의원 6명과 전 베르사투 의원 6명, 사이드 사딕 의원 등 13명과 신임·공급 협약을 맺었다 [사실]",
  "조건: 의원들은 정부 측과 같은 지역구 개발 예산을 원했고, 총리 임기 최대 2회 제한과 법무장관 권한 분리도 조건으로 거론됐다 [사실]",
  "다음 단계: 위원회 심의는 11월 2~26일이며 이후 3독회와 상원 심의를 거친다 [사실]"],
 "basis": "verified",
 "check": "The Star·Malaysiakini·The Edge 검색 결과 요약으로 정책 단계 통과·13명 협약·위원회 일정 확인",
 "src": [{"o": "The Star", "d": "2026-10-29", "u": "https://www.thestar.com.my/news/nation/2026/10/29/dewan-rakyat-passes-supply-bill-2027-at-policy-stage"},
         {"o": "Malaysiakini", "d": "2026-10-29", "u": "https://www.malaysiakini.com/news/888129-budget-2027-breezes-through-dewan-rakyat-after-csa-signing"},
         {"o": "The Edge Malaysia", "d": "2026-10-29", "u": "https://theedgemalaysia.com/node/823792"}],
 "inds": ["macro"], "nodes": ["macro/fiscal"],
 "vc": [{"ind": "macro", "node": "fiscal", "f": "-", "dir": "flat", "k": "실제", "t": "말레이시아 2027년 예산안 하원 정책 단계 통과"}],
 "items": [
  it("안와르, 야당과 합의해 2027년 예산 관문 넘어", BB, "2026-10-29", B+"articles/2026-10-29/anwar-cuts-a-deal-with-opposition-to-clear-a-2027-budget-hurdle")]
})

# ---------- G2-067 사모펀드
I.append({
 "cid": "G2-067", "attachTo": "",
 "title": "사모펀드 '심한 과대평가' 시대 퇴조…좀비 펀드는 늘어",
 "one": "\n".join([
  "사모펀드 자산을 크게 부풀려 평가하던 시대가 저물고 좀비 펀드가 늘고 있다는 진단이 나왔다.",
  "· 블룸버그 뉴스레터는 이를 '심하게 과대평가된' 사모펀드 시대의 퇴조로 표현했다 (제목 기준)"]),
 "facts": [
  "무엇이: 사모펀드의 '심한 과대평가' 시대가 저물고 좀비 펀드가 늘고 있다 [제목]",
  "범위: 평가 하락 폭과 좀비 펀드 수는 확인하지 못했다 [미확인]"],
 "basis": "title",
 "check": "검색 한도로 별도 확인 안 함, 블룸버그 뉴스레터 제목 기준",
 "src": [],
 "inds": ["fin"], "nodes": [],
 "vc": [{"ind": "fin", "node": "assetmgmt", "f": "가격", "dir": "down", "k": "예상", "t": "사모펀드 과대평가 시대 퇴조·좀비 펀드 증가"}],
 "items": [
  it("사모펀드 '심한 과대평가' 시대 퇴조, 좀비 펀드 증가", BB, "2026-10-30", B+"newsletters/2026-10-29/heard-on-y-all-street-way-over-marked-pe-era-fades-while-zombies-rise")]
})

for x in I:
    x["one"] = "\n".join(l[:-1] if l.endswith(".") else l for l in x["one"].split("\n"))
out = {"agent": "W1", "searches_used": 18, "fetches_used": 2, "items": I,
       "skipped": [{"cid": "G2-026", "reason": "범위 밖(관세·이란 전쟁 비용과 체감 경기 해설 기사 제목뿐, 구체 사실 없음)"}]}
json.dump(out, open('/home/user/news-desk/data/mix-2026-10-30/out2/W1.json', 'w'), ensure_ascii=False, indent=1)
print(len(I))
