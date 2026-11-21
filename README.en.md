# maERP

[Русский](README.md) · **English** · [Français](README.fr.md) · [Español](README.es.md)

maERP is a packaged business management system for the 1C:Enterprise 8.5 platform: sales, purchasing, warehouse,
production, retail with a point of sale, cash and accounting in one database. It is developed by TinyCIO. The interface
and print forms are available in Russian, French, English and Spanish; the tax setup targets Morocco and is extended
with country rates when a database is created.

Ready-to-install files (`.cf` and `.cfu`) are in [Releases](https://github.com/bigsofter/maERP/releases); the change
history is in [docs/CHANGELOG.md](docs/CHANGELOG.md).

## Features

| Area | What it covers |
|---|---|
| Sales | Quotes, customer orders, delivery notes and tax invoices, returns, discounts by amount and percent, credit control and shipment blocking, an "Items" tab with document lines right in the list |
| Retail | Cashier workstation, cash shifts, receipts, price checker, labels and price tags, store replenishment needs, the "Phones and accessories" industry with serial number (IMEI) tracking |
| Purchasing | Supplier orders, tenders, receipts, supplier returns, purchase planning by need, purchasing workstation |
| Warehouse | Transfers, order-based warehouses, stock counts with a valued count sheet and a variance report, lots and lot traceability, mobile receiving and counting |
| Production | Bills of materials, make-to-order production, material requisitions, output, subcontracting for several orders, product cost, machine management: load, downtime, maintenance, effectiveness (OEE) |
| Cash | Cash desk and bank, settlements with customers and suppliers, documents in foreign currency, overdue debts, cash flow |
| Accounting and taxes | Chart of accounts and entries, separate management and tax accounting, VAT zones and exemption, VAT withholding at source, tax invoice registers |
| Payroll and HR | Employees, timesheets, payroll calculation and statements |
| Service | Exchange between maERP databases through a shared folder or HTTPS, Excel import, additional attributes, role-based rights, a "What's new" window, automatic data update |

The configuration has 54 document types, 70 reports and 26 roles. Print forms are branded, with the company logo,
a preview and output in the counterparty's language.

## Installation and update

You need the 1C:Enterprise 8.5.1 platform and its licenses. They are purchased from 1C and its partners and are not
part of maERP.

- **New database.** Create an infobase from `maERP-<version>.cf`. A wizard opens on first start: company, country,
  industry, users.
- **Update.** Load `maERP-<version>.cfu` (update from published releases) or the full `.cf`. On the administrator's
  first login the program updates the data and shows the "What's new" window.
- **Headless deployment** (server, web client): [docs/DEPLOY.md](docs/DEPLOY.md), in Russian.

Back up your production database before updating.

## For developers

Sources are stored in the 1C:EDT format: a tree of text files (`.mdo` for metadata, `.bsl` for module code). The `.cf`
file is a build artifact and is not committed. Project documentation is in Russian.

```
src/cf/      EDT project of the configuration
docs/        environment, tests, releasing, plans
scripts/     build and checks on top of the platform CLI
tools/       data migration from the previous edition
build/       build artifacts (not in git)
```

Development happens on `develop`; `main` only receives release states. Requirements: 1C platform 8.5.1.1150, 1C:EDT
(see [docs/EDT-SETUP.md](docs/EDT-SETUP.md)) and Java 17, which ships with EDT.

## Licenses

- **maERP code and materials** — © TinyCIO, licensed under the
  [GNU Affero General Public License version 3](LICENSE) (AGPL-3.0). You may freely use, study, modify and
  redistribute the program. Anyone who distributes a modified version or offers it over a network must publish its
  source code under the same terms. The program comes with no warranty.
- **Third-party components** — retail equipment drivers and 1C libraries — belong to their developers. They are not
  covered by the maERP license, and using them requires a separate agreement with their owners. TinyCIO is not
  responsible for such use. The list and the additional permission for running on the 1C platform are in
  [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) (in Russian).
- **The 1C:Enterprise platform** is licensed separately by 1C.
- **The maERP name and logo** are not covered by the code license.

## Contact

Implementation, support and commercial terms: TinyCIO, [tinycio.ru](https://tinycio.ru).
