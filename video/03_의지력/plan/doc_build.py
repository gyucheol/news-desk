import json, os, importlib.util, sys
D = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(D, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
data, reg = load('plan_data'), load('plan_registry')
s = json.load(open(os.path.join(D, 'summary.json'), encoding='utf-8'))
rd = lambda n: open(os.path.join(D, n), encoding='utf-8').read().strip()
blacks, n = [], 0
for sec in data.SECTIONS:
    for pcs in sec['sents']:
        n += 1
        if any(p[1] == 'K' for p in pcs):
            blacks.append(f'[{n}] ' + ' '.join(p[0] for p in pcs if p[1] == 'K'))
sc = s['scene_counts']; total = sum(sc.values())
dur = 557.0
groups_used = [g for g, lst in s['groups'].items() if lst]
fact = rd('fact.md') if os.path.exists(os.path.join(D, 'fact.md')) else '확인 중입니다.'
rep = {
 '@@N_AI@@': str(s['ai']), '@@N_GROUPS@@': str(len(groups_used)), '@@N_STOCK@@': str(s['stock']), '@@N_G@@': str(s['graphics']),
 '@@N_BLACK_SENT@@': str(len(blacks)), '@@N_SCENES@@': str(total), '@@AVG@@': f'{dur/total:.1f}',
 '@@N_SUB@@': str(sum(s['subtitle_counts'].values())), '@@N_B@@': str(s['subtitle_counts']['아래']),
 '@@N_C@@': str(s['subtitle_counts']['가운데']), '@@N_I@@': str(s['subtitle_counts']['가운데 기울임']),
 '@@FACT@@': fact, '@@SCENES@@': rd('scene_list.md'), '@@AI@@': rd('ai_list.md'), '@@STOCK@@': rd('stock_list.md'),
 '@@GRAPHICS@@': rd('graphics_list.md'), '@@BLACKS@@': ' / '.join(blacks), '@@LOOK@@': reg.LOOK, '@@PERSON@@': reg.PERSON,
 '@@ROOMREF@@': s['ai_map']['pack_bag'], '@@BAG@@': s['ai_map']['bag_floor'],
 '@@STOCKNOTE@@': ('Mixkit에서 장면마다 알맞은 영상을 고르고, 영상 페이지에서 무료 라이선스를 확인하는 중입니다. 끝나는 대로 영상 번호, 링크, 쓸 구간을 이 장에 채워 다시 보내 드립니다. 지금은 어떤 장면이 들어가는지만 적었습니다.'
                  if '고르는 중' in rd('stock_list.md') else '영상 페이지에서 무료 라이선스를 확인한 날짜를 적었습니다. 쓸 구간은 작은 미리보기로 고른 것이라, 영상을 만들 때 원래 크기로 다시 보고(로고, 글자, 빨리 감긴 구간) 바꿀 수 있습니다.'),
}
t = open(os.path.join(D, 'doc_template.md'), encoding='utf-8').read()
for k, v in rep.items():
    t = t.replace(k, v)
assert '@@' not in t, [l for l in t.split('\n') if '@@' in l][:5]
open(OUT, 'w', encoding='utf-8').write(t)
print('written', OUT, len(t), 'chars;', 'scenes', total, 'avg', f'{dur/total:.1f}')
