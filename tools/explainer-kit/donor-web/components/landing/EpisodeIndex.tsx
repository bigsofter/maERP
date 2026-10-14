// Index de la série sur la page d'un épisode — les groupes de la vidéothèque,
// un épisode par ligne en libellé court. Sur grand écran il flotte à gauche
// (sticky, défile seul); sur mobile il se replie sous l'épisode. Composant
// SERVEUR: des `<details>` natifs, le groupe courant ouvert — zéro JavaScript.

import type { IndexGroup } from './videos-library';

export function EpisodeIndex({
  groups,
  current,
  title,
  allHref,
}: {
  groups: readonly IndexGroup[];
  current: string;
  /** «Toutes les vidéos» — titre de l'index et lien vers la vidéothèque. */
  title: string;
  allHref: string;
}) {
  return (
    <nav aria-label={title} className="text-[13px]">
      <a
        href={allHref}
        className="block px-2 pb-2 text-[11px] font-semibold uppercase tracking-[1.4px] text-slate-400 no-underline hover:text-route-700"
      >
        {title}
      </a>
      {groups.map((g) => {
        const open = g.items.some((i) => i.episode === current);
        return (
          <details key={g.id} open={open} className="group border-t border-line-soft py-1">
            <summary className="flex cursor-pointer list-none items-center justify-between gap-2 rounded-[8px] px-2 py-1.5 font-semibold text-slate-700 hover:bg-white">
              <span>{g.label}</span>
              <span className="text-[11px] font-medium tabular-nums text-slate-400">{g.items.length}</span>
            </summary>
            <ul className="mb-1 mt-0.5 flex flex-col">
              {g.items.map((i) => {
                const here = i.episode === current;
                return (
                  <li key={i.episode}>
                    <a
                      href={i.href}
                      aria-current={here ? 'page' : undefined}
                      className={`block rounded-[8px] px-2 py-1.5 leading-[1.35] no-underline ${
                        here ? 'bg-route-50 text-route-700' : 'text-slate-600 hover:bg-white hover:text-slate-900'
                      }`}
                    >
                      <span className="block text-[10.5px] font-semibold uppercase tracking-[0.8px] opacity-70">{i.kicker}</span>
                      <span className={`block first-letter:uppercase ${here ? 'font-semibold' : ''}`}>{i.short}</span>
                    </a>
                  </li>
                );
              })}
            </ul>
          </details>
        );
      })}
    </nav>
  );
}
