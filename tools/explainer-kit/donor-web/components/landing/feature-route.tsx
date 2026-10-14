import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { setRequestLocale } from 'next-intl/server';
import { headers } from 'next/headers';
import { routing } from '@/i18n/routing';
import { LandingNav } from './LandingNav';
import { heroVideo, libraryLabels, relatedVideos, videoNav } from './videos-library';
import { RelatedVideos } from './RelatedVideos';
import { LandingFooter } from './LandingFooter';
import { CtaBand } from './CtaBand';
import { FeaturePage } from './FeaturePage';
import { featureNav, featurePage } from './features-content';
import './landing.css';

// Fabrique des routes «fonctions»: sept pages, un seul assemblage.
//
// Next.js exige que chaque route exporte SES propres `generateMetadata`,
// `generateStaticParams` et composant par défaut — on ne peut pas partager un
// fichier de page. Ce qu'on peut partager, c'est ce qu'ils font: le fichier de
// route se réduit alors à trois ré-exports et le jour où l'on ajoute une
// balise OG ou un fil d'Ariane, on l'ajoute une fois pour les sept pages.
//
// Ces pages existent en français, anglais, espagnol et russe (un fichier de
// contenu par langue). L'arabe n'a pas encore d'argumentaire relu et retombe
// explicitement sur le français plutôt que d'afficher une traduction que
// personne n'a validée. `generateStaticParams` couvre donc TOUTES les locales:
// un visiteur arrivé en /ar/tresorerie doit trouver une page lisible, pas un
// 404 — et le chrome autour reste, lui, dans sa langue.

/** Hôte du landing (les pages publiques vivent sur `transport.*`). */
export function landingHost(host: string): string {
  const h = host.split(':')[0];
  return h.startsWith('my.transport.') ? h.slice(3) : h;
}

/** Base cross-hôte de l'espace de travail, pour «Se connecter». */
export function workspaceBase(host: string): string {
  const h = host.split(':')[0];
  return h.startsWith('transport.') ? `https://my.${h}` : '';
}

export function featureRoute(slug: string) {
  function generateStaticParams() {
    return routing.locales.map((locale) => ({ locale }));
  }

  async function generateMetadata({
    params,
  }: {
    params: Promise<{ locale: string }>;
  }): Promise<Metadata> {
    const { locale } = await params;
    const content = featurePage(slug, locale);
    if (!content) return {};
    const host = (await headers()).get('host') ?? 'transport.tinycio.ma';
    const base = `https://${landingHost(host)}`;
    const languages = Object.fromEntries(routing.locales.map((l) => [l, `${base}/${l}/${slug}`]));
    return {
      title: content.metaTitle,
      description: content.metaDescription,
      alternates: {
        canonical: `${base}/${locale}/${slug}`,
        languages: { ...languages, 'x-default': `${base}/${routing.defaultLocale}/${slug}` },
      },
      openGraph: {
        type: 'website',
        siteName: 'maTransports',
        title: content.metaTitle,
        description: content.metaDescription,
        url: `${base}/${locale}/${slug}`,
        locale,
      },
    };
  }

  async function Page({ params }: { params: Promise<{ locale: string }> }) {
    const { locale } = await params;
    setRequestLocale(locale);
    const content = featurePage(slug, locale);
    if (!content) notFound();
    const host = (await headers()).get('host') ?? 'transport.tinycio.ma';
    const wsBase = workspaceBase(host);
    const nav = featureNav(locale);
    const lib = libraryLabels(locale);
    const video = heroVideo(slug, locale);
    const hero = video && lib ? { video, episodePage: lib.episodePage, captionsLabel: lib.captions } : undefined;

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
        <FeaturePage content={content} locale={locale} wsBase={wsBase} hero={hero} />
        <RelatedVideos related={relatedVideos(slug, locale)} />
        <div className="pt-16">
          <CtaBand signupHref={`${wsBase}/${locale}/signup`} />
        </div>
        <LandingFooter locale={locale} ldHost={landingHost(host)} />
      </div>
    );
  }

  return { generateStaticParams, generateMetadata, Page };
}
