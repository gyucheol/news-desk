import json

D = "2026-10-23"
R = "로이터"; B = "블룸버그"


def it(t, o, u, s=None, d=D):
    x = {"t": t, "o": o, "d": d, "u": u}
    if s:
        x["s"] = s
    return x


items = []
skipped = []

# G1-001
items.append({
    "cid": "G1-001", "attachTo": "",
    "title": "석유 기업 실적 호조…에니 특별배당 13억 유로·자사주 38억 유로, SLB 매출 94.5억 달러",
    "one": "\n".join([
        "고유가 속 석유·에너지 기업들이 3분기 실적 호조와 주주환원 확대를 잇달아 내놨다.",
        "· 에니는 주당 0.46유로(약 13억 유로) 특별배당과 자사주 매입 38억 유로 증액을 결정했다.",
        "· SLB의 3분기 매출은 94.5억 달러, 조정 EPS는 0.64달러로 예상을 웃돌았다.",
        "· SLB는 중동 유전 활동이 회복되면 추가 성장 여력이 있다고 내다봤다.",
        "· 유럽 기업 실적은 에너지 횡재로 개선될 전망이지만 트레이더들은 석유주가 과열됐다고 본다.",
        "· 스위스 바로에너지는 유럽 연료난 속에 2030년까지 이익을 2배로 늘리는 목표를 내걸었다.",
        "· 영국 최대 민간 연기금 USS는 탄소 배출 책임을 석유 기업에 돌리는 것을 멈춰야 한다고 했다.",
    ]),
    "facts": [
        "무엇이: 에니가 3분기 조정 순이익 28억 유로(예상 24.8억 유로)를 내고 주당 0.46유로(약 13억 유로) 특별배당과 2026년 자사주 매입 38억 유로(종전 34억 유로) 증액을 발표했다 [사실]",
        "배경: 3분기 브렌트유 평균이 배럴당 97달러로 에니의 2026년 영업현금흐름 전망은 165억 유로로 올라갔다 [사실]",
        "SLB: 3분기 매출 94.5억 달러(예상 92.9억 달러), 조정 EPS 0.64달러(예상 0.62달러), 조정 EBITDA 20.7억 달러, 설비투자 4.85억 달러(예상 5.29억 달러)였고 2027년 전망을 긍정적으로 봤다 [채널]",
        "시장: 유럽 기업 실적은 에너지 횡재로 개선될 전망이지만 트레이더들은 실적 발표를 앞둔 석유주가 과열됐다고 본다 [제목]",
        "기관: 스위스 바로에너지는 유럽 연료난 속 2030년 이익 2배를 노리고, 영국 최대 민간 연기금 USS는 석유 기업 탓하기를 멈춰야 한다고 했다 [제목]",
    ],
    "basis": "partial",
    "check": "에니 특별배당·자사주·순이익은 회사 발표(검색 결과 요약)로 확인. SLB 수치는 텔레그램 원문, 바로에너지·USS·유럽 실적·석유주 과열은 제목·채널 기준으로 확인 못 함",
    "src": [{"o": "에니 3분기 실적 발표", "d": D, "u": "https://www.eni.com/en-IT/media/press-release/2026/10/2026-third-quarter-results.html"}],
    "inds": ["oil", "drilling"], "nodes": ["drilling/services"],
    "vc": [
        {"ind": "drilling", "node": "services", "f": "수요", "dir": "up", "k": "예상", "t": "SLB 중동 유전 활동 회복에 성장 전망"},
        {"ind": "oil", "node": "price", "f": "가격", "dir": "up", "k": "실제", "t": "고유가에 에니 특별배당·자사주 매입 확대"},
    ],
    "items": [
        it("유럽 기업 실적, 에너지 부문 횡재 이익 덕에 개선될 전망", R, "https://www.reuters.com/business/european-corporate-earnings-set-get-boost-energy-windfall-2026-10-22/",
           "유럽 기업들의 실적이 에너지 부문 횡재 이익에 힘입어 개선될 것으로 보이면서 에너지 업종이 실적 시즌을 떠받칠 수 있다 (제목 기준)"),
        it("실적 발표 앞두고 트레이더들 '석유주 주가 과열' 판단", B, "https://www.bloomberg.com/news/articles/2026-10-22/oil-stocks-are-looking-stretched-to-traders-as-earnings-loom",
           "트레이더들이 실적 발표를 앞둔 석유주가 지나치게 올랐다고 보면서 에너지주 추가 상승 여력에 경계감이 생겼다 (제목 기준)"),
        it("스위스 에너지 기업 바로, 유럽 연료난 속 2030년 이익 2배 노려", R, "https://www.reuters.com/business/energy/swiss-energy-company-varopreem-looks-double-earnings-by-2030-europe-faces-fuel-2026-10-23/",
           "스위스 바로에너지가 유럽 연료난을 배경으로 2030년까지 이익을 2배로 늘리겠다고 하면서 정유·연료 유통의 고마진 국면을 겨냥했다 (제목 기준)"),
        it("에니, 고유가에 현금흐름 늘자 투자자 환원 확대", B, "https://www.bloomberg.com/news/articles/2026-10-23/eni-raises-investor-payouts-as-high-fuel-prices-boost-cash-flow",
           "에니가 고유가로 현금흐름이 늘자 주주환원을 키우면서 2026년 자사주 매입을 38억 유로로 늘리고 특별배당을 결정했다"),
        it("에니, 3분기 호실적에 특별배당 지급·자사주 매입 확대", R, "https://www.reuters.com/business/energy/eni-pay-special-dividend-lift-buyback-after-strong-third-quarter-results-2026-10-23/",
           "에니가 3분기 조정 순이익 28억 유로로 예상을 넘자 주당 0.46유로 특별배당을 12월에 지급하기로 하면서 주주 몫을 늘렸다"),
        it("SLB 3분기 매출 94.5억 달러·조정 EPS 0.64달러로 예상 상회", "텔레그램 미국 주식 인사이더", "https://t.me/insidertracking/67107",
           "SLB가 3분기 매출 94.5억 달러, 조정 EPS 0.64달러로 예상을 넘으면서 설비투자는 4.85억 달러로 예상보다 적게 썼다"),
        it("SLB, 중동 유전 회복이 성장 이끌 것으로 전망", B, "https://www.bloomberg.com/news/articles/2026-10-23/slb-sees-growth-driven-by-middle-east-oil-field-recovery",
           "SLB가 중동 유전 활동 회복을 성장 동력으로 꼽으면서 유전 서비스 수요가 다시 늘 수 있다고 내다봤다 (제목 기준)"),
        it("영국 최대 민간 연기금 USS '석유기업 탓하기 이제 멈춰야'", "텔레그램 Polaristimes", "https://t.me/The_MariTimes/63945",
           "영국 최대 민간 연기금 USS가 탄소 배출 증가를 석유 기업 탓으로 돌리는 것은 경제 논리에 어긋난다고 하면서 기관의 에너지주 시각 변화를 드러냈다"),
        it("최대 유전 서비스 기업 SLB, 분기 이익 시장 예상 상회", R, "https://www.reuters.com/business/energy/top-oilfield-services-firm-slb-beats-quarterly-profit-estimates-2026-10-23/",
           "세계 최대 유전 서비스 기업 SLB가 분기 이익 예상을 넘으면서 유정 건설 부문 매출도 28.9억 달러로 예상을 웃돌았다"),
    ],
})

