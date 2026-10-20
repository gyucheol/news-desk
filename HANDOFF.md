# 핸드오프 — 회차 3번(10월 17일 2차·18일·20일), 안 읽은 문서 합치기·재작성, 강관 PDF, 한줄 요약 규칙 강화

작성 시점: 2026-10-20 오전(KST). 이번 세션('뉴스 읽음처리 및 투자 인사이트', session_01XpkKhzMUenzCqhzFWvkjVQ)은 저장소 gyucheol/news-desk를 /home/user/gyucheol/news-desk에 받아 썼고(/home/user/news-desk는 그 클론을 가리키는 심볼릭 링크라 도구의 '/home/user/news-desk' 경로가 그대로 동작), 작업은 브랜치 claude/news-round-2026-10-17b에 커밋·푸시했습니다(claude/youthful-thompson-02m8hc에서 시작). PR은 만들지 않았습니다. 직전 핸드오프는 HANDOFF-prev-2026-10-17-eve.md입니다.

---

## 1. 한눈에 보기

1. 회차 3번 (절차는 직전 핸드오프 2절 + 아래 2절)
   - 10월 17일 2차(data/mix-2026-10-17b): 17일 10시 50분~20시 30분, 후보 163 → 거르기 74 → 묶음 22(엄격) → 새 문서 1, 기존 문서에 더함 18, 기사 46.
   - 10월 18일(data/mix-2026-10-18): 17일 20시 30분~18일 20시 30분, 후보 321 → 153 → 묶음 43(엄격) → 새 6, 더함 36, 기사 114.
   - 10월 20일(data/mix-2026-10-20): 18일 20시 30분~20일 7시(월요일 포함), 후보 1,110 → 614 → 사용자가 '더 엄격하게(주요 흐름만)' 선택 → 분야별 2그룹 묶기(G1 291·G2 323, 목표 6분의 1) → 82묶음 → 새 31, 더함 50, 기사 427(verified 48, partial 30, channel 3).
2. 안 읽은 문서 합치기(사용자 "내가 안 읽음 한 것들까지 해서 묶어 줘", '합쳐서 문서 수 줄이기' 선택, data/merge-2026-10-20)
   - 당시 안 읽음 44건(U 42, P 2) 중 11묶음, 15건 흡수·삭제. 규칙은 10월 9일 합치기와 같음(keep=같은 흐름 가장 이른 문서, absorb=U만, P는 흡수 안 함).
   - 흡수된 문서를 가리키던 산업 페이지 nid 79곳(11개 산업)을 keep id로 바꿈(링크만). newsSeen·Old·Old3·Old4 줄의 id도 keep으로 바꿈.
   - 같은 회차 새 글 묶음이 흡수된 문서를 가리키면 keep으로 옮기고, 같은 문서를 가리키는 묶음은 하나로 합친 뒤 작성.
3. 한줄 요약 규칙 강화(사용자 지시, 규칙 24) → 안 읽은 묶음 문서 93건 점검, 45건 제목·한줄·사실 재작성(data/rewrite-2026-10-20, 검색 없이 문서 안 원문 내용만, update로 title·headline·one·facts만 바꿈, updatedAt 그대로).
   - 원인: mk_bundles.py가 기존 문서의 제목·한줄·사실 5줄만 넘기고 이미 묶인 원문(원문별 한줄 s)을 넘기지 않았음 → data/mix-2026-10-20/mk_bundles.py부터 사실 전부·추가된 내용·묶인 원문 목록(강조 {{ }} 지움)을 넘김. WRITE.md 1절 3번·한줄 요약 절, MERGE.md에 규칙 반영.
