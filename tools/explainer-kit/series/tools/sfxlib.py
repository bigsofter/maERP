#!/usr/bin/env python3
"""Procedural energetic soundtrack for the maTransports motion videos.

Everything is synthesized from scratch (no samples, no licensing questions).
The tempo grid is shared with the video: at 120 BPM and 30 fps one beat is
exactly 15 frames and one bar is 60 frames, so a cut placed on a bar boundary
in Remotion lands on the downbeat in the audio.

Usage: python music.py arrangement.json out.wav
"""
import json
import sys

import numpy as np
from scipy import signal

SR = 48000
rng = np.random.default_rng(20260901)


# ---------------------------------------------------------------- helpers

def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def secs(n):
    return np.arange(int(n * SR)) / SR


def saw(freq, n, phase0=0.0):
    """PolyBLEP band-limited sawtooth."""
    dt = freq / SR
    ph = (phase0 + dt * np.arange(n)) % 1.0
    y = 2 * ph - 1
    m1 = ph < dt
    t1 = ph[m1] / dt
    y[m1] -= t1 + t1 - t1 * t1 - 1
    m2 = ph > 1 - dt
    t2 = (ph[m2] - 1) / dt
    y[m2] -= t2 * t2 + t2 + t2 + 1
    return y


def square(freq, n, phase0=0.0):
    return saw(freq, n, phase0) - saw(freq, n, (phase0 + 0.5) % 1.0)


def lp(x, fc, order=2):
    sos = signal.butter(order, min(fc, SR * 0.45), "low", fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=-1)


def hp(x, fc, order=2):
    sos = signal.butter(order, fc, "high", fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=-1)


def bp(x, lo, hi, order=2):
    sos = signal.butter(order, [lo, min(hi, SR * 0.45)], "band", fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=-1)


def adsr(n, a=0.005, d=0.1, s=0.7, r=0.05, gate=None):
    gate = n / SR if gate is None else gate
    t = np.arange(n) / SR
    env = np.where(t < a, t / max(a, 1e-6), s + (1 - s) * np.exp(-(t - a) / max(d, 1e-6)))
    rel = t > gate
    env[rel] *= np.exp(-(t[rel] - gate) / max(r, 1e-6))
    return env


def sweep_filter(x, cutoff_curve, kind="low", block=256):
    """Time-varying 2-pole filter; cutoff_curve has one value per sample."""
    y = np.zeros_like(x)
    zi = None
    for i in range(0, x.shape[-1], block):
        fc = float(np.clip(cutoff_curve[min(i, len(cutoff_curve) - 1)], 30, SR * 0.45))
        sos = signal.butter(2, fc, kind, fs=SR, output="sos")
        if zi is None:
            zi = np.zeros((sos.shape[0], 2)) if x.ndim == 1 else np.zeros((sos.shape[0], x.shape[0], 2))
        if x.ndim == 1:
            y[i:i + block], zi = signal.sosfilt(sos, x[i:i + block], zi=zi)
        else:
            y[:, i:i + block], zi = signal.sosfilt(sos, x[:, i:i + block], axis=-1, zi=zi)
    return y


def pan2(x, pan):
    """Constant-power pan, pan in [-1, 1]."""
    a = (pan + 1) * np.pi / 4
    return np.vstack([x * np.cos(a), x * np.sin(a)])


# ---------------------------------------------------------------- instruments

def kick():
    t = secs(0.5)
    f = 46 + 120 * np.exp(-t * 32)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 6.5)
    click = hp(rng.standard_normal(len(t)), 2500) * np.exp(-t * 380) * 0.5
    return np.tanh(1.8 * (body + click)) * 0.95


def clap():
    t = secs(0.45)
    noise = rng.standard_normal(len(t))
    env = np.zeros(len(t))
    for k, off in enumerate([0.0, 0.011, 0.022]):
        m = t >= off
        env[m] += np.exp(-(t[m] - off) * (140 if k < 2 else 16)) * (0.8 if k < 2 else 1.0)
    x = bp(noise, 900, 5200) * env
    snare_body = np.sin(2 * np.pi * 185 * t) * np.exp(-t * 28) * 0.35
    return np.tanh(1.4 * (x * 0.8 + snare_body))


