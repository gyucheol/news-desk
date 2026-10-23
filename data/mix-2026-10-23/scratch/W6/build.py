import json
OUT = '/home/user/news-desk/data/mix-2026-10-23/out2/W6.json'
D = '2026-10-23'
TG_INS = '텔레그램 미국 주식 인사이더'
TG_COMP = '텔레그램 부의 나침반'
TG_TRIL = '텔레그램 트릴리온'
TG_POL = '텔레그램 Polaristimes'
TG_HANA = '텔레그램 하나증권 중국전략'
B, R = '블룸버그', '로이터'

def it(t, o, u, s=None):
    x = {"t": t, "o": o, "d": D, "u": u}
    if s: x["s"] = s
    return x

items = []

items.append({"cid": "G1-005", "attachTo": "",
 "title": "우크라 스타실드 제한 논란…트럼프, 머스크에 해제 요청에도 시속 161km 제한 여전·美 상원 조사",
 "one": "\n".join([
  "트럼프 대통령이 머스크에게 우크라이나 스타실드 제한 해제를 요청했다는 보도에도 현지 제한은 이어졌다.",
  "· WSJ는 트럼프가 수요일 머스크에게 직접 전화해 제한 해제를 요청했다고 전했다.",
  "· 트럼프는 통화 여부 언급을 피하면서 머스크가 서비스를 복구했다고 말했다.",
  "· 해제 발표 뒤에도 대부분 부대에서 시속 약 161km를 넘는 드론의 통신이 다시 끊겼다.",
  "· 자포리자의 한 드론 조종사는 목요일 밤 작전 한 번에 드론 10대 중 5대를 잃었다고 말했다.",
  "· 민주당 블루먼솔 상원의원은 스타실드 성능 저하 경위 조사에 나서 머스크와 헤그세스에게 서한을 보냈다.",
  "· 카니 캐나다 총리는 우크라이나 전쟁에서의 스타링크 조작이 우려스럽다고 밝혔다."]),
 "facts": [
  "무엇이: WSJ는 트럼프 대통령이 머스크에게 전화해 우크라이나 스타실드 제한 해제를 요청했다고 보도했고, 트럼프는 통화 여부 언급을 피하며 머스크가 서비스를 되돌렸다고 말했다 [사실]",
  "현지 상황: 해제 발표 뒤에도 시속 약 161km를 넘는 드론의 통신이 끊기고 있으며, 우크라이나 당국자도 161km 제한이 여전하다고 말했다 [사실]",
  "피해: 자포리자의 한 드론 조종사는 목요일 밤 작전 한 번에 드론 10대 중 5대를 잃었다고 말했고, 젤렌스키 대변인은 달라진 것이 없다고 지적했다 [채널]",
  "조사: 민주당 리처드 블루먼솔 상원의원이 스타실드 성능 저하 경위 조사에 착수해 머스크와 헤그세스 국방장관에게 서한을 보냈다 [사실]",
  "동맹 반응: 마크 카니 캐나다 총리는 우크라이나 전쟁에서의 스타링크 조작이 캐나다를 우려하게 한다고 말했다 [제목]"],
 "basis": "partial",
 "check": "WSJ 보도·트럼프 발언·161km 제한 지속·블루먼솔 조사는 CNBC·키이우인디펜던트 검색 결과 요약으로 확인, 카니 발언은 제목만 근거",
 "src": [{"o": "CNBC", "d": "2026-10-22", "u": "https://www.cnbc.com/2026/10/22/trump-musk-starlink-ukraine.html"},
         {"o": "키이우인디펜던트", "d": "2026-10-22", "u": "https://kyivindependent.com/us-senator-blumenthal-opens-probe-into-ukraine-starshield-restrictions/"}],
 "inds": ["macro", "tech"], "nodes": ["macro/geo"],
 "vc": [{"ind": "tech", "node": "telecom", "f": "공급", "dir": "down", "k": "실제", "t": "우크라 스타실드 시속 161km 초과 드론 통신 끊김"},
        {"ind": "macro", "node": "geo", "f": "-", "dir": "flat", "k": "예상", "t": "스타실드 제한 경위 두고 미 상원 조사 착수"}],
 "items": [
  it("WSJ '트럼프, 머스크에 전화해 우크라 스타링크 제한 해제 요청'", B, "https://www.bloomberg.com/news/articles/2026-10-22/trump-called-musk-to-lift-starlink-limits-in-ukraine-wsj-says",
     "트럼프 대통령이 머스크에게 직접 전화해 우크라이나 스타링크 제한을 풀어 달라고 했다고 WSJ가 전하면서, 백악관이 해제에 직접 나선 정황이 드러났다 (제목 기준)"),
  it("美 민주당 상원의원, 우크라 스타실드 서비스 상실 경위 조사 착수", R, "https://www.reuters.com/legal/government/us-democratic-senator-probes-ukraines-loss-starshield-service-2026-10-22/",
     "블루먼솔 민주당 상원의원이 우크라이나의 스타실드 서비스 상실 경위 조사에 나서면서, 머스크와 헤그세스 국방장관이 의회 질의를 받게 됐다"),
  it("카니 캐나다 총리 '우크라 전쟁 속 스타링크 조작이 우려스럽다'", B, "https://www.bloomberg.com/news/articles/2026-10-23/mark-carney-says-starlink-manipulation-in-ukraine-war-worries-canada",
     "마크 카니 캐나다 총리가 우크라이나 전쟁에서의 스타링크 조작이 우려스럽다고 밝히면서, 동맹국 안에서도 미국 위성통신 의존 위험이 거론됐다 (제목 기준)"),
  it("해제 발표에도 우크라 스타실드 제한 지속…시속 161km 넘으면 드론 끊겨", TG_INS, "https://t.me/insidertracking/67119",
     "트럼프의 해제 발표에도 우크라이나 대부분 부대에서 시속 약 161km를 넘는 드론 통신이 끊기면서, 한 조종사는 작전 한 번에 드론 10대 중 5대를 잃었다"),
  it("WSJ '트럼프, 머스크에 우크라 스타링크 제한 해제 요청' 로이터 전재", R, "https://www.reuters.com/business/media-telecom/trump-asks-musk-lift-ukraine-starlink-restrictions-wsj-reports-2026-10-22/",
     "트럼프가 머스크에게 우크라이나 스타링크 제한 해제를 요청했다는 WSJ 보도를 로이터가 전하면서, 해제 뒤에도 제한이 남았는지가 쟁점으로 떠올랐다 (제목 기준)")]})

items.append({"cid": "G1-020", "attachTo": "",
 "title": "비만약 확산에 식음료 업계 대응…하이네켄 맥주 판매 우려·단백질 식품 붐·허쉬 단백질 초콜릿 검토",
 "one": "\n".join([
  "비만약(GLP-1) 확산이 맥주와 과자 같은 식음료 수요를 바꾸면서 업체들이 대응에 나섰다.",
  "· 하이네켄은 영국 펍 고객용 자료에서 GLP-1 약물이 포만감과 주문 감소로 맥주 판매를 압박할 수 있다고 경고했다.",
  "· 하이네켄은 펍들에 하프 파인트와 저알코올·무알코올 음료 판촉을 권했다.",
  "· 비만약 확산으로 단백질 식품 붐이 일면서 소비자 검증도 강해지고 있다.",
  "· 허쉬 CEO는 마스에 맞서 단백질·건강 지향 초콜릿을 검토하고 있다."]),
 "facts": [
  "무엇이: 하이네켄이 이달 영국 외식업 고객에게 보낸 자료에서 GLP-1 약물이 맥주·사이다 판매를 압박할 수 있다며 하프 파인트·저알코올 음료 판촉을 권했다 [사실]",
  "업계 시각: 디아지오는 GLP-1 영향이 관리 가능하다고 했고, 칼스버그는 기존 데이터가 아직 약물을 맥주 소비 추세의 뚜렷한 원인으로 뒷받침하지 않는다고 봤다 [사실]",
  "규모: JP모건 조사로는 지난해 미국에서 약 1,000만 명이 오젬픽·위고비 같은 약을 썼다 [사실]",
  "식품: 비만약이 단백질 식품 붐을 불러 소비자 검증이 강화되고 있으며, 허쉬 CEO는 마스에 맞서 단백질·건강 지향 초콜릿을 검토한다 [제목]"],
 "basis": "partial",
 "check": "하이네켄 자료 내용은 키프로스메일·ESM 등 검색 결과 요약으로 확인, 단백질 식품 붐과 허쉬 검토는 제목만 근거",
 "src": [{"o": "키프로스메일", "d": "2026-10-23", "u": "https://cyprus-mail.com/2026/10/23/heineken-warns-weight-loss-drugs-could-hit-beer-sales-in-british-pubs"},
         {"o": "ESM매거진", "d": "2026-10-23", "u": "https://www.esmmagazine.com/drinks/heineken-document-reveals-worries-over-weight-loss-drugs-and-beer-sales-324410"}],
 "inds": ["consumer", "pharma"], "nodes": [],
 "vc": [{"ind": "consumer", "node": "alcohol", "f": "수요", "dir": "down", "k": "예상", "t": "비만약 확산에 맥주 판매 감소 우려"},
        {"ind": "consumer", "node": "food", "f": "수요", "dir": "up", "k": "실제", "t": "비만약 확산에 단백질 식품 붐"}],
 "items": [
  it("하이네켄 내부 문서, 비만약이 맥주 판매에 미칠 영향 우려 드러나", R, "https://www.reuters.com/legal/litigation/heineken-document-reveals-worries-over-weight-loss-drugs-beer-sales-2026-10-23/",
     "하이네켄이 영국 펍 고객용 자료에서 GLP-1 약물이 맥주·사이다 판매를 줄일 수 있다고 경고하면서, 하프 파인트·저알코올 음료 판촉을 권했다"),
  it("허쉬 CEO, 마스에 맞서 단백질·건강 지향 초콜릿 검토", B, "https://www.bloomberg.com/news/features/2026-10-23/hershey-ceo-fights-back-mars-mulls-protein-and-better-for-you-chocolates",
     "허쉬 CEO가 마스와의 경쟁에 맞서 단백질·건강 지향 초콜릿을 검토하면서, 건강 수요에 맞춰 과자 제품 구성을 바꿀 수 있다 (제목 기준)"),
  it("비만약이 단백질 식품 붐 불러…소비자 검증도 한층 강화", R, "https://www.reuters.com/legal/litigation/weight-loss-drugs-fuel-protein-boom-with-more-consumer-scrutiny-2026-10-23/",
     "비만약 확산이 단백질 식품 붐을 일으키면서, 소비자들이 단백질 제품의 성분과 효과를 더 꼼꼼히 따지기 시작했다 (제목 기준)")]})

