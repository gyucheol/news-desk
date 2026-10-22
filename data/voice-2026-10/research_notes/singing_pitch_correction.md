# Singing-Voice Pitch & Timing Correction (음정 보정 / "튠"): How the Tools Work, How They're Used, and Where They Fail (state as of Oct 2026)

*How the sources were checked: most claims come from pages I opened and read in full (patents, vendor manuals and help pages, Apple's guide, Sound On Sound articles, and paper PDFs/abstracts). A few claims rest only on search-result summaries because the page was blocked or not opened. Those are tagged **[search summary]**, and the report writer should treat them with more caution.*

---

## 1. How automatic pitch correction (Antares Auto-Tune) works: detection, key/scale mapping, Retune Speed, Humanize, Flex-Tune, and the hard-tuned "Auto-Tune effect"

### Takeaway
Auto-Tune's automatic mode is a continuous real-time loop with three steps:
1. Measure the period (pitch) of a monophonic voice using an efficient autocorrelation-type test.
2. Choose the nearest allowed note from a user-defined key/scale, or take a MIDI note.
3. Re-pitch the audio toward that target at a user-set speed.

The robotic "Auto-Tune / Cher effect" is this same loop with the speed set to instantaneous (Retune Speed 0, Flex-Tune and Humanize off). Antares itself calls the result "pitch quantization": glides and vibrato are stripped out, and note changes become instant steps.

### Cited Findings

#### The original patent (US 5,973,252)
- **Bibliographic data.** Title: "Pitch detection and intonation correction apparatus and method". Inventor: Harold A. ("Andy") Hildebrand. Original assignee: Auburn Audio Technologies; current assignee listed as Antares Audio Technologies. Filed 15 Oct 1998, with priority to a provisional filed 27 Oct 1997. Granted 26 Oct 1999. — [Google Patents US5973252A](https://patents.google.com/patent/US5973252A/en)
- **Pitch detection.** Pitch is found by determining the waveform's period of repetition with autocorrelation at lag L. To make this cheap, the patent keeps two running sums, "E" and "H", and updates them sample by sample: each update adds the newest term and subtracts the term from 2L samples earlier. A period is declared because "E_i(L) is nearly equal to 2H_i(L) only at values of L that are periods of repetition of the data". The test is E_i(L) − 2H_i(L) ≤ eps·E_i(L). — [Google Patents US5973252A](https://patents.google.com/patent/US5973252A/en)
- **Search range.** In detection mode the signal is downsampled by 8 and lags 2–110 are searched. The patent says this covers about 50.1 Hz–2756 Hz at 44.1 kHz input. A separate check on the full-rate data tests for a missing fundamental, i.e. a harmonic mistaken for the fundamental. Once pitch is locked, "correction mode" tracks it by evaluating only a small range of lags around the detected period. — [Google Patents US5973252A](https://patents.google.com/patent/US5973252A/en)
- **Choosing the target.**
  - Scale mode: "a first method determines the desired period as being the period of a note from a musical scale that is closest to the input period".
  - MIDI mode: the currently sounding MIDI note is the target, and pitch bend can modify it.
  — [Google Patents US5973252A](https://patents.google.com/patent/US5973252A/en)
- **Applying the correction.** The output is resampled at the ratio of detected period to desired period. To keep the output pointer from running ahead of or behind the input, "exactly one cycle period will be subtracted from the output pointer" when raising pitch, which repeats a cycle. When lowering pitch, one cycle is added, which drops a cycle. — [Google Patents US5973252A](https://patents.google.com/patent/US5973252A/en)
- **Speed control.** In the patent the speed control is called "Decay", a user value from 0 to 1. At 0, pitch changes are instantaneous, and "A value close to one causes a lot of smoothing, making pitch changes gradual." The patent also describes user-set vibrato depth, rate and onset delay. — [Google Patents US5973252A](https://patents.google.com/patent/US5973252A/en)
- **Inventor background.** An AAPG Explorer profile (1 Nov 2012) says Hildebrand had "a stint with Exxon", co-founded the seismic-interpretation software firm Landmark Graphics, and in the 1990s applied his knowledge of autocorrelation, DSP and seismic deconvolution to music, which led to Antares and Auto-Tune. — [AAPG Explorer](https://www.aapg.org/news-and-media/details/explorer/articleid/2104/from-rocks-to-rock-his-ideas-sound-good)

#### How Antares documents the controls
Source for this group: Antares' Auto-Tune Realtime Advanced manual, hosted by Universal Audio. The control names match Auto-Tune Pro.
- **Core principle.** "Auto-Tune works by continuously tracking the pitch of an input sound and comparing it to a user-defined scale. The scale tone closest to the input is continuously identified. If the input pitch exactly matches the scale tone, no correction is applied. If the input pitch varies from the desired scale tone, Auto-Tune will adjust the pitch toward the target scale tone." — [Auto-Tune Realtime Advanced manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Key / Scale.** Together these define the set of target notes. A Chromatic scale makes it "always tune to the closest pitch in the 12-tone chromatic scale", and an Auto-Key option exists. — [manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Input Type.** Choices are Soprano, Alto/Tenor, Low Male and Instrument: "For more accurate pitch detection and correction, choose the Input Type that best describes your audio." — [manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Tracking.** Auto-Tune "requires a periodically repeating waveform, characteristic of a solo voice or solo, non-chordal instrument". Tracking sets how much waveform variation is still accepted as periodic. The default is 50. Noisy or very breathy vocals may need a higher ("relaxed") value; clicks or pops call for a lower ("choosier") value. — [manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Retune Speed.** "controls how rapidly the pitch correction is applied to the incoming audio. The units are milliseconds. A zero setting will cause immediate changes from one pitch to another, and will completely suppress any vibrato or deviations in pitch." Also: "A setting between 10 and 50 is typical for more natural sounding pitch correction. Larger values allow through more vibrato and other interpretive pitch gestures, but slow down how rapidly corrections are made." — [manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Flex-Tune.** At 0, Auto-Tune "is always pulling every note toward a target scale note". When engaged, "it only applies correction as the performer approaches the target note". Higher values make "the correction area around the scale note" smaller, so "more expressive pitch variation is allowed through". In the manual's tutorial, a setting of 10 leaves the correction range "still quite wide", while 55 makes it narrow, so a sweep is tuned only briefly near each scale note. — [manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Humanize.** It exists because short notes need a fast Retune Speed, but that speed "can cause sustained notes to sound unnaturally static". "Humanize applies a slower Retune Speed only during the sustained portion of longer notes." Recommended workflow: start Humanize at 0, set Retune Speed until the shortest problem notes are in tune, then raise Humanize if sustained notes sound static. — [manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Vibrato controls.**
  - Natural Vibrato increases or reduces vibrato already present in the audio; separate Create Vibrato controls synthesize new vibrato.
  - "Targeting Ignores Vibrato" helps Auto-Tune pick the right target when vibrato is so wide it approaches adjacent notes. In the manual's demo (a wide-vibrato male "G"), without this option Auto-Tune moves the input toward G# or F# whenever it thinks those are the target.
  — [manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Formants and Classic Mode.** The manual defines formants as "the resonant frequencies that result from the physical structure of whatever is producing the sound (e.g. the human mouth and vocal tract)". It notes that features such as "Formant Correction, Throat Modeling, and Flex-Tune" were added over the versions and changed the algorithm's sound. "Classic Mode" brings back the "Auto-Tune 5 sound": slightly brighter, with "a more pronounced attack and transition between notes at faster Retune Speeds". — [manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)

#### The hard-tuned "Auto-Tune effect" and its history
- **Antares' own definition.** The effect "is what is technically known as 'pitch quantization.' Instead of allowing all of the small variations in pitch and the gradual transitions between notes that are a normal part of singing, the Auto-Tune Effect limits each note to its exact target pitch, stripping out any variation, and forcing instantaneous transitions between notes."
  - The recipe: Flex-Tune 0, Retune Speed 0, and the right scale.
  - Removing scale notes gives a more dramatic effect on note transitions.
  - A Retune Speed of 2–3 gives "slightly less instant note transitions".
  - The manual says the effect was "First heard on Cher's 1998 hit song 'Believe'".
  — [manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Antares' Auto-Tune Pro guide (21 Feb 2020).** Settings: Retune Speed 0, Flex-Tune off, Humanize off, Natural Vibrato at 0, scale set to the song's key, Input Type matched to the voice. In Graph Mode, the separate retune control also goes to 0. The guide says "you'll hear it the most during transitions between notes" and suggests exaggerated transitions. It cites Kanye West's *808s & Heartbreak* / "Love Lockdown". — [Antares blog](https://www.antarestech.com/blog/auto-tune-effect-using-auto-tune)
- **Sound On Sound (Mike Thornton, Dec 2011).** "The 'retune' speed has to be set to zero, as it is the crucial part of creating the 'robotic' sound." Singers naturally modulate pitch as they reach a note, and "with the retune speed right down, the pitch-correction software pulls the note in right from the start". A Chromatic scale makes the effect much less noticeable. Auto-Tune EFX's "Hard EFX" setting is the "Cher effect". — [Sound On Sound](https://www.soundonsound.com/techniques/pitch-correction-plug-ins)
- **Sound On Sound "Recording Cher's 'Believe'" (Sue Sillitoe, Feb 1999), with a later "Historical Footnote" by Matt Bell.**
  - The footnote says "Believe" (December 1998) "was the first commercial recording to feature the audible side-effects of Antares Auto‑Tune software used as a deliberate creative effect".
  - It says the "tonal mangling occurs when the pitch correction speed is set too fast for the audio that it is processing".
  - It says the producers were "so keen to maintain their 'trade secret' process" that they credited the then-new Digitech Talker vocoder pedal. The original 1999 article text kept that vocoder story.
  — [Sound On Sound](https://www.soundonsound.com/techniques/recording-cher-believe)

#### Recent product status (2024–2026)
- **Auto-Tune Pro 11 (MusicTech, 16 Apr 2024).**
  - A new Harmony Player with "four individual harmonies that can be mixed and MIDI-triggered".
  - Auto Mode for real-time correction.
  - Graph Mode with per-note retune speed, vibrato and formant.
  - Updated ARA2 support (Logic, Studio One, Cubase/Nuendo), Smart MIDI mapping and Multi-View.
  - Price: $459 at Plugin Boutique.
  - The article makes no AI or machine-learning claims.
  — [MusicTech](https://musictech.com/news/gear/antares-auto-tune-pro-11/)
- Release dated 12 Apr 2024 by another outlet. **[search summary]** — [Sonicstate](https://www.sonicstate.com/news/2024/04/12/antares-releases-auto-tune-pro-11)

### Inferences
- **(Inference) The patent's detection test is a squared-difference test.** E_i(L) behaves as an energy sum over 2L samples and H_i(L) as a lag-L cross-product sum. In that case E − 2H equals Σ(x_j − x_{j−L})², the squared difference between the signal and a copy delayed by one candidate period. This is the same quantity YIN later formalized as its "difference function" (see Q3). Auto-Tune's "autocorrelation" detector is therefore close kin to YIN, with a normalized threshold (eps·E) in place of YIN's cumulative-mean normalization. This is my algebraic reading of the patent summary; it is not stated in the patent text I saw.
- **(Inference) Lineage of the controls.** The patent's 0–1 "Decay" smoothing is the conceptual ancestor of the product's Retune Speed (milliseconds). Humanize and Flex-Tune are later refinements that make the smoothing depend on note duration (Humanize) or on distance from the target (Flex-Tune).
- **(Inference) The patent's correction moves formants slightly.** Resampling each cycle by the period ratio would move formants by the same small ratio: about 2.9% for a 50-cent correction and about 5.9% for 100 cents. That is acceptable for small fixes but not for large shifts. This is consistent with Antares later adding "Formant Correction" and "Throat Modeling" (manual).
- **(Inference) Why the hard-tuned sound is robotic.** Natural singing contains continuous glides, scoops, drift and vibrato. At Retune Speed 0 the output pitch becomes a step function between scale notes, so the steps are most audible at note transitions. This matches Antares' "pitch quantization" description and its "hear it the most during transitions" remark.

### Gaps
- Auto-Tune's first commercial release date (often given as 1997) could not be confirmed from a primary source in this session. The verified anchor is the patent's 27 Oct 1997 provisional priority date.
- How current Auto-Tune versions (Pro 11) detect and shift pitch internally is not publicly documented. It is unknown whether they still use the 1998 patent's method; Flex-Tune, Humanize and formant/throat modeling are documented only by their behavior.
- The numeric ranges come from the Realtime Advanced manual and may differ slightly in Auto-Tune Pro's interface.

---

## 2. Graphical / offline note-based editing: Melodyne, Auto-Tune Graph Mode, Logic Pro Flex Pitch, Waves Tune, Synchro Arts RePitch/VocAlign, and free tools

### Takeaway
Graphical editors first analyze a whole take. They split it into note objects ("blobs" in Melodyne, piano-roll notes in Logic, Note/Curve/Line objects in Auto-Tune Graph Mode) and split each note's pitch into separately editable layers:
- **pitch center:** the note's perceived average pitch;
- **slow drift:** gradual, usually unintentional wandering;
- **fast modulation/vibrato:** rapid, usually intentional variation;
- plus timing, length, level and formants.

This lets an engineer move a note to the right pitch while keeping its vibrato and expression. Automatic real-time correction can only approximate that with speed and flex controls.

### Cited Findings

#### Celemony Melodyne (current major version: Melodyne 5)
- **Note model.** "In Melodyne, notes are represented by blobs." Melodyne's analysis recognizes "notes, scales, keys, chords, timing, tempo, and tone color". Users can edit "the pitch, vibrato, volume, sibilants, length, timing and formants of each note".
  - It runs via ARA, as a plug-in, or standalone.
  - Editions: studio, assistant, editor, essential. The editor edition includes "the legendary DNA algorithm for polyphonic audio".
  — [Celemony: What is Melodyne](https://www.celemony.com/en/melodyne/what-is-melodyne)
- **Pitch modulation vs. pitch drift.** "The term 'pitch modulation' covers rapid and usually intentional variations in pitch such as trills or vibrato." "'Pitch drift' is our term for slow fluctuations in pitch."
  - The Modulation and Drift tools are dragged vertically to scale the curve.
  - In the inspector, "100% represents in this case the original modulation or drift, 0% a straight line"; −100% inverts it.
  — [Celemony Help: Pitch modulation and drift](https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_ToolModulationDrift_2)
- **Correct Pitch macro.**
  - Pitch center is "the same parameter that is modified when pitch correction is performed manually using the Pitch Tool".
  - The upper slider runs 0–100%. Low settings affect only notes far off pitch, and "at 100% all the selected notes are exactly in tune".
  - Notes snap to the nearest semitone by default. "Snap to Chord Scale" instead snaps to the nearest scale degree or chord tone.
  - The lower "Correct Pitch Drift" slider reduces slow wavering, while "More rapid fluctuations in pitch, such as pitch modulation or vibrato, remain unaffected."
  — [Celemony Help: Correct Pitch Macro](https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_MacroPitch?env=dawsWithAra)
- **Sibilant handling.** With the Melodic algorithm, Melodyne marks sibilants (fricatives, some word fragments, breaths). They move on screen with the macro, but "acoustically they remain unaltered". Altering their frequency "would sound unnatural". — [Celemony Help: Correct Pitch Macro](https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_MacroPitch?env=dawsWithAra)
- **Sound On Sound review of Melodyne 5 (Sam Inglis, July 2020).**
  - "If there is pitch variation in the course of a sustained note, Melodyne defines its pitch centre as an average value", so snapping a whole note may not put every part of it in tune. Melodyne 5 adds a "musically weighted algorithm to calculate pitch centres".
  - Practical tip: "Chop it into smaller pieces and quantise each of these separately".
  - The Melodic algorithm "automatically splits out sections of an otherwise pitched source that contain mainly noise", and pitch, formant and time edits "apply only to the pitched element of the note". You cannot force Melodyne to reclassify what counts as pitched or sibilant.
  - Melodyne 5's Leveling macro "doesn't also pull up noise and unwanted sounds such as breaths".
  — [Sound On Sound](https://www.soundonsound.com/reviews/celemony-melodyne-5)
- **Automatic formant correction.** When notes are transposed, formants "are automatically corrected to avoid, in the case of vocals, the dreaded 'Mickey Mouse' effect". For example, after a whole-tone transposition up, formants are shifted back down a tone.
  - Separate Formants Up/Down sliders set how much of this correction applies.
  - A "Formant Character" slider changes the weighting of the shifted formants.
  - For vocals, "Sibilant Handling is without question ideal". Use "Tonal (high)" for very high voices and a robust pitch curve for deep, throaty (often male rock) singers.
  — [Celemony Help: Algorithm Inspector](https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_NA_Mode_2?env=standAlone)
- **Formant Tool.** Dragging a note shifts its formants independently of pitch, in cents (from a few cents to several thousand), with adjustable formant transitions between adjacent notes. **[search summary]** — [Celemony Help: Formant Tool](https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_ToolFormants?env=standAlone)
- **DNA (Direct Note Access, polyphonic).**
  - Shown at Musikmesse 2008 and released in Melodyne editor 1.0 in November 2009. Celemony calls it the first note-based editing of polyphonic audio; that is a vendor claim. **[search summary]** — [Sonicstate, 2019](https://www.sonicstate.com/news/2019/11/21/10-years-of-melodyne-with-dna/)
  - Sound On Sound's review (Mike Senior, Dec 2009): Melodyne "needs a precise map of all the notes in a given chord". Detection is "pretty good, but it's not infallible". A Note Assignment mode grades each detection by probability. — [Sound On Sound](https://www.soundonsound.com/reviews/celemony-melodyne-dna-editor)
- **Version status.** Celemony's help center still documents Melodyne 5. The Melodyne 5 editor manual is listed as "Last updated on 10/15/2026". I found no announcement of a Melodyne 6. **[search summary]** — [Celemony Help Center PDF](https://helpcenter.celemony.com/M5/pdf/melodyneEditor5/en?env=live)

#### Antares Auto-Tune Graph Mode
- **Workflow (Antares, 16 Oct 2022, Auto-Tune Pro X).**
  - The user first presses Track Pitch (or Track Pitch + Time) and plays the audio; tracking stops when playback stops.
  - Correction objects (Notes, Curves, Lines) are then auto-created or drawn. Create Notes / Create Curves generate them from the tracked audio.
  - "Per Object Control" gives individual notes or phrases their own Retune Speed, Vibrato and Formant settings.
  - Time Correction tools (Point or Region) adjust timing.
  - "Auto Mode applies the same settings to an entire track", whereas Graph Mode edits individual notes and phrases.
  — [Antares blog](https://www.antarestech.com/blog/understanding-graph-mode-in-auto-tune-pro-x)
- **Hard tuning in graphical mode (Auto-Tune 7 era).** Set "Default Notes Retune Speed" to 0 and "Make sure that all of the Note objects butt up against each other". — [Sound On Sound, 2011](https://www.soundonsound.com/techniques/pitch-correction-plug-ins)

#### Apple Logic Pro Flex Pitch
- **Note view.** Sections of audio identified as notes are "displayed like notes in the Piano Roll Editor". The user can edit pitch, time position and length, and can cut and merge notes. — [Apple: Edit pitch and timing with Flex Pitch](https://support.apple.com/guide/logicpro/edit-pitch-and-timing-with-flex-pitch-lgcpc53e6bef/mac)
- **Note hotspots.**
  - Upper-left: pitch drift at note start. Upper-mid: vibrato. Upper-right: pitch drift at note end.
  - Lower-left: gain. Lower-mid: fine pitch. Lower-right: formant shift.
  - The Audio Track Editor also has dedicated Vibrato and Volume tools.
  — [Apple: Edit pitch and timing with Flex Pitch](https://support.apple.com/guide/logicpro/edit-pitch-and-timing-with-flex-pitch-lgcpc53e6bef/mac)
- **Algorithm parameters.**
  - "Formant Track: Determines the interval at which formants are transposed along with the pitch."
  - "Formant Shift: Determines how formants adjust to pitch shifts. When set to 0, formants are adjusted together with pitch shifts."
  - Formants menu: "Process always", or "Keep Unvoiced Formants: Only voiced formants are processed. Sibilant and plosive sounds are retained, producing a more natural-sounding effect."
  - Turning on Flex Pitch deactivates destructive editing in the Audio File Editor.
  — [Apple: Flex Pitch algorithm and parameters](https://support.apple.com/guide/logicpro/flex-pitch-algorithm-and-parameters-lgcpba8e3301/mac)
- **Scope.** Tutorials describe Flex Pitch as meant for monophonic material (vocals, bass, lead lines), not chords or mixes. **[search summary]** — [SoundGirls](https://soundgirls.org/an-introduction-to-flexpitch-in-logic-pro-x/)

#### Waves Tune
- **Waves' description.**
  - "Surgical vocal pitch correction" with "formant-corrected pitch shifts".
  - Conforms notes to "43 scales, or a custom scale".
  - Notes can be sliced and merged, and pitch curves edited with Pencil, Curve and Line tools.
  - Users can "Choose correction speed, transition time, and amount".
  - Natural vibrato can be kept, reduced or flattened, or new vibrato synthesized.
  - Waves Tune is listed as "Offline" with a 10-minute processing limit. Waves Tune Real-Time is the separate live product.
  - "Works for guitar and monophonic instruments in a vocal's range."
  — [Waves](https://www.waves.com/plugins/waves-tune)

#### Synchro Arts RePitch (and VocAlign; see also Q4)
- **RePitch (launched 2022). [search summary]**
  - Edits pitch, timing, vibrato, formants and sibilance.
  - Identifies notes "based on human pitch perception".
  - Processes pitched and non-pitched note sections separately (consonants, breaths).
  - Suggests the most likely scale; supports ARA2.
  - A "SynchroLink" sends pitch and timing edits to VocAlign Ultra for double tracks. A RePitch 2 edition exists.
  — [Sonicstate 2022](https://sonicstate.com/news/2022/09/20/natural-vocal-pitch-editing-plug-in); [Best Service](https://www.bestservice.com/repitch.html); [Thomann (RePitch 2)](https://www.thomann.co.uk/synchro_arts_repitch_2_standard_crossgrade.htm)

#### Free tools (Sound On Sound, Luke Wood, Feb 2025)
- **Graillon 3 (Auburn Sounds).** A "pitch‑ and formant‑shifting plug‑in that's capable of both natural‑sounding correction and more extreme creative effects". It is free to download; a paid Full Edition adds non-standard tunings and a vocal doubler. It has three pitch engines: G2 keeps the predecessor's sound, and I1 "offers more natural‑sounding correction on complex source material". — [Sound On Sound](https://www.soundonsound.com/reviews/creative-pitch-correction-plug-ins)
- **MAutoPitch (MeldaProduction).** Part of the free MFreeFXBundle. "Incoming monophonic audio signals can be locked to chromatic, major, minor and pentatonic scales", with formant-shift and stereo-width processors in an Effects section. Paid upgrades add features such as oversampling. — [Sound On Sound](https://www.soundonsound.com/reviews/creative-pitch-correction-plug-ins)

### Inferences
- **(Inference) Real-time vs. offline is the key split.** Auto Mode (Auto-Tune, Waves Tune Real-Time, Graillon, MAutoPitch) must decide the target note causally with low latency. It can only trade correction speed against naturalness through global knobs (Retune Speed, Flex-Tune, Humanize).
  - Offline or graphical editors (Melodyne, Graph Mode, Flex Pitch, Waves Tune, RePitch) see the whole note before deciding. That lets them compute a note's pitch center and separate drift from vibrato, so the center can be moved without flattening expression.
- **(Inference) Shared design across vendors.** Melodyne, Logic and RePitch all treat unvoiced, noise-like parts (sibilants, plosives, breaths) as untouchable by pitch processing. All major editors handle formants separately from pitch, by automatic correction or a dedicated control. This is the main design difference from a naive pitch shifter.

### Gaps
- Melodyne's note-detection and DNA source-separation methods are proprietary and unpublished; vendor patents were not researched.
- RePitch and VocAlign feature details rest partly on reseller and press summaries, not Synchro Arts' own RePitch documentation.
- Whether Graillon's I1 engine is free or paid-only was not verified from Auburn Sounds' site.
- Quality comparisons between tools are subjective; I found no independent, controlled listening test of commercial tuners.

---

## 3. Underlying signal processing: pitch detection (autocorrelation, YIN, pYIN, CREPE), pitch shifting (TD-PSOLA, phase vocoder), and formant preservation ("chipmunk" timbre)

### Takeaway
Every tuner has two halves:
1. **An f0 (fundamental-frequency) tracker.** The lineage is autocorrelation, then difference-function methods (Auto-Tune's patent, YIN 2002), then probabilistic/HMM smoothing (pYIN 2014), then neural networks (CREPE 2018).
2. **A re-pitcher.** Options are time-domain pitch-synchronous overlap-add (TD-PSOLA, 1990), frequency-domain phase-vocoder methods (e.g., Laroche & Dolson 1999), or resampling.

Plain resampling scales the whole spectrum, so the vocal-tract resonances (formants) move with the pitch. That is the "chipmunk" / "Mickey Mouse" timbre. Formant-preserving methods keep the spectral envelope fixed: implicitly (PSOLA), by estimating and re-imposing it (phase vocoder + envelope estimation), or by explicit formant correction.

### Cited Findings

#### Pitch (f0) detection
- **YIN (de Cheveigné & Kawahara, JASA 111(4):1917–1930, 2002).** Abstract:
  - "It is based on the well-known autocorrelation method with a number of modifications that combine to prevent errors."
  - "Error rates are about three times lower than the best competing methods, as evaluated over a database of speech recorded together with a laryngograph signal."
  - "There is no upper limit on the frequency search range, so the algorithm is suited for high-pitched voices and music."
  - It can be implemented "efficiently and with low latency" with few parameters.
  — [YIN paper (PDF)](https://cagnazzo.wp.imt.fr/files/2013/05/2002_JASA_YIN.pdf)
- **YIN's six steps and their measured gross error rates** (Table I; 25 ms window, 40–800 Hz search, threshold 0.1):

  | Step | Gross error |
  |---|---|
  | 1. Unbiased autocorrelation | 10.0% |
  | 2. Difference function | 1.95% |
  | 3. Cumulative-mean-normalized difference | 1.69% |
  | 4. Absolute threshold | 0.78% |
  | 5. Parabolic interpolation | 0.77% |
  | 6. Best local estimate | 0.50% |

  A "gross error" is an estimate more than 20% away from the laryngograph reference. — [YIN paper (PDF)](https://cagnazzo.wp.imt.fr/files/2013/05/2002_JASA_YIN.pdf)
- **Octave errors.** The paper explains the classic failure: a higher-order dip deeper than the true period dip produces "a subharmonic error, sometimes called 'octave error'". The absolute threshold (choose the smallest lag whose dip falls below the threshold) is the fix. — [YIN paper (PDF)](https://cagnazzo.wp.imt.fr/files/2013/05/2002_JASA_YIN.pdf)
- **YIN's limits, per librosa.** YIN "assumes that every frame has a fundamental frequency", which makes it unstable in silence. It "does not do much to enforce continuity of f0 estimates, leading to abrupt jumps". pYIN "models continuity in time by using a Markov chain" and "can estimate whether or not each frame has a fundamental frequency", returning voiced flags and probabilities. Both suit monophonic signals only. — [librosa F0 tutorial](https://librosa.org/doc/dev/auto_tutorials/01-intro/03-f0.html)
- **pYIN (Mauch & Dixon, ICASSP 2014, pp. 659–663).** Replaces YIN's single threshold with a threshold distribution, producing several f0 candidates per frame, then Viterbi-decodes an HMM to find a smooth pitch track. **[search summary]** — [QMUL repository](https://qmro.qmul.ac.uk/xmlui/handle/123456789/6040)
- **CREPE (Kim, Salamon, Li & Bello, NYU; ICASSP 2018).** A deep convolutional network operating "directly on the time-domain waveform", reported "performing equally or better than pYIN" and evaluated for noise robustness. It was released as an open-source Python module; Essentia's wrapper expects 16 kHz input. — [arXiv 1802.06182](https://arxiv.org/abs/1802.06182); [Essentia docs](https://essentia.upf.edu/reference/std_PitchCREPE.html)
- **Algorithms named in a singing-app patent.** Smule's mobile-karaoke patent lists:
  - for detection: AMDF (average magnitude difference function) and autocorrelation, combined with zero-crossing and peak picking;
  - for correction: PSOLA and LPC (linear predictive coding);
  - frequency-domain options: FFT peak picking and phase vocoding.
  It also refers to simplified autocorrelation as used in Auto-Tune-style implementations. — [Google Patents US9147385B2](https://patents.google.com/patent/US9147385B2/en)

#### Pitch shifting and formants
- **Why plain speed or sample-rate changes fail.** "speeding up or slowing down recordings … changes not only the duration but also the pitch". "over- or under-sampling alters duration, but also modifies the spectral envelope: formants become compressed/dilated". — [R. Gutierrez-Osuna, TAMU lecture L19 (PDF)](https://people.engr.tamu.edu/rgutier/lectures/sp/l19.pdf)
- **TD-PSOLA origin.** Moulines & Charpentier, "Pitch-synchronous waveform processing techniques for text-to-speech synthesis using diphones", *Speech Communication* 9(5–6):453–467 (1990). It reviews PSOLA methods for modifying prosody and concatenating speech waveforms. It contrasts FD-PSOLA (FFT-based, more spectral flexibility) with TD-PSOLA, whose time-domain approach gives "very efficient solutions for the real time implementation". **[search summary of abstract]** — [IP Paris research portal](https://researchportal.ip-paris.fr/en/publications/pitch-synchronous-waveform-processing-techniques-for-text-to-spee/); [Praat manual citation](https://www.fon.hum.uva.nl/praat/manual/Moulines___Charpentier__1990_.html)
- **How TD-PSOLA works (TAMU lecture).**
  - PSOLA modifies speech "without performing any explicit source/filter separation". The steps are "Isolate pitch periods … Perform the required modification … Resynthesize the final waveform through an overlap-add operation".
  - TD-PSOLA uses "one analysis window per pitch period", which requires epochs (pitch marks) "determined with great accuracy". It uses a Hanning window "generally extending two pitch periods".
  - Quality is "extremely high" provided epoch marking is accurate ("critical") and "Modifications do not exceed a factor of two".
  - Stretching unvoiced portions by about 2× creates a perceived "tonal" noise.
  — [TAMU L19 (PDF)](https://people.engr.tamu.edu/rgutier/lectures/sp/l19.pdf)
- **Phase vocoder (Laroche & Dolson, IEEE WASPAA 1999).** Phase-vocoder pitch shifting is "usually achieved via a combination of time-scaling and sampling rate conversion". For example, raising pitch by 2× means time-stretching by 2× and then resampling to restore the duration. A drawback is that "only linear frequency-modifications can be achieved". The paper proposes direct frequency-domain methods: "a simple peak-detection stage where prominent peaks are identified and the frequency axis divided into 'regions of influence'", whose regions are then shifted. Integer-bin shifts allow 50% overlap; fractional shifts need 75%. — [Laroche & Dolson 1999 (PDF)](https://www.ee.columbia.edu/~dpwe/papers/LaroD99-pvoc.pdf)
- **Envelope preservation.** Röbel & Rodet (IRCAM, DAFx 2005), "Efficient spectral envelope estimation and its application to pitch shifting and envelope preservation", target "pitch shifting with preservation of the spectral envelope in the phase vocoder". They select a cepstrum-based iterative "true envelope" estimator and speed it up 2.5–11×. **[search summary of abstract]** — [DAFx paper archive](https://dafx.de/paper-archive/details/EDSTSaO17Gd_0LV03iwDfw)
- **What vendors say about formants.**
  - Melodyne auto-corrects formants on transposition to avoid the "Mickey Mouse" effect. — [Celemony Help](https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_NA_Mode_2?env=standAlone)
  - Logic exposes Formant Track and Formant Shift. — [Apple](https://support.apple.com/guide/logicpro/flex-pitch-algorithm-and-parameters-lgcpba8e3301/mac)
  - Waves advertises "formant-corrected pitch shifts". — [Waves](https://www.waves.com/plugins/waves-tune)
  - Antares defines formants as resonances of "the human mouth and vocal tract". — [Antares manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Artifacts still unsolved in 2026.** A January 2026 preprint states that conventional pitch-shifting methods introduce "formant shifts and robotic coloration" that worsen with larger transposition intervals. — [arXiv 2601.10345](https://arxiv.org/abs/2601.10345)

### Inferences
- **(Inference / standard source-filter reasoning) Why PSOLA keeps formants.** A voiced sound is roughly a periodic glottal source (it sets the pitch, i.e. the harmonic spacing) filtered by the vocal tract (it sets the spectral envelope, i.e. the formants).
  - Resampling scales both together: +12 semitones doubles the formant frequencies too, which sounds like a much smaller vocal tract (chipmunk / Mickey Mouse).
  - PSOLA re-spaces short grains, each about two periods long. Each grain keeps the original local spectrum (envelope) while the new spacing sets a new harmonic spacing, so formants are approximately preserved. The TAMU lecture states the result but not this explanation.
  - Phase-vocoder methods need an explicit envelope estimate (e.g., Röbel & Rodet) to do the same.
- **(Inference) Generic pipeline shared by all the tools above:**
  1. f0 tracking and voiced/unvoiced decision;
  2. note segmentation;
  3. a target pitch curve (from a scale, MIDI, a score, or manual edits);
  4. a smoothing/expressiveness policy (retune speed, Flex-Tune, Humanize, drift vs. vibrato handling);
  5. resynthesis with formant handling, with unvoiced segments left alone.
  Detection errors at step 1 propagate into wrong target notes.
- **(Inference) Arithmetic check.** The patent's stated 50.1–2756 Hz range is consistent with 44,100/8 = 5,512.5 Hz divided by lags 110 and 2. YIN's evaluation used 40–800 Hz. The singing range is therefore well inside the search ranges of both.

### Gaps
- Which detection and shifting algorithms today's commercial products (Melodyne 5, Auto-Tune Pro 11, Waves Tune) actually use is not publicly documented. The Auto-Tune patent and the Smule patent are the only primary disclosures found.
- I did not find singing-specific benchmark numbers for YIN, pYIN or CREPE (the YIN figures are on speech).

---

## 4. Timing correction and alignment (VocAlign for doubles, Melodyne timing tools, Graph Mode, Flex Pitch)

### Takeaway
Timing correction has two forms:
- **Quantizing to a grid.** Notes are moved toward beat positions, as in Melodyne's Quantize Time or by dragging notes in Melodyne, Logic or Graph Mode.
- **Aligning to another performance.** VocAlign computes a time-warping path between a "Guide" and a "Dub" and stretches or compresses the Dub, optionally matching its pitch as well. This is the standard way to tighten doubled vocals and ADR.

The underlying operation is time-scale modification: changing duration without changing pitch.

### Cited Findings
- **VocAlign Ultra's core idea.** It aligns one performance (the Dub) to a reference (the Guide) "in the time or pitch domains, or both". — [Synchro Arts VocAlign Ultra manual](https://www.synchroarts.com/manuals/VocAlignUltraV1.1/Manual/HTML/what-is-vocalign-ultra.html)
- **VocAlign Ultra's mechanism.**
  - Both signals pass through identical spectrum analyzers that produce time-varying energy patterns and pitch maps.
  - Pattern recognition builds a "time-warping path" governed by a "Matching" tightness setting.
  - An editing processor applies variable time-stretching and compression so the Dub's energy peaks and troughs line up with the Guide's.
  — [Synchro Arts manual](https://www.synchroarts.com/manuals/VocAlignUltraV1.1/Manual/HTML/what-is-vocalign-ultra.html)
- **VocAlign Ultra's uses and tools.** Uses include syncing replacement dialogue, matching overdub intonation, lip-sync for foreign dubs and double-tracking vocals. Tools include Protected Ranges and Sync Points; version 1.1 added SmartAlign. — [Synchro Arts manual](https://www.synchroarts.com/manuals/VocAlignUltraV1.1/Manual/HTML/what-is-vocalign-ultra.html)
- **VocAlign Ultra review details. [search summary]**
  - Match Timing and Match Pitch knobs run from "Loose to Tight".
  - Formant Shift is ±20%.
  - Six "Alignment Rule" presets and a "Pitch Target" control that favors the Dub or the Guide.
  - The engine uses Revoice Pro's time compression/expansion algorithms.
  — [MusicRadar review](https://www.musicradar.com/reviews/synchro-arts-vocalign-ultra)
- **Melodyne Quantize Time macro. [search summary]**
  - Moves each note's "musical starting point" toward the beat assigned during analysis by an intensity of 0–100% (100% means exactly on the beat).
  - Can use another track's notes as the grid.
  - Edits "points of rhythmic emphasis" rather than snapping every note.
  - For notes that begin with a sibilant, places the musical start after the sibilant.
  - Double-clicking with the Time Tool quantizes to Melodyne's detected "intended" positions.
  — [Celemony Help: Quantize Time Macro](https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_MacroTiming?env=logic); [Celemony Help: Timing Tool](https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_ToolTiming_2?env=logic)
- **Auto-Tune Graph Mode timing.** Offers "Track Pitch + Time" and Time Correction tools that adjust timing by Point or Region. — [Antares blog](https://www.antarestech.com/blog/understanding-graph-mode-in-auto-tune-pro-x)
- **Logic Flex Pitch timing.** Notes can be moved horizontally and resized. Apple's guide also has a section on correcting the timing of audio regions with Flex Pitch. — [Apple: Edit pitch and timing with Flex Pitch](https://support.apple.com/guide/logicpro/edit-pitch-and-timing-with-flex-pitch-lgcpc53e6bef/mac)
- **RePitch → VocAlign.** RePitch's SynchroLink passes pitch and timing edits to VocAlign Ultra for double tracks. **[search summary]** — [Best Service](https://www.bestservice.com/repitch.html)
- **Timing edits in polyphonic mode.** In DNA polyphonic mode, the Timing tool can "all but obliterate" the transients of closely spaced notes. — [Sound On Sound, 2009](https://www.soundonsound.com/reviews/celemony-melodyne-dna-editor)

### Inferences
- **(Inference)** VocAlign's "time-warping path" from feature matching is functionally a dynamic-time-warping-style alignment. Synchro Arts does not name the algorithm in the page read.
- **(Inference)** Timing correction is separate from pitch correction but uses the same toolbox: time-scale modification (TD-PSOLA or phase-vocoder style, see Q3). Big stretches therefore risk similar artifacts, such as smeared transients and tonal noise when stretching unvoiced sound.

### Gaps
- No independent measurement of alignment accuracy or artifacts for VocAlign or Melodyne was found.
- The Melodyne timing-tool details rest on search summaries of Celemony pages.

---

## 5. AI-based developments for singing (AI pitch correction, singing-voice enhancement, singing-voice conversion), 2023–2026, only where documented

### Takeaway
Documented AI work on singing is mostly academic:
- diffusion-based pitch correction (Diff-Pitcher, WASPAA 2023);
- diffusion "restoration" of pitch-shifted vocals (2026 preprint);
- singing-voice conversion benchmarks (SVCC 2023, SVCC 2025).

Industry examples include HYBE/Supertone's AI pronunciation correction (2023) and vague "AI-powered tools" in Smule's app listing. I found no documentation that the market-leading tuners (Auto-Tune Pro 11, Melodyne 5) use neural networks for their core correction.

### Cited Findings
- **Diff-Pitcher (Jiarui Hai & Mounya Elhilali, Johns Hopkins; IEEE WASPAA 2023). [search summary]**
  - A pitch-control model combining "diffusion modeling and source-filter mechanisms".
  - Does not need paired out-of-tune/corrected training data.
  - Tested on pitch shifting and automatic pitch correction (template-based and score-based).
  - The authors claim it outperforms prior pitch-control methods in sound quality and naturalness.
  - The code is on Hugging Face, with a to-do list (checkpoints) and license not finalized when indexed.
  — [WASPAA paper (PDF)](https://engineering.jhu.edu/lcap/data/uploads/pdfs/waspaa2023_hai.pdf); [Hugging Face repo](https://huggingface.co/Higobeatz/Diff-Pitcher); [MusicRadar](https://musicradar.com/news/diff-pitcher-ai-pitch-correction)
- **Liu & Akama, "Self-supervised restoration of singing voice degraded by pitch shifting using shallow diffusion" (arXiv, 15 Jan 2026).**
  - Treats high-quality singing pitch shifting as restoration: a lightweight mel-spectrogram diffusion model conditioned on f0, volume and content.
  - Training pairs come from shifting and then un-shifting audio, which simulates artifacts while keeping ground truth.
  - Reports substantially reduced artifacts vs. "representative classical baselines".
  - It is a preprint.
  — [arXiv 2601.10345](https://arxiv.org/abs/2601.10345)
- **Pre-2023 background: "Deep Autotuner" (Wager, Tzanetakis, Wang & Kim; ICASSP 2020).**
  - Predicts note-wise pitch shifts from the relationship between singing and accompaniment spectrograms.
  - Does not snap to a score or to the nearest equal-tempered pitch, leaving room for intentional variation.
  - Trained on 4,702 amateur karaoke performances selected for good intonation.
  - **[search summary of abstract]**
  — [arXiv 2002.05511](https://arxiv.org/abs/2002.05511)
- **Singing Voice Conversion Challenge 2023 (SVCC 2023). [search summary of abstract]**
  - Two tasks: in-domain and cross-domain SVC.
  - 26 submissions including 2 baselines.
  - "human-level naturalness was achieved by the top system", but "no team was able to obtain a similarity score as high as the target speakers".
  - Cross-domain conversion was harder.
  - Few objective metrics correlated significantly with listener judgments.
  — [arXiv 2306.14422](https://arxiv.org/abs/2306.14422)
- **SVCC 2025 analysis (Violeta, Zhang, Shi, Yasuda, Huang, Wu & Toda; arXiv v1 Sep 2025, v2 28 May 2026; submitted to IEEE TASLP).**
  - The challenge added singing-style conversion; 33 systems were evaluated.
  - Top systems reached singer-identity scores "comparable" to ground truth.
  - Style conversion remains hard, mainly in capturing dynamic features of breathy, glissando and vibrato singing.
  - Naturalness lags when style is modeled.
  - Objective metrics are not yet adequate replacements for listening tests.
  — [arXiv 2509.15629](https://arxiv.org/abs/2509.15629)
- **HYBE / Supertone, MIDNATT "Masquerade" (May 2023). [search summary]**
  - Released in six languages (Korean, English, Japanese, Chinese, Spanish, Vietnamese).
  - Native speakers' readings were combined by AI with the singer's vocals to refine pronunciation and, per HYBE, intonation. Supertone's tech is built on the "NANSY" framework.
  - HYBE bought Supertone in Jan 2023 (₩45bn per Reuters; about $32m per MBW).
  - Sources differ on the exact release date.
  — [Korea Times](https://www.koreatimes.co.kr/amp/entertainment/k-pop/20230515/hybe-uses-ai-voice-technology-for-midnatts-multilingual-single); [Music Business Worldwide](https://www.musicbusinessworldwide.com/hybe-just-released-a-k-pop-track-sung-in-six-different-languages-using-ai-voice-technology); [GMA/Reuters](https://www.gmanetwork.com/news/lifestyle/hobbiesandactivities/876371/k-pop-s-biggest-music-label-hybe-looks-to-lift-language-barrier-with-ai/story/)
- **Smule's 2026 App Store listing.** Invites users to "explore optional AI‑powered tools to refine tone and range". It does not specify what they do. — [App Store: Smule](https://apps.apple.com/sg/app/smule-sing-record-karaoke/id509993510)
- **Antares.** MusicTech's Auto-Tune Pro 11 launch coverage (Apr 2024) "makes no AI or machine-learning claims". — [MusicTech](https://musictech.com/news/gear/antares-auto-tune-pro-11/)

### Inferences
- **(Inference)** AI is entering vocal tuning in three directions:
  1. better detection (CREPE-style neural f0 trackers, Q3);
  2. more natural resynthesis (diffusion or neural vocoders replacing PSOLA or phase vocoders, aimed at removing "robotic coloration");
  3. "beyond tuning" edits: changing who sings (SVC) or how they pronounce (HYBE/Supertone).
  Directions 2 and 3 blur the line between correcting a singer's performance and generating or replacing it, which matters for how the report frames "보정" (correction).
- **(Inference)** The SVCC results show that expressive singing features (breathiness, glissando, vibrato) remain the hardest part for AI. These are exactly the features that classic tuners strip out when over-applied.

### Gaps
- I found no vendor documentation that Auto-Tune Pro 11, Melodyne 5, Waves Tune or Flex Pitch use machine learning for pitch correction. Commercial "AI pitch correction" products from 2025–2026 were not identified or verified.
- Diff-Pitcher details come from summaries (the JHU news pages returned HTTP 403). Its baseline comparisons in the 2026 preprint were not verified.
- No credible source was found on AI singing-voice enhancement (denoise/dereverb) specific to singing, as distinct from speech.

---

## 6. Limitations and audible artifacts, plus vendor best-practice cautions (and the cleanup vs. tuning distinction)

### Takeaway
Tuning tools only work as well as their pitch detection. Detection assumes a dry, isolated, monophonic, periodic voice, so noise, breathiness, reverb, bleed, wide vibrato and unvoiced consonants cause wrong or missing pitch estimates.

Even with perfect detection, over-correction causes the characteristic artifacts:
- static or robotic sustained notes;
- stripped vibrato;
- instant note steps;
- note "flipping" with wide vibrato;
- formant or timbre shifts and robotic coloration on large shifts;
- smeared transients in polyphonic or timing edits.

Vendors' advice is consistent: correct only what is needed, protect consonants and breaths, preserve vibrato and drift, and replace badly missed notes with a better take rather than forcing large shifts.

### Cited Findings

#### Input requirements and detection failures
- Auto-Tune "is intended for use with a well-isolated, monophonic sound source" and "is not intended for multiples voices or instruments recorded onto the same track". "Noise content, or extreme breathiness in vocal performance can sometimes lead to tracking errors." Clicks and pops suggest the Tracking setting is wrong. — [Antares manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- Subharmonic ("octave") errors arise when a higher-order dip beats the true period. — [YIN paper](https://cagnazzo.wp.imt.fr/files/2013/05/2002_JASA_YIN.pdf)
- Auto-Tune's patent includes a missing-fundamental check against this kind of error. — [Google Patents US5973252A](https://patents.google.com/patent/US5973252A/en)
- YIN-type trackers are unstable in silent or unvoiced frames and produce abrupt jumps between notes. pYIN adds voicing decisions and continuity. — [librosa](https://librosa.org/doc/dev/auto_tutorials/01-intro/03-f0.html)
- **Wide vibrato.** Without "Targeting Ignores Vibrato", Auto-Tune pulls a wide-vibrato "G" toward G# or F# whenever it misjudges the target. — [Antares manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Reverb and echo (weak sourcing).** A Melodyne user review says recording "dry" helps analysis more than a signal with "a lot of reverb or echo", and that effects should be added after Melodyne. This is a user opinion, not vendor documentation. **[search summary]** — [Audiofanzine user review](https://fr.audiofanzine.com/pitch-shifter-time-stretcher/celemony/Melodyne-Plug-In/avis/r.111147.html)

#### Over-correction artifacts
- Retune Speed 0 "will completely suppress any vibrato or deviations in pitch". Fast settings make sustained notes "unnaturally static", which is the reason Humanize exists. — [Antares manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- "Tonal mangling occurs when the pitch correction speed is set too fast for the audio that it is processing." — [Sound On Sound (Cher footnote)](https://www.soundonsound.com/techniques/recording-cher-believe)
- Sibilants and consonants are mostly noise; pitch-correcting them only degrades the sound. Melodyne therefore leaves detected sibilants acoustically unaltered and limits pitch, formant and time edits to the pitched part of each note. — [Sound On Sound, Melodyne 5](https://www.soundonsound.com/reviews/celemony-melodyne-5); [Celemony Help](https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_MacroPitch?env=dawsWithAra)
- Logic's "Keep Unvoiced Formants" retains sibilants and plosives "producing a more natural-sounding effect". — [Apple](https://support.apple.com/guide/logicpro/flex-pitch-algorithm-and-parameters-lgcpba8e3301/mac)
- Melodyne's pitch center is an average over the note, so a drifting sustained note snapped as a whole may stay partly out of tune. The advice is to split the note. — [Sound On Sound, Melodyne 5](https://www.soundonsound.com/reviews/celemony-melodyne-5)
- Practitioner advice: keep drift and vibrato when moving a note's center, because fully flattened notes can sound robotic. **[search summary]** — [Violet Recording](https://violetrecording.com/how-to-manually-tune-vocals/)

#### Artifacts in polyphonic, timing and large-shift edits
- **Polyphonic (DNA) processing.** It "changes the sound of your audio" (less high-end air) and smears transients. Pitch moves beyond a couple of semitones can sound "unpleasantly modulated". Muting more than about 30% of notes makes artifacts obvious. — [Sound On Sound, 2009](https://www.soundonsound.com/reviews/celemony-melodyne-dna-editor)
- **PSOLA-family limits.** Quality depends on accurate epoch marking and modifications ≤ 2×. Stretching unvoiced sound produces "tonal" noise. — [TAMU L19](https://people.engr.tamu.edu/rgutier/lectures/sp/l19.pdf)
- **Large shifts in general.** Conventional pitch shifting adds "formant shifts and robotic coloration" that grow with interval size. — [arXiv 2601.10345](https://arxiv.org/abs/2601.10345)

#### Vendor and expert best practice
- **Auto-Tune setup.** Set the correct key/scale (or Chromatic), Input Type and Tracking. Tune Retune Speed for the shortest problem notes, then add Humanize. Use Flex-Tune to keep expressive gestures. — [Antares manual](https://media.uaudio.com/support/manuals/dd/Auto-Tune%20Realtime%20Advanced%20Manual.pdf)
- **Melodyne correction amount.** Use Correct Pitch at less than 100% so that only notes far off pitch are moved. The drift slider leaves vibrato untouched. — [Celemony Help](https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_MacroPitch?env=dawsWithAra)
- **Sound On Sound (2011).**
  - Transparent fixes typically involve "very small changes of usually no more than 10 cents or so" in manual correction.
  - For badly missed notes, comp in a note from another take rather than forcing the plug-in.
  — [Sound On Sound](https://www.soundonsound.com/techniques/pitch-correction-plug-ins)

### Inferences
- **(Inference) Cleanup vs. tuning: the core distinction for the report.**
  - **"Voice cleanup"** (noise reduction, de-reverb/echo removal, de-essing, level riding) changes the non-musical parts of the signal. It does not change which notes are sung or when they are sung.
  - **"Vocal tuning" (음정/타이밍 보정)** changes the musical parameters of the sung notes: the f0 contour (pitch center, drift, vibrato) and the note timing and lengths. Formant handling is a side-control to keep timbre natural.
  - **How they interact:**
    1. Cleanup does not fix an off-key note, and tuning does not remove noise or room sound.
    2. Tuning depends on clean input. Vendors require isolated, monophonic, low-noise signals, and noise or breathiness causes tracking errors. In practice, cleanup and dry recording come before tuning.
    3. Some tuning suites include cleanup-like level tools (Melodyne 5's Leveling macro, Logic Flex Pitch's per-note gain hotspot), and apps bundle reverb as an effect. Product categories therefore overlap even though the underlying operations differ.
- **(Inference) "Warbling".** The term was not found in vendor documents. Its mechanisms are documented, though: target-note flipping under wide vibrato (Antares tutorial), frame-to-frame f0 jumps (librosa on YIN), and modulation artifacts on larger shifts (SOS DNA review, arXiv 2026). A reasonable explanation of audible warble is these effects combined with moderate retune speeds.

### Gaps
- I found no vendor-primary statement that reverb specifically degrades pitch detection. The claim rests on a user review and on inference from Antares' "periodically repeating waveform" requirement.
- No quantitative data was found on how much noise or reverb (SNR, RT60) degrades commercial tuners.

---

## 7. Mobile karaoke / singing apps that apply automatic tuning or vocal effects (Smule; Korean apps such as Everysing / 에브리싱)

### Takeaway
Smule's patents (priority 2009) document real-time, on-device pitch correction during karaoke capture. The correction targets either a key/scale or a per-song "score-coded" melody or harmony, using standard DSP (autocorrelation/AMDF detection, PSOLA/LPC correction). Smule's current store listing speaks only of "vocal effects", reverb and filters, and "optional AI‑powered tools".

For Everysing (에브리싱, SM Entertainment's karaoke app), I found no documentation of an automatic pitch-correction feature. Some other Korean karaoke and voice apps advertise "오토튠" (auto-tune) and echo in their store listings.

### Cited Findings
- **Smule patent US 9,147,385 B2, "Continuous score-coded pitch correction".**
  - Inventors: Salazar, Fiebrink, Wang, Ljungström, Smith, Cook. Assignee: Smule (originally SonicMule). Priority 15 Dec 2009; granted 29 Sep 2015.
  - Abstract: vocals captured during karaoke-style lyric display "can be pitch-corrected in real-time at the mobile device in accord with pitch correction settings".
  - Targets: a key or scale, or a "score-coded" note sequence synchronized with lyrics and backing track, including harmony note sets. A "Freestyle" fallback uses key-based correction.
  - Algorithms: AMDF/autocorrelation detection; PSOLA/LPC correction; FFT peak picking and phase vocoding as frequency-domain alternatives.
  — [Google Patents US9147385B2](https://patents.google.com/patent/US9147385B2/en)
- **Smule's Glee app (2010). [search summary]** Coverage says the app detects and corrects the user's pitch and doubles voices into harmonies. Smule said "It's not auto-tune; it's our own technology". Engineers encoded each note and its harmonies per song. Smule separately made a T-Pain app with the classic hard-tuned effect. — [Macworld](https://www.macworld.com/article/204873/smule_glee.html); [VatorNews](https://vator.tv/2010-04-15-glee-comes-to-the-iphone-with-help-of-smule/)
- **Smule's current App Store listing (© 2012–2026).**
  - "Smule uses studio‑quality audio and vocal effects to support creativity without replacing your unique sound."
  - "Enhance recordings with reverb, filters, and other vocal tools."
  - "explore optional AI‑powered tools to refine tone and range."
  - "Use pitch guidance, adjust song keys to better fit your vocal range."
  - It does not name auto-tune or pitch correction.
  — [App Store: Smule](https://apps.apple.com/sg/app/smule-sing-record-karaoke/id509993510)
- **Everysing (에브리싱). [search summary]** Described in 2015 as SM Entertainment's "smart karaoke" app, launching Chromecast support with about 24,000 K-pop and about 1,000 pop songs. No source found mentions pitch correction or auto-tune in Everysing. — [TenAsia (Korean)](https://www.tenasia.co.kr/article/2015031684164)
- **Other Korean listings. [search summary]**
  - "마이 마이크 – 목소리 변조 스피커 및 AI 노래 녹음" advertises "음악 오토튠, 에코" (music auto-tune, echo).
  - "모두의노래방" advertises voice recording, key change and scoring, with no auto-tune mention.
  — [App Store KR: 마이 마이크](https://apps.apple.com/kr/app/%EB%A7%88%EC%9D%B4-%EB%A7%88%EC%9D%B4%ED%81%AC-%EB%AA%A9%EC%86%8C%EB%A6%AC-%EB%B3%80%EC%A1%B0-%EC%8A%A4%ED%94%BC%EC%BB%A4-%EB%B0%8F-ai-%EB%85%B8%EB%9E%98-%EB%85%B9%EC%9D%8C/id1350312428); [App Store: 모두의노래방](https://apps.apple.com/us/app/%EB%85%B8%EB%9E%98%EB%B0%A9-%EC%96%B4%ED%94%8C-%EB%AA%A8%EB%91%90%EC%9D%98%EB%85%B8%EB%9E%98%EB%B0%A9-%EB%85%B8%EB%9E%98%EB%B0%A9-%EB%85%B8%EB%9E%98-%EB%B6%80%EB%A5%B4%EA%B8%B0/id1546687773?l=ko)

### Inferences
- **(Inference) How karaoke apps can differ from Auto-Tune's scale mode.** Because a karaoke app knows the song, it can correct toward the actual melody note in the score rather than the nearest scale note. That avoids wrong-note snapping, at the cost of per-song note data (as Smule's Glee coverage notes).
- **(Inference) Read store claims narrowly.** App-store wording such as "vocal effects", "AI tools" and "오토튠/에코" mixes three different things: effects (reverb/echo), cleanup, and pitch correction. It should not be taken as evidence of any specific tuning algorithm.

### Gaps
- Everysing: no official feature documentation on pitch correction was found (searches in Korean and English).
- Whether Smule's current app applies automatic pitch correction by default, and with which engine, is not documented in the current listing; the patents describe design intent, not the shipping product.
- No technical documentation was found for Korean apps' "오토튠" features.
