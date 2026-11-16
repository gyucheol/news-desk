# 다시 녹음한 조각의 음색을 앞뒤 원래 녹음에 맞춤(한 번만 거는 고정 EQ). 말소리 프레임의 1/3옥타브 평균 세기 차이를
# 부드럽게 해서 firequalizer로 적용(최대 ±MAXDB). 크기는 앞뒤 녹음의 LUFS에 맞춤(고정 이득).
# usage: match_tone.py new.wav ref.wav out.wav report.json
import json, re, subprocess, sys
import numpy as np
new_p, ref_p, out_p, rep_p = sys.argv[1:5]
MAXDB = 6.0
def load(p):
    return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-ac','1','-ar','48000','-f','f32le','-'],capture_output=True,check=True).stdout,np.float32)
def lufs(a):
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-f','f32le','-ar','48000','-ac','1','-i','-','-af','ebur128','-f','null','-'],input=a.astype(np.float32).tobytes(),capture_output=True)
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS',r.stderr.decode())[-1])
def spec(a):
    n=4096; hop=2048; win=np.hanning(n)
    fr=np.array([a[i:i+n]*win for i in range(0,len(a)-n,hop)])
    X=np.abs(np.fft.rfft(fr,axis=1))**2; e=10*np.log10(X.sum(1)+1e-12)
    return X[e>np.percentile(e,40)].mean(0), np.fft.rfftfreq(n,1/48000)
a_new, a_ref = load(new_p), load(ref_p)
Pn, f = spec(a_new); Pr, _ = spec(a_ref)
cent = 1000 * 2 ** (np.arange(-17, 15) / 3)          # 20 Hz .. 20 kHz, 1/3 oct
cent = cent[(cent > 60) & (cent < 16000)]
d = []
for c in cent:
    m = (f >= c / 2 ** (1/6)) & (f < c * 2 ** (1/6))
    d.append(10*np.log10(Pr[m].mean()+1e-20) - 10*np.log10(Pn[m].mean()+1e-20))
d = np.array(d)
mid = (cent >= 315) & (cent <= 1250)
d -= d[mid].mean()                                   # 가운데 대역 기준(크기는 LUFS로 따로 맞춤)
ds = np.convolve(np.pad(d, 1, mode='edge'), [0.25, 0.5, 0.25], 'valid')   # 이웃과 고르게
g = np.clip(ds, -MAXDB, MAXDB)
top = cent >= 12000
g[top] = np.clip(d[top], -MAXDB, MAXDB)          # 맨 위 대역은 이웃(10 kHz) 깎임이 번지지 않게 고르기 전 값
entries = ';'.join(f'entry({c:.0f},{x:.2f})' for c, x in zip(cent, g))
tmp = out_p + '.eq.wav'
subprocess.run(['ffmpeg','-v','error','-y','-i',new_p,'-af',f"firequalizer=gain_entry='{entries}':delay=0.05:zero_phase=on",
                '-ar','48000','-ac','1','-c:a','pcm_f32le',tmp],check=True)
eq = load(tmp)
D = int(0.05 * 48000)                               # firequalizer의 delay(50ms)만큼 늦게 나와서 되돌림(원본과 같은 길이)
eq = eq[D:D + len(a_new)]
gain_db = lufs(a_ref) - lufs(eq)
out = eq * 10 ** (gain_db / 20)
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar','48000','-ac','1','-i','-','-c:a','pcm_f32le',out_p],input=out.astype(np.float32).tobytes(),check=True)
import os; os.remove(tmp)
json.dump({'bands_hz':[round(float(c)) for c in cent],'diff_db':[round(float(x),2) for x in d],'eq_db':[round(float(x),2) for x in g],
           'gain_db':round(float(gain_db),2),'lufs_ref':lufs(a_ref),'lufs_out':lufs(out)},open(rep_p,'w'),indent=1)
print('gain', round(gain_db,2), 'dB | eq', ' '.join(f'{c:.0f}:{x:+.1f}' for c, x in zip(cent, g)))
