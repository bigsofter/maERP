# Cas client — Iso Froid : le comptoir qui vend sans scanner

Brouillon de la fiche cas pour le portail tinycio (section maERP → Point de vente).
Les cas ne sont pas des fichiers sur la landing : ils sont saisis dans le portail, la landing
les récupère par requête. Ce fichier contient le texte dans la structure de la fiche.

> **À confirmer avant publication**
> 1. **Raison sociale exacte et accord écrit du client.** `client_display` ne doit porter
>    « Iso Froid » qu'avec son accord ; sinon on publie une forme anonymisée
>    (« un distributeur de froid et climatisation à Tanger »). Le logo existe déjà côté landing
>    (`public/landing-v2/reviews/IsoFroid-logo.webp`).
> 2. **Le profil du client.** La landing décrit aujourd'hui Iso Froid par le multi-dépôts, le
>    stock en temps réel et l'inventaire mobile — pas par la caisse. Le propriétaire a confirmé
>    le 2026-09-24 qu'il y a bien un comptoir. À vérifier avant publication : combien de postes
>    de caisse, et qui les tient.
> 3. **Les chiffres du bloc « Résultat »** — aucune mesure relevée à ce jour. Les valeurs sont
>    laissées en `{{…}}` : soit elles sont mesurées chez le client, soit les phrases chiffrées
>    sont supprimées. **Ne rien publier de non mesuré.**
> 4. La **relecture linguistique** par un locuteur natif (cf. `docs/FRENCH-REVIEW.xlsx`).
> 5. Les **captures** restent à prendre (voir l'annexe), sur la version 2.0.15.57 ou ultérieure.

**Champs `kb_cases` :** `lang` = `fr` · `product_codes` = `["maerp"]` ·
`tags` = `froid, point-de-vente, caisse` · `cta_kind` = `consult` · `status` = `draft`.

---

## Le client

**Iso Froid**, Tanger, Maroc. Climatisation et froid : négoce et installation, plusieurs dépôts,
et un **comptoir** où les installateurs et les particuliers viennent chercher la pièce dont ils
ont besoin le jour même.

## Le défi

Un comptoir de pièces détachées ne ressemble pas à une caisse de supermarché.

Le catalogue compte des milliers de références, mais **la journée se joue sur quelques dizaines**
d'entre elles : gaz, raccords, filtres, colliers, la visserie courante. Ce sont justement les
articles qui se vendent le plus mal au scanner :

- **beaucoup n'ont pas de code-barres exploitable** — pièce nue, sachet reconditionné, article
  vendu à l'unité depuis une boîte ;
- **le code est illisible ou absent** sur les petites pièces, et le client attend devant le
  comptoir pendant que le vendeur cherche ;
- **passer par la recherche catalogue** oblige à taper un nom ou une référence pour un article
  que le vendeur vend vingt fois par jour — et à le refaire à chaque ligne du ticket.

Le résultat est toujours le même : la file s'allonge, et le vendeur finit par noter la vente sur
un papier pour la ressaisir « plus tard ». Ce qui est saisi plus tard n'est pas saisi du tout :
le stock décroche du réel, et c'est le stock qui fait vivre l'atelier.

## Ce que nous avons fait

Nous n'avons pas ajouté un mode de saisie rapide de plus. Nous avons donné au vendeur **sa propre
liste**, celle de ses articles à lui, et nous l'avons rendue accessible en un clic.

**1. Chaque caissier a ses favoris.** Les articles favoris sont attachés à l'utilisateur, pas au
poste ni à la société : deux vendeurs d'un même comptoir n'ont pas le même quotidien et n'ont pas
la même liste. Rien n'est à paramétrer par un administrateur.

**2. On met un article en favori pendant la vente, pas dans un écran de réglages.** Le vendeur
ajoute l'article au ticket une fois — au scanner, au code ou par la recherche — puis fait un
**clic droit sur la ligne** et choisit « Ajouter aux favoris ». La liste se construit toute seule,
à partir de ce qui se vend vraiment.

**3. Le bouton « Favoris » ouvre une grille de tuiles.** Chaque tuile porte **le nom de l'article
et son prix**, dans une fenêtre assez grande pour en afficher plusieurs dizaines. Le vendeur
reconnaît la tuile, il ne lit pas une ligne de tableau.

**4. Un clic vend.** Un clic sur la tuile ajoute l'article au ticket au prix affiché. Un deuxième
clic sur la même tuile **augmente la quantité** au lieu d'ouvrir une boîte de dialogue : trois
raccords, c'est trois clics, sans clavier.

**5. Le prix de la tuile est le prix du ticket.** La tuile affiche le prix du type de prix
appliqué au comptoir — le même que celui repris dans la vente. Un article sans prix est marqué
comme tel : il est visible, mais le vendeur sait avant de cliquer qu'il devra le renseigner.

**6. On retire un favori du bout de la souris.** Clic droit sur la tuile, « Retirer des
favoris ». La liste reste courte parce qu'elle coûte deux clics à nettoyer — et aucun bouton
supplémentaire n'a été ajouté à l'écran pour cela.

**7. L'écran a été rendu au travail.** La ligne de titre du poste de caisse a été supprimée :
sur un écran de comptoir, chaque ligne compte, et le nom du poste reste visible dans l'onglet.

## Les bénéfices

- **La vente se saisit pendant la vente**, pas le soir sur un carnet.
- **Le stock reste vrai** : ce qui sort du comptoir sort de la base au même moment.
- **Le vendeur n'a rien à apprendre** : il reconnaît un nom et un prix, il clique.
- **La liste s'adapte à la saison** sans intervention : on ajoute les articles de l'été, on retire
  ceux de l'hiver, en deux clics droits.
- **Aucun matériel supplémentaire** : ni scanner en plus, ni écran tactile obligatoire.

## Résultat

- Temps de saisie d'une ligne de comptoir : de {{avant}} à {{après}}.
- Part des tickets saisis au comptoir en temps réel : de {{avant}} à {{après}}.
- Articles couverts par les favoris : {{n}} références, soit {{part}} du chiffre du comptoir.

> Ces valeurs sont à mesurer chez le client avant publication. Aucune n'est publiée sans source.

## Pourquoi maERP

1. **La liste appartient au vendeur** — pas à un paramétrage central qu'il faut demander.
2. **Deux clics droits suffisent** à gérer la liste : rien n'occupe l'écran de vente.
3. **Nom et prix sur la tuile** — la reconnaissance visuelle remplace la lecture.
4. **Le deuxième clic compte** — la quantité s'incrémente sans dialogue.
5. **Une solution éditeur, pas un développement spécifique** — construit pour ce comptoir,
   livré à tous les clients de maERP.
6. **Multilingue** — l'interface est disponible en français, anglais, espagnol et russe.

## Appel à l'action

Votre comptoir vend des pièces qui n'ont pas de code-barres ? Demandez une démonstration de
maERP sur vos propres références : nous partons de votre catalogue et de vos prix.

**{{Bouton : Demander une démonstration}}** · **{{Bouton : Voir la fiche produit maERP}}**

---

## Partie méthodologique — mettre en place les favoris du comptoir

À publier en encadré du cas, ou en article lié.

**1. Rien à paramétrer.** Les favoris sont disponibles dès la mise à jour, pour tout utilisateur
qui a accès au poste de caisse. Chaque utilisateur constitue sa liste lui-même.

**2. Constituer la liste pendant une journée normale.** Plutôt que de dresser la liste à
l'avance, on laisse le comptoir la révéler : chaque fois qu'un article est cherché deux fois dans
la journée, clic droit sur sa ligne du ticket, « Ajouter aux favoris ».

**3. Garder la liste courte.** La fenêtre affiche les quarante premières tuiles et prévient quand
la liste dépasse ce seuil. Une liste de comptoir utile tient entre vingt et quarante références :
au-delà, la reconnaissance visuelle cesse de fonctionner et il vaut mieux retirer que compléter.

**4. Vérifier les prix.** Une tuile marquée « pas de prix » signale un article sans prix pour le
type de prix du comptoir : la vente sera refusée tant que le prix n'est pas renseigné. C'est un
bon détecteur de trous dans le tarif.

**5. Revoir la liste au changement de saison.** Clic droit, « Retirer des favoris » sur ce qui
ne tourne plus ; la place se libère pour la saison suivante.

---

## Annexe — captures d'écran à préparer

Prises sur le jeu de données de démonstration, **fenêtre 1C en plein écran uniquement**, chaque
capture accompagnée de sa propre légende. Client lancé en français (`/L fr`).

> **Attention** — l'organisation de la base de démonstration s'appelle aujourd'hui « Drissotex »,
> nom de la base d'un autre client, et elle apparaît à l'écran. La renommer avant toute capture.

| № | Capture | Légende |
|---|---|---|
| 1 | Poste de caisse, ticket en cours | le comptoir au travail, le bouton « Favoris » à côté de « Ajouter » |
| 2 | Clic droit sur une ligne du ticket | « Ajouter aux favoris » dans le menu contextuel |
| 3 | Fenêtre des favoris, grille complète | les tuiles avec nom et prix |
| 4 | Gros plan sur une tuile | le nom, le prix, la zone cliquable |
| 5 | Ticket après trois clics sur la même tuile | la quantité s'incrémente, une seule ligne |
| 6 | Clic droit sur une tuile | « Retirer des favoris » |
| 7 | Fenêtre des favoris vide | le message d'amorçage pour un nouveau caissier |
| 8 | Tuile d'un article sans prix | la mention « pas de prix » |
