# 서브 에이전트 지시서 (2026-10-22 음성 작업)

이번 세션에서 서브 에이전트에게 준 지시를 그대로 보관합니다. 재사용할 수 있도록 세션마다 달라지는 경로만 자리표시자로 바꿨습니다.

1. `<SCRATCH>`: 세션 scratchpad 폴더
2. `<DEEP_RESEARCH_SKILL>`: deep-research 스킬 폴더(researcher.md, report-writer.md가 있는 곳)

조사 4개와 환경 검증은 동시에 띄웠습니다. 조사 4개가 끝난 뒤 보고서 작성을 띄웠고, AI 고음 복원 시험은 사용자가 처음 방식을 고르면서 중단했습니다.

---

## 1. 조사: 전통 신호처리

```
Research the traditional (non-AI) digital signal processing techniques that audio-repair and voice-polishing software uses to clean up and improve spoken-voice recordings, plus the loudness standards used to finish them.

Objective: Compile dense, well-sourced notes that explain, for each standard processing step, (a) what problem it fixes, (b) how it works technically (accurate, but explainable to a non-engineer), (c) typical settings for spoken voice, (d) where it usually sits in a processing chain and why, and (e) its known side effects, artifacts and limits. This research covers general methods and standards, not product-by-product feature lists (another researcher covers products).

Key questions:
- Noise reduction: how do classic methods work — spectral subtraction (Boll 1979), Wiener filtering, MMSE-STSA / log-MMSE (Ephraim & Malah 1984/1985), noise-profile ("noise print") learning and spectral gating as in Audacity's Noise Reduction effect? What causes "musical noise" and "underwater/watery" artifacts, and how do tools mitigate them (smoothing, limits on the reduction amount)?
- Hum/buzz removal (50/60 Hz plus harmonics; notch or comb filters) and high-pass / low-cut filtering for rumble and plosives — typical cutoff frequencies used for voice.
- EQ for voice: which frequency regions are commonly adjusted (e.g., mud/boxiness, presence, sibilance, air) and why — separate documented guidance from rule-of-thumb folklore.
- Dynamics processing: compression (threshold, ratio, attack/release, makeup gain), noise gate / downward expander, limiter, and automatic leveling; de-essing (sibilance band, split-band or dynamic EQ); de-plosive; de-click / mouth-click removal; de-clipping (how clipped peaks are reconstructed); breath reduction.
- Classic dereverberation (e.g., spectral late-reverberation suppression, weighted prediction error / WPE): how it works and why reverb is harder to remove than steady noise.
- Loudness normalization: ITU-R BS.1770 (LUFS/LKFS, K-weighting, gating, true peak), EBU R128 (−23 LUFS), and common delivery targets for podcasts / streaming / video platforms (e.g., Apple Podcasts, Spotify, YouTube) — cite official documentation for each target and note where targets differ or have changed over time. Also explain the difference between peak normalization and loudness normalization.
- What processing order do authoritative sources recommend for a voice chain, and what do they say about over-processing?

Suggested sources:
- Original academic papers (IEEE Transactions on Acoustics, Speech, and Signal Processing: Boll 1979; Ephraim & Malah 1984/1985; Nakatani et al. on WPE) and textbooks or lecture notes on speech enhancement (e.g., Loizou, "Speech Enhancement: Theory and Practice")
- Official standards: ITU-R BS.1770 (itu.int), EBU R128 and EBU Tech 3341/3342/3343 (tech.ebu.ch)
- Official software documentation describing the algorithms: Audacity manual (manual.audacityteam.org) and Audacity wiki for Noise Reduction / Compressor / Normalize / Loudness Normalization; FFmpeg filter documentation (ffmpeg.org/ffmpeg-filters.html) for afftdn, anlmdn, deesser, acompressor, agate, loudnorm, dynaudnorm, speechnorm; iZotope educational articles on de-click, de-clip, de-hum and de-ess concepts
- Official platform loudness guidance (Apple Podcasts, Spotify for Creators/Podcasters, YouTube Help)
- Audio engineering references (AES papers, Sound On Sound articles) for EQ and compression practice on speech

Constraints:
- Focus on spoken voice (speech, podcasts, narration, voice memos, lectures, video voice-over), not music mixing in general.
- Cite a source URL for every factual claim. Clearly label anything that is a rule of thumb rather than a documented standard, and anything that is your own inference.
- Reflect the state of knowledge as of October 2026; note where standards or platform targets have changed, with dates.

Save your output notes to <SCRATCH>/research_notes/음성 녹음 보정 프로그램 원리/traditional_dsp.md

**As a first step, you must read <DEEP_RESEARCH_SKILL>/references/researcher.md for instructions on how to conduct research.**
```

