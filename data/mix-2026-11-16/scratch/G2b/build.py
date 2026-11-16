import json, sys
from pathlib import Path

BASE = Path('/home/user/news-desk/data/mix-2026-11-16')

C = []
def add(theme, field, attach, core, lines):
    C.append({"theme": theme, "field": field, "attachTo": attach, "core": core, "lines": lines})

# 1. Nvidia CEO saga -> earliest Huang scandal doc
add("엔비디아 CEO 사태-황 복귀 공방·베센트 쇄신 요구·주가 급락", "semis", "n-tg-0826",
    ["젠슨 황, 中 스파이 의심 인물·부하 직원과 불륜 보도 뒤 사임",
     "황 복귀 청원 12만 명 서명…머스크 '황 없인 핵심 거래 잃을 것'",
     "황 복귀 타진·트럼프 '나쁘지 않아' vs 베센트 '외부 CEO로 쇄신'",
     "공매도 240억 달러 이익·HSBC 목표가 반토막·주주소송 보험 공백",
     "대만, 엔비디아 직원 칩 밀수를 국가안보 범죄로 수사"],
    [461, 556,
     5, 27, 29, 74, 92, 130, 152,
     189, 203, 204, 217, 219, 220, 254, 261, 400, 435, 496, 531, 600, 606, 609, 657,
     248, 267, 661, 702, 709, 134,
     187, 446])

# 2. Export controls -> Taiwan AI chip export-control doc
add("엔비디아 사태 후폭풍-美 AI칩 수출통제 강화", "semis", "n-bbg-0338",
    ["美 BIS, AI칩 원격접근 규제…싱가포르 등 5개국 수출 허가 추가",
     "美 의회, 러트닉에 엔비디아 수출 단속 해명 요구…통제 공감대 확산",
     "로이터 '中 인민해방군 연계 대학, 지난달 엔비디아 H200 구매'",
     "노무라 '대중 칩 법안 시행 시 HBM 수요 2% 미만·D램 0.5% 감소'"],
    [584, 614, 703, 198, 590, 627, 165, 159, 307, 478])

# 3. AI funding (n-tg-0743 already used by G2a-009 -> new cluster, theme tag)
add("AI 자금조달-엔비디아 자금줄 축소·아시아 DC 대출 지연", "ai", "",
    ["WSJ '엔비디아 백지수표 시대 끝'…황도 8월부터 보증 기준 강화",
     "엔비디아 5천억 달러 AI 금융지원, 잔존가치 보증 25%에 딜 0건",
     "황 퇴진에 엔비디아의 네오클라우드·고객사 지원 의구심 확산",
     "아시아 데이터센터 대출 신디케이션 이례적 지연"],
    [450, 442, 654, 83, 320, 441])

# 4. Memory prices -> Nov 2 merged memory doc
add("메모리 가격-낸드 현물 20%↓·공급 과잉·AI 수요 과대 계상 우려", "semis", "n-tg-0297",
    ["BofA, 낸드 현물가 10월 중하순 이후 20%↓·웨이퍼 14.3달러",
     "삼성·SK, 中 AI 기업 주문 감소에 eSSD 물량 美 CSP로 전환",
     "모건스탠리 '美 DC 5GW 2029년으로 지연·2028년 이후 공급 증가'",
     "Verte '메모리 가격 위쪽은 좁아지고 아래쪽은 열려'",
     "알트먼 '칩 업체들, 우리가 다 살 거라 가정'…AI 수요 이중 계산"],
    [491, 256, 477, 273, 674])

# 5. AI capex cycle slowdown -> Goldman capex-cycle doc
add("AI 투자 사이클 둔화-SemiAnalysis 전망 하향·과열 경고", "ai", "n-tg-0559",
    ["세미애널리시스, 2028년 AI 가속기 투자 전망 28%·2030년 40%↓",
     "현대경제연구원 '美 AI 투자, 2028년 전후 둔화 가능'",
     "맥쿼리, 설비투자 슈퍼사이클 속 데이터센터 과열 경고"],
    [557, 563, 581, 176, 678])

