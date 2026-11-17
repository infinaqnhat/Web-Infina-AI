"""Procedural, royalty-free music bed for the Realisa clip (no samples). Usage: python3 gen-music.py out.wav seconds"""
import sys, wave, numpy as np
out, dur = sys.argv[1], float(sys.argv[2]); sr = 44100; bpm = 100; beat = 60/bpm
n = int(sr*dur); t = np.arange(n)/sr; mix = np.zeros(n)
def note(f): return 440*2**((f-69)/12)
# C maj7, A m7, F maj7, G6 (two bars each)
prog = [[48,55,59,64,67],[45,52,55,60,64],[41,48,52,57,60],[43,50,55,59,64]]
bar = 4*beat
def env(length, a, r):
    m = int(length*sr); e = np.ones(m); ai=min(int(a*sr),m//2); ri=max(1,min(int(r*sr),m//2))
    e[:ai] = np.linspace(0,1,ai)
    e[-ri:] *= np.linspace(1,0,ri); return e
k = 0; pos = 0.0
while pos < dur:
    ch = prog[k % 4]; L = min(2*bar, dur-pos); i0 = int(pos*sr); m = int(L*sr); tt = np.arange(m)/sr
    pad = sum(np.sin(2*np.pi*note(x+12)*tt*(1+d)) for x in ch for d in (-.002,.002))/len(ch)/2
    mix[i0:i0+m] += .16*pad*env(L, .8, .8)[:m]
    bass = np.sin(2*np.pi*note(ch[0]-12)*tt)+.3*np.sin(4*np.pi*note(ch[0]-12)*tt)
    mix[i0:i0+m] += .12*bass*env(L,.05,.4)[:m]
    # arpeggio, eighth notes, starts after the hook
    if pos >= 5.0:
        arp = [ch[1]+12, ch[2]+12, ch[3]+12, ch[4]+12, ch[3]+12, ch[2]+12, ch[4]+12, ch[3]+24]
        for j in range(int(L/(beat/2))):
            s = i0 + int(j*beat/2*sr); ln = int(.6*sr); ln = min(ln, n-s)
            if ln <= 0: break
            q = np.arange(ln)/sr; f = note(arp[j % 8])
            mix[s:s+ln] += .07*(np.sin(2*np.pi*f*q)+.25*np.sin(4*np.pi*f*q))*np.exp(-q*6)
    # soft kick + hat from the reveal to the recap
    if 5.3 <= pos < 47.0:
        for j in range(int(L/beat)):
            s = i0 + int(j*beat*sr); ln = min(int(.25*sr), n-s)
            if ln <= 0: break
            q = np.arange(ln)/sr
            mix[s:s+ln] += .22*np.sin(2*np.pi*(50+80*np.exp(-q*30))*q)*np.exp(-q*14)
            hs = s + int(beat/2*sr); hl = min(int(.05*sr), n-hs)
            if hl > 0: mix[hs:hs+hl] += .025*np.random.default_rng(j).standard_normal(hl)*np.exp(-np.arange(hl)/sr*80)
    pos += 2*bar; k += 1
# gentle low-pass (one-pole) and master fades
y = np.zeros(n); a = .35
for i in range(1,n): y[i] = y[i-1] + a*(mix[i]-y[i-1])
fade = np.ones(n); fi=int(1.5*sr); fo=int(3*sr); fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
y = y*fade; y = y/np.max(np.abs(y))*.8
d = (y*32767).astype(np.int16)
with wave.open(out,'wb') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(d.tobytes())