## 2. 조사: AI 음성 향상

```
Research AI / deep-learning based speech enhancement as used to clean up and "polish" spoken-voice recordings.

Objective: Compile dense, well-sourced notes explaining the main families of AI voice-enhancement methods, how each works conceptually, representative published models, what they can fix that classic DSP cannot, how quality is measured, and their documented limitations and failure modes. This research covers methods and research results, not product-by-product feature lists (another researcher covers products).

Key questions:
- Discriminative / mask-based denoising: how do networks estimate time-frequency masks or clean spectra? Representative models: RNNoise (Valin 2018, hybrid DSP + RNN), PercepNet (2020), DeepFilterNet (Schröter et al. 2022/2023), Meta's Demucs-based "Denoiser" (Défossez et al. 2020). How are they trained (clean speech + noise mixtures, simulated room impulse responses)?
- Neural dereverberation and "dialogue isolation": how do networks separate a voice from room echo, background music or other speakers (e.g., source separation such as Conv-TasNet / Demucs, target-speaker extraction)?
- Generative / resynthesis-based enhancement ("speech restoration"): GAN, diffusion, flow or neural-vocoder methods that regenerate clean speech from degraded input — e.g., Adobe Research's HiFi-GAN (Su, Jin & Finkelstein 2020) and HiFi-GAN-2 (2021), VoiceFixer (2021/2022), Google's Miipher (2023), Resemble Enhance, diffusion-based SGMSE+ / StoRM, and notable 2024–2026 work. How do they differ from mask-based methods, and why can they make a phone recording sound "studio-like"? What extra risks do they carry?
- Documented limitations and failure modes: over-suppression of speech, artifacts, "robotic" or "AI-sounding" timbre, hallucinated or altered phonemes/words, changes in speaker identity / accent / emotion, problems with music, laughter, overlapping speakers, singing, non-English languages (Korean if there is any evidence), very low SNR, or clipping. What do papers, challenge reports (Microsoft DNS Challenge, URGENT Challenge 2024/2025) and evaluations say?
- How is enhancement quality measured (PESQ, STOI, SI-SDR, DNSMOS, NISQA, MOS / MUSHRA listening tests), and what are those metrics' caveats?
- Real-time versus offline enhancement: how do latency budgets and model design differ between real-time call/stream noise suppression (e.g., Krisp, NVIDIA RTX Voice / Broadcast, Apple Voice Isolation) and offline file enhancement? Only state product internals that are publicly documented.

Suggested sources:
- arXiv, IEEE/ACM TASLP, ICASSP and Interspeech papers for the named models; official GitHub repositories (xiph/rnnoise, Rikorose/DeepFilterNet, facebookresearch/denoiser, haoheliu/voicefixer, resemble-ai/resemble-enhance, sp-uhh/sgmse)
- Microsoft DNS Challenge papers and results; URGENT challenge papers and results pages
- Adobe Research publication pages; Google Research blog posts (e.g., Miipher); Jean-Marc Valin's RNNoise demo pages (jmvalin.ca / xiph.org)
- Recent survey papers on speech enhancement (2022–2026)

Constraints:
- Focus on spoken voice recordings.
- Cite a source URL for every factual claim. Clearly separate (a) what a paper or official document states, (b) vendor marketing claims, and (c) your own inference. Do NOT claim that a commercial product uses a specific algorithm unless the vendor or a credible primary source says so; otherwise write that it is not publicly documented.
- Reflect the state of the field as of October 2026, including notable 2024–2026 developments.

Save your output notes to <SCRATCH>/research_notes/음성 녹음 보정 프로그램 원리/ai_speech_enhancement.md

**As a first step, you must read <DEEP_RESEARCH_SKILL>/references/researcher.md for instructions on how to conduct research.**
```