4. 산업 한 페이지 강관(OCTG) PDF: data/industry-pdf/강관-OCTG-2026-10-19.pdf(해양시추·OCTG 페이지의 OCTG·강관 부분 발췌, 기준일 10월 17일), 만든 스크립트 tools/industry/octg_pdf.py(HTML → Chromium headless 인쇄, 글꼴 design/fonts/PretendardVariable.woff2).
5. 기타
   - 거르기 에이전트가 실수로 만든 빈 원격 세션 session_019yyDSza7bHib7RdZYMzsCU는 사용자 승인으로 보관(archive) 처리.
   - 새 산업 후보 '포장재'(실간·트리비움 인수, n-bbg-0355)는 사용자가 추가하지 말라고 함(규칙 25). 그 문서의 포장재 vc 줄은 뺐음.
   - 산업 저녁 자동 업데이트: 10월 17일 밤에는 chainsLog가 v7 그대로였고, 10월 20일 아침에는 v9(그 사이 돌았던 것으로 보임). 전용 세션 기록은 확인하지 않았음.
6. DB 현재(10월 20일 아침 저장 뒤): news 997, chains 23(합치기로 11개 nid만 바뀜: aero v4·agri v5·drilling v12·fin v4·gas v13·macro v13·oil v4·petchem v12·semis v4·shipping v4·tech v4), meta newsSeen v22·newsSeenOld v6·Old2 v1·Old3 v3·Old4 v3·progressV4 v27·chainsLog v9. 최신 사본 work/live31(압축 파일).

---

## 2. 회차 절차 (바뀐 점만)

1. 새 회차 폴더에 복사할 최신판은 data/mix-2026-10-20/(FILTER·CLUSTER·WRITE.md, build_all.py, mk_bundles.py, mk_keep.py, fix_urls.py, chan.json). 바꿀 곳: build_all.py의 W·LIVE·prev(직전 두 회차 폴더)·smN·dumpN, WRITE.md '오늘은' 날짜, CLUSTER.md의 '오늘(…)'·'이번 회차(…)' 날짜, 세 md의 work/liveN 경로(10월 20일판은 합치기 때문에 work/live29m을 가리킴 → 새 사본으로).
2. CLUSTER.md '목표' 줄은 10월 20일판이 '6분의 1(더 엄격하게)'임. 다음 회차에는 건수 알려 드리고 묶기 방식을 다시 물을 것(엄격 4분의 1 / 더 엄격 6분의 1).
3. 수집 스크립트: work/collect14.sh(텔레그램 11채널 dump + bbg·rtr sitemap + fedspeech, 백그라운드, 끝나면 work/log14/ALL). 다음 since: 블룸버그·로이터·연준 2026-10-19T21:30:00Z(직전 회차 마지막 글 10월 20일 7시 14분 KST), 텔레그램 dump 시작 2026-10-20T06:30 KST(progressV4.telegram.new 다음 id만 쓰임).
4. 후보가 많으면 거르기 Haiku를 약 185줄씩 여러 개(10월 20일 6개), 묶기 Opus는 300줄 안팎씩 분야 그룹으로 나눔(G1: geo energy metals power trade shipping agri industrial auto aero consumer realestate / G2: macro rates fed fin ai tech semis pharma other). 두 그룹이 같은 기존 문서에 붙으면 작성 전에 묶음을 하나로 합칠 것(mk_mix는 같은 attachTo를 두 번 받으면 뒤의 제목·한줄로 덮음).
5. mk_mix 검사에서 자주 나온 것: partial인데 src 빈 것 → channel/title로 낮추고 꼬리 붙임, fed 항목 role 빈 것 → 사람이 아니면 who '연준'·role에 내용 설명.
6. newsSeenOld가 256KB를 넘으면: mk_mix가 옮긴 줄만 newsSeenOld4에 덧붙이고(count·updated 갱신), mk_mix의 newsSeenOld.json은 newsSeenOld.unused.json으로 이름 바꾸고 원래 Old를 저장. 10월 18일·20일 회차에 이렇게 함(Old4 지금 약 164KB).
7. 저장은 batch 900KB·50건 이하로 나누고, 삭제와 meta는 마지막 batch. 저장 전 query로 버전 받아 사본과 대조, 저장 뒤 processed로 다시 받아 대조.

---

## 3. 남은 일

