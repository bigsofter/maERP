"""Append to every briefs/s*.md a table of the tokens it uses, with exact values in ru/fr/en/es, and fail on unknown keys.
usage (from an episode folder): python3 ../tools/brief_tables.py"""
import glob, json, re, sys
ui = json.load(open("i18n/ui.json")); cp = json.load(open("i18n/copy.json"))
bad = []
for f in sorted(glob.glob("briefs/s*.md")):
    s = open(f).read().split("\n## Strings (generated")[0]
    toks = []
    for kind, key in re.findall(r"\{\{(ui|copy):([\w.\-]+)\}\}", s):
        if (kind, key) not in toks: toks.append((kind, key))
    rows = ["", "## Strings (generated — exact values per language; size for the LONGEST)", "", "| token | ru | fr | en | es |", "|---|---|---|---|---|"]
    for kind, key in toks:
        t = ui if kind == "ui" else cp
        if key not in t: bad.append((f, kind, key)); continue
        rows.append(f"| `{{{{{kind}:{key}}}}}` | " + " | ".join(t[key][l].replace("|", "\\|") for l in ["ru", "fr", "en", "es"]) + " |")
    open(f, "w").write(s.rstrip() + "\n" + "\n".join(rows) + "\n")
    print(f, len(toks), "tokens")
print("MISSING:", bad or "none"); sys.exit(1 if bad else 0)
