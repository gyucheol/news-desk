#!/usr/bin/env bash
# One-time setup in a fresh cloud session (run from video/burnout/).
#   default : Python env (pillow, numpy, faster-whisper, rembg, torch, transformers), Pretendard + Noto Sans KR fonts
#             (OFL), faster-whisper large-v3 (MIT, ~2.9 GB) and kresnik/wav2vec2-large-xlsr-korean (Apache-2.0, 1.27 GB,
#             syllable-level subtitle timing in ctc_align.py) for syncing the owner's recording
#   WITH_AI=1 ./setup.sh : also torch/diffusers + RealVisXL V5.0 Lightning (openrail++, ~6.5 GB)
#             only needed for AI object images (slow without AMX: check `grep -o amx_bf16 /proc/cpuinfo`)
# ffmpeg must exist (it does in Claude Code cloud sessions).
set -euo pipefail
ROOT="${VIDEO_ROOT:-$(cd "$(dirname "$0")" && pwd)}"
cd "$ROOT"
command -v ffmpeg >/dev/null || { echo "ffmpeg not found"; exit 1; }
[ -x venv/bin/python ] || python3 -m venv venv
./venv/bin/pip install -q --upgrade pip
./venv/bin/pip install -q pillow numpy faster-whisper huggingface_hub rembg onnxruntime   # rembg: thumbnail cut-outs (MIT)
mkdir -p fonts models work
command -v rubberband >/dev/null || { (apt-get update -qq && apt-get install -y -qq rubberband-cli) >/dev/null 2>&1 \
  || echo "warning: rubberband-cli not installed (needed only for polish_voice.py --tempo)"; }
command -v tesseract >/dev/null || { (apt-get update -qq && apt-get install -y -qq tesseract-ocr) >/dev/null 2>&1 \
  || echo "warning: tesseract-ocr not installed (needed only for scripts/ocr_scan.py, the stock text check)"; }
for w in Medium SemiBold Bold ExtraBold; do
  [ -s "fonts/Pretendard-$w.otf" ] || curl -sSf -o "fonts/Pretendard-$w.otf" \
    "https://cdn.jsdelivr.net/npm/pretendard@1.3.9/dist/public/static/Pretendard-$w.otf"
done
[ -s fonts/NotoSansKR-VF.ttf ] || curl -sSf -o fonts/NotoSansKR-VF.ttf \
  "https://raw.githubusercontent.com/google/fonts/main/ofl/notosanskr/NotoSansKR%5Bwght%5D.ttf"   # thumbnails (OFL)
./venv/bin/python - <<'PY'
from huggingface_hub import snapshot_download
snapshot_download('Systran/faster-whisper-large-v3', local_dir='models/fw-large-v3')
PY
./venv/bin/pip install -q torch --index-url https://download.pytorch.org/whl/cpu
./venv/bin/pip install -q transformers safetensors
./venv/bin/python - <<'PY'
from huggingface_hub import snapshot_download
snapshot_download('kresnik/wav2vec2-large-xlsr-korean', local_dir='models/w2v_ko', allow_patterns=[
    'config.json', 'vocab.json', 'preprocessor_config.json', 'tokenizer_config.json', 'special_tokens_map.config',
    'model.safetensors'])
PY
if [ "${WITH_AI:-0}" = "1" ]; then
  ./venv/bin/pip install -q torch --index-url https://download.pytorch.org/whl/cpu
  ./venv/bin/pip install -q diffusers transformers accelerate safetensors torchsde
  ./venv/bin/python - <<'PY'
from huggingface_hub import snapshot_download
snapshot_download('SG161222/RealVisXL_V5.0_Lightning', local_dir='models/realvisxl5l', allow_patterns=[
    'model_index.json', 'scheduler/*', 'text_encoder/config.json', 'text_encoder/model.fp16.safetensors',
    'text_encoder_2/config.json', 'text_encoder_2/model.fp16.safetensors', 'tokenizer/*', 'tokenizer_2/*',
    'unet/config.json', 'unet/diffusion_pytorch_model.fp16.safetensors', 'vae/config.json',
    'vae/diffusion_pytorch_model.fp16.safetensors'])
PY
fi
echo "setup done: $ROOT (AI images: ${WITH_AI:-0})"