## 3. 조사: 제품별 기능

```
Research how specific, widely used voice-recording cleanup and polishing products process the voice, based primarily on their official documentation.

Objective: For each product, compile well-sourced notes on: which voice-processing features or modules it offers, what each one does, whether it is documented as classic DSP or AI / machine learning, the user-adjustable controls, the vendor-recommended workflow or processing order, where processing runs (on-device vs cloud upload) and any documented data/privacy terms for uploaded audio, and the limitations or cautions the vendor itself documents. Also cover the "tidying" edit features commonly used to polish recordings (silence trimming, filler-word removal such as "um/uh", transcript-based editing). This research covers products; the general theory of the algorithms is covered by other researchers, so keep explanations of theory brief.

Products to cover (prioritize the first five):
- iZotope RX (current version): Repair Assistant, Voice De-noise, Spectral De-noise, Dialogue Isolate, Dialogue De-reverb / De-reverb, De-click, Mouth De-click, De-plosive, De-ess, Breath Control, De-hum, De-clip, Spectral Repair, Loudness Control; iZotope's statements about machine learning in RX
- Adobe Podcast "Enhance Speech" (v1 vs v2 if documented; strength / mix controls), and Enhance Speech inside Adobe Premiere Pro / Audition
- Descript: Studio Sound (intensity control), filler-word removal, removing/shortening word gaps, Regenerate / Overdub
- Auphonic: Adaptive Leveler, Noise & Reverb Reduction (its documented methods, e.g., Static / Dynamic / Speech Isolation), Filtering / AutoEQ, Loudness Normalization targets, silence and filler cutting
- Audacity: built-in Noise Reduction, Compressor, Normalize, Loudness Normalization; the Intel OpenVINO AI plugins (noise suppression, etc.)
- Real-time tools: Krisp, NVIDIA Broadcast (Noise Removal, Room Echo Removal, Studio Voice), Apple "Voice Isolation" microphone mode
- Mobile / consumer tools likely used by Korean users: Apple Voice Memos "Enhance Recording", Samsung Galaxy "Audio Eraser" (오디오 지우개) and Samsung Voice Recorder features, CapCut "Enhance voice" / "Reduce noise", Vrew (브루) audio features, and any other notable Korean-market tool you find (e.g., Naver Clova-related tools). Skip tools with no documented voice-enhancement feature.

Key questions:
- What exactly does each product say it does to the voice, and which claims are verifiable from official docs versus marketing language?
- What processing order or workflow does each vendor recommend (e.g., repair before leveling, noise reduction before compression)?
- What limitations or cautions does each vendor document (artifacts at high strength, not for music/singing, file length/size/format limits, languages supported for transcript-based features)?
- Free vs paid availability at a high level only (no detailed pricing).

Suggested sources:
- Official documentation and help centers: izotope.com / docs.izotope.com, helpx.adobe.com and podcast.adobe.com, help.descript.com, auphonic.com/help, manual.audacityteam.org and Intel's OpenVINO Audacity plugin GitHub repository, krisp.ai, nvidia.com, support.apple.com, samsung.com (including Korean pages at samsung.com/sec), capcut.com, vrew.ai
- Vendor blogs and release notes for version and date information; reputable independent reviews (e.g., Sound On Sound) for independent observations

Constraints:
- Focus on spoken voice; note whether each product explicitly supports or warns against singing or music.
- Cite a source URL for every factual claim; label marketing claims as such; do not guess proprietary internals — write "not publicly documented" when unknown.
- Reflect the current state as of October 2026, with version numbers and dates where available.

Save your output notes to <SCRATCH>/research_notes/음성 녹음 보정 프로그램 원리/products_and_workflows.md

**As a first step, you must read <DEEP_RESEARCH_SKILL>/references/researcher.md for instructions on how to conduct research.**
```