1. 다음 '오늘자 뉴스 ㄱㄱ'부터 새 규칙(24)으로 쓰이는지 첫 회차 결과를 몇 건 직접 확인.
2. 산업 저녁 자동 업데이트(전용 세션 session_015NFMUw3CuVTBrLXt9nXVWt, 예약 20시 47분) 결과 확인. 이번 세션 3회차의 뉴스가 산업 페이지에 들어갔는지 chainsLog.applied로 확인.
3. 사용자에게 제안해 둔 것(답 없음): 세아제강 3분기 자세히(n-tg-0278)도 PDF로 만들지, 산업 페이지를 최신으로 갱신한 뒤 강관 PDF를 다시 만들지.
4. 직전 핸드오프 3절의 질문들(뉴스 화면에 남은 숫자 표시, 저장된 {{ }} 지울지, 읽은 뉴스 vc, 인사이트 4건 다시 쓸지, 탄산리튬 날짜 불일치)은 아직 못 물음.
5. 이전부터 남은 일(그대로): 연준 칸 보강, 국면 재판단 후보(매크로·전력·우라늄), 공유받은 사람 읽음 문제, 레거시 dupOf, 9월 30일 이전 소급, 7월 텔레그램 252건, RUNBOOK 갱신, merge_docs.py·mk_one_tg.py가 newsSeenOld만 읽음.
6. 확인 못 한 것: 10월 20일 작성 에이전트가 묶음 제목의 금액 단위를 고친 곳 2곳(로슈–한서 15억→150억 달러 이상, 한 거래 150억 달러→150억 파운드)은 에이전트 검색 근거이고 직접 확인 안 함.

---

## 4. 이어서 하는 절차 (Claude Code)

1. 지정 브랜치를 받고(필요하면 claude/news-round-2026-10-17b로 앞으로 감기), 압축 파일의 work/를 풀거나 DB를 새로 받음(meta·chains list 100, news list 1000 두 번, data/users/me reads·detailReq). 그 뒤 python3 -I tools/mk_seen.py <사본>.
2. 저장소를 /home/user/news-desk가 아닌 곳에 받았으면 ln -sfn <클론> /home/user/news-desk (도구 경로가 박혀 있음).
3. 안 읽음 판단: reads.ids[id] >= updatedAt(ms)일 때만 읽음. 보호(P) = detail·insight2가 있거나 detailReq ids·sent에 있음.
4. 데이터를 페이지보다 먼저 바꾸지 말 것(이번 세션은 페이지를 바꾸지 않았음, 데스크 Version 76 그대로).

---

## 5. 사용자 작업 규칙 (계속 적용, 24~25 추가)

