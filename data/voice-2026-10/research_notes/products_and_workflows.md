# Voice-recording cleanup & polishing products: features, processing, workflows and vendor cautions (state as of Oct 2026)

Scope note: product-level notes drawn mainly from official documentation (iZotope RX 12 user guide, Descript help center, Auphonic help, Audacity manual/changelog, Intel OpenVINO GitHub, Apple/Samsung/NVIDIA support pages, Adobe staff posts). Access caveats: helpx.adobe.com and help.krisp.ai blocked automated fetching (HTTP 403 / bot wall), so Adobe help-page and Krisp help-center statements below come from search-result excerpts and are flagged as such. Items marked "(marketing)" are vendor promotional claims that the vendor's technical docs do not substantiate.

## 1. What does each product say it does to the voice (modules, DSP vs AI/ML, user controls), and which claims are verifiable from official docs vs marketing?

### Takeaway
Official documentation is most detailed for iZotope RX 12, Auphonic, Descript and Audacity. Within RX, the module docs explicitly label only Dialogue Isolate and Breath Control as machine learning. iZotope's product page and blog also attribute ML or "neural nets" to the separation tools: Music Rebalance, Scene Rebalance and De-bleed. Others are documented as classic signal processing: Voice De-noise is described as a 64-band multiband gate, and Spectral De-noise as noise-profile spectral subtraction. The rest (De-reverb, De-click, De-ess, De-hum, De-clip, Loudness Control) carry no ML claim. Adobe Enhance Speech, Descript Studio Sound, NVIDIA Broadcast, Samsung Audio Eraser, Apple Voice Isolation and CapCut describe outcomes ("studio quality", "AI") but publish no technical internals. Their claims are therefore verifiable only at the level of what the feature is said to remove and which controls exist.

### Cited Findings

