# 핸드오프 — 새 글 함께 묶기 2회(10월 8~9일·12~13일), 데스크 테마·읽음 보관, 요청 조사에 원문 전체 반영

작성 시점: 2026-10-13 14시 30분(KST). 이번 세션은 저장소(gyucheol/news-desk)에 연결된 Claude Code 클라우드 세션이었고, 작업은 브랜치 claude/busy-dirac-rdnh60에 커밋·푸시했습니다(시작 때 직전 브랜치 claude/sweet-heisenberg-x437s0을 앞으로 감음). PR은 만들지 않았습니다. 직전 핸드오프는 HANDOFF-prev-2026-10-09-18h.md입니다.
중요: 데스크의 '요청' 버튼이 여는 새 세션은 이제 이 브랜치(claude/busy-dirac-rdnh60)에서 시작합니다(desk/parts/js2.js의 CCR.rev). 다른 브랜치로 옮겨 작업하면 이 값도 바꾸고 페이지를 다시 게시해야 합니다.

---

## 1. 한눈에 보기

1. 텔레그램·블룸버그·로이터를 출처 구분 없이 함께 거르고 같은 흐름끼리 묶는 방식(data/mix-*/, tools/mk_mix.py)으로 두 번 저장했습니다.
   - 10월 8일 17시 45분~9일 18시 30분: 후보 325 → 남김 187 → 82묶음 → 새 문서 47건, 기존 문서 30건에 더함(기사 133). 근거: 확인 51, 일부 19, 채널 전언 3, 제목 기준 4.
   - 10월 12일 0시~13일 07시 50분: 후보 962(블룸버그 241·로이터 392·텔레그램 329) → 남김 544 → 168묶음(같은 문서에 붙는 묶음은 하나로 합침) → 새 문서 96건(n-bbg-0229~0264, n-rtr-0198~0230, n-tg-0225~0251), 기존 문서 60건에 더함(기사 498). 근거: 확인 84, 일부 35, 채널 전언 16, 제목 기준 21. 건너뜀 12.
   - 두 번 모두 DB를 다시 받아 저장 파일과 같음을 확인했습니다. 표본 대조는 각 2~3건뿐입니다.
2. 비어 있는 구간: 10월 9일 18시 30분~11일 24시(블룸버그·로이터·텔레그램 모두)는 처리하지 않았습니다. 10월 13일 07시 50분 이후도 아직입니다.
3. n-bbg-0210: 재검색 2회로도 원문 요약을 못 찾아 제목 기준 유지(check만 갱신).
4. chains(산업 한 페이지) 7개 문서에서 소급 묶기로 지운 문서 id 72곳을 남은 문서 id로 바꿈. n-tg-0200을 가리키는 1곳은 대신할 문서가 없어 그대로.
5. 데스크 페이지(같은 주소) Version 48~51:
   - v48 어두운 테마, v50 다크·라이트 바꾸기 버튼(기본 다크, 고른 값은 브라우저 localStorage 'deskTheme').
   - v49 요청 버튼 세션 브랜치를 이 브랜치로.
   - v51 읽음 기록을 계정별로 브라우저에도 보관(localStorage 'deskReads:<id>'). 링크로 공유받은 조직 밖 사람은 '보기' 권한이라 개인 저장소(data/users/<id>/reads)에 쓸 수 없어(플랫폼 규칙) 읽음이 사라지던 문제를 그 브라우저 안에서는 해결. 다른 기기에서는 유지되지 않음.
   - '내가 읽음 처리하면 공유받은 사람에게도 읽음' 문제는 원인을 찾지 못했습니다(개인 저장소는 서로 읽을 수 없고 코드에도 경로 없음). 사용자에게 그 사람의 로그인 계정·화면을 물어 둔 상태.
6. 요청한 뉴스 조사(tools/insight/): 묶음 뉴스의 원문 전체를 반영하도록 바꿈 — sources.py(원문 목록 + 텔레그램 본문 받기), INSIGHT_PROMPT.md('원문 N건 핵심' 절, 검색 한도 20+원문 수), RUN.md, check.py(원문 주소가 자세한 정리에 모두 있는지 검사). 실제 요청으로 끝까지 돌려 본 적은 없음.
7. 저녁 예약 작업(trig_014res2hazUFUcx55wHPWtoU, 매일 20:47 KST) 지시문을 읽어 확인: 대상은 processed가 최근 7일이고 meta/chainsLog.applied에 없는 카드. 그래서 이미 반영된 카드는 다시 반영되지 않고(중복 없음), 기사를 더 붙인 기존 문서의 새 내용도 반영되지 않습니다. 예약 작업은 바꾸지 않았습니다.
8. DB 현재: news 701건, meta/newsSeen v12, newsSeenOld v3, progressV4 v17, newsSeq bbg 264·rtr 230·tg 251.
9. 검색: 이번 세션 약 215회(에이전트 보고 합). '세션당 약 200회' 한도는 이번에 막히지 않았음(미확인 그대로).

---

## 2. 함께 묶기 절차 (data/mix-2026-10-13/ 기준, 다음에도 이 방식)

