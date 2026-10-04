# 뉴스 수집 절차 (다운턴 뉴스 선별 데스크)

대상 아티팩트: https://claude.ai/artifact/1QxhURJDYUkJG1Je8g9ARB (DB: news, meta, chains)
카드 형식·검사 규칙은 핸드오프 문서와 압축 파일의 news-work/(cardlib.py, check_cards.py, hlcheck.py, run_mk.py)를 따른다.

## 0. 세션 시작

1. 클라우드 환경 Network access(Custom)에 t.me, www.bloomberg.com, www.reuters.com이 허용돼 있어야 한다.
   확인: `curl -s -o /dev/null -w '%{http_code}' https://t.me/s/HANAchina` → 200
2. ArtifactData list(collection=meta, out_dir=work/live)로 meta를 내려받고 이미 처리한 주소 목록을 만든다.
   ```
   python3 -c "import json;L=json.load(open('work/live/meta/newsSeen.json'))['lines'];open('work/seen_urls.txt','w').write('\n'.join(l.rsplit(' | ',1)[1].strip() for l in L if ' | ' in l))"
   ```
3. 읽을 위치는 meta/progressV4의 telegram.new·telegram.backfill, reuters.lastEnd, 블룸버그 note에 있다.

## 1. 텔레그램 (이 세션에서 직접 수집 — 토큰 최소)

채널 11개: Onionfarmer, The_MariTimes(카드 표기 Polaristimes), insidertracking, HANAchina, TNBfolio,
w_compass, Trillion_labs, cahier_de_market, PipeBeom, kkkontemp, Badonions

```
python3 tools/tgcollect.py new  <채널> <시작id>              # 새 글
python3 tools/tgcollect.py back <채널> <시작id> <끝시각KST>   # 소급
python3 tools/tgcollect.py find <채널> 2026-08-15T00:00       # 날짜로 시작 id 찾기
```
- 원본 HTML은 출력하지 않고 id·KST 시각·본문 앞 160자만 보여 준다. 이미 처리한 글과 본문 없는 글(사진·파일)은 뺀다.
- 429·연결 끊김은 자동 재시도. 개별 글 원문 확인은 https://t.me/<채널>/<id>?embed=1
- w_compass: 2026-10-04 추가. 8월 15일 소급 시작 id 6641(08-15 17:50 KST), 당시 최신 7171.
  사용자 지시로 다른 산업 채널과 같이 8월 15일분부터 소급한다.

## 2. 블룸버그·로이터 (목록은 이 세션, 본문은 Chrome의 Claude 확장)

1. 이 세션에서 제목 목록만 받는다(본문은 블룸버그 403, 로이터 401로 막힘).
   ```
   python3 tools/sitemap_list.py bbg <since UTC>    # 뉴스 사이트맵 latest.xml(최근 약 3~4일)
   python3 tools/sitemap_list.py rtr <since UTC>    # 사이트맵 100건 단위로 since까지
   ```
   키워드로 산업을 추정해 거른다(1차 필터). 제목을 보고 관심 산업에 맞는 기사를 Claude가 고른다.
2. 고른 기사는 사용자 Chrome의 Claude 확장으로 연다. 이 클라우드 세션은 사용자 브라우저를 조작할 수 없으므로,
   Claude가 확장에 붙여 넣을 지시문(주소 목록 + 뽑을 항목)을 만들어 주고 사용자가 확장에서 실행한다.
   블룸버그·로이터는 브라우저에 로그인돼 있어야 전문이 보인다.
3. 확장의 결과(사실·수치·시점·원문 주소)를 사용자가 이 세션에 붙여 주면, 여기서 카드로 만들고
   check_cards·hlcheck를 거쳐 DB에 저장한다(카드 번호 newsSeq와 progressV4는 이 세션에서만 고친다).

## 3. 저장

ArtifactData batch: news 신규는 if_version 없이, meta/progressV4·newsSeen은 방금 읽은 버전을 if_version으로.
