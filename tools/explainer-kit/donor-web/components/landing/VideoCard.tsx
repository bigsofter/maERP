// Carte d'un épisode vidéo — affiche, durée, kicker, titre-question, «ce que
// vous verrez». Partagée par la vidéothèque (FeatureExplorer, composant client)
// et le bloc «Vidéos sur ce sujet» des pages «fonctions» (rendu serveur): pas
// d'état, pas de hook, elle se rend des deux côtés.

import type { ExplorerItem } from './FeatureExplorer';

export function VideoCard({ item: f }: { item: ExplorerItem }) {
  return (
    <a
      href={f.href}
      className="group flex flex-col overflow-hidden rounded-lg border border-line bg-white no-underline transition-all duration-200 hover:-translate-y-[2px] hover:border-route-300 hover:shadow-2"
    >
      <span className="relative block aspect-video bg-slate-900">
        {/* eslint-disable-next-line @next/next/no-img-element -- affiche Bunny ou locale, pas d'optimiseur d'images ici */}
        <img src={f.poster} alt="" loading="lazy" className="h-full w-full object-cover" />
        <span className="absolute inset-0 flex items-center justify-center" aria-hidden>
          <span className="flex h-11 w-11 items-center justify-center rounded-pill bg-white/90 text-route-700 shadow-2 transition-transform duration-200 group-hover:scale-110">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M8 5.5v13l11-6.5z" />
            </svg>
          </span>
        </span>
        {f.duration && (
          <span className="absolute bottom-2 end-2 rounded-[6px] bg-slate-900/80 px-1.5 py-0.5 text-[11px] font-semibold tabular-nums text-white">
            {f.duration}
          </span>
        )}
      </span>
      <span className="flex flex-1 flex-col gap-1.5 p-4">
        <span className="text-[11px] font-semibold uppercase tracking-[1px] text-route-700">{f.label}</span>
        <span className="font-display text-[14.5px] font-semibold leading-[1.35] text-slate-900">{f.title}</span>
        {f.lead && <span className="text-[12px] leading-[1.5] text-slate-500">{f.lead}</span>}
      </span>
    </a>
  );
}