items.append({"cid": "G1-024", "attachTo": "",
 "title": "美 재무부 COINS법 규칙안…AI 투자 금지 확대·HBM 등 반도체·바이오 추가, 베네수엘라 제외",
 "one": "\n".join([
  "미국 재무부가 COINS법 시행 규칙안을 내고 우려국 첨단기술 대외투자 제한을 넓히기로 했다.",
  "· AI 분야는 신고 후 가능하던 일부 투자까지 금지 거래로 바뀐다.",
  "· 반도체는 HBM·광자 칩·방사선 내성 칩이 더 엄격한 규제 대상에 들어간다.",
  "· 생명공학이 새 규제 분야로 추가돼 뇌·컴퓨터 인터페이스 등이 포함된다.",
  "· 재무부는 마두로 정부가 더는 없다며 제한 대상국에서 베네수엘라를 뺐다.",
  "· 규칙안은 12월 7일까지 의견을 받으며 아직 발효되지 않았다."]),
 "facts": [
  "무엇이: 미국 재무부는 10월 22일 COINS법 시행 규칙안을 내고 반도체·양자·AI·고성능 컴퓨팅·극초음속·생명공학 분야 우려국 투자 규제를 제안했다 [사실]",
  "AI: 현행 규정상 신고 후 진행할 수 있던 일부 AI 투자까지 금지 거래로 바뀐다 [사실]",
  "반도체·바이오: HBM·광자 칩·방사선 내성 칩이 더 엄격한 규제 대상이 되고 뇌·컴퓨터 인터페이스·자동화 실험실 소프트웨어가 새로 포함되며, 투자자 실사 의무도 강화된다 [채널]",
  "대상국: 재무부는 1월 마두로 체포 뒤 그 정부가 더는 없다며 베네수엘라를 제한 대상국에서 뺐다 [사실]",
  "일정: 의견 수렴은 12월 7일까지이며 발효일은 최종 규칙에서 정한다 [사실]"],
 "basis": "verified",
 "check": "규칙안 발표·AI 금지·바이오 추가·베네수엘라 제외·의견 기한은 재무부 보도자료·바이오팜인터내셔널 검색 결과 요약으로 확인, HBM 등 세부 칩은 채널 기준",
 "src": [{"o": "미 재무부", "d": "2026-10-22", "u": "https://home.treasury.gov/news/press-releases/sb0667/"},
         {"o": "바이오팜인터내셔널", "d": "2026-10-22", "u": "https://www.biopharminternational.com/view/treasury-proposes-adding-biotech-to-outbound-investment-restrictions-under-coins-act"}],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "vc": [{"ind": "macro", "node": "geo", "f": "공급", "dir": "down", "k": "예상", "t": "AI·반도체·바이오 대외투자 제한 확대안"}],
 "items": [
  it("美 재무부, 대외투자 제한 대상국 명단에서 베네수엘라 제외", R, "https://www.reuters.com/world/us-treasury-drops-venezuela-countries-facing-outbound-us-investment-restrictions-2026-10-22/",
     "미국 재무부가 대외투자 제한 대상국에서 베네수엘라를 빼면서, 미국인의 베네수엘라 첨단기술 투자는 이 규제를 받지 않게 된다"),
  it("글로벌 브리핑: 美 재무부, 우려국 AI·반도체 투자 제한 규정 제안", TG_INS, "https://t.me/insidertracking/67088",
     "미국 재무부가 특정 외국의 AI·반도체 산업에 대한 미국인 투자를 제한하는 새 규정을 제안하면서, 대중국 기술 투자 통제가 넓어질 수 있다"),
  it("COINS법 규칙안, AI 금지 확대·HBM 등 반도체·생명공학 규제 추가", TG_INS, "https://t.me/insidertracking/67111",
     "재무부 COINS법 규칙안이 일부 AI 투자를 금지 거래로 바꾸고 HBM·광자 칩과 생명공학을 규제에 넣으면서, 투자자의 실사 의무도 무거워진다")]})

items.append({"cid": "G1-036", "attachTo": "",
 "title": "북미 석유 M&A 활발…데본에너지 인수 후보 5곳 거론·NGP '캐나다 M&A 사상 최고'",
 "one": "\n".join([
  "북미 석유·가스 업계의 인수합병 움직임이 미국 셰일과 캐나다에서 함께 활발해지고 있다.",
  "· 블룸버그는 데본에너지를 인수할 수 있는 후보 5곳을 짚었다.",
  "· NGP의 크리스 카터는 캐나다에서 사상 최고 수준의 M&A가 이뤄져 출구 시장이 활짝 열렸다고 말했다.",
  "· 카터는 몬트니·듀버네 지역의 단일 유정 수익률이 퍼미안과 견줄 만하다고 봤다 (채널 전언)"]),
 "facts": [
  "무엇이: 블룸버그는 데본에너지의 잠재 인수자 5곳을 다뤘다 [제목]",
  "캐나다: NGP 매니징 파트너 크리스 카터는 캐나다에서 사상 최고 수준의 M&A가 이뤄져 출구 전략 시장이 열려 있다고 말했다 [채널]",
  "유정 수익률: 카터는 몬트니·듀버네를 단일 유정 수익률 면에서 '캐나다의 퍼미안'과 비교할 수 있다고 했다 [채널]"],
 "basis": "channel",
 "check": "검색 한도 배분상 검색 생략(텔레그램 인용이 구체적), 데본 인수 후보 이름은 제목에 없어 쓰지 않음",
 "src": [],
 "inds": ["oil", "gas"], "nodes": ["gas/upstream"],
 "vc": [{"ind": "oil", "node": "nonopec", "f": "공급", "dir": "down", "k": "예상", "t": "데본에너지 인수 후보 5곳 거론되며 셰일 통합 관측"}],
 "items": [
  it("데본에너지 M&A: 주목할 만한 잠재 인수자 5곳", B, "https://www.bloomberg.com/news/articles/2026-10-22/devon-energy-dvn-m-a-5-potential-buyers-to-watch",
     "블룸버그가 데본에너지를 인수할 수 있는 후보 5곳을 짚으면서, 미국 셰일 업계의 통합이 이어질 수 있다는 관측이 나왔다 (제목 기준)"),
  it("NGP '캐나다 M&A 사상 최고…몬트니는 캐나다의 퍼미안'", TG_TRIL, "https://t.me/Trillion_labs/11144",
     "NGP의 크리스 카터가 캐나다 M&A가 사상 최고 수준이라 출구 시장이 열렸다고 말하면서, 몬트니·듀버네를 퍼미안급 유정 수익 지역으로 평가했다")]})

