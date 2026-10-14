import type { MetadataRoute } from 'next';
import { routing } from '@/i18n/routing';
import { PAGES_FR } from '@/components/landing/features-content';
import { VIDEO_LOCALES, episodeSlug, landingVideo } from '@/components/landing/videos';
import { LIBRARY_EPISODES, episodeText } from '@/components/landing/videos-library';

// Landing sitemap — one entry per locale with hreflang alternates. Metadata
// routes are static per deployment, so the canonical landing origin comes
// from the env (each market's deployment sets its own transport.tinycio.{tld});
// the .ma launch market is the default.
const BASE = process.env.NEXT_PUBLIC_LANDING_ORIGIN ?? 'https://transport.tinycio.ma';

// Les pages publiques hors accueil. Elles sont rédigées en français, mais
// existent sous chaque préfixe de locale (voir feature-route.tsx) — donc
// hreflang complet, et priorité plus basse que l'accueil.
// Les slugs ne sont pas traduits (voir features-content.ts): n'importe quelle
// langue donne la même liste, le français sert de référence.
const PUBLIC_PATHS = [...PAGES_FR.map((f) => f.slug), 'integrations'];

export default function sitemap(): MetadataRoute.Sitemap {
  const home = routing.locales.map((locale) => ({
    url: `${BASE}/${locale}`,
    lastModified: new Date(),
    changeFrequency: 'weekly' as const,
    priority: locale === routing.defaultLocale ? 1 : 0.8,
    alternates: {
      languages: Object.fromEntries(routing.locales.map((l) => [l, `${BASE}/${l}`])),
    },
  }));

  const pages = PUBLIC_PATHS.flatMap((path) =>
    routing.locales.map((locale) => ({
      url: `${BASE}/${locale}/${path}`,
      lastModified: new Date(),
      changeFrequency: 'monthly' as const,
      priority: locale === routing.defaultLocale ? 0.8 : 0.6,
      alternates: {
        languages: Object.fromEntries(routing.locales.map((l) => [l, `${BASE}/${l}/${path}`])),
      },
    })),
  );

  // La vidéothèque et ses épisodes n'existent que dans les langues de la série
  // (pas d'arabe — /ar/videos est un 404): hreflang limité à ces langues.
  const videoPaths = [
    'videos',
    ...LIBRARY_EPISODES.filter((ep) => VIDEO_LOCALES.some((l) => landingVideo(ep, l) && episodeText(ep, l))).map(
      (ep) => `videos/${episodeSlug(ep)}`,
    ),
  ];
  const videos = videoPaths.flatMap((path) => {
    const ep = LIBRARY_EPISODES.find((e) => path === `videos/${episodeSlug(e)}`);
    const locales = VIDEO_LOCALES.filter((l) => !ep || (landingVideo(ep, l) && episodeText(ep, l)));
    return locales.map((locale) => ({
      url: `${BASE}/${locale}/${path}`,
      lastModified: new Date(),
      changeFrequency: 'monthly' as const,
      priority: locale === routing.defaultLocale ? 0.7 : 0.5,
      alternates: {
        languages: Object.fromEntries(locales.map((l) => [l, `${BASE}/${l}/${path}`])),
      },
    }));
  });

  return [...home, ...pages, ...videos];
}
