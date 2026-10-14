import { NextRequest, NextResponse } from 'next/server';
import createIntlMiddleware from 'next-intl/middleware';
import { routing } from './i18n/routing';
import { VIDEO_HOSTS } from './components/landing/videos';

// NOTE (ADR-006): unlike the maOptique donor there is NO per-tenant subdomain
// logic here — no slug extraction from the host, no RESERVED_SLUGS, no
// ?workspace= plumbing. One workspace host per market (my.transport.tinycio.{tld});
// the tenant is resolved from the session cookie.

// Routes that are always public — no auth cookie required.
const PUBLIC_PATHS = [
  '/login', '/signup',
  // /welcome is reached right after finalize when cookies are fresh; public so
  // JWT expiry mid-celebration doesn't bounce users to login with no context.
  '/welcome',
  // /set-password is the welcome-email landing — the owner sets their first
  // password before any session exists. /forgot-password mints that email.
  '/set-password',
  '/forgot-password',
  '/team/accept', '/healthz',
  // Legal hub is public — linked from the landing footer and signup consent
  // text, which anonymous visitors must be able to read.
  '/legal',
  // Marketing page about what the product exchanges with Odoo, Sage and the
  // bank. Public for the same reason as the landing itself: it answers the
  // objection a prospect has BEFORE they would ever create an account.
  '/integrations',
  // The ten feature pages (components/landing/features-content.ts). Same
  // reason as /integrations, plus one that is specific to them: they are the
  // pages a prospect reaches from a search engine, and an auth redirect on a
  // search result is a bounce. `/documents-de-transport` carries that longer
  // slug precisely because `/documents` is a PORTAL route and must stay gated;
  // `/carburant`, `/entretien` and `/caisse-chauffeurs` are French for the same
  // reason the others are — and they avoid the portal routes /fuel,
  // /maintenance and /cash, which must stay gated.
  '/exploitation',
  '/conteneurs',
  '/documents-de-transport',
  '/facturation',
  '/tresorerie',
  '/marges',
  '/carburant',
  '/entretien',
  '/caisse-chauffeurs',
  '/securite',
  // The video library and one page per episode (components/landing/
  // videos-library.ts) — the episode page is the address people forward on
  // WhatsApp, so an auth redirect there would lose the very visitor it exists
  // for. No portal route is called /videos.
  '/videos',
];

// TLD → default locale. Domain dictates language; browser Accept-Language is
// ignored. .ma → French, .es → Spanish, .com → English, .ru → Russian.
const TLD_LOCALE: Record<string, 'en' | 'es' | 'fr' | 'ru'> = {
  com: 'en',
  es:  'es',
  ma:  'fr',
  ru:  'ru',
};

function getHostLocale(hostname: string): 'en' | 'es' | 'fr' | 'ru' {
  const host = hostname.split(':')[0];
  const tld = host.split('.').pop() ?? '';
  return TLD_LOCALE[tld] ?? 'fr';
}

const LOCALE_PREFIX_RE = /^\/(?:fr|ar|ru|es|en)(?=\/|$)/;

const intlMiddleware = createIntlMiddleware(routing);

// ── Content-Security-Policy ──────────────────────────────────────────────────
// script-src uses 'self' + 'unsafe-inline'. A per-request nonce is
// fundamentally incompatible with this app (donor lesson, maOptique 43f50cc):
// the whole `[locale]` tree is statically prerendered (generateStaticParams +
// setRequestLocale), and Next.js only stamps nonces onto its inline bootstrap
// scripts during *dynamic* per-request rendering. Static pages (login, landing)
// would ship nonce-less scripts while the header carried 'strict-dynamic' —
// which disables 'self' — so every script gets blocked and the page renders
// blank. 'unsafe-inline' is the only script-src that works for a statically
// rendered app; the remaining directives keep the rest of the hardening.
// style-src keeps 'unsafe-inline' (Next/Tailwind inject inline <style>).
// 'unsafe-eval' is dev-only (webpack HMR / React refresh use eval).
function buildCsp(): string {
  const dev = process.env.NODE_ENV !== 'production';
  return [
    "default-src 'self'",
    `script-src 'self' 'unsafe-inline'${dev ? " 'unsafe-eval'" : ''}`,
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "img-src 'self' data: blob: https:",
    "font-src 'self' data: https://fonts.gstatic.com",
    // Same-origin API ('self'), plus the workspace hosts landing/CTA flows post to.
    "connect-src 'self' https://my.transport.tinycio.com https://my.transport.tinycio.ma https://my.transport.tinycio.ru https://my.transport.tinycio.es",
    // The explainer videos are served by Bunny Stream (components/landing/videos.ts).
    // Named hosts, not `https:` — media-src is the directive that decides what
    // a <video> may load, and a wildcard there lets any injected markup play
    // anything. The hosts (the Bunny one + each verified video.tinycio.*) come
    // from the same manifest the pages read, so a CDN or domain change cannot
    // leave the policy pointing elsewhere than the <video> does.
    `media-src 'self' blob: ${VIDEO_HOSTS.map((h) => `https://${h}`).join(' ')}`,
    "worker-src 'self' blob:",
    // frame-src has to be spelled out, and blob: has to be in it. The document
    // previews (/documents/orders, /invoicing) fetch a Bearer-authenticated PDF
    // and show it through an object URL — a browser attaches no token to an
    // <iframe src>, so there is no other way to render the file the client
    // actually receives. Without this directive the frame falls back to
    // default-src 'self', which rejects blob: and leaves a silent white pane:
    // the bons register shipped that way and the console error was the only
    // sign of it.
    "frame-src 'self' blob:",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'",
    ...(dev ? [] : ['upgrade-insecure-requests']),
  ].join('; ');
}