def hat(open_=False):
    t = secs(0.32 if open_ else 0.07)
    x = hp(rng.standard_normal(len(t)), 7500, 4)
    metal = sum(square(f, len(t), rng.random()) for f in (3150, 4280, 5370, 6510)) * 0.06
    x = x + hp(metal, 6000)
    return x * np.exp(-t * (11 if open_ else 70)) * (0.5 if open_ else 0.38)


def crash(dur=2.4):
    t = secs(dur)
    x = hp(rng.standard_normal(len(t)), 4200, 2)
    metal = sum(square(f, len(t), rng.random()) for f in (2210, 3367, 4790, 6011, 7333)) * 0.05
    x = (x + hp(metal, 3000)) * np.exp(-t * 2.2)
    return x * 0.45


def impact():
    t = secs(2.2)
    f = 30 + 70 * np.exp(-t * 6)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.4)
    rumble = lp(rng.standard_normal(len(t)), 260) * np.exp(-t * 3.2) * 0.9
    return np.tanh(1.5 * (boom + rumble)) * 0.9


def riser(dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    prog = t / dur
    noise = rng.standard_normal(n)
    cutoff = 250 * (9000 / 250) ** (prog ** 1.6)
    x = sweep_filter(noise, cutoff, "low") - sweep_filter(noise, cutoff * 0.25, "low")
    pitch = hz(57) * 2 ** (prog ** 2 * 2.0)
    ph = 2 * np.pi * np.cumsum(pitch) / SR
    tone = (np.sin(ph) + 0.4 * np.sin(2 * ph)) * 0.18
    amp = prog ** 2.2
    return (x * 0.55 + tone) * amp


def reverse_crash(dur):
    c = crash(dur)
    return c[::-1] * np.linspace(0.2, 1, len(c)) ** 2


def supersaw(midi, dur, voices=7, spread=0.32):
    n = int(dur * SR)
    out = np.zeros((2, n))
    det = np.linspace(-spread, spread, voices)
    for i, d in enumerate(det):
        v = saw(hz(midi + d), n, rng.random())
        p = (i / (voices - 1)) * 1.6 - 0.8
        out += pan2(v, p)
    return out / voices


def pluck(midi, dur=0.22, bright=1.0):
    n = int(max(dur, 0.25) * SR)
    t = np.arange(n) / SR
    x = saw(hz(midi), n, rng.random()) * 0.6 + square(hz(midi) * 1.002, n, rng.random()) * 0.4
    dark = lp(x, 900)
    y = dark * 0.55 + (x - dark) * np.exp(-t * 34) * bright
    return y * np.exp(-t * 9)


def lead(midi, dur):
    n = int((dur + 0.15) * SR)
    t = np.arange(n) / SR
    vib = 1 + 0.004 * np.sin(2 * np.pi * 5.5 * t) * np.clip((t - 0.18) * 4, 0, 1)
    f = hz(midi) * vib
    ph = np.cumsum(f) / SR
    a = 2 * (ph % 1.0) - 1
    b = 2 * ((ph * 1.006 + 0.3) % 1.0) - 1
    c = np.sign(np.sin(2 * np.pi * ph * 0.5))
    x = lp(a * 0.45 + b * 0.45 + c * 0.12, 5200)
    return x * adsr(n, a=0.006, d=0.18, s=0.62, r=0.09, gate=dur)


def bass_note(midi, dur):
    n = int((dur + 0.03) * SR)
    t = np.arange(n) / SR
    x = saw(hz(midi), n) * 0.6 + np.sin(2 * np.pi * hz(midi) * t) * 0.55
    bright = lp(x, 1500)
    dark = lp(x, 520)
    x = dark + (bright - dark) * np.exp(-t * 18)
    return np.tanh(1.3 * x) * adsr(n, a=0.003, d=0.12, s=0.85, r=0.025, gate=dur)


# ---------------------------------------------------------------- sound effects
# Each returns (signal, lead_in_seconds): lead_in > 0 means the sound must start
# that much BEFORE the cue (a swell or whoosh peaks on the cut, not after it).

def sfx_click():
    t = secs(0.08)
    x = hp(rng.standard_normal(len(t)), 3000) * np.exp(-t * 260) * 0.6
    x += np.sin(2 * np.pi * 2100 * t) * np.exp(-t * 180) * 0.35
    x += np.sin(2 * np.pi * 190 * t) * np.exp(-t * 90) * 0.4
    return x, 0.0


def sfx_key():
    t = secs(0.14)
    x = hp(rng.standard_normal(len(t)), 1500) * np.exp(-t * 200) * 0.7
    x += np.sin(2 * np.pi * 120 * t) * np.exp(-t * 45) * 0.8
    x += np.sin(2 * np.pi * 3400 * t) * np.exp(-t * 300) * 0.2
    return np.tanh(1.4 * x), 0.0


def sfx_type():
    t = secs(0.05)
    x = hp(rng.standard_normal(len(t)), 2500) * np.exp(-t * 320) * 0.5
    x += np.sin(2 * np.pi * (1500 + 400 * rng.random()) * t) * np.exp(-t * 260) * 0.2
    return x, 0.0


def sfx_pop():
    t = secs(0.12)
    f = 260 + 520 * np.exp(-t * 45)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 30)
    return x * 0.8, 0.0


