"""Builds the voice-over and subtitles for lead-capture-video.html from voiceover.json.

Two voices are supported:
  python voiceover.py gemini [--dir product-tour]   Google Gemini TTS (needs GEMINI_API_KEY in the environment;
                                          the key is never written to disk by this script)
  python voiceover.py kokoro <model dir>  Kokoro TTS, offline (pip install kokoro-onnx soundfile; model
                                          files from https://github.com/thewh1teagle/kokoro-onnx/releases)
Writes voiceover.m4a (the mixed track), subtitles.srt and subtitles.js (cues for the HTML page).
A line never overlaps the previous one: when a line runs long, it starts later and the picture waits for it
(TIMEWARP in subtitles.js), so the read keeps its natural pace and stays in sync.
"""
import base64, json, os, re, subprocess, sys, tempfile, time, urllib.request
import numpy as np, soundfile as sf

here = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]
if '--dir' in ARGS:   # another video's folder, e.g. --dir product-tour (holds its own voiceover.json)
    i = ARGS.index('--dir'); here = os.path.join(here, ARGS[i + 1]); del ARGS[i:i + 2]
sys.argv = [sys.argv[0]] + ARGS
cfg = json.load(open(os.path.join(here, 'voiceover.json')))
ENGINE = sys.argv[1] if len(sys.argv) > 1 else 'gemini'
SR = 24000

def synth_kokoro():
    from kokoro_onnx import Kokoro
    model = sys.argv[2]
    k = Kokoro(os.path.join(model, 'kokoro-v1.0.onnx'), os.path.join(model, 'voices-v1.0.bin'))
    say = {'ReallyWise': 'Really Wise', 'HOA': 'H O A', 'QR': 'Q R'}
    def run(text):
        for a, b in say.items(): text = text.replace(a, b)
        audio, _ = k.create(text, voice=cfg['kokoro']['voice'], speed=cfg['kokoro']['speed'], lang='en-us')
        return audio
    return run

def synth_gemini():
    g = cfg['gemini']; key = os.environ['GEMINI_API_KEY']
    base = 'https://generativelanguage.googleapis.com/v1beta/models/'
    def call(model, body):
        for attempt in range(5):
            try:
                req = urllib.request.Request(base + model + ':generateContent', json.dumps(body).encode(),
                                             {'Content-Type': 'application/json', 'x-goog-api-key': key})
                return json.load(urllib.request.urlopen(req, timeout=120))['candidates'][0]['content']['parts']
            except Exception as e:
                print(f'  retry {attempt + 1}: {e}'); time.sleep(4 * (attempt + 1))
        raise SystemExit('Gemini request failed')
    def decode(part):
        raw = base64.b64decode(part['inlineData']['data']); mime = part['inlineData'].get('mimeType', '')
        if 'wav' in mime:   # a full WAV file: read it as one, so the header and metadata chunks are not played
            import io
            audio, sr = sf.read(io.BytesIO(raw), dtype='float32')
            if audio.ndim > 1: audio = audio.mean(axis=1)
        else:               # raw 16-bit PCM, audio/L16;rate=24000
            audio, sr = np.frombuffer(raw, dtype='<i2').astype(np.float32) / 32768, 24000
        if sr != SR:
            idx = np.arange(0, len(audio), sr / SR); audio = np.interp(idx, np.arange(len(audio)), audio).astype(np.float32)
        return audio
    def words(t):   # brand written either way counts as one word
        t = re.sub(r"[^a-z0-9 ]", ' ', t.lower().replace('-', ' '))
        t = re.sub(r"\breally\s+wise\b", 'reallywise', t)
        t = re.sub(r'\b([ap]) m\b', r'\1m', t)   # p.m. / PM
        t = re.sub(r'\b(re[a-z]?|ri[a-z]?|ra[a-z]?)\s?lisa\b', 'realisa', t)   # the assistant's name, however it is spelled back
        for x, y in (('any time', 'anytime'), ('open house', 'openhouse'), ('sign ins', 'signins'), ('sign up', 'signup'), ('24 7', '247')):
            t = t.replace(x, y)
        return t.split()
    def heard(audio):
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, 'c.wav'); sf.write(f, audio, SR, subtype='PCM_16')
            data = base64.b64encode(open(f, 'rb').read()).decode()
        parts = call(g['check_model'], {'contents': [{'parts': [{'inlineData': {'mimeType': 'audio/wav', 'data': data}},
                     {'text': 'Transcribe this audio word for word. Output only the words.'}]}]})
        return parts[0]['text']
    def limit(n): return 0.45 * n + 1.5          # slower than about 2.2 words a second means long pauses or a repeat
    def first_read(audio):
        """When a line is read twice, keep the part before the longest pause in the middle."""
        w = int(SR * 0.02); n = len(audio) // w
        quiet = [20 * np.log10(np.sqrt(np.mean(audio[i * w:(i + 1) * w] ** 2)) + 1e-9) < -45 for i in range(n)]
        best, i = None, int(n * 0.3)
        while i < int(n * 0.7):
            if quiet[i]:
                j = i
                while j < n and quiet[j]: j += 1
                if not best or j - i > best[1] - best[0]: best = (i, j)
                i = j
            else: i += 1
        return audio[:best[0] * w + int(SR * 0.1)] if best else audio
    def run(text):
        # the camel-case brand trips the voice up, and the domain is read out
        spoken = text.replace('ReallyWise.ai', 'Really Wise dot A I').replace('ReallyWise', 'Really Wise').replace('Realisa', 'Rea Lisa')
        want = words(text)
        models = [g['model']] * 3 + [g.get('fallback_model', g['model'])] * 3
        for attempt, model in enumerate(models):
            body = {'contents': [{'parts': [{'text': g['style'] + '\n' + spoken}]}],
                    'generationConfig': {'responseModalities': ['AUDIO'], 'speechConfig': {
                        'voiceConfig': {'prebuiltVoiceConfig': {'voiceName': g['voice']}}}}}
            audio = decode(call(model, body)[0])
            got = words(heard(audio))
            if len(got) >= 1.7 * len(want) and got[:len(want)] == want:   # read twice: keep the first read
                audio = first_read(audio); got = words(heard(audio))
            ok_words = len(want) - 1 <= len(got) <= len(want) and len(set(got) - set(want)) == 0 and len(set(want) - set(got)) <= 1   # no extra words
            ok_len = len(clean(audio)) / SR <= limit(len(want))
            if ok_words and ok_len: return audio
            print(f'  attempt {attempt + 1} ({model}): ' + ('too slow, ' if not ok_len else '') + f'heard: {" ".join(got)[:70]}')
        raise SystemExit(f'TTS kept misreading: {text}')
    run.limit = limit; run.words = words
    return run

