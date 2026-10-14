"""Render a picture-locked SFX track from events. usage: python render_sfx.py <sfx.json> <out.wav> <total_seconds>
Events: [{"t": seconds, "type": "click|key|type|pop|whoosh|swell|error|stamp|shimmer", "gain": 1.0, "pan": 0.0}].
The synth lives in tools/sfxlib.py (numpy + scipy)."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sfxlib as base
from sfxlib import SR, pan2

events = json.load(open(sys.argv[1])); total = float(sys.argv[3])
n = int(total * SR); out = np.zeros((2, n))
for ev in events:
    x, lead = base.SFX[ev["type"]]()
    g = ev.get("gain", 1.0) * base.SFX_GAIN[ev["type"]]
    y = pan2(x, ev.get("pan", 0.0)) if x.ndim == 1 else x
    i = int(round((ev["t"] - lead) * SR)); j = 0
    if i < 0: j, i = -i, 0
    m = min(y.shape[1] - j, n - i)
    if m > 0:
        out[:, i:i + m] += y[:, j:j + m] * g
peak = np.abs(out).max(); print("sfx peak", round(float(peak), 3))
if peak > 0.98: out *= 0.98 / peak
base.write_wav(sys.argv[2], out)