def sfx_whoosh():
    dur = 0.55
    n = int(dur * SR)
    t = np.arange(n) / SR
    prog = t / dur
    bell = np.sin(np.pi * prog) ** 2
    cutoff = 500 * (5200 / 500) ** np.sin(np.pi * prog)
    x = sweep_filter(rng.standard_normal(n), cutoff, "low") - sweep_filter(rng.standard_normal(n), cutoff * 0.2, "low") * 0.3
    return x * bell * 0.8, dur * 0.5


def sfx_swell():
    dur = 0.9
    n = int(dur * SR)
    t = np.arange(n) / SR
    prog = t / dur
    x = sweep_filter(rng.standard_normal(n), 300 * (7000 / 300) ** prog, "low")
    return x * prog ** 3 * 0.9, dur


def sfx_error():
    out = np.zeros(int(0.26 * SR))
    for k, f in enumerate((233.0, 196.0)):
        n = int(0.085 * SR)
        t = np.arange(n) / SR
        b = lp(square(f, n), 1800) * np.exp(-t * 14) * 0.55
        i = int(k * 0.12 * SR)
        out[i:i + n] += b
    return out, 0.0


def sfx_stamp():
    t = secs(0.6)
    f = 55 + 60 * np.exp(-t * 18)
    thud = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)
    slap = lp(rng.standard_normal(len(t)), 1400) * np.exp(-t * 40) * 0.8
    return np.tanh(1.8 * (thud + slap)) * 0.9, 0.0


def sfx_shimmer():
    t = secs(1.2)
    x = np.zeros(len(t))
    for k, f in enumerate((2093, 2637, 3136, 4186, 5274)):
        x += np.sin(2 * np.pi * f * (1 + 0.002 * k) * t + k) * np.exp(-t * (3 + k)) / (k + 1.5)
    return x * 0.5, 0.0


SFX = {"click": sfx_click, "key": sfx_key, "type": sfx_type, "pop": sfx_pop, "whoosh": sfx_whoosh,
       "swell": sfx_swell, "error": sfx_error, "stamp": sfx_stamp, "shimmer": sfx_shimmer}
SFX_GAIN = {"click": 0.55, "key": 0.7, "type": 0.35, "pop": 0.4, "whoosh": 0.5, "swell": 0.45,
            "error": 0.5, "stamp": 0.85, "shimmer": 0.3}