def tempo(audio, rate):
    """Speeds a clip up (pitch kept) with ffmpeg's atempo."""
    with tempfile.TemporaryDirectory() as t:
        a, b = os.path.join(t, 'a.wav'), os.path.join(t, 'b.wav')
        sf.write(a, audio, SR)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', a, '-af', f'atempo={rate}', b], check=True)
        return sf.read(b, dtype='float32')[0]

def clean(audio):
    """Removes DC offset, trims the silence at both ends and fades the edges, so lines join without clicks."""
    audio = audio - audio.mean()
    w = int(SR * 0.02); n = len(audio) // w
    db = np.array([20 * np.log10(np.sqrt(np.mean(audio[i * w:(i + 1) * w] ** 2)) + 1e-9) for i in range(n)])
    on = np.where(db > -45)[0]
    a, b = max(0, on[0] * w - int(SR * 0.04)), min(len(audio), (on[-1] + 1) * w + int(SR * 0.12))
    audio = audio[a:b].copy()
    # pauses inside a line longer than MAX_PAUSE are shortened to it, with short fades, so the read stays tight
    MAX_PAUSE = cfg.get('max_pause', 0.35)
    n = len(audio) // w
    quiet = [20 * np.log10(np.sqrt(np.mean(audio[i * w:(i + 1) * w] ** 2)) + 1e-9) < -45 for i in range(n)]
    keep, i = [], 0
    while i < n:
        j = i
        while j < n and quiet[j] == quiet[i]: j += 1
        seg = audio[i * w:j * w]
        if quiet[i] and 0 < i and j < n and (j - i) * 0.02 > MAX_PAUSE:
            half = int(SR * MAX_PAUSE / 2); seg = np.concatenate([seg[:half], seg[-half:]])
        keep.append(seg); i = j
    audio = np.concatenate(keep + [audio[n * w:]])
    fi, fo = int(SR * 0.01), int(SR * 0.08)
    audio[:fi] *= np.linspace(0, 1, fi); audio[-fo:] *= np.linspace(1, 0, fo)
    return audio

