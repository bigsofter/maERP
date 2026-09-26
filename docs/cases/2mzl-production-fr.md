# Cas client — 2MZL : la production pilotée depuis la commande client

Brouillon de la fiche cas pour le portail tinycio (section maERP → Production).
Les cas ne sont pas des fichiers sur la landing : ils sont saisis dans le portail, la landing
les récupère par requête. Ce fichier contient le texte dans la structure de la fiche.

> **À confirmer avant publication**
> 1. **Raison sociale exacte et logo** du client (décision du propriétaire 2026-09-09 : le cas est
>    publié en français, nom du client divulgué). Ici : « 2MZL », forme à valider.
> 2. **Les chiffres du bloc « Résultat »** — aucune mesure n'a été relevée à ce jour. Les valeurs
>    sont laissées en `{{…}}` : soit elles sont mesurées chez le client, soit les phrases
>    chiffrées sont supprimées. Ne rien publier de non mesuré.
> 3. La **relecture linguistique** du texte par un locuteur natif (cf. `docs/FRENCH-REVIEW.xlsx`).

---

## Le client

**2MZL**, Maroc. Fabrication sur commande : chaque commande client est un produit à fabriquer,
avec ses matières, ses achats dédiés et, pour une partie des opérations, un sous-traitant.

## Le défi

La chaîne réelle de l'entreprise était simple à décrire et coûteuse à tenir :

> devis → commande client du produit fini → commande fournisseur des matières →
> réception des matières → fabrication → vente

Le point de blocage n'était pas le logiciel, mais **les ressources** : personne, à l'atelier,
n'a le temps de saisir des documents de production. Chaque ordre de fabrication, chaque bon de
sortie matière et chaque bon de production saisis à la main, c'est du temps qui n'est pas passé
à produire. Résultat, dans la plupart des ERP : soit l'atelier saisit et la production ralentit,
soit l'atelier ne saisit pas et la comptabilité matière décroche du réel.

S'ajoutaient trois difficultés propres à la fabrication sur commande :

- **Les matières achetées pour une commande donnée** doivent rester rattachées à cette commande :
  sinon le coût de revient du produit fini est une moyenne, pas un coût réel.
- **Les nomenclatures changent.** Une commande passée en mars doit rester calculée sur la
  nomenclature de mars, même si la nomenclature a été corrigée depuis.
- **La sous-traitance** ajoute un niveau : un semi-fini part chez le sous-traitant, revient
  transformé, et son coût doit inclure la prestation du sous-traitant.

## Ce que nous avons fait

Nous n'avons pas ajouté un module de production classique. Nous avons fait de la **commande
client le seul document que l'atelier pilote**, et laissé le système produire les écritures.

**1. Les nomenclatures deviennent versionnées.** La composition d'un produit est conservée dans
un registre à historique : la validation d'une commande enregistre la version de la nomenclature
utilisée. Une correction ultérieure de la nomenclature ne réécrit jamais le passé.

**2. La commande client porte ses matières.** À la saisie du produit, les matières sont reprises
de la nomenclature. La validation de la commande crée un **besoin en matières** dans un registre
dédié, ligne par ligne, produit par produit.

**3. Les achats se rattachent au besoin.** La commande fournisseur et la réception écrivent en
face du besoin ce qui est « commandé » puis « arrivé ». À tout moment, pour chaque matière d'une
commande, on lit : besoin, commandé, arrivé, manquant.

**4. L'étape de la commande se calcule toute seule.** Personne ne saisit de statut. L'étape est
recalculée à chaque écriture de la chaîne : brouillon → besoins en préparation → commande
fournisseur → approvisionnement des besoins → en production → en attente d'expédition →
en attente de paiement → terminée. L'annulation d'une validation fait reculer l'étape : l'étape
est toujours le reflet des données du moment.

**5. La production se déclenche à l'expédition.** C'est la réponse au vrai problème du client :
la validation de la vente **crée et valide elle-même le bon de production** de ce qui est expédié.
Les matières sont consommées selon la composition de la commande et, en priorité, **sur les lots
achetés pour cette commande**. L'atelier ne saisit aucun document de production.

**6. La sous-traitance suit la même logique.** L'envoi chez le sous-traitant produit
automatiquement le semi-fini concerné, qui part à son compte ; la réception de sous-traitance
solde les matières transférées et valorise le produit reçu, prestation du sous-traitant incluse
dans son coût.

