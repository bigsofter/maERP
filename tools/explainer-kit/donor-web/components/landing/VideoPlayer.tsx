// Lecteur des vidéos explicatives — un `<video>` natif, rien d'autre.
//
// Composant SERVEUR, zéro JavaScript: `preload="none"` + `poster` font que la
// page ne télécharge que l'affiche tant qu'on n'a pas appuyé sur lecture, et
// les commandes sont celles du navigateur (plein écran, vitesse, AirPlay
// compris). Voir videos.ts pour les deux verrous (CSP, referrers Bunny).
//
// `aspect-video` réserve la place avant le chargement de l'affiche: sans lui la
// section sauterait de 16:9 au premier octet d'image (CLS).
//
// Sous-titres: une piste `<track kind="captions">` servie par NOTRE origine
// (public/videos/…, voir videos.ts), éteinte par défaut — la vidéo parle et
// porte déjà ses titres à l'écran; le bouton «CC» du navigateur l'allume.

import type { LandingVideo } from './videos';

export interface VideoCaptions {
  src: string;
  srcLang: string;
  /** Nom de la langue, dans cette langue («Français»). */
  label: string;
}

export function VideoPlayer({
  video,
  label,
  captions,
}: {
  video: LandingVideo;
  label: string;
  captions?: VideoCaptions;
}) {
  return (
    <video
      controls
      playsInline
      preload="none"
      poster={video.poster}
      aria-label={label}
      className="aspect-video w-full rounded-xl border border-line bg-slate-900 shadow-2"
    >
      <source src={video.src} type="video/mp4" />
      {captions && <track kind="captions" src={captions.src} srcLang={captions.srcLang} label={captions.label} />}
    </video>
  );
}