_synth = synth_gemini() if ENGINE == 'gemini' else synth_kokoro()
CACHE = os.environ.get('VO_CACHE', os.path.join(here, '.vo-cache'))
def synth(text):
    """Clips are cached by engine, voice, style and text, so re-runs only call the TTS for changed lines."""
    import hashlib
    eng = cfg[ENGINE]
    h = hashlib.sha1(json.dumps([ENGINE, eng, text], sort_keys=True).encode()).hexdigest()[:16]
    f = os.path.join(CACHE, f'{ENGINE}-{h}.wav')
    if os.path.exists(f):
        audio = sf.read(f, dtype='float32')[0]
        lim = getattr(_synth, 'limit', None)
        if not lim or len(clean(audio)) / SR <= lim(len(_synth.words(text))): return audio
        print(f'  cached clip too slow, regenerating: {text[:50]}')
    audio = _synth(text); os.makedirs(CACHE, exist_ok=True); sf.write(f, audio, SR); return audio
TOTAL = cfg.get('duration', 68)
subs = []
GAP = cfg.get('gap', 0.4)
clips, prev_end, prev_d, prev_t = [], 0.0, 0.0, 0.0
for i, (d, text, *opt) in enumerate(cfg['cues']):
    rate = (opt[0] if opt else {}).get('rate', 1.0)   # rate > 1 plays this line, and the picture leading to it, faster
    audio = clean(synth(text))
    if rate != 1.0: audio = tempo(audio, rate)
    # real start: the picture runs at `rate` since the previous line, and waits if that line is still being read
    t = max(prev_t + (d - prev_d) / rate, prev_end + GAP / rate)
    if cfg.get('tight') and i > 0: t = prev_end + GAP / rate   # no silence between lines: the picture is shortened to match
    prev_end, prev_d, prev_t = t + len(audio) / SR, d, t
    clips.append((d, t, audio, text))
    print(f'{d:5.2f} -> {t:5.2f}s  {len(audio) / SR:4.2f}s' + (f'  x{rate}' if rate != 1 else '') + f'  {text[:60]}')
shift = prev_t - prev_d
TOTAL_REAL = round(prev_end + cfg['tail'], 2) if cfg.get('tail') else round(max(TOTAL + shift, prev_end + 1.5), 2)
# warp: [design time, real time] anchors; the page plays design time t_d at real time warp(t_d)
WARP = [[0, 0]] + [[round(d, 3), round(t, 3)] for d, t, _, _ in clips] + [[TOTAL, TOTAL_REAL]]
mix = np.zeros(int(TOTAL_REAL * SR) + SR, dtype=np.float32)
for i, (d, t, audio, text) in enumerate(clips):
    s = int(t * SR); mix[s:s + len(audio)] += audio
    end = t + len(audio) / SR
    nxt = clips[i + 1][1] if i + 1 < len(clips) else TOTAL_REAL
    subs.append([round(t, 2), round(min(end + 0.3, nxt - 0.05), 2), text])
mix = mix[:int(TOTAL_REAL * SR)]
mix = mix / max(1e-6, np.abs(mix).max()) * 0.89
with tempfile.TemporaryDirectory() as d:
    wav = os.path.join(d, 'vo.wav'); sf.write(wav, mix, SR)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11',
                    '-ar', '48000', '-c:a', 'aac', '-b:a', '160k', os.path.join(here, 'voiceover.m4a')], check=True)
def ts(x):
    ms = int(round(x * 1000)); return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'
with open(os.path.join(here, 'subtitles.srt'), 'w') as f:
    for n, (a, b, text) in enumerate(subs, 1): f.write(f'{n}\n{ts(a)} --> {ts(b)}\n{text}\n\n')
with open(os.path.join(here, 'subtitles.js'), 'w') as f:
    f.write('// Generated by voiceover.py from voiceover.json. Times are real seconds in the final video.\n'
            '// SUBTITLES: [start, end, text]. TIMEWARP: [design time, real time] anchors. DURATION: real length.\n'
            'window.SUBTITLES = ' + json.dumps(subs, indent=1) + ';\nwindow.TIMEWARP = ' + json.dumps(WARP) +
            ';\nwindow.VO_DURATION = ' + json.dumps(TOTAL_REAL) + ';\n')
print('cues', len(subs), 'video length', TOTAL_REAL)
