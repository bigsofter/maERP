'use client';

// Sticky landing nav — anchor links to the page sections, the «fonctions»
// menu, cross-host «Se connecter» to the workspace, amber «Créer un compte»
// CTA. Client-only for the mobile hamburger and the menu; below lg the link
// row collapses into a dropdown panel (Landing Mobile.dc.html).

import { useEffect, useRef, useState } from 'react';
import { useTranslations } from 'next-intl';
import { BrandMark, BrandWordmark, ByTinyCIO } from './Brand';
import { useBrandHosts } from '@/lib/brand-links';

const ANCHORS = [
  ['#hero', 'overview'],
  ['#problemes', 'problems'],
  ['#chauffeur', 'driver_app'],
  ['#modules', 'modules'],
  ['#comparatif', 'comparison'],
  ['#tarifs', 'pricing'],
  ['#faq', 'faq'],
] as const;

/**
 * En haut, sur grand écran, on n'en garde que deux — plus le menu «fonctions».
 * «Modules» n'y est plus (2026-10-04, propriétaire): pour le visiteur, c'est la
 * même chose que «Fonctions»; la vitrine des modules devient le dernier lien du
 * menu déroulant.
 * Sept ancres plus un menu déroulant, cela faisait une barre plus longue que la
 * promesse du produit, et une barre longue ne se lit pas: elle se saute. Les
 * quatre autres restent dans le panneau mobile (où la place est gratuite) et
 * dans le pied de page, qui est fait pour ça.
 */
const PRIMARY: ReadonlySet<string> = new Set(['#tarifs', '#faq']);

/**
 * Les pages «fonctions» arrivent en props DÉJÀ résolues (href + libellé) au lieu
 * d'être lues ici par `featurePages(locale)`: ce composant est client, et
 * importer le module de contenu enverrait les dix pages × quatre langues dans le
 * bundle du navigateur. Le landing a un budget de LCP ≤ 2 s en 4G marocaine.
 */
export interface NavFeature {
  href: string;
  label: string;
  /** Catégorie de la page, déjà traduite. Absente → liste à plat. */
  group?: string;
  /** Ancre de cette catégorie dans la section «fonctions» de l'accueil. */
  groupHref?: string;
}

interface NavSection {
  group?: string;
  groupHref?: string;
  items: NavFeature[];
}

/**
 * Les pages arrivent déjà ordonnées par catégorie (featureNav): il suffit de
 * couper la liste là où la catégorie change. Pas de tri ici — l'ordre est celui
 * des espaces du portail, et il se décide à un seul endroit.
 */
function sections(items: readonly NavFeature[]): NavSection[] {
  const out: NavSection[] = [];
  for (const f of items) {
    const last = out[out.length - 1];
    if (last && last.group === f.group) last.items.push(f);
    else out.push({ group: f.group, groupHref: f.groupHref, items: [f] });
  }
  return out;
}

