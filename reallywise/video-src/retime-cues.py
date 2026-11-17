"""Reads vo/<cue id>.wav lengths and writes cues.js (window.CUE_OVERRIDE) so each cue starts where the
previous line ends plus the gap the original timing had (at least 0.15 s). Run after recording or
generating the voiceover, then re-render."""
import re, os, wave, json
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'realisa-intro.html')).read()
cues = [(m.group(1), float(m.group(2)), float(m.group(3))) for m in re.finditer(r"\{id:'(\w+)',\s*s:([\d.]+),\s*d:([\d.]+)", src)]
out = {}; t = cues[0][1]
for i, (cid, s, d) in enumerate(cues):
    f = os.path.join(here, 'vo', cid + '.wav')
    if os.path.exists(f):
        with wave.open(f) as w: d = w.getnframes() / w.getframerate()
    if i: t = max(t, out[cues[i-1][0]]['s'] + out[cues[i-1][0]]['d'] + max(.15, s - (cues[i-1][1] + cues[i-1][2])))
    out[cid] = {'s': round(t, 3), 'd': round(d, 3)}
open(os.path.join(here, 'cues.js'), 'w').write('window.CUE_OVERRIDE = ' + json.dumps(out, indent=1) + ';\n')
print('cues.js written, ends at %.1fs' % (out[cues[-1][0]]['s'] + out[cues[-1][0]]['d']))