**7. Tout se pilote depuis un poste de travail unique.** Le « Poste de production » réunit la
file des commandes et, sous elle, des onglets — matières, commandes fournisseur, réceptions,
sous-traitance, production, expéditions. **On saisit dans les lignes du tableau** : la ligne
terminée, le document est créé, rempli et validé. Les formulaires de document ne s'ouvrent que
pour les cas particuliers.

## Le tableau de bord et l'analytique

Deux niveaux de lecture, pensés pour deux métiers différents.

### Le tableau de bord — la vue du dirigeant

Il s'ouvre à l'entrée dans le programme, sans réglage ni filtre à poser.

- **Quatre indicateurs de situation** : commandes en production, produit sur 30 jours,
  productions du jour, articles actuellement chez les sous-traitants.
- **Trois graphiques** : production par jour sur 30 jours, commandes actives par statut
  (camembert), top 5 des produits sur 30 jours.
- **Quatre indicateurs de rythme**, qui répondent à « est-ce qu'on accélère ? » plutôt qu'à
  « combien ? » : série de jours consécutifs avec production, record de la journée sur 30 jours,
  mois en cours comparé au mois précédent, et **expéditions en retard** — le seul indicateur
  d'alerte du tableau.

Le dirigeant n'a rien à demander à personne : les chiffres viennent des documents saisis par
l'atelier pour son propre travail. C'est la différence entre un reporting et un tableau de bord —
ici, aucune donnée n'est saisie *pour* le tableau de bord.

### L'indicateur de commande — la vue de l'atelier

Chaque commande porte, à côté de son étape, **cinq cercles** :

> approvisionnement en matières · réception des matières · production · expédition · paiement
>
> `○` non commencé · `◐` partiel · `●` complet

L'étape nomme le premier maillon non bouclé ; les cinq cercles montrent la commande entière d'un
coup d'œil. Une commande peut être « en production » et déjà à moitié expédiée — l'étape seule ne
le dit pas, l'indicateur si. Sur une file de trente commandes, l'opérateur voit en une seconde
laquelle est bloquée et sur quoi.

### Le détail matière

Sous chaque commande, l'onglet « Matières » donne, pour chaque composant : besoin, commandé,
arrivé, pris sur stock, **manque** et **reste à recevoir**. C'est la liste de travail de
l'acheteur, et c'est aussi le rapport « Besoins de production », imprimable par commande.

## Les bénéfices

- **L'atelier ne saisit pas la production.** Les bons de production et les consommations matières
  naissent de l'expédition et de l'envoi en sous-traitance. Zéro double saisie.
- **Un coût de revient réel, pas moyen.** Les matières sont consommées sur les lots achetés pour
  la commande ; la prestation du sous-traitant entre dans le coût du produit reçu.
- **L'historique est intact.** Une nomenclature corrigée aujourd'hui ne modifie pas le calcul des
  commandes passées.
- **Le statut n'est plus déclaratif.** Il est calculé ; il ne peut ni être oublié, ni être forcé.
- **Les achats sont rattachés à la commande** : on sait pour quoi on a acheté, et ce qui manque
  encore pour livrer.
- **Le pilotage est immédiat** : retards d'expédition et rythme de production visibles à l'entrée
  dans le programme.
- **Les prix restent confidentiels** : le rôle « opérateur de production » travaille sans voir ni
  prix ni montants.

## Résultat

> Bloc à compléter avec des valeurs mesurées chez le client — à défaut, supprimer les phrases chiffrées.

- Documents de production saisis manuellement par l'atelier : **{{avant}} → 0**.
- Délai entre l'expédition et la comptabilisation de la production : **{{avant}} → immédiat**.
- Temps de préparation d'une commande fournisseur à partir des besoins : **{{avant}} → {{après}}**.
- Écart entre stock théorique et stock réel de matières : **{{avant}} → {{après}}**.

## Pourquoi maERP (points forts)

1. **La production sans saisie de production** — la chaîne se documente depuis la vente.
2. **La commande comme axe unique** — besoins, achats, sous-traitance, production, expédition et
   paiement se lisent sur un seul document.
