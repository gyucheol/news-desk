# 7월 텔레그램 요약 카드 작성 (서브 에이전트 공통 지시)

사용자는 2026년 7월부터의 산업 흐름을 파악하려고 텔레그램 글을 요약 카드로 받습니다.
당신은 배치 파일 하나(후보 약 27건)를 받아 후보마다 카드 1장을 씁니다. DB 저장은 하지 않습니다(메인 세션이 모아서 저장).

## 작업 폴더 (다른 에이전트와 섞이지 않게 자기 폴더만 씀)
- 입력: /home/user/news-desk/work/july/batchNN.json
- 출력: /home/user/news-desk/work/july/out/bNN/cards/<key>.json  (key는 배치 파일의 key 그대로)
- 보조 스크립트를 만들면 /home/user/news-desk/work/july/out/bNN/ 안에만 두세요. scratchpad 최상위는 쓰지 마세요.

## 먼저 읽을 것
1. /home/user/news-desk/tools/cardkit/mkcards_1002n.py — 카드 형식 예시(3장). 형식·문체·강조를 이대로 따릅니다.
2. /home/user/news-desk/tools/cardkit/GUIDE-short.md — 강조({{ }}) 기준.
3. /home/user/news-desk/tools/cardkit/check_cards.py — 검사 규칙(NODES 목록, 필드, 꼬리표 등).
4. 해당 산업 자료: /home/user/news-desk/work/brief/<산업>.txt — 현재 사이클 판정(cycle stage)과 노드, 이미 있는 카드.

## 카드 필드 (cardlib.card 형식, JSON으로 저장)
- key, source='텔레그램', channel(배치의 channel), published(대표 글 main의 시각, 'YYYY-MM-DDTHH:MM:00+09:00'), url('https://t.me/<채널>/<id>'), dupOf(''), insight({})
- inds: 관련 산업 id 목록(macro·power·gas·coal·uranium·drilling·petchem·jpins·beauty). 반도체는 macro, 노드 macro/semis.
- nodes: '산업/노드' 형식, check_cards.py의 NODES 안에서만.
- headline: 한 줄 제목(무엇이 — 핵심 수치).
- facts: 3~6개. 첫 항목은 '무엇이: ', 항목명 8자 이하 + ': '. 문장 끝에 꼬리표 [사실|귀납|연역|유추|추측] 중 하나.
- tags: 0~3개 {'s':0,'t':'<머리말> — 내용 [꼬리표]'}, 머리말은 동인·병목 이동·과열 신호·정책 충격·산업 통합·자본 철수·심리 극단·실물 공급 파괴 중 하나.
- cycles: 산업마다 {'ind','stage','why'}. stage는 brief의 현재 판정(매크로 1~4, 나머지 1~8). 이 사실이 현재 판정과 같은 방향인지 다른지 why에 밝힘.
- incentive: 발표·보도 주체의 동기 한 문장 [유추].
- check: 무엇으로 확인했고 무엇을 확인하지 못했는지 [사실].
- src: [{'o':출처 이름,'d':'YYYY-MM-DD','u':주소}] — 텔레그램 글(들) + 확인에 쓴 기사·1차 자료.
- 배치의 status가 follow면 기존 카드의 후속입니다. 배치의 dupOf에 기존 카드 id(n-…, pf-…, tg-…)가 있으면 카드의 dupOf에 넣고, facts 첫 항목을 '무엇이: 이미 다룬 사건(<그 id>)의 새 내용입니다 — …'로 시작하세요.

## 사실 확인 (가장 중요)
- 배치의 posts[].text가 원문입니다(전문). agentSummary/agentWhy는 다른 에이전트의 메모일 뿐 근거가 아닙니다.
- 핵심 수치·주장은 WebSearch/WebFetch로 다른 매체나 1차 자료 1곳 이상에서 확인하세요(카드당 웹 호출 3회 안팎으로 절약).
  reuters.com·bloomberg.com 본문은 막혀 있으니 전재 기사나 1차 자료를 쓰세요. t.me 글은 https://t.me/<채널>/<id>?embed=1 로 열 수 있습니다.
- 확인 못 한 것은 지어내지 말고 check에 '확인하지 못했습니다'로 적고, 해당 fact 꼬리표는 [사실]이 아니라 채널 주장임을 밝히세요(예: '채널에 따르면 …').
- 원문이 관심 산업과 무관하거나 근거가 너무 약하면 카드를 쓰지 말고 skip 목록에 이유를 남기세요.
- 여러 posts가 같은 사건이면 한 카드로 합치고 src에 모두 넣습니다.

## 검사 (모두 통과해야 끝)
cd /home/user/news-desk/work/july/out/bNN && python3 /home/user/news-desk/tools/cardkit/check_cards.py && python3 /home/user/news-desk/tools/cardkit/hlcheck.py
- check_cards: PROBLEMS 0. hlcheck: 문제·경고 0, 강조 비율은 GUIDE-short 기준.

## 끝낼 때
/home/user/news-desk/work/july/out/bNN/report.json 에 {"written":[key...], "skipped":[{"cid","key","reason"}], "unverified":[{"key","what"}]} 를 쓰고,
저에게는 3줄 이내로: 쓴 카드 수, 건너뛴 수, 검사 결과(PROBLEMS·경고 수)만 답하세요.
