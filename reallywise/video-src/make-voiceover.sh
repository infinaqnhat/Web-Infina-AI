#!/usr/bin/env bash
# Generates vo/<cue id>.wav for every cue in realisa-intro.html with Google Cloud Text-to-Speech,
# then writes cues.js so the animation follows the real voice. Needs: gcloud logged in, a project
# with the Text-to-Speech API on, python3, ffmpeg.
# Usage: bash make-voiceover.sh [voice] [speaking_rate]
#   voice defaults to en-US-Chirp3-HD-Aoede (warm, upbeat); rate 1.12 keeps the pace fast.
set -euo pipefail
cd "$(dirname "$0")"
VOICE="${1:-en-US-Chirp3-HD-Aoede}"; RATE="${2:-1.12}"
TOKEN="$(gcloud auth print-access-token)"; PROJECT="$(gcloud config get-value project 2>/dev/null)"
mkdir -p vo
python3 - <<'PY' > vo/cues.tsv
import re
src = open('realisa-intro.html').read()
for m in re.finditer(r"\{id:'(\w+)',\s*s:[\d.]+,\s*d:[\d.]+,\s*text:\"([^\"]+)\"\}", src): print(m.group(1) + '\t' + m.group(2))
PY
while IFS=$'\t' read -r id text; do
  body=$(python3 -c 'import json,sys; print(json.dumps({"input":{"text":sys.argv[1]},"voice":{"languageCode":"en-US","name":sys.argv[2]},"audioConfig":{"audioEncoding":"LINEAR16","sampleRateHertz":44100,"speakingRate":float(sys.argv[3])}}))' "$text" "$VOICE" "$RATE")
  curl -sS -X POST "https://texttospeech.googleapis.com/v1/text:synthesize" \
    -H "Authorization: Bearer $TOKEN" -H "x-goog-user-project: $PROJECT" -H "Content-Type: application/json" -d "$body" \
    | python3 -c 'import json,sys,base64; d=json.load(sys.stdin); open(sys.argv[1],"wb").write(base64.b64decode(d["audioContent"]))' "vo/$id.raw.wav"
  # trim leading/trailing silence, force mono 44.1 kHz
  ffmpeg -v error -y -i "vo/$id.raw.wav" -af "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse" -ac 1 -ar 44100 "vo/$id.wav"
  rm "vo/$id.raw.wav"; echo "vo/$id.wav"
done < vo/cues.tsv
python3 retime-cues.py