function isPublicPath(pathname: string): boolean {
  // Strip locale prefix (/fr/, /ar/, etc.) before checking.
  const stripped = pathname.replace(LOCALE_PREFIX_RE, '');
  if (stripped === '' || stripped === '/') return true; // / = landing page, public
  return PUBLIC_PATHS.some((p) => stripped === p || stripped.startsWith(p + '/'));
}

export default async function middleware(req: NextRequest) {
  const { pathname } = req.nextUrl;
  const hostname = req.headers.get('host') ?? '';

  // ── CSP ──────────────────────────────────────────────────────────────────
  // `withCsp` stamps the enforced header on every response we return.
  const csp = buildCsp();
  const withCsp = <T extends NextResponse>(res: T): T => {
    res.headers.set('Content-Security-Policy', csp);
    return res;
  };

  // ── Skip auth/locale gating for /api/*, /_next/*, static assets ──────────
  // These still get the CSP header; only the gating below is skipped.
  if (
    pathname.startsWith('/api/') ||
    pathname.startsWith('/_next/') ||
    pathname.startsWith('/healthz') ||
    pathname.includes('.')
  ) {
    return withCsp(NextResponse.next());
  }

  // ── Locale resolution: saved choice → domain TLD ─────────────────────────
  // A persisted NEXT_LOCALE cookie wins. It is written only on an EXPLICIT
  // user choice (login BFF when user.locale is set, or the topbar language
  // switch), so a returning user keeps their language across prefix-less
  // visits. With no cookie we fall back to the domain TLD; browser
  // Accept-Language is ignored either way.
  const cookieLocale = req.cookies.get('NEXT_LOCALE')?.value;
  const savedLocale =
    cookieLocale && routing.locales.includes(cookieLocale as (typeof routing.locales)[number])
      ? (cookieLocale as (typeof routing.locales)[number])
      : null;
  const hostLocale = savedLocale ?? getHostLocale(hostname);
  if (!LOCALE_PREFIX_RE.test(pathname)) {
    const url = req.nextUrl.clone();
    url.pathname = `/${hostLocale}${pathname === '/' ? '' : pathname}`;
    return withCsp(NextResponse.redirect(url));
  }

  // ── Auth gate for workspace routes ────────────────────────────────────────
  if (!isPublicPath(pathname)) {
    const at = req.cookies.get('matransports_at')?.value;
    const ctxRaw = req.cookies.get('matransports_ctx')?.value;
    // The refresh token is httpOnly and lives thirty days: while it is here the
    // session is recoverable, and the client recovers it on mount
    // (hooks/useAutoRefresh). Bouncing to /login on a fifteen-minute-old access
    // cookie was how a dispatcher lost a dossier they had been filling for
    // twenty minutes (live acceptance 2026-09-06). No data hangs on this gate —
    // every byte of the portal comes from the API against the bearer.
    const recoverable = Boolean(req.cookies.get('matransports_rt')?.value);

    let authenticated = false;
    if (at && ctxRaw) {
      try {
        const ctx = JSON.parse(ctxRaw) as { expires_at: number };
        authenticated = ctx.expires_at > Math.floor(Date.now() / 1000);
      } catch {
        authenticated = false;
      }
    }

    if (!authenticated && !recoverable) {
      // Preserve the requested URL so login can redirect back after auth.
      const loginUrl = req.nextUrl.clone();
      loginUrl.pathname = `/${hostLocale}/login`;
      loginUrl.search = '';
      loginUrl.searchParams.set('next', pathname);
      const res = NextResponse.redirect(loginUrl);
      res.cookies.delete('matransports_at');
      res.cookies.delete('matransports_ctx');
      return withCsp(res);
    }
  }

  // ── next-intl ─────────────────────────────────────────────────────────────
  return withCsp(intlMiddleware(req));
}

// Exclude /healthz (container probes), /api/*, /_next/*, static files.
export const config = {
  matcher: ['/((?!api|_next|_vercel|healthz|.*\\..*).*)'],
};