# G1-013
items.append({
    "cid": "G1-013", "attachTo": "",
    "title": "러시아 경유 4만 톤 첫 대미 화물 뉴욕행…외국기업 20곳 국유화·핀란드 '러 가스 불가'",
    "one": "\n".join([
        "러시아가 푸틴·트럼프 합의에 따른 첫 경유 화물을 미국으로 보내며 대미 경제관계를 넓히고 있다.",
        "· 러시아 경유 4만 톤을 실은 몰타 선적 유조선 아기오이 파넨데스호가 뉴욕으로 향하고 있다.",
        "· 이 배는 10월 22일 프리모르스크항에서 선적됐고 11월 7일 도착이 예상된다.",
        "· 푸틴 대통령은 2025년 1월 이후 외국 기업 20곳을 넘겨받았고 그중 17곳이 유럽 기업이다.",
        "· 핀란드 오르포 총리는 전쟁이 이어지는 동안 러시아 가스를 사서는 안 된다고 했다.",
    ]),
    "facts": [
        "무엇이: 러시아 경유 4만 톤을 실은 몰타 선적 유조선 아기오이 파넨데스호가 10월 22일 프리모르스크항에서 선적돼 뉴욕으로 향하고 있으며 Kpler는 11월 7일 도착을 예상했다 [사실]",
        "합의: 트럼프 대통령은 10월 9일 러시아가 30만 톤을 즉시, 11월 50만 톤, 이후 100만 톤을 수출한다고 밝혔고 페스코프 대변인은 첫 배가 출발했다고 했다 [사실]",
        "국유화: 2025년 1월 이후 러시아에 넘어간 외국 기업 20곳 중 17곳이 유럽, 3곳이 미국 기업이며 EU 집행위는 이를 강제 수용으로 규정했다 [채널]",
        "가스: 핀란드 오르포 총리는 러시아가 우크라이나 전쟁을 계속하는 동안 러시아 가스를 구매해선 안 된다고 주장했다 [채널]",
    ],
    "basis": "partial",
    "check": "경유 4만 톤 유조선·선적일·도착 예정은 유로뉴스·포춘 검색 결과 요약으로 확인. 외국기업 국유화 숫자와 핀란드 총리 발언은 텔레그램 원문 기준",
    "src": [
        {"o": "유로뉴스", "d": D, "u": "https://www.euronews.com/2026/10/23/first-russian-diesel-shipment-is-heading-to-us-under-trump-putin-deal"},
        {"o": "포춘", "d": D, "u": "https://fortune.com/2026/10/23/russia-ukraine-trump-diesel-tanker/"},
    ],
    "inds": ["oil", "gas", "macro"], "nodes": ["gas/trade", "macro/geo"],
    "vc": [
        {"ind": "oil", "node": "products", "f": "공급", "dir": "up", "k": "실제", "t": "러시아 경유 4만 톤 첫 대미 화물 뉴욕행"},
        {"ind": "gas", "node": "trade", "f": "수요", "dir": "down", "k": "예상", "t": "핀란드 총리 전쟁 중 러시아 가스 구매 반대"},
    ],
    "items": [
        it("러시아, 2025년 이후 외국기업 20곳 넘겨받아…17곳이 유럽 기업", "텔레그램 트릴리온", "https://t.me/Trillion_labs/11146",
           "푸틴 대통령이 2025년 1월 이후 외국 기업 20곳을 러시아 기업에 넘기면서 그중 17곳이 유럽 기업이어서 미국 기업만 피해 가는 모양새가 됐다"),
        it("핀란드 총리 '전쟁 중에는 러시아 가스 구매해선 안 돼'", "텔레그램 Polaristimes", "https://t.me/The_MariTimes/63938",
           "핀란드 오르포 총리가 러시아가 전쟁을 계속하는 동안 러시아 가스를 사지 말아야 한다고 하면서 유럽의 러시아 가스 복귀 논의에 선을 그었다"),
        it("크렘린 '미국과 합의한 러시아 경유 첫 화물선 출발'", R, "https://www.reuters.com/business/energy/kremlin-says-first-ship-carrying-russian-diesel-under-deal-with-us-is-its-way-2026-10-23/",
           "크렘린궁이 미국과의 합의에 따른 러시아 경유 첫 화물선이 출발했다고 밝히면서 앞으로 꾸준히 선적이 이어질 것이라고 했다"),
        it("러시아 경유 4만 톤 실은 유조선, 푸틴·트럼프 합의 뒤 뉴욕행", R, "https://www.reuters.com/business/energy/tanker-carrying-40000-t-russian-diesel-heads-new-york-after-putin-trump-deal-2026-10-23/",
           "러시아 경유 4만 톤을 실은 유조선이 푸틴·트럼프 합의 뒤 뉴욕으로 향하면서 2023년 이후 첫 러시아 경유의 미국 입항을 앞두게 됐다"),
    ],
})

# G1-022
items.append({
    "cid": "G1-022", "attachTo": "",
    "title": "트럼프·김정은 연내 회담 가능성 낮아…한국, 북한에 지상 경계선 군사회담 재제안",
    "one": "\n".join([
        "한미 당국이 북미 정상회담의 연내 성사 가능성을 낮게 보는 가운데 한국이 북한에 군사회담을 다시 제안했다.",
        "· 미국은 회담 개최와 관련해 북한으로부터 아무 응답을 받지 못했다고 소식통 5명이 전했다.",
        "· 국정원은 APEC 계기 북미 회담 가능성을 50%로 봤지만 카네기재단 판다 연구원은 10% 미만으로 봤다.",
        "· 한국 국방부는 군사분계선 공동 확인과 군 통신선 복구를 위한 회담을 10월 23일 제안했다.",
        "· 이번 제안은 북한이 답하지 않은 2025년 11월 제안을 되풀이한 것이다.",
    ]),
    "facts": [
        "무엇이: 한미 당국자들은 11월 18~19일 선전 APEC 정상회의 계기 트럼프·김정은 회담 가능성이 낮아지고 있다고 본다 [채널]",
        "전망: 국정원은 가능성을 50%로, 카네기재단 앤킷 판다 선임연구원은 10% 미만으로 봤고 북한 매체는 제재 완화 등 조건을 붙일 수 있다고 했다 [채널]",
        "회담 제안: 김홍철 국방차관은 10월 23일 군사분계선 공동 확인·군 통신선 복구·충돌 방지를 위한 군사회담을 제안했고 유엔사를 포함한 3자 회담도 가능하다고 했다 [사실]",
        "배경: 9월 21일 비무장지대 지뢰 폭발로 한국 장병이 다쳤고 한국군은 북한이 군사분계선 남쪽에 매설한 지뢰가 원인이라고 결론 냈다 [사실]",
    ],
    "basis": "partial",
    "check": "한국의 군사회담 재제안은 알자지라·UPI 검색 결과 요약으로 확인. 북미 회담 가능성 관련 수치는 텔레그램 원문·로이터 제목 기준",
    "src": [
        {"o": "알자지라", "d": D, "u": "https://www.aljazeera.com/news/2026/10/23/south-korea-invites-north-for-military-talks-over-border"},
        {"o": "UPI", "d": D, "u": "https://www.upi.com/Top_News/World-News/2026/10/23/korea-North-Korea-DMZ-border-defense-ministry-talks-MDL/4061792742282/"},
    ],
    "inds": ["macro"], "nodes": ["macro/geo"],
    "vc": [{"ind": "macro", "node": "geo", "f": "-", "dir": "flat", "k": "예상", "t": "북미 회담 불투명 속 남북 군사회담 재제안"}],
    "items": [
        it("한미 당국 '트럼프·김정은 연내 회담 가능성 낮아져'", "텔레그램 TNBfolio", "https://t.me/TNBfolio/71687",
           "한미 당국자들이 북한의 무응답 속에 트럼프·김정은 연내 회담 가능성을 낮게 보면서 APEC 계기 북미 회담 기대가 약해졌다"),
        it("한국, 북한에 지상 경계선 관련 회담 다시 제안", R, "https://www.reuters.com/world/asia-pacific/south-korea-proposes-talks-with-north-korea-land-border-again-2026-10-23/",
           "한국 국방부가 군사분계선 공동 확인과 통신선 복구를 위한 회담을 북한에 다시 제안하면서 접경 지역 우발 충돌 위험을 줄이려 했다"),
        it("한미 당국자들 '트럼프·김정은 연내 회담 가능성 거의 없어'", R, "https://www.reuters.com/world/china/us-south-korean-officials-see-little-chance-trump-kim-meeting-this-year-2026-10-23/",
           "한미 당국자들이 트럼프·김정은의 연내 만남 가능성을 거의 없다고 보면서 11월 APEC 계기 회담 전망이 어두워졌다 (제목 기준)"),
    ],
})

# G1-029
items.append({
    "cid": "G1-029", "attachTo": "",
    "title": "이란 장기전 대비…하메네이 '3천만 명 희생 각오'·강경파 핵무장 촉구·걸프 탈출 48시간 급증",
    "one": "\n".join([
        "이란이 장기 대결에 대비해 군사 동원을 강화하고 내부에서는 핵무장론이 커지고 있다.",
        "· 모즈타바 하메네이 최고지도자는 3천만 명 이상이 국가를 위해 희생할 뜻을 밝혔다고 주장했다.",
        "· 이란 강경파는 핵무기 개발 공식화를 촉구했고 고농축 우라늄 약 440kg이 변수로 꼽힌다.",
        "· 걸프 지역을 떠나는 전세기 요청이 지난 48시간 동안 급증했다 (채널 전언)",
    ]),
    "facts": [
        "무엇이: 모즈타바 하메네이 최고지도자가 3천만 명 이상의 이란인이 희생할 뜻을 밝혔다고 주장했고 이란은 바시즈 동원·핵시설 주변 방어 강화 등 장기 대결에 대비하고 있다 [채널]",
        "참고: 3천만 명 주장은 9월 28일 이란·이라크 전쟁 기념 메시지에서도 나왔고 독립적으로 검증되지 않은 수치다 [사실]",
        "핵무장론: FT에 따르면 국가안보위원회 하산 가슈가비 등 강경파가 핵 억지력 구축을 주장하며, 이란이 보유한 고농축 우라늄 약 440kg은 핵무기 약 10기 분량으로 평가된다 [채널]",
        "위협 대상: 이란은 호르무즈 해협 7개 조건을 거두지 않은 채 해저 통신 케이블·데이터센터·에너지 시설·미군 기지·상선을 위협 대상으로 삼고 있다 [채널]",
        "탈출: 걸프 지역을 떠나는 전세기 요청이 월요일 밤부터 48시간 사이 급증했고 외국인 부유층·외교관·왕족이 포함됐다 [채널]",
    ],
    "basis": "channel",
    "check": "3천만 명 주장은 9월 28일 메시지 보도(이란와이어)에서만 찾았고 이번 메시지 날짜·핵무장 촉구·전세기 급증은 확인 못 함",
    "src": [{"o": "이란와이어", "d": "2026-09-28", "u": "https://iranwire.com/en/news/158197-mojtaba-khamenei-declares-iran-first-power-of-the-world/"}],
    "inds": ["macro", "oil"], "nodes": ["macro/geo"],
    "vc": [
        {"ind": "oil", "node": "transport", "f": "공급", "dir": "down", "k": "예상", "t": "이란 장기전 대비하며 호르무즈 양보 거부"},
        {"ind": "macro", "node": "geo", "f": "-", "dir": "flat", "k": "예상", "t": "이란 강경파 핵무기 개발 공식화 촉구"},
    ],
    "items": [
        it("걸프 떠나는 전세기 요청 48시간 새 급증…왕족도 포함", "텔레그램 트릴리온", "https://t.me/Trillion_labs/11134",
           "민간 항공사들에 걸프 지역을 떠나는 전세기 요청이 48시간 사이 몰리면서 부유층·외교관·왕족까지 역내를 빠져나가고 있다"),
        it("모즈타바 하메네이 '3천만 명 희생 각오'…이란 장기 대결 대비", "텔레그램 미국 주식 인사이더", "https://t.me/insidertracking/67044",
           "모즈타바 하메네이가 3천만 명 이상의 희생 의지를 내세우면서 이란이 해저 케이블·에너지 시설 등을 겨냥한 장기 대결 태세를 드러냈다"),
        it("이란 강경파, 핵무기 개발 공식화 촉구…고농축 우라늄 440kg 변수", "텔레그램 미국 주식 인사이더", "https://t.me/insidertracking/67080",
           "이란 강경파가 핵무기 금지 원칙 폐기를 요구하면서 고농축 우라늄 약 440kg의 행방이 미국과의 협상과 중동 핵확산 위험의 변수가 됐다"),
    ],
})