## 4. 조사: 노래 음정 보정

```
Research how software corrects singing-voice recordings: pitch correction, timing correction, and related vocal tuning (commonly called "음정 보정" or "튠" in Korean).

Objective: Compile dense, well-sourced notes explaining how pitch and timing correction tools work technically and in practice, plus their limitations, so that a reader can clearly distinguish "voice cleanup" (noise, echo, levels) from "vocal tuning" (pitch and timing). Spoken-voice cleanup is covered by other researchers; focus here on singing.

Key questions:
- How does automatic pitch correction (Antares Auto-Tune) work: pitch detection (e.g., the autocorrelation approach in Andy Hildebrand's US patent 5,973,252), mapping to a key/scale, Retune Speed, Humanize, Flex-Tune; and how the "Auto-Tune effect" (hard-tuned sound) results from very fast retune settings?
- How does graphical / offline note-based editing work: Celemony Melodyne (note detection, pitch center vs pitch drift/modulation, formants, timing, DNA polyphonic), Auto-Tune's Graph mode, Logic Pro Flex Pitch, Waves Tune, Synchro Arts RePitch / VocAlign, and free tools (e.g., Graillon, MAutoPitch)?
- Underlying signal processing: pitch detection algorithms (autocorrelation, YIN by de Cheveigné & Kawahara 2002, pYIN, CREPE 2018), pitch shifting (TD-PSOLA by Moulines & Charpentier 1990, phase vocoder), and formant preservation — why shifting pitch without formant preservation causes a "chipmunk" or unnatural timbre.
- Timing correction and alignment (e.g., VocAlign for doubled vocals, Melodyne timing tools).
- AI-based developments for singing (AI pitch correction, singing-voice enhancement, singing-voice conversion) from credible sources, 2023–2026, only where documented.
- Limitations and audible artifacts (warbling, robotic sound, problems with breaths, consonants and vibrato, noisy or reverberant recordings degrading pitch detection) and vendor best-practice cautions.
- Briefly: mobile karaoke / singing apps that apply automatic tuning or vocal effects (e.g., Smule; Korean apps such as Everysing / 에브리싱), only where documented.

Suggested sources:
- Antares (antarestech.com) and Celemony (celemony.com) official manuals and help pages; Apple Logic Pro user guide; Synchro Arts documentation
- Patents (patents.google.com); academic papers on pitch detection and PSOLA (JASA, ICASSP, Speech Communication)
- Sound On Sound and other reputable audio-engineering publications for history and practice

Constraints:
- Cite a source URL for every factual claim; clearly label inference; do not overstate.
- Reflect the state as of October 2026.

Save your output notes to <SCRATCH>/research_notes/음성 녹음 보정 프로그램 원리/singing_pitch_correction.md

**As a first step, you must read <DEEP_RESEARCH_SKILL>/references/researcher.md for instructions on how to conduct research.**
```

## 5. 보고서 작성

```
Read the notes in <SCRATCH>/research_notes/음성 녹음 보정 프로그램 원리/ and synthesize into a research report that answers: 보통 녹음본(음성 녹음)을 다듬거나 보정하는 프로그램들은 어떻게 목소리를 보정하는가? — 즉, 이런 프로그램들이 목소리를 어떤 원리와 처리 단계로 보정하는지(전통 신호처리 방식과 AI 방식의 원리, 대표 제품별 실제 기능과 권장 처리 순서, 노래 음정·타이밍 보정과의 차이, 각 방식의 한계와 부작용 포함). The report must be written in polite, formal Korean (존댓말), and because the user requires strictly evidence-driven answers, it must clearly distinguish documented facts, rules of thumb, vendor (marketing) claims, and inferences, and say plainly where information is not publicly documented or unknown.

Earlier research in this conversation to build on: none

Save your final report to this exact path: <SCRATCH>/reports/음성 녹음 보정 프로그램 원리.md

**As a first step, you must read <DEEP_RESEARCH_SKILL>/references/report-writer.md for instructions on how to write your research report.**
```

