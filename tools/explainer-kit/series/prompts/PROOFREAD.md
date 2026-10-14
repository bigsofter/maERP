Native-level proofreader for Russian, French, English, Spanish. Do not edit files.
Episode folder: {EP}. Check vo/{ru,fr,en,es}.txt (one paragraph per line; `{word}` markers are sync points — ignore;
lines starting with # are comments; ru is the master, the others must say the same thing paragraph by paragraph) and
i18n/copy.json (on-screen text {key: {ru,fr,en,es}}; keys `demo.*` are product templates filled with values — the usual
place for agreement errors). i18n/ui.json holds exact product labels shown verbatim — report real errors there as
"product bugs" only.
Check: case / gender / number agreement, plurals with numbers ("1 ждёт", "4 lignes"), prepositions, articles/elision,
diacritics; typography (the build adds French narrow no-break spaces and ’ automatically — ignore those); meaning parity
with ru; consistent terms within one language (unless the product UI itself uses two words); natural spoken phrasing for
a TTS voice. Write {EP}/i18n/proofread.md (must-fix vs optional vs product bugs). Reply ≤ 20 lines: must-fix list
(current → corrected).
