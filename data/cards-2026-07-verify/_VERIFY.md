# 7월 카드 재확인 (서브 에이전트 공통 지시)

이미 쓴 텔레그램 요약 카드 중, 다른 매체로 확인하지 못한 내용이 있는 카드를 다시 확인해 고칩니다.
이제 네트워크가 넓어져 대부분의 기사 사이트를 WebFetch로 열 수 있습니다(cnbc·investing 등 일부는 사이트가 막음, reuters·bloomberg 본문도 막힘).

## 폴더 (자기 폴더만 사용)
- /home/user/news-desk/work/july/verify/vNN/cards/*.json — 고칠 카드(제자리 수정)
- /home/user/news-desk/work/july/verify/vNN/unverified.json — 처음 작성자가 남긴 미확인 항목(카드 key별)
- 보조 스크립트는 vNN/ 안에만 둡니다.

## 할 일 (카드마다)
1. check 문장, '채널 전언'·'채널에 따르면'이 붙은 facts, unverified.json 항목을 봅니다. 원문은 카드 src의 t.me 주소(?embed=1)로 볼 수 있습니다.
2. WebSearch로 찾고 WebFetch로 기사나 1차 자료(정부·기관·기업 발표, 통계)를 열어 수치·사실을 대조합니다. 카드당 웹 호출 4회 안팎, 전체 검색은 60회 안팎으로 아낍니다.
3. 결과에 따라 고칩니다.
   - 확인됨: '채널 전언/채널에 따르면' 표현과 꼬리표 '[사실(채널 전언)]' 등을 [사실]로 바꾸고, src에 확인 출처 {'o','d','u'}를 추가, check를 '…로 확인했습니다'로 고칩니다.
   - 어긋남: 확인된 값으로 고치고 check에 '채널은 X, 매체는 Y'처럼 차이를 적습니다. headline도 필요하면 고칩니다.
   - 끝내 확인 안 됨: 그대로 두고 check에 무엇을 찾아봤는지 짧게 남깁니다.
   - 사실이 틀린 것으로 드러나 카드 자체가 성립하지 않으면 카드를 지우지 말고 report의 drop에 이유를 적습니다.
4. 형식·문체·강조({{ }})는 기존 카드와 GUIDE(/home/user/news-desk/tools/cardkit/GUIDE-short.md)를 따릅니다. 새 내용을 지어내지 않습니다.

## 검사 (통과해야 끝)
cd /home/user/news-desk/work/july/verify/vNN && python3 /home/user/news-desk/tools/cardkit/check_cards.py && python3 /home/user/news-desk/tools/cardkit/hlcheck.py
→ PROBLEMS 0, 경고 0.

## 끝낼 때
vNN/report.json: {"verified":[key...], "corrected":[{"key","what"}], "still_unverified":[{"key","what"}], "drop":[{"key","reason"}]}
저에게는 3줄 이내로 개수와 검사 결과만 답하세요. 웹 검색 한도에 걸리면 그때까지 한 것을 저장하고 그 사실을 알려 주세요.

## 웹 검색 한도(WebSearch 200회)에 걸렸거나 아끼고 싶을 때 — Bash 검색 도구
WebSearch는 세션 전체가 함께 쓰는 한도가 있어 금방 바닥납니다. 처음부터 아래 도구를 주로 쓰세요(한도 없음).
- 뉴스 검색(기사 원래 주소 + 요약): python3 /home/user/news-desk/tools/websearch.py "검색어" [--lang ko] [--n 8]
- 구글 뉴스(보도 존재·제목·매체·날짜 확인): python3 /home/user/news-desk/tools/websearch.py "검색어" --gnews [--lang ko]
- 일반 검색(기관·기업 1차 자료 찾기): python3 /home/user/news-desk/tools/websearch.py "검색어" --web
- 기사 본문 뽑기(키워드 주변 문장만): python3 /home/user/news-desk/tools/websearch.py --fetch <주소> --grep 단어1,단어2
  (WebFetch로 열어도 됩니다. msn.com 전재 기사는 자바스크립트로 그려져 --fetch로는 빈 결과가 나올 수 있으니 WebFetch를 쓰세요.)
- 로이터·블룸버그 기사는 msn.com·yahoo·marketscreener·rigzone 등 전재본을 찾아 쓰세요.
