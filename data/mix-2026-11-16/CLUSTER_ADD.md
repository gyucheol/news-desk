# 추가분 묶기 (11월 17일, G1b) — CLUSTER.md의 보충 지시

먼저 data/mix-2026-11-16/CLUSTER.md를 처음부터 끝까지 읽습니다. 그 규칙을 그대로 따르되, 이번에는 이미 만든 묶음이 있습니다.
- data/mix-2026-11-16/clusters_G1.json: 11월 15~16일 오전 글(줄 1~288)로 이미 정한 G1 묶음 36개(cid G1-001~G1-036, attachTo 25개). 이것은 바꾸지 않습니다.
- 당신의 입력: data/mix-2026-11-16/keep_G1b.tsv — 11월 16일 오전~17일 아침 새 글 122줄(줄 289 이후). 형식은 keep_G1.tsv와 같음.

## 할 일
새 줄마다 아래 중 하나로 정합니다.
1. 이미 정한 G1 묶음과 같은 흐름이면 그 묶음에 더합니다(add). 그 묶음의 attachTo 문서와 같은 흐름인 경우도 여기에 해당합니다.
2. G1 묶음에는 없지만 existing.tsv의 기존 문서와 같은 흐름이면 새 묶음을 만들고 attachTo에 그 문서를 적습니다. 단 clusters_G1.json에서 이미 attachTo로 쓴 문서라면 새 묶음이 아니라 1번(그 묶음에 add)으로 합니다.
3. 어디에도 없는 새 흐름이면 새 묶음(attachTo "").
4. 투자와 무관·중복·구체 정보 없음이면 drop(CLUSTER.md 기준). 텔레그램 정보형 글은 '새 사건 아님'으로 drop하지 않습니다.
사용자 지시(11월 2일): "같은 내용이면 묶어달라" — 날짜가 달라도 같은 흐름이면 반드시 붙입니다(기사 60건 넘는 문서만 예외).

## 출력: data/mix-2026-11-16/clusters_G1b.json
{
 "add": [{"cid": "G1-003", "lines": [301, 455], "core_add": ["새로 생긴 핵심 사건(주체+변화+숫자), 없으면 빈 배열"]}],
 "clusters": [{"cid": "G1-037", "theme": "...", "field": "...", "attachTo": "n-... 또는 \"\"", "core": ["..."], "lines": [..]}],
 "drop": [{"line": 330, "reason": "..."}]
}
- 새 묶음 cid는 G1-037부터. keep_G1b.tsv의 모든 줄번호가 add·clusters·drop 중 정확히 한 곳에 들어가야 합니다.
- 다 쓰면 python3로 누락·중복과 add의 cid가 clusters_G1.json에 있는지 확인하고, add 묶음 수·새 묶음 수·attachTo 수·drop 수를 3줄 이내로 보고합니다.
- 보조 파일은 data/mix-2026-11-16/scratch/G1b/ 안에만.