# G1-041
items.append({
    "cid": "G1-041", "attachTo": "n-rtr-0569",
    "title": "EU 통상장관들 '차이나 쇼크 2.0' 협의로 대응…하루 10억 유로 대중 적자 압박",
    "one": "\n".join([
        "EU가 대중 무역적자를 줄이려 중국과 협의를 이어가며 '차이나 쇼크 2.0' 대응을 다짐했다.",
        "· EU는 10월 7~8일 강경 기조로 협의를 시작했고 셰프초비치 집행위원이 왕원타오 상무부장과 회담했다.",
        "· EU의 대중 상품 무역적자는 하루 10억 유로를 넘는다.",
        "· 셰프초비치 집행위원은 중국이 대EU 하이브리드차 수출을 절반으로 줄이기로 했다고 밝혔다.",
        "· EU 통상장관들은 10월 23일 화학·기계·의약품 수입을 억제하는 합의를 중국과 맺어야 한다고 했다.",
        "· 같은 날 볼보자동차 주가 급락이 중국발 도전을 부각했고 중국산 견제가 강해질 수 있다.",
    ]),
    "facts": [
        "무엇이: EU 통상장관들이 10월 23일 '차이나 쇼크 2.0'에 중국과의 협의로 대응하겠다고 다짐하며 화학·기계·의약품 수입 억제 합의를 추진해야 한다고 했다 [사실]",
        "협의 경과: EU는 10월 7~8일 대중 무역적자 축소를 내걸고 강경 기조로 협의를 시작했고 셰프초비치 무역·경제안보 담당 집행위원이 베이징에서 왕원타오 상무부장과 회담했다 [사실]",
        "적자 규모: EU의 대중 상품 무역적자는 하루 10억 유로를 넘고 장관들은 이를 지속 불가능하다고 봤다 [사실]",
        "자동차: 셰프초비치 집행위원은 중국이 대EU 하이브리드차 수출을 절반으로 줄이기로 했다고 밝혔다(EU 최종 승인 필요) [사실]",
        "시장: 볼보자동차 주가 급락이 EU의 대중 과제를 부각했고 EU의 압박으로 중국산 수입품 견제가 강해질 수 있다 [제목]",
    ],
    "basis": "partial",
    "check": "통상장관들의 협의 대응·화학·기계·의약품 수입 억제와 하이브리드차 수출 절반 감축은 검색 결과 요약으로 확인. 볼보차 주가 급락은 블룸버그 제목 기준",
    "src": [
        {"o": "글로벌뱅킹앤파이낸스", "d": D, "u": "https://www.globalbankingandfinance.com/eu-ministers-vow-tackle-china-shock-2-0-through-talks/"},
        {"o": "CNBC", "d": "2026-10-09", "u": "https://www.cnbc.com/2026/10/09/china-europe-hybrid-vehicle-exports-deal.html"},
    ],
    "inds": ["macro", "auto"], "nodes": ["macro/geo"],
    "vc": [
        {"ind": "macro", "node": "geo", "f": "공급", "dir": "down", "k": "예상", "t": "EU 중국산 화학·기계·의약품 수입 억제 추진"},
        {"ind": "auto", "node": "chinaoem", "f": "공급", "dir": "down", "k": "예상", "t": "중국 대EU 하이브리드차 수출 절반 감축"},
    ],
    "added": "로이터·블룸버그 2건 — EU 통상장관들의 '차이나 쇼크 2.0' 협의 대응 다짐, 화학·기계·의약품 수입 억제 추진, 볼보차 주가 급락 내용이 추가됨",
    "items": [
        it("EU 장관들, 중국과의 협의로 '차이나 쇼크 2.0' 대응 다짐", R, "https://www.reuters.com/world/china/eu-ministers-vow-tackle-china-shock-20-through-talks-with-beijing-2026-10-23/",
           "EU 통상장관들이 중국과의 협의로 '차이나 쇼크 2.0'에 대응하겠다고 하면서 화학·기계·의약품 수입을 억제하는 합의를 추진하기로 했다"),
        it("EU 통상장관 회의…볼보차 주가 급락이 중국발 도전 부각", B, "https://www.bloomberg.com/news/newsletters/2026-10-23/eu-trade-minister-meet-as-volvo-cars-share-plunge-underscores-china-challenge",
           "EU 통상장관들이 모인 날 볼보자동차 주가가 급락하면서 유럽 자동차 업계가 받는 중국발 압박이 드러났다 (제목 기준)"),
    ],
})

# G1-051
items.append({
    "cid": "G1-051", "attachTo": "",
    "title": "P&G 1분기 유기적 매출 4%↑ 예상 상회…원자재 비용 부담 14억 달러로 확대 경고",
    "one": "\n".join([
        "P&G가 1분기 매출은 예상을 넘었지만 원자재 비용 상승으로 연간 이익 타격이 커질 것이라고 경고했다.",
        "· 1분기 순매출은 233억 달러, 유기적 매출은 4% 늘었고 판매량이 성장을 이끌었다.",
        "· 핵심 영업이익률은 25.9%로 80bp 떨어졌고 핵심 매출총이익률은 150bp 낮아졌다.",
        "· 원자재·에너지 세후 비용 부담 전망은 브렌트유 배럴당 약 100달러 가정에서 약 14억 달러로 커졌다.",
        "· 연간 유기적 매출 1~3%, 핵심 EPS 0~3% 성장 전망은 그대로 유지했다.",
    ]),
    "facts": [
        "무엇이: P&G의 2027 회계연도 1분기 순매출이 233억 달러로 4% 늘었고 유기적 매출도 4% 증가했다 [사실]",
        "이익: 희석 EPS 1.97달러, 핵심 EPS 2.00달러로 각각 1% 늘었고 핵심 영업이익률은 25.9%로 80bp 하락했다 [사실]",
        "비용: 원자재·에너지 세후 비용 부담 전망을 약 14억 달러로 올렸고(브렌트유 배럴당 약 100달러 가정), 영업이익 아래 항목까지 포함하면 약 19억 달러로 봤다 [채널]",
        "전망: 연간 유기적 매출 1~3%, 핵심 EPS 0~3% 성장 가이던스는 유지했고 연간 FCF 생산성 전망은 85~90%로 낮췄다 [채널]",
        "지역: 10개 제품군과 6개 지역 모두 성장했고 중화권 유기적 매출은 8% 늘었다 [채널]",
    ],
    "basis": "verified",
    "check": "매출·EPS·영업이익률은 회사 발표·CNBC, 원자재 비용 14억 달러는 모틀리풀 어닝콜 요약(검색 결과 요약)으로 확인",
    "src": [
        {"o": "P&G 실적 발표", "d": "2026-10-22", "u": "https://www.pginvestor.com/news/news-details/2026/PG-Announces-Fiscal-Year-2027-First-Quarter-Results/default.aspx"},
        {"o": "모틀리풀 어닝콜", "d": "2026-10-22", "u": "https://www.fool.com/earnings/call-transcripts/2026/10/22/pg-pg-q1-2027-earnings-call-transcript/"},
    ],
    "inds": ["consumer"], "nodes": [],
    "vc": [
        {"ind": "consumer", "node": "household", "f": "가격", "dir": "up", "k": "예상", "t": "P&G 원자재·에너지 비용 부담 14억 달러로 확대"},
        {"ind": "consumer", "node": "household", "f": "수요", "dir": "up", "k": "실제", "t": "P&G 1분기 유기적 매출 4% 증가"},
    ],
    "items": [
        it("P&G, 원자재 비용 상승에 연간 이익 타격 확대 경고…매출은 예상 상회", R, "https://www.reuters.com/business/retail-consumer/pg-flags-bigger-hit-annual-profit-higher-commodity-costs-beats-revenue-estimates-2026-10-22/",
           "P&G가 매출 예상을 넘었지만 원자재 비용 상승으로 연간 이익 타격이 커진다고 경고하면서 생활용품 업체의 원가 부담을 드러냈다", "2026-10-23"),
        it("P&G 1분기 유기적 매출 4% 증가…판매량 회복이 성장 견인", "텔레그램 미국 주식 인사이더", "https://t.me/insidertracking/67063",
           "P&G가 판매량 2.4%p 기여로 유기적 매출을 4% 늘렸지만 핵심 매출총이익률이 150bp 떨어지면서 하반기 비용 압박이 커질 것으로 봤다"),
    ],
})

