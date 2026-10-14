import fs from 'node:fs';
import path from 'node:path';
import { describe, expect, it } from 'vitest';
import { FEATURE_CATEGORIES, FEATURE_CATEGORY, FEATURE_PAGES_BY_LOCALE } from './features-content';
import {
  LIBRARY_EPISODES,
  episodeText,
  episodeTranscript,
  libraryGroup,
  libraryGroups,
  libraryLabels,
  PAGE_EPISODES,
  adjacentEpisodes,
  fromPage,
  heroVideo,
  libraryIndex,
  relatedVideos,
  videoNav,
} from './videos-library';
import {
  TRAILER_EPISODE,
  VIDEO_LOCALES,
  episodeFromSlug,
  episodeSlug,
  roundMinutes,
  videoFiles,
  VIDEO_CDN_HOST,
  VIDEO_HOSTS,
  formatDuration,
  landingVideo,
  trailerLabels,
  videoEpisodes,
  videoHostFor,
} from './videos';

// Garde-fou du manifeste écrit par l'outil de publication: un épisode publié
// dans trois langues sur quatre laisserait une page avec un trou à la place de
// la vidéo, et personne ne le verrait avant un visiteur.

const NO_GAINS = [TRAILER_EPISODE, '41-e35'];
const LOCALES = Object.keys(FEATURE_PAGES_BY_LOCALE); // fr, en, es, ru — les langues du contenu

describe('landing videos manifest', () => {
  it('points at a Bunny CDN host', () => {
    expect(VIDEO_CDN_HOST).toMatch(/^vz-[a-z0-9-]+\.b-cdn\.net$/);
  });

  it('publishes the trailer', () => {
    expect(videoEpisodes()).toContain(TRAILER_EPISODE);
  });

  it.each(videoEpisodes())('episode %s exists in every content language', (episode) => {
    for (const locale of LOCALES) {
      const v = landingVideo(episode, locale);
      expect(v, `${episode}.${locale}`).toBeDefined();
      expect(v!.src).toMatch(new RegExp(`^https://${VIDEO_CDN_HOST}/[0-9a-f-]{36}/play_720p\\.mp4$`));
      expect(v!.poster.startsWith(`https://${VIDEO_CDN_HOST}/`)).toBe(true);
      // La règle de la série: 60 à 120 s par vidéo, dans chaque langue.
      expect(v!.duration, `${episode}.${locale} duration`).toBeGreaterThanOrEqual(60);
      expect(v!.duration, `${episode}.${locale} duration`).toBeLessThanOrEqual(120);
    }
  });

  it('offers no video and no section in Arabic', () => {
    expect(landingVideo(TRAILER_EPISODE, 'ar')).toBeUndefined();
    expect(trailerLabels('ar')).toBeUndefined();
  });

  it('labels the trailer section in every content language', () => {
    for (const locale of LOCALES) expect(trailerLabels(locale)?.title.trim()).toBeTruthy();
  });

  it('ships the series in the four content languages, not in Arabic', () => {
    expect([...VIDEO_LOCALES]).toEqual([...LOCALES].sort());
  });
  it('formats durations as m:ss', () => {
    expect(formatDuration(117)).toBe('1:57');
    expect(formatDuration(60)).toBe('1:00');
    expect(formatDuration(119.6)).toBe('2:00');
    expect(formatDuration(59.5)).toBe('1:00');
  });
});

// La vidéothèque: chaque vidéo publiée a sa page, ses textes, ses sous-titres,
// son affiche locale (aperçu OG) et sa transcription — sinon la page aurait un
// trou, ou un lien partagé sur WhatsApp n'aurait pas d'image.
const PUBLIC = path.resolve(__dirname, '../../public');