items.append({"cid": "G1-046", "attachTo": "",
 "title": "로보택시 유럽 진출…볼트·스텔란티스 2028년 파리 시험 계획·바이두, 런던 도로 시험 운행",
 "one": "\n".join([
  "유럽 대도시에서 차량호출 업체와 완성차·중국 기술사의 로보택시 시험이 잇따르고 있다.",
  "· 볼트·스텔란티스는 파리 수도권과 함께 2028년 자율주행 차량호출 시험을 시작할 계획이다.",
  "· 두 회사는 인허가를 전제로 2030년 파리 수도권 상업 운행을 노린다.",
  "· 바이두는 리프트 자회사 프리나우와 런던 도로에서 RT6 로보택시를 시험하고 있다.",
  "· 바이두와 프리나우는 규제 승인을 전제로 2027년 런던 무인 로보택시 서비스를 목표로 한다."]),
 "facts": [
  "무엇이: 볼트·스텔란티스·파리 수도권은 2028년 자율주행 차량호출 시험을 시작해 인허가를 전제로 2030년 상업 운행을 노린다 [사실]",
  "파리 세부: 초기 운행은 북서부 최대 5개 기초자치단체에서 하며 스텔란티스가 차량을, 볼트가 서비스를 맡고 포니AI는 기술 공급 후보다 [사실]",
  "런던: 바이두는 프리나우와 7월부터 런던 브렌트구에서 안전요원이 탄 RT6 차량을 시험 중이며 2027년 무인 서비스를 목표로 한다 [사실]",
  "경쟁: 우버·웨이브는 9월 런던에서 안전요원 탑승 로보택시를 시작했고 웨이모는 연내 런던 완전 무인 서비스를 노린다 [사실]"],
 "basis": "verified",
 "check": "두 계획 모두 일렉트릭비히클스·테크크런치·플리트포인트 검색 결과 요약으로 확인",
 "src": [{"o": "eletric-vehicles.com", "d": "2026-10-23", "u": "https://eletric-vehicles.com/stellantis/bolt-plans-paris-robotaxi-pilot-with-stellantis-from-2028-eyes-pony-ai/"},
         {"o": "테크크런치", "d": "2026-07-28", "u": "https://techcrunch.com/2026/07/28/lyft-and-baidu-enter-londons-robotaxi-battleground-as-testing-begins/"}],
 "inds": ["auto"], "nodes": [],
 "vc": [{"ind": "auto", "node": "autonomy", "f": "공급", "dir": "up", "k": "예상", "t": "볼트·스텔란티스 2028년 파리 로보택시 시험"}],
 "items": [
  it("볼트·스텔란티스, 2028년 파리 수도권 자율주행 시험 계획", R, "https://www.reuters.com/world/china/bolt-stellantis-plan-autonomous-driving-experiment-greater-paris-2028-2026-10-23/",
     "볼트와 스텔란티스가 파리 수도권과 2028년 자율주행 차량호출 시험을 계획하면서, 인허가를 전제로 2030년 상업 운행을 노린다"),
  it("中 바이두, 런던 도로에서 로보택시 시험 운행 진행", R, "https://www.reuters.com/business/finance/chinas-baidu-tests-robotaxi-london-streets-2026-10-23/",
     "바이두가 리프트 자회사 프리나우와 런던 도로에서 RT6 로보택시를 시험하면서, 2027년 런던 무인 서비스 경쟁에 뛰어들었다")]})

items.append({"cid": "G1-056", "attachTo": "n-bbg-0350",
 "title": "최강 엘니뇨 피해 확산…중남미 폭우로 칠레 구리·농작물 위협, 파나마운하 36→32척·인도 설탕 에탄올 중단",
 "one": "\n".join([
  "한 세대 만의 가장 강한 엘니뇨 피해가 운하·광산·농산물 공급에 이어 중남미 폭우로 번지고 있다.",
  "· 멕시코에서 칠레까지 폭우가 이어지며 칠레 구리 생산과 농작물이 위협받고 있다.",
  "· 파나마운하 하루 통과 선박이 36척에서 32척으로 줄고 갑문 경매가는 80만 달러에서 250만 달러로 뛰었다.",
  "· 칠레 구리광산이 멈췄고 인도 몬순은 13% 부족했다.",
  "· 인도는 2026~27년 설탕의 에탄올 전용을 막고 옥수수·쌀 원료 에탄올 110억 리터를 입찰했다.",
  "· 인도 순 설탕 생산 전망은 3,100만 톤에서 2,800만 톤으로 낮아졌다.",
  "· 미 기후예측센터는 1~3월에도 강한 엘니뇨가 이어지고 중립은 6월께에야 온다고 봤다."]),
 "facts": [
  "무엇이: 엘니뇨 폭우가 멕시코에서 칠레까지 중남미를 덮쳐 파라과이 홍수, 아르헨티나 농장 노동자 2명 사망, 페루·멕시코 해안 피해가 났고 칠레는 10월 20일 산티아고 수도권에 적색경보를 냈다 [사실]",
  "칠레: 엘니뇨 폭풍이 칠레 구리와 농작물을 위협하며, 수확기 비는 중부 와인 산지의 병해와 과일 품질 저하를 부를 수 있다 [제목]",
  "인도 설탕: 인도는 2026~27년 설탕의 에탄올 전용을 막고 옥수수·쌀 원료 에탄올 약 110억 리터를 입찰했으며, ISMA는 순 설탕 생산을 3,100만 톤에서 2,800만 톤으로 낮춰 봤다 [사실]",
  "운하·광산: 파나마운하는 하루 통과 선박을 36척에서 32척으로 줄였고 갑문 경매가는 약 80만 달러에서 250만 달러로 뛰었으며, 칠레 로스펠람브레스 구리광산이 멈추고 인도 몬순은 13% 부족했다 [채널]",
  "팜유·전망: 인도네시아 팜 농가가 가뭄으로 고립됐고, 미 기후예측센터는 1~3월에도 강한 엘니뇨가 이어지고 중립은 6월께 올 것으로 봤다 [채널]"],
 "basis": "partial",
 "check": "중남미 폭우 피해(파라과이 홍수·아르헨티나 2명 사망·칠레 적색경보)는 더프린트·비즈니스월드 검색 결과 요약으로 확인, 칠레 구리 피해는 블룸버그 제목과 6월 전망 기사뿐이라 실제 감산은 확인 못 함",
 "src": [{"o": "더프린트", "d": "2026-10-22", "u": "https://theprint.in/world/el-nino-rains-batter-latin-america-from-mexico-to-chile/3079230/"},
         {"o": "비즈니스월드", "d": "2026-10-23", "u": "https://bworldonline.com/world/2026/10/23/788858/el-nino-rains-batter-latin-america-from-mexico-to-chile/"}],
 "inds": ["agri", "metals"], "nodes": [],
 "vc": [{"ind": "agri", "node": "weather", "f": "공급", "dir": "down", "k": "실제", "t": "엘니뇨 폭우로 중남미 농작물 피해"},
        {"ind": "metals", "node": "copper", "f": "공급", "dir": "down", "k": "예상", "t": "엘니뇨 폭풍에 칠레 구리 생산 위협"}],
 "added": "블룸버그·로이터 2건 — 엘니뇨 폭우가 멕시코~칠레 중남미를 덮쳐 칠레 구리·농작물 위협, 파라과이 홍수·칠레 적색경보 내용이 추가됨",
 "items": [
  it("칠레: 엘니뇨 폭풍, 구리 생산과 농작물을 위협", B, "https://www.bloomberg.com/news/articles/2026-10-22/chile-tormentas-de-el-nino-amenazan-el-cobre-y-los-cultivos-mvjo9iw8",
     "엘니뇨가 몰고 온 폭풍이 칠레를 덮치면서, 칠레의 구리 생산과 농작물 수확이 함께 위협받고 있다 (제목 기준)"),
  it("엘니뇨 폭우, 멕시코에서 칠레까지 중남미 곳곳 강타", R, "https://www.reuters.com/business/environment/el-nio-rains-batter-latin-america-mexico-chile-2026-10-22/",
     "엘니뇨 폭우가 멕시코에서 칠레까지 중남미를 강타하면서, 파라과이 홍수와 아르헨티나 농장 노동자 2명 사망, 칠레 산티아고 적색경보가 이어졌다")]})

items.append({"cid": "G1-060", "attachTo": "n-tg-0662",
 "title": "미국 구리 재고 쏠림…LME 미국 창고 16.9만 톤 2014년 이후 최고·COMEX 72만 톤 사상 최고",
 "one": "\n".join([
  "관세 위협으로 미국에 쌓인 구리 재고가 LME 미국 창고와 COMEX 모두에서 기록적 수준으로 불었다.",
  "· LME 미국 창고 구리 재고는 16만 9,475톤으로 2014년 4월 이후 최고이며 LME 전체의 약 62%다.",
  "· COMEX 구리 재고는 23일 연속 늘어 72만 712톤으로 사상 최고를 경신했다.",
  "· 미국 구리 재고는 160만 톤으로 세계 가시재고의 약 70%에 이른다.",
  "· 미국향 차익은 톤당 3,000달러 이상에서 약 310달러로 줄어 추가 유입 유인은 약해졌다.",
  "· 미 상무부는 정제 구리에 2027년 15%, 2028년 30% 관세안을 제안했지만 부과 여부는 아직 밝히지 않았다 (채널 전언)"]),
 "facts": [
  "무엇이: LME 미국 창고 구리 재고가 16만 9,475톤으로 2014년 4월 이후 최고를 기록했고, LME 전체의 약 62%로 대부분 뉴올리언스·볼티모어에 있다 [채널]",
  "COMEX: COMEX 구리 재고는 23일 연속 늘어 72만 712톤으로 사상 최고다 [채널]",
  "규모·차익: 관세 위협으로 미국에 쌓인 구리는 160만 톤으로 세계 가시재고의 약 70%이고, 미국향 차익은 톤당 3,000달러 이상에서 약 310달러로 줄었다 [채널]",
  "관세안: 미 상무부는 정제 구리에 2027년부터 15%, 2028년 30% 추가 관세를 매기는 안을 제안했으나 부과 여부는 발표하지 않았다 [채널]",
  "전망: 추가 유입 유인은 약해졌지만 이미 쌓인 재고는 미국에 머물 수 있다 [채널]"],
 "basis": "channel",
 "check": "검색 한도 배분상 별도 확인 생략, 텔레그램 글이 로이터를 출처로 밝힘",
 "src": [],
 "inds": ["metals"], "nodes": [],
 "vc": [{"ind": "metals", "node": "copper", "f": "공급", "dir": "up", "k": "실제", "t": "미국 COMEX 구리 재고 72만 톤 사상 최고"}],
 "added": "텔레그램 1건 — LME 미국 창고 재고 16만 9,475톤(2014년 이후 최고)·COMEX 72만 712톤 사상 최고, 정제 구리 15~30% 관세안 내용이 추가됨",
 "items": [
  it("LME 미국 창고 구리 재고 16.9만 톤, 2014년 이후 최고…COMEX 72만 톤", TG_TRIL, "https://t.me/Trillion_labs/11142",
     "LME 미국 창고 구리 재고가 2014년 4월 이후 최고인 16만 9,475톤으로 늘고 COMEX 재고도 72만 712톤으로 사상 최고를 찍으면서, 미국 쏠림이 이어졌다")]})