1. 존댓말, 결론 먼저. 표는 쓰지 않고 보고서류에는 굵은 글씨를 쓰지 않습니다.
2. 근거가 부족하면 모른다고 밝히고 지어내지 않습니다. 추론이면 유형과 근거를 밝힙니다. 애매하면 먼저 묻습니다.
3. 링크에 근거했으면 답변 끝에 Sources. 게시된 페이지 주소는 요청이 없으면 채팅에 붙이지 않습니다.
4. 요청 범위 밖의 데이터·기능은 바꾸지 않습니다. 예약 작업과 메모리는 명시적 요청이 있을 때만 바꿉니다.
5. 같은 아티팩트를 같은 주소에 갱신합니다.
6. 요청 표현: "handoff" = 이 문서와 압축 파일. "ㄱㄱ"·"ㄱㄱㄱ"·"진행시켜"·"가"·"ㅇㅇ"·"이어서 ㄱㄱ" = 진행(단 선택지 질문에 대한 "가"는 '가' 선택지). "오늘자 뉴스 ㄱㄱ" = 회차. "산업 한 페이지에 전부 업데이트" = 산업 업데이트(수동).
7. 무거운 작업은 서브 에이전트(Opus), 깊게 생각할 필요 없는 작업은 Haiku(노력 max). 토큰을 적게 쓰는 방법 우선.
8. 뉴스 고르기: 반도체 투자 증액과 AI 투자 증액만 뺌. 축소·취소·연기류는 넣음. 그 밖의 모든 산업은 남김. 블룸버그·로이터는 분야를 넓게.
9. 비슷한 뉴스 묶기: 출처와 상관없이 같은 흐름이면 묶고, 기존 문서와 같은 흐름이면 처음 저장한 문서에 더함(넓게). 새 기사를 더하면 다시 안 읽음. 모든 뉴스에 원문 링크. 큰 묶음도 나누지 않음(10월 17일 답).
10. 뉴스 내용 및 인사이트 요청: 묶음의 원문들을 모두 활용해 작성. 버튼이 막히면 저장된 요청을 Claude Code에서 처리(tools/insight/RUN.md).
11. 대량 작업 전에는 총 건수부터 알려 드리고 진행 여부를 묻습니다(예외: 저녁 자동 업데이트는 묻지 않고 진행 후 보고).
12. 커밋: 세션의 지정 브랜치에 커밋·푸시(작성 중인 파일도 stop hook 때문에 중간 커밋함).
13. 강조 {{ }}는 쓰지 않음. 화면에도 보이지 않음. 원문별 한줄 요약은 그대로.
14. 기존 데이터 소급 수정은 사용자가 안 읽은 문서에만(읽음 = reads 시각 ≥ updatedAt). 범위가 다르면 물을 것. 단 숫자 오류 정정은 물어서 진행(n-tg-0125).
15. 뉴스 목록 버튼 순서는 '읽음 처리'가 앞. 읽음 애니메이션은 넣지 않음.
16. 인사이트 결과를 PDF로 달라고 하면 이미 만든 것이 있으면 그대로 전달. .md로 달라고 하면 tools/insight/to_md.py로 옮겨 SendUserFile.
17. 산업 데스크: 뉴스에 나오는 모든 산업은 '산업 한 페이지'를 가짐. 새 산업이 나오면 BUILD.md로 페이지를 만들어 추가(저녁 자동은 만들지 않고 보고만).
18. 모든 뉴스에 밸류체인 한 줄(vc). 새 뉴스는 작성 단계에서, 지난 뉴스는 안 읽은 문서에만.
19. 매크로에 연준 인사 발언과 관련 뉴스를 꼭 담음(fed 목록, who·role 채움).
20. 묶기는 '엄격' 기준을 계속 씀. 사용자가 바꾸라고 할 때까지.
21. (새) 추가된 내용: 같은 회차의 여러 글은 새 문서 하나로 겹침 없이 정리(added 없음). 이전에 보여 드린 문서에 글을 더하면 '추가된 내용: [출처·건수] — ~ 내용이 추가됨' 한 줄을 꼭 씀.
22. (새) 뉴스 화면에 숫자 표시를 줄이는 중: '안 읽은 것만'·'모두 읽음'·날짜 옆 건수는 지움. 다시 넣지 말 것.
23. (새) 산업 한 페이지 저녁 자동 업데이트는 전용 세션 + 예약 작업(20시 47분)으로 돎. 절차는 tools/industry/NIGHTLY.md.
24. 한줄 요약 = 묶인 모든 원문의 내용 + 문서 본문의 내용을 합친 요약. 기존 문서에 붙일 때는 이전 회차에 묶인 원문까지 포함해 다시 요약하고, 원문에 있는데 본문(사실)에 없는 핵심 내용은 사실에 더함. mk_bundles.py가 기존 문서의 사실 전부·추가된 내용·이미 묶인 원문 목록(원문별 한줄)을 작성 에이전트에게 넘김(data/mix-2026-10-20 판부터).
25. 새 산업 '포장재'는 산업 한 페이지에 추가하지 않음(사용자 지시).

---

## 6. 압축 파일

news-desk-handoff-v19.zip
- news-desk/: 저장소 구조(.git 제외). work/에는 live31(10월 20일 재작성 뒤 DB 사본: news 997, chains 23, meta 16, data/users/me reads·detailReq), sm14·dump14(10월 20일 회차 수집본), collect14.sh, seen.txt·seen_urls.txt.
- handoff.md: 이 문서 사본.