describe('video library', () => {
  it('describes every published episode', () => {
    for (const ep of videoEpisodes()) expect(LIBRARY_EPISODES, ep).toContain(ep);
  });

  it('keeps an episode that is described but not yet published out of the library', () => {
    for (const ep of LIBRARY_EPISODES.filter((e) => !videoEpisodes().includes(e))) {
      expect(libraryGroups('fr').flatMap((g) => g.items).some((i) => i.slug === episodeSlug(ep)), ep).toBe(false);
    }
  });

  it.each(videoEpisodes())('episode %s has text, captions, poster and transcript in every content language', (episode) => {
    for (const locale of LOCALES) {
      const t = episodeText(episode, locale);
      expect(t?.title.trim(), `${episode}.${locale} title`).toBeTruthy();
      expect(t?.lead.trim(), `${episode}.${locale} lead`).toBeTruthy();
      // Pas de carte «ce que vous y gagnez»: la bande-annonce, et E35 (feuille de
      // route) qui finit sur une question au spectateur.
      if (!NO_GAINS.includes(episode)) expect(t?.gains, `${episode}.${locale} gains`).toHaveLength(3);
      const files = videoFiles(episode, locale)!;
      const vtt = fs.readFileSync(path.join(PUBLIC, files.captions), 'utf8');
      expect(vtt.startsWith('WEBVTT'), `${files.captions}`).toBe(true);
      // la dernière réplique finit avant la fin de la vidéo
      const ends = [...vtt.matchAll(/--> (\d\d):(\d\d):(\d\d\.\d{3})/g)].map((m) => +m[1] * 3600 + +m[2] * 60 + +m[3]);
      expect(Math.max(...ends)).toBeLessThanOrEqual(landingVideo(episode, locale)!.duration + 1);
      expect(vtt).not.toMatch(/\{\w+\}/); // pas de repère de synchro oublié
      expect(fs.statSync(path.join(PUBLIC, files.image)).size, files.image).toBeGreaterThan(5000);
      const tr = episodeTranscript(episode, locale);
      expect(tr?.length, `${episode}.${locale} transcript`).toBeGreaterThan(0);
      expect(tr!.join(' ')).not.toMatch(/[{}]/);
    }
    expect(episodeText(episode, 'ar')).toBeUndefined();
  });

  it('files every episode in Découverte or in a feature category', () => {
    for (const ep of LIBRARY_EPISODES) {
      const g = libraryGroup(ep)!;
      expect(g === 'intro' || FEATURE_CATEGORIES.includes(g as never), `${ep} → ${g}`).toBe(true);
    }
  });

  it('shows every published episode somewhere in the library, in every content language', () => {
    for (const locale of LOCALES) {
      const shown = libraryGroups(locale).flatMap((g) => g.items.map((i) => i.slug));
      for (const ep of videoEpisodes()) expect(shown, `${ep}.${locale}`).toContain(episodeSlug(ep));
    }
  });

  it('gives each episode a stable short address, and keeps the old #e01 anchor', () => {
    expect(episodeSlug('01-e01')).toBe('e01');
    expect(episodeSlug(TRAILER_EPISODE)).toBe('trailer');
    for (const ep of videoEpisodes()) expect(episodeFromSlug(episodeSlug(ep))).toBe(ep);
    expect(episodeFromSlug('e99')).toBeUndefined();
  });

  it('groups the library with Découverte first, and has no menu, page or group in Arabic', () => {
    const groups = libraryGroups('fr');
    expect(groups[0].id).toBe('intro');
    expect(groups.every((g) => g.items.length > 0)).toBe(true);
    expect(groups.flatMap((g) => g.items).every((i) => i.poster && i.duration && i.href.startsWith('/fr/videos/'))).toBe(true);
    expect(libraryLabels('ar')).toBeUndefined();
    expect(videoNav('ar')).toBeUndefined();
    expect(libraryGroups('ar')).toEqual([]);
    for (const locale of LOCALES) expect(videoNav(locale)?.href).toBe(`/${locale}/videos`);
  });

  it('rounds the hero button to whole minutes', () => {
    expect(roundMinutes(117)).toBe(2);
    expect(roundMinutes(20)).toBe(1);
  });
});

describe('video host per landing domain', () => {
  it('falls back to the Bunny host off the landing domains and before a domain is verified', () => {
    expect(videoHostFor(undefined)).toBe(VIDEO_CDN_HOST);
    expect(videoHostFor('localhost:3400')).toBe(VIDEO_CDN_HOST);
    expect(videoHostFor('transport.tinycio.zz')).toBe(VIDEO_CDN_HOST);
  });

  it('serves each landing domain from its own verified video host, and lists it in the CSP set', () => {
    for (const host of VIDEO_HOSTS.filter((h) => h !== VIDEO_CDN_HOST)) {
      const tld = host.split('.').pop();
      expect(host).toBe(`video.tinycio.${tld}`);
      expect(videoHostFor(`transport.tinycio.${tld}`)).toBe(host);
      expect(landingVideo(TRAILER_EPISODE, 'fr', `transport.tinycio.${tld}`)!.src.startsWith(`https://${host}/`)).toBe(true);
    }
  });

  it('allows the Bunny host in the CSP set whatever else is live', () => {
    expect(VIDEO_HOSTS).toContain(VIDEO_CDN_HOST);
  });
});

