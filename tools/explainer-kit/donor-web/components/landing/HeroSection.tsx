// Hero — H1 + CTAs + trust line + 3 stat chips on the start side; la scène
// (carte, poste de travail, sources) vit dans HeroCanvas, qui porte tout le
// raisonnement de composition.

import { useTranslations } from 'next-intl';
import { HeroCanvas } from './HeroCanvas';
import { COMPANY_TEL } from './legal-registry';

/**
 * `video`: lien vers la bande-annonce (`#video`), sous les deux boutons. Sans
 * lui, la vidéo ne se trouvait qu'en faisant défiler — le propriétaire ne l'a
 * pas trouvée. Absent quand la langue n'a pas de vidéo (l'arabe).
 */
export function HeroSection({ signupHref, video }: { signupHref: string; video?: { href: string; label: string } }) {
  const t = useTranslations('landing.hero');

  return (
    <section id="hero" className="relative overflow-clip px-4 pb-16 pt-10 sm:px-8 sm:pb-[88px] sm:pt-16">
      <div
        className="absolute inset-0"
        style={{
          background:
            'radial-gradient(ellipse at top right, rgba(29,78,216,0.10), transparent 55%), radial-gradient(ellipse at bottom left, rgba(245,158,11,0.10), transparent 60%)',
        }}
        aria-hidden
      />
      <div
        className="absolute inset-0 opacity-50"
        style={{ backgroundImage: 'linear-gradient(#F1F5F9 1px, transparent 1px)', backgroundSize: '100% 80px' }}
        aria-hidden
      />
      <div className="relative mx-auto grid max-w-[1240px] items-center gap-10 lg:grid-cols-[minmax(0,420px)_minmax(0,1fr)] lg:gap-12">
        <div>
          <span className="inline-flex items-center gap-[7px] rounded-pill border border-line bg-white px-3 py-[5px] text-[11px] font-medium tracking-[0.2px] text-route-900 shadow-1">
            <span className="h-1.5 w-1.5 rounded-pill bg-amber-500" aria-hidden />
            {t('badge')}
          </span>
          <h1 className="mt-5 font-display text-[32px] font-semibold leading-[1.1] tracking-[-1px] text-slate-900 sm:text-[54px] sm:leading-[1.08] sm:tracking-[-1.8px]">
            {t('title_l1')}
            <br />
            {t('title_l2')}{' '}
            <span className="relative inline-block">
              <span className="bg-grad-brand bg-clip-text text-transparent">{t('title_hl')}</span>
              <svg
                viewBox="0 0 270 12"
                preserveAspectRatio="none"
                className="absolute -bottom-2.5 start-0 block h-3 w-full"
                aria-hidden
              >
                <line x1="4" y1="6" x2="266" y2="6" stroke="#F59E0B" strokeWidth="4" strokeLinecap="round" strokeDasharray="18 12" />
              </svg>
            </span>
          </h1>
          <p className="mt-7 max-w-[460px] text-[15px] leading-[1.6] text-slate-700 sm:text-base">{t('subtitle')}</p>
          <div className="mt-7 flex flex-wrap items-center gap-2.5">
            <a
              href={signupHref}
              className="inline-flex h-12 items-center gap-2 rounded-pill bg-grad-amber px-6 text-sm font-semibold text-slate-900 no-underline shadow-amber hover:brightness-105"
            >
              {t('cta_signup')} <span aria-hidden>→</span>
            </a>
            <a
              href={COMPANY_TEL}
              className="inline-flex h-12 items-center gap-2 rounded-pill border border-line bg-white px-[22px] text-sm font-medium text-slate-900 no-underline shadow-1 hover:bg-slate-50"
            >
              {t('cta_demo')}
            </a>
          </div>
          {video && (
            <a
              href={video.href}
              className="group mt-4 inline-flex items-center gap-2.5 text-[14px] font-semibold text-route-700 no-underline hover:text-route-900"
            >
              <span
                className="flex h-8 w-8 items-center justify-center rounded-pill bg-route-700 text-white shadow-1 transition-transform duration-200 group-hover:scale-110"
                aria-hidden
              >
                <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M8 5.5v13l11-6.5z" />
                </svg>
              </span>
              {video.label}
            </a>
          )}
          <div className="mt-4 text-xs text-slate-500">{t('foot')}</div>
          <div className="mt-7 grid grid-cols-3 gap-4 sm:flex sm:gap-8">
            {(['stat1', 'stat2', 'stat3'] as const).map((s) => (
              <div key={s}>
                <div className="font-display text-lg font-semibold tracking-[-0.8px] text-route-700 sm:text-[26px]">
                  {t(`${s}_value`)}
                </div>
                <div className="mt-0.5 text-[11px] text-slate-500">{t(`${s}_label`)}</div>
              </div>
            ))}
          </div>
        </div>

        <HeroCanvas />
      </div>
    </section>
  );
}
