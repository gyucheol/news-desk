"""Opening BGM candidates (2026-10-30 request: tense, slightly mysterious music for the opening).
For each candidate: v1 bgm_segments.json with segment 1 (0-65.54 s) replaced, same tools and levels as v1
(bgm_sequence.py --lufs -36 --constant --fade-out 4, mix_audio.py to -14 LUFS), then the first 70 s as m4a."""
import json, os, subprocess, sys
S = sys.argv[1]; V1 = f'{S}/ep3/v3'; SC = f'{S}/ep3/tools/F의연애/영상/scripts'; PY = f'{S}/venv/bin/python'
W = os.path.dirname(os.path.abspath(__file__)); os.makedirs(f'{W}/prev', exist_ok=True)
C = {v['id']: v for v in json.load(open(f'{W}/cands.json'))}
L = json.load(open(f'{W}/lic.json'))
cands = [('A', '548', 0.0), ('B', '597', 5.3), ('C', '871', 0.0), ('D', '565', 0.0)]
base = json.load(open(f'{V1}/audio/bgm_segments.json'))
for tag, i, off in cands:
    segs = json.loads(json.dumps(base))
    segs[0].update({'track': f'{W}/mp3/{i}.mp3', 'id': i, 'name': f"{C[i]['title']} / {C[i]['author']}", 'offset': off,
                    'why': '① 도입 후보: 긴장감, 약간 미스터리 (' + ', '.join(C[i]['tags']) + ')',
                    'license': L[i]['copyrightNotice'] + ' (' + L[i]['license'] + ')'})
    p = f'{W}/prev/segs_{tag}.json'; json.dump(segs, open(p, 'w'), ensure_ascii=False, indent=1)
    bgm, mix = f'{W}/prev/bgm_{tag}.wav', f'{W}/prev/mix_{tag}.wav'
    subprocess.run([PY, '-I', f'{SC}/bgm_sequence.py', p, '560.0', bgm, '--lufs', '-36', '--constant', '--fade-out', '4'], check=True)
    subprocess.run([PY, '-I', f'{SC}/mix_audio.py', f'{V1}/audio/narration_end.wav', bgm, mix], check=True)
    name = f"{W}/prev/배경음악후보_{tag}_{C[i]['title'].replace(' ', '_')}.m4a"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mix, '-t', '70', '-af', 'afade=t=out:st=68:d=2', '-c:a', 'aac', '-b:a', '192k',
                    '-ar', '48000', name], check=True)
    os.remove(bgm); os.remove(mix); os.remove(mix.replace('.wav', '_raw.wav'))
    print(tag, i, C[i]['title'], '->', name)
