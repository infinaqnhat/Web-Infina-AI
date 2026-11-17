"""Builds the soundtrack for realisa-intro.mp4 from timeline.json (written by the renderer).
Procedural music bed (no samples), click and whoosh effects, and, when vo/<cue id>.wav files exist,
the voiceover placed at each cue start with the music ducked under it.
Usage: python3 build-audio.py timeline.json out.wav [vo_dir]"""
import sys, os, json, wave, numpy as np
tl = json.load(open(sys.argv[1])); out = sys.argv[2]; vo_dir = sys.argv[3] if len(sys.argv) > 3 else None
sr = 44100; dur = tl['duration']; n = int(sr*dur); bpm = 120; beat = 60/bpm
rng = np.random.default_rng(7)
def note(m): return 440*2**((m-69)/12)
def add(buf, start, sig):
    i = int(start*sr)
    if i >= n or i + len(sig) <= 0: return
    if i < 0: sig = sig[-i:]; i = 0
    m = min(len(sig), n-i); buf[i:i+m] += sig[:m]
music = np.zeros(n); sfx = np.zeros(n); vo = np.zeros(n)
prog = [[45,52,57,60,64],[41,48,53,57,60],[48,55,60,64,67],[43,50,55,59,62]]  # Am F C G
bar = 4*beat; intro_end = tl['whooshes'][1]; outro = tl['whooshes'][-1]
k = 0; pos = 0.0
while pos < dur:
    ch = prog[k % 4]; L = bar; m = int(L*sr); tt = np.arange(m)/sr
    pad = sum(np.sin(2*np.pi*note(x+12)*tt*(1+d)) for x in ch for d in (-.003,.003))/len(ch)/2
    e = np.minimum(1, tt/.15)*np.minimum(1, (L-tt)/.2)
    add(music, pos, .10*pad*e)
    full = pos >= tl['whooshes'][0] - .01 and pos < outro + 1
    for j in range(8):  # 8th-note bass pulse
        q = np.arange(int(beat/2*sr))/sr; f = note(ch[0]-12)
        add(music, pos+j*beat/2, (.16 if full else .07)*(np.sin(2*np.pi*f*q)+.35*np.sin(4*np.pi*f*q))*np.exp(-q*7))
    if pos >= intro_end - .01 and pos < outro:  # 16th-note pluck arpeggio
        arp = [ch[2]+12, ch[3]+12, ch[4]+12, ch[3]+24, ch[4]+12, ch[3]+12, ch[2]+24, ch[4]+12]
        for j in range(16):
            q = np.arange(int(.3*sr))/sr; f = note(arp[j % 8])
            add(music, pos+j*beat/4, .045*(np.sin(2*np.pi*f*q)+.3*np.sin(6*np.pi*f*q))*np.exp(-q*14))
    if full:
        for j in range(4):
            q = np.arange(int(.3*sr))/sr
            add(music, pos+j*beat, .5*np.sin(2*np.pi*(48+110*np.exp(-q*35))*q)*np.exp(-q*11))
            hq = np.arange(int(.04*sr))/sr
            add(music, pos+j*beat+beat/2, .05*rng.standard_normal(len(hq))*np.exp(-hq*90))
            if j in (1,3):
                sq = np.arange(int(.18*sr))/sr
                add(music, pos+j*beat, .12*rng.standard_normal(len(sq))*np.exp(-sq*22) + .1*np.sin(2*np.pi*190*sq)*np.exp(-sq*30))
    pos += bar; k += 1
for c in tl['clicks']:
    q = np.arange(int(.03*sr))/sr; add(sfx, c, .35*np.sin(2*np.pi*2400*q)*np.exp(-q*220) + .2*rng.standard_normal(len(q))*np.exp(-q*300))
for w in tl['whooshes']:
    L = .45; q = np.arange(int(L*sr))/sr; noise = rng.standard_normal(len(q))
    sm = np.convolve(noise, np.ones(12)/12, mode='same'); env = np.sin(np.pi*q/L)**2
    add(sfx, w-.3, .22*sm*env)
have_vo = False
if vo_dir and os.path.isdir(vo_dir):
    for c in tl['cues']:
        f = os.path.join(vo_dir, c['id'] + '.wav')
        if not os.path.exists(f): continue
        with wave.open(f) as w:
            assert w.getframerate() == sr and w.getnchannels() == 1, f
            add(vo, c['s'], np.frombuffer(w.readframes(w.getnframes()), np.int16)/32768.0)
        have_vo = True
duck = np.ones(n)
if have_vo:
    envv = np.convolve(np.abs(vo), np.ones(2205)/2205, mode='same') > .01
    target = np.where(envv, .45, 1.0); a = 1/(sr*.08)
    duck = np.copy(target)
    for i in range(1, n): duck[i] = duck[i-1] + (target[i]-duck[i-1])*a
fade = np.ones(n); fo = int(2*sr); fade[-fo:] = np.linspace(1,0,fo)
y = (music*duck*.8 + sfx)*fade + vo*1.0
y = np.tanh(y*1.2)/np.tanh(1.2); y = y/np.max(np.abs(y))*.92
with wave.open(out, 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((y*32767).astype(np.int16).tobytes())
print('audio', out, 'voiceover' if have_vo else 'no voiceover', f'{dur:.1f}s')