items.append({"cid": "G1-070", "attachTo": "",
 "title": "뉴몬트 3분기 조정 주당순이익 2.20달러로 예상 상회…금값 상승에 매출 15%↑",
 "one": "\n".join([
  "뉴몬트가 금값 상승에 힘입어 3분기 이익이 시장 예상을 웃돌았다.",
  "· 조정 순이익은 23억 1,000만 달러, 주당 2.20달러로 예상치 1.95달러를 넘었다.",
  "· 매출은 63억 6,000만 달러로 15% 늘었고 잉여현금흐름은 19억 1,000만 달러였다."]),
 "facts": [
  "무엇이: 뉴몬트는 10월 22일 3분기 조정 순이익 23억 1,000만 달러, 주당 2.20달러를 발표했다 [사실]",
  "예상 대비: 인베스팅닷컴 집계 예상치 주당 1.95달러를 웃돌았다 [사실]",
  "매출·현금: 매출은 63억 6,000만 달러로 전년 55억 2,000만 달러보다 15% 늘었고 잉여현금흐름은 19억 1,000만 달러였다 [사실]",
  "금값: 실현 금값은 온스당 평균 4,317달러였고 회사는 연간 생산 목표 달성을 유지했다 [사실]"],
 "basis": "verified",
 "check": "뉴몬트 SEC 8-K·인베스팅닷컴 실적 기사 검색 결과 요약으로 확인",
 "src": [{"o": "뉴몬트 8-K(SEC)", "d": "2026-10-22", "u": "https://www.sec.gov/Archives/edgar/data/0001164727/000116472726000041/newmontq32026earningsrelea.htm"},
         {"o": "인베스팅닷컴", "d": "2026-10-23", "u": "https://www.investing.com/news/transcripts/earnings-call-transcript-newmont-beats-q3-2026-estimates-as-cash-flow-hits-record-93CH-4967771"}],
 "inds": ["metals"], "nodes": [],
 "vc": [{"ind": "metals", "node": "precious", "f": "가격", "dir": "up", "k": "실제", "t": "실현 금값 온스당 4,317달러로 이익 예상 상회"}],
 "items": [it("뉴몬트, 금값 상승에 힘입어 분기 이익 예상 상회", R, "https://www.reuters.com/business/newmont-beats-quarterly-profit-estimates-higher-gold-prices-2026-10-22/")]})

items.append({"cid": "G1-080", "attachTo": "",
 "title": "멕시코 빔보, 연간 EBITDA 마진 전망 하단 60→85bp 상향…3분기 순이익 22%↑",
 "one": "\n".join([
  "멕시코 제빵업체 빔보가 3분기 호실적에 연간 조정 EBITDA 마진 전망 하단을 높였다.",
  "· 마진 확대 폭 전망 하단은 60bp에서 85bp로 올랐고 상단 120bp는 그대로다.",
  "· 3분기 순이익은 22% 늘었고 조정 EBITDA 마진은 15.7%로 100bp 개선됐다."]),
 "facts": [
  "무엇이: 빔보는 10월 22일 3분기 실적과 함께 올해 조정 EBITDA 마진 확대 전망 하단을 60bp에서 85bp로 높이고 상단 120bp는 유지했다 [사실]",
  "3분기: 순이익은 전년보다 22% 늘고 환율 효과를 뺀 순매출은 3.6% 늘었으며, 조정 EBITDA 마진은 15.7%였다 [사실]",
  "유지: 한 자릿수 중반 매출 증가 전망과 10억~20억 달러 설비투자 계획은 그대로다 [사실]",
  "위험: 경영진은 2027년 멕시코·북미의 물가 부담을 경고했다 [사실]"],
 "basis": "verified",
 "check": "구루포커스·트레이더스유니언 검색 결과 요약으로 확인",
 "src": [{"o": "구루포커스", "d": "2026-10-23", "u": "https://www.gurufocus.com/news/9138476/grupo-bimbo-bmboy-raises-fullyear-ebitda-margin-guidance-following-strong-q3-2026-results"},
         {"o": "트레이더스유니언", "d": "2026-10-23", "u": "https://tradersunion.com/news/companies/show/3936335-grupo-bimbo-raises-ebitda-margin/"}],
 "inds": ["consumer"], "nodes": [],
 "vc": [{"ind": "consumer", "node": "food", "f": "가격", "dir": "up", "k": "실제", "t": "빔보 조정 EBITDA 마진 15.7%로 100bp 개선"}],
 "items": [it("멕시코 빔보, 연간 EBITDA 전망 하단을 상향 조정", R, "https://www.reuters.com/business/retail-consumer/mexicos-bimbo-lifts-lower-end-full-year-ebitda-outlook-2026-10-22/")]})

items.append({"cid": "G1-090", "attachTo": "",
 "title": "英 데버넘스 그룹, 5년 만에 세전 흑자 2,830만 파운드…추가 비용 절감 예고",
 "one": "\n".join([
  "옛 부후 그룹인 데버넘스 그룹이 8월까지 6개월 동안 5년 만에 세전 흑자를 냈다.",
  "· 세전이익은 2,830만 파운드였지만 약 4,000만 파운드의 일회성 리스 이익이 포함됐다.",
  "· 매출은 3% 줄었고, 회사는 다음 회계연도에 추가로 큰 비용 절감을 예고했다."]),
 "facts": [
  "무엇이: 데버넘스 그룹은 8월 31일까지 6개월 세전이익 2,830만 파운드로 전년 1,790만 파운드 손실에서 2021년 이후 첫 흑자를 냈다 [사실]",
  "일회성: 미국 물류센터 관련 약 4,000만 파운드 비현금 리스 이익을 빼면 세전손실은 약 5,200만 파운드에서 1,200만 파운드로 줄었다 [사실]",
  "영업: 매출은 3% 줄어 4억 960만 파운드였고 조정 EBITDA는 14.6% 늘어 2,400만 파운드였다 [사실]",
  "비용·부채: 고정비 1억 파운드 절감을 추진하며 다음 회계연도 추가 비용 절감을 예상하고, 순부채는 9,850만 파운드로 줄었다 [사실]"],
 "basis": "verified",
 "check": "리테일가제트·드레이퍼스 검색 결과 요약으로 확인",
 "src": [{"o": "리테일가제트", "d": "2026-10-23", "u": "https://www.retailgazette.co.uk/blog/2026/10/debenhams-group-returns-to-profit-for-first-time-in-five-years-as-turnaround-accelerates/"},
         {"o": "드레이퍼스", "d": "2026-10-23", "u": "https://www.drapersonline.com/news/debenhams-group-swings-to-first-pre-tax-profit-in-five-years"}],
 "inds": ["consumer"], "nodes": [],
 "vc": [{"ind": "consumer", "node": "retail", "f": "수요", "dir": "down", "k": "실제", "t": "데버넘스 그룹 매출 3% 감소 속 비용 절감으로 흑자"}],
 "items": [it("英 데버넘스, 5년 만에 흑자 전환…추가 비용 절감 예상", R, "https://www.reuters.com/business/retail-consumer/uks-debenhams-returns-profit-after-five-years-expects-further-cost-cuts-2026-10-23/")]})

