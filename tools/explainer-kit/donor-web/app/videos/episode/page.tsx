import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { headers } from 'next/headers';
import { setRequestLocale } from 'next-intl/server';
import { routing } from '@/i18n/routing';
import { LandingNav } from '@/components/landing/LandingNav';
import { LandingFooter } from '@/components/landing/LandingFooter';
import { CtaBand } from '@/components/landing/CtaBand';
import { VideoPlayer } from '@/components/landing/VideoPlayer';
import { featureNav } from '@/components/landing/features-content';
import { landingHost, workspaceBase } from '@/components/landing/feature-route';
import {
  VIDEO_LOCALES,
  episodeFromSlug,
  formatDuration,
  landingVideo,
  videoFiles,
  videoUploaded,
} from '@/components/landing/videos';
import {
  adjacentEpisodes,
  episodeHref,
  episodeShort,
  episodeText,
  episodeTranscript,
  fromPage,
  libraryGroup,
  libraryIndex,
  libraryLabels,
  trialCta,
  videoNav,
} from '@/components/landing/videos-library';
import { EpisodeIndex } from '@/components/landing/EpisodeIndex';
import '@/components/landing/landing.css';

// Page d'un épisode — l'adresse qu'on envoie (WhatsApp, e-mail):
// `transport.tinycio.ma/fr/videos/e01`. Une page et pas une ancre, parce
// qu'une ancre partage l'aperçu de toute la page: ici l'aperçu OG est l'affiche
// de CET épisode (copie locale — Bunny refuse les robots, voir videos.ts), et
// le JSON-LD `VideoObject` décrit CETTE vidéo.
//
// Contenu: le fil d'Ariane, le lecteur (avec sous-titres), l'épisode précédent
// et le suivant dans l'ordre de la série, «ce que vous y gagnez» repris de la
// carte finale de la vidéo, la transcription repliée, l'essai 14 jours; à
// gauche, l'index de la série qui flotte (sous l'épisode sur mobile).
//
// Fil d'Ariane: Accueil › Vidéos › catégorie › épisode — ou, arrivé d'une page
// «fonctions» (`?from=tresorerie`, posé par ses liens), Accueil › Trésorerie ›
// épisode: le retour mène là d'où l'on vient. Le paramètre ne change ni
// l'URL canonique ni le contenu.
// Rendu dynamique pour la même raison que la vidéothèque (hôte vidéo par
// domaine). Épisode inconnu, pas publié dans cette langue, ou arabe: 404.

type Params = Promise<{ locale: string; episode: string }>;

async function resolve(params: Params) {
  const { locale, episode: slug } = await params;
  const episode = episodeFromSlug(slug);
  const lib = libraryLabels(locale);
  const text = episode ? episodeText(episode, locale) : undefined;
  if (!episode || !lib || !text || !landingVideo(episode, locale)) return undefined;
  const host = (await headers()).get('host') ?? 'transport.tinycio.ma';
  return { locale, slug, episode, lib, text, host, base: `https://${landingHost(host)}` };
}

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const r = await resolve(params);
  if (!r) return {};
  const { locale, slug, episode, text, base } = r;
  const path = `/videos/${slug}`;
  const languages = Object.fromEntries(
    VIDEO_LOCALES.filter((l) => episodeText(episode, l) && landingVideo(episode, l)).map((l) => [l, `${base}/${l}${path}`]),
  );
  const image = `${base}${videoFiles(episode, locale)!.image}`;
  const title = `${text.title} · maTransports`;
  return {
    title,
    description: text.lead,
    alternates: {
      canonical: `${base}/${locale}${path}`,
      languages: { ...languages, 'x-default': `${base}/${routing.defaultLocale}${path}` },
    },
    openGraph: {
      type: 'video.other',
      siteName: 'maTransports',
      title: text.title,
      description: text.lead,
      url: `${base}/${locale}${path}`,
      locale,
      images: [{ url: image, width: 1920, height: 1080, alt: text.title }],
    },
    twitter: { card: 'summary_large_image', title: text.title, description: text.lead, images: [image] },
  };
}

