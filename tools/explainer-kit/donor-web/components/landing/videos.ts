// Vidéos explicatives du landing — où elles sont et comment une page en obtient une.
//
// Les fichiers vivent chez Bunny Stream (bibliothèque `matransports-explainers`),
// pas dans le dépôt ni sur le serveur de l'application: une vidéo servie par la
// machine du portail prend sa bande passante au portail. `videos.json` est écrit
// par l'outil de publication de la série, après le rendu: il téléverse les MP4,
// attend l'encodage et recopie ici guid et durée mesurée (ffprobe). L'outil vit
// avec la chaîne de production des vidéos, HORS dépôt
// (`tmp/explainer/series/tools/publish.mjs`, dossier non suivi) — ne le cherchez
// pas sous `tools/`. On n'édite donc pas ce fichier à la main: une durée tapée
// à la main est une durée que personne n'a comparée au fichier.
//
// SOUS-TITRES ET AFFICHES LOCALES. L'outil de la série (`web_assets.mjs`, lancé
// par `publish.mjs`) tire de la voix CORRIGÉE et de son minutage un WebVTT par
// langue, et recopie l'affiche Bunny dans `public/videos/<slug>/<lang>.{vtt,jpg}`.
// Le WebVTT est servi par notre origine: une piste `<track>` d'une autre origine
// exigerait CORS chez Bunny et `crossorigin` sur la vidéo. L'affiche locale sert
// à l'aperçu OG (WhatsApp) et au JSON-LD: Bunny répond 403 à toute requête sans
// referrer autorisé, et un robot n'en envoie pas. Le test vérifie que chaque
// vidéo publiée a ses deux fichiers.
//
// UNE VIDÉO PAR LANGUE. La voix et les titres à l'écran changent: ce ne sont pas
// des sous-titres sur une même image. Les épisodes existent en fr / en / es / ru;
// l'arabe n'en a pas, et la règle est celle des pages «fonctions»: on ne propose
// pas à un lecteur un contenu dans une langue qu'il n'a pas choisie — `landingVideo`
// renvoie `undefined` et la section disparaît.
//
// LECTURE. Un `<video>` natif sur le MP4 720p, `preload="none"`: tant que le
// visiteur n'a pas cliqué, la page ne télécharge que l'affiche. Pas de lecteur
// tiers, pas de script — le budget du landing est LCP ≤ 2 s en 4G marocaine, et
// 720p à ~0,7 Mbit/s passe sur cette 4G-là. Le flux adaptatif (playlist.m3u8)
// existe côté Bunny; le brancher demanderait hls.js partout sauf Safari.
//
// DEUX VERROUS À CONNAÎTRE avant de s'étonner d'un écran noir:
//   • la CSP (middleware.ts) n'autorise en `media-src` que VIDEO_CDN_HOST;
//   • Bunny ne sert les fichiers qu'aux pages des hôtes déclarés dans la
//     bibliothèque (referrers autorisés: transport.tinycio.{ma,com,es,ru},
//     localhost). Un nouvel hôte du landing s'ajoute LÀ-BAS aussi, sinon 403.
//
// DOMAINE. Chaque landing sert ses vidéos depuis son propre domaine:
// transport.tinycio.ma → video.tinycio.ma, et ainsi de suite. Le visiteur ne voit
// pas passer un domaine tiers, et le jour où l'on change de CDN, on repointe un
// CNAME au lieu de republier chaque page. Un domaine n'entre dans `customHosts`
// que vérifié de bout en bout (DNS, certificat, un vrai 206 sur un MP4) par
// l'outil de la série `video_hosts.mjs`; tant qu'il n'y est pas — DNS pas encore
// posé chez le registraire, hôte de dev, tunnel — on sert depuis l'hôte Bunny.
// La page ne pointe donc jamais vers un nom qui ne répond pas encore.

import manifest from './videos.json';

/** L'hôte Bunny de la bibliothèque — toujours valide, c'est le repli. */
export const VIDEO_CDN_HOST: string = manifest.cdnHost;

/** TLD du landing → domaine vidéo vérifié (`ma` → `video.tinycio.ma`). */
const CUSTOM_HOSTS: Record<string, string> = (manifest as { customHosts?: Record<string, string> }).customHosts ?? {};

/** Tous les hôtes d'où une vidéo peut venir — pour la CSP (`media-src`). */
export const VIDEO_HOSTS: readonly string[] = [VIDEO_CDN_HOST, ...Object.values(CUSTOM_HOSTS)];

/** Hôte vidéo pour la page servie sur `pageHost` (en-tête Host, port compris). */
export function videoHostFor(pageHost: string | undefined): string {
  const m = /^(?:my\.)?transport\.tinycio\.([a-z]+)$/.exec((pageHost ?? '').split(':')[0]);
  return (m && CUSTOM_HOSTS[m[1]]) || VIDEO_CDN_HOST;
}

