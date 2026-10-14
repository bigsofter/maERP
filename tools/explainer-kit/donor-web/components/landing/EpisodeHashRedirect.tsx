'use client';

// Les anciens liens d'épisode de l'accueil (`transport.tinycio.ma/fr#e01`) ont
// déjà été envoyés: l'épisode 1 a vécu sous la bande-annonce, avec son ancre,
// avant que la vidéothèque n'existe. Une ancre ne part jamais au serveur — seul
// le navigateur la voit, donc la redirection se fait ici. `replace`: le retour
// arrière ne doit pas ramener sur l'accueil qui redirige aussitôt.

import { useEffect } from 'react';

export function EpisodeHashRedirect({ targets }: { targets: Record<string, string> }) {
  useEffect(() => {
    const to = targets[window.location.hash.slice(1)];
    if (to) window.location.replace(to);
  }, [targets]);
  return null;
}
