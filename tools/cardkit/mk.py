import json, glob, os, re, sys, argparse, datetime
ap = argparse.ArgumentParser()
ap.add_argument('--dump', default='db'); ap.add_argument('--date'); ap.add_argument('--log', required=True)
ap.add_argument('--new', default=''); ap.add_argument('--backfill', default='')
ap.add_argument('--note-new'); ap.add_argument('--note-backfill'); ap.add_argument('--bbg-note'); ap.add_argument('--rtr-note')
ap.add_argument('--pv', type=int, required=True); ap.add_argument('--sv', type=int, required=True)
a = ap.parse_args()
today = a.date or (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9)).strftime('%Y-%m-%d')
prog = json.load(open(f'{a.dump}/meta/progressV4.json')); seen = json.load(open(f'{a.dump}/meta/newsSeen.json'))
PRE = {'텔레그램': 'tg', '블룸버그': 'bbg', '로이터': 'rtr'}
cards = [json.load(open(p)) for p in sorted(glob.glob('cards/*.json'))]
if not cards: sys.exit('cards/ 가 비어 있습니다')
os.makedirs('newsdocs', exist_ok=True); os.makedirs('out', exist_ok=True)
for f in glob.glob('newsdocs/*.json'): os.remove(f)
known = set(l.split(' ')[1] for l in seen['lines'] if len(l.split(' ')) > 1)
strip = re.compile(r'\{\{|\}\}'); new_lines = []; ids = []
for src, pre in PRE.items():
    lst = sorted([c for c in cards if c['source'] == src], key=lambda c: (c['published'], c['key']))
    n0 = prog['newsSeq'].get(pre, 0)
    for i, c in enumerate(lst, 1):
        n = n0 + i; nid = f'n-{pre}-{n:04d}'
        if nid in known: sys.exit(nid + ' 가 이미 있습니다 — DB를 다시 내려받으세요')
        d = {'id': nid, 'feed': 'v4', 'format': 'sum1', 'num': n, 'processed': today, 'source': src}
        if src == '텔레그램': d['channel'] = c.get('channel', '')
        for f in ['published', 'url', 'inds', 'nodes', 'headline', 'facts', 'tags', 'cycles', 'incentive', 'check', 'src']: d[f] = c[f]
        if c.get('dupOf'): d['dupOf'] = c['dupOf']
        d['insight'] = {}; d['key'] = c['key']
        json.dump(d, open(f'newsdocs/{nid}.json', 'w'), ensure_ascii=False, indent=1)
        new_lines.append(f"{c['published'][:16]} {nid} {strip.sub('', c['headline'])} | {c['url']}"); ids.append(nid)
    prog['newsSeq'][pre] = n0 + len(lst)
def kv(s): return {k: int(v) for k, v in (x.split('=') for x in s.split(',') if x)}
prog['telegram']['new'].update(kv(a.new)); prog['telegram']['backfill'].update(kv(a.backfill))
if a.note_new: prog['telegram']['newNote'] = a.note_new
if a.note_backfill: prog['telegram']['backfillNote'] = a.note_backfill
if a.bbg_note: prog.setdefault('bloomberg', {})['note'] = a.bbg_note
if a.rtr_note: prog.setdefault('reuters', {})['newNote'] = a.rtr_note
prog['log'] = (prog['log'] + [{'d': today, 't': a.log}])[-60:]
json.dump(prog, open('out/progressV4.json', 'w'), ensure_ascii=False, indent=1)
seen['lines'] = (seen['lines'] + new_lines)[-1500:]; seen['count'] = len(seen['lines']); seen['updated'] = today
json.dump(seen, open('out/newsSeen.json', 'w'), ensure_ascii=False)
cwd = os.getcwd()
w = [{'op': 'set', 'collection': 'news', 'doc_id': i, 'file_path': f'{cwd}/newsdocs/{i}.json'} for i in ids]
w += [{'op': 'set', 'collection': 'meta', 'doc_id': 'progressV4', 'file_path': f'{cwd}/out/progressV4.json', 'if_version': a.pv},
      {'op': 'set', 'collection': 'meta', 'doc_id': 'newsSeen', 'file_path': f'{cwd}/out/newsSeen.json', 'if_version': a.sv}]
for i in range(0, len(w), 50): print('WRITES', json.dumps(w[i:i + 50], ensure_ascii=False, separators=(',', ':')))
print('ids', ids[0], '~', ids[-1], len(ids), '건 · newsSeq', prog['newsSeq'], '· processed', today)
