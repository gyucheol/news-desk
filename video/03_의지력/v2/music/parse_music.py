"""Parse Mixkit music listing pages (pages/*.html) into cands.json: id, title, author, tags, time, pages."""
import glob, html, json, re, sys
out = {}
for f in sorted(glob.glob('pages/*.html')):
    s = open(f, encoding='utf-8', errors='ignore').read()
    for c in re.split(r"<div class=\"item-grid__item\">", s)[1:]:
        m = re.search(r'data-audio-player-item-id-value="(\d+)"', c)
        if not m:
            continue
        i = m.group(1)
        t = re.search(r'item-grid-card__title">\s*(.*?)\s*</h2>', c, re.S)
        a = re.search(r'item-grid-music-preview__author">\s*by\s*(.*?)\s*</p>', c, re.S)
        tags = [html.unescape(x) for x in re.findall(r'meta-links__link" data-global--meta-links-target="link" href="[^"]+">([^<]+)</a>', c)]
        d = re.search(r'data-test-id="duration">\s*([\d:]+)', c)
        v = out.setdefault(i, {'id': i, 'title': html.unescape(t.group(1)) if t else '', 'author': html.unescape(a.group(1)) if a else '',
                               'tags': tags, 'time': d.group(1) if d else '', 'pages': []})
        p = f.split('/')[-1][:-5]
        if p not in v['pages']:
            v['pages'].append(p)
json.dump(list(out.values()), open('cands.json', 'w'), ensure_ascii=False, indent=1)
for v in out.values():
    print(v['id'], '|', v['title'], '|', v['author'], '|', v['time'], '|', ', '.join(v['tags']), '|', ','.join(v['pages']))
