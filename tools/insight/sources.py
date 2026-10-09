"""요청한 뉴스의 원문 목록(items)을 조사 에이전트가 쓰기 좋게 한 파일로 모은다. 텔레그램 글은 본문까지 받아 둔다.
사용(저장소 루트에서, 메인 세션이 실행): python3 -I tools/insight/sources.py data/insight/in/news/<id>.json
결과: data/insight/in/<id>.sources.json — [{"n": 번호, "d": 날짜, "o": 출처, "t": 제목, "u": 주소, "text": 텔레그램 본문 또는 ""}]
블룸버그·로이터 본문은 이 환경에서 열리지 않으므로 받지 않는다(에이전트가 독립 출처로 확인)."""
import html, json, os, re, subprocess, sys, time

src = sys.argv[1]
d = json.load(open(src, encoding='utf-8'))
d = d.get('data', d) if isinstance(d.get('data'), dict) else d
items = d.get('items') or [{'d': (d.get('published') or '')[:10], 'o': d.get('source', ''), 't': d.get('title', ''),
                             'u': d.get('url') or ((d.get('src') or [{}])[0].get('u', ''))}]
TG = re.compile(r'^https://t\.me/([A-Za-z0-9_]+)/(\d+)')

def tg_text(u):
    m = TG.match(u)
    if not m: return ''
    for i in range(3):
        r = subprocess.run(['curl', '-sS', '-m', '20', '-A', 'Mozilla/5.0', f'https://t.me/{m.group(1)}/{m.group(2)}?embed=1'],
                           capture_output=True, text=True)
        x = re.search(r'tgme_widget_message_text[^>]*>(.*?)</div>', r.stdout, re.S)
        if x:
            t = re.sub(r'<br\s*/?>', '\n', x.group(1))
            return html.unescape(re.sub(r'<[^>]+>', '', t)).strip()[:4000]
        time.sleep(2 * (i + 1))
    return ''

out = []
for n, it in enumerate(sorted(items, key=lambda x: x.get('d', '')), 1):
    out.append({'n': n, 'd': it.get('d', ''), 'o': it.get('o', ''), 't': it.get('t', ''), 'u': it.get('u', ''), 'text': tg_text(it.get('u', ''))})
    time.sleep(0.5)
path = os.path.join(os.path.dirname(src).rsplit('/news', 1)[0], d['id'] + '.sources.json')
json.dump(out, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(path, len(out), '건, 텔레그램 본문', sum(1 for x in out if x['text']), '건')