# ---------------------------------------------------------------- harmony
# i - VI - III - VII in A minor: Am | F | C | G
PROG = [
    {"root": 45, "pad": [57, 60, 64, 69], "arp": [69, 72, 76, 81]},
    {"root": 41, "pad": [53, 57, 60, 64], "arp": [65, 69, 72, 77]},
    {"root": 48, "pad": [55, 60, 64, 67], "arp": [67, 72, 76, 79]},
    {"root": 43, "pad": [55, 59, 62, 67], "arp": [67, 71, 74, 79]},
]
# hook on an 8th-note grid, one row per chord bar (None = rest)
HOOK = [
    [76, None, 76, 74, 76, None, 81, 79],
    [77, None, 76, 72, None, 72, 74, 76],
    [79, None, 76, 72, 76, None, 79, 81],
    [79, None, 74, 71, 74, None, 76, None],
]
ARP_PATTERN = [0, 2, 1, 3, 2, 1, 3, 2, 0, 2, 1, 3, 2, 3, 1, 2]

# what each section type plays
STYLES = {
    #            kick  clap  hats  ohat  bass    pad   arp   lead  filter
    "intro":   dict(kick=0, clap=0, hats=0, ohat=0, bass=0, pad=1, arp=1, lead=0, sweep=(650, 3800)),
    "build":   dict(kick=1, clap=0, hats=1, ohat=0, bass=1, pad=1, arp=1, lead=0, sweep=(1400, 9000)),
    "drop":    dict(kick=1, clap=1, hats=2, ohat=1, bass=2, pad=1, arp=1, lead=1, sweep=None),
    "groove":  dict(kick=1, clap=1, hats=2, ohat=1, bass=2, pad=1, arp=1, lead=0, sweep=None),
    "break":   dict(kick=0, clap=0, hats=1, ohat=0, bass=0, pad=1, arp=1, lead=0, sweep=(2600, 700)),
    "outro":   dict(kick=0, clap=0, hats=0, ohat=0, bass=0, pad=1, arp=0, lead=0, sweep=(18000, 900)),
}


