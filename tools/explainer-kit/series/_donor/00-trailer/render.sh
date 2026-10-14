#!/bin/bash
# Build + gate + render every language. usage: ./render.sh [ru fr en es]
set -e
cd "$(dirname "$0")"
EP=$(basename "$PWD")
PY=${SFX_PY:-$( [ -x ../.venv/bin/python ] && echo ../.venv/bin/python || echo python3 )}
OUT=../_renders
mkdir -p "$OUT"
LANGS=${@:-ru fr en es}
for l in $LANGS; do
  echo "=== $l"
  $PY build.py --lang $l
  (cd build/$l && npx hyperframes lint 2>&1 | grep -E '◇|error' | tail -3)
  (cd build/$l && npx hyperframes render --quality high --output renders/$EP.$l.mp4 2>&1 | tail -4)
  # web loudness: -16 LUFS integrated, -1.5 dBTP; video stream copied untouched
  ffmpeg -y -v error -i build/$l/renders/$EP.$l.mp4 -c:v copy -af loudnorm=I=-16:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 192k -movflags +faststart "$OUT/$EP.$l.mp4"
  ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT/$EP.$l.mp4"
done
