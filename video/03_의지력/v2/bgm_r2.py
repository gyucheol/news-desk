# 03편 v2 배경음악 구간: v1(audio/bgm_segments.json)과 같은 8곡에서 ① 도입(0:00~"수요일 저녁 8시입니다" 0.4초 전)만
# 사용자가 고른 D. Fallen (Asper) / Eugenio Mininni(Mixkit 565, Mixkit Stock Music Free License)로 바꿉니다(2026-10-30).
# 곡이 바뀌는 자리는 v1과 같은 규칙: 그 구간 첫 줄의 목소리 시작 0.4초 전(새 녹음으로 시각이 바뀌어 다시 계산).
# usage: bgm_r2.py v1_segments.json onsets.json END out.json   (track 경로는 VIDEO_ROOT 기준 stock/music/NNN.mp3)
import json, sys
segs = json.load(open(sys.argv[1], encoding='utf-8'))
O = {o['id']: o for o in json.load(open(sys.argv[2], encoding='utf-8'))}
END = float(sys.argv[3])
FIRST = ['V001', 'V054', 'V103', 'V158', 'V229', 'V275', 'V353', 'V423']      # 각 구간의 첫 줄(v1에서 확인)
starts = [0.0] + [round(O[v]['start'] - 0.4, 2) for v in FIRST[1:]]
for k, s in enumerate(segs):
    s['track'] = f"stock/music/{s['id']}.mp3"
    s['start'] = starts[k]
    s['end'] = starts[k + 1] if k + 1 < len(segs) else END
segs[0].update({'track': 'stock/music/565.mp3', 'id': '565', 'name': 'Fallen (Asper) / Eugenio Mininni', 'offset': 0,
                'why': '① 도입: 긴장감 있고 약간 미스터리한 곡(2026-10-30 사용자가 후보 4곡 중 D를 고름; Atmospheres, Film Score, '
                       'Mysterious, Atmospheric, Bass, Drums, Documentary, Mystery)',
                'license': 'Mixkit Stock Music Free License (https://mixkit.co/license/#musicFree)'})
json.dump(segs, open(sys.argv[4], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for s in segs:
    print(f"{s['start']:8.2f} {s['end']:8.2f} {s['id']:>4} off {s.get('offset', 0)} {s['name']}")