# G1-065
items.append({
    "cid": "G1-065", "attachTo": "",
    "title": "PG&E, 캘리포니아 산불 책임 규정 탓에 가스 사업 분리·매각 검토",
    "one": "\n".join([
        "PG&E가 캘리포니아 산불 책임 제도 개편이 무산되자 가스 사업 분리를 검토하고 있다.",
        "· 패티 포피 CEO는 실적 발표에서 가스 사업 분사나 매각 가능성을 밝혔다.",
        "· 약 400만 가스 고객이 모회사 산불 위험 탓에 투자등급 미만 차입비용을 낸다는 이유다.",
    ]),
    "facts": [
        "무엇이: PG&E가 주 의회가 산불 책임 법안을 처리하지 않자 가스 사업 분사·매각 등 분리를 검토한다고 밝혔다 [사실]",
        "이유: 약 400만 가스 고객이 모회사의 산불 책임 노출 탓에 투자등급 미만 차입비용을 부담하고 있다고 회사는 주장했다 [사실]",
        "일정: 링펜싱·자산 매각·사업 분리를 아우르는 검토 결과를 늦어도 내년 여름까지 내놓고, 11월 1일 나올 CPUC 보고서를 지켜본다 [사실]",
    ],
    "basis": "verified",
    "check": "가스 사업 분리 검토·400만 고객·검토 일정은 3분기 어닝콜 보도(검색 결과 요약)로 확인",
    "src": [
        {"o": "모틀리풀 어닝콜", "d": "2026-10-22", "u": "https://www.fool.com/earnings/call-transcripts/2026/10/22/pge-pcg-q3-2026-earnings-call-transcript/"},
        {"o": "후드라인", "d": D, "u": "https://hoodline.com/2026/10/pg-e-might-spin-off-gas-unit-as-california-fire-rules-stall-ceo-says/"},
    ],
    "inds": ["utilities"], "nodes": [],
    "vc": [{"ind": "utilities", "node": "capital", "f": "가격", "dir": "up", "k": "실제", "t": "산불 위험에 가스 고객 차입비용 투자등급 미만 수준"}],
    "items": [
        it("PG&E, 캘리포니아 산불 규정 때문에 가스 사업 분리 검토", B, "https://www.bloomberg.com/news/articles/2026-10-22/pg-e-weighs-gas-business-separation-over-california-fire-rules"),
    ],
})

# G1-075
items.append({
    "cid": "G1-075", "attachTo": "",
    "title": "HSBC, 2026년 백금·팔라듐 평균가 전망 하향…펀더멘털 변화·투자자 포지션 축소",
    "one": "\n".join([
        "HSBC가 시장 펀더멘털 변화와 투자자 포지션 축소를 이유로 2026년 백금·팔라듐 평균가 전망을 낮췄다.",
        "· HSBC는 두 금속 모두 여전히 반등 여지가 있다고 덧붙였다 (채널 전언)",
    ]),
    "facts": [
        "무엇이: HSBC가 펀더멘털 변화와 투자자 포지션 축소를 이유로 2026년 백금·팔라듐 평균 가격 전망을 하향했다 [채널]",
        "수치: 새 전망은 백금 온스당 1,925달러, 팔라듐 1,436달러로 전해졌다 [미확인]",
        "단서: HSBC는 두 금속 모두 반등 여지가 있다고 했다 [채널]",
    ],
    "basis": "channel",
    "check": "새 전망치는 로이터 전재 기사의 검색 결과 요약에만 있어 독립 출처로 확인 못 함",
    "src": [],
    "inds": ["metals"], "nodes": [],
    "vc": [{"ind": "metals", "node": "precious", "f": "가격", "dir": "down", "k": "예상", "t": "HSBC 2026년 백금·팔라듐 평균가 전망 하향"}],
    "items": [
        it("HSBC, 2026년 백금·팔라듐 평균 가격 전망치 하향 조정", "텔레그램 하나증권 중국전략", "https://t.me/HANAchina/70874"),
    ],
})

# G1-085
items.append({
    "cid": "G1-085", "attachTo": "",
    "title": "시그니파이, 美 관세 환급 2,800만 유로에 3분기 조정 EBITA 1.45억 유로…예상 상회",
    "one": "\n".join([
        "시그니파이가 미국 관세 환급과 비용 절감 덕에 3분기 이익 시장 예상을 넘었다.",
        "· 조정 EBITA는 1억 4,500만 유로로 시장 예상 1억 1,300만 유로를 웃돌았다.",
        "· 관세 환급이 2,800만 유로를 보탰지만 비교 가능 매출은 3.4% 줄었다.",
    ]),
    "facts": [
        "무엇이: 시그니파이의 3분기 조정 EBITA가 1억 4,500만 유로로 회사 집계 예상치 1억 1,300만 유로를 넘었다 [사실]",
        "관세 환급: 미국 관세 환급이 순 2,800만 유로를 기여해 조정 EBITA 마진을 약 2.1%p 끌어올렸고, 이를 빼면 마진은 8.5%였다 [사실]",
        "매출: 매출은 13억 6,700만 유로, 비교 가능 매출은 3.4% 줄었고 소비자·OEM·재래식 조명이 부진했다 [사실]",
        "전망: 연간 조정 EBITA 마진은 가이던스 7.5~8.5% 범위 상단을 예상한다 [사실]",
    ],
    "basis": "verified",
    "check": "조정 EBITA·관세 환급 기여·매출 감소는 에디슨리포트 등 검색 결과 요약으로 확인",
    "src": [{"o": "에디슨리포트", "d": D, "u": "https://edisonreport.com/2026/10/23/signify-q3-2026-results/"}],
    "inds": ["industrial"], "nodes": [],
    "vc": [{"ind": "industrial", "node": "electrical", "f": "수요", "dir": "down", "k": "실제", "t": "시그니파이 비교 가능 매출 3.4% 감소"}],
    "items": [
        it("시그니파이, 미국 관세 환급 덕에 이익 시장 예상 상회", R, "https://www.reuters.com/business/signify-beats-profit-expectations-helped-by-us-tariff-refund-2026-10-23/"),
    ],
})

# G1-095
items.append({
    "cid": "G1-095", "attachTo": "",
    "title": "소덱소, 2026 회계연도 유기적 성장 2.0%로 가이던스 상회…턴어라운드 진전",
    "one": "\n".join([
        "소덱소가 2026 회계연도 유기적 매출 성장률 2.0%로 회사 가이던스를 넘으며 턴어라운드 진전을 보였다.",
        "· 4분기 유기적 성장은 2.6%로 빨라졌지만 기초 영업이익률은 3.4%로 130bp 떨어졌다.",
        "· 2027 회계연도 유기적 성장 2~3% 전망을 재확인했다.",
    ]),
    "facts": [
        "무엇이: 소덱소의 2026 회계연도 유기적 매출 성장률이 2.0%로 7월 가이던스 1.2~1.5%를 넘었다 [사실]",
        "수익성: 기초 영업이익률은 3.4%로 130bp 하락했고 기초 영업이익은 약 29% 줄어 8억 1,000만 유로였다 [사실]",
        "지역: 북미 -1.0%, 유럽 2.1%, 기타 지역 9.7%의 유기적 성장을 기록했다 [사실]",
        "전망: 2027 회계연도 유기적 성장 2~3% 전망을 재확인하고 주당 1.74유로 배당을 제안했다 [사실]",
    ],
    "basis": "verified",
    "check": "회사 실적 발표(검색 결과 요약)로 확인. 애널리스트 컨센서스 대비 상회 여부는 확인 못 함",
    "src": [{"o": "소덱소 실적 발표(글로브뉴스와이어)", "d": D, "u": "https://www.manilatimes.net/2026/10/23/tmt-newswire/globenewswire/sodexo-fiscal-2026-results-organic-growth-above-guidance-fiscal-2027-outlook-confirmed/2452502/amp"}],
    "inds": ["consumer"], "nodes": [],
    "vc": [{"ind": "consumer", "node": "dining", "f": "수요", "dir": "up", "k": "실제", "t": "소덱소 유기적 성장 2.0%로 가이던스 상회"}],
    "items": [
        it("소덱소, 실적 예상 상회하며 턴어라운드 진전 신호", R, "https://www.reuters.com/business/sodexo-beats-expectations-signals-progress-turnaround-2026-10-23/"),
    ],
})