#### iZotope RX 12 (current version; Elements / Standard / Advanced)
- Version/date: iZotope's "RX 12 new tools" blog post is dated May 14, 2026. It lists new Scene Rebalance (ADV), Stems View (STD/ADV) and Trim Silence (ADV), a rebuilt De-bleed and Breath Control, and improved Music Rebalance and Dialogue Isolate — [iZotope blog: RX 12](https://www.izotope.com/community/blog/rx-12). Third-party trade coverage dates the launch to late April 2026 (Mix Online cites Apr 29, 2026; KVR is dated May 3, 2026). This was seen only in search-result summaries — [Mix Online](https://www.mixonline.com/technology/news-products/izotope-remains-in-the-restoration-game-with-rx-12-launch).
- Vendor-level ML statements (marketing):
  - RX is "Powered by pioneering machine learning tech."
  - "Updated neural nets, new realtime plugins, rebuilt fan-favorites with cutting-edge machine learning."
  - "For RX 12, our award-winning research team has developed brand-new neural nets for some of our most popular tools, letting you achieve cleaner processing with fewer artifacts."
  - Source: [iZotope RX 12 Advanced product page](https://www.izotope.com/products/rx-advanced). The blog adds that Breath Control is "Powered by advanced ML technology" and that Music Rebalance/Dialogue Isolate have "Upgraded neural nets" — [iZotope blog: RX 12](https://www.izotope.com/community/blog/rx-12).
- **Repair Assistant** (documented behaviour):
  - "designed to detect common audio problems in a recording and quickly provide suggested settings."
  - The user picks Voice mode ("intended for spoken word or dialogue") or Music mode ("full-mix music recording, individual instruments, or isolated sung vocals"), then clicks Learn. Learn analyzes any selection and doesn't need noise-only audio.
  - Voice-mode sections:
    - Clean Up: De-noise "Controls the applied amount of Dialogue Isolation processing"; De-reverb; De-hum on/off (works only if hum was detected); De-click on/off.
    - Tone: Tilt/Scoop %, Lo-cut, Hi-cut.
    - De-Ess: Shaping, Threshold, Fast/Slow.
    - De-Clip: Threshold, Output Gain, true-peak Limiter.
  - Each section has an Audition button that plays only what is being removed.
  - Open Module Chain is "available in RX 12 Advanced only."
  - Source: [RX 12 docs: Repair Assistant](https://docs.izotope.com/rx12/en/repair-assistant.html). The product page's "intelligently recognizes and proposes fixes" is marketing wording; the docs do not say whether Repair Assistant's analysis is ML-based — [product page](https://www.izotope.com/products/rx-advanced).
- **Dialogue Isolate** (STD & ADV, module & plug-in):
  - Separates "spoken dialogue from a constant or non-stationary background noise, such as hiss, crowds, traffic, footsteps, weather". It "includes reverb removal technology".
  - It "uses a machine learning algorithm trained on a large library of speech, noise, and reverberant data" and separates audio into three components: dialogue, noise and reverberation.
  - Controls: Voice, Reverb and Noise gain (dB), plus Sensitivity. Higher Sensitivity "might also introduce artifacts and reduce dialogue clarity."
  - ADV-only controls: Quality ("Good / Real-time" vs "Best / Offline"), a 4-band multi-band interface, and Stem Split.
  - Source: [RX 12 docs: Dialogue Isolate](https://docs.izotope.com/rx12/en/dialogue-isolate.html).
- **Dialogue De-reverb**: the RX 12 Module List contains "De-reverb" but no separate "Dialogue De-reverb" module — [RX 12 docs: Module List](https://docs.izotope.com/rx12/en/module-list.html). Dialogue-specific reverb removal is documented inside Dialogue Isolate — [Dialogue Isolate](https://docs.izotope.com/rx12/en/dialogue-isolate.html).
- **De-reverb** (no ML claim in docs):
  - "processes audio according to the reverberant/direct ratio (also known as wet/dry ratio)."
  - Controls: Learn; Reduction (negative values add reverb); Reverb Profile per band; Tail Length ("an approximation of RT-60"); Artifact Smoothing; Enhance Dry Signal; Output Reverb Only.
  - RX Elements: plug-in only.
  - Source: [RX 12 docs: De-reverb](https://docs.izotope.com/rx12/en/de-reverb.html).
- **Voice De-noise** (classic DSP per docs):
  - "an intuitive, zero latency de-noiser". "Under the hood is a series of 64 psychoacoustically spaced bandpass filters which act as a multiband gate."
  - Controls: Adaptive mode (automatic threshold, "set lower to prevent artifacts"); Learn in Manual mode ("at least one second of pure noise" recommended); Optimize for Dialogue/Music; Filter type Surgical/Gentle; 6 threshold nodes; Threshold; Reduction (dB).
  - RX Elements: plug-in only.
  - Source: [RX 12 docs: Voice De-noise](https://docs.izotope.com/rx12/en/voice-de-noise.html).
- **Spectral De-noise** (classic DSP per docs):
  - Removes "stationary or slowly changing tonal noise and broadband hiss by learning a profile of the offending noise and then subtracting it."
  - Controls: Learn (fixed profile); Adaptive mode (for changing noise such as traffic or ocean); separate Threshold and Reduction for "Noisy/Tonal".
  - Quality algorithms A–D: A uses time smoothing; B adaptive 2D smoothing; C multiresolution; D "adds high-frequency synthesis". C and D are "not recommended for real-time operation."
  - Artifact Control blends "spectral subtraction or wide band gating."
  - Source: [RX 12 docs: Spectral De-noise](https://docs.izotope.com/rx12/en/spectral-de-noise.html).
- **De-click**:
  - "analyzes audio for amplitude irregularities and smoothes them out" (mouth noises, digital errors, cell-phone interference).
  - Algorithms: Single band; Multi-band (periodic / random clicks); Low latency ("Works well on mouth clicks"; suitable for real time).
  - Controls: Sensitivity, Frequency Skew, Click Widening.
  - The Instant Process tool uses Interpolate for selections under 4,000 samples.
  - Source: [RX 12 docs: De-click](https://docs.izotope.com/rx12/en/de-click.html).
- **Mouth De-click** (STD & ADV): "detects and reduces mouth noises such as clicks and lip smacks." Controls: Sensitivity, Frequency Skew, Click Widening — [RX 12 docs: Mouth De-click](https://docs.izotope.com/rx12/en/mouth-de-click.html).
- **De-plosive** (STD & ADV): "intelligently identify, separate and reduce plosives … while still preserving the fundamental frequency content and harmonics." Detection targets 20–80 Hz. Controls: Sensitivity, Strength, Frequency Limit (plosives "typically manifest between 20Hz to 300Hz, but may sometimes reach as high as 500Hz"). The method is not documented — [RX 12 docs: De-plosive](https://docs.izotope.com/rx12/en/de-plosive.html).
- **De-ess** (STD & ADV): Classic mode is a "broadband gain envelope"; Spectral mode "is a multiband compressor with dozens of bands". Controls: Threshold (Relative/Absolute), Cutoff Frequency, Spectral Flattening, Spectral Tilt, Speed Fast/Slow — [RX 12 docs: De-ess](https://docs.izotope.com/rx12/en/de-ess.html).
- **Breath Control** (STD & ADV, rebuilt in RX 12):
  - "uses machine-learning algorithms to detect breaths in dialogue or vocal recordings and suppress them." It distinguishes breaths "based on their harmonic structure" and works "regardless of level."
  - Controls: Level (−Inf to 0 dB); Target/Gain mode; Natural/Gated (keeps or removes ambience); Sensitivity; Algorithm (Real-time / Offline / Classic = "legacy algorithm used in RX 11").
  - Source: [RX 12 docs: Breath Control](https://docs.izotope.com/rx12/en/breath-control.html).
- **De-hum**:
  - Two modes. Static is for simple hum with few harmonics that doesn't overlap speech. Dynamic is for hum with "more than a dozen harmonics", inharmonic hum, or buzz overlapping speech ("Less Ringing due to gated notching").
  - Controls: Learn, Adaptive, Sensitivity, Bands, Filter Q, Range, and up to 16 harmonics.
  - RX Elements: plug-in only.
  - Source: [RX 12 docs: De-hum](https://docs.izotope.com/rx12/en/de-hum.html).
- **De-clip**: "will process any audio above a given threshold, interpolating the waveform to be more round." Controls: histogram-guided Threshold, quality modes, Makeup Gain, Post-limiter — [RX 12 docs: De-clip](https://docs.izotope.com/rx12/en/de-clip.html).
- **Spectral Repair** (STD & ADV): "treats selections within the spectrogram/waveform display as corrupted audio that will be repaired using information from outside of the selection." It can attenuate the selection to the noise floor, replace it with surrounding audio, "or generate entirely new audio." Attenuate "does not resynthesize any audio." Example targets include coughs, chair squeaks and phones ringing — [RX 12 docs: Spectral Repair](https://docs.izotope.com/rx12/en/spectral-repair.html).
- **Loudness Control** (STD & ADV): "adjusts the gain of the signal in order to meet the specified loudness standard, such as BS.1770". The gain "stays fixed in time" with a post-limiter for true peak. Presets include EBU R128 (−23 LUFS, −1 dBTP), ATSC A/85 (−24, −2) and AES TD1006 (−16, −1) — [RX 12 docs: Loudness Control](https://docs.izotope.com/rx12/en/loudness-control.html).
- **Leveler** (ADV): "a compressor with a makeup gain" aiming at a K-weighted target RMS. It writes a Clip Gain envelope and has Dialogue/Music optimization plus Ess and Breath parameters to avoid pumping — [RX 12 docs: Leveler](https://docs.izotope.com/rx12/en/leveler.html).
- **Edition gating**: Trim Silence, Leveler, De-rustle, Dialogue Contour, Scene Rebalance, Spectral Recovery and others are ADV-only. Dialogue Isolate, Breath Control, Mouth De-click, De-plosive and Spectral De-noise are STD & ADV — [RX 12 docs: Module List](https://docs.izotope.com/rx12/en/module-list.html).
- Independent review (Sound On Sound, RX 11 Advanced, John Walden, July 2024):
  - Dialogue Isolate "did a remarkable job of clearing away the sonic clutter … without compromising the quality of the spoken voice"; real-time latency "perfectly acceptable".
  - Repair Assistant "does seem fairly CPU intensive."
  - Competitor Accentize dxRevive was "particularly impressive."
  - Source: [Sound On Sound](https://www.soundonsound.com/reviews/izotope-rx11-advanced).

#### Adobe Enhance Speech (Adobe Podcast web; Premiere Pro; Audition)
- Adobe Podcast web page (marketing): "Free AI filter for cleaning up spoken audio"; "This AI audio filter improves spoken audio to make it sound like it was recorded in a soundproofed studio" — [Adobe Podcast Enhance](https://podcast.adobe.com/en/enhance).
- Adobe Podcast FAQ, seen only as a search excerpt because the page blocks automated fetch: Enhance Speech works by "filtering out noise and artifacts, adjusting pitch and volume levels, and normalizing the audio" — [Adobe Podcast FAQ](https://helpx.adobe.com/podcast/adobe-podcast-faq.html).
- **v2** (Adobe community manager announcement, Nov 20, 2024):
  - "Powered by our Sound Lift AI model, the updated slider allows you to balance speech clarity with ambient noise."
  - Marketing claims: "Clear, natural dialogue without robotic tones—no matter the language or recording conditions"; "Background noise, reverb, and music—v2 removes it all"; a clarity boost for quiet or distant audio.
  - A staff reply says users will be able to "independently control speech enhancement and background noise."
  - Source: [Adobe Community: Enhance Speech v2 is here](https://community.adobe.com/questions-514/enhance-speech-v2-is-here-1498584).
- **v2 slider: user reports, not official.** Some users say there is "barely any difference between 1% processing and 100%" and that v2 removes laughter. Adobe staff replied that adjusting the sliders should produce an audible difference and asked for sample files — [Adobe Community thread, p.2](https://community.adobe.com/t5/adobe-podcast-discussions/enhance-speech-v2-is-here/td-p/14992650/highlight/true/page/2); [v2 thread](https://community.adobe.com/questions-514/enhance-speech-v2-is-here-1498584).
- **Premiere Pro** (Adobe staff, beta announced Sept 13, 2023):
  - "the same feature that has been available online via Adobe Podcast", but "optimized to perform locally on your machine".
  - The Mix Amount slider blends raw and enhanced audio so natural background noise can come through.
  - Source: [Adobe Community announcement](https://community.adobe.com/announcements-732/now-released-enhance-speech-in-premiere-pro-313485). General release came in Premiere Pro 24.2 (search-summary only) — [RedShark News](https://www.redsharknews.com/adobe-premiere-pro-24.2-officially-adds-enhance-speech-tiktok-export-and-more).
- **v1 vs v2 in Premiere**: in August 2025 Adobe staff wrote "At the moment, Enhance Speech v1 in available in Premiere". The goal is "to eventually make v2 available in Premiere, but I don't have a timeline" — [v2 thread](https://community.adobe.com/questions-514/enhance-speech-v2-is-here-1498584).
- **Audition**: no official documentation found confirming Enhance Speech in Audition. A March 2024 user idea post asks for it — [Adobe Community idea](https://community.adobe.com/t5/audition-ideas/ai-speech-enhancement-for-essential-sound-in-audition/idi-p/14459257).

#### Descript (Studio Sound, Regenerate / AI Speakers, leveling, room tone)
- **Studio Sound**:
  - "an AI-powered audio effect that enhances spoken voice by reducing background noise, echo, and other distractions." The marketing-style line "Descript's AI cleans up the voice so a rough take sounds far closer to a studio recording" appears on the same page.
  - It "requires an internet connection and is applied at the file level."
  - Control: an **Intensity** slider "to control how much enhancement is applied." It can also be enabled while recording.
  - Source: [Descript: Studio Sound](https://help.descript.com/effects-animations-transitions/studio-sound).
  - The AI Tools overview adds that Studio Sound "improves clarity, removes room echo, and smooths inconsistent audio across speakers" — [Descript: Sound good with AI tools](https://help.descript.com/descript-tour/sound-good-tools).
- **Auto-leveling** (project setting): "Automatically apply -16dB loudness normalization to all audio in your project" — [Descript: Project settings](https://help.descript.com/working-in-projects/project-settings).
- **Room tone**: "uses artificial intelligence to recognize the background sound in a speech recording, then creates a similar noise profile." It is added to gap clips. It analyzes the first 30 s, and Descript recommends recording at least 15 s of silence first — [Descript: Room tone](https://help.descript.com/effects-animations-transitions/room-tone).
- **Regenerate** (successor workflow to the former Overdub; the current help center uses "Regenerate" and "AI Speakers"):
  - "uses AI to smooth, polish, or rewrite parts of a video". Uses: "heal jump cuts, clean up awkward pacing, fix a distracting noise, or change what a speaker originally said".
  - Output is "Audio & video" by default, or "Audio only."
  - Source: [Descript: Regenerate overview](https://help.descript.com/script-editing/regenerate-overview).
  - Changing words requires an authorized custom AI speaker; stock voices are not supported — [Descript: Use Regenerate to change recorded audio](https://help.descript.com/script-editing/change-meaning).
- **Voice clone consent**: Descript requires "explicit recorded authorization" from the person whose voice is cloned, via an English consent statement. It "cannot create voice clones for" a deceased person, a non-consenting person, or "Audio from an AI or artificial source." Clones are "generated using a model based on US English pronunciation"; users can switch among ElevenLabs v2/v3/v4 models — [Descript: Create a custom voice clone](https://help.descript.com/ai-speech/custom-speaker).

#### Auphonic (web service)
- Global claim: "All algorithms were trained with data from our web service and they keep learning and adapting to new audio signals every day." Audio "is processed with AI algorithms, that are permanently changing over time" — [Auphonic: Singletrack algorithms](https://auphonic.com/help/algorithms/singletrack.html).
- **Adaptive Leveler**:
  - "corrects loudness differences between segments within one file". It classifies speech, music and background segments. "The algorithm was trained with over five years of audio files" — [Auphonic: Singletrack algorithms](https://auphonic.com/help/algorithms/singletrack.html).
  - **Leveler Strength**: 100% = full leveling; 70% ≈ 3 dB more dynamic range. Below a set dynamic range ("Loudness Comfort Zone") the leveler is bypassed.
  - **Compressor**: Auto / … / Off. Auto uses Medium compression for strength ≤100% and Hard for >100%.
  - **Music/speech handling**: separate music/speech strength and compressor, a MusicSpeech Classifier, and Music Gain.
  - **Broadcast Mode** targets: MaxLRA, MaxS (3 s window) and MaxM (0.4 s window).
  - Source: [Auphonic: Production settings](https://auphonic.com/help/web/production.html).
- **Noise & Reverb Reduction** (current methods):
  - **Static Denoiser** "removes reverb and stationary, technical noises". It "uses AI algorithms for noise detection" and so can work under continuous music.
  - **Dynamic Denoiser** "removes everything but voice and music."
  - **Speech Isolation** keeps only speech, so "all noise and even music will be removed."
  - **Classic Denoiser** "works only if there is a short silent segment, where a noise print can be extracted". It includes hum reduction with a 50/60 Hz/Auto base frequency and a hum amount setting.
  - Sources: [Auphonic: Production settings](https://auphonic.com/help/web/production.html); [Singletrack algorithms](https://auphonic.com/help/algorithms/singletrack.html).
- **Denoiser controls**: Remove Noise (maximum reduction in dB, "default value is 100 dB (full)"); Remove Reverb (Static, Dynamic and Speech Isolation; default 100 dB); Remove Breaths (Dynamic and Speech Isolation). Denoise segments can be edited per segment in the Auphonic Editor — [Auphonic: Production settings](https://auphonic.com/help/web/production.html).
- **July 31, 2025 change**: a new Static Denoiser was introduced, and the original Static Denoiser was renamed "Classic" — [Auphonic blog, 2025-07-31](https://auphonic.com/blog/2025/07/31/new-auphonic-static-and-music-denoiser/). A May 2024 post said the Static Denoiser had no Remove Reverb or Remove Breathings parameters — [Auphonic blog, 2024-05-16](https://auphonic.com/blog/2024/05/16/independently-control-noise-reverb-and-breath-reduction-amounts/). That apparent conflict is explained by the 2025 rename (see Inferences).
- **Filtering**:
  - Adaptive high-pass filtering, applied per segment.
  - **Voice AutoEQ** "automatically removes sibilance (De-Esser), plosives (De-Plosive) and optimizes the frequency spectrum". Auphonic calls it "essentially dynamic equalization and filtering."
  - **Voice AutoEQ + Bandwidth extension** "recovers lost high frequencies" (speech only).
  - **Studio Voice (Beta)** "reconstructs a clear, studio-quality voice". It addresses "codec and compression artefacts, distorted or clipped voices" and artefacts from other denoisers.
  - Source: [Auphonic: Production settings](https://auphonic.com/help/web/production.html).
- **Loudness targets**:
  - TV (EBU R128, ATSC A/85); −16 LUFS (Apple Music, Google, AES recommendation); −14 LUFS (YouTube, Spotify, Tidal); Netflix (−27 LUFS); Audible/ACX (−18 to −23 dB RMS) — [Auphonic: Singletrack algorithms](https://auphonic.com/help/algorithms/singletrack.html).
  - True peak defaults to −1 dBTP for targets ≥ −23 LUFS and −2 dBTP for targets ≤ −24 LUFS. An optional "Dual Mono" flag subtracts 3 LU for mono productions. Normalization method can be Program Loudness, Dialog Loudness or RMS (ACX) — [Auphonic: Production settings](https://auphonic.com/help/web/production.html).

#### Audacity (built-in effects) and Intel OpenVINO AI plugins
- **Noise Reduction** (classic noise-profile method):
  - "can reduce constant background sounds such as hum, whistle, whine, buzz, and 'hiss'". It needs "a region in the waveform that contains only the noise."
  - Step 1 is Get Noise Profile (minimum 2048 samples). Step 2 sets the controls:
    - Noise Reduction (dB): "Use the lowest value that reduces the noise to an acceptable level".
    - Sensitivity: 0–24.
    - Frequency Smoothing: default 6; "lower … favor music and higher settings tend to favor spoken word."
    - Reduce / Residue options.
  - Time smoothing is fixed (20 ms attack, 100 ms release).
  - Source: [Audacity Manual: Noise Reduction](https://manual.audacityteam.org/man/noise_reduction.html).
- **Compressor**: Threshold, Ratio, Knee width, Make-up gain, Lookahead, Attack and Release. Presets include "Voice Memos Balance" for iPhone Voice Memos recordings — [Audacity Manual: Compressor](https://manual.audacityteam.org/man/compressor.html).
- **Normalize**: peak normalization (default −1 dB) with "Remove DC offset" on by default — [Audacity Manual: Normalize](https://manual.audacityteam.org/man/normalize.html).
- **Loudness Normalization**: "based on EBU R 128". "Perceived loudness" defaults to −23 LUFS; RMS defaults to −20 dB. "Treat mono as dual-mono" is checked by default — [Audacity Manual: Loudness Normalization](https://manual.audacityteam.org/man/loudness_normalization.html).
- **OpenVINO AI plugins** (Intel, GPL v3):
  - The effects "run 100% locally on your PC — no internet connection necessary." They run on CPU, GPU or NPU.
  - Features: Noise Suppression; Whisper Transcription (whisper.cpp); Super Resolution (port of AudioSR); Music Separation (Demucs v4); Music Generation (MusicGen).
  - Source: [intel/openvino-plugins-ai-audacity README](https://github.com/intel/openvino-plugins-ai-audacity).
- **OpenVINO Noise Suppression**: "removes background noise from an audio sample containing spoken audio." Models: deepfilternet2, deepfilternet3 and denseunet. "It's recommended to use one of the deepfilternet models, as denseunet is included only for legacy purposes." First model load "usually takes 10 to 30 seconds"; compiled models are then cached — [OpenVINO Noise Suppression doc](https://github.com/intel/openvino-plugins-ai-audacity/blob/main/doc/feature_doc/noise_suppression/README.md).

#### Real-time tools
- **Krisp**: the vendor blog (updated Aug 2026) says "Krisp's noise cancellation also runs on-device: your audio is processed locally on your machine rather than sent to a server." The site lists AI Noise Cancellation, Accent Conversion (speaker and listener side) and an AI Meeting Assistant — [Krisp blog](https://krisp.ai/blog/remove-background-noise/). Technical internals: not publicly documented in the sources reached.
- **NVIDIA Broadcast** (NVIDIA FAQ):
  - **Noise Removal**: "Remove distracting background sounds from your microphone feed"; can also be applied to incoming audio.
  - **Room Echo Removal**: reduces echo and reverb typical of small untreated rooms.
  - **Studio Voice**: "uses an AI equalizer to spectrally enhance your voice", with Default/Bright/Full/Warm mic profiles. It is in beta.
  - Source: [NVIDIA Broadcast FAQ](https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-app/faq/).
  - Effects run on "AI processors called Tensor Cores", and "You can also adjust the effect strength" — [NVIDIA Broadcast setup guide](https://www.nvidia.com/en-us/geforce/guides/broadcast-app-setup-guide/).
- **Apple Mic Modes**:
  - **Standard** "Uses standard voice processing"; **Voice Isolation** "Prioritizes your voice and blocks ambient noises"; **Wide Spectrum** "Leaves ambient noises unfiltered"; **Automatic** picks the best mode. For example, it uses Voice Isolation on receiver calls and Standard on speakerphone.
  - iOS version requirements (FaceTime: iOS 15; phone calls: iOS 16.4; recording apps such as Voice Memos: iOS 26; Automatic: iOS 18) are listed under question 6.
  - Source: [Apple Support 101993](https://support.apple.com/en-us/101993). The method is not publicly documented.

#### Mobile / consumer tools (Korean-market relevant)
- **Apple Voice Memos**: "Enhance a recording. Improve the sound quality of your Voice Memos by reducing background noise and room reverberation", turned on under Playback Settings → Enhance Recording — [Apple: Voice Memos (Mac guide)](https://support.apple.com/guide/mac-pro-rack/apdd1444d464/mac). Third-party coverage of the iPhone version says it is a magic-wand on/off toggle with "no dials or sliders" and can be reverted — [Business Insider NL](https://www.businessinsider.nl/a-new-ios-14-feature-allows-you-to-enhance-your-iphone-voice-memo-recordings-for-clearer-audio-files-heres-how-to-use-it/).
- **Apple Audio Mix** (iPhone 16 family and later, Photos → Edit; third-party descriptions only): modes Standard / In-Frame / Studio / Cinematic, each with an intensity slider — [TapSmart guide](https://www.tapsmart.com/tips-and-tricks/audio-mix-guide/); [BGR](https://www.bgr.com/2276353/audio-mix-iphone-feature-to-improve-audio-quality-in-videos/). Not verified on support.apple.com.
- **Samsung Galaxy Audio Eraser (오디오 지우개)** — Samsung Canada support page:
  - Analyzes a video's audio and lets you adjust each detected sound type with sliders: Voices, Wind, Music, Nature, Crowd, Noise.
  - "Hear original" compares against the unedited audio. "Select Auto to have Galaxy AI automatically reduce noise."
  - Source: [Samsung CA support](https://www.samsung.com/ca/support/mobile-devices/how-to-remove-unwanted-sound-from-videos-using-audio-eraser-on-your-galaxy/).
- **Samsung Korea service page** (삼성전자서비스, dated 2026-02-26):
  - Supported devices: Galaxy S24 series and later, and Z Fold6/Flip6 and later, on One UI 7.0+.
  - Apps: Gallery (editing); YouTube app (via the quick panel, with strength and voice-emphasis settings); Samsung Notes (reduces background sound in recordings).
  - Edits are saved as a new copy and the original is kept.
  - Source: [삼성전자서비스: 오디오 지우개](https://www.samsungsvc.co.kr/solution/4036399).
- **Audio Eraser in Voice Recorder and call recording**: a Samsung Community post (unofficial) says the feature also works in Voice Recorder and call recording on One UI 8 devices — [Samsung Community](https://r1.community.samsung.com/t5/camcyclopedia/%EC%98%A4%EB%94%94%EC%98%A4-%EC%A7%80%EC%9A%B0%EA%B0%9C-audio-eraser/ba-p/34063686). Android Authority reports that the Galaxy S26 extends Audio Eraser to third-party apps (YouTube, Netflix) via quick settings — [Android Authority](https://www.androidauthority.com/samsung-galaxy-s26-audio-eraser-3644193).
- **CapCut**: a vendor resource article (Nov 5, 2025) on the desktop editor says Reduce noise is a toggle: "Simply toggle it on, and you can adjust the intensity to your liking." It calls this "literally a one-click solution" (marketing) — [CapCut: Mastering Audio](https://www.capcut.com/resource/noise-reduction-guidance). An Apple App Store editorial (search summary) describes the mobile flow: select a clip → Edit → "Enhance voice" → adjust the level — [App Store story](https://apps.apple.com/st/ipad/story/id1745127492). CapCut's "voice isolator" page claims removal of music, wind and traffic (marketing; search summary) — [CapCut voice isolator](https://www.capcut.com/resource/voice-isolator).
- **Vrew (브루)**: "Remove Noise" lives under [Effects] → [Noise Removal]. Release 4.2.0 brought it to the web version, and it "now replaces the audio directly" instead of making a separate file — [Vrew 4.2.0 update](https://docs.channel.io/vrew-us/en/articles/Vrew-420-Update-3425c357). Whether this is AI or DSP is not documented.
- **Naver CLOVA Note (클로바노트)**: the App Store and search sources describe recording, Korean/English/Japanese/Chinese transcription, speaker identification and AI summaries. No noise-reduction or voice-enhancement feature was found, so it is skipped — [App Store: 클로바노트](https://apps.apple.com/kr/app/%ED%81%B4%EB%A1%9C%EB%B0%94%EB%85%B8%ED%8A%B8-ai-%EC%9D%8C%EC%84%B1-%EA%B8%B0%EB%A1%9D/id1530010245).

### Inferences
- In RX 12, documented ML is concentrated in source-separation-style tools (Dialogue Isolate, Breath Control, Music/Scene Rebalance, De-bleed). The workhorse repair modules are documented with classic DSP descriptions. Voice De-noise is a multiband gate; Spectral De-noise uses profile subtraction and gating; De-ess is a multiband compressor; De-hum uses notch filters; De-clip interpolates. The product page's blanket "machine learning" framing therefore overstates how much of RX is ML.
- Repair Assistant's Voice-mode "De-noise" slider drives Dialogue Isolation processing (per docs). Its default noise reduction for speech is therefore the ML separator, not Spectral/Voice De-noise.
- The Auphonic conflict over Static Denoiser reverb control is most likely resolved by the July 2025 rename. The 2024 "Static Denoiser" without reverb or breath controls is today's "Classic" method. The new Static Denoiser has Remove Reverb.
- Adobe, Descript, NVIDIA, Samsung, Apple and CapCut publish no algorithmic details. "Studio quality" style claims are marketing; only the listed targets (noise, reverb/echo, music) and controls are verifiable.
- Descript Regenerate's "change what was said" (voice cloning) is generative re-synthesis, not cleanup. Report writers should keep it separate from enhancement features.

### Gaps
- iZotope does not document whether Repair Assistant's problem detection is ML-based. Neural-network architectures and training data are not publicly documented beyond "a large library of speech, noise, and reverberant data."
- The date when Dialogue De-reverb stopped being a separate RX module was not verified; the RX 11 docs were not fetched.
- No official Adobe help page could be fetched (403). Adobe's documented technical description of v1 vs v2, the exact slider names and ranges, and Audition support remain unverified.
- No official CapCut help-center page was found. CapCut's descriptions come from its marketing "resource" articles and third-party guides.
- No official Vrew documentation was found for filler-word removal or for the noise-removal method. A blog claims an "AI 음성 분리" feature, but this is unverified.

## 2. Where does processing run (on-device vs cloud upload), and what data/privacy terms are documented for uploaded audio?

### Takeaway
Local processing: iZotope RX, Audacity (including the OpenVINO plugins), Adobe's Premiere Pro Enhance Speech, Krisp noise cancellation and NVIDIA Broadcast (on the GPU). Cloud processing: Adobe Podcast (web), Descript Studio Sound (internet required) and Auphonic (web service). Only Descript and Auphonic publish explicit training and retention terms. Apple, Samsung, CapCut and Vrew do not say where voice processing runs in the pages reached.

### Cited Findings
- **iZotope RX**: plug-in formats are VST3, AU, AAX and AAX AudioSuite, and VST2 is no longer supported (trade coverage, search summary) — [KVR](https://www.kvraudio.com/news-print.php?id=66802). The RX 12 module docs describe only local editor and plug-in operation. Text Navigation transcription "runs in the background at approximately 7 - 9X real time" — [RX 12 docs: Text Navigation](https://docs.izotope.com/rx12/en/text-navigation.html).
- **Adobe Premiere Pro Enhance Speech**:
  - "optimized to perform locally on your machine"; "no internet connection is required"; usable on "an unlimited number of clips"; "The model is not trained on your usage."
  - Source: [Adobe Community announcement](https://community.adobe.com/announcements-732/now-released-enhance-speech-in-premiere-pro-313485).
- **Adobe Podcast (web)**:
  - Processing is cloud-based: the Premiere post contrasts local processing with "the Adobe Podcast service" — [Adobe Community announcement](https://community.adobe.com/announcements-732/now-released-enhance-speech-in-premiere-pro-313485).
  - A September 2026 community request asking Adobe whether Enhance Speech-processed audio is used for AI voice-model training shows no reply (search summary) — [Adobe Community](https://community.adobe.com/questions-514/request-for-clarification-regarding-the-use-of-adobe-podcast-enhance-speech-processed-audio-for-ai-voice-model-training-1639827).
- **Descript**:
  - Studio Sound "requires an internet connection" — [Descript: Studio Sound](https://help.descript.com/effects-animations-transitions/studio-sound).
  - Descript "automatically saves and syncs your work to the cloud as you edit" — [Descript: Save your work to the cloud](https://help.descript.com/working-in-projects/save).
  - Privacy page: "Current AI models in production use no Descript user data." Internal R&D models use "only data from users who have opted into data sharing." Sub-processors such as OpenAI are bound by agreements "that no data is used by them to train their AI models." Enterprise drives have data sharing "disabled by default." Users can opt out under App Settings → Profile → "Share data with Descript."
  - Source: [Descript: Account data and privacy](https://help.descript.com/account-and-app-settings/data-privacy).
- **Auphonic** (privacy policy):
  - Uploaded content "may be viewed and/or listened to by an Auphonic employee or any person contracted by Auphonic to work on our audio processing algorithms."
  - "Business customers can opt out" of use for "training and fine-tuning our models" via a training opt-out flag.
  - Productions and files "will be permanently deleted from our servers … after a certain number of days … (21 days for audio, 7 days for video and API …)."
  - The policy also mentions storage "in an internal storage space for the purpose of improving our audio processing algorithms." The excerpt retrieved was truncated, so its scope is unclear.
  - Users "fully retain any rights" to content, and it is not shared with third parties without permission.
  - Source: [Auphonic Privacy Policy](https://auphonic.com/privacy).
- **Auphonic transcription**: speech recognition sends "small audio segments to the speech recognition engine". Options are internal "Auphonic Whisper ASR" or connected external ASR services — [Auphonic: Production settings](https://auphonic.com/help/web/production.html).
- **Audacity OpenVINO plugins**: "run 100% locally on your PC — no internet connection necessary" — [OpenVINO README](https://github.com/intel/openvino-plugins-ai-audacity).
- **Krisp**:
  - Vendor blog: noise cancellation "runs on-device: your audio is processed locally on your machine rather than sent to a server" — [Krisp blog](https://krisp.ai/blog/remove-background-noise/).
  - Krisp help-center search excerpts (page itself blocked to fetch): audio data "is not sent to or stored on clouds or servers", but "we store analytical events to monitor and improve your experience" — [Krisp help: What data Krisp sends to the cloud?](https://help.krisp.ai/hc/en-us/articles/360012035500-What-data-Krisp-sends-to-the-cloud); "All audio processing happens on-device, with no audio sent to external servers" — [Krisp help: AI Noise Cancellation](https://help.krisp.ai/hc/en-us/articles/28299368036124-Krisp-AI-Noise-Cancellation).
- **NVIDIA Broadcast**: an internet connection is "Required during installation", which downloads the AI models for your GPU. Effects use GPU Tensor Cores. Cloud processing of audio is not mentioned — [NVIDIA Broadcast FAQ](https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-app/faq/).
- **Samsung Audio Eraser**: on-device vs cloud processing is not stated. Requirements include "Samsung account login required"; Galaxy AI availability "may vary by region, One UI version, device model, and carrier"; and features "may be limited for minors in some regions" — [Samsung CA support](https://www.samsung.com/ca/support/mobile-devices/how-to-remove-unwanted-sound-from-videos-using-audio-eraser-on-your-galaxy/). The Korean service page also says nothing about processing location — [삼성전자서비스](https://www.samsungsvc.co.kr/solution/4036399).
- **Vrew**: Remove Noise exists in both the desktop app and the web version. Projects can be saved "to your computer or the cloud (or browser if you're on the web version)" — [Vrew 4.2.0 update](https://docs.channel.io/vrew-us/en/articles/Vrew-420-Update-3425c357).

### Inferences
- For confidential or sensitive Korean-language recordings, the documented local options are RX, Audacity + OpenVINO, Premiere's Enhance Speech, Krisp and NVIDIA Broadcast. Adobe Podcast web, Descript Studio Sound and Auphonic require uploading audio.
- Auphonic is the only vendor here that explicitly says staff/contractors may listen to uploads for algorithm work. Its opt-out is limited to business customers.

### Gaps
- Adobe Podcast (web) retention and training terms for uploaded audio were not found in fetchable official documentation.
- Apple does not state in the pages reached whether Voice Isolation, Enhance Recording or Audio Mix run fully on-device.
- Samsung does not state whether Audio Eraser processing is on-device.
- CapCut and Vrew do not state whether "Reduce noise", "Enhance voice" or "Remove Noise" run on-device or in the cloud.
- Krisp's meeting-assistant features (recording, transcription, summaries) are not documented as on-device in the sources reached. The help center could not be opened directly.

## 3. How do products implement "tidying" edits (silence trimming, filler-word removal, breath/cough removal, transcript-based editing), and what language support is documented?

### Takeaway
Transcript-based tidying is strongest in Descript, but its transcription is limited to 26 Latin-alphabet languages. Korean is not listed, and filler-word detection and Regenerate are English-only. Auphonic's filler cutting is acoustic, trained on English, German and Romance-language data. Silence trimming is broadly available: RX 12 Trim Silence (Advanced only), Auphonic Cut Silence, Descript Shorten Word Gaps and Vrew Silence Remover. Apple Voice Memos offers Skip Silence, which is playback-only.

### Cited Findings
- **Descript filler words**:
  - Detects "um," "uh," and "you know". "This feature currently detects filler words in English transcripts only."
  - Per-instance options: Delete; Delete and replace with gap; Ignore ("Strikes through the filler word in the script but removes the audio"); Remove from transcript (audio unchanged).
  - "Avoid harsh cuts" skips fillers that can't be removed "without clipping into nearby words or leaving behind an awkward cut."
  - Source: [Descript: Filler words](https://help.descript.com/script-editing/filler-words).
  - An older help-center URL surfaced in search claimed support for more languages; the current pages say English-only — [older Descript article](https://help.descript.com/hc/en-us/articles/10164806394509-Remove-filler-words) vs [Descript: Supported transcription languages](https://help.descript.com/script-editing/supported-transcription-languages).
- **Descript word gaps**:
  - Shorten Word Gaps lets users define a gap with "more than" or "between" durations, set "a new target length (e.g. 200ms)", then "Shorten" or "Shorten all" — [Descript: Shorten Word Gaps](https://help.descript.com/script-editing/shorten-word-gaps).
  - Manual gap editing uses Cmd/Ctrl+G; "adjusting word gaps on a selected range is not supported" — [Descript: Edit word gaps](https://help.descript.com/script-editing/word-gaps).
- **Descript other cleanup tools**: Remove Retakes "detects where you've re-recorded a phrase". Edit for Clarity "clean[s] up wordiness, retakes, filler, and off-topic segments" with an intensity slider and optional AI speech rewording — [Descript: Sound good with AI tools](https://help.descript.com/descript-tour/sound-good-tools).
- **Descript transcription languages**:
  - "Descript automatically transcribes audio and video in 26 languages," all Latin-alphabet. "Languages such as Chinese, Japanese, or Russian are not yet supported."
  - The list includes English, Spanish, French, German, Italian, Portuguese, Hindi (Beta), Greek (Beta) and others, but no Korean.
  - "Descript supports transcription in only one language per file."
  - Source: [Descript: Supported transcription languages](https://help.descript.com/script-editing/supported-transcription-languages).
- **Descript Regenerate** "currently supports English audio and video only" — [Descript: Regenerate overview](https://help.descript.com/script-editing/regenerate-overview). Word replacement allows "Up to 250 characters per regenerate action" — [Descript: change-meaning](https://help.descript.com/script-editing/change-meaning).
- **Auphonic cutting**:
  - Cut Silence detects silent segments, while "speech breaks, e.g. between two sentences, remain untouched."
  - Cut Fillers: "We have trained our filler word cutting algorithm to remove filler words, namely any kind of 'uhm', 'uh', 'mh', 'ähm', 'euh', 'eh', and similar with English, German, and Romance language data." It "already works quite well for many similar-sounding languages."
  - Cut Coughs covers coughs, throat-clearing and sneezes. Cut Music removes foreground music "longer than about 20 seconds."
  - Source: [Auphonic: Singletrack algorithms](https://auphonic.com/help/algorithms/singletrack.html).
- **Auphonic cut modes and transcripts**:
  - Cut modes: "Apply Cuts", "Set Cuts To Silent" and "Export Uncut Audio". The last two generate cut lists for Audacity, Audition, Reaper, EDL and other formats. Cuts are editable in the Auphonic Editor.
  - Speech recognition is offered "in over 100 languages" (Auphonic Whisper ASR or external engines).
  - Source: [Auphonic: Production settings](https://auphonic.com/help/web/production.html).
- **iZotope RX 12**:
  - Trim Silence (ADV) "removes silent sections from your audio file", for "podcasts, dialogue mixes or field recordings". Controls: Threshold, Post-roll, Silence (target length), Crossfade. It "ignores your current selection and always processes the entire audio file" — [RX 12 docs: Trim Silence](https://docs.izotope.com/rx12/en/trim-silence.html).
  - Text Navigation is "an editing navigation tool and not a transcription service". "Only American English is supported." Files must be at least 10 s and contain speech, not lyrics. It offers fuzzy word search and up to 8-speaker detection — [RX 12 docs: Text Navigation](https://docs.izotope.com/rx12/en/text-navigation.html).
  - Breath Control handles breaths and Mouth De-click handles clicks; see question 1 — [Breath Control](https://docs.izotope.com/rx12/en/breath-control.html).
- **Vrew Silence Remover**:
  - "auto-detects silences and lets you adjust them all at once". Users can shorten or remove them, set a minimum length, and apply to the whole video or chosen clips.
  - "Vrew can even detect and remove non-speech segments like applause or laughter."
  - Source: [Vrew: Silence Remover](https://vrew.ai/en/feature/auto-silence-removal).
- **Apple Voice Memos**: "Skip silence. Skip over gaps in your audio" via Playback Settings, a playback setting — [Apple: Voice Memos (Mac guide)](https://support.apple.com/guide/mac-pro-rack/apdd1444d464/mac).
- **Audacity**: the OpenVINO Whisper Transcription feature generates "a label track containing the transcription or translation" — [OpenVINO README](https://github.com/intel/openvino-plugins-ai-audacity).

### Inferences
- For Korean speech, Descript's transcript-based editing (filler removal, Regenerate) is not available per its own language list. Auphonic's filler cutter is not trained on Korean. Korean users relying on these features should expect them to be unavailable or untested. Korean fillers such as "음/어/그" are not in any vendor's documented list.
- RX's Text Navigation is navigation-only (American English). Unlike Descript, RX does not offer text-driven deletion of words.

### Gaps
- Vrew's filler-word removal, and its Korean-specific transcription and editing features, were not verified in official docs. Only blog sources describe a filler cleaner.
- Audacity's own silence-trimming effect (e.g., "Truncate Silence") was not fetched.
- Whether Auphonic's Whisper-based transcript editor supports Korean filler detection is not documented.

## 4. What processing order or workflow does each vendor recommend?

### Takeaway
iZotope publishes a "deepest damage first" repair order: clipping → stereo → clicks → hum → steady broadband noise → variable noise. It also gives module-level ordering cautions, such as De-plosive before any high-pass filter. Auphonic runs a fixed automated chain and asks users not to pre-level or gate input. Audacity advises notch-filtering hum before Noise Reduction and removing DC offset right after recording. Most consumer tools present a single toggle or slider with no ordering guidance.

### Cited Findings
- **iZotope article** "Order of Operations: Audio Repair" (Mike Metlay, Apr 8, 2021):
  - Order: clipping first ("nothing cuts deeper than clipping"; "later operations will magnify their damage"); then stereo/channel mismatches (Azimuth); then clicks/crackle; then hum (De-hum only if hum is present); then broadband noise, steady before variable, because noise modules "need to work with the cleanest possible audio."
  - Cautions: the order is a convention; for conflicting variable-noise fixes, "try both possible orderings." Spectral De-noise at high reduction can have "a dire effect on voice quality."
  - Source: [iZotope Learn](https://www.izotope.com/en/learn/order-of-audio-repair-operations.html).
- **iZotope module docs (ordering hints)**:
  - "it is recommended that De-plosive be used before applying a high-pass filter" — [De-plosive](https://docs.izotope.com/rx12/en/de-plosive.html).
  - De-reverb's Enhance Dry Signal "can also help prepare material for later de-noising" — [De-reverb](https://docs.izotope.com/rx12/en/de-reverb.html).
  - "Running Mouth De-click twice sometimes produces a better result" — [Mouth De-click](https://docs.izotope.com/rx12/en/mouth-de-click.html).
  - Leveler's clip-gain values are "destructively written to the file" if another module is applied afterwards — [Leveler](https://docs.izotope.com/rx12/en/leveler.html).
  - For buzz with harmonics above 400 Hz, "the Spectral De-noise tool is often more effective" than hum tools — [Identifying Audio Problems](https://docs.izotope.com/rx12/en/identifying-audio-problems.html).
- **iZotope Repair Assistant** builds the chain automatically after Learn. ADV users can open it in the Module Chain to edit before rendering — [Repair Assistant](https://docs.izotope.com/rx12/en/repair-assistant.html).
- **Auphonic**:
  - "Please do not use leveling or gain control before our noise reduction algorithms!" "No noise gates: we need the noise in quiet segments." "Excessive use of dynamic range compression may be problematic."
  - Keep the microphone close in reverberant rooms.
  - Filler cutting is recommended "always in combination with our Dynamic Denoiser or Speech Isolation algorithms."
  - Source: [Auphonic: Singletrack algorithms](https://auphonic.com/help/algorithms/singletrack.html).
  - "Please don't change our default values if you don't know what these parameters mean." Loudness normalization with a True Peak Limiter is the global output stage — [Auphonic: Production settings](https://auphonic.com/help/web/production.html).
- **Audacity**:
  - For mains hum or a whistle, "the use of a Notch Filter may help, which should be carried out before applying Noise Reduction."
  - For different noise types, profile and reduce the first type, then profile and reduce the next.
  - Settings are "best done by trial and error" with Preview and Residue.
  - Source: [Audacity Manual: Noise Reduction](https://manual.audacityteam.org/man/noise_reduction.html).
  - "Immediately after recording capture (or import) … this effect should be used only to remove any DC offset" — [Audacity Manual: Normalize](https://manual.audacityteam.org/man/normalize.html).
- **Adobe Premiere Pro**: Essential Sound panel → select the speech clip → "Dialogue" → "Enhance" → adjust Mix Amount — [Adobe Community announcement](https://community.adobe.com/announcements-732/now-released-enhance-speech-in-premiere-pro-313485).
- **Descript**: Studio Sound applies per file. To treat only part of a file: duplicate the section into a new composition → Flatten tracks → apply Studio Sound → replace the section. Long recordings should be split — [Descript: Studio Sound](https://help.descript.com/effects-animations-transitions/studio-sound). Room tone is disabled for clips of a file with Studio Sound enabled — [Descript: Room tone](https://help.descript.com/effects-animations-transitions/room-tone).
- **NVIDIA Broadcast**:
  - "Applying an effect twice will often result in the effect not working correctly." Disable third-party noise cancellation in apps and drivers.
  - "Studio Voice cannot be combined with microphone background noise reduction."
  - Turn on only the effects you need.
  - Source: [NVIDIA Broadcast setup guide](https://www.nvidia.com/en-us/geforce/guides/broadcast-app-setup-guide/).
- **Samsung Audio Eraser**: Gallery → open video → Edit → Audio → Audio eraser → adjust sliders or Auto → Apply → Save copy — [Samsung CA support](https://www.samsung.com/ca/support/mobile-devices/how-to-remove-unwanted-sound-from-videos-using-audio-eraser-on-your-galaxy/).

### Inferences
- Across vendors the documented logic is consistent: repair destructive damage (clipping, clicks) and stationary noise before dynamics. Avoid leveling, gates or AGC before noise reduction (Auphonic). Apply loudness normalization last as a fixed-gain step (RX Loudness Control, Auphonic's global normalization stage).
- Double noise suppression is a documented failure mode in real-time chains (NVIDIA). The same logic plausibly applies to running Voice Isolation on iPhone and then an AI enhancer, but no vendor documents that combination.

### Gaps
- iZotope's current RX 12 "process flowchart" referenced in its docs is an image and was not machine-readable. Its exact step list was not verified.
- No vendor documents a recommended order for stacking two AI enhancers (e.g., Voice Isolation, then Adobe or Descript).

## 5. What limitations or cautions does each vendor document (artifacts at high strength, music/singing, file length/size/format limits, languages)?

### Takeaway
Vendors consistently warn that aggressive settings cause artifacts or eat into speech. Examples: RX Sensitivity and Surgical mode, Audacity "musical noise", Descript Studio Sound silencing speech in very loud noise. Speech-specific AI enhancers warn against music, sound effects and singing (Adobe; Auphonic's Speech Isolation and Dynamic modes remove music or ambience). RX instead offers explicit "Music"/singing modes. File limits are documented for Adobe Podcast and Descript, and language limits for Descript, RX Text Navigation and Auphonic fillers.

### Cited Findings
- **iZotope RX 12**:
  - Dialogue Isolate's higher Sensitivity "might also introduce artifacts and reduce dialogue clarity" — [Dialogue Isolate](https://docs.izotope.com/rx12/en/dialogue-isolate.html).
  - Voice De-noise Surgical mode "can lead to musical noise artifacts", described as "chirpy" or "watery". Optimize for Dialogue "isn't meant to handle the noise found in sung vocals"; Music mode "is more transparent when applied to sung vocals" — [Voice De-noise](https://docs.izotope.com/rx12/en/voice-de-noise.html).
  - Spectral De-noise Adaptive mode "uses a significant amount of memory and computational power". Algorithms C and D are not for real-time — [Spectral De-noise](https://docs.izotope.com/rx12/en/spectral-de-noise.html).
  - De-click Sensitivity "can impact plosives" — [De-click](https://docs.izotope.com/rx12/en/de-click.html).
  - De-plosive "may not function correctly" after a high-pass filter — [De-plosive](https://docs.izotope.com/rx12/en/de-plosive.html).
  - Breath Control works best on selections "at least 3 seconds long" — [Breath Control](https://docs.izotope.com/rx12/en/breath-control.html).
  - Repair Assistant in AudioSuite needs clips "longer than 7 seconds" or it may appear to hang — [Repair Assistant](https://docs.izotope.com/rx12/en/repair-assistant.html).
  - Adaptive Dynamic mode in the De-hum plug-in "is not optimized for real time use" — [De-hum](https://docs.izotope.com/rx12/en/de-hum.html).
- **iZotope singing/music**:
  - Dialogue Isolate's docs point to Spectral De-noise for "singing voice, instrumental tracks, or full mixes" — [Dialogue Isolate](https://docs.izotope.com/rx12/en/dialogue-isolate.html).
  - The product page says Dialogue Isolate also works on "vocals for your track" (marketing) — [product page](https://www.izotope.com/products/rx-advanced).
  - Repair Assistant has a Music mode for "isolated sung vocals" — [Repair Assistant](https://docs.izotope.com/rx12/en/repair-assistant.html).
- **Adobe**:
  - Premiere Enhance Speech "won't work with music, sound effects, or ambient audio". It is not suited to extremely poor-quality audio, multiple overlapping speakers, whispers, loud background music or singing. It "requires a performant system" — [Adobe Community announcement](https://community.adobe.com/announcements-732/now-released-enhance-speech-in-premiere-pro-313485).
  - v2 is limited to 4 hours per day of processing, and limits "may change over time" — [v2 thread](https://community.adobe.com/questions-514/enhance-speech-v2-is-here-1498584).
  - Adobe help page, search excerpt only (page blocked to fetch): Free plan "Up to 500 MB", "Up to 30 minutes per file and 1 hour maximum per day". Premium: "up to 4 hours of content per day, with individual files up to 1 GB". Video: "Up to 1 GB; Up to 4K resolution; Up to 2 hours per day" — [Adobe help: Enhance Speech FAQ](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-audio/frequently-asked-questions-about-enhance-speech.html).
- **Descript**:
  - With very loud background noise, "Studio Sound may not be able to separate the speech from the noise, resulting in a silent waveform"; the fix is to reduce Intensity.
  - "Very large files (6+ hours or several GB) may be slow to process."
  - Studio Sound "only works on recorded audio, not AI-generated speech."
  - Source: [Descript: Studio Sound](https://help.descript.com/effects-animations-transitions/studio-sound).
  - Language limits are covered in question 3: English-only filler detection and Regenerate, and Latin-alphabet-only transcription — [Supported transcription languages](https://help.descript.com/script-editing/supported-transcription-languages).
- **Auphonic**:
  - Remove Noise: "custom set higher values might result in artifacts or destroy music segments!" — [Auphonic: Production settings](https://auphonic.com/help/web/production.html).
  - Dynamic Denoiser and Speech Isolation should be avoided when sound effects, ambience or jingles must be kept; Speech Isolation also removes music.
  - The Classic Denoiser needs a silent segment and can struggle with reverb. Studio Voice is beta.
  - Cut Music is "tuned for music segments longer than about 20 seconds."
  - Source: [Auphonic: Singletrack algorithms](https://auphonic.com/help/algorithms/singletrack.html).
  - The Classic model "cannot handle recordings with background music" — [Auphonic blog 2025-07-31](https://auphonic.com/blog/2025/07/31/new-auphonic-static-and-music-denoiser/).
  - If MaxLRA/MaxS/MaxM targets cannot be met, "you will receive a warning message" — [Auphonic: Production settings](https://auphonic.com/help/web/production.html).
- **Audacity**:
  - Noise Reduction "is not suitable for individual clicks and pops, or irregular background noise such as from traffic or an audience."
  - "Reducing noise usually results in some distortion." Artifacts ("musical noise", "bird song", "tinkly-bells") "can be even more objectionable than the original noise."
  - The noise profile is not retained after closing Audacity, and sample rates must match.
  - Source: [Audacity Manual: Noise Reduction](https://manual.audacityteam.org/man/noise_reduction.html).
  - Compression "necessarily means modifying its waveshape, which causes distortion" — [Audacity Manual: Compressor](https://manual.audacityteam.org/man/compressor.html).
- **Audacity 4.0 and the OpenVINO plugins**:
  - Audacity 4 "is not fully feature-compatible with the Audacity 3.x series" (LWN, search summary) — [LWN](https://lwn.net/Articles/1092439/).
  - Coverage reports Time Tracks, Mixer, VAMP/LADSPA hosting and "some audio effects" missing (search summary) — [OMG! Ubuntu](https://www.omgubuntu.co.uk/2026/09/audacity-4-released).
  - The latest OpenVINO plugin release found (v3.7.1-R4.2) is a Windows installer for Audacity 3.7.1/3.7.3; Linux requires building from source — [OpenVINO releases](https://github.com/intel/openvino-plugins-ai-audacity/releases).
- **NVIDIA Broadcast**:
  - Base requirement is RTX 2060 / Quadro RTX 3000 or higher. Studio Voice is "not recommended" while gaming, and "Not all effects can be combined" — [NVIDIA Broadcast FAQ (US)](https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-app/faq/).
  - The US FAQ lists GeForce RTX 3060 or higher for Studio Voice (fetched Oct 2026). The UK FAQ (search summary) states RTX 4080, 5070 or higher — [NVIDIA UK FAQ](https://www.nvidia.com/en-gb/geforce/broadcasting/broadcast-app/faq). PCWorld reported RTX 4080/5080 at launch (search summary) — [PCWorld](https://www.pcworld.com/article/2594753/nvidia-new-studio-voice-ai-feature-makes-your-crappy-mic-sound-pro).
- **Apple**: "Wide Spectrum is not available in phone calls." Voice Isolation in recording apps needs iOS 26 or later — [Apple Support 101993](https://support.apple.com/en-us/101993).
- **Samsung**: "Accuracy of results is not guaranteed." Sound detection "may vary depending on audio source and the condition of the video." Supported models are S and Z series only — [Samsung CA support](https://www.samsung.com/ca/support/mobile-devices/how-to-remove-unwanted-sound-from-videos-using-audio-eraser-on-your-galaxy/). Menus and paths "may vary by model/software/app version" — [삼성전자서비스](https://www.samsungsvc.co.kr/solution/4036399).
- **CapCut** (third-party guide, not official; attributed via search-result summary): CapCut "usually works best on mild, steady background noise" and is weaker on wind bursts, room echo, clipped audio, overlapping voices and music under speech — [SimpleClean guide](https://simpleclean.app/blog/remove-background-noise-in-capcut-2).

### Inferences
- Speech-only AI enhancers (Adobe, Descript Studio Sound, Auphonic Speech Isolation) are documented or implied to suppress music, laughter or ambience. They are poor choices for singing, or for content where room ambience is wanted, unless strength or mix is reduced. RX and Auphonic's Static Denoiser are the documented options for keeping music or ambience.
- The NVIDIA Studio Voice requirement appears to have been relaxed over time: RTX 4080/5080 at launch, RTX 3060+ in the current US FAQ. Regional FAQ pages may be stale.

### Gaps
- No official documentation was found for CapCut file-length limits, artifacts, or music/singing guidance.
- Apple and Samsung document no file-length limits for Enhance Recording or Audio Eraser.
- Whether the Intel OpenVINO plugins work with Audacity 4.x is not documented in the sources reached.

## 6. Free vs paid availability (high level) and current versions/dates

### Takeaway
Fully free: Audacity and the OpenVINO plugins (open source), Apple's built-in features, and Krisp's basic noise cancellation (per Krisp). Freemium or metered: Adobe Podcast (Free vs Premium daily limits), Descript (AI Credits) and Auphonic (speech recognition only for paying users). Paid tiers: iZotope RX (Elements/Standard/Advanced). Samsung Galaxy AI was promised free through end-2025; current status is unverified.

### Cited Findings
- **iZotope RX 12**: sold as Elements, Standard and Advanced editions, with module availability gated by edition (e.g., Trim Silence and Leveler ADV-only) — [RX 12 docs: Module List](https://docs.izotope.com/rx12/en/module-list.html); [iZotope blog](https://www.izotope.com/community/blog/rx-12).
- **Adobe Podcast**: Free and Premium plans with per-file and daily limits (search excerpt of the Adobe help page) — [Adobe help: Enhance Speech FAQ](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-audio/frequently-asked-questions-about-enhance-speech.html).
- **Descript**: "On current plans, this feature uses AI Credits." This applies to Studio Sound, filler-word removal and Shorten Word Gaps — [Descript: Studio Sound](https://help.descript.com/effects-animations-transitions/studio-sound); [Descript: Filler words](https://help.descript.com/script-editing/filler-words); [Descript: Shorten Word Gaps](https://help.descript.com/script-editing/shorten-word-gaps).
- **Auphonic**: "IMPORTANT: Speech Recognition is only available for paying users!" — [Auphonic: Production settings](https://auphonic.com/help/web/production.html). "Re-processing is free as long as the input file is unchanged" (paraphrase from the fetch summary) — [Auphonic blog 2025-07-31](https://auphonic.com/blog/2025/07/31/new-auphonic-static-and-music-denoiser/).
- **Audacity versions**: the official changelog lists 4.0.1 as "Current" (30 Sept 2026), 4.0.0 (3 Sept 2026) and the last 3.x release, 3.7.9 (1 Sept 2026) — [Audacity changelog](https://www.audacityteam.org/changelog/). Audacity 4 is free and open source, with official builds distributed via MuseHub (search summary) — [MusicRadar](https://www.musicradar.com/music-tech/audacity-enters-a-new-era-with-the-biggest-update-in-the-free-and-open-source-audio-editors-25-year-history); [MuseHub: Audacity](https://www.musehub.com/de-de/app/audacity).
- **OpenVINO plugins**: GPL v3 licensed — [OpenVINO README](https://github.com/intel/openvino-plugins-ai-audacity). The latest release shown is v3.7.1-R4.2 (Dec 20; year not displayed). It adds Audio Super Resolution and OpenVINO 2024.6.0, and is compatible with Audacity 3.7.1 and 3.7.3 — [OpenVINO releases](https://github.com/intel/openvino-plugins-ai-audacity/releases).
- **Krisp**: "noise cancellation is the free part. Krisp's meeting-assistant features (recording, transcription, and summaries) sit behind a paid plan after a short trial" — [Krisp blog](https://krisp.ai/blog/remove-background-noise/).
- **NVIDIA Broadcast**: requires an NVIDIA RTX-class GPU and driver 572.61 or newer on Windows — [NVIDIA Broadcast FAQ](https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-app/faq/).
- **Apple OS requirements**: Voice Isolation needs iOS 15 (FaceTime), iOS 16.4 (phone calls) or iOS 26 (recording apps such as Voice Memos). Automatic Mic Mode needs iOS 18. iOS 26.1 adds input gain adjustment for supported wired mics — [Apple Support 101993](https://support.apple.com/en-us/101993).
- **Samsung**: Galaxy AI features "will be provided for free until the end of 2025" (statement on the Samsung CA page) — [Samsung CA support](https://www.samsung.com/ca/support/mobile-devices/how-to-remove-unwanted-sound-from-videos-using-audio-eraser-on-your-galaxy/).
- **Adobe and Premiere dates**: Premiere Enhance Speech beta was announced Sept 13, 2023 — [Adobe Community](https://community.adobe.com/announcements-732/now-released-enhance-speech-in-premiere-pro-313485). Enhance Speech v2 was announced Nov 20, 2024 — [Adobe Community](https://community.adobe.com/questions-514/enhance-speech-v2-is-here-1498584).
- **Auphonic date**: the new Static Denoiser arrived July 31, 2025 — [Auphonic blog](https://auphonic.com/blog/2025/07/31/new-auphonic-static-and-music-denoiser/).
- **Vrew**: release 4.2.0 brought Remove Noise to the web (page undated). AI Proofread costs "1 credit / 100 characters" — [Vrew 4.2.0 update](https://docs.channel.io/vrew-us/en/articles/Vrew-420-Update-3425c357).

### Inferences
- The OpenVINO v3.7.1-R4.2 release is most likely from December 2024. It bundles OpenVINO 2024.6.0, and Audacity 3.7.1 shipped on 12 Dec 2024 per the changelog. No newer plugin build for Audacity 3.7.9 or 4.x was seen, so the plugins appear to lag current Audacity.
- Because Audacity 4.0 dropped some 3.x features and effects, a Korean user following a "Audacity Noise Reduction" tutorial on 4.0.x should check that the effect still exists. The 3.x manual pages cited here may not reflect 4.x UI changes.

### Gaps
- Current Galaxy AI pricing after 2025, and Audio Eraser's free/paid status in Korea in 2026, were not verified.
- Free-tier quotas for Auphonic (monthly free hours) and Descript (credit amounts) were not verified in the sources fetched.
- CapCut's free vs Pro gating for Enhance voice and Reduce noise, and Vrew's credit usage for Remove Noise, are not documented in the sources reached.
- NVIDIA Broadcast and Krisp version numbers as of Oct 2026 were not found.
