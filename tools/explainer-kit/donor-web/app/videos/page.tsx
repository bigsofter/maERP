import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { headers } from 'next/headers';
import { setRequestLocale } from 'next-intl/server';
import { routing } from '@/i18n/routing';
import { LandingNav } from '@/components/landing/LandingNav';
import { LandingFooter } from '@/components/landing/LandingFooter';
import { CtaBand } from '@/components/landing/CtaBand';
import { FeatureExplorer } from '@/components/landing/FeatureExplorer';
import { featureNav } from '@/components/landing/features-content';
import { landingHost, workspaceBase } from '@/components/landing/feature-route';
import { VIDEO_LOCALES } from '@/components/landing/videos';
import { LIBRARY_ANCHOR, libraryGroups, libraryLabels, videoNav } from '@/components/landing/videos-library';
import '@/components/landing/landing.css';

// Vidéothèque — tous les épisodes publiés, rangés comme les pages «fonctions»
// (même FeatureExplorer, mêmes catégories), plus le groupe «Découverte» en tête.
// Le contenu et le classement vivent dans components/landing/videos-library.ts.
//
// Rendu dynamique, pas `force-static`: l'hôte vidéo dépend du domaine du
// landing (transport.tinycio.ma → video.tinycio.ma, voir videos.ts), et une
// page figée au build aurait celui du build sur les quatre domaines.
// En arabe: 404 — la série n'existe pas en arabe et aucun lien n'y mène.

export async function generateMetadata({ params }: { params: Promise<{ locale: string }> }): Promise<Metadata> {
  const { locale } = await params;
  const l = libraryLabels(locale);
  if (!l) return {};
  const base = `https://${landingHost((await headers()).get('host') ?? 'transport.tinycio.ma')}`;
  const languages = Object.fromEntries(VIDEO_LOCALES.map((v) => [v, `${base}/${v}/videos`]));
  const title = `${l.title} · maTransports`;
  return {
    title,
    description: l.lead,
    alternates: {
      canonical: `${base}/${locale}/videos`,
      languages: { ...languages, 'x-default': `${base}/${routing.defaultLocale}/videos` },
    },
    openGraph: { type: 'website', siteName: 'maTransports', title, description: l.lead, url: `${base}/${locale}/videos`, locale },
  };
}

export default async function VideosPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const l = libraryLabels(locale);
  if (!l) notFound();
  const host = (await headers()).get('host') ?? 'transport.tinycio.ma';
  const wsBase = workspaceBase(host);
  const nav = featureNav(locale);
  const groups = libraryGroups(locale, host);

  return (
    <div className="min-h-screen overflow-x-clip bg-bg text-slate-900">
      <LandingNav
        loginHref={`${wsBase}/${locale}/login`}
        signupHref={`${wsBase}/${locale}/signup`}
        anchorBase={`/${locale}`}
        features={nav?.items}
        featuresLabel={nav?.label}
        videos={videoNav(locale)}
      />
      <main>
        <FeatureExplorer
          anchor={LIBRARY_ANCHOR}
          kicker={l.kicker}
          title={l.title}
          lead={l.lead}
          all={nav?.all ?? ''}
          groups={groups}
          asPageTitle
        />
        <CtaBand signupHref={`${wsBase}/${locale}/signup`} />
      </main>
      <LandingFooter locale={locale} ldHost={landingHost(host)} />
    </div>
  );
}