# G1-105
items.append({
    "cid": "G1-105", "attachTo": "",
    "title": "바릴라, 미국 맥앤치즈 브랜드 굿을스 7.5억 달러 전액 현금 인수",
    "one": "\n".join([
        "바릴라가 미국 맥앤치즈 브랜드 굿을스를 7억 5,000만 달러에 전액 현금으로 인수했다.",
        "· 실적 목표에 따라 최소 1억 달러를 더 지급하는 조건이 붙었다고 밀라노피난차가 전했다.",
        "· 굿을스의 최근 12개월 순매출은 1억 9,000만 달러로 인수가는 매출의 약 3.9배다.",
    ]),
    "facts": [
        "무엇이: 바릴라가 굿을스 인수 대금 7억 5,000만 달러를 전액 현금으로 치렀다 [제목]",
        "조건: 실적 연동 추가 지급 최소 1억 달러가 붙었고 거래는 이번 주 마무리됐으며 바릴라는 금액 언급을 거절했다 [사실]",
        "규모: 굿을스의 최근 12개월 순매출은 1억 9,000만 달러다 [사실]",
        "배경: 양사는 9월 초 인수에 합의하며 금액을 공개하지 않았고 굿을스는 독립 브랜드로 남는다 [사실]",
    ],
    "basis": "partial",
    "check": "인수 합의·완료와 추가 지급 조건은 밀라노피난차·비즈니스와이어로 확인. 7.5억 달러는 밀라노피난차도 블룸버그를 인용해 독립 확인 못 함",
    "src": [
        {"o": "밀라노피난차", "d": D, "u": "https://milanofinanza.it/news/barilla-750-milioni-di-dollari-per-goodles-la-scommessa-sul-mac-cheese-202610231445168274"},
        {"o": "비즈니스와이어", "d": "2026-09-02", "u": "https://www.businesswire.com/news/home/20260902759486/en/This-is-HUGE.-GOODLES-Finds-Its-Perfect-Match-With-Barilla-Group-for-a-New-Chapter-of-Growth."},
    ],
    "inds": ["consumer"], "nodes": [],
    "vc": [{"ind": "consumer", "node": "food", "f": "공급", "dir": "down", "k": "실제", "t": "바릴라 굿을스 인수로 맥앤치즈 경쟁사 흡수"}],
    "items": [
        it("바릴라, 굿을스 인수에 7억 5,000만 달러 전액 현금 지급", B, "https://www.bloomberg.com/news/articles/2026-10-23/barilla-paid-750-million-for-goodles-in-an-all-cash-deal"),
    ],
})

# G2-012
items.append({
    "cid": "G2-012", "attachTo": "",
    "title": "PHP 결함에 세계 웹 70% 흔들려…AI 발견 취약점 급증 경고·일본 사이버공격 모의훈련",
    "one": "\n".join([
        "AI가 찾아낸 PHP 결함 php2shell이 공개되며 세계 웹사이트들이 긴급 대응에 나섰다.",
        "· PHP는 세계 웹사이트의 70%를 떠받치며 미국·영국 등에서 사이트 수십 곳이 일시 차단됐다.",
        "· 클라우드플레어는 공개 2시간 만에 수십만 건의 공격 시도를 관측했다.",
        "· 일본은 PHP 결함 혼란 속에 사이버공격 모의훈련을 벌이기로 했다.",
        "· 전문가들은 AI가 찾은 버그가 곧 새로운 장애를 일으킬 수 있다고 경고했다.",
        "· 미국 임상검사업체 퀘스트 진단은 사이버 침해로 환자 기록이 영향을 받았다고 공개했다.",
    ]),
    "facts": [
        "무엇이: PHP 재단이 약 14년간 숨어 있던 치명적 결함 2건(php2shell)을 공개·패치했고 미 NSA와 유럽 사이버보안청이 즉각 조치를 권고했다 [사실]",
        "규모: PHP는 세계 웹사이트의 70%를 떠받치며, 클라우드플레어는 2시간 만에 수십만 건의 공격 시도를, 팔로알토는 잠재 취약 인스턴스 2,260만 개를 집계했다 [사실]",
        "AI 역할: 오픈AI·구글 모델 등 AI 도구가 결함 발견에 핵심 역할을 했고, 전문가들은 AI가 찾은 버그가 새로운 장애를 부를 수 있다고 경고했다 [사실]",
        "파장: 중국 매체는 월가가 긴급히 망 연결을 차단했고 중남미 은행 400곳이 AI 에이전트에 털렸다고 전했다 [채널]",
        "대응: 다카이치 일본 총리는 필요하면 서비스 중단을 검토하라고 했고 일본은 사이버공격 모의훈련을 벌이며, 퀘스트 진단은 환자 기록 침해를 공개했다 [제목]",
    ],
    "basis": "verified",
    "check": "php2shell 공개·70%·공격 시도·AI 역할은 악시오스·CNN·포춘 검색 결과 요약으로 확인. 월가 망 차단·중남미 은행 400곳은 중국 매체 전언으로 확인 못 함, 일본 모의훈련·퀘스트 침해는 제목 기준",
    "src": [
        {"o": "악시오스", "d": "2026-10-22", "u": "https://www.axios.com/2026/10/22/php-vulnerability-security-update-websites"},
        {"o": "CNN", "d": "2026-10-21", "u": "https://www.cnn.com/2026/10/21/tech/php2shell-vulnerability-ai-intl"},
        {"o": "포춘", "d": "2026-10-21", "u": "https://fortune.com/2026/10/21/ai-tools-discovered-the-php-vulnerability-that-could-take-down-70-of-the-internet-now-the-race-is-on-to-patch-it-before-ai-powered-hackers-attack/"},
    ],
    "inds": ["tech"], "nodes": [],
    "vc": [{"ind": "tech", "node": "software", "f": "공급", "dir": "down", "k": "실제", "t": "PHP 결함에 세계 웹사이트 일시 차단"}],
    "items": [
        it("임상검사업체 퀘스트, 환자 기록 영향 준 사이버 침해 공개", R, "https://www.reuters.com/legal/litigation/laboratory-operator-quest-reports-cyber-breach-affecting-patient-records-2026-10-22/",
           "미국 임상검사업체 퀘스트 진단이 사이버 침해로 환자 기록이 영향을 받았다고 밝히면서 의료 데이터 보안 우려가 커졌다 (제목 기준)"),
        it("中 매체 'PHP 결함에 사이버 보안 역사상 가장 어두운 48시간'", "텔레그램 하나증권 중국전략", "https://t.me/HANAchina/70868",
           "중국 매체가 세계 웹의 70%를 받치는 코드가 무너져 월가가 망을 차단하고 중남미 은행 400곳이 AI 에이전트에 털렸다고 전하며 AI발 사이버 위기를 부각했다"),
        it("일본, PHP 결함이 세계 인터넷 뒤흔들자 사이버공격 모의훈련", R, "https://www.reuters.com/business/media-telecom/japan-simulate-cyberattacks-php-flaws-roil-global-internet-2026-10-23/",
           "일본이 PHP 결함으로 세계 인터넷이 흔들리자 사이버공격 모의훈련에 나서면서 정부 차원의 대응 태세를 점검하기로 했다 (제목 기준)"),
        it("사이버 전문가들 'AI가 찾은 버그, 곧 새로운 장애 일으킬 수도'", R, "https://www.reuters.com/legal/litigation/ai-discovered-bugs-may-soon-trigger-fresh-disruptions-cyber-experts-say-2026-10-23/",
           "사이버 전문가들이 AI가 찾아낸 소프트웨어 버그가 곧 새로운 장애를 일으킬 수 있다고 경고하면서 PHP 사태가 되풀이될 위험을 지적했다 (제목 기준)"),
        it("AI가 소프트웨어 취약점이 빠르게 쏟아지는 시대 열어", B, "https://www.bloomberg.com/news/articles/2026-10-23/ai-ushers-in-era-of-rapid-fire-software-vulnerabilities",
           "AI가 소프트웨어 취약점을 빠르게 찾아내는 시대를 열면서 기업과 정부의 보안 패치 부담이 커지고 있다 (제목 기준)"),
    ],
})