# 6. AI listings -> AI IPO doc
add("AI 상장-앤트로픽 IPO 매출 의문·클로드 사용 정체", "ai", "n-bbg-0671",
    ["앤트로픽 IPO, 엔비디아 사태 직후 AI 매출·밸류 시험대에 올라",
     "MS 데이터 '오피스 내 클로드 사용량, 코파일럿의 10% 미만'"],
    [719, 541, 492, 641])

# 7. Canadian telecom -> Canadian telecom stocks doc
add("캐나다 통신-퀘베코, 텔러스 217억 달러 인수 제안", "tech", "n-bbg-0828",
    ["퀘베코, 경쟁사 텔러스에 217억 달러 인수 제안",
     "퀘베코 주주 피에라 지지…스타링크 위협 부각",
     "텔러스 CEO, 광통신 자산 가치 들어 퀘베코 제안 비판"],
    [567, 685, 713])

# 8. DRAM antitrust class action (no existing doc)
add("메모리 3사 D램 담합 집단소송-각하 신청 기각", "semis", "",
    ["美 법원, 삼성·SK·마이크론 D램 담합 소송 각하 신청 기각(14일)"],
    [162, 382, 560])

# 9. AI sell-off (n-bbg-0449 already used by G2a-010 -> new cluster, theme tag)
add("AI 매도 시황-아시아 반도체주 재하락·약세 전망", "ai", "",
    ["엔비디아 사태·앤트로픽 IPO에 아시아 반도체주 재차 하락",
     "캐피털 이코노믹스 'AI주 하락세 더 깊어질 수도'",
     "버리, 나스닥 약세 베팅 확대…'내년 반도체주 하락' 전망"],
    [412, 444, 247])

# single-line clusters attached to existing flows
add("AI 신용위험-IMF 총재 순환금융 경고", "ai", "n-tg-0702",
    ["IMF 총재 '세계경제 AI 한쪽 다리'…순환금융 1조 달러·3분의 2 부채"], [409])
add("AI 반발-아일랜드 데이터센터 소송", "ai", "n-rtr-0719",
    ["아일랜드 데이터센터 소송, 에너지 정책 점검대에 올라"], [141])
add("AI 감원-인도 IT 인력 대량 해고 위기", "ai", "n-rtr-0027",
    ["AI 도입에 인도 IT 인력 대량 해고 위기…아웃소싱 모델 흔들"], [146])
add("인텔 가이던스 쇼크-주주 집단소송", "semis", "n-bbg-0817",
    ["인텔, 주가 29% 폭락 뒤 실적 악화 은폐 의혹 집단소송 피소"], [404])
add("메타 규제·소송-이탈리아 과징금", "tech", "n-rtr-0712",
    ["이탈리아, 이용자 사진 접근 문제로 메타에 8억 500만 과징금"], [17])
add("플랫폼 아동 보호-로블록스 상원 청문회", "tech", "n-rtr-0036",
    ["美 상원, 로블록스 중심 아동 안전 청문회 예정"], [708])
add("PE 소프트웨어 인수-프루프포인트 차입", "tech", "n-rtr-0267",
    ["토마브라보 계열 프루프포인트, M&A용 20억 달러 차입 착수"], [649])
add("버진미디어 O2 신용-무디스 강등", "tech", "n-bbg-0536",
    ["무디스, 턴어라운드 우려로 버진미디어 O2 신용등급 강등"], [683])
add("스마트 안경 시장-AR 글래스 출하 전망", "tech", "n-rtr-0651",
    ["AR 글래스 출하량, 내년 2배 증가 전망"], [77])

# single-line new clusters
add("중국 AI 연산력 부족-딥시크 사용량 제한", "ai", "",
    ["딥시크, 연산력 부족에 입력 4만 자·일일 대화량 제한"], [353])
add("신(新) 차이나 쇼크-세계 AI·자동차 산업 위협", "ai", "",
    ["블룸버그 '새 차이나 쇼크, 세계 AI·자동차 산업 위협'"], [548])
add("바이두 실적-매출 6분기 연속 감소", "tech", "",
    ["바이두, AI 부담 지속에 매출 6분기 연속 감소"], [443])
add("리노공업 3Q 어닝쇼크-생산 차질", "semis", "",
    ["리노공업 3Q 영업익 394억 원, 컨센 16% 하회…목표가 7만 원"], [405])
