"""Build one HyperFrames project per language from the shared scene templates.

    python build.py                 # all four languages
    python build.py --lang ru       # one language
    python build.py --lang es --only s03   # index carries only bg + s03 (for a worker's checks)

Each language keeps its OWN pacing: paragraphs are placed back to back with the
gaps below, so every cue (a {marker} in vo/<lang>.txt) lands on that language's
word. Scenes start at a cue, and each scene gets its timing as `T` (seconds,
scene-local): every cue id, plus `in` (0), `out` (exit start) and `dur`.

Template tokens inside src/compositions/*.html:
    {{ui:<key>}}    exact product label from i18n/ui.json  (HTML-escaped)
    {{copy:<key>}}  composed / narrative text from i18n/copy.json (HTML-escaped)
    {{T}}           JSON timing object for this scene
    {{LANG}}        ru | fr | en | es
SFX: each scene may carry <script type="application/json" id="<sid>-sfx">[{"cue":"accept","off":0.05,"type":"stamp","gain":1}]</script>
     types: click key type pop whoosh swell error stamp shimmer. Rendered into one picture-locked track.
"""
import argparse, html, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")
LANGS = ["ru", "fr", "en", "es"]
SERIES = os.path.dirname(HERE)

def _sfx_python():
    """numpy+scipy interpreter for the SFX synth: $SFX_PY, else series/.venv, else this one."""
    if os.environ.get("SFX_PY"):
        return os.environ["SFX_PY"]
    venv = os.path.join(SERIES, ".venv", "bin", "python")
    return venv if os.path.exists(venv) else sys.executable

PY_SFX = _sfx_python()

# Per-episode pacing and scene list live in episode.json (see series/README.md):
#   lead / tail        silence before the first word / after the last one
#   gaps               pause after paragraph i (len = paragraphs - 1); longer where a picture must land
#   gap_scale          per-language multiplier on gaps (keep every language <= 120 s)
#   gap_override       per-language absolute gap for one paragraph index: {"es": {"6": 2.3}}
#   tail_lang, tempo   per-language tail; pitch-preserving voice speed-up (ffmpeg atempo)
#   scenes             [id, file, start cue (null = t0), lead before that cue]
EP = json.load(open(os.path.join(HERE, "episode.json")))
LEAD = EP.get("lead", 1.4)
TAIL = EP.get("tail", 3.2)
GAPS = EP["gaps"]
GAP_SCALE = EP.get("gap_scale", {})
TEMPO = EP.get("tempo", {})
GAP_OVERRIDE = {l: {int(k): v for k, v in d.items()} for l, d in EP.get("gap_override", {}).items()}
TAIL_LANG = EP.get("tail_lang", {})
OVERLAP = EP.get("overlap", 0.25)   # scenes overlap their neighbours by this much on each side of a boundary
EXIT = EP.get("exit", 0.5)          # length of a scene's exit window
SCENES = [tuple(x) for x in EP["scenes"]]
DISPLAY_FONT = {"ru": '"Manrope", "Inter", sans-serif'}  # Sora has no Cyrillic


def timing(lang):
    voice = json.load(open(os.path.join(HERE, "audio", lang, "voice.json")))
    k = TEMPO.get(lang, 1.0)
    for p in voice:
        p["duration"], p["speechEnd"] = round(p["duration"] / k, 3), round(p["speechEnd"] / k, 3)
        p["cues"] = [{"id": c["id"], "t": round(c["t"] / k, 3)} for c in p["cues"]]
    t, clips, cues = LEAD, [], {}
    for i, p in enumerate(voice):
        clips.append({"id": p["id"], "file": p["file"], "start": round(t, 3), "dur": p["duration"]})
        for c in p["cues"]:
            cues[c["id"]] = round(t + c["t"], 3)
        cues[f"p{i+1}end"] = round(t + p["speechEnd"], 3)
        if i < len(GAPS):
            t += p["speechEnd"] + GAP_OVERRIDE.get(lang, {}).get(i, GAPS[i] * GAP_SCALE.get(lang, 1.0))
    total = round(cues[f"p{len(voice)}end"] + TAIL_LANG.get(lang, TAIL), 2)
    bounds = [0.0 if c is None else round(cues[c] - lead, 3) for _, _, c, lead in SCENES]
    scenes = []
    for k, (sid, f, _, _) in enumerate(SCENES):
        start = bounds[k] - (OVERLAP if k else 0)
        end = bounds[k + 1] + OVERLAP if k + 1 < len(SCENES) else total
        dur = round(end - start, 3)
        T = {cid: round(v - start, 3) for cid, v in cues.items()}
        T.update({"in": 0, "out": round(dur - (EXIT if k + 1 < len(SCENES) else 1.2), 3), "dur": dur})
        scenes.append({"id": sid, "file": f, "start": round(start, 3), "dur": dur, "T": T})
    return {"lang": lang, "total": total, "clips": clips, "cues": cues, "scenes": scenes}


def fill(text, lang, ui, copy, T):
    def sub(m):
        kind, key = m.group(1), m.group(2)
        table = ui if kind == "ui" else copy
        if key not in table:
            raise KeyError(f"missing {kind}:{key}")
        return html.escape(typo(lang, table[key][lang]), quote=False)
    text = re.sub(r"\{\{(ui|copy):([\w.\-]+)\}\}", sub, text)
    return text.replace("{{T}}", json.dumps(T)).replace("{{LANG}}", lang)


def typo(lang, s):
    """French typography: narrow no-break space before : ; ? ! and inside « » (also keeps them from wrapping)."""
    if lang != "fr":
        return s
    s = s.replace("'", "\u2019")  # typographic apostrophe (some product strings use the straight one)
    s = re.sub(r" ([:;?!»])", "\u202f\\1", s)
    return re.sub(r"« ", "«\u202f", s)


