#!/usr/bin/env bash
# One-time setup in a fresh cloud session: Python env, fonts (Pretendard, OFL), models.
#   RealVisXL V5.0 Lightning (openrail++, commercial use allowed)  ~6.5 GB
#   faster-whisper large-v3 (MIT)                                   ~2.9 GB
set -euo pipefail
ROOT="${VIDEO_ROOT:-$(cd "$(dirname "$0")" && pwd)}"
cd "$ROOT"
python3 -m venv venv
./venv/bin/pip install -q --upgrade pip
./venv/bin/pip install -q torch --index-url https://download.pytorch.org/whl/cpu
./venv/bin/pip install -q diffusers transformers accelerate safetensors huggingface_hub torchsde \
    pillow numpy edge-tts faster-whisper
mkdir -p fonts models work
for w in Medium SemiBold Bold ExtraBold; do
  curl -sSf -o "fonts/Pretendard-$w.otf" "https://cdn.jsdelivr.net/npm/pretendard@1.3.9/dist/public/static/Pretendard-$w.otf"
done
./venv/bin/python - <<'PY'
from huggingface_hub import snapshot_download
snapshot_download('SG161222/RealVisXL_V5.0_Lightning', local_dir='models/realvisxl5l', allow_patterns=[
    'model_index.json', 'scheduler/*', 'text_encoder/config.json', 'text_encoder/model.fp16.safetensors',
    'text_encoder_2/config.json', 'text_encoder_2/model.fp16.safetensors', 'tokenizer/*', 'tokenizer_2/*',
    'unet/config.json', 'unet/diffusion_pytorch_model.fp16.safetensors', 'vae/config.json',
    'vae/diffusion_pytorch_model.fp16.safetensors'])
snapshot_download('Systran/faster-whisper-large-v3', local_dir='models/fw-large-v3')
PY
echo "setup done: $ROOT"
