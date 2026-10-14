#!/bin/bash
# ElevenLabs characters used / limit this period (the key itself is never printed).
KEY=$(grep -o 'ELEVENLABS_API_KEY=\S*' "$(dirname "$0")/../../.env" | cut -d= -f2)
[ -z "$KEY" ] && { echo "no ELEVENLABS_API_KEY in tmp/explainer/.env"; exit 1; }
curl -s https://api.elevenlabs.io/v1/user/subscription -H "xi-api-key: $KEY" | python3 -c "
import json,sys,datetime; d=json.load(sys.stdin)
print('tier', d.get('tier'), '| used', d.get('character_count'), 'of', d.get('character_limit'), '| left', (d.get('character_limit') or 0)-(d.get('character_count') or 0), '| resets', datetime.datetime.fromtimestamp(d.get('next_character_count_reset_unix') or 0).date())"