def build(lang, only=None, out=None):
    tm = timing(lang)
    ui = json.load(open(os.path.join(HERE, "i18n", "ui.json")))
    copy = json.load(open(os.path.join(HERE, "i18n", "copy.json")))
    out = out or os.path.join(HERE, "build", lang)
    os.makedirs(os.path.join(out, "compositions"), exist_ok=True)
    for f in ("hyperframes.json", "package.json", "meta.json", "AGENTS.md", "CLAUDE.md"):
        if os.path.exists(os.path.join(SRC, f)):
            shutil.copy(os.path.join(SRC, f), out)
    if os.path.exists(os.path.join(out, "assets")):
        shutil.rmtree(os.path.join(out, "assets"))
    shutil.copytree(os.path.join(SRC, "assets"), os.path.join(out, "assets"))
    vdir = os.path.join(out, "assets", "voice")
    os.makedirs(vdir, exist_ok=True)
    for c in tm["clips"]:
        src = os.path.join(HERE, "audio", lang, c["file"])
        if lang in TEMPO:
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-filter:a", f"atempo={TEMPO[lang]}", os.path.join(vdir, c["file"])], check=True)
        else:
            shutil.copy(src, vdir)

    # compositions
    present, sfx = [], []
    bg = open(os.path.join(SRC, "compositions", "bg.html")).read()
    open(os.path.join(out, "compositions", "bg.html"), "w").write(fill(bg, lang, ui, copy, {"dur": tm["total"]}).replace("__TOTAL__", str(tm["total"])))
    for sc in tm["scenes"]:
        p = os.path.join(SRC, "compositions", sc["file"])
        if (only and sc["id"] not in only) or not os.path.exists(p):
            continue
        txt = fill(open(p).read(), lang, ui, copy, sc["T"])
        open(os.path.join(out, "compositions", sc["file"]), "w").write(txt)
        present.append(sc)
        m = re.search(r'<script type="application/json" id="%s-sfx">(.*?)</script>' % sc["id"], txt, re.S)
        if m:
            for ev in json.loads(m.group(1)):
                at = sc["T"][ev["cue"]] + ev.get("off", 0)
                sfx.append({"t": round(sc["start"] + at, 3), "type": ev["type"], "gain": ev.get("gain", 1.0), "pan": ev.get("pan", 0.0)})

    has_sfx = bool(sfx)
    if has_sfx:
        json.dump(sfx, open(os.path.join(out, "assets", "sfx.json"), "w"), indent=0)
        subprocess.run([PY_SFX, os.path.join(HERE, "..", "tools", "render_sfx.py"),
                        os.path.join(out, "assets", "sfx.json"), os.path.join(out, "assets", "sfx.wav"), str(tm["total"])], check=True)

    # index
    disp = DISPLAY_FONT.get(lang, '"Sora", "Inter", sans-serif')
    hosts = []
    for i, sc in enumerate(present):
        track = 2 + (int(sc["id"][1:]) % 2)  # alternate lanes so overlapping neighbours stack predictably
        hosts.append(f'      <div id="el-{sc["id"]}" data-composition-id="{sc["id"]}" data-composition-src="compositions/{sc["file"]}" '
                     f'data-start="{sc["start"]}" data-duration="{sc["dur"]}" data-track-index="{track}" data-width="1920" data-height="1080"></div>')
    audio = []
    for c in tm["clips"]:
        audio.append(f'      <audio id="vo-{c["id"]}" src="assets/voice/{c["file"]}" data-start="{c["start"]}" data-duration="{c["dur"]}" data-track-index="10" data-volume="1"></audio>')
    if has_sfx:
        audio.append(f'      <audio id="sfx" src="assets/sfx.wav" data-start="0" data-duration="{tm["total"]}" data-track-index="12" data-volume="0.55"></audio>')
    tpl = open(os.path.join(SRC, "index.tpl.html")).read()
    fonts = open(os.path.join(SRC, "assets", "fonts", "fonts.css")).read()
    kit = open(os.path.join(SRC, "assets", "kit.css")).read()
    kitjs = open(os.path.join(SRC, "assets", "kit.js")).read()
    idx = (tpl.replace("{{FONTS}}", fonts).replace("{{KIT}}", kit).replace("{{KITJS}}", kitjs).replace("{{LANG}}", lang).replace("{{DISPLAY}}", disp).replace("{{TOTAL}}", str(tm["total"]))
              .replace("{{HOSTS}}", "\n".join(hosts)).replace("{{AUDIO}}", "\n".join(audio))
              .replace("{{FADE_AT}}", str(round(tm["total"] - 1.0, 3))))
    open(os.path.join(out, "index.html"), "w").write(idx)
    json.dump(tm, open(os.path.join(out, "timing.json"), "w"), indent=1)
    print(f"{lang}: {tm['total']}s, {len(present)} scenes, {len(sfx)} sfx ->", out)
    return tm


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=LANGS)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--out", help="output dir (workers: build/_w/<scene>-<lang>)")
    ap.add_argument("--timing", action="store_true", help="print the timing table only")
    a = ap.parse_args()
    for l in ([a.lang] if a.lang else LANGS):
        if a.timing:
            tm = timing(l)
            print(l, "total", tm["total"])
            for s in tm["scenes"]:
                print("  ", s["id"], "start", s["start"], "dur", s["dur"], {k: v for k, v in s["T"].items() if 0 <= v <= s["dur"] and not k.startswith("p")})
        else:
            build(l, a.only, a.out)
