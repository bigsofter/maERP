// Gabarit des pages «fonctions» du landing (/exploitation, /conteneurs, …).
//
// Une seule mise en page pour les sept pages: le contenu vit dans
// features-content.ts et la page de route ne fait qu'appeler ce composant. Ce
// n'est pas de l'abstraction pour l'abstraction — c'est ce qui garantit que la
// huitième page, écrite dans six mois par quelqu'un d'autre, argumente dans le
// même ordre: douleur → fonction → détail qui compte → ce qui vous protège →
// prix → objections.
//
// L'ordre des sections est un argumentaire, pas une esthétique:
//
//   1. le prospect doit se reconnaître (les douleurs) avant qu'on lui vende;
//   2. chaque fonction porte son «détail qui compte» — la décision produit
//      qu'un transporteur expérimenté reconnaît et qu'un concurrent n'a pas;
//   3. l'esquisse d'écran arrive APRÈS les fonctions: elle confirme, elle
//      n'explique pas (un tableau ne se lit pas avant d'avoir compris);
//   4. «ce qui vous protège» est la section qui vend le plus, et c'est la
//      raison pour laquelle les contraintes du produit y sont écrites comme
//      des garanties et non cachées comme des limitations;
//   5. le prix vient en dernier, quand la valeur a été posée.
//
// Le composant est SERVEUR (pas de 'use client'): ces pages sont statiques,
// n'ont aucun état, et le budget du landing est LCP ≤ 2 s en 4G marocaine.
// L'esquisse d'écran est un tableau HTML, pas une image: zéro octet de plus,
// lisible par un lecteur d'écran et par Google.

import type { FeaturePageContent } from './features-content';
import { featureLabels, featurePages } from './features-content';
import { Icon, blockIcon, pageIcon } from './icons';
import { ScreenMock } from './ScreenMock';
import { VideoPlayer } from './VideoPlayer';
import { formatDuration } from './videos';
import type { HeroVideo } from './videos-library';
import './landing.css';

function SectionTitle({ children }: { children: React.ReactNode }) {
  return (
    <h2 className="font-display text-[22px] font-semibold leading-[1.25] tracking-[-0.4px] text-slate-900 sm:text-[26px]">
      {children}
    </h2>
  );
}

