"""Generates vo/<cue id>.wav for every cue in realisa-intro.html with Gemini text-to-speech, then runs
retime-cues.py so the animation follows the real voice.
The API key is read from the GEMINI_API_KEY environment variable (never commit it).
Usage: GEMINI_API_KEY=... python3 make-voiceover-gemini.py [voice] [model] [only_id]"""
import os, re, sys, json, base64, wave, subprocess, urllib.request, time
here = os.path.dirname(os.path.abspath(__file__))
voice = sys.argv[1] if len(sys.argv) > 1 else 'Laomedeia'
model = sys.argv[2] if len(sys.argv) > 2 else 'gemini-3.8-flash-tts'
only = sys.argv[3] if len(sys.argv) > 3 else None
key = os.environ['GEMINI_API_KEY']
TEMPO = float(os.environ.get("VO_TEMPO", "1.08"))
src = open(os.path.join(here, 'realisa-intro.html')).read()
cues = re.findall(r"\{id:'(\w+)',\s*s:[\d.]+,\s*d:[\d.]+,\s*text:\"([^\"]+)\"\}", src)
os.makedirs(os.path.join(here, 'vo'), exist_ok=True)
for cid, text in cues:
    if only and cid != only: continue
    body = {"contents": [{"parts": [{"text": text}]}],  # no style prefix: TTS reads any instruction aloud
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}}}}
    req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                                 data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": key})
    for attempt in range(4):
        try:
            d = json.load(urllib.request.urlopen(req, timeout=120)); break
        except Exception as e:
            if attempt == 3: raise
            print('retry', cid, e); time.sleep(3 * (attempt + 1))
    part = d['candidates'][0]['content']['parts'][0]['inlineData']
    pcm = base64.b64decode(part['data'])
    mt = part.get('mimeType', ''); m = re.search(r'rate=(\d+)', mt); rate = int(m.group(1)) if m else 24000
    raw = os.path.join(here, 'vo', cid + '.raw.wav')
    if 'wav' in mt: open(raw, 'wb').write(pcm)  # already a WAV file
    else:
        with wave.open(raw, 'wb') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(pcm)
    out = os.path.join(here, 'vo', cid + '.wav')
    trim = f"atempo={TEMPO},silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', raw, '-af', trim, '-ac', '1', '-ar', '44100', out], check=True)
    os.remove(raw)
    with wave.open(out) as w: print(f'{cid:8s} {w.getnframes()/w.getframerate():5.2f}s  {text}')
if not only: subprocess.run([sys.executable, os.path.join(here, 'retime-cues.py')], check=True)
