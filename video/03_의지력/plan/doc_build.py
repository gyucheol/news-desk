# 03_의지력_장면표시.md 만들기 (2판): doc_template.md의 @@…@@ 자리를 summary.json과 목록 파일로 채움
import json, os, re, importlib.util, sys
D = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(D, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
data, reg = load('plan_data'), load('plan_registry')
s = json.load(open(os.path.join(D, 'summary.json'), encoding='utf-8'))
rd = lambda n: open(os.path.join(D, n), encoding='utf-8').read().strip()
V1 = {'ai': 44, 'stock': 54, 'graphics': 13}   # 1판 숫자(비교용)
sents = [' '.join(p[0] for p in s_) for sec in data.SECTIONS for s_ in sec['sents']]
blacks = ' / '.join(f'[{n}] {sents[n - 1]}' for n in s['black_sents'])
scene_of = {}
for r in s['scene_rows']:
    for n in range(r['sents'][0], r['sents'][1] + 1): scene_of[n] = r['no']
stock_list = rd('stock_list.md')
rep = {
 '@@N_AI@@': s['ai'], '@@N_GROUPS@@': sum(1 for v in s['groups'].values() if v), '@@N_STOCK@@': s['stock'], '@@N_G@@': s['graphics'],
 '@@N_BLACK_SENT@@': len(s['black_sents']), '@@N_BLACK_SCENES@@': s['scene_kinds']['K'], '@@N_SPLIT@@': s['scene_kinds']['SPLIT'],
 '@@N_SCENES@@': s['scenes'], '@@AVG@@': s['avg_s'],
 '@@N_SUB@@': sum(s['subtitle_counts'].values()), '@@N_B@@': s['subtitle_counts']['아래'],
 '@@N_C@@': s['subtitle_counts']['가운데'], '@@N_I@@': s['subtitle_counts']['가운데 기울임'],
 '@@D_AI@@': V1['ai'] - s['ai'], '@@D_STOCK@@': V1['stock'] - s['stock'], '@@D_G@@': V1['graphics'] - s['graphics'],
 '@@FACT@@': rd('fact.md'), '@@SCENES@@': rd('scene_list.md'), '@@AI@@': rd('ai_list.md'), '@@STOCK@@': stock_list,
 '@@GRAPHICS@@': rd('graphics_list.md'), '@@BLACKS@@': blacks, '@@LOOK@@': reg.LOOK, '@@PERSON@@': reg.PERSON,
 '@@ROOMREF@@': s['groups']['g1'][0],
 '@@PERSON_IN@@': ', '.join(s['person_in']),
 '@@STOCKNOTE@@': ('2판에서 장면이 길어져 스톡을 @@N_STOCK@@개로 줄였고, 쓰는 곳마다 화면에 나오는 시간을 괄호 안에 적었습니다. '
                  'Mixkit에서 그 시간 이상 끊김 없이 쓸 수 있는 영상을 고르고, 영상 페이지에서 무료 라이선스를 확인하는 중입니다. '
                  '끝나는 대로 영상 번호, 링크, 쓸 구간을 이 장에 채워 다시 보내 드립니다. 지금은 어떤 장면이 들어가는지만 적었습니다.')
                 if '고르는 중' in stock_list else
                 ('고른 영상마다 영상 페이지에서 무료 라이선스를 확인했습니다. 쓸 구간은 작은 미리보기(360p)로 고른 것이라, '
                  '영상을 만들 때 원래 크기로 다시 보고(작은 상표, 글자, 빨리 감긴 구간) 바꿀 수 있습니다. '
                  '맞는 무료 영상이 없던 곳(지하철 @@A:subway_tired@@, 밤 사무실 @@A:office_late@@, 배드민턴 @@A:badminton@@)과 '
                  '스톡에서 주인공 자리에 다른 사람 얼굴이 보이던 곳(침대에서 휴대폰 @@A:bed_scroll@@)은 AI 사진으로 바꿨습니다. '
                  '설명과 조금 다른 영상은 메모에 적었습니다(@@S:S30@@ 논문 대신 오래된 책, @@S:S44@@ 동네 골목 대신 탁 트인 산책로, '
                  '@@S:S24@@ 가게 대신 길가, @@S:S49@@ 지루한 표정 대신 숨을 고르는 모습, @@S:S12@@ 쓰러지듯 앉는 동작 없음). '
                  '마음에 들지 않는 것은 번호를 알려 주시면 다른 영상이나 AI 사진으로 바꾸겠습니다.'),
}
t = open(os.path.join(D, 'doc_template.md'), encoding='utf-8').read()
for _ in range(2):   # 채운 글 안의 자리(예: 1-1의 @@A:…@@)까지
    for k, v in rep.items():
        t = t.replace(k, str(v))
    t = re.sub(r'@@([ASG]):([A-Za-z0-9_]+)@@', lambda m: {'A': s['ai_map'], 'S': s['stock_map'], 'G': s['graphics_map']}[m.group(1)][m.group(2)], t)
    t = re.sub(r'@@SC:([A-Za-z0-9_]+)@@', lambda m: '장면 ' + ', '.join(str(x) for x in s['ai_uses'][m.group(1)]), t)
    t = re.sub(r'@@SCN:(\d+)@@', lambda m: str(scene_of[int(m.group(1))]), t)
assert '@@' not in t, [l for l in t.split('\n') if '@@' in l][:5]
open(OUT, 'w', encoding='utf-8').write(t)
print('written', OUT, len(t), 'chars,', t.count('\n'), 'lines; scenes', s['scenes'], 'avg', s['avg_s'])
