"""데스크를 Claude 밖에서 볼 수 있는 정적 웹사이트로 만든다(GitHub Pages용).

사용: python3 -I tools/site/build.py <DB 사본 폴더> <출력 폴더> [읽음 기록 reads.json]
  예) python3 -I tools/site/build.py work/live49 work/site
- DB 사본: ArtifactData list로 받은 폴더(news/, chains/, meta/cycle.json).
- 화면은 desk/index.html(데스크 게시본 원본)을 그대로 쓰고, tools/site/shim.js로 데이터 읽기를 data/*.json으로 바꾼다.
- 데스크와 같게 뉴스는 processed 최신순 1,000건만 넣는다.
- 읽음 기록(data/users/me/reads)을 주면 그 시점에 읽은 뉴스 id만 data/reads.json에 넣는다(읽은 시각은 넣지 않고 그 뉴스의 updatedAt만).
  사이트는 처음 열 때 이 목록을 그 브라우저의 읽음 기록에 합치고, '안 읽은 것만'이 켜진 채로 시작한다(2026-11-02 사용자 요청).
- 요청 버튼(뉴스 내용 및 인사이트 요청)은 Claude 안에서만 동작하므로 숨긴다. 읽음 표시는 보는 브라우저에만 남는다.
"""
import json, glob, os, sys, shutil, re
from datetime import datetime, timezone, timedelta

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
DB, OUT = sys.argv[1], sys.argv[2]
READS = sys.argv[3] if len(sys.argv) > 3 else None
KST = timezone(timedelta(hours=9))
stamp = datetime.now(KST).strftime('%Y-%m-%d %H:%M')

def docs(coll):
    out = []
    for p in sorted(glob.glob(f'{DB}/{coll}/*.json')):
        d = json.load(open(p))
        d.pop('version', None)
        d['id'] = d.get('id') or os.path.basename(p)[:-5]
        out.append(d)
    return out

news = docs('news')
news.sort(key=lambda d: str(d.get('processed') or ''), reverse=True)
news = news[:1000]
chains = docs('chains')
cyc = json.load(open(f'{DB}/meta/cycle.json')) if os.path.exists(f'{DB}/meta/cycle.json') else None
if cyc: cyc.pop('version', None)
assert news and chains, 'DB 사본에 news·chains가 없습니다'

os.makedirs(f'{OUT}/data', exist_ok=True); os.makedirs(f'{OUT}/fonts', exist_ok=True)
dump = lambda o, f: json.dump(o, open(f'{OUT}/data/{f}', 'w'), ensure_ascii=False, separators=(',', ':'))
def upd(d):
    u = d.get('updatedAt')
    return int(datetime.fromisoformat(u.replace('Z', '+00:00')).timestamp() * 1000) if u else 0
readmap = {}
if READS:
    ids = json.load(open(READS)).get('ids', {})
    readmap = {d['id']: max(upd(d), 1) for d in news if ids.get(d['id']) and ids[d['id']] >= upd(d)}
dump({'asof': stamp, 'ids': readmap}, 'reads.json')
dump(news, 'news.json'); dump(chains, 'chains.json'); dump(cyc, 'cycle.json')
shutil.copy(f'{R}/tools/site/shim.js', f'{OUT}/shim.js')
shutil.copy(f'{R}/design/fonts/PretendardVariable.woff2', f'{OUT}/fonts/PretendardVariable.woff2')
open(f'{OUT}/.nojekyll', 'w').close()

page = open(f'{R}/desk/index.html', encoding='utf-8').read()
head = ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="robots" content="noindex,nofollow">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-title" content="뉴스 데스크">\n'
        '<meta name="theme-color" content="#101318">\n'
        '<style>.reqbar,[data-act="dreq"],[data-act="req"]{display:none!important}'
        '.sitenote{margin:0;color:var(--muted);font-size:13px}.sitesync{display:flex;flex-wrap:wrap;gap:8px;align-items:center}'
        '.sitemsg{font-size:13px;color:var(--good-strong)}</style>\n'
        f'<script>window.SITE_BUILD={json.dumps(stamp)};</script>\n'
        '<script src="shim.js"></script>\n</head>\n<body>\n')
main = '<script>\n(() => {\n  const $ = id => document.getElementById(id);'
assert page.count(main) == 1, '데스크 원본의 본 스크립트 시작을 찾지 못했습니다'
ub = "tab: 'news', src: 'all', nind: 'all', unreadOnly: false,"
assert page.count(ub) == 1
page = page.replace(ub, "tab: 'news', src: 'all', nind: 'all', unreadOnly: true,")
note = (f'<p class="sitenote">웹 보기판 · 마지막 갱신 {stamp} (KST) · 여기서 누른 읽음은 이 기기에만 저장됩니다. '
        'Claude 데스크에도 반영하려면 아래 버튼으로 복사해 Claude 대화에 붙여 주세요. 요청 버튼은 Claude 데스크에서만 쓸 수 있습니다.</p>\n'
        '<div class="sitesync"><button type="button" class="tg" id="sitesync">Claude에 보낼 읽음 기록 복사</button>'
        '<span class="sitemsg" id="sitemsg" aria-live="polite"></span>'
        '<textarea id="sitetext" class="reqtext" readonly hidden aria-label="Claude에 붙여 넣을 읽음 기록"></textarea></div>\n')
# 웹에서 새로 읽음 처리한 뉴스 = 이 브라우저 읽음 기록 중 데스크 사본(data/reads.json)보다 새로 생긴 것
sync = '''<script>
(() => {
  const $ = id => document.getElementById(id);
  const btn = $('sitesync'); if (!btn) return;
  btn.addEventListener('click', async () => {
    let seed = {}, cur = {};
    try { seed = ((await (await fetch('data/reads.json?v=' + encodeURIComponent(window.SITE_BUILD || ''), { cache: 'no-cache' })).json()) || {}).ids || {}; } catch (e) {}
    try { cur = JSON.parse(localStorage.getItem('deskReads:anon') || '{}') || {}; } catch (e) {}
    const ids = Object.keys(cur).filter(k => cur[k] && (!seed[k] || cur[k] > seed[k])).sort();
    const t = $('sitetext'), m = $('sitemsg');
    if (!ids.length) { m.textContent = '웹에서 새로 읽음 처리한 뉴스가 없습니다.'; t.hidden = true; return; }
    const text = '웹 읽음 ' + ids.length + '건: ' + ids.join(' ');
    t.value = text; t.hidden = false;
    let ok = false;
    try { await navigator.clipboard.writeText(text); ok = true; } catch (e) { try { t.select(); ok = document.execCommand('copy'); } catch (e2) {} }
    m.textContent = ok ? ids.length + '건을 복사했습니다. Claude 대화에 붙여 넣어 주세요.' : '아래 글을 길게 눌러 복사해 Claude 대화에 붙여 넣어 주세요.';
  });
})();
</script>'''
anchor = '<p class="status" id="status">'
assert page.count(anchor) == 1
page = page.replace(anchor, note + anchor)
open(f'{OUT}/index.html', 'w', encoding='utf-8').write(head + page + '\n' + sync + '\n</body>\n</html>\n')
print('read', len(readmap), 'unread', len(news) - len(readmap), 'news', len(news), 'chains', len(chains), 'cycle', bool(cyc), 'stamp', stamp,
      'size', {f: os.path.getsize(f'{OUT}/data/{f}') for f in os.listdir(f'{OUT}/data')})