1. 목록
   - 텔레그램: for c in 11개 채널; python3 tools/tgcollect.py dump $c <시작 KST ISO> work/dumpN/$c.jsonl (seen 표시 포함).
   - 블룸버그·로이터: python3 -I tools/sitemap_list.py bbg|rtr <since UTC> --all > work/smN/bbg.txt (사용자 컴퓨터 불필요. 본문은 열리지 않음).
2. all.tsv(줄번호·출처 tg:<채널>|bbg|rtr·KST·제목/본문·주소) → in/F*.tsv(본문 260자) → Haiku 에이전트(노력 max, 지시서 FILTER.md, 320줄 안팎씩) → out/F*.tsv(K/D).
3. keep.tsv(본문 300~400자) + existing.tsv(최근 1주 문서) → Opus 1개, CLUSTER.md → clusters.json. 같은 attachTo를 가진 묶음은 메인 세션이 하나로 합침(clusters_orig.json이 원본).
4. python3 -I mk_bundles.py <DB 사본> <에이전트 수> → bundle/W*.md → Opus 에이전트, WRITE.md(검색 16회·열람 4회 이내) → out2/W*.json.
5. 작업 폴더에서 python3 -I ../../tools/mk_mix.py <DB 사본> <processed 날짜> <텔레그램 덤프 폴더> '<기간 설명>' → newsdocs/, meta_out/(progressV4·newsSeen·newsSeenOld), attached.txt. PROBLEMS 0이 될 때까지 out2만 고침.
6. 저장: ArtifactData batch(50개·1MiB 이하). 기존 문서는 list 결과의 version으로 if_version, meta는 마지막 배치에. 저장 뒤 다시 받아 대조, work/seen.txt·seen_urls.txt를 newsSeenOld+newsSeen으로 다시 만듦.
7. 주의: n-tg-0166(후티·사우디 흐름)은 기사 66건까지 커졌습니다. 너무 크면 나눌지 사용자에게 물을 것.

---

## 3. 남은 일

1. 10월 9일 18시 30분~11일, 10월 13일 07시 50분 이후 새 글.
2. 공유받은 사람에게 내 읽음이 보인다는 문제: 사용자 답(그 사람의 계정·화면)을 받아 확인.
3. 요청 버튼 첫 실사용(원문 전체 반영 절차) 결과 확인.
4. 표본 대조(두 번의 묶기 저장분), 이란 묶음(n-rtr-0014)·후티 묶음(n-tg-0166) 크기 확인.
5. 직전 핸드오프 3절의 남은 일 중 미처리: 레거시 dupOf 20건, 인사이트 시험 결과 대조, 9월 30일 이전 소급, 7월 텔레그램 252건, RUNBOOK 갱신.

---

## 4. 이어서 하는 절차 (Claude Code)

1. 브랜치 claude/busy-dirac-rdnh60을 받고, 압축 파일의 news-desk/work/를 저장소 work/에 풉니다(work/는 .gitignore 대상, live7이 최신 DB 사본).
2. DB를 새로 받습니다(meta, news limit 1000, chains; out_dir=work/liveN). 기존 문서를 고칠 때는 list 결과의 version을 씁니다.
3. 페이지 수정: desk/parts에서 python3 build.py v39.html ../index.html → Artifact publish(같은 주소). 시험 화면은 playwright(executablePath /opt/pw-browsers/chromium) + window.PREVIEW_CLAUDE 모의 객체(스크립트는 저장소에 없음).

---

## 5. 사용자 작업 규칙 (계속 적용)

1. 존댓말, 결론 먼저. 표는 쓰지 않고 보고서류에는 굵은 글씨를 쓰지 않습니다.
2. 근거가 부족하면 모른다고 밝히고 지어내지 않습니다. 추론이면 유형과 근거를 밝힙니다.
3. 링크에 근거했으면 답변 끝에 Sources. 게시된 페이지 주소는 요청이 없으면 채팅에 붙이지 않습니다.
4. 요청 범위 밖의 데이터·기능은 바꾸지 않습니다. 예약 작업과 메모리는 명시적 요청이 있을 때만 바꿉니다.
5. 같은 아티팩트를 같은 주소에 갱신합니다.
6. 요청 표현: "handoff" = 이 문서와 압축 파일. "ㄱㄱ"·"진행시켜" = 진행.
7. 무거운 작업은 서브 에이전트(Opus), 깊게 생각할 필요 없는 작업은 Haiku(노력 max). 토큰을 적게 쓰는 방법 우선.
8. 뉴스 고르기: AI 투자 증액류 제외, 축소·취소·연기류 포함. 블룸버그·로이터는 분야를 넓게.
9. 비슷한 뉴스 묶기: 출처와 상관없이 같은 흐름이면 묶고, 기존 문서와 같은 흐름이면 처음 저장한 문서에 더함(넓게). 새 기사를 더하면 다시 안 읽음. 모든 뉴스에 원문 링크.
10. 뉴스 내용 및 인사이트 요청: 묶음의 원문들을 모두 활용해 작성.
11. 대량 작업 전에는 총 건수부터 알려 드리고 진행 여부를 묻습니다.
12. 커밋: 세션의 지정 브랜치에 커밋·푸시.

---

## 6. 압축 파일 구성

news-desk/ (저장소 구조, .git 제외, work/는 live7·dump5·dump6·sm5·sm6·seen.txt·seen_urls.txt만), handoff.md(이 문서 사본).
