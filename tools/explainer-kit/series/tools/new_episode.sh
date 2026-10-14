#!/bin/bash
# Scaffold a new episode folder from the approved trailer pipeline.
# usage (from tmp/explainer/series): tools/new_episode.sh 01-e01-workspace "E01 · Рабочее место: …"
set -e
cd "$(dirname "$0")/.."
NAME=$1; TITLE=$2
[ -z "$NAME" ] && { echo "usage: tools/new_episode.sh <NN-slug> \"<script heading>\""; exit 1; }
[ -e "$NAME" ] && { echo "$NAME exists"; exit 1; }
T=00-trailer
mkdir -p "$NAME"/{vo,audio,i18n,briefs,src/compositions,src/assets}
cp $T/build.py $T/render.sh "$NAME/"
cp $T/src/index.tpl.html $T/src/hyperframes.json $T/src/package.json "$NAME/src/"
cp -R $T/src/assets/fonts $T/src/assets/kit.css $T/src/assets/kit.js $T/src/assets/icon.svg "$NAME/src/assets/"
cp $T/src/compositions/bg.html "$NAME/src/compositions/"
printf '{\n  "id": "%s",\n  "name": "%s"\n}\n' "$NAME" "$NAME" > "$NAME/src/meta.json"
# a sensible base set of shell/product keys; extend per episode, then: python3 ../tools/ui_strings.py i18n/ui-keys.txt i18n/ui.json
grep -E '^(#|web:nav_|web:espace_|web:group_|web:missions\.page_step_)' $T/i18n/ui-keys.txt > "$NAME/i18n/ui-keys.txt"
echo '{}' > "$NAME/i18n/copy.json"
python3 - "$NAME" "$TITLE" <<'PY'
import json, sys
name, title = sys.argv[1], sys.argv[2]
json.dump({"name": name, "title": title, "lead": 1.2, "tail": 3.0,
           "gaps": [], "gap_scale": {}, "tempo": {}, "gap_override": {}, "tail_lang": {},
           "overlap": 0.25, "exit": 0.5,
           "scenes": [["s01", "s01-xxx.html", None, 0.0]]},
          open(f"{name}/episode.json", "w"), ensure_ascii=False, indent=1)
PY
for l in ru fr en es; do echo "# $TITLE · $l. One line = one paragraph = one TTS clip. {cue} = picture sync point (before the word)." > "$NAME/vo/$l.txt"; done
echo "created $NAME — next: fact-check, vo/<lang>.txt, episode.json (gaps + scenes), briefs/sNN.md"