describe('«Vidéos sur ce sujet» on the feature pages', () => {
  const PAGES = Object.keys(FEATURE_CATEGORY);

  it('features only episodes of the page’s own category', () => {
    for (const [slug, eps] of Object.entries(PAGE_EPISODES)) {
      expect(FEATURE_CATEGORY[slug], slug).toBeDefined();
      for (const ep of eps) expect(libraryGroup(ep), `${slug} → ${ep}`).toBe(FEATURE_CATEGORY[slug]);
    }
  });

  it.each(PAGES)('page %s: its screen’s episode on top, the rest of its category below', (slug) => {
    const category = FEATURE_CATEGORY[slug];
    for (const locale of LOCALES) {
      const published = LIBRARY_EPISODES.filter((ep) => libraryGroup(ep) === category && landingVideo(ep, locale));
      const hero = heroVideo(slug, locale);
      const r = relatedVideos(slug, locale);
      expect(hero === undefined, `${slug}.${locale} hero`).toBe(published.length === 0);
      if (!hero) continue;
      const screen = (PAGE_EPISODES[slug] ?? []).find((ep) => published.includes(ep));
      expect(hero.episode).toBe(screen ?? published[0]);
      // Page figée au build: affiche et sous-titres de notre origine.
      expect(hero.video.poster).toBe(videoFiles(hero.episode, locale)!.image);
      expect(hero.href).toBe(`/${locale}/videos/${episodeSlug(hero.episode)}?from=${slug}`);
      // Le bloc du bas ne répète pas la vidéo du haut.
      expect(r === undefined).toBe(published.length === 1);
      if (!r) continue;
      expect(r.items).toHaveLength(Math.min(6, published.length - 1));
      expect(r.items.map((i) => i.slug)).not.toContain(episodeSlug(hero.episode));
      expect(r.allHref).toBe(`/${locale}/videos#videos-${category}`);
      for (const item of r.items) {
        const ep = episodeFromSlug(item.slug)!;
        expect(libraryGroup(ep), `${slug} → ${ep}`).toBe(category);
        expect(item.poster).toBe(videoFiles(ep, locale)!.image);
        expect(item.href.endsWith(`?from=${slug}`)).toBe(true);
      }
    }
  });

  it('shows nothing in Arabic', () => {
    for (const slug of PAGES) {
      expect(relatedVideos(slug, 'ar')).toBeUndefined();
      expect(heroVideo(slug, 'ar')).toBeUndefined();
    }
  });
});

describe('episode page navigation', () => {
  it('walks the whole series in order, one step at a time', () => {
    for (const locale of LOCALES) {
      const order = libraryIndex(locale).flatMap((g) => g.items.map((i) => i.episode));
      const series = LIBRARY_EPISODES.filter((ep) => order.includes(ep));
      // L'index montre chaque épisode visible une fois.
      expect(new Set(order).size).toBe(order.length);
      expect([...order].sort()).toEqual([...series].sort());
      series.forEach((ep, i) => {
        expect(adjacentEpisodes(ep, locale), `${ep}.${locale}`).toEqual({ prev: series[i - 1], next: series[i + 1] });
      });
    }
  });

  it('gives every episode a short index label', () => {
    for (const locale of LOCALES)
      for (const g of libraryIndex(locale))
        for (const i of g.items) {
          expect(i.short.length, `${i.episode}.${locale}`).toBeGreaterThan(2);
          expect(i.short).not.toMatch(/^(Épisode|Episode|Episodio|Эпизод|Bande|Trailer|Tráiler|Трейлер)/);
        }
  });

  it('breadcrumbs back to a feature page only for real feature slugs', () => {
    expect(fromPage('tresorerie', 'fr')?.href).toBe('/fr/tresorerie');
    expect(fromPage('nope', 'fr')).toBeUndefined();
    expect(fromPage(undefined, 'fr')).toBeUndefined();
  });
});
