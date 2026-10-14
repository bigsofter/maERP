// «Tout le produit en deux minutes» — la bande-annonce, juste après les
// problèmes: le visiteur vient de se reconnaître dans la douleur, c'est le
// moment où deux minutes de démonstration valent plus que six cartes de texte.
//
// Les épisodes vivent dans la vidéothèque (`/{locale}/videos`), pas ici: la
// section ne garde qu'un lien vers elle. L'épisode 1 a d'abord vécu sous la
// bande-annonce avec l'ancre `#e01`, et ces liens circulent — EpisodeHashRedirect
// les envoie sur la page de l'épisode.
//
// Absente quand la langue n'a pas de vidéo (l'arabe): même règle que le menu
// «fonctions» — voir videos.ts.

import { EpisodeHashRedirect } from './EpisodeHashRedirect';
import { VideoPlayer } from './VideoPlayer';
import { TRAILER_EPISODE, episodeSlug, formatDuration, landingVideo, trailerLabels, videoFiles } from './videos';
import { LIBRARY_EPISODES, episodeHref, libraryLabels } from './videos-library';

export function TrailerSection({ locale, host }: { locale: string; host: string }) {
  const video = landingVideo(TRAILER_EPISODE, locale, host);
  const t = trailerLabels(locale);
  const lib = libraryLabels(locale);
  if (!video || !t) return null;
  const files = videoFiles(TRAILER_EPISODE, locale);

  // `#e01` → `/fr/videos/e01`: seulement les épisodes publiés dans cette langue.
  const targets = Object.fromEntries(
    LIBRARY_EPISODES.filter((ep) => ep !== TRAILER_EPISODE && landingVideo(ep, locale)).map((ep) => [
      episodeSlug(ep),
      episodeHref(ep, locale),
    ]),
  );

  return (
    <section id="video" className="scroll-mt-[72px] bg-white px-4 pb-[84px] pt-[84px] sm:px-8">
      <EpisodeHashRedirect targets={targets} />
      <div className="mx-auto grid max-w-[1180px] items-center gap-8 lg:grid-cols-[1fr_1.6fr] lg:gap-12">
        <div>
          <span className="text-[11px] font-semibold uppercase tracking-[1.6px] text-route-700">{t.kicker}</span>
          <h2 className="mt-3 font-display text-[28px] font-semibold leading-[1.15] tracking-[-1px] text-slate-900 sm:text-4xl sm:tracking-[-1.2px]">
            {t.title}
          </h2>
          <p className="mt-4 text-[15px] leading-[1.7] text-slate-600">{t.lead}</p>
          <p className="mt-4 text-[12.5px] font-semibold tabular-nums text-slate-400">{formatDuration(video.duration)}</p>
          {lib && (
            <a
              href={`/${locale}/videos`}
              className="mt-6 inline-flex items-center gap-1.5 text-[14px] font-semibold text-route-700 no-underline hover:text-route-900"
            >
              {lib.allVideos} <span aria-hidden>→</span>
            </a>
          )}
        </div>
        <VideoPlayer
          video={video}
          label={t.aria}
          captions={files && lib ? { src: files.captions, srcLang: locale, label: lib.captions } : undefined}
        />
      </div>
    </section>
  );
}
