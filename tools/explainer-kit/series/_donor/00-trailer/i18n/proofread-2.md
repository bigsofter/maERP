# Proofread pass 2 (status: done)

## Must-fix
- demo.line2 en: "Port scanner" (reads as network port scanner) -> "Scan at the port"
- demo.line2 fr: "Passage scanner" (loses "в порту", ungrammatical noun-noun) -> "Passage au scanner du port"
- demo.line2 es: "Paso por escáner" (loses "port") -> "Paso por el escáner del puerto"
- demo.curve_baseline fr: straight apostrophe "d'une" -> "d’une" (rest of file uses ’)

## Should-fix (minor)
- vo/fr.txt p5: "un camion ou un chauffeur ... ne part pas" -> "ne partent pas" (two alternatives, more natural plural)
- vo/es.txt p5: "no sale a ruta" is looser than RU "не встанут на рейс" (assignment) -> "no se asigna a una misión"
- vo/es.txt p7: "Y el margen, con dos cifras:" sounds clipped for TTS -> "Y el margen se da en dos cifras:"
- demo.gate (all langs): capital after colon (RU "Водительское", FR "Permis", EN "Driving", ES "Permiso") -> lowercase if string is built mid-sentence
- demo.curve_baseline en: "180 000,00 MAD" uses French number format; if EN UI shows "180,000.00 MAD", align
- demo.gate does not name "required" document (fine as the on-screen reason, only s05/VO need it)

## Checked OK
- VO ru/fr/en/es p5-7: parity good; only REQUIRED documents block; forecast = quarter-end amount AND tight week; margins two figures direct (documents) / net (after overheads), never mixed; no "always" wording.
- s05.title1, s07.title, demo.line1, demo.queue_1, demo.week6_detail: grammar and parity OK.