# G2-020
items.append({
    "cid": "G2-020", "attachTo": "",
    "title": "AI 부채 공포…네오클라우드 공매도 60억 달러 수익·코어위브 자금 부족 230억 vs 760억 달러",
    "one": "\n".join([
        "AI 인프라 부채 우려로 네오클라우드 주가가 밀리며 신용시장의 AI 노출이 부각됐다.",
        "· 네오클라우드·데이터센터 공매도 세력은 이달 들어 60억 달러의 평가이익을 거뒀다.",
        "· 코어위브 자금 부족분을 골드만삭스는 230억 달러, 번스타인은 760억 달러로 추정했다.",
        "· 블랙스톤의 칩 담보 대출 베팅이 신용시장을 뒤흔드는 부채 붐을 낳았다고 블룸버그가 전했다.",
        "· 미국 생명보험사들의 AI 익스포저는 1~6월 사이 24% 늘었다.",
    ]),
    "facts": [
        "무엇이: ORTEX 집계로 미국 네오클라우드·데이터센터 공매도 세력이 10월 들어 60억 달러 평가이익을 냈고 네비우스 29.4억 달러, 코어위브 약 17억 달러였다 [사실]",
        "코어위브: 무담보 채권 수익률은 약 15%로 올랐고, 자금 부족분 추정은 골드만삭스 230억 달러, 번스타인 760억 달러로 엇갈린다 [채널]",
        "신용: 블랙스톤의 칩 담보 대출 베팅이 신용시장을 뒤흔드는 부채 붐을 촉발했다 [제목]",
        "보험: 미국 생보사의 AI 익스포저가 1~6월 사이 24% 늘었다 [제목]",
    ],
    "basis": "partial",
    "check": "공매도 60억 달러 평가이익과 코어위브 채권 수익률 약 15%는 검색 결과 요약으로 확인. 번스타인 760억 달러 추정, 블랙스톤·생보사 내용은 확인 못 함",
    "src": [{"o": "포위크MBA", "d": "2026-10-22", "u": "https://fourweekmba.com/ai-neocloud-shorts-book-6b-paper-gains-nebius-leads-at-2-94b/"}],
    "inds": ["tech", "fin", "macro"], "nodes": ["macro/semis"],
    "vc": [{"ind": "tech", "node": "cloud", "f": "가격", "dir": "down", "k": "실제", "t": "AI 부채 우려에 네오클라우드 주가 급락"}],
    "items": [
        it("공매도 세력, AI 부채 공포에 네오클라우드 급락하자 60억 달러 수익", R, "https://www.reuters.com/business/short-sellers-pocket-6-billion-profits-neoclouds-slide-ai-debt-fears-2026-10-22/",
           "AI 부채 우려로 네오클라우드 주가가 밀리면서 공매도 세력이 10월 들어 60억 달러의 평가이익을 거뒀고 네비우스·코어위브 공매도가 컸다"),
        it("미 생명보험사 AI 익스포저, 1~6월 24% 급증", B, "https://www.bloomberg.com/news/articles/2026-10-22/us-life-insurers-exposure-to-ai-jumped-24-from-january-to-june",
           "미국 생명보험사들의 AI 관련 익스포저가 1~6월 24% 늘면서 AI 부채 부실이 보험사 자산으로 번질 수 있다는 우려를 키웠다 (제목 기준)"),
        it("코어위브 자금 부족분, 골드만 230억 vs 번스타인 760억 달러", "텔레그램 하나증권 중국전략", "https://t.me/HANAchina/70899",
           "번스타인이 코어위브 자금 부족분을 골드만삭스 추정 230억 달러보다 훨씬 큰 760억 달러로 보면서 무담보채 수익률 15%의 회사 신용 위험을 경고했다"),
        it("블랙스톤의 칩 베팅이 신용시장 뒤흔드는 부채 붐 촉발", B, "https://www.bloomberg.com/news/articles/2026-10-23/blackstone-bet-on-chips-drove-a-debt-boom-that-s-upending-credit",
           "블랙스톤의 칩 담보 대출 베팅이 부채 붐을 일으키면서 신용시장의 대출 구조와 위험 배분을 흔들고 있다 (제목 기준)"),
    ],
})

# G2-036
items.append({
    "cid": "G2-036", "attachTo": "n-bbg-0640",
    "title": "예측시장 규제·경쟁…헤그세스, 군 내부정보 베팅 금지·칼시 CPI 선물로 월가 공략",
    "one": "\n".join([
        "예측시장이 군 내부정보 베팅 금지와 상품 확대, 경영 압박이 겹치며 규제와 경쟁의 시험대에 올랐다.",
        "· 헤그세스 장관은 군사작전 비공개 정보를 이용한 폴리마켓·칼시 베팅을 전 인력에 금지했다.",
        "· 마두로 축출 작전 참가 군인이 3만 3,000달러를 걸어 40만 9,000달러를 번 혐의 사건이 배경이다.",
        "· 칼시는 CPI 선물로 월가를 공략하며 '인플레이션 거래소'가 되려 한다.",
        "· 15분 단위 비트코인 예측시장 베팅이 투기 수요를 끌어들이고 있다.",
        "· 폴리마켓 투자자들은 칼시의 추격에 쿠플란 CEO에게 변화를 요구하고 있다.",
    ]),
    "facts": [
        "무엇이: 헤그세스 장관이 10월 20일자 지침으로 군사작전 관련 비공개 정보를 이용한 폴리마켓·칼시 등 예측시장 베팅을 전 인력에 금지하고 위반 시 군법·연방법 처벌을 경고했다 [사실]",
        "배경: 마두로 축출 작전 정보를 이용해 폴리마켓에 베팅한 혐의로 미군 특수부대원이 체포됐으며 3만 3,000달러 이상을 걸어 40만 9,000달러 이상을 번 혐의를 받는다 [채널]",
        "칼시: 칼시는 CPI 선물로 월가를 끌어들여 '인플레이션 거래소'가 되려 한다 [제목]",
        "상품: 15분 단위 비트코인 예측시장 베팅이 확산하고 있다 [제목]",
        "경쟁: 폴리마켓 투자자들은 칼시가 입지를 넓히자 쿠플란 CEO에게 변화를 요구하고 있다 [제목]",
    ],
    "basis": "partial",
    "check": "헤그세스 지침은 CBS·ABC 검색 결과 요약으로 확인. 베팅 금액은 텔레그램 원문, 칼시 CPI 선물·15분 비트코인 베팅은 블룸버그 제목 기준",
    "src": [
        {"o": "CBS뉴스", "d": "2026-10-22", "u": "https://www.cbsnews.com/news/hegseth-betting-ban-military-operations/"},
        {"o": "ABC뉴스", "d": "2026-10-22", "u": "https://abcnews.com/US/wireStory/new-pentagon-directive-bans-troops-nonpublic-info-bet-137493082"},
    ],
    "inds": ["fin"], "nodes": [],
    "vc": [
        {"ind": "fin", "node": "markets", "f": "공급", "dir": "up", "k": "예상", "t": "칼시 CPI 선물로 월가 공략 추진"},
        {"ind": "fin", "node": "regulation", "f": "수요", "dir": "down", "k": "실제", "t": "군 인력 내부정보 예측시장 베팅 금지"},
    ],
    "added": "블룸버그·텔레그램 3건 — 헤그세스의 군 내부정보 예측시장 베팅 금지, 칼시 CPI 선물 추진, 15분 단위 비트코인 베팅 확산 내용이 추가됨",
    "items": [
        it("15분 단위 예측시장 베팅, 비트코인 투기 수요 흡수", B, "https://www.bloomberg.com/news/newsletters/2026-10-22/fifteen-minute-prediction-market-bets-scratch-the-bitcoin-itch",
           "15분 단위로 결과가 나는 예측시장 비트코인 베팅이 늘면서 단기 투기 수요가 예측시장으로 옮겨 가고 있다 (제목 기준)"),
        it("헤그세스, 군사작전 내부정보 이용한 예측시장 베팅 금지", "텔레그램 미국 주식 인사이더", "https://t.me/insidertracking/67081",
           "헤그세스 장관이 군사작전 비공개 정보를 이용한 폴리마켓·칼시 베팅을 금지하면서 위반 시 형사처벌까지 경고해 예측시장 이용에 제동을 걸었다"),
        it("칼시, CPI 선물로 월가 공략하며 '인플레이션 거래소' 노려", B, "https://www.bloomberg.com/news/articles/2026-10-23/kalshi-courts-wall-street-in-bid-to-be-the-inflation-exchange-with-cpi-futures",
           "칼시가 CPI 선물을 내세워 월가 기관을 끌어들이면서 예측시장을 인플레이션 헤지 거래소로 넓히려 하고 있다 (제목 기준)"),
    ],
})