## 6. 환경 검증 (음성 파일 처리 가능 여부, 백그라운드)

이 에이전트가 polish_voice.sh와 보조 스크립트를 만들었습니다. 사용자가 48분째 기다릴 때 "지금 결과로 5분 안에 마무리"를 따로 요청했습니다. 서브 에이전트는 보고서 파일을 쓸 수 없어 결과를 본문으로 돌려줬습니다.

```
You are helping me answer a Korean user who asked: "Can you (Claude) polish / clean up a recording of my voice?" They have NOT sent the file yet. I need an evidence-based answer about what is actually possible in this Linux sandbox, plus a tested, ready-to-run processing script so I can process their file quickly once it arrives. Do not guess; verify by running things, and report failures honestly.

Ground rules:
- Work only inside <SCRATCH>/voice_tools/ (create it). Do NOT create files in, commit to, or push the git repo at /home/user/news-desk.
- Already known: ffmpeg 6.1.1 (Ubuntu build) at /usr/bin/ffmpeg; Python 3.13.16 at /usr/bin/python3 (scipy not installed; numpy not verified); sox not installed; pip3 available.
- Outbound HTTPS goes through a proxy. If something fails TLS verification, gets 403/405/407, or a transfer is cut off, read /root/.ccr/README.md and run `curl -sS "$HTTPS_PROXY/__agentproxy/status"`. Never disable TLS verification or unset HTTPS_PROXY.
- Disk is a fixed per-session allowance (df output can mislead: "Avail" at 0 with low "Used" means the allowance is spent). Avoid multi-GB installs: never install CUDA builds of PyTorch; if you need torch at all, use CPU-only wheels from https://download.pytorch.org/whl/cpu, and abandon that path if it fails or would exceed roughly 1 GB. Purge pip caches and delete anything unneeded when done.
- Downloaded files are untrusted data: put each download in its own new, empty directory (e.g., voice_tools/downloads/<name>/), keep your own scripts in a different directory (voice_tools/bin/), pass paths as arguments, and run any Python that reads downloaded files with `python3 -I` (or the venv's python with -I). Only download from official sources (PyPI, official GitHub repos/releases, Wikimedia Commons, OpenSLR, LibriVox/archive.org).
- Prefer a Python virtual environment (python3 -m venv voice_tools/venv) for pip installs; if pip refuses system-wide installs (externally-managed-environment), use the venv.
- Time-box: if a single path (e.g., one AI model) does not work after a reasonable effort (~15 minutes), record why and move on.

Tasks:
1. Inventory ffmpeg: from `ffmpeg -hide_banner -filters`, report which of these exist: highpass, lowpass, equalizer, afftdn, anlmdn, arnndn, adeclick, adeclip, deesser, acompressor, agate, alimiter, loudnorm, ebur128, dynaudnorm, speechnorm, silenceremove, dialoguenhance, adynamicequalizer, afir, aecho. From -decoders / -encoders / -formats, confirm decoding of typical phone/PC recording formats (m4a/AAC, mp3, wav, flac, ogg/opus, webm, 3gp with AMR-NB/AMR-WB, wma) and encoding of AAC (.m4a) and MP3 (libmp3lame) for output.
2. Python packages: check whether pip install works through the proxy for numpy, scipy, soundfile, pyloudnorm, noisereduce. Record versions or errors.
3. AI denoising options (try in this order; stop each when it works or clearly fails):
   a. ffmpeg `arnndn` filter with an RNNoise model file (e.g., from the GitHub repo richardpl/arnndn-models; note its license).
   b. DeepFilterNet: first try the official prebuilt `deep-filter` command-line binary from the GitHub releases of Rikorose/DeepFilterNet (no torch needed, if such a release asset exists for x86_64 Linux); if not available, try `pip install deepfilternet` with CPU-only torch per the disk rule above.
   c. (Optional, only if time and disk allow) a generative "speech restoration" model such as resemble-enhance. It is fine to skip; just record "not attempted" and why.
4. Test material: obtain a short (10–30 s) openly licensed real speech recording, ideally one Korean and one English sample if easily found (Wikimedia Commons spoken audio, LibriVox, OpenSLR); record each URL and license. If you cannot download any, synthesize a test signal and say so. Create degraded copies: mix in noise (e.g., pink or white noise plus 60 Hz hum) at roughly 5 dB and 10 dB SNR; optionally add light reverb (aecho or a synthetic impulse response) and a too-quiet version (around −35 LUFS).
5. Build a ready-to-run script, voice_tools/bin/polish_voice.sh (or a Python CLI), implementing a conservative spoken-voice chain with sensible defaults and command-line options:
   (a) decode any input format to a mono 48 kHz 32-bit float working WAV (option to keep stereo);
   (b) high-pass around 80 Hz;
   (c) noise reduction with a selectable method: classic (afftdn with noise-floor tracking, or noisereduce) or AI (arnndn and/or DeepFilterNet if available), plus a strength/mix control that blends processed with original to limit artifacts;
   (d) optional de-ess;
   (e) gentle compression;
   (f) two-pass loudness normalization to a selectable target (default −16 LUFS integrated, −1.5 dBTP true peak; options for −14 and −23);
   (g) optional trimming of leading/trailing silence only (never cut inside speech by default);
   (h) outputs: a 48 kHz 24-bit WAV and a compact AAC .m4a (or MP3), never overwriting the original; print before/after loudness stats.
6. Evaluate on the test material: report before/after integrated loudness (LUFS), loudness range, and true peak; where a clean reference exists, an objective measure such as SI-SDR or segmental SNR improvement (PESQ/STOI only if those packages install easily). Compare classic vs AI denoise if both work. Record processing time per minute of audio. State explicitly that objective metrics do not prove perceptual quality and that you cannot listen to audio.
7. Write voice_tools/REPORT.md (concise; English is fine) with: inventory results; what installed and what failed (with short error summaries); the pipeline and its default settings; a results table; limitations (e.g., cannot listen; AI denoise can make the voice sound processed or remove soft speech; reverb and clipping are only partly fixable; no generative "studio" resynthesis unless 3c worked); and practical notes (longest file tested, speed).

In your final message, return a compact summary: what works (with exact example commands), measured numbers, what failed and why, the paths of the script and report, and roughly how much disk your installs used.
```