items.append({"cid": "G1-100", "attachTo": "",
 "title": "사우디 알두와드미 미사일 공장 확장…연구진 '더 강력한 고체연료 미사일 생산 가능'",
 "one": "\n".join([
  "미국 연구진이 사우디가 미사일 공장을 넓혀 더 강력한 미사일을 만들 수 있다고 분석했다.",
  "· 리야드 서쪽 약 200km 알두와드미 공장에 기존의 두 배 이상인 새 주조 시설이 들어서고 있다.",
  "· 연구진은 이르면 연말 생산이 가능하다고 봤고, 사우디는 그런 계획을 부인했다."]),
 "facts": [
  "무엇이: 외교정책연구소(FPRI) 연구진은 2025년 4월~2026년 9월 위성사진을 분석해 사우디가 알두와드미 탄도미사일 공장을 더 큰 고체연료 미사일용으로 넓히고 있다고 봤다 [사실]",
  "규모: 새 건물은 연료 주조 피트를 담은 것으로 보이며 기존 주조 건물의 최소 두 배 크기다 [사실]",
  "시점: 연구진은 이르면 올해 말 생산 준비가 될 수 있다고 봤다 [사실]",
  "반응: 사우디는 그런 계획이 없다고 부인했고, 미·사우디 민간 원자력 협정에 대한 미 의회 반대 가능성도 거론된다 [사실]"],
 "basis": "verified",
 "check": "타임스오브이스라엘·bdnews24 검색 결과 요약으로 확인",
 "src": [{"o": "타임스오브이스라엘", "d": "2026-10-23", "u": "https://www.timesofisrael.com/liveblog_entry/saudi-missile-plant-expansion-may-produce-more-powerful-missiles-researchers-say"},
         {"o": "bdnews24", "d": "2026-10-23", "u": "https://bdnews24.com/world/middle-east/tqrbo1v3p9"}],
 "inds": ["aero", "macro"], "nodes": ["macro/geo"],
 "vc": [{"ind": "aero", "node": "munitions", "f": "공급", "dir": "up", "k": "예상", "t": "사우디 고체연료 미사일 생산 확대 가능성"}],
 "items": [it("연구 '사우디 미사일 공장 확장, 더 강력한 미사일 생산 가능'", R, "https://www.reuters.com/world/middle-east/saudi-missile-plant-expansion-may-produce-more-powerful-missiles-study-says-2026-10-23/")]})

items.append({"cid": "G2-003", "attachTo": "",
 "title": "유로존 10월 PMI 51.9로 4개월 최저·독일 서비스 둔화…ECB 12월 인상 전망·기대물가 상승",
 "one": "\n".join([
  "유로존 10월 경기가 프랑스 소요와 비용 상승 속에 둔화했지만 ECB 인상 전망은 이어졌다.",
  "· 유로존 10월 종합 PMI는 51.9로 9월 53.1에서 내려 4개월 최저를 기록했다.",
  "· 프랑스 서비스업이 다시 위축되며 프랑스 민간 부문 산출이 수축으로 돌아섰다.",
  "· 독일 종합 PMI는 서비스업 부진에 52.8로 예상치 53.3을 밑돌았다.",
  "· ECB 조사에서 9월 소비자 기대인플레이션은 소폭 올랐다.",
  "· 이코노미스트들은 ECB가 동결 뒤 12월에 금리 인상을 재개할 것으로 봤다.",
  "· 파네타 ECB 위원은 국채금리 상승이 경기를 억제할 것이라고 말했다."]),
 "facts": [
  "무엇이: 유로존 10월 HCOB 종합 PMI 속보치는 51.9로 9월 53.1과 예상치 52.7을 밑돌아 4개월 최저였다 [사실]",
  "국가별: 프랑스는 서비스업 재위축으로 민간 산출이 수축했고, 독일 종합 PMI는 52.8로 예상 53.3을 밑돌았으며 서비스 PMI는 51.7이었다 [사실]",
  "비용: 에너지 비용 상승에 투입 비용 물가 오름폭이 커졌고 판매가 물가는 둔화했다 [사실]",
  "ECB: 이코노미스트들은 동결 뒤 12월 인상을 예상했고, ECB 조사에서 9월 소비자 기대인플레이션은 소폭 올랐다 [제목]",
  "파네타: 파네타 ECB 위원은 국채금리 상승이 경기를 억제할 것이라고 말했다 [제목]"],
 "basis": "partial",
 "check": "PMI 수치는 FX스트리트·S&P글로벌·인베스팅라이브 검색 결과 요약으로 확인, ECB 12월 인상 전망·기대인플레이션·파네타 발언은 제목만 근거",
 "src": [{"o": "FX스트리트", "d": "2026-10-23", "u": "https://www.fxstreet.com/news/eurozone-hcob-composite-pmi-declines-to-519-in-october-vs-527-expected-202610230806"},
         {"o": "인베스팅라이브", "d": "2026-10-23", "u": "https://investinglive.com/news/eurozone-october-pmi-misses-estimates-as-growth-slows-keeping-ecb-rate-hike-dilemma-alive/"}],
 "inds": ["macro"], "nodes": ["macro/growth", "macro/cb"],
 "vc": [{"ind": "macro", "node": "growth", "f": "수요", "dir": "down", "k": "실제", "t": "유로존 10월 종합 PMI 51.9로 4개월 최저"},
        {"ind": "macro", "node": "cb", "f": "가격", "dir": "up", "k": "예상", "t": "ECB 동결 뒤 12월 금리 인상 전망"}],
 "items": [
  it("ECB 파네타 '국채금리 상승이 경기를 억제할 것'", B, "https://www.bloomberg.com/news/articles/2026-10-22/ecb-s-panetta-says-rising-bond-yields-will-restrain-economy",
     "파네타 ECB 위원이 국채금리 상승이 경기를 억제할 것이라고 말하면서, 시장금리가 추가 긴축 일부를 대신할 수 있다는 시각을 드러냈다 (제목 기준)"),
  it("이코노미스트들 'ECB, 동결 뒤 12월에 금리 인상할 것'", B, "https://www.bloomberg.com/news/articles/2026-10-23/ecb-set-to-raise-rates-in-december-after-pause-economists-say",
     "이코노미스트들이 ECB가 이번 동결 뒤 12월에 금리를 올릴 것으로 보면서, 유로존 긴축 재개 기대가 이어졌다 (제목 기준)"),
  it("독일 기업활동, 서비스업 탓에 예상보다 크게 둔화", B, "https://www.bloomberg.com/news/articles/2026-10-23/german-business-activity-slows-more-than-expected-on-services",
     "독일 10월 기업활동이 서비스업 부진으로 예상보다 크게 둔화하면서, 종합 PMI가 52.8로 예상치 53.3을 밑돌았다"),
  it("독일 10월 기업활동 성장세 약화, PMI 조사 결과", R, "https://www.reuters.com/world/europe/german-business-activity-growth-softens-october-pmi-shows-2026-10-23/",
     "독일 10월 PMI에서 제조업과 서비스업 성장이 함께 느려지면서, 서비스 PMI는 51.7로 예상치 52.5에 못 미쳤다"),
  it("프랑스 소요 여파에 유로존 기업활동 둔화", B, "https://www.bloomberg.com/news/articles/2026-10-23/euro-zone-business-activity-slowed-as-france-unrest-weighs",
     "프랑스 파업·소요가 서비스업을 끌어내리면서 유로존 종합 PMI가 51.9로 떨어졌고, 프랑스 민간 산출은 수축으로 돌아섰다"),
  it("ECB '9월 소비자 기대인플레이션 소폭 상승'", B, "https://www.bloomberg.com/news/articles/2026-10-23/ecb-says-consumers-inflation-expectations-edge-up-in-september",
     "ECB 소비자 기대 조사에서 9월 기대인플레이션이 소폭 오르면서, 12월 인상론에 힘을 보탤 수 있다 (제목 기준)"),
  it("유로존 성장 4개월 최저로 둔화…비용 상승·프랑스 혼란 겹쳐", R, "https://www.reuters.com/world/europe/euro-zone-growth-slows-4-month-low-amid-rising-costs-french-turmoil-pmi-shows-2026-10-23/",
     "유로존 10월 종합 PMI가 4개월 최저인 51.9로 내려가면서, 에너지발 투입 비용 상승과 프랑스 혼란이 성장을 눌렀다")]})

