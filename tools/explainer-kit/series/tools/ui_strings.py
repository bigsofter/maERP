"""Pull exact UI strings from the product's i18n catalogs (web + mobile) for the 4 video languages.
usage: python3 ui_strings.py <keys.txt> <out.json>
keys.txt: one key per line, 'web:<ns.key>' or 'app:<ns.key>'. Output: {key: {ru, fr, en, es}}."""
import json, glob, sys
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))  # repo root (tmp/explainer/series/tools → ../../../..)
LANGS = ["ru", "fr", "en", "es"]

def flat(d, pre=""):
    for k, v in d.items():
        p = f"{pre}.{k}" if pre else k
        if isinstance(v, dict): yield from flat(v, p)
        else: yield p, v

web, app = {}, {}
for l in LANGS:
    merged = {}
    for f in glob.glob(f"{ROOT}/apps/web/i18n/messages/{l}/*.json"):
        merged.update(json.load(open(f)))
    web[l] = dict(flat(merged))
    mob = f"{ROOT}/apps/mobile/src/i18n/{l}.json"   # maOptique has no mobile app — skip when absent
    app[l] = dict(flat(json.load(open(mob)))) if os.path.exists(mob) else {}

out, missing = {}, []
for line in open(sys.argv[1]):
    line = line.strip()
    if not line or line.startswith("#"): continue
    src, key = line.split(":", 1)
    cat = web if src == "web" else app
    vals = {l: cat[l].get(key) for l in LANGS}
    if any(v is None for v in vals.values()): missing.append((line, [l for l, v in vals.items() if v is None]))
    out[f"{src}.{key}"] = vals
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(len(out), "keys;", "missing:", missing or "none")