add("파크시스템스 3Q-컨센 하회·EPS 하향", "semis", "",
    ["파크시스템스 3Q 영업익 121억 원, 컨센 33% 하회…EPS 17% 하향"], [406])
add("마이크로소프트 세계 장애-7월부터 숨은 버그", "tech", "",
    ["MS, 7월부터 못 찾은 버그가 세계적 서비스 장애 유발"], [681])
add("카카오-AI 대응 그룹 분할", "tech", "",
    ["카카오, AI 경쟁 대응해 인터넷 제국 역사적 분할 준비"], [293])
add("캐나다 감청법 C-22-빅테크 반발", "tech", "",
    ["카니 정부 감청 허용법 C-22에 메타·구글·애플 반발"], [502])
add("남아공 통신-MTN 텔콤 인수 협상 재개", "tech", "",
    ["MTN, 텔콤 인수 협상 재개…텔콤 주가 7년 만에 최고"], [402])
add("디케이티 3Q-영업익 추정 55% 상회", "tech", "",
    ["디케이티 3Q 영업익 129억 원, 추정치 55% 상회"], [538])

DROP = [
    (41, "한국 증시 신용융자 쏠림(비미일 증시·금융 규제, 10/30 지시)"),
    (60, "한국 증시 신용융자 쏠림(비미일 증시·금융 규제, 10/30 지시)"),
    (72, "중요도 낮음(국내 개인 엔비디아 순매수 동향)"),
    (153, "중요도 낮음(젠슨 황 인물 일화)"),
    (251, "중요도 낮음(넷플릭스 체험 사업 뉴스레터)"),
    (423, "중요도 낮음(소형 통신망 보안 제휴)"),
    (533, "반도체·AI 긍정(AI 서버 부품 공급 부족·리드타임 증가, 10/30 지시)"),
    (591, "이미 다룸(n-bbg-0133, 10월 8일 밴스 H-1B·영주권 조치 재탕)"),
    (653, "이미 다룸(n-bbg-0817, 인텔 폭락 정부 지분 120억 달러 손실)"),
    (672, "중요도 낮음(아이폰 듀오 기능 추가)"),
]

# order: bigger clusters first (stable for ties)
order = sorted(range(len(C)), key=lambda i: (-len(C[i]["lines"]), i))
clusters = []
for n, i in enumerate(order, 1):
    c = C[i]
    clusters.append({"cid": f"G2b-{n:03d}", "theme": c["theme"], "field": c["field"],
                     "attachTo": c["attachTo"], "core": c["core"],
                     "lines": c["lines"]})
out = {"clusters": clusters, "drop": [{"line": l, "reason": r} for l, r in DROP]}

# ---- checks ----
keep = [int(l.split('\t', 1)[0]) for l in (BASE / 'keep_G2b.tsv').read_text().splitlines() if l.strip()]
used = [l for c in clusters for l in c["lines"]] + [d["line"] for d in out["drop"]]
errs = []
if len(keep) != len(set(keep)):
    errs.append('keep has duplicate line numbers')
dup = sorted({x for x in used if used.count(x) > 1})
miss = sorted(set(keep) - set(used))
extra = sorted(set(used) - set(keep))
if dup: errs.append(f'duplicate: {dup}')
if miss: errs.append(f'missing: {miss}')
if extra: errs.append(f'not in keep: {extra}')
for c in clusters:
    if not 1 <= len(c["core"]) <= 5:
        errs.append(f'{c["cid"]} core count {len(c["core"])}')
    for k in c["core"]:
        if not 15 <= len(k) <= 45:
            errs.append(f'{c["cid"]} core length {len(k)}: {k}')
att = [c["attachTo"] for c in clusters if c["attachTo"]]
if len(att) != len(set(att)):
    errs.append('attachTo reused within group')
sizes = [len(c["lines"]) for c in clusters]
if sizes != sorted(sizes, reverse=True):
    errs.append('clusters not ordered by size')

if errs:
    print('ERRORS:'); print('\n'.join(errs)); sys.exit(1)

(BASE / 'clusters_G2b.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
single = sum(1 for c in clusters if len(c["lines"]) == 1)
print(f'keep lines {len(keep)}, covered {len(used)}; clusters {len(clusters)}, single {single}, '
      f'attachTo {len(att)}, drop {len(out["drop"])}')
