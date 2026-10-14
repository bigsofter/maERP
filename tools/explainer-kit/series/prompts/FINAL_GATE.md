Final pre-render gate. Episode folder: {EP}. Do NOT edit source files.
1. For each lang in ru fr en es: `python3 build.py --lang <lang> --out build/_final-<lang>`; in that dir run
   `npx hyperframes lint` and `npx hyperframes check`. Any lint error = FAIL; note check findings on #sNN-* elements.
2. For the shortest and the longest language (see total in timing.json): snapshot (batches ≤ 6 timestamps) every scene
   boundary ± 0.15 s, every lower-third title at mid-hold, and T.out − 0.1 of each scene. READ every image: no
   black/empty/flash seams, nothing at 0,0, no tofu/clipped text, no untranslated words, titles readable and clear of UI.
3. assets/sfx.json has events; assets/voice has every clip.
Write {EP}/build/_final-REPORT.md. Reply ≤ 12 lines: PASS/FAIL per language and any MUST problem (time + scene).
