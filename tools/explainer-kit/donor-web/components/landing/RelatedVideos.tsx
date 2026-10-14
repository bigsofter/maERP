import type { RelatedVideos as Related } from './videos-library';
import { VideoCard } from './VideoCard';

// «Vidéos sur ce sujet» sous une page «fonctions»: les épisodes de sa catégorie,
// rendus côté serveur avec la carte de la vidéothèque. Rien quand la catégorie
// n'a pas d'épisode publié dans la langue (et jamais en arabe).

export function RelatedVideos({ related }: { related: Related | undefined }) {
  if (!related) return null;
  return (
    <section className="mx-auto max-w-[1180px] px-4 pt-14 sm:px-8">
      <div className="flex flex-wrap items-baseline justify-between gap-3">
        <h2 className="font-display text-[22px] font-semibold leading-[1.25] tracking-[-0.4px] text-slate-900 sm:text-[26px]">
          {related.title}
        </h2>
        <a href={related.allHref} className="text-[13px] font-semibold text-route-700 no-underline hover:text-route-900">
          {related.all} →
        </a>
      </div>
      <div className="mt-6 grid gap-2.5 sm:grid-cols-2 xl:grid-cols-3">
        {related.items.map((item) => (
          <VideoCard key={item.href} item={item} />
        ))}
      </div>
    </section>
  );
}