/** Menu déroulant: survol, clic, Échap, clic dehors — les quatre sorties. */
function FeaturesMenu({
  label,
  items,
  footer,
}: {
  label: string;
  items: readonly NavFeature[];
  /** Dernier lien du menu, sous les catégories: la vitrine des modules de l'accueil. */
  footer?: { href: string; label: string };
}) {
  const [open, setOpen] = useState(false);
  const wrap = useRef<HTMLDivElement>(null);
  const groups = sections(items);

  useEffect(() => {
    if (!open) return;
    const onDown = (e: MouseEvent) => {
      if (!wrap.current?.contains(e.target as Node)) setOpen(false);
    };
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setOpen(false);
    };
    document.addEventListener('mousedown', onDown);
    document.addEventListener('keydown', onKey);
    return () => {
      document.removeEventListener('mousedown', onDown);
      document.removeEventListener('keydown', onKey);
    };
  }, [open]);

  return (
    <div
      ref={wrap}
      className="relative"
      onMouseEnter={() => setOpen(true)}
      onMouseLeave={() => setOpen(false)}
    >
      <button
        type="button"
        aria-haspopup="true"
        aria-expanded={open}
        onClick={() => setOpen((v) => !v)}
        className={`inline-flex items-center gap-1 px-[13px] py-2.5 text-[13px] font-medium ${
          open ? 'text-slate-900' : 'text-slate-600 hover:text-slate-900'
        }`}
      >
        {label}
        <svg
          width="11"
          height="11"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2.4"
          strokeLinecap="round"
          strokeLinejoin="round"
          className={open ? 'rotate-180' : undefined}
          aria-hidden
        >
          <polyline points="6 9 12 15 18 9" />
        </svg>
      </button>
      {open && (
        // Deux colonnes dès qu'il y a des catégories: une colonne de quarante
        // liens sortirait de l'écran d'un portable. `break-inside-avoid` garde
        // chaque catégorie entière — un intertitre orphelin en bas de colonne
        // se lit comme le titre de la colonne voisine.
        <div
          className={`absolute start-0 top-full z-50 rounded-[12px] border border-line bg-white p-1.5 shadow-[0_12px_28px_rgba(15,23,42,0.12)] ${
            groups.length > 1 ? 'w-[460px] columns-2 gap-1.5' : 'min-w-[248px]'
          }`}
        >
          {groups.map((g) => (
            <div key={g.group ?? g.items[0].href} className="break-inside-avoid pb-1">
              {g.group &&
                (g.groupHref ? (
                  <a
                    href={g.groupHref}
                    onClick={() => setOpen(false)}
                    className="block px-3 pb-1 pt-2 text-[10.5px] font-semibold uppercase tracking-[1px] text-slate-400 no-underline hover:text-route-700"
                  >
                    {g.group}
                  </a>
                ) : (
                  <span className="block px-3 pb-1 pt-2 text-[10.5px] font-semibold uppercase tracking-[1px] text-slate-400">
                    {g.group}
                  </span>
                ))}
              {g.items.map((f) => (
                <a
                  key={f.href}
                  href={f.href}
                  onClick={() => setOpen(false)}
                  className="block rounded-[8px] px-3 py-[7px] text-[13px] font-medium text-slate-600 no-underline hover:bg-slate-50 hover:text-slate-900"
                >
                  {f.label}
                </a>
              ))}
            </div>
          ))}
          {footer && (
            <a
              href={footer.href}
              onClick={() => setOpen(false)}
              className="mt-1 block break-inside-avoid rounded-[8px] border-t [column-span:all] border-line-soft px-3 pb-[7px] pt-2.5 text-[13px] font-semibold text-route-700 no-underline hover:bg-slate-50"
            >
              {footer.label} <span aria-hidden>→</span>
            </a>
          )}
        </div>
      )}
    </div>
  );
}