export function FeaturePage({
  content,
  locale,
  wsBase,
  hero,
}: {
  content: FeaturePageContent;
  locale: string;
  wsBase: string;
  /**
   * L'épisode vidéo de l'écran que vend la page, à côté du titre: on voit le
   * produit bouger sans descendre jusqu'au bloc «Vidéos sur ce sujet».
   * `episodePage` = libellé du lien vers la page de l'épisode.
   */
  hero?: { video: HeroVideo; episodePage: string; captionsLabel: string };
}) {
  const others = featurePages(locale).filter((p) => p.slug !== content.slug);
  const t = featureLabels(locale);

  return (
    <main>
      {/* ── Hero ─────────────────────────────────────────────────────────── */}
      <section className="relative overflow-clip px-4 pb-2 pt-14 sm:px-8">
        {/* Lueur d'accueil — les mêmes deux halos que la page d'accueil, pour
            que la page de fonction se lise comme la suite du même site. */}
        <div
          className="pointer-events-none absolute inset-0"
          style={{
            background:
              'radial-gradient(ellipse at top right, rgba(29,78,216,0.10), transparent 55%), radial-gradient(ellipse at bottom left, rgba(245,158,11,0.08), transparent 60%)',
          }}
          aria-hidden
        />
        <div className="relative mx-auto max-w-[1180px]">
          <span className="inline-flex items-center gap-2 rounded-pill border border-route-100 bg-white px-3 py-1.5 text-[11.5px] font-semibold text-route-700 shadow-1">
            <Icon name={pageIcon(content.slug)} className="h-[15px] w-[15px]" strokeWidth={2} />
            {content.kicker}
          </span>
          <div className={hero ? 'grid items-start gap-8 lg:grid-cols-[minmax(0,1fr)_minmax(0,520px)] lg:gap-10' : undefined}>
            <div>
              <h1 className="mt-5 max-w-[820px] font-display text-[30px] font-semibold leading-[1.15] tracking-[-0.8px] text-slate-900 sm:text-[44px]">
                {content.title}
              </h1>
              <p className="mt-5 max-w-[760px] text-[15px] leading-[1.75] text-slate-600">{content.intro}</p>
            </div>
            {hero && (
              <figure className="m-0 lg:mt-5">
                <VideoPlayer
                  video={hero.video.video}
                  label={hero.video.text.aria}
                  captions={{ src: hero.video.captions, srcLang: locale, label: hero.captionsLabel }}
                />
                <figcaption className="mt-3 flex flex-wrap items-baseline justify-between gap-x-3 gap-y-1 text-[12.5px] text-slate-500">
                  <span>
                    <span className="font-semibold uppercase tracking-[1px] text-route-700">{hero.video.text.kicker}</span>
                    {' · '}
                    <span className="tabular-nums">{formatDuration(hero.video.video.duration)}</span>
                    {' · '}
                    {hero.video.text.title}
                  </span>
                  <a href={hero.video.href} className="font-semibold text-route-700 no-underline hover:text-route-900">
                    {hero.episodePage} →
                  </a>
                </figcaption>
              </figure>
            )}
          </div>

          <div className="mt-stagger mt-8 grid gap-3 sm:grid-cols-3">
            {content.stats.map((s) => (
              <div key={s.label} className="rounded-lg border border-line bg-white px-5 py-4 shadow-1 transition-shadow hover:shadow-2">
                <div className="font-display text-[24px] font-semibold tracking-[-0.6px] text-route-700">{s.value}</div>
                <div className="mt-1 text-[12.5px] leading-[1.55] text-slate-500">{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── Les douleurs ─────────────────────────────────────────────────── */}
      <section className="mx-auto max-w-[1180px] px-4 pt-12 sm:px-8">
        <SectionTitle>{content.painsTitle}</SectionTitle>
        <div className="mt-stagger mt-5 grid gap-4 md:grid-cols-3">
          {content.pains.map((p) => (
            <article key={p.title} className="rounded-lg border border-line bg-slate-50 p-5">
              <span className="mb-3 inline-flex h-8 w-8 items-center justify-center rounded-[10px] bg-white text-slate-400 shadow-1" aria-hidden>
                <Icon name="alert" className="h-[17px] w-[17px]" />
              </span>
              <h3 className="text-[14.5px] font-semibold text-slate-900">{p.title}</h3>
              <p className="mt-2 text-[13px] leading-[1.7] text-slate-600">{p.text}</p>
            </article>
          ))}
        </div>
      </section>

      {/* ── Les fonctions ────────────────────────────────────────────────── */}
      <section className="mx-auto max-w-[1180px] px-4 pt-14 sm:px-8">
        <SectionTitle>{content.blocksTitle}</SectionTitle>
        <div className="mt-stagger mt-5 grid gap-4 md:grid-cols-2">
          {content.blocks.map((b, i) => (
            <article
              key={b.title}
              className="rounded-lg border border-line bg-white p-6 shadow-1 transition-all duration-200 hover:-translate-y-[3px] hover:border-route-200 hover:shadow-2"
            >
              <span className="mb-3.5 inline-flex h-10 w-10 items-center justify-center rounded-[12px] bg-route-50 text-route-700" aria-hidden>
                <Icon name={blockIcon(content.slug, i)} className="h-[21px] w-[21px]" />
              </span>
              <h3 className="font-display text-[17px] font-semibold leading-[1.3] text-slate-900">{b.title}</h3>
              <p className="mt-2.5 text-[13.5px] leading-[1.7] text-slate-600">{b.text}</p>
              {b.detail ? (
                <p className="mt-3 border-t border-line-soft pt-3 text-[12.5px] leading-[1.65] text-slate-500">
                  <span className="font-semibold text-route-700">{t.detail} </span>
                  {b.detail}
                </p>
              ) : null}
            </article>
          ))}
        </div>
      </section>

      {/* ── L'écran ──────────────────────────────────────────────────────── */}
      <section className="mx-auto max-w-[1180px] px-4 pt-14 sm:px-8">
        <div className="mt-reveal">
          <ScreenMock screen={content.screen} slug={content.slug} navLabel={content.nav} />
        </div>
      </section>

      {/* ── Ce qui vous protège ──────────────────────────────────────────── */}
      <section className="mx-auto max-w-[1180px] px-4 pt-14 sm:px-8">
        <SectionTitle>{content.protectionsTitle}</SectionTitle>
        <div className="mt-stagger mt-5 grid gap-4 md:grid-cols-2">
          {content.protections.map((p) => (
            <article key={p.title} className="flex gap-3.5 rounded-lg border border-route-100 bg-route-50/50 p-5">
              <span className="mt-0.5 inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-pill bg-white text-route-700 shadow-1" aria-hidden>
                <Icon name="shield" className="h-[17px] w-[17px]" />
              </span>
              <div className="min-w-0">
                <h3 className="text-[14.5px] font-semibold text-route-900">{p.title}</h3>
                <p className="mt-2 text-[13px] leading-[1.7] text-slate-600">{p.text}</p>
              </div>
            </article>
          ))}
        </div>
      </section>

      {/* ── Ce qui n'existe pas encore ───────────────────────────────────── */}
      {content.planned ? (
        <section className="mx-auto max-w-[1180px] px-4 pt-10 sm:px-8">
          <div className="rounded-lg border border-warning-bg bg-warning-bg/60 p-5">
            <div className="text-[11px] font-semibold uppercase tracking-[0.8px] text-warning-fg">
              {t.planned}
            </div>
            <p className="mt-2 max-w-[860px] text-[13px] leading-[1.7] text-slate-700">{content.planned}</p>
          </div>
        </section>
      ) : null}

      {/* ── Prix ─────────────────────────────────────────────────────────── */}
      <section className="mx-auto max-w-[1180px] px-4 pt-12 sm:px-8">
        <div className="flex flex-wrap items-center justify-between gap-5 rounded-2xl border border-line bg-white p-6 sm:p-8">
          <div className="min-w-[280px] flex-1">
            <div className="font-display text-[19px] font-semibold leading-[1.3] text-slate-900">
              {content.priceLine}
            </div>
            <p className="mt-2 max-w-[640px] text-[13px] leading-[1.7] text-slate-500">{content.priceNote}</p>
          </div>
          <a
            href={`${wsBase}/${locale}/signup`}
            className="inline-flex h-11 items-center rounded-pill bg-grad-amber px-6 text-[13.5px] font-semibold text-slate-900 no-underline shadow-amber hover:brightness-105"
          >
            {t.cta}
          </a>
        </div>
      </section>

      {/* ── FAQ ──────────────────────────────────────────────────────────── */}
      <section className="mx-auto max-w-[1180px] px-4 pt-14 sm:px-8">
        <SectionTitle>{t.faq}</SectionTitle>
        <div className="mt-stagger mt-5 grid gap-3">
          {content.faq.map((f) => (
            <details key={f.q} className="group rounded-lg border border-line bg-white p-5 open:bg-slate-50/60">
              <summary className="cursor-pointer list-none text-[14px] font-semibold text-slate-900 marker:hidden">
                {f.q}
              </summary>
              <p className="mt-2.5 max-w-[860px] text-[13.5px] leading-[1.75] text-slate-600">{f.a}</p>
            </details>
          ))}
        </div>
      </section>

      {/* ── Les autres pages ─────────────────────────────────────────────── */}
      <section className="mx-auto max-w-[1180px] px-4 pt-14 sm:px-8">
        <div className="text-[11px] font-semibold uppercase tracking-[1px] text-slate-400">{t.seeAlso}</div>
        <div className="mt-3 flex flex-wrap gap-2">
          {others.map((p) => (
            <a
              key={p.slug}
              href={`/${locale}/${p.slug}`}
              className="inline-flex items-center rounded-pill border border-line bg-white px-4 py-2 text-[12.5px] font-medium text-slate-700 no-underline hover:border-route-200 hover:text-route-700"
            >
              {p.nav}
            </a>
          ))}
        </div>
      </section>
    </main>
  );
}
