"""블룸버그 뉴스 목록을 월별 사이트맵(sitemaps/news/YYYY-M.xml)과 latest.xml을 합쳐 받는다(2026-11-02부터: latest.xml만으로는 빠지는 날이 있음).
사용: python3 tools/bbg_sitemap.py <since ISO UTC> <출력 파일> [이미 처리한 주소 파일 ...]
출력 줄: 번호 \t 'MM-DD HH:MM'(KST) \t [-] \t 제목(없으면 빈칸) \t 주소   — sitemap_list.py와 같은 꼴(build_all.py가 읽음)."""
import sys, re, html, subprocess
from datetime import datetime, timedelta, timezone
KST = timezone(timedelta(hours=9))
since = datetime.fromisoformat(sys.argv[1].replace('Z', '+00:00')); out = sys.argv[2]
seen = set()
for p in sys.argv[3:]:
    seen |= set(open(p).read().split())
def get(u):
    r = subprocess.run(['curl', '-s', '-A', 'Mozilla/5.0', '--max-time', '60', u], capture_output=True, text=True)
    return r.stdout
months, d = [], since.astimezone(timezone.utc)
now = datetime.now(timezone.utc)
while (d.year, d.month) <= (now.year, now.month):
    months.append(f'{d.year}-{d.month}'); d = (d.replace(day=1) + timedelta(days=32)).replace(day=1)
rows = {}
for u in [f'https://www.bloomberg.com/sitemaps/news/{m}.xml' for m in months] + ['https://www.bloomberg.com/sitemaps/news/latest.xml']:
    x = get(u); n = 0
    for it in re.findall(r'<url>(.*?)</url>', x, re.S):
        loc = html.unescape(re.search(r'<loc>(.*?)</loc>', it).group(1))
        m = re.search(r'<news:publication_date>(.*?)<', it) or re.search(r'<lastmod>(.*?)<', it)
        if not m: continue
        dt = datetime.fromisoformat(m.group(1).replace('Z', '+00:00'))
        t = re.search(r'<news:title>(.*?)</news:title>', it, re.S)
        title = html.unescape(re.sub(r'<!\[CDATA\[|\]\]>', '', t.group(1))).strip() if t else ''
        if dt < since or loc in seen: continue
        n += 1
        if loc in rows and rows[loc][1]: continue
        rows[loc] = (dt, title)
    print(u.rsplit('/', 1)[-1], len(x), 'bytes', n, 'since', file=sys.stderr)
lines = [f'{i}\t{dt.astimezone(KST):%m-%d %H:%M}\t[-]\t{t}\t{u}' for i, (u, (dt, t)) in enumerate(sorted(rows.items(), key=lambda x: x[1][0], reverse=True), 1)]
open(out, 'w').write('\n'.join(lines) + f'\n# bbg: 월별+latest {since:%m-%d %H:%M}Z 이후 {len(lines)}건\n')
print(len(lines), file=sys.stderr)
