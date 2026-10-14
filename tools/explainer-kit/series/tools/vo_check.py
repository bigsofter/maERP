"""Check an episode's VO scripts: same paragraphs and cue ids in every language; characters to synthesise.
usage (from an episode folder): python3 ../tools/vo_check.py"""
import re
ref = None; tot = 0
for l in ["ru", "fr", "en", "es"]:
    lines = [x for x in open(f"vo/{l}.txt").read().split("\n") if x.strip() and not x.startswith("#")]
    cues = [re.findall(r"\{(\w+)\}", x) for x in lines]
    chars = sum(len(re.sub(r"\{\w+\}", "", x)) for x in lines); tot += chars
    words = sum(len(re.sub(r"\{\w+\}", "", x).split()) for x in lines)
    print(f"{l}: {len(lines)} paragraphs, {sum(map(len, cues))} cues, {chars} chars, {words} words (~{words/2.4:.0f} s speech)")
    if ref is None: ref = cues
    elif cues != ref: print(f"  CUE MISMATCH in {l}: {cues} vs ru {ref}")
print("total chars to synthesise:", tot)