items.append({"cid": "G2-015", "attachTo": "",
 "title": "코스피 선행 PER 4.2배로 세계 최저 수준…예탁금 90조 원 하회·레버리지 ETF 개인 손실 6.3조 원",
 "one": "\n".join([
  "기술주 급락 뒤 한국 증시가 세계에서 가장 싼 시장이 되고 투자 심리도 크게 얼어붙었다.",
  "· 코스피 12개월 선행 PER은 4.2배로 시총 1조 달러 이상 시장 가운데 2006년 이후 처음 5배를 밑돌았다.",
  "· 코스피는 6월 고점 대비 약 40% 떨어졌지만 12개월 이익 전망은 22% 올랐다.",
  "· 투자자예탁금은 90조 원 아래로 내려가 1월 수준으로 줄었다.",
  "· 단일종목 레버리지 ETF에서 개인 손실은 6조 3,000억 원을 넘었고 40·50대가 62%를 차지했다.",
  "· 국내 투자자의 미국 주식 순매수는 이달 50억 달러에 육박해 9개월 만에 최대다 (채널 전언)"]),
 "facts": [
  "무엇이: 코스피 12개월 선행 PER이 4.2배로 떨어져 블룸버그 집계가 시작된 2006년 이후 시총 1조 달러 이상 시장 중 처음 5배를 밑돌았다 [채널]",
  "낙폭: 코스피는 6월 고점 대비 약 40% 하락한 반면 12개월 이익 전망은 22% 올랐고, 밸류에이션은 인도네시아의 절반 수준이다 [채널]",
  "수급: 투자자예탁금이 1월 수준인 90조 원 아래로 줄었고, 미국 주식 순매수는 이달 50억 달러에 육박해 1월 이후 9개월 만에 최대다 [채널]",
  "레버리지 ETF: 출시 2개월여 만에 개인 손실이 6조 3,000억 원을 넘고 40·50대가 62%를 차지했으며, 70대 이상 계좌당 손실은 2,994만 원이었다 [채널]"],
 "basis": "channel",
 "check": "검색 한도 배분상 생략, 텔레그램 원문이 블룸버그·한국일보·파이낸셜뉴스를 인용해 숫자가 구체적",
 "src": [],
 "inds": ["fin", "macro"], "nodes": ["macro/liquidity"],
 "vc": [{"ind": "fin", "node": "markets", "f": "가격", "dir": "down", "k": "실제", "t": "코스피 선행 PER 4.2배로 하락"},
        {"ind": "macro", "node": "liquidity", "f": "공급", "dir": "down", "k": "실제", "t": "투자자예탁금 90조 원 아래로 감소"}],
 "items": [
  it("투자자예탁금, 1월 수준인 90조 원 아래로 하락", TG_COMP, "https://t.me/w_compass/7445",
     "투자자예탁금이 1월 수준인 90조 원 아래로 내려가면서, 국내 증시 투자 심리가 최악 수준이라는 진단이 나왔다"),
  it("단일종목 레버리지 ETF 개인 손실 6.3조 원…40·50대가 62%", TG_COMP, "https://t.me/w_compass/7447",
     "단일종목 레버리지 ETF 출시 2개월여 만에 개인 손실이 6조 3,000억 원을 넘으면서, 70대 이상 계좌당 손실은 평균의 2.6배인 2,994만 원에 달했다"),
  it("서학개미 미국 주식 순매수 50억 달러 육박, 9개월 만에 최대", TG_COMP, "https://t.me/w_compass/7448",
     "국내 투자자의 미국 주식 순매수가 이달 50억 달러에 육박하면서, 국내 증시를 떠나 미국으로 향하는 자금이 1월 이후 최대가 됐다"),
  it("코스피 선행 PER 4.2배, 시총 1조 달러 시장 중 첫 5배 하회", TG_HANA, "https://t.me/HANAchina/70907",
     "코스피 12개월 선행 PER이 4.2배로 떨어지면서, 시총 1조 달러 이상 시장 가운데 2006년 이후 처음 5배를 밑도는 사례가 됐다"),
  it("기술주 폭락에 한국 증시, 인도네시아보다 두 배 싸져", TG_COMP, "https://t.me/w_compass/7458",
     "코스피가 6월 고점 대비 약 40% 떨어진 사이 12개월 이익 전망은 22% 오르면서, 한국 증시 밸류에이션이 인도네시아의 절반으로 낮아졌다")]})

items.append({"cid": "G2-018", "attachTo": "n-bbg-0428",
 "title": "스페이스X 스타링크 모바일 확장…800MHz 인수 이어 FCC 15MHz 면허 승인·기지국 8만 곳 협상",
 "one": "\n".join([
  "스페이스X가 스타링크 휴대전화 사업을 위해 주파수와 지상 기지국 확보를 넓히고 있다.",
  "· 스페이스X는 10월 9일 스타링크 휴대전화용 800MHz 저주파 대역 주파수 인수 계약을 발표했다.",
  "· FCC는 스페이스X의 트라이스타 주파수 면허 3건, 1695~1710MHz 대역 15MHz 인수를 승인했다.",
  "· FCC는 기지국 구축 의무를 면제하고 이 주파수를 위성통신에 쓰도록 허용했다.",
  "· 스페이스X가 미국 기지국 8만 곳 접근을 협상한다는 보도에 T모바일·AT&T 주가는 5% 가까이 내렸다.",
  "· 같은 보도에 크라운캐슬·아메리칸타워 주가는 5% 넘게 올랐다."]),
 "facts": [
  "무엇이: 스페이스X가 10월 9일 스타링크 휴대전화 서비스에 쓸 800MHz 대역 주파수 인수 계약을 발표해 T모바일·AT&T·버라이즌과 직접 경쟁할 기반을 마련했다 [사실]",
  "FCC 승인: FCC는 10월 21일 트라이스타 자회사의 AWS-3 면허 3건(1695~1710MHz, 15MHz) 이전을 승인하고 기지국 구축 의무를 면제했으며, 이 면허는 미국 인구 약 4%를 덮는다 [사실]",
  "기지국: 스페이스X가 새 무선 네트워크를 위해 미국 기지국 8만 곳 접근을 협상 중이라고 블룸버그가 보도했다 [제목]",
  "주가 반응: 기지국 협상 보도 뒤 T모바일·AT&T는 5% 가까이 내리고 크라운캐슬·아메리칸타워는 5% 넘게 올랐다 [채널]",
  "앞선 반응: 10월 9일 발표 당일 STOXX 600 통신지수가 3.3% 내리고 도이치텔레콤이 7~8% 급락했다 [사실]"],
 "basis": "partial",
 "check": "FCC 트라이스타 면허 승인은 드라이브테슬라캐나다·테슬라노스 검색 결과 요약으로 확인, 기지국 8만 곳 협상은 검색에 나오지 않아 블룸버그 제목·텔레그램 기준",
 "src": [{"o": "드라이브테슬라캐나다", "d": "2026-10-21", "u": "https://driveteslacanada.ca/news/fcc-approves-spacex-tristar-aws-3-spectrum/"},
         {"o": "테슬라노스", "d": "2026-10-21", "u": "https://teslanorth.com/2026/10/21/the-fcc-just-handed-spacex-more-spectrum-for-starlink-mobile/"}],
 "inds": ["tech"], "nodes": [],
 "vc": [{"ind": "tech", "node": "telecom", "f": "공급", "dir": "up", "k": "예상", "t": "스페이스X 기지국 8만 곳 접근 협상"},
        {"ind": "tech", "node": "telecom", "f": "가격", "dir": "down", "k": "실제", "t": "T모바일·AT&T 주가 5% 가까이 하락"}],
 "added": "블룸버그·로이터·텔레그램 4건 — FCC의 트라이스타 15MHz 면허 3건 인수 승인, 미 기지국 8만 곳 접근 협상과 통신주 5% 하락·타워주 급등 내용이 추가됨",
 "items": [
  it("스페이스X, 새 네트워크 위해 기지국 8만 곳 접근 협상", B, "https://www.bloomberg.com/news/articles/2026-10-22/spacex-in-talks-to-access-80-000-cell-sites-for-wireless-network",
     "스페이스X가 새 무선 네트워크를 위해 기지국 8만 곳 접근을 협상하면서, 스타링크 모바일이 지상망까지 갖출 수 있다 (제목 기준)"),
  it("스페이스X 기지국 8만 곳 협상 보도에 통신주 하락·타워주 급등", TG_INS, "https://t.me/insidertracking/67060",
     "스페이스X의 기지국 8만 곳 접근 협상 보도가 나오면서, T모바일·AT&T는 5% 가까이 내리고 크라운캐슬·아메리칸타워는 5% 넘게 올랐다"),
  it("스페이스X, 무선망 위해 미국 기지국 8만 곳 접근 모색", R, "https://www.reuters.com/business/media-telecom/spacex-seeks-access-80000-us-cell-sites-wireless-network-bloomberg-news-reports-2026-10-22/",
     "스페이스X가 무선 네트워크용으로 미국 기지국 8만 곳 접근을 모색한다는 블룸버그 보도를 로이터가 전하면서, 기존 이통사와의 경쟁 구도가 부각됐다 (제목 기준)"),
  it("FCC, 스페이스X의 트라이스타 주파수 면허 3건 인수 승인", TG_INS, "https://t.me/insidertracking/67082",
     "FCC가 스페이스X의 트라이스타 1695~1710MHz 대역 15MHz 면허 3건 인수를 승인하면서, 기지국 구축 대신 위성통신에 쓰도록 규제를 면제했다")]})