3. **Les nomenclatures versionnées** — le passé n'est jamais réécrit.
4. **Un poste de travail, pas une pile de formulaires** — la saisie se fait dans les lignes.
5. **Une solution éditeur, pas un développement spécifique** — le client reçoit le produit
   standard ; ce qui a été construit pour lui est livré à tous.
6. **Multilingue** — l'interface est disponible en français, anglais, espagnol et russe.

## Appel à l'action

Vous fabriquez sur commande et vos documents de production sont saisis en retard — ou pas saisis ?
Demandez une démonstration de maERP sur vos propres produits : nous partons de votre nomenclature
et de votre chaîne réelle.

**{{Bouton : Demander une démonstration}}** · **{{Bouton : Voir la fiche produit maERP}}**

---

## Partie méthodologique — organiser sa production dans maERP

À publier en encadré du cas, ou en article lié.

**1. Préparer les articles.** Les produits fabriqués portent le type « Produit fini » ou
« Produit semi-fini » et le mode de réapprovisionnement « Production » (ou « Les deux »). Les
matières restent en « Achat ». Ce réglage détermine ce qui sera proposé dans chaque colonne de
saisie, et où s'arrête le déroulement des nomenclatures.

**2. Saisir les nomenclatures.** Une nomenclature par produit fabriqué, quantité rapportée à une
unité de produit. Un semi-fini confié au sous-traitant est marqué comme tel : il reste une ligne
de besoin à part entière et n'est pas éclaté en ses composants.

**3. Choisir son schéma de production.** Trois schémas cohabitent :
   - **production automatique à l'expédition** — pour les ateliers sans ressource de saisie ;
   - **production saisie à l'avance**, ligne par ligne dans le poste de travail — pour produire
     sur stock ou par lots ;
   - **sous-traitance** — l'envoi produit le semi-fini, la réception le valorise.

**4. Travailler depuis le poste de production.** La commande se crée dans l'onglet « Produit »,
passe « en travail » par le bouton « Statut », puis tout le reste se saisit dans les onglets du
bas. Le rapport « Besoins de production » sert de liste d'achats.

**5. Lire les indicateurs.** L'étape et les cinq cercles remplacent les réunions de point :
ce qui est en retard est visible sans être déclaré.

---

## Annexe — captures d'écran à préparer

Prises sur le jeu de données de démonstration, **fenêtre 1C en plein écran uniquement**, chaque
capture accompagnée de sa propre légende. Un formulaire de document se photographie **onglet par
onglet** (« Principal » et chaque onglet de partie tabulaire), jamais en une seule image.

> **État au 2026-09-23.** Une première série a été prise pour l'article de la base de
> connaissances, mais **en russe** (`docs/kb/img/`, client lancé avec `/L ru`). Elle sert de
> repère pour le cadrage ; elle n'est pas utilisable ici. Les captures du cas se prennent avec
> le client lancé en français (`/L fr`), après avoir renommé l'organisation de la base de
> démonstration : elle s'appelle aujourd'hui « Drissotex », nom de la base d'un autre client, et
> il apparaît dans le titre de la fenêtre et sur le formulaire de commande.

| № | Capture | Légende |
|---|---|---|
| 1 | Tableau de bord, onglet « Production » | la vue d'entrée du dirigeant : indicateurs, rythme, graphiques |
| 2 | Indicateurs et bloc de rythme en gros plan | production du jour, série, retards d'expédition |
| 3 | Poste de production, onglet « Commandes » | la file des commandes avec étape et indicateur à cinq cercles |
| 4 | Gros plan sur la colonne « Indicateur » | la légende des cercles |
| 5 | Onglet « Produit », saisie d'une ligne | la commande se crée depuis le tableau |
| 6 | Onglet « Matières » | besoin, commandé, arrivé, manque |
| 7 | Onglet « Commandes fournisseur » | l'achat rattaché au besoin |
| 8 | Onglet « Réceptions » | numéro et date du bon fournisseur saisis dans la ligne |
| 9 | Onglet « Sous-traitance » | l'envoi chez le sous-traitant |
| 10 | Onglet « Réceptions de sous-traitance » | pertes et prestation du sous-traitant |
| 11 | Onglet « Production » | production automatique, colonne d'origine renseignée |
| 12 | Onglet « Expéditions » | la vente qui déclenche la production |
| 13 | Rapport « Besoins de production » | la liste d'achats par commande |
