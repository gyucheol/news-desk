import json, re, difflib, importlib.util, os
D = os.path.dirname(os.path.abspath(__file__))
S = '/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad'
spec = importlib.util.spec_from_file_location('plan_data', os.path.join(D, 'plan_data.py'))
data = importlib.util.module_from_spec(spec); spec.loader.exec_module(data)
norm = lambda s: re.sub(r'[^0-9A-Za-z가-힣]', '', s)
w = json.load(open(S + '/ep3/rec/rec_words.json', encoding='utf-8'))
achars, atimes = [], []
for x in w:
    for c in norm(x[0]):
        achars.append(c); atimes.append(x[1])
asr = ''.join(achars)
ptext, sent_start_idx, sec_first = '', [], []
for sec in data.SECTIONS:
    sec_first.append(len(sent_start_idx))
    for pieces in sec['sents']:
        sent_start_idx.append(len(ptext))
        ptext += norm(''.join(p[0] for p in pieces))
sm = difflib.SequenceMatcher(None, ptext, asr, autojunk=False)
blocks = sm.get_matching_blocks()
def map_idx(i):
    for a, b, n in blocks:
        if a <= i < a + n:
            return atimes[b + (i - a)]
    # next block start
    for a, b, n in blocks:
        if a > i and n:
            return atimes[min(b, len(atimes) - 1)]
    return atimes[-1]
sent_times = [map_idx(i) for i in sent_start_idx]
fmt = lambda t: f'{int(t)//60}:{int(t)%60:02d}'
sec_time = {}
for k, sec in enumerate(data.SECTIONS):
    a = sent_times[sec_first[k]]
    b = sent_times[sec_first[k + 1]] if k + 1 < len(data.SECTIONS) else w[-1][2]
    sec_time[sec['title']] = f'{fmt(a)}~{fmt(b)}'
extra = json.load(open(os.path.join(D, 'extra.json'), encoding='utf-8')) if os.path.exists(os.path.join(D, 'extra.json')) else {}
extra['sec_time'] = sec_time
extra['sent_time'] = [fmt(t) for t in sent_times]
extra['sent_time_s'] = sent_times
json.dump(extra, open(os.path.join(D, 'extra.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in sec_time.items(): print(v, k)
# monotonic check
bad = [i + 1 for i in range(1, len(sent_times)) if sent_times[i] < sent_times[i - 1]]
print('non-monotonic sentences:', bad)