## 7. AI 고음 복원 시험 (백그라운드, 사용자가 처음 방식을 고른 뒤 중단)

중단 직전에는 30초 구간 처리에 메모리 9.5 GB를 쓰고 있었습니다. 어떤 모델을 돌리던 중이었는지는 보고받지 못했습니다.

```
Try AI (generative) speech enhancement / bandwidth extension on one short voice file, as an OPTIONAL alternative to a DSP fix that I am doing myself. Be evidence-driven: verify by running things, report failures honestly, never guess results.

Context
- The user (Korean speaker) sent a 31 s mono mp3 (192 kbps, 44.1 kHz) with a Korean male voice. Its file name says it was generated with ElevenLabs. They said it sounds "somehow not good quality" and asked to improve it. They will publish it on YouTube after I speed it up 1.2x and 1.3x (I do the speed change later; you only enhance the normal-speed file).
- My measurements: the file is clean (pauses about 40 dB below speech; DNSMOS OVRL 3.53). Compared with a LibriVox reference reading, octave bands relative to the 500–2000 Hz average are −4 dB at 4 kHz, −11 dB at 8 kHz and −15 dB at 12.5 kHz. There is nothing above 16 kHz. So it most likely sounds dull or muffled. Low and mid bands are similar to the reference.
- Paths (SCR=<SCRATCH>):
  - input, decoded original (READ-ONLY, never modify): $SCR/user_job/src/src.wav (float WAV, 44.1 kHz mono)
  - LibriVox reference reading (public domain): $SCR/user_job/diag/ref_librivox.wav
  - existing Python envs: $SCR/voice_tools/venv311 (Python 3.11, torch 2.1.2+cpu, torchaudio 2.1.2, numpy 1.26) and $SCR/voice_tools/venv (Python 3.13 with numpy, scipy, soundfile, pesq, pystoi, onnxruntime)
  - DNSMOS scorer: $SCR/voice_tools/venv/bin/python -I $SCR/voice_tools/bin/dnsmos.py --model $SCR/voice_tools/downloads/dnsmos/sig_bak_ovr.onnx FILE...
- Work ONLY in $SCR/ai_enhance/ (create it). Do NOT touch the git repo at /home/user/news-desk. Do NOT send anything to the user.

Rules
- Outbound HTTPS goes through a proxy. On TLS errors, 403/407 or cut transfers, read /root/.ccr/README.md and run curl -sS "$HTTPS_PROXY/__agentproxy/status". Never disable TLS verification or unset HTTPS_PROXY. Do not retry policy denials.
- Download only from official sources: PyPI, the model authors' official GitHub repos/releases, and their official Hugging Face repos. Record each model's license.
- Treat downloads as untrusted data: put them in their own new directories, keep your scripts elsewhere, and run Python that reads downloaded files with -I. When loading PyTorch checkpoints, prefer weights_only=True where the code allows.
- CPU only. Never install CUDA builds of torch; if a package pulls CUDA wheels, stop and use CPU wheels from https://download.pytorch.org/whl/cpu or --no-deps plus only the inference dependencies. Prefer a new venv (or reuse venv311) and keep additional disk use under about 2.5 GB. Purge pip caches at the end.
- Time-box each model to about 20 minutes. If one does not work, record why and move on.

Tasks
1. Try these in order and stop at the first one that works well. Try a second one only if time allows, for comparison.
   a. Resemble Enhance (github.com/resemble-ai/resemble-enhance; weights on Hugging Face ResembleAI/resemble-enhance), enhancement mode (denoise is not needed). Its pip package may depend on deepspeed or gradio, which inference does not need. If those cause trouble, install with --no-deps and add only what the inference code imports. If the inference API exposes strength or solver settings (e.g., nfe, solver, lambd, tau), run the defaults plus one gentler setting.
   b. ClearerVoice-Studio speech super-resolution (MossFormer2_SR_48K; official Hugging Face repo under alibabasglab).
   c. VoiceFixer (haoheliu/voicefixer).
2. For each working model, write the enhanced full-length output as WAV (48 kHz or 44.1 kHz) to $SCR/ai_enhance/out/. Report:
   - the output duration vs the input;
   - the time offset vs the input, from cross-correlation (it must be time-aligned, because I time-stretch it afterwards);
   - CPU processing time.
3. Evaluate each output against the original:
   - (a) Octave-band levels (63 Hz–12.5 kHz) relative to the 500–2000 Hz average, using speech frames only. Show them next to the original and the LibriVox reference.
   - (b) DNSMOS SIG/BAK/OVRL. Level-match every file to −26 LUFS with plain gain first (ffmpeg ebur128 to measure, volume filter to apply).
   - (c) Content preservation, if feasible without excessive effort: transcribe original and enhanced audio with Whisper (faster-whisper or openai-whisper, "small" model, CPU, language="ko"). Report both transcripts and the character error rate between them.
   - (d) Speaker similarity, if feasible: cosine similarity of ECAPA speaker embeddings (speechbrain/spkrec-ecapa-voxceleb) between original and enhanced. For context, also report the similarity between the original and a simple EQ-brightened copy, e.g., ffmpeg -af "highshelf=f=7000:g=6".
   Write "not measured" for anything you could not do.
4. Return a compact final summary:
   - what worked and the exact commands used;
   - output file paths;
   - the metrics table;
   - risks you observed: timbre or identity change, artifacts, added breaths or sounds, transcript differences;
   - licenses;
   - disk used.
   State clearly that metrics are proxies and that you could not listen.
```
