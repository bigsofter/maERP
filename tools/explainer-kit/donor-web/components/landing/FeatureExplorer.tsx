'use client';

// Section «fonctions» de l'accueil — les pages de fonctions, classées.
//
// Remplace la grille à plat qui vivait sous la vitrine des modules: dix cartes
// se lisaient encore, mais la série de vidéos en annonce une page par épisode,
// et une grille de quarante cartes ne se lit pas, elle se fait défiler. D'où le
// classement par espace de travail (les mêmes mots que la barre latérale du
// portail — voir FEATURE_CATEGORIES) et un filtre au-dessus.
//
// Deux choses tenues volontairement:
//
//   • TOUTES les cartes sont dans le HTML servi. L'état par défaut est «tout»,
//     le filtre ne fait que masquer: Google suit chaque lien, et un navigateur
//     sans JavaScript voit le classement complet — il perd les puces, pas le
//     contenu. Chaque groupe porte une ancre (`#fonctions-finance`), c'est par
//     elle que le menu du haut mène à une catégorie.
//   • Les groupes arrivent en PROPS, déjà résolus par le serveur (même règle
//     que LandingNav): importer `features-content` ici enverrait dix pages ×
//     quatre langues dans le bundle du navigateur.
//
// La vidéothèque (`/{locale}/videos`) réutilise le composant tel quel: mêmes
// catégories, mêmes puces, mêmes ancres. Une carte qui porte une affiche
// (`poster`) devient une carte vidéo — l'image et la durée remplacent l'icône.

import { useState } from 'react';
import { Icon, pageIcon } from './icons';
import { VideoCard } from './VideoCard';

export interface ExplorerItem {
  href: string;
  slug: string;
  label: string;
  title: string;
  /** Carte vidéo: une phrase «ce que vous verrez». */
  lead?: string;
  /** Carte vidéo: l'affiche (Bunny) — sa présence fait la carte vidéo. */
  poster?: string;
  /** Carte vidéo: «1:54». */
  duration?: string;
}

export interface ExplorerGroup {
  id: string;
  label: string;
  hint: string;
  /** «Dans le portail : Finance» — le nom que le client lira dans le produit. */
  portal?: string;
  items: readonly ExplorerItem[];
}

export function FeatureExplorer({
  anchor,
  kicker,
  title,
  all,
  groups,
  lead,
  asPageTitle,
}: {
  /** Id de la section; les groupes portent `${anchor}-${group.id}`. */
  anchor: string;
  kicker: string;
  title: string;
  /** Libellé de la puce «tout afficher». */
  all: string;
  groups: readonly ExplorerGroup[];
  /** Une phrase sous le titre (vidéothèque). */
  lead?: string;
  /** Le titre de la section est le titre de la page (`h1`) — vidéothèque. */
  asPageTitle?: boolean;
}) {
  const [active, setActive] = useState<string | null>(null);
  const shown = active ? groups.filter((g) => g.id === active) : groups;
  const total = groups.reduce((n, g) => n + g.items.length, 0);
  const Heading = asPageTitle ? 'h1' : 'h2';

  const chip = (id: string | null, label: string, count: number) => {
    const on = active === id;
    return (
      <button
        key={id ?? 'all'}
        type="button"
        aria-pressed={on}
        onClick={() => setActive(id)}
        className={`inline-flex h-9 items-center gap-2 rounded-pill border px-4 text-[13px] font-medium transition-colors ${
          on
            ? 'border-route-700 bg-route-700 text-white'
            : 'border-line bg-white text-slate-600 hover:border-route-300 hover:text-slate-900'
        }`}
      >
        {label}
        <span className={`text-[11px] font-semibold tabular-nums ${on ? 'text-route-200' : 'text-slate-400'}`}>
          {count}
        </span>
      </button>
    );
  };

  return (
    <section id={anchor} className="scroll-mt-[72px] bg-bg px-4 pb-[84px] pt-[84px] sm:px-8">
      <div className="mx-auto max-w-[1180px]">
        <span className="text-[11px] font-semibold uppercase tracking-[1.6px] text-route-700">{kicker}</span>
        <Heading className="mt-3 max-w-[620px] font-display text-[28px] font-semibold leading-[1.15] tracking-[-1px] text-slate-900 sm:text-4xl sm:tracking-[-1.2px]">
          {title}
        </Heading>
        {lead && <p className="mt-4 max-w-[620px] text-[15px] leading-[1.7] text-slate-600">{lead}</p>}

        {/* Une seule catégorie: le filtre n'aurait rien à filtrer. */}
        {groups.length > 1 && (
          <div role="group" aria-label={title} className="mt-7 flex flex-wrap gap-2">
            {chip(null, all, total)}
            {groups.map((g) => chip(g.id, g.label, g.items.length))}
          </div>
        )}

        <div className="mt-8 flex flex-col gap-9">
          {shown.map((g) => (
            <div
              key={g.id}
              id={`${anchor}-${g.id}`}
              className="grid scroll-mt-[72px] items-start gap-4 border-t border-line pt-6 lg:grid-cols-[220px_1fr] lg:gap-8"
            >
              <div>
                <h3 className="font-display text-[19px] font-semibold tracking-[-0.4px] text-slate-900">{g.label}</h3>
                <p className="mt-1.5 text-[12.5px] leading-[1.6] text-slate-500">{g.hint}</p>
                {g.portal && <p className="mt-2 text-[11px] text-slate-400">{g.portal}</p>}
              </div>
              <div className="mt-stagger grid gap-2.5 sm:grid-cols-2 xl:grid-cols-3">
                {g.items.map((f) =>
                  f.poster ? (
                    <VideoCard key={f.href} item={f} />
                  ) : (
                    <a
                      key={f.href}
                      href={f.href}
                      className="group flex flex-col gap-1.5 rounded-lg border border-line bg-white p-4 no-underline transition-all duration-200 hover:-translate-y-[2px] hover:border-route-300 hover:shadow-2"
                    >
                      <span className="inline-flex h-8 w-8 items-center justify-center rounded-[9px] bg-route-50 text-route-700" aria-hidden>
                        <Icon name={pageIcon(f.slug)} className="h-[17px] w-[17px]" />
                      </span>
                      <span className="font-display text-[14px] font-semibold text-slate-900">{f.label}</span>
                      <span className="flex-1 text-[12px] leading-[1.5] text-slate-500">{f.title}</span>
                      <span className="text-[12px] font-semibold text-route-700" aria-hidden>
                        →
                      </span>
                    </a>
                  ),
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
