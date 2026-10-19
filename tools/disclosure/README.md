# 공시 알림 (텔레그램)

관심 종목의 새 공시를 5분마다 확인해 텔레그램으로 보냅니다.

- 한국: DART. 기본은 DART 사이트의 회사별 검색을 읽습니다. `DART_API_KEY`가 있으면 DART 오픈API를 씁니다.
- 미국: SEC EDGAR(`data.sec.gov/submissions`). 8-K·6-K는 보도자료 첨부(EX-99)도 함께 읽습니다.
- 요약: `ANTHROPIC_API_KEY`가 있으면 Claude가 한국어 3~5줄로 요약합니다. 없으면 원문 앞부분을 보냅니다.
- 실행: `.github/workflows/disclosure-watch.yml`(GitHub Actions, 5분 간격). 예약 실행은 기본 브랜치에 있는 설정만 동작합니다.

## 종목 바꾸기

`watchlist.json`을 고칩니다.

- 한국: `corp_code`(DART 고유번호 8자리)
- 미국: `cik`(10자리)

새로 넣은 종목은 첫 실행 때 기존 공시를 기록만 하고 보내지 않습니다.

## 저장소 시크릿 (Settings → Secrets and variables → Actions)

| 이름 | 필수 | 내용 |
|---|---|---|
| `TELEGRAM_BOT_TOKEN` | 예 | BotFather가 준 토큰 |
| `TELEGRAM_CHAT_ID` | 예 | 받을 대화방 번호(숫자). 봇에게 `/start`를 보낸 뒤 `--find-chat-id`로 확인 |
| `ANTHROPIC_API_KEY` | 아니오 | Claude 요약용 API 키(사용한 만큼 요금) |
| `DART_API_KEY` | 아니오 | DART 오픈API 인증키 |
| `SEC_USER_AGENT` | 권장 | SEC가 요구하는 연락처. 예: `news-desk 홍길동 name@example.com` |

변수(Variables) `CLAUDE_MODEL`로 요약 모델을 바꿀 수 있습니다. 기본은 `claude-opus-5-5`이고, 더 싼 `claude-haiku-5-5`도 쓸 수 있습니다.

## 직접 실행

```
python3 tools/disclosure/watch.py --find-chat-id     # chat_id 찾기
python3 tools/disclosure/watch.py --test-message     # 연결 시험
python3 tools/disclosure/watch.py --preview 1        # 종목별 최근 1건 메시지 미리보기(보내지 않음)
python3 tools/disclosure/watch.py --dry-run          # 새 공시 확인만(보내지 않음, 상태 저장 안 함)
```

## 알려진 한계

- GitHub 예약 실행은 부하가 크면 늦어지거나 건너뛸 수 있습니다.
- 공개 저장소는 60일 동안 저장소 활동이 없으면 예약 실행이 자동으로 꺼집니다. 꺼지면 Actions 화면에서 다시 켜야 합니다.
- 이미 보낸 공시 번호는 Actions 캐시에 보관합니다. 캐시가 지워지면 그 시점에 있던 공시는 다시 기록만 하고 보내지 않습니다.
- 한 번 실행에 최대 10건을 보내고, 나머지는 다음 실행 때 보냅니다.
- DART 사이트 읽기 방식은 사이트 구조가 바뀌면 동작하지 않을 수 있습니다. 오픈API 키를 쓰면 이 위험이 줄어듭니다.