items.append({"cid": "G2-031", "attachTo": "",
 "title": "인도 금융사 2분기 실적…SBI카드 이익 75%↑·인더스인드은행 흑자 전환·슈리람 금 담보 연체 증가",
 "one": "\n".join([
  "인도 카드사·은행·비은행 금융사들이 2분기 이익을 늘렸지만 일부 대출에서는 연체가 늘었다.",
  "· SBI카드 순이익은 신용비용 감소로 약 75% 늘어 77억 8,000만 루피를 기록했다.",
  "· 인더스인드은행은 순이익 124억 2,000만 루피로 전년 손실에서 흑자로 돌아섰다.",
  "· 인더스인드은행 총부실채권비율은 2.73%로 전년 3.60%에서 낮아졌다.",
  "· 슈리람파이낸스는 이익이 예상을 웃돌았지만 금 담보 대출 연체가 늘었다."]),
 "facts": [
  "무엇이: SBI카드의 2분기(7~9월) 연결 순이익은 77억 8,000만 루피로 전년보다 약 75% 늘었고 총신용손실률은 5.6%로 개선됐다 [사실]",
  "인더스인드: 순이익 124억 2,000만 루피로 전년 43억 7,000만 루피 손실에서 흑자 전환했고 순이자이익은 3.62% 늘었다 [사실]",
  "건전성: 인더스인드은행 총부실채권비율은 2.73%로 전년 3.60%에서 낮아졌다 [사실]",
  "슈리람: 슈리람파이낸스는 이익이 예상을 웃돌았지만 금 담보 대출 연체가 늘었다 [제목]"],
 "basis": "partial",
 "check": "SBI카드·인더스인드은행은 APAC뉴스네트워크·비즈니스투데이 검색 결과 요약으로 확인, 슈리람파이낸스는 검색에 나오지 않아 제목 기준",
 "src": [{"o": "APAC뉴스네트워크", "d": "2026-10-23", "u": "https://apacnewsnetwork.com/2026/10/sbi-card-q2-results-net-profit-778-crore/"},
         {"o": "비즈니스투데이", "d": "2026-10-23", "u": "https://www.businesstoday.in/markets/stocks/story/indusind-bank-q2-profit-at-rs-1242-crore-nii-up-4-yoy-563338-2026-10-23"}],
 "inds": ["fin"], "nodes": [],
 "vc": [{"ind": "fin", "node": "banks", "f": "수요", "dir": "up", "k": "실제", "t": "인더스인드은행 대출 증가 속 흑자 전환"},
        {"ind": "fin", "node": "pcredit", "f": "공급", "dir": "down", "k": "예상", "t": "슈리람 금 담보 대출 연체 증가"}],
 "items": [
  it("인도 SBI카드, 자산건전성 개선에 분기 이익 증가", R, "https://www.reuters.com/world/india/indias-sbi-card-posts-higher-quarterly-profit-improving-asset-quality-2026-10-23/",
     "SBI카드가 신용비용 감소로 2분기 순이익을 약 75% 늘린 77억 8,000만 루피로 기록하면서, 총신용손실률이 5.6%로 낮아졌다"),
  it("인도 슈리람파이낸스, 이익 예상 상회…금 담보 대출 연체는 증가", R, "https://www.reuters.com/world/india/indias-shriram-finance-beats-profit-view-gold-loan-delinquencies-rise-2026-10-23/",
     "슈리람파이낸스가 시장 예상을 웃도는 이익을 냈지만 금 담보 대출 연체가 늘면서, 비은행 대출의 건전성 부담이 드러났다 (제목 기준)"),
  it("인도 인더스인드은행, 대출 증가·건전성 개선에 분기 흑자", R, "https://www.reuters.com/world/india/indias-indusind-bank-posts-quarterly-profit-loan-growth-asset-quality-boost-2026-10-23/",
     "인더스인드은행이 2분기 순이익 124억 2,000만 루피로 흑자 전환하면서, 총부실채권비율이 2.73%로 낮아지고 대출도 늘었다")]})

items.append({"cid": "G2-047", "attachTo": "",
 "title": "외국 금융사 중국 진출…씨티, 100% 소유 증권사 인가·모건스탠리, 미 은행 첫 판다본드 발행",
 "one": "\n".join([
  "미국 대형 금융사들이 중국 본토 증권업과 위안화 채권 시장으로 발을 넓히고 있다.",
  "· 씨티는 중국 증감회로부터 100% 소유 증권사 씨티그룹증권(중국) 설립 인가를 받았다.",
  "· 새 증권사는 상하이에 등록자본 12억 위안으로 세워지며 외국계 7번째 단독 소유 증권사가 된다.",
  "· 모건스탠리는 미국 은행 가운데 처음으로 위안화 표시 판다본드를 발행했다."]),
 "facts": [
  "무엇이: 중국 증권감독관리위원회가 씨티의 100% 소유 증권사 씨티그룹증권(중국) 설립을 승인했다 [사실]",
  "세부: 상하이에 등록자본 12억 위안으로 세워지며 인수·주식 중개·리서치·자문 업무를 하고, 외국계로는 7번째 단독 소유 증권사다 [사실]",
  "판다본드: 모건스탠리가 미국 은행은 물론 미국 기업 가운데 처음으로 위안화 표시 판다본드를 발행했다 [채널]"],
 "basis": "partial",
 "check": "씨티 인가는 씨티 보도자료·파이뉴스 검색 결과 요약으로 확인(5월 카이신 보도와 시점이 엇갈림), 모건스탠리 판다본드는 확인 못 함",
 "src": [{"o": "씨티그룹", "d": "2026-10-23", "u": "https://www.citigroup.com/global/news/press-release/2026/citi-receives-approval-establish-wholly-owned-securities-venture-china"},
         {"o": "파이뉴스 아시아", "d": "2026-10-23", "u": "https://www.finews.asia/finance/45152-citi-approval-china-security-firm"}],
 "inds": ["fin"], "nodes": [],
 "vc": [{"ind": "fin", "node": "ib", "f": "공급", "dir": "up", "k": "실제", "t": "씨티 중국 100% 소유 증권사 설립 인가"}],
 "items": [
  it("씨티, 중국 100% 소유 증권사 설립 인가 획득", R, "https://www.reuters.com/world/china/citi-wins-licence-set-up-fully-owned-china-securities-unit-2026-10-23/",
     "씨티가 중국에서 100% 소유 증권사 설립 인가를 받으면서, 외국계로는 7번째로 본토 인수·중개 업무를 단독으로 하게 된다"),
  it("모건스탠리, 미국 은행·기업 가운데 첫 판다본드 발행", TG_POL, "https://t.me/The_MariTimes/63950",
     "모건스탠리가 미국 은행과 기업을 통틀어 처음으로 위안화 표시 판다본드를 발행하면서, 미국 금융사의 위안화 조달 창구가 열렸다")]})

items.append({"cid": "G2-057", "attachTo": "n-bbg-0548",
 "title": "브라질 10월 중순 물가 0.32%↑, 12개월 4.62%로 목표 상한 돌파…결선 앞두고 셀릭 13.75%",
 "one": "\n".join([
  "브라질 물가가 대선 결선을 앞두고 목표 상한 4.5%를 넘어선 가운데 중앙은행은 소비자 부채 관리에 나섰다.",
  "· 10월 중순 물가(IPCA-15)는 전월 대비 0.32% 올라 12개월 상승률이 4.62%로 높아졌다.",
  "· 12개월 물가는 예상치 4.73%보다 낮았지만 목표 상한을 웃돌았다.",
  "· 9월 물가는 연 4.58%로 6월 이후 처음 목표 상단을 넘었다.",
  "· 이코노미스트들은 연말 셀릭 금리 전망을 13.50%에서 13.25%로 낮추고 올해 물가 전망을 5.22%로 높였다.",
  "· 셀릭 금리는 13.75%이며 다음 결정은 11월 4일이다.",
  "· 중앙은행은 소비자 부채를 단속하고 책임 있는 대출을 유도하려 한다."]),
 "facts": [
  "무엇이: 브라질 10월 중순 소비자물가(IPCA-15)는 0.32% 올라 9월 0.70%와 예상 0.43%를 밑돌았지만 12개월 상승률은 4.47%에서 4.62%로 높아져 목표 상한 4.5%를 넘었다 [사실]",
  "품목: 식품이 0.88% 올랐고 토마토는 24.54% 뛰었으며, 항공료는 9.24% 내렸다 [사실]",
  "9월: 9월 물가는 연 4.58%로 6월 이후 처음 목표 상단 4.5%를 넘었다 [사실]",
  "금리 전망: 셀릭 금리는 13.75%이고 다음 결정은 11월 4일이며, 이코노미스트들은 연말 셀릭 전망을 13.50%에서 13.25%로 낮추고 올해 물가 전망을 5.22%로 봤다 [사실]",
  "신용: 중앙은행은 소비자 부채 단속과 함께 책임 있는 대출을 유도하려 한다 [제목]"],
 "basis": "verified",
 "check": "IPCA-15 0.32%·12개월 4.62%·품목별 상승률은 리오타임스 검색 결과 요약으로 확인",
 "src": [{"o": "리오타임스", "d": "2026-10-23", "u": "https://www.riotimesonline.com/brazil-ipca-15-october-2026-inflation"}],
 "inds": ["macro"], "nodes": ["macro/inflation", "macro/cb"],
 "vc": [{"ind": "macro", "node": "inflation", "f": "가격", "dir": "up", "k": "실제", "t": "브라질 12개월 물가 4.62%로 목표 상한 돌파"}],
 "added": "블룸버그·로이터 2건 — 10월 중순 물가 0.32% 상승으로 12개월 4.62%를 기록해 결선 투표 전 목표 상한 4.5%를 넘은 내용이 추가됨",
 "items": [
  it("브라질 물가, 대선 결선 투표 앞두고 목표 상한 돌파", B, "https://www.bloomberg.com/news/articles/2026-10-23/brazil-inflation-shoots-through-target-limit-before-runoff-vote",
     "브라질 물가가 대선 결선 투표를 앞두고 목표 상한 4.5%를 넘어서면서, 12개월 상승률이 4.62%로 높아졌다"),
  it("브라질 10월 중순 소비자물가, 전월 대비 0.32% 상승", R, "https://www.reuters.com/world/americas/brazil-consumer-prices-rise-032-mid-october-2026-10-23/",
     "브라질 10월 중순 소비자물가가 0.32% 오르면서 9월 0.70%보다 둔화했지만, 식품값이 0.88% 올라 상승을 이끌었다")]})

