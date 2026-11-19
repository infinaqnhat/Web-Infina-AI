"""Makes every "Realisa" in the voiceover sound like the reference take: the word in vo/meet.wav
("Meet Realisa.", 0:05 to 0:07 in the clip). The word's position in each other line was read off
its loudness envelope (pauses and stop closures around the word) and is listed in TARGETS; the
reference is swapped in with level matching and short crossfades. Originals are kept in vo/original/.
If a line is regenerated, measure its word again before running this.
Usage: python3 fix-realisa.py [ref_start ref_end]   (seconds inside vo/meet.wav, default 0.295 0.95)"""
import os, sys, wave, shutil, numpy as np
here = os.path.dirname(os.path.abspath(__file__)); vo = os.path.join(here, 'vo'); orig = os.path.join(vo, 'original')
TARGETS = {'four': (0.00, 0.42), 'list': (1.26, 1.82), 'deal': (1.11, 1.55), 'end': (0.00, 0.68)}
rs, re_ = (float(sys.argv[1]), float(sys.argv[2])) if len(sys.argv) > 2 else (0.295, 0.95)
def load(p):
    with wave.open(p) as w: return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float64)/32768, w.getframerate()
def save(p, x, sr):
    with wave.open(p, 'wb') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((np.clip(x,-1,1)*32767).astype(np.int16).tobytes())
os.makedirs(orig, exist_ok=True)
for cid in ['meet', *TARGETS]:
    if not os.path.exists(os.path.join(orig, cid + '.wav')): shutil.copy(os.path.join(vo, cid + '.wav'), orig)
x, sr = load(os.path.join(orig, 'meet.wav'))
ref = x[int(rs*sr):int(re_*sr)].copy(); fade = int(.01*sr)
ref[:fade] *= np.linspace(0, 1, fade); ref[-fade:] *= np.linspace(1, 0, fade)
save(os.path.join(vo, 'realisa-reference.wav'), ref, sr)
for cid, (a, b) in TARGETS.items():
    y, sr2 = load(os.path.join(orig, cid + '.wav')); assert sr2 == sr
    s0, s1 = int(a*sr), min(len(y), int(b*sr))
    seg = y[s0:s1]; gain = np.sqrt(np.mean(seg**2))/(np.sqrt(np.mean(ref**2))+1e-9)
    r = ref*np.clip(gain, .6, 1.6); xf = int(.015*sr)
    head, tail = np.concatenate([np.zeros(xf), y[:s0+xf]]), y[s1-xf:].copy()
    head[-xf:] *= np.linspace(1, 0, xf); tail[:xf] *= np.linspace(0, 1, xf)
    rr = r.copy(); rr[:xf] *= np.linspace(0, 1, xf); rr[-xf:] *= np.linspace(1, 0, xf)
    out = np.concatenate([head[:-xf], head[-xf:] + rr[:xf], rr[xf:-xf], rr[-xf:] + tail[:xf], tail[xf:]])
    save(os.path.join(vo, cid + '.wav'), out, sr)
    print(f'{cid:5s} replaced {s0/sr:.2f}s to {s1/sr:.2f}s (gain {gain:.2f}), new length {len(out)/sr:.2f}s')
