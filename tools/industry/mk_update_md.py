"""UPDATE.md(원본 지시서)의 {W}{DB}{REPO}{TODAY}{SINCE}{MODE}를 채워 <작업 폴더>/UPDATE.md로 쓴다.
사용: python3 -I tools/industry/mk_update_md.py <저장소> <작업 폴더> <DB 사본> <오늘> <처리일 하한> <실행 방식>"""
import os, sys
REPO, W, DB, TODAY, SINCE, MODE = [os.path.abspath(a) if i < 3 else a for i, a in enumerate(sys.argv[1:7])]
s = open(f'{REPO}/tools/industry/UPDATE.md').read()
for k, v in {'{W}': W, '{DB}': DB, '{REPO}': REPO, '{TODAY}': TODAY, '{SINCE}': SINCE, '{MODE}': MODE}.items():
    s = s.replace(k, v)
os.makedirs(W, exist_ok=True)
open(f'{W}/UPDATE.md', 'w').write(s)
print(f'{W}/UPDATE.md')