items.append({"cid": "G2-074", "attachTo": "n-rtr-0551",
 "title": "튀르키예 펀드 청산법 국회 통과…최대 100만 리라 중간 지급, 예금자 다수 여전히 대기",
 "one": "\n".join([
  "튀르키예 국회가 부실 펀드 청산법을 통과시켰지만 다수 예금자는 아직 돈을 찾지 못하고 있다.",
  "· 자본시장위원회는 운용사 7곳의 펀드 131개 청산을 명령했고 얽힌 투자자는 약 45만 6,000명이다.",
  "· 국회는 10월 22일 투자자에게 최대 100만 리라를 중간 지급하는 법을 통과시켰다.",
  "· 지금까지 5만 5,755개 계좌에 497억 리라가 지급·이전됐고 청산 중인 펀드는 47개로 줄었다.",
  "· 당국은 지급 뒤 보상을 기다리는 투자자가 10만 명 아래로 줄 것으로 본다."]),
 "facts": [
  "무엇이: 튀르키예 국회는 10월 22일 청산 펀드 투자자에게 최대 100만 리라를 중간 지급하는 법을 통과시켰고, 대통령 승인과 관보 게재 뒤 시행된다 [사실]",
  "대상: 9월 17일 자본시장위원회가 청산을 명령한 펀드 투자자와 환매 주문이 묶인 투자자가 포함되며, 시장 조작 가담자는 제외된다 [사실]",
  "규모: 위원회는 운용사 7곳 펀드 131개(자산 약 170억~183억 달러) 청산을 명령했고 피해 투자자는 약 45만 6,000명이다 [사실]",
  "진행: 지금까지 5만 5,755개 계좌에 497억 리라가 지급·이전됐고 청산 중인 펀드는 131개에서 47개로 줄었다 [사실]",
  "전망: 당국은 지급 뒤 보상을 기다리는 투자자가 10만 명 아래로 줄 것으로 본다 [사실]"],
 "basis": "verified",
 "check": "데일리사바·후리예트데일리뉴스 검색 결과 요약으로 확인",
 "src": [{"o": "데일리사바", "d": "2026-10-22", "u": "https://www.dailysabah.com/business/economy/turkish-parliament-passes-fund-liquidation-law"},
         {"o": "후리예트데일리뉴스", "d": "2026-10-23", "u": "https://www.hurriyetdailynews.com/parliament-passes-law-on-fund-repayments-228493"}],
 "inds": ["fin"], "nodes": [],
 "vc": [{"ind": "fin", "node": "assetmgmt", "f": "공급", "dir": "up", "k": "예상", "t": "청산 펀드 투자자에 최대 100만 리라 중간 지급"}],
 "added": "로이터 1건 — 국회가 10월 22일 최대 100만 리라 중간 지급법을 통과시켰고 497억 리라 지급·청산 펀드 47개로 감소, 다수는 여전히 대기 내용이 추가됨",
 "items": [
  it("튀르키예 펀드 청산법 통과…예금자 다수는 여전히 인출 대기", R, "https://www.reuters.com/world/middle-east/turkey-passes-fund-liquidation-law-many-savers-still-await-access-money-2026-10-23/",
     "튀르키예가 펀드 청산법을 통과시켜 최대 100만 리라 중간 지급 길을 열었지만, 많은 예금자가 여전히 돈을 찾지 못하고 기다리고 있다")]})

items.append({"cid": "G2-084", "attachTo": "",
 "title": "UAE·그리스 127.5억 유로 협정 체결…아부다비, 그리스에 150억 유로 추가 투자 계획",
 "one": "\n".join([
  "UAE와 그리스가 아테네 전략 포럼에서 대규모 투자·사업 협정을 맺었다.",
  "· 양국은 18건, 127.5억 유로(약 143억 달러) 규모 협정과 사업 제휴를 발표했다.",
  "· 아부다비는 그리스에 150억 유로를 추가로 투자할 계획이라고 밝혔다."]),
 "facts": [
  "무엇이: UAE와 그리스는 10월 22일 아테네 전략 포럼에서 127.5억 유로(약 143억 달러) 규모 협정·사업 제휴 18건을 발표했다 [사실]",
  "추가 계획: 아부다비는 그리스에 150억 유로를 더 투자할 계획이며, 2022년 약속한 40억 유로에 더해진다 [사실]",
  "분야: 협정은 디지털 인프라·재생에너지·교통·항만·보건·식량안보 등에 걸치지만 사업별 내역은 공개되지 않았다 [사실]"],
 "basis": "verified",
 "check": "그리크헤럴드·아라비안포스트 검색 결과 요약으로 확인, 금액 단위는 달러가 아닌 유로(묶음 core의 '달러'와 다름)",
 "src": [{"o": "그리크헤럴드", "d": "2026-10-23", "u": "https://greekherald.com.au/news/uae-and-greece-announce-e12-75bn-in-deals-as-plans-for-further-e15bn-investment/"},
         {"o": "아라비안포스트", "d": "2026-10-23", "u": "https://thearabianpost.com/uae-and-greece-unveil-e12-75-billion-partnership-package/"}],
 "inds": ["macro"], "nodes": ["macro/geo"],
 "vc": [{"ind": "macro", "node": "liquidity", "f": "공급", "dir": "up", "k": "예상", "t": "아부다비, 그리스에 150억 유로 추가 투자 계획"}],
 "items": [it("UAE·그리스 127.5억 유로 협정, 아부다비는 150억 유로 추가 투자 계획", R, "https://www.reuters.com/world/middle-east/uae-greece-announce-1275-billion-deals-abu-dhabi-plans-further-15-billion-2026-10-22/")]})

items.append({"cid": "G2-094", "attachTo": "",
 "title": "도쿄증권거래소 데이터 정정에 키옥시아 신용매수 잔고 우려 재부상…3,117만→4,694만 주",
 "one": "\n".join([
  "도쿄증권거래소가 키옥시아 신용매수 잔고 자료를 정정하면서 매물 부담 우려가 다시 커졌다.",
  "· 정정으로 신용매수 잔고는 3,117만 주로 줄었다는 수치가 4,694만 주로 오히려 늘어난 것으로 바뀌었다.",
  "· 10월 15일 기준 신용매수 잔고는 약 9,200억 엔으로 거래소 최대이며 주가는 6월 고점 대비 63% 내렸다."]),
 "facts": [
  "무엇이: 도쿄증권거래소 정정으로 키옥시아 신용매수 잔고가 3,117만 주로 줄었다는 원래 자료가 4,694만 주로 늘어난 것으로 바뀌었다 [사실]",
  "규모: 10월 15일 기준 키옥시아 신용매수 잔고는 약 9,200억 엔으로 도쿄증권거래소 상장사 중 최대다 [사실]",
  "주가·일정: 주가는 6월 고점 대비 63% 내렸고, 6개월 상환 기한이 연말~2027년 초에 몰리며 10월 30일 분기 실적이 다음 고비다 [사실]"],
 "basis": "partial",
 "check": "정정 수치는 애드혹뉴스 한 곳에서만 확인, 9,200억 엔·63% 하락은 서울경제 검색 결과 요약으로 확인",
 "src": [{"o": "애드혹뉴스", "d": "2026-10-23", "u": "https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/kioxia-s-leverage-overhang-survives-a-data-correction-as-ai-spending-doubts-bite/70399023"},
         {"o": "서울경제", "d": "2026-10-20", "u": "https://en.sedaily.com/society/2026/10/20/kioxia-margin-debt-hits-920-billion-yen-raising-forced"}],
 "inds": ["jpins", "semis"], "nodes": ["jpins/securities"],
 "vc": [{"ind": "semis", "node": "memory", "f": "가격", "dir": "down", "k": "예상", "t": "키옥시아 신용잔고 9,200억 엔 매물 부담"}],
 "items": [it("도쿄증권거래소 데이터 정정에 키옥시아 신용잔고 우려 재부상", B, "https://www.bloomberg.com/news/articles/2026-10-23/tokyo-bourse-data-fix-revives-kioxia-margin-position-concerns")]})

skipped = [{"cid": "G2-064", "reason": "범위 밖(9월 2일 연준 감찰관 경고·9월 5일 보우먼·파월 블랙아웃 접촉 보도의 재탕)"}]

out = {"agent": "W6", "searches_used": 18, "fetches_used": 1, "items": items, "skipped": skipped}
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)

# length checks
TAILS = (' (제목 기준)', ' (채널 전언)')
def strip(s):
    for t in TAILS:
        if s.endswith(t): return s[:-len(t)]
    return s
for x in items:
    c = x['cid']
    if not 20 <= len(x['title']) <= 70: print(c, 'title', len(x['title']))
    L = strip(x['one']).split('\n')
    if not 40 <= len(L[0]) <= 90: print(c, 'first', len(L[0]))
    for l in L[1:]:
        if not 25 <= len(l) <= 90: print(c, 'line', len(l), l)
    if 'added' in x and not 40 <= len(x['added']) <= 140: print(c, 'added', len(x['added']))
    for v in x['vc']:
        if not 12 <= len(v['t']) <= 45: print(c, 'vc', len(v['t']), v['t'])
    for i in x['items']:
        if not 25 <= len(i['t']) <= 60: print(c, 't', len(i['t']), i['t'])
        if 's' in i and not 45 <= len(strip(i['s'])) <= 110: print(c, 's', len(strip(i['s'])), i['s'][:30])
        if len(x['items']) == 1 and not x['attachTo'] and 's' in i: print(c, 's should not exist')
