# maERP

[Русский](README.md) · [English](README.en.md) · **Français** · [Español](README.es.md)

maERP est un progiciel de gestion d'entreprise pour la plateforme 1C:Enterprise 8.5 : ventes, achats, stock,
production, vente au détail avec caisse, trésorerie et comptabilité dans une seule base. Il est développé par TinyCIO.
L'interface et les imprimés existent en russe, français, anglais et espagnol ; le paramétrage fiscal vise le Maroc
et se complète par les taux du pays à la création de la base.

Les fichiers prêts à installer (`.cf` et `.cfu`) se trouvent dans [Releases](https://github.com/bigsofter/maERP/releases) ;
l'historique des changements est dans [docs/CHANGELOG.md](docs/CHANGELOG.md).

## Fonctionnalités

| Domaine | Contenu |
|---|---|
| Ventes | Devis, commandes clients, bons de livraison et factures fiscales, retours, remises en montant et en pourcentage, contrôle du crédit et blocage des expéditions, onglet « Articles » avec les lignes des documents dans la liste |
| Détail | Poste de caisse, sessions de caisse, tickets, vérificateur de prix, étiquettes, besoins des points de vente, secteur « Téléphones et accessoires » avec suivi par numéro de série (IMEI) |
| Achats | Commandes fournisseurs, appels d'offres, réceptions, retours fournisseurs, planification des achats selon le besoin, poste des achats |
| Stock | Transferts, entrepôts à bons, inventaires avec inventaire valorisé et état des écarts, lots et traçabilité, réception et comptage mobiles |
| Production | Nomenclatures, production à la commande, bons de sortie matières, déclarations de production, sous-traitance sur plusieurs commandes, coût de revient, gestion des machines : charge, arrêts, maintenance, efficacité (OEE) |
| Trésorerie | Caisse et banque, règlements clients et fournisseurs, documents en devises, créances échues, flux de trésorerie |
| Comptabilité et fiscalité | Plan comptable et écritures, comptabilités de gestion et fiscale séparées, zones de TVA et exonération, retenue à la source de la TVA, registres des factures fiscales |
| Paie et RH | Salariés, pointage, calcul de la paie et états |
| Service | Échange entre bases maERP par dossier partagé ou HTTPS, import Excel, attributs supplémentaires, droits par rôle, fenêtre « Nouveautés », mise à jour automatique des données |

La configuration compte 54 types de documents, 70 rapports et 26 rôles. Les imprimés sont à en-tête, avec le logo
de la société, un aperçu et une sortie dans la langue de la contrepartie.

## Installation et mise à jour

Il faut la plateforme 1C:Enterprise 8.5.1 et ses licences. Elles s'achètent auprès de 1C et de ses partenaires
et ne font pas partie de maERP.

- **Nouvelle base.** Créer la base à partir de `maERP-<version>.cf`. Un assistant s'ouvre au premier démarrage :
  société, pays, secteur, utilisateurs.
- **Mise à jour.** Charger `maERP-<version>.cfu` (mise à jour depuis les versions publiées) ou le `.cf` complet.
  À la première connexion de l'administrateur, le programme met à jour les données et affiche « Nouveautés ».
- **Déploiement sans interface** (serveur, client web) : [docs/DEPLOY.md](docs/DEPLOY.md), en russe.

Sauvegardez votre base de production avant toute mise à jour.

## Pour les développeurs

Les sources sont au format 1C:EDT : une arborescence de fichiers texte (`.mdo` pour les métadonnées, `.bsl` pour
le code). Le fichier `.cf` est un produit de build et n'est pas versionné. La documentation du projet est en russe.

Le développement se fait sur `develop` ; `main` ne reçoit que les états de version. Prérequis : plateforme 1C
8.5.1.1150, 1C:EDT (voir [docs/EDT-SETUP.md](docs/EDT-SETUP.md)) et Java 17, fourni avec EDT.

## Licences

- **Code et contenus de maERP** — © TinyCIO, sous licence
  [GNU Affero General Public License version 3](LICENSE) (AGPL-3.0). Le programme peut être librement utilisé, étudié,
  modifié et redistribué. Quiconque distribue une version modifiée ou y donne accès par le réseau doit en publier
  le code source aux mêmes conditions. Le programme est fourni sans aucune garantie.
- **Composants tiers** — pilotes d'équipements de vente et bibliothèques de 1C — appartiennent à leurs développeurs.
  Ils ne relèvent pas de la licence de maERP, et leur utilisation exige un accord distinct avec leurs titulaires.
  TinyCIO n'est pas responsable de cette utilisation. La liste et la permission supplémentaire pour l'exécution sur
  la plateforme 1C figurent dans [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) (en russe).
- **La plateforme 1C:Enterprise** fait l'objet d'une licence distincte de 1C.
- **Le nom et le logo maERP** ne sont pas couverts par la licence du code.

## Contact

Mise en place, support et conditions commerciales : TinyCIO, [tinycio.ru](https://tinycio.ru).