def render(arr):
    bpm = arr.get("bpm", 120)
    beat = 60.0 / bpm
    bar = 4 * beat
    total_bars = sum(s["bars"] for s in arr["sections"])
    tail = arr.get("tail", 3.0)
    n = int((total_bars * bar + tail) * SR)

    buses = {k: np.zeros((2, n)) for k in ("drums", "bass", "music", "lead", "fx", "verb_send", "delay_send")}

    def put(bus, t0, x, pan=0.0, gain=1.0):
        i = int(round(t0 * SR))
        if i >= n:
            return
        y = pan2(x, pan) if x.ndim == 1 else x
        m = min(y.shape[1], n - i)
        if i < 0:
            y = y[:, -i:]
            m = min(y.shape[1], n)
            i = 0
        buses[bus][:, i:i + m] += y[:, :m] * gain

    K, C, H, OH = kick(), clap(), hat(), hat(True)
    kick_times = []
    music_cut = np.full(n, 20000.0)
    cues = {"bpm": bpm, "bar_seconds": bar, "sections": [], "impacts": []}

    b0 = 0
    for si, sec in enumerate(arr["sections"]):
        st = STYLES[sec["type"]]
        nb = sec["bars"]
        t_sec = b0 * bar
        cues["sections"].append({"name": sec["name"], "type": sec["type"], "start_bar": b0, "bars": nb,
                                 "start_s": round(t_sec, 3)})
        next_type = arr["sections"][si + 1]["type"] if si + 1 < len(arr["sections"]) else None

        if st["sweep"]:
            lo, hi = st["sweep"]
            i0, i1 = int(t_sec * SR), int((t_sec + nb * bar) * SR)
            prog = np.linspace(0, 1, i1 - i0)
            music_cut[i0:i1] = lo * (hi / lo) ** prog

        for b in range(nb):
            gb = b0 + b
            tb = gb * bar
            ch = PROG[gb % 4]
            last_bar = b == nb - 1
            into_drop = last_bar and next_type in ("drop", "groove")
            into_end = last_bar and next_type is None

            # drums
            for q in range(4):
                tq = tb + q * beat
                if st["kick"] and not ((into_drop or into_end) and q == 3 and sec["type"] != "build"):
                    put("drums", tq, K, gain=0.8)
                    kick_times.append(tq)
                if st["clap"] and q in (1, 3):
                    put("drums", tq, C, pan=0.0, gain=0.62)
                    put("verb_send", tq, C, gain=0.18)
            if st["hats"]:
                steps = 16 if st["hats"] == 2 else 8
                for s in range(steps):
                    ts = tb + s * (bar / steps)
                    accent = 1.0 if s % (steps // 4) == (steps // 8) else 0.55
                    put("drums", ts, H, pan=0.25 * np.sin(s), gain=0.36 * accent)
            if st["ohat"]:
                for q in range(4):
                    put("drums", tb + q * beat + beat / 2, OH, pan=-0.2, gain=0.3)

            # snare roll into a drop
            if (into_drop and sec["type"] in ("build", "break", "intro")) or into_end:
                for s in range(16):
                    if s < 8 and s % 2:
                        continue
                    put("drums", tb + s * bar / 16, C, gain=0.18 + 0.5 * (s / 15) ** 2)

            # bass
            if st["bass"]:
                if st["bass"] == 2:  # off-beat pumping 8ths with octave pops
                    for e in range(8):
                        note = ch["root"] + (12 if e in (3, 7) else 0)
                        if e % 2 == 1 or e == 6:
                            put("bass", tb + e * beat / 2, bass_note(note, beat / 2 * 0.9), gain=0.62)
                else:
                    for e in range(8):
                        put("bass", tb + e * beat / 2, bass_note(ch["root"], beat / 2 * 0.8), gain=0.42)

            # chords
            if st["pad"]:
                for m in ch["pad"]:
                    x = supersaw(m, bar + 0.05)
                    x = lp(x, 3800 if sec["type"] in ("drop", "groove") else 2400)
                    env = adsr(x.shape[1], a=0.03 if sec["type"] != "intro" else 0.35, d=0.6, s=0.75, r=0.2, gate=bar)
                    put("music", tb, x * env, gain={"groove": 0.11, "intro": 0.24, "break": 0.22}.get(sec["type"], 0.16))
                    put("verb_send", tb, x * env, gain=0.05)

            # arp
            if st["arp"]:
                bright = 1.0 if sec["type"] in ("drop", "groove") else 0.6
                for s in range(16):
                    note = ch["arp"][ARP_PATTERN[s] % 4]
                    x = pluck(note, bright=bright)
                    put("music", tb + s * bar / 16, x, pan=0.35 if s % 2 else -0.35, gain=0.24 if sec["type"] in ("intro", "break") else 0.17)
                    put("delay_send", tb + s * bar / 16, x, gain=0.07)

            # hook
            if st["lead"]:
                row = HOOK[gb % 4]
                for e, m in enumerate(row):
                    if m is None:
                        continue
                    length = beat / 2
                    k = e + 1
                    while k < 8 and row[k] is None:
                        length += beat / 2
                        k += 1
                    x = lead(m, length * 0.92)
                    put("lead", tb + e * beat / 2, x, gain=0.2)
                    put("delay_send", tb + e * beat / 2, x, gain=0.12)
                    put("verb_send", tb + e * beat / 2, x, gain=0.08)

        # transitions into the next section
        if next_type in ("drop", "groove") and sec["type"] in ("intro", "build", "break"):
            rdur = min(nb, 2) * bar
            put("fx", t_sec + nb * bar - rdur, riser(rdur), gain=0.55)
            put("fx", t_sec + nb * bar - 1.6, reverse_crash(1.6), gain=0.5)
        if sec["type"] in ("drop", "groove", "outro") and sec.get("impact", True):
            put("fx", t_sec, impact(), gain=0.7 if sec["type"] != "groove" else 0.45)
            put("fx", t_sec, crash(), gain=0.5)
            put("verb_send", t_sec, crash(), gain=0.25)
            cues["impacts"].append(round(t_sec, 3))
        b0 += nb

    # final sting on the last downbeat: riser + reversed crash into it, then
    # whole chord + impact
    end_t = total_bars * bar
    put("fx", end_t - bar, riser(bar), gain=0.45)
    put("fx", end_t - 1.6, reverse_crash(1.6), gain=0.5)
    put("fx", end_t, impact(), gain=0.55)
    put("fx", end_t, crash(3.0), gain=0.45)
    for m in PROG[0]["pad"] + [PROG[0]["root"] + 12]:
        x = supersaw(m, tail, voices=5) * np.exp(-secs(tail) * 1.4)
        put("music", end_t, lp(x, 3000), gain=0.12)
        put("verb_send", end_t, x, gain=0.08)
    cues["end_s"] = round(end_t, 3)
    cues["impacts"].append(round(end_t, 3))

    # sound effects locked to picture events (seconds, from the scene builds)
    for ev in arr.get("sfx", []):
        fn = SFX.get(ev["type"])
        if fn is None:
            continue
        x, lead_in = fn()
        g = ev.get("gain", 1.0) * SFX_GAIN[ev["type"]]
        put("fx", ev["t"] - lead_in, x, pan=ev.get("pan", 0.0), gain=g)
        if ev["type"] in ("stamp", "shimmer", "whoosh", "swell"):
            put("verb_send", ev["t"] - lead_in, x, gain=g * 0.3)

    # sidechain ducking on bass + music (kick-driven pump)
    duck = np.ones(n)
    rel = beat * 0.85
    for tk in kick_times:
        i = int(tk * SR)
        m = min(int(rel * SR), n - i)
        if m <= 0:
            continue
        x = np.arange(m) / (rel * SR)
        duck[i:i + m] = np.minimum(duck[i:i + m], 1 - 0.72 * (1 - x) ** 2.2)
    buses["music"] *= duck
    buses["bass"] *= np.maximum(duck, 0.15)

    # delay: dotted 8th ping-pong
    d = int(beat * 0.75 * SR)
    dl = buses["delay_send"].copy()
    echo = np.zeros_like(dl)
    fb, src = 0.42, lp(dl, 4200)
    for k in range(1, 6):
        shift = d * k
        if shift >= n:
            break
        ch = k % 2
        echo[ch, shift:] += src[0 if ch else 1, :n - shift] * fb ** (k - 1) * 0.9
    buses["verb_send"] += echo * 0.4

    # reverb: synthetic stereo IR (exponential decay, darker tail)
    ir_len = int(2.4 * SR)
    t_ir = np.arange(ir_len) / SR
    ir = rng.standard_normal((2, ir_len)) * np.exp(-t_ir * 2.9)
    ir = lp(ir, 6500)
    ir[:, : int(0.018 * SR)] = 0
    ir /= np.sqrt((ir ** 2).sum(axis=1, keepdims=True))
    wet = np.vstack([signal.fftconvolve(buses["verb_send"][c], ir[c])[:n] for c in range(2)])

    music = buses["music"] + buses["lead"] + echo
    music = sweep_filter(music, music_cut, "low")
    mix = buses["drums"] + buses["bass"] + music + buses["fx"] + wet * 0.55
    mix = hp(mix, 32)
    # high shelf: tame hats/noise sizzle (~ -5 dB above 7 kHz) and a touch of 3 kHz harshness
    mix = mix - 0.45 * hp(mix, 7000, 2)
    mix = mix - 0.15 * bp(mix, 2500, 4500)
    # tame the sub so laptop speakers are not swamped
    mix = mix - 0.35 * lp(mix, 90)

    # glue + limiter
    mix /= np.max(np.abs(mix)) + 1e-9
    mix = np.tanh(mix * 1.25) / np.tanh(1.25)
    fade = int(0.6 * SR)
    mix[:, -fade:] *= np.linspace(1, 0, fade) ** 2
    mix *= 10 ** (-2.0 / 20) / (np.max(np.abs(mix)) + 1e-9)
    return mix, cues


def write_wav(path, x):
    from scipy.io import wavfile
    wavfile.write(path, SR, (x.T * 32767).astype(np.int16))


if __name__ == "__main__":
    arr = json.load(open(sys.argv[1]))
    mix, cues = render(arr)
    write_wav(sys.argv[2], mix)
    json.dump(cues, open(sys.argv[2].rsplit(".", 1)[0] + ".cues.json", "w"), indent=2)
    print(json.dumps(cues, indent=2))
