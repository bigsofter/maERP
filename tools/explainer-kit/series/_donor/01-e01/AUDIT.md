# AUDIT 01-e01 (read-only fact audit; CHANGES.md decisions taken as given)

## MUST-FIX
1. s03 (phone, VO {phone} "from laptop to phone"): the phone shows an invented mobile layout (switcher chip beside a URL bar, 3 tick rows). The portal has no responsive rail: PortalShell.tsx:311 `<aside>` has no mobile/drawer variant (only `sm:` on the Cmd-K badge, :559); switcher lives in the rail header (:335). apps/mobile is driver-only. The server-side pref (migr. 074, PortalShell.tsx:289) is true, the picture is not. Fix: show a second desktop browser window (or a phone-width screenshot of the real portal) and word it "on any device in the browser"; or drop the phone frame.
2. s06 counts line "2025-04-03 -> 2026-10-03" (copy s06.counts): period start is the FIRST of the oldest month (demo.go:628-631, firstOfMonth(today-18 months)); for 2026-10-03 it is 2025-04-01. Fix: "2025-04-01 -> 2026-10-03" (all 4 langs).

## SHOULD-FIX
1. s01 topbar title uses nav_pouls ("Pouls entreprise"); the dashboard sets its own header (dashboard/page.tsx:121 usePageHeader title t('title') = "Pouls de l'entreprise"; PortalShell.tsx:251 prefers header.title over the nav label). Use the page-title string in the topbar, the nav label in the rail.
2. s06 overdue pill is amber (k-pill is-amber); product is TonePill tone="red" (InvoicesView.tsx:159-160), next to the status pill (Emise/Envoyee). Make it red. Row in product also carries VAT pill and "Echeance dd.MM.yyyy" under the client; acceptable to omit.
3. s06 invoice list is ascending and gap-numbered (0398, 0402, 0405, 0409, 0411, 0412). Product sorts created_at DESC (repo/invoice.go:322) and numbering is continuous per tenant (invariant 8, invoice.go:21), so a visible unfiltered register cannot skip numbers. Use consecutive numbers, newest first (or show it as a filtered view).
4. s06 CMR card "CMR - M-1042": M-n is a mission number (service/invoice.go:497); CMR numbers are CMR-%06d (demo.go:1231). Use e.g. "CMR-100412" with status "With the driver" (label ok).
5. s06 ru overdue "Prosrochena - 34 dn." differs from the product label ("Prosrochen", PRODUCT_BUGS #1). Intentional, but CHANGES.md does not list it; on-screen text is not what the prospect will see in ru. Either keep and log in CHANGES, or use the product wording.
6. VO fr {remove}: "Le dirigeant supprime la demo" while {roles} says "le proprietaire" and the product role label is "Proprietaire" (web.review.owner). Use "le proprietaire" (en/es/ru already say owner).
7. s04 role pills come from signup `team_roles` (Exploitant / Commercial / Mecanicien), while the portal shows DB/fixture names (PRODUCT_BUGS #5); fine as role names, but the fr "Exploitant" pill vs DB "Operateur / Dispatch" may mismatch what a prospect later sees in /team.
8. s01 jumps from address bar to a loaded Pouls with no login step; no claim made, but "opens straight in the workplace" is implied. Consider a one-frame login or leave the VO neutral (it is).
9. s03/s02 omit the padlock glyphs the product shows on Groupage, Carburant, Maintenance, Conseiller, Direction (espaces.ts lockIcon; PortalShell.tsx:451). Omission is safe; do not add words about "locked".
10. s06 demo client CITRUS SOUSS SARL (copy demo.cl1) may be a real Souss-region company; FRIGO NORD SARL ok. Prefer a clearly fictional name. ATLAS FRUITS EXPORT is not from the seed (customer's own row, fine).

## OK-noted
- Menu contents s02 match espaces.ts incl. groups; Admin pinned bottom with Equipe/Modules/Parametres; 4 spaces + hidden `personnel`. Four columns side by side is an illustration (product stacks selected spaces).
- s03 flow: switcher in rail header, tick Parc -> count 2->3, owner defaults 2 (Exploitation+Direction), last space cannot be unticked (not shown), Cmd-K -> "banque" -> Banque - FINANCE -> ghost "de passage" badge: matches (espaces.ts:227-233, 298-329; PortalShell.tsx:280-301). Depends on treasury module being on for the demo tenant.
- s04 role/module matrices match migration 033+ grants: sales sees Factures/Traites/Previsions/Missions, not Banque/Paiements/Fleet; mechanic sees Missions/Flotte/Chauffeurs/Carburant/Maintenance, not Factures. "Nobody hides anything by hand": true for gating; the space selector only hides from one's own view (stated in VO as ticking).
- s05 themes Clair/Mixte/Nuit/Auto on /profile, dusk = dark rail + light work area, Auto night 20:00-07:00 (theme.ts:56-60), pills FR AR EN ES RU in that order, Arabic mirrors (layout.tsx:32-35). Crossfade vs instant switch: declared in CHANGES.
- s06 banner text, "Les supprimer" -> inline confirm "Supprimer la demo / Garder" -> progress bar; owner only; own rows stay (DemoBanner.tsx, demo.go purge by registry). Raw count and ISO dates match the product (PRODUCT_BUGS #2-3). 18-month history "year and a half" true; overdue invoices and unreturned CMR exist in the seed.
- s07 "9 minutes" is the official landing/signup claim (landing.json cta.title, signup footer_note). URL transport.tinycio.ma is the landing host.
- VO identical in meaning across ru/fr/en/es; "year and a half", "two clicks", "two or three" consistent. Totals: no totals shown; amounts format fr-FR with MAD, consistent.
