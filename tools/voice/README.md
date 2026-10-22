# 음성 처리 도구 (tools/voice)

말소리 녹음을 음높이를 유지한 채 빠르게 만들고(기본 1.2배속) 유튜브용 음량(−14 LUFS)으로 맞춥니다. 2026-10-22 세션에서 만들었고, 경위와 시험 결과는 저장소 루트의 HANDOFF-voice.md에 있습니다.

## 기본 사용 (사용자가 고른 방식)

```
tools/voice/bin/speedup_voice.sh -o work/voice/out "<입력 파일>"
```

1. 결과는 `<이름>_x1.2.wav`(48 kHz 24비트 스테레오)와 `<이름>_x1.2.m4a`(AAC 192 kbps 스테레오)입니다. 입력이 영상이면 `<이름>_x1.2.mp4`도 만듭니다(화면도 같은 배속, libx264 CRF 18).
2. 처리 순서는 ffmpeg atempo(WSOLA)로 1.2배속 → 스테레오 재생 기준 −14 LUFS, 트루피크 −1.5 dBTP 이하로 음량 맞춤 → 같은 소리를 두 채널에 넣은 스테레오 → AAC입니다. 잡음 제거와 음색 보정은 하지 않습니다.
3. 필요한 것은 ffmpeg뿐입니다(6.1.1 Ubuntu 빌드에서 확인). 이 기본 경로에는 파이썬 환경이 필요 없습니다.
4. 입력 파일은 바꾸지 않습니다. 같은 이름의 결과가 있으면 `_2`, `_3`을 붙입니다.
5. work/는 .gitignore에 들어 있습니다. 이 저장소는 공개 저장소이므로 음성 파일을 커밋하지 마십시오.

## 옵션

1. `-s 1.3`: 다른 배속(0.5~2.0)
2. `-t -16`: 다른 음량 목표(LUFS)
3. `--rb`: rubberband로 속도 변경. 이 세션 시험에서는 atempo보다 음질 지표가 낮았습니다.
4. `--af "<ffmpeg 필터>"`: 속도 변경 전에 필터를 더합니다(예: 음색 EQ).
5. `--clean`: 잡음 제거(DeepFilterNet3), 80 Hz 저음 컷, 부드러운 압축을 더합니다. 아래 추가 설치가 필요합니다.
6. `--preset P`: 영상 인코딩 속도(기본 veryfast)

## 파일

1. bin/speedup_voice.sh: 위 처리 전체를 맡는 입구입니다.
2. bin/polish_voice.sh: 정리 체인과 2단계 음량 맞춤(속도 변경 없음)입니다. speedup_voice.sh가 음량 맞춤에 이것을 씁니다. `--help`로 옵션을 볼 수 있습니다.
3. bin/vt_util.py, bin/dfn_enhance.py, bin/nr_enhance.py: polish_voice.sh의 잡음 제거·무음 자르기 보조입니다(파이썬 필요).
4. bin/tempo_eval.py: 속도 변경 전후의 길이 비율, 음높이, 음색(1/3옥타브) 비교
5. bin/f0_aligned.py: 같은 말 지점끼리 음높이를 센트 단위로 비교합니다. 유성음 전체 중앙값 비교는 배속 뒤에 치우칠 수 있어 이것을 씁니다.
6. bin/tone.py: 옥타브 대역 균형과 치찰음 지표
7. bin/deess.py: 대역 분리형 치찰음 억제기입니다. 이번에 사용자가 고르지 않은 방식이라 보관용입니다.
8. bin/dnsmos.py: DNSMOS 음질 예측 점수(onnxruntime와 모델 필요)

## 추가 설치 (선택)

분석 도구와 `--clean`에만 필요합니다. 이 저장소 위치에서 처음부터 다시 설치해 시험하지는 않았습니다.

1. 분석용 파이썬(3.13에서 확인): `python3 -m venv tools/voice/venv && tools/voice/venv/bin/pip install numpy scipy soundfile pyloudnorm noisereduce onnxruntime pesq pystoi`
2. DeepFilterNet3(`--clean`의 기본 잡음 제거)
   - 파이썬 3.11 venv를 tools/voice/venv311에 만들고, CPU용 torch·torchaudio 2.1.2(https://download.pytorch.org/whl/cpu)와 deepfilternet 0.5.6을 설치합니다.
   - deepfilternet은 파이썬 3.13에 설치되지 않습니다(numpy<2 고정, DeepFilterLib 휠이 3.8~3.11뿐).
   - 가중치는 DeepFilterNet 공식 GitHub 저장소(Rikorose/DeepFilterNet, MIT)의 DeepFilterNet3를 tools/voice/downloads/dfn3-model/DeepFilterNet3/(config.ini, checkpoints/)에 둡니다. 이번 세션에서는 raw.githubusercontent.com에서 받았고, 정확한 경로는 기록하지 못했습니다.
3. RNNoise 모델(`-d rnn`): GitHub richardpl/arnndn-models의 *.rnnn을 tools/voice/downloads/arnndn-models/에 둡니다. std는 Xiph RNNoise(BSD-3)에서 왔고, 나머지는 Gregor Richards가 만들었습니다(그 저장소에는 라이선스 파일이 없습니다).
4. DNSMOS 모델: microsoft/DNS-Challenge의 DNSMOS/sig_bak_ovr.onnx(CC BY 4.0)를 tools/voice/downloads/dnsmos/에 둡니다.