# G2-042
items.append({
    "cid": "G2-042", "attachTo": "",
    "title": "AI 매도 앞서 개인은 AI 수혜주 대량 매수…캘퍼스는 M7 줄이고 사모펀드 확대",
    "one": "\n".join([
        "AI 관련주 매도세를 전후해 개인투자자와 대형 연기금의 포지션이 서로 엇갈렸다.",
        "· 개인투자자들은 매도세 직전 AI 지출 수혜주를 대거 사들였다.",
        "· 캘리포니아 공무원연금 캘퍼스는 M7 빅테크 투자를 줄이고 사모펀드 투자를 늘리고 있다고 밝혔다 (채널 전언)",
    ]),
    "facts": [
        "무엇이: 개인투자자들이 AI 관련주 매도 직전 AI 지출 수혜주를 대거 사들였다 [제목]",
        "연기금: 캘퍼스가 M7 빅테크 투자를 줄이고 사모펀드 투자를 늘리고 있다고 FT가 전했다 [채널]",
    ],
    "basis": "channel",
    "check": "검색 한도로 독립 확인 못 함. 캘퍼스 내용은 텔레그램 원문(FT 인용) 기준",
    "src": [],
    "inds": ["fin", "macro"], "nodes": ["macro/semis"],
    "vc": [{"ind": "fin", "node": "assetmgmt", "f": "수요", "dir": "up", "k": "실제", "t": "캘퍼스 M7 줄이고 사모펀드 투자 확대"}],
    "items": [
        it("개인투자자, 매도세 직전 AI 지출 수혜주 대거 매수", B, "https://www.bloomberg.com/news/articles/2026-10-22/retail-traders-loaded-up-on-ai-spending-winners-before-selloff",
           "개인투자자들이 매도세 직전 AI 지출 수혜주를 대거 사들이면서 AI 관련주 급락의 손실을 고스란히 떠안게 됐다 (제목 기준)"),
        it("캘퍼스, M7 빅테크 비중 줄이고 사모펀드 투자 확대", "텔레그램 Polaristimes", "https://t.me/The_MariTimes/63942",
           "미국 대형 연기금 캘퍼스가 M7 빅테크 투자를 줄이고 사모펀드 투자를 늘리면서 대형 기술주 집중 위험을 덜어 내고 있다"),
    ],
})

# G2-052
items.append({
    "cid": "G2-052", "attachTo": "n-rtr-0647",
    "title": "비만약 시장…JP모건 '신흥 3국 GLP-1 2035년 220억 달러'·닥터레디스 오젬픽 제네릭 출시",
    "one": "\n".join([
        "비만치료제 시장에서 효능 데이터와 유통 확대에 이어 신흥국 제네릭 경쟁이 본격화하고 있다.",
        "· 노보 카그리세마는 REDEFINE 1 여성 2,309명에서 68주간 평균 25.0% 감량을 보였다.",
        "· 폐경 전 26.7%, 폐경 후 23.1% 감량이었지만 노보는 가설 생성용 사후 분석이라고 밝혔다.",
        "· 힘스앤허스는 독일에서 남성 대상 온라인 체중 관리 서비스를 시작했다.",
        "· 비만약 사용자들이 식이 보충제로 몰리자 의사와 규제당국이 경고하고 나섰다.",
        "· JP모건은 중국·인도·브라질 GLP-1 시장이 66억 달러에서 2035년 220억 달러로 커질 수 있다고 봤다.",
        "· 닥터레디스는 오베다 공급 차질 속에 오젬픽 제네릭 새 브랜드를 내놨다.",
    ]),
    "facts": [
        "무엇이: 노보노디스크는 REDEFINE 1 여성 2,309명에서 카그리세마 2.4mg/2.4mg이 68주간 평균 25.0%(위약 3.0%) 체중을 줄였고 폐경 전 26.7%, 이행기 24.8%, 폐경 후 23.1%였다고 밝혔다(사후 분석) [사실]",
        "허가: 노보는 2025년 12월 FDA에 카그리세마 허가를 신청했고 결정은 2026년 4분기로 예상된다 [사실]",
        "유통·안전: 힘스앤허스는 독일에서 남성 대상 온라인 체중 관리 서비스를 출시했고, 비만약 사용자의 보충제 의존에 의사·규제당국이 우려를 제기했다 [제목]",
        "신흥국: JP모건은 중국·인도·브라질 GLP-1 시장이 현재 66억 달러에서 2035년 220억 달러(연 15%)로 커지고 중국이 2027년 브라질을 앞질러 2035년 137억 달러에 이를 것으로 봤다 [사실]",
        "제네릭: 닥터레디스는 오베다 공급 차질 속에 오젬픽 제네릭 새 브랜드를 출시했다 [제목]",
    ],
    "basis": "partial",
    "check": "JP모건 220억 달러 전망과 세부 수치는 검색 결과 요약으로 확인. 닥터레디스 새 브랜드 출시는 제목 외 세부(브랜드명·차질 원인) 확인 못 함",
    "src": [{"o": "inkl", "d": D, "u": "https://www.inkl.com/news/glp-1-boom-in-china-india-brazil-could-create-22-billion-market-by-2035-j-p-morgan-says"}],
    "inds": ["pharma"], "nodes": [],
    "vc": [
        {"ind": "pharma", "node": "obesity", "f": "수요", "dir": "up", "k": "예상", "t": "신흥 3국 GLP-1 시장 2035년 220억 달러 전망"},
        {"ind": "pharma", "node": "obesity", "f": "공급", "dir": "up", "k": "실제", "t": "닥터레디스 오젬픽 제네릭 새 브랜드 출시"},
    ],
    "added": "로이터 2건 — JP모건의 중국·인도·브라질 GLP-1 시장 2035년 220억 달러 전망, 닥터레디스 오젬픽 제네릭 새 브랜드 출시 내용이 추가됨",
    "items": [
        it("JP모건 '중국·인도·브라질 GLP-1 붐, 2035년 220억 달러 시장 될 수도'", R, "https://www.reuters.com/business/healthcare-pharmaceuticals/glp-1-boom-china-india-brazil-could-create-22-bln-market-by-2035-jp-morgan-says-2026-10-23/",
           "JP모건이 제네릭과 가격 인하로 중국·인도·브라질 GLP-1 시장이 2035년 220억 달러로 커질 수 있다고 보면서 신흥국 비만약 수요 확대를 전망했다"),
        it("닥터레디스, 오베다 공급 차질 속 오젬픽 제네릭 새 브랜드 출시", R, "https://www.reuters.com/legal/litigation/dr-reddys-rolls-out-new-generic-ozempic-brands-amid-obeda-supply-disruption-2026-10-23/",
           "닥터레디스가 기존 오베다 공급 차질 속에 오젬픽 제네릭 새 브랜드를 내놓으면서 세마글루타이드 제네릭 공급을 이어 가려 했다 (제목 기준)"),
    ],
})

# G2-062
items.append({
    "cid": "G2-062", "attachTo": "",
    "title": "인도네시아 회사채 위험지표 6년 최고…중앙은행 '동결·인상·인하 정책 조합에 논리'",
    "one": "\n".join([
        "MSCI 지위 하향 우려 속에 인도네시아 회사채 위험 프리미엄이 6년 만에 최고로 올랐다.",
        "· MSCI 우려는 주식을 넘어 국채와 루피아로 번졌다.",
        "· 인도네시아중앙은행은 금리 동결·인상·인하를 섞은 정책 조합에 논리가 있다고 밝혔다.",
    ]),
    "facts": [
        "무엇이: 인도네시아 회사채 위험 지표가 MSCI 우려 속에 6년 최고로 올랐다 [사실]",
        "파급: MSCI는 인도네시아를 신흥시장에서 단독 시장으로 재분류하는 안을 내놨고, 10년물 국채와 미국채 스프레드는 219.4bp에서 228.6bp로 벌어졌다 [사실]",
        "중앙은행: 인도네시아중앙은행은 동결·인상·인하가 뒤섞인 정책 조합에 논리가 있다고 밝혔다 [제목]",
        "전망: MUFG는 연말까지 기준금리 6.25% 인상을, 골드만삭스는 2026년 4분기와 2027년 1분기 25bp씩 두 차례 인상을 예상했다 [사실]",
    ],
    "basis": "partial",
    "check": "회사채 위험 6년 최고·국채 스프레드·인상 전망은 검색 결과 요약으로 확인. 중앙은행 정책 조합 발언은 로이터 제목 기준",
    "src": [
        {"o": "바자르타임스", "d": D, "u": "https://bazaartimes.com/indonesias-private-sector-bond-risk-hits-six-year-high-amid-msci-warning/"},
        {"o": "MUFG 리서치", "d": "2026-10-21", "u": "https://www.mufgresearch.com/fx/asia-fx-special-focus-21-october-2026"},
    ],
    "inds": ["macro"], "nodes": ["macro/rates", "macro/cb"],
    "vc": [
        {"ind": "macro", "node": "rates", "f": "가격", "dir": "up", "k": "실제", "t": "인도네시아 회사채 위험 프리미엄 6년 최고"},
        {"ind": "macro", "node": "cb", "f": "가격", "dir": "up", "k": "예상", "t": "MUFG 인도네시아 연말 기준금리 6.25% 인상 전망"},
    ],
    "items": [
        it("인도네시아 회사채 위험 지표, 6년 만에 최고로 상승", B, "https://www.bloomberg.com/news/articles/2026-10-23/indonesian-corporate-bond-premia-hit-six-year-high-on-msci-angst",
           "MSCI 지위 하향 우려로 인도네시아 회사채 위험 지표가 6년 만에 최고로 오르면서 기업들의 조달 비용 부담이 커졌다"),
        it("인도네시아중앙은행 '동결·인상·인하 정책 조합에 논리 있어'", R, "https://www.reuters.com/world/asia-pacific/hold-hike-cut-bank-indonesia-says-theres-logic-policy-mix-2026-10-23/",
           "인도네시아중앙은행이 금리 동결과 인상·인하가 섞인 정책 조합에 논리가 있다고 하면서 시장의 정책 혼선 지적을 반박했다 (제목 기준)"),
    ],
})

