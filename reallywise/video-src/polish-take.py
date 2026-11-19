"""Polishes a voiceover take: light compression so soft syllables are not swallowed, level matched,
then a peak limiter (so loud peaks do not force the whole take down).
Usage: python3 polish-take.py in.wav out.wav [--match ref1.wav ...] [--prefix head.wav --prefix-end SEC [--gap SEC]]
  --match   level target = median RMS of these files (default: every vo/*.wav except the output)
  --prefix  keep head.wav up to SEC seconds, add --gap seconds of silence, then the polished take
            (keeps "Meet Realisa." from the approved take and replaces only the rest of the line)"""
import sys, os, glob, wave, subprocess, tempfile, numpy as np
args = sys.argv[1:]; src, out = args[0], args[1]
def opt(name, many=False):
    if name not in args: return [] if many else None
    vals = []
    for a in args[args.index(name)+1:]:
        if a.startswith('--'): break
        vals.append(a)
    return vals if many else vals[0]
def load(p):
    with wave.open(p) as w: return np.frombuffer(w.readframes(w.getnframes()), np.int16)/32768
def save(p, y):
    with wave.open(p, 'wb') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(44100); w.writeframes((np.clip(y, -1, 1)*32767).astype(np.int16).tobytes())
rms = lambda x: np.sqrt(np.mean(x**2))
ff = lambda i, o, af: subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', i, '-af', af, '-ar', '44100', '-ac', '1', o], check=True)
here = os.path.dirname(os.path.abspath(__file__))
refs = opt('--match', True) or [p for p in glob.glob(os.path.join(here, 'vo', '*.wav')) if os.path.abspath(p) != os.path.abspath(out) and 'reference' not in p]
target = np.median([rms(load(r)) for r in refs])
t1, t2 = tempfile.mktemp(suffix='.wav'), tempfile.mktemp(suffix='.wav')
ff(src, t1, 'acompressor=threshold=-26dB:ratio=3:attack=5:release=80')
y = load(t1); head = opt('--prefix')
if head:
    h = load(head)[:int(float(opt('--prefix-end'))*44100)].copy()
    gain = rms(h[np.abs(h) > .02]) / rms(y[np.abs(y) > .02])  # match the kept half's speech level
    f = int(.01*44100); h[-f:] *= np.linspace(1, 0, f)
else:
    gain = target / rms(y)
ff(t1, t2, f'volume={20*np.log10(gain):.2f}dB,alimiter=limit=0.95:level=disabled')
y = load(t2)
if head: y = np.concatenate([h, np.zeros(int(float(opt('--gap') or 0)*44100)), y])
save(out, y); os.remove(t1); os.remove(t2)
print(f'{out}: {len(y)/44100:.2f}s, rms {20*np.log10(rms(y)):.1f} dB (target {20*np.log10(target):.1f} dB)')
