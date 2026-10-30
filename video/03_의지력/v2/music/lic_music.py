"""Read MusicRecording JSON-LD (copyrightNotice, license, url) from Mixkit listing pages -> lic.json {id: {...}}."""
import glob, json, re
res = {}
def walk(n, page):
    if isinstance(n, list):
        for x in n: walk(x, page)
    elif isinstance(n, dict):
        if n.get('@type') == 'MusicRecording':
            m = re.search(r'/music/(\d+)/', n.get('url', '') or '')
            if m:
                r = res.setdefault(m.group(1), {k: n.get(k) for k in ('name', 'byArtist', 'genre', 'duration', 'url', 'copyrightNotice', 'license', 'isAccessibleForFree')})
                r.setdefault('pages', []).append(page)
        for v in n.values():
            if isinstance(v, (list, dict)): walk(v, page)
for f in sorted(glob.glob('pages/*.html')):
    s = open(f, encoding='utf-8', errors='ignore').read()
    for blk in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>', s, flags=re.S):
        try: walk(json.loads(blk), f.split('/')[-1])
        except Exception: pass
json.dump(res, open('lic.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(res), Counter(v['copyrightNotice'] for v in res.values()))