/** 114 → «PT1M54S» (ISO 8601), la durée du JSON-LD. */
function isoDuration(seconds: number): string {
  const s = Math.round(seconds);
  return `PT${Math.floor(s / 60)}M${s % 60}S`;
}

export default async function EpisodePage({
  params,
  searchParams,
}: {
  params: Params;
  searchParams: Promise<{ from?: string | string[] }>;
}) {
  const r = await resolve(params);
  if (!r) notFound();
  const { locale, slug, episode, lib, text, host, base } = r;
  setRequestLocale(locale);
  const video = landingVideo(episode, locale, host)!;
  const files = videoFiles(episode, locale)!;
  const transcript = episodeTranscript(episode, locale);
  const wsBase = workspaceBase(host);
  const signupHref = `${wsBase}/${locale}/signup`;
  const nav = featureNav(locale);
  const group = libraryGroup(episode);
  const uploaded = videoUploaded(episode, locale);
  const from = (await searchParams).from;
  const origin = fromPage(typeof from === 'string' ? from : undefined, locale);
  const index = libraryIndex(locale);
  const groupLabel = index.find((g) => g.id === group)?.label;
  const { prev, next } = adjacentEpisodes(episode, locale);
  const crumbs = [
    { href: `/${locale}`, label: lib.home },
    ...(origin
      ? [origin]
      : [
          { href: `/${locale}/videos`, label: lib.nav },
          ...(groupLabel ? [{ href: `/${locale}/videos#videos-${group}`, label: groupLabel }] : []),
        ]),
  ];
  const step = (ep: string | undefined, label: string, dir: 'prev' | 'next') => {
    const t = ep ? episodeText(ep, locale) : undefined;
    if (!ep || !t) return <span />;
    return (
      <a
        href={episodeHref(ep, locale)}
        rel={dir}
        className={`group flex flex-col gap-1 rounded-lg border border-line bg-white px-4 py-3 no-underline transition-colors hover:border-route-300 ${
          dir === 'next' ? 'text-end' : ''
        }`}
      >
        <span className="text-[11px] font-semibold uppercase tracking-[1px] text-slate-400">
          {dir === 'prev' && <span aria-hidden className="rtl:rotate-180">← </span>}
          {label}
          {dir === 'next' && <span aria-hidden className="rtl:rotate-180"> →</span>}
        </span>
        <span className="text-[13.5px] font-semibold leading-[1.35] text-slate-900 group-hover:text-route-700">
          {t.kicker} · {episodeShort(t)}
        </span>
      </a>
    );
  };

  const ld = {
    '@context': 'https://schema.org',
    '@type': 'VideoObject',
    name: text.title,
    description: text.lead,
    thumbnailUrl: [`${base}${files.image}`],
    ...(uploaded ? { uploadDate: uploaded } : {}),
    duration: isoDuration(video.duration),
    inLanguage: locale,
    url: `${base}/${locale}/videos/${slug}`,
    // Le MP4 Bunny exige un referrer autorisé: un robot sans referrer reçoit
    // 403. On le déclare quand même — c'est la vraie adresse de la vidéo.
    contentUrl: video.src,
    ...(transcript ? { transcript: { '@type': 'CreativeWork', text: transcript.join('\n') } } : {}),
    publisher: { '@type': 'Organization', name: 'maTransports' },
  };

  return (
    <div className="min-h-screen overflow-x-clip bg-bg text-slate-900">
      <script
        type="application/ld+json"
        // `<` échappé: une transcription contenant «</script>» fermerait la balise.
        dangerouslySetInnerHTML={{ __html: JSON.stringify(ld).replace(/</g, '\\u003c') }}
      />
      <LandingNav
        loginHref={`${wsBase}/${locale}/login`}
        signupHref={signupHref}
        anchorBase={`/${locale}`}
        features={nav?.items}
        featuresLabel={nav?.label}
        videos={videoNav(locale)}
      />
      <main className="px-4 pb-[72px] pt-8 sm:px-8 sm:pt-10">
        <div className="mx-auto grid max-w-[1244px] gap-10 lg:grid-cols-[250px_minmax(0,1fr)]">
          <aside className="hidden lg:block">
            <div className="sticky top-[76px] max-h-[calc(100vh-96px)] overflow-y-auto pe-2">
              <EpisodeIndex groups={index} current={episode} title={lib.allVideos} allHref={`/${locale}/videos`} />
            </div>
          </aside>
        <div className="min-w-0 max-w-[980px]">
          <nav aria-label="breadcrumb">
            <ol className="flex flex-wrap items-center gap-x-1.5 gap-y-1 text-[13px] text-slate-500">
              {crumbs.map((c) => (
                <li key={c.href} className="flex items-center gap-1.5">
                  <a href={c.href} className="font-medium text-slate-500 no-underline hover:text-route-700">
                    {c.label}
                  </a>
                  <span aria-hidden className="text-slate-300 rtl:rotate-180">
                    ›
                  </span>
                </li>
              ))}
              <li aria-current="page" className="font-medium text-slate-700">
                {text.kicker}
              </li>
            </ol>
          </nav>
          <span className="mt-6 block text-[11px] font-semibold uppercase tracking-[1.6px] text-route-700">
            {text.kicker} · <span className="tabular-nums">{formatDuration(video.duration)}</span>
          </span>
          <h1 className="mt-3 font-display text-[28px] font-semibold leading-[1.15] tracking-[-1px] text-slate-900 sm:text-[40px] sm:tracking-[-1.3px]">
            {text.title}
          </h1>
          <p className="mt-4 max-w-[720px] text-[15px] leading-[1.7] text-slate-600 sm:text-base">{text.lead}</p>

          <div className="mt-8">
            <VideoPlayer
              video={video}
              label={text.aria}
              captions={{ src: files.captions, srcLang: locale, label: lib.captions }}
            />
          </div>

          {(prev || next) && (
            <div className="mt-5 grid gap-3 sm:grid-cols-2">
              {step(prev, lib.prev, 'prev')}
              {step(next, lib.next, 'next')}
            </div>
          )}

          <div className="mt-10 grid gap-8 lg:grid-cols-[1fr_auto] lg:items-start">
            {text.gains && (
              <section>
                <h2 className="font-display text-[20px] font-semibold tracking-[-0.4px] text-slate-900">{lib.gains}</h2>
                <ul className="mt-4 flex flex-col gap-3">
                  {text.gains.map((g) => (
                    <li key={g} className="flex gap-3 text-[15px] leading-[1.6] text-slate-700">
                      <span className="mt-[9px] h-1.5 w-1.5 flex-none rounded-pill bg-amber-500" aria-hidden />
                      {g}
                    </li>
                  ))}
                </ul>
              </section>
            )}
            <a
              href={signupHref}
              className="inline-flex h-12 items-center gap-2 self-start justify-self-start rounded-pill bg-grad-amber px-6 text-sm font-semibold text-slate-900 no-underline shadow-amber hover:brightness-105"
            >
              {trialCta(locale)} <span aria-hidden>→</span>
            </a>
          </div>

          {transcript && (
            <details className="group mt-10 rounded-lg border border-line bg-white">
              <summary className="flex cursor-pointer list-none items-center justify-between gap-3 px-5 py-4 font-display text-[15px] font-semibold text-slate-900">
                {lib.transcript}
                <svg
                  width="14"
                  height="14"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2.4"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  className="text-slate-400 transition-transform group-open:rotate-180"
                  aria-hidden
                >
                  <polyline points="6 9 12 15 18 9" />
                </svg>
              </summary>
              <div className="flex flex-col gap-3 border-t border-line-soft px-5 pb-5 pt-4 text-[14px] leading-[1.7] text-slate-600">
                {transcript.map((p, i) => (
                  <p key={i}>{p}</p>
                ))}
              </div>
            </details>
          )}

          <div className="mt-10 rounded-lg border border-line bg-white p-3 lg:hidden">
            <EpisodeIndex groups={index} current={episode} title={lib.allVideos} allHref={`/${locale}/videos`} />
          </div>
        </div>
        </div>
      </main>
      <CtaBand signupHref={signupHref} />
      <LandingFooter locale={locale} ldHost={landingHost(host)} />
    </div>
  );
}