export function LandingNav({
  loginHref,
  signupHref,
  anchorBase = '',
  features,
  featuresLabel,
  videos,
}: {
  loginHref: string;
  signupHref: string;
  /**
   * Préfixe des ancres. Vide sur la page d'accueil (les sections sont sur la
   * page); `/fr` sur les pages de fonctions et /integrations, où `#tarifs`
   * seul ne mène nulle part et laisserait le visiteur sur un lien mort.
   */
  anchorBase?: string;
  /**
   * Pages «fonctions» du menu. Absentes en arabe (elles retombent sur le
   * français — même règle que la colonne du pied de page), et le menu
   * disparaît alors au lieu d'afficher des liens dans une autre langue.
   */
  features?: readonly NavFeature[];
  featuresLabel?: string;
  /**
   * La vidéothèque (`videoNav`): à côté du menu «fonctions» sur grand écran,
   * en tête du panneau mobile. Absente en arabe — la série n'y existe pas.
   */
  videos?: { href: string; label: string };
}) {
  const t = useTranslations('landing.nav');
  const [open, setOpen] = useState(false);
  const hosts = useBrandHosts();
  const hasFeatures = Boolean(features && features.length > 0 && featuresLabel);

  return (
    <nav className="sticky top-0 z-40 border-b border-line bg-[rgba(248,250,252,0.92)] backdrop-blur-[14px]">
      <div className="mx-auto flex h-[60px] max-w-[1244px] items-center justify-between gap-3 px-4 sm:px-8">
        <div className="flex min-w-0 items-center gap-6">
          {/* «by TinyCIO» is its own link (the hub's site on the same TLD),
              so it lives OUTSIDE the home anchor — nested links are invalid
              HTML and browsers split them unpredictably. */}
          <span className="inline-flex items-center gap-2.5">
            <a href={`${anchorBase}#hero`} className="inline-flex items-center gap-2.5 no-underline">
              <BrandMark />
              <BrandWordmark textClass="text-[15px] sm:text-[17px]" />
            </a>
            <span className="hidden h-4 w-px bg-line sm:block" />
            <span className="hidden sm:block">
              {hosts ? (
                <a href={hosts.tinycio} className="no-underline">
                  <ByTinyCIO by={t('by')} />
                </a>
              ) : (
                <ByTinyCIO by={t('by')} />
              )}
            </span>
          </span>
          <div className="hidden items-center gap-0.5 lg:flex">
            {hasFeatures && (
              <FeaturesMenu
                label={featuresLabel!}
                items={features!}
                footer={{ href: `${anchorBase}#modules`, label: t('modules') }}
              />
            )}
            {videos && (
              <a
                href={videos.href}
                className="px-[13px] py-2.5 text-[13px] font-medium text-slate-600 no-underline hover:text-slate-900"
              >
                {videos.label}
              </a>
            )}
            {/* Sans menu «fonctions» (arabe), «Modules» reprend sa place dans la barre. */}
            {ANCHORS.filter(([href]) => PRIMARY.has(href) || (href === '#modules' && !hasFeatures)).map(([href, key]) => (
              <a
                key={key}
                href={`${anchorBase}${href}`}
                className="px-[13px] py-2.5 text-[13px] font-medium text-slate-600 no-underline hover:text-slate-900"
              >
                {t(key)}
              </a>
            ))}
          </div>
        </div>
        <div className="flex items-center gap-2.5">
          <a
            href={loginHref}
            className="hidden h-9 items-center rounded-pill border border-line bg-white px-4 text-[13px] font-medium text-slate-700 no-underline hover:bg-slate-50 sm:inline-flex"
          >
            {t('login')}
          </a>
          <a
            href={signupHref}
            className="inline-flex h-9 items-center gap-1.5 whitespace-nowrap rounded-pill bg-grad-amber px-4 text-[12px] font-semibold text-slate-900 no-underline shadow-amber hover:brightness-105 sm:px-[18px] sm:text-[13px]"
          >
            {t('signup')} <span aria-hidden>→</span>
          </a>
          <button
            type="button"
            aria-label={t('menu')}
            aria-expanded={open}
            onClick={() => setOpen((v) => !v)}
            className="inline-flex h-8 w-8 items-center justify-center rounded-[9px] border border-line bg-white text-slate-600 lg:hidden"
          >
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" aria-hidden>
              <line x1="4" y1="7" x2="20" y2="7" />
              <line x1="4" y1="12" x2="20" y2="12" />
              <line x1="4" y1="17" x2="20" y2="17" />
            </svg>
          </button>
        </div>
      </div>
      {open && (
        <div className="border-t border-line-soft bg-bg px-4 pb-4 pt-2 lg:hidden">
          {videos && (
            <a
              href={videos.href}
              onClick={() => setOpen(false)}
              className="block rounded-md px-3 py-2.5 text-[14px] font-medium text-slate-700 no-underline hover:bg-white"
            >
              {videos.label}
            </a>
          )}
          {ANCHORS.map(([href, key]) => (
            <a
              key={key}
              href={`${anchorBase}${href}`}
              onClick={() => setOpen(false)}
              className="block rounded-md px-3 py-2.5 text-[14px] font-medium text-slate-700 no-underline hover:bg-white"
            >
              {t(key)}
            </a>
          ))}
          {/* Pas de sous-menu sur mobile: une liste à plat sous son titre. Un
              accordéon dans un panneau déjà déroulé se ferme deux fois. */}
          {features && features.length > 0 && featuresLabel && (
            <>
              <span className="mt-3 block px-3 text-[11px] font-semibold uppercase tracking-[1px] text-slate-400">
                {featuresLabel}
              </span>
              {sections(features).map((g) => (
                <div key={g.group ?? g.items[0].href}>
                  {g.group && (
                    <span className="mt-2 block px-3 text-[11px] font-medium text-slate-400">{g.group}</span>
                  )}
                  {g.items.map((f) => (
                    <a
                      key={f.href}
                      href={f.href}
                      onClick={() => setOpen(false)}
                      className="block rounded-md px-3 py-2 text-[13.5px] text-slate-600 no-underline hover:bg-white"
                    >
                      {f.label}
                    </a>
                  ))}
                </div>
              ))}
            </>
          )}
          <a
            href={loginHref}
            className="mt-2 block rounded-md border border-line bg-white px-3 py-2.5 text-center text-[14px] font-medium text-slate-700 no-underline"
          >
            {t('login')}
          </a>
        </div>
      )}
    </nav>
  );
}
