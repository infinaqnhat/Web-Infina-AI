"""Builds the voice-over and subtitles for lead-capture-video.html from voiceover.json.

Two voices are supported:
  python voiceover.py gemini              Google Gemini TTS (needs GEMINI_API_KEY in the environment;
                                          the key is never written to disk by this script)
  python voiceover.py kokoro <model dir>  Kokoro TTS, offline (pip install kokoro-onnx soundfile; model
                                          files from https://github.com/thewh1teagle/kokoro-onnx/releases)
Writes voiceover.m4a (the mixed track), subtitles.srt and subtitles.js (cues for the HTML page).
A line that runs into the next cue is sped up slightly (at most 12%) so the timing holds.
"""
import base64, json, os, subprocess, sys, tempfile, time, urllib.request
import numpy as np, soundfile as sf

here = os.path.dirname(os.path.abspath(__file__))
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
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{g['model']}:generateContent"
    def run(text):
        body = {'contents': [{'parts': [{'text': g['style'] + '\n' + text}]}],
                'generationConfig': {'responseModalities': ['AUDIO'], 'speechConfig': {
                    'voiceConfig': {'prebuiltVoiceConfig': {'voiceName': g['voice']}}}}}
        for attempt in range(5):
            try:
                req = urllib.request.Request(url, json.dumps(body).encode(), {'Content-Type': 'application/json', 'x-goog-api-key': key})
                data = json.load(urllib.request.urlopen(req, timeout=120))
                pcm = base64.b64decode(data['candidates'][0]['content']['parts'][0]['inlineData']['data'])
                return np.frombuffer(pcm, dtype='<i2').astype(np.float32) / 32768
            except Exception as e:
                print(f'retry {attempt + 1} for "{text[:30]}": {e}'); time.sleep(4 * (attempt + 1))
        raise SystemExit('Gemini TTS failed')
    return run

def fit(audio, slot):
    """Speed a clip up (pitch kept) when it is longer than its slot, by at most 12%."""
    d = len(audio) / SR
    if d <= slot: return audio
    tempo = min(1.12, d / slot)
    with tempfile.TemporaryDirectory() as t:
        a, b = os.path.join(t, 'a.wav'), os.path.join(t, 'b.wav')
        sf.write(a, audio, SR)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', a, '-af', f'atempo={tempo:.3f}', b], check=True)
        return sf.read(b, dtype='float32')[0]

_synth = synth_gemini() if ENGINE == 'gemini' else synth_kokoro()
CACHE = os.environ.get('VO_CACHE', os.path.join(here, '.vo-cache'))
def synth(text):
    """Clips are cached by engine, voice, style and text, so re-runs only call the TTS for changed lines."""
    import hashlib
    eng = cfg[ENGINE]
    h = hashlib.sha1(json.dumps([ENGINE, eng, text], sort_keys=True).encode()).hexdigest()[:16]
    f = os.path.join(CACHE, f'{ENGINE}-{h}.wav')
    if os.path.exists(f): return sf.read(f, dtype='float32')[0]
    audio = _synth(text); os.makedirs(CACHE, exist_ok=True); sf.write(f, audio, SR); return audio
TOTAL = cfg.get('duration', 68)
mix = np.zeros(int(TOTAL * SR), dtype=np.float32)
subs = []
prev_end = 0.0
for i, (t, text) in enumerate(cfg['cues']):
    t = max(t, prev_end + 0.2)          # a line never starts before the previous one has finished
    nxt = cfg['cues'][i + 1][0] if i + 1 < len(cfg['cues']) else TOTAL
    audio = synth(text)
    nz = np.where(np.abs(audio) > 0.01)[0]
    audio = audio[max(0, nz[0] - 600): nz[-1] + 2400]
    audio = fit(audio, nxt - 0.15 - t)
    s = int(t * SR); mix[s:s + len(audio)] += audio[:len(mix) - s]
    end = prev_end = t + len(audio) / SR
    shift = t - cfg['cues'][i][0]
    print(f'{t:5.2f}s  {len(audio) / SR:4.2f}s' + (f'  (+{shift:.2f}s)' if shift > 0.005 else '') + f'  {text[:60]}')
    subs.append([round(t, 2), round(min(end + 0.3, nxt + max(0, end + 0.2 - nxt) - 0.05), 2), text])
if prev_end > TOTAL: print(f'warning: the voice-over ends at {prev_end:.2f}s, after the video ({TOTAL}s)')
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
    f.write('// Generated by voiceover.py from voiceover.json. [start, end, text] in seconds.\nwindow.SUBTITLES = ' + json.dumps(subs, indent=1) + ';\n')
print('cues', len(subs), 'last ends', subs[-1][1])