# G2-069
items.append({
    "cid": "G2-069", "attachTo": "",
    "title": "힘스앤허스, 이용자 데이터·구독 관행 문제 삼은 FTC 소송 기각 요청",
    "one": "\n".join([
        "힘스앤허스가 이용자 데이터와 구독 관행을 문제 삼은 미 연방거래위원회 소송의 기각을 요청했다.",
        "· FTC 소송은 힘스앤허스의 이용자 데이터 처리와 구독 방식을 겨냥하고 있다 (제목 기준)",
    ]),
    "facts": [
        "무엇이: 힘스앤허스가 미 연방거래위원회(FTC) 소송의 기각을 요청했다 [제목]",
        "쟁점: FTC 소송은 이용자 데이터와 구독 관행을 다룬다 [제목]",
    ],
    "basis": "title",
    "check": "검색 한도로 독립 확인 못 함",
    "src": [],
    "inds": ["pharma"], "nodes": [],
    "vc": [{"ind": "pharma", "node": "regulatory", "f": "-", "dir": "flat", "k": "예상", "t": "힘스앤허스 FTC 소송 기각 요청으로 공방 진행"}],
    "items": [
        it("힘스앤허스, 이용자 데이터·구독 문제 FTC 소송 기각 요청", B, "https://www.bloomberg.com/news/articles/2026-10-22/hims-seeks-dismissal-of-ftc-suit-over-user-data-subscriptions"),
    ],
})

# G2-079
items.append({
    "cid": "G2-079", "attachTo": "",
    "title": "베네수엘라, 20억 달러 넘는 IDB 연체 해소 위해 카타르 브리지론 모색",
    "one": "\n".join([
        "베네수엘라가 미주개발은행 연체금을 갚기 위해 카타르에서 브리지론을 빌리는 방안을 검토하고 있다.",
        "· 연체금은 20억 달러를 넘으며 IDB는 2018년 5월부터 신규 대출을 멈춘 상태다.",
        "· 연체를 해소하면 IDB 자금을 다시 받아 카타르에 갚는 구조가 거론된다.",
    ]),
    "facts": [
        "무엇이: 베네수엘라가 20억 달러가 넘는 IDB 연체금을 갚기 위해 미국의 지원 아래 카타르 브리지론을 검토하고 있다고 소식통 6명이 전했다 [사실]",
        "배경: IDB는 2018년 5월 베네수엘라 신규 대출을 중단했고 연체를 해소하면 대출 재개가 가능하다 [사실]",
        "구조: 연체 해소 뒤 IDB의 첫 지급금으로 카타르에 상환하는 방안이며 관련 승인이 필요하다 [사실]",
        "참고: 앞서 10월 6일 보도는 카타르가 약 25억 달러 IDB 부채 해소용 기금을 마련하고 최대 80억 달러 신용선이 열릴 수 있다고 했다 [미확인]",
    ],
    "basis": "verified",
    "check": "카타르 브리지론·20억 달러 이상 연체·2018년 대출 중단은 인덱스박스·베네수엘라애널리시스 검색 결과 요약으로 확인",
    "src": [
        {"o": "인덱스박스", "d": D, "u": "https://www.indexbox.io/blog/venezuela-weighs-qatar-bridge-loan-to-clear-2-billion-idb-arrears/"},
        {"o": "베네수엘라애널리시스", "d": "2026-10-06", "u": "https://venezuelanalysis.com/news/venezuela-qatari-fund-to-unblock-access-to-idb-loans/"},
    ],
    "inds": ["macro"], "nodes": ["macro/liquidity"],
    "vc": [{"ind": "macro", "node": "liquidity", "f": "공급", "dir": "up", "k": "예상", "t": "베네수엘라 IDB 연체 해소용 카타르 브리지론 검토"}],
    "items": [
        it("베네수엘라, IDB 연체 해소 위해 카타르 브리지론 모색", R, "https://www.reuters.com/world/americas/venezuela-eyes-qatar-bridge-loan-clear-idb-arrears-sources-say-2026-10-22/"),
    ],
})

# G2-089
items.append({
    "cid": "G2-089", "attachTo": "",
    "title": "일렉트로룩스 3분기 조정 영업이익 9.12억 크로나로 예상 상회…순손실 3.4억 크로나",
    "one": "\n".join([
        "일렉트로룩스의 3분기 조정 영업이익이 비용 절감 덕에 시장 예상을 넘었다.",
        "· 조정 영업이익은 9억 1,200만 크로나로 예상치 8억 6,700만 크로나를 웃돌았다.",
        "· 다만 순손실 3억 4,000만 크로나를 냈고 연간 물량·가격·믹스 기여 전망을 중립으로 낮췄다.",
    ]),
    "facts": [
        "무엇이: 일렉트로룩스의 3분기 조정 영업이익이 9억 1,200만 크로나로 회사 집계 예상 8억 6,700만 크로나를 넘었고 유기적 매출은 3.5% 늘었다 [사실]",
        "손익: 순매출은 339억 2,000만 크로나였고 순손실 3억 4,000만 크로나로 순이익 예상 6,360만 크로나에 못 미쳤다 [사실]",
        "비용: 비용 효율화가 14억 크로나를 보탰지만 중동 분쟁에 따른 원자재·물류비와 미국 관세가 부담이 됐다 [사실]",
        "전망: 연간 물량·가격·믹스의 영업이익 기여 전망을 긍정에서 중립으로 낮췄다 [사실]",
    ],
    "basis": "verified",
    "check": "회사 3분기 보고서·RTE 보도(검색 결과 요약)로 확인",
    "src": [
        {"o": "일렉트로룩스 3분기 보고서", "d": D, "u": "https://www.electroluxgroup.com/en/electrolux-group-interim-report-q3-2026-47822/"},
        {"o": "RTE", "d": D, "u": "https://www.rte.ie/news/business/2026/1023/1596546-electroluxs-third-quarter-results/"},
    ],
    "inds": ["consumer"], "nodes": [],
    "vc": [{"ind": "consumer", "node": "durables", "f": "수요", "dir": "down", "k": "예상", "t": "일렉트로룩스 물량·가격·믹스 전망 중립으로 하향"}],
    "items": [
        it("일렉트로룩스, 3분기 핵심 이익 시장 예상 상회", R, "https://www.reuters.com/business/electrolux-q3-core-profit-tops-expectations-2026-10-23/"),
    ],
})

# G2-099
items.append({
    "cid": "G2-099", "attachTo": "",
    "title": "한국은행, 해외 이전 이력 코인 보유자 거래내역·잔액·개인정보 매달 보고받는다",
    "one": "\n".join([
        "한국은행이 12월 3일 개정 외국환거래법 시행에 맞춰 가상자산 국경 간 이전 보고 체계를 마련하고 있다.",
        "· 거래소는 유출입 내역을 다음 날 오전 11시까지, 보유자 개인정보와 잔액을 매달 보고해야 한다.",
        "· 2024년 7월 19일 이후 해외 이전 이력이 있는 이용자 127만 2,878명이 대상이 될 수 있다.",
    ]),
    "facts": [
        "무엇이: 한국은행이 거래소에 일별 가상자산 유출입 내역과 월별 보유자 개인정보·잔액 보고를 요구하는 외환전산망 보고 체계를 마련 중이다 [사실]",
        "근거: 12월 3일 시행되는 개정 외국환거래법에 따른 국경 간 가상자산 이전 모니터링 강화 조치다 [사실]",
        "대상: 2024년 7월 19일 이후 한 번이라도 해외 이전거래를 한 이용자가 대상이며, 2026년 9월 30일까지 5대 거래소의 해당 이용자는 127만 2,878명이다 [사실]",
        "공유·논란: 보고 정보는 국세청·관세청·금감원·FIU와 공유되며, 박수영 의원은 과도한 개인정보 수집이 시장을 위축시킬 수 있다고 비판했다 [사실]",
    ],
    "basis": "verified",
    "check": "텔레그램이 건 디지털타임스 기사를 열어 확인",
    "src": [{"o": "디지털타임스", "d": D, "u": "https://www.dt.co.kr/article/12090844"}],
    "inds": ["fin"], "nodes": [],
    "vc": [{"ind": "fin", "node": "payments", "f": "수요", "dir": "down", "k": "예상", "t": "해외 이전 코인 보유자 매달 점검에 시장 위축 우려"}],
    "items": [
        it("해외거래 한 번이라도 하면 코인 보유자 내역·잔액 매달 점검", "텔레그램 미국 주식 인사이더", "https://t.me/insidertracking/67093"),
    ],
})

out = {"agent": "W2", "searches_used": 18, "fetches_used": 1, "items": items, "skipped": skipped}
json.dump(out, open("/home/user/news-desk/data/mix-2026-10-23/out2/W2.json", "w"), ensure_ascii=False, indent=1)
print(len(items))