export interface LandingVideo {
  /** MP4 progressif 720p — la source du `<video>`. */
  src: string;
  /** Image d'attente générée par Bunny. */
  poster: string;
  /** Durée en secondes. */
  duration: number;
}

type Entry = { guid: string; duration: number; uploaded?: string };
const VIDEOS = manifest.videos as Record<string, Record<string, Entry>>;

/** Épisodes publiés, par identifiant de dossier (`00-trailer`, `01-e01`, …). */
export function videoEpisodes(): string[] {
  return Object.keys(VIDEOS);
}

export function landingVideo(episode: string, locale: string, pageHost?: string): LandingVideo | undefined {
  const v = VIDEOS[episode]?.[locale];
  if (!v) return undefined;
  const base = `https://${videoHostFor(pageHost)}/${v.guid}`;
  return { src: `${base}/play_720p.mp4`, poster: `${base}/thumbnail.jpg`, duration: v.duration };
}

/** «1:57» — la durée telle qu'on l'annonce à côté du bouton. */
export function formatDuration(seconds: number): string {
  // Arrondir UNE fois, puis découper: arrondir les secondes après avoir tronqué
  // les minutes écrit «1:60» pour 119,6 s.
  const s = Math.round(seconds);
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
}

// Chrome de la section «bande-annonce» de l'accueil. Ici et non dans les
// messages pour la raison donnée en tête de features-content.ts: la parité des
// cinq dictionnaires obligerait à écrire un texte arabe pour une section que
// l'arabe n'affiche pas.
export interface TrailerLabels {
  kicker: string;
  title: string;
  /** Le sous-titre de la bande-annonce dans le script (code names déjà appliqués). */
  lead: string;
  /** Libellé accessible du lecteur. */
  aria: string;
}

const TRAILER: Record<string, TrailerLabels> = {
  fr: {
    kicker: 'En vidéo',
    title: 'Tout le produit en deux minutes',
    lead: 'Un voyage, de la demande jusqu’à l’encaissement : le devis, la mission, le chauffeur sur la route, la facture et la banque.',
    aria: 'Bande-annonce maTransports',
  },
  en: {
    kicker: 'Video',
    title: 'The whole product in two minutes',
    lead: 'One trip, from request to cash: the quote, the mission, the driver on the road, the invoice and the bank.',
    aria: 'maTransports trailer',
  },
  es: {
    kicker: 'En vídeo',
    title: 'Todo el producto en dos minutos',
    lead: 'Un viaje, de la solicitud al cobro: el presupuesto, la misión, el conductor en ruta, la factura y el banco.',
    aria: 'Tráiler de maTransports',
  },
  ru: {
    kicker: 'Видео',
    title: 'Весь продукт за две минуты',
    lead: 'Один рейс — от заявки до денег: предложение, рейс, водитель в дороге, фактура и банк.',
    aria: 'Трейлер maTransports',
  },
};

export const TRAILER_EPISODE = '00-trailer';

export function trailerLabels(locale: string): TrailerLabels | undefined {
  return TRAILER[locale];
}

/**
 * Identifiant court d'un épisode, celui de l'URL (`/fr/videos/e01`) et du
 * dossier `public/videos/e01/`: `00-trailer` → `trailer`, `01-e01` → `e01`.
 * Même règle que l'outil `web_assets.mjs`.
 */
export function episodeSlug(episode: string): string {
  return episode === TRAILER_EPISODE ? 'trailer' : episode.split('-').slice(1).join('-');
}

export function episodeFromSlug(slug: string): string | undefined {
  return videoEpisodes().find((ep) => episodeSlug(ep) === slug);
}

/** Langues où la série existe — celles de la bande-annonce (fr, en, es, ru). */
export const VIDEO_LOCALES: readonly string[] = Object.keys(VIDEOS[TRAILER_EPISODE] ?? {}).sort();

/** Sous-titres (même origine que la page) et affiche locale d'une vidéo publiée. */
export function videoFiles(episode: string, locale: string): { captions: string; image: string } | undefined {
  if (!VIDEOS[episode]?.[locale]) return undefined;
  const base = `/videos/${episodeSlug(episode)}/${locale}`;
  return { captions: `${base}.vtt`, image: `${base}.jpg` };
}

/** Date de mise en ligne (aaaa-mm-jj), pour `uploadDate` du JSON-LD. */
export function videoUploaded(episode: string, locale: string): string | undefined {
  return VIDEOS[episode]?.[locale]?.uploaded;
}

/** «1:57» → «2 min» pour un bouton: on annonce un ordre de grandeur, pas un minutage. */
export function roundMinutes(seconds: number): number {
  return Math.max(1, Math.round(seconds / 60));
}
