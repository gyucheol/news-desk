"""텔레그램 공개 미리보기(t.me/s) 수집기 — 원본 HTML은 파일로만 두고, 걸러낸 짧은 목록만 출력한다.

사용:
  python3 tgcollect.py new  <채널> <시작id>          # 시작id 이후 새 글
  python3 tgcollect.py back <채널> <시작id> <끝시각>  # 소급: 시작id부터 끝시각(ISO, KST)까지 앞으로
  python3 tgcollect.py find <채널> <ISO날짜>          # 그 날짜(KST) 첫 글 id 찾기
출력: id  KST시각  본문 앞 160자 (사진·파일만 있는 글, seen.txt에 있는 글은 뺌)
"""
import sys, re, time, html, random, subprocess, json, os
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))
SEEN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'work', 'seen_urls.txt')
seen = set(open(SEEN).read().split()) if os.path.exists(SEEN) else set()
POST = re.compile(r'data-post="([^/"]+)/(\d+)"(.*?)(?=data-post="|\Z)', re.S)

def get(url, tries=4):
    for i in range(tries):
        r = subprocess.run(['curl', '-sS', '-m', '25', '-A', 'Mozilla/5.0', '-w', '\n%{http_code}', url],
                           capture_output=True, text=True)
        body, _, code = r.stdout.rpartition('\n')
        if code == '200':
            return body
        if code in ('429', '000', '') or code.startswith('5'):  # 000: 연결 끊김 등
            time.sleep(2 ** (i + 1)); continue
        raise SystemExit(f'HTTP {code or "000"} {url} {r.stderr.strip()[:120]}')
    raise SystemExit(f'재시도 초과 {url}')

def page(ch, **q):
    q['nc'] = random.randint(1, 10**9)
    qs = '&'.join(f'{k}={v}' for k, v in q.items())
    out = []
    for m in POST.finditer(get(f'https://t.me/s/{ch}?{qs}')):
        pid, blk = int(m.group(2)), m.group(3)
        t = re.search(r'datetime="([^"]+)"', blk)
        tx = re.search(r'tgme_widget_message_text[^>]*>(.*?)</div>', blk, re.S)
        text = html.unescape(re.sub(r'<br\s*/?>', ' ', tx.group(1))) if tx else ''
        text = re.sub(r'<[^>]+>', '', text).strip()
        kst = datetime.fromisoformat(t.group(1)).astimezone(KST) if t else None
        out.append((pid, kst, text))
    time.sleep(1.0)  # 429 회피
    return out

def show(ch, posts):
    n = 0
    for pid, kst, text in posts:
        if f'https://t.me/{ch}/{pid}' in seen or not text:
            continue
        print(f'{pid}\t{kst:%m-%d %H:%M}\t{text[:160]}'); n += 1
    return n

def collect(ch, start, until=None):
    cur, allp = start - 1, []
    while True:
        ps = [p for p in page(ch, after=cur) if p[0] > cur]
        if not ps: break
        ps.sort()
        if until:
            ps = [p for p in ps if p[1] and p[1] <= until] or []
            if not ps: break
        allp += ps; cur = ps[-1][0]
        if len(allp) > 400: break  # 한 번에 너무 많이 읽지 않음
    return allp, cur

if __name__ == '__main__':
    mode, ch = sys.argv[1], sys.argv[2]
    if mode == 'find':
        target = datetime.fromisoformat(sys.argv[3]).replace(tzinfo=KST)
        latest = max(p[0] for p in page(ch))
        lo, hi = 1, latest
        while hi - lo > 20:
            mid = (lo + hi) // 2
            ps = [p for p in page(ch, before=mid + 1) if p[1]]
            if not ps: lo = mid; continue
            print(f'  {mid}: {max(ps)[1]:%m-%d %H:%M}', file=sys.stderr)
            if max(ps)[1] < target: lo = mid
            else: hi = mid
        print(ch, '대략 시작 id', lo, '(최신', latest, ')')
    else:
        start = int(sys.argv[3])
        until = datetime.fromisoformat(sys.argv[4]).replace(tzinfo=KST) if mode == 'back' else None
        ps, last = collect(ch, start, until)
        k = show(ch, ps)
        print(f'# {ch}: 읽음 {len(ps)}개, 표시 {k}개, 마지막 id {last}')
