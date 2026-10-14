/* maTransports explainer motion kit — one motion feel for every scene.
   Smooth long-tail decel (power3.out) for arrivals, power2.inOut for travel, no bounce, no loops.
   Every helper ADDS tweens to the scene's paused timeline at an absolute scene-local time. */
window.K = (function () {
  const OUT = "power3.out", MOVE = "power2.inOut", IN = "power2.in";

  /** Scene entrance: the whole camera arrives from slight depth. Runs in [at, at+0.75]. */
  function camIn(tl, cam, at = 0) {
    tl.fromTo(cam, { opacity: 0, scale: 0.965, filter: "blur(10px)" },
      { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.75, ease: OUT }, at);
  }
  /** Scene exit: push through, toward the viewer. Starts at T.out, lasts 0.5 s. */
  function camOut(tl, cam, at) {
    tl.to(cam, { opacity: 0, scale: 1.035, filter: "blur(10px)", duration: 0.5, ease: IN }, at);
  }

  /** Wrap each word of el's text in <span class="w"> (keeps spaces). Call once, before building tweens. */
  function splitWords(el) {
    const text = el.textContent;
    el.textContent = "";
    text.split(/(\s+)/).forEach((part) => {
      if (!part) return;
      if (/^\s+$/.test(part)) { el.appendChild(document.createTextNode(" ")); return; }
      const s = document.createElement("span");
      s.className = "w";
      s.textContent = part;
      el.appendChild(s);
    });
    return el.querySelectorAll(".w");
  }

  /** Lower-third title (.k-title > .k-title-bar + .k-title-text): bar grows, words rise. */
  function title(tl, root, at) {
    const bar = root.querySelector(".k-title-bar");
    const text = root.querySelector(".k-title-text");
    const words = text.querySelectorAll(".w").length ? text.querySelectorAll(".w") : splitWords(text);
    tl.fromTo(root, { opacity: 0 }, { opacity: 1, duration: 0.2, ease: "none" }, at);
    tl.fromTo(bar, { scaleY: 0 }, { scaleY: 1, duration: 0.5, ease: OUT }, at);
    tl.fromTo(words, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.65, ease: OUT, stagger: 0.055 }, at + 0.1);
  }
  function titleOut(tl, root, at) {
    tl.to(root, { opacity: 0, y: -16, duration: 0.4, ease: IN }, at);
  }

  /** Staggered arrival from below (cards, rows, labels). */
  function rise(tl, els, at, o = {}) {
    tl.fromTo(els, { opacity: 0, y: o.y ?? 28 }, { opacity: 1, y: 0, duration: o.d ?? 0.7, ease: OUT, stagger: o.stagger ?? 0.09 }, at);
  }
  /** Small element appearing in place (chips, badges, callouts) — smooth settle, no overshoot. */
  function pop(tl, el, at, o = {}) {
    tl.fromTo(el, { opacity: 0, scale: o.from ?? 0.7 }, { opacity: 1, scale: 1, duration: o.d ?? 0.45, ease: OUT }, at);
  }
  function fadeOut(tl, el, at, d = 0.35) {
    tl.to(el, { opacity: 0, duration: d, ease: IN }, at);
  }

  /** Cursor travel (cursor is absolutely positioned at 0,0 and moved with x/y). */
  function cursorTo(tl, cur, x, y, at, d = 0.85) {
    tl.to(cur, { x, y, duration: d, ease: MOVE }, at);
  }
  /** Click: cursor dips, target presses, ripple expands at (rx, ry) if given. */
  function click(tl, cur, target, at, ripple, rx, ry) {
    tl.to(cur, { scale: 0.84, duration: 0.09, ease: "power2.out" }, at)
      .to(cur, { scale: 1, duration: 0.22, ease: "power2.out" }, at + 0.09);
    if (target) {
      tl.to(target, { scale: 0.965, duration: 0.09, ease: "power2.out" }, at)
        .to(target, { scale: 1, duration: 0.28, ease: "power2.out" }, at + 0.09);
    }
    if (ripple) {
      // set + to (not fromTo): a fromTo renders its start state immediately, which would show the
      // ripple at 0,0 from t=0 until the click. A timeline set at `at` reverts cleanly when seeking back.
      const start = { opacity: 0.95, scale: 0.25 };
      if (rx !== undefined) { start.x = rx; start.y = ry; }
      tl.set(ripple, start, at);
      tl.to(ripple, { opacity: 0, scale: 1.7, duration: 0.65, ease: "power2.out" }, at);
    }
  }

  /** Product amount format: fr-FR grouping with a plain space, 2 decimals — in every locale (InvoicesView.formatAmount). */
  function fmtAmount(v, dec = 2) {
    const neg = v < 0; v = Math.abs(v);
    const fixed = v.toFixed(dec);
    let [i, f] = fixed.split(".");
    i = i.replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return (neg ? "− " : "") + i + (dec ? "," + f : "");
  }
  /** Count a number up inside el; el's authored text must already be the start value. */
  function count(tl, el, from, to, at, d, fmt = fmtAmount) {
    const o = { v: from };
    tl.fromTo(o, { v: from }, { v: to, duration: d, ease: "power2.out", onUpdate: () => { el.textContent = fmt(o.v); } }, at);
  }

  /** Swap two stacked elements in place (old slides up and out, new rises in). */
  function swap(tl, oldEl, newEl, at, d = 0.45) {
    tl.to(oldEl, { opacity: 0, y: -18, duration: d * 0.8, ease: IN }, at);
    tl.fromTo(newEl, { opacity: 0, y: 18 }, { opacity: 1, y: 0, duration: d + 0.15, ease: OUT }, at + d * 0.45);
  }

  /** A deterministic tiny jitter for a held element (the only sanctioned "aliveness"). */
  function jitter(tl, el, at, d, amp = 1.5) {
    const n = Math.max(1, Math.floor(d / 0.12));
    for (let i = 0; i < n; i++) {
      const s = Math.sin(i * 12.9898) * 43758.5453; const r = s - Math.floor(s);
      tl.to(el, { x: (r - 0.5) * 2 * amp, y: ((r * 7) % 1 - 0.5) * 2 * amp, duration: 0.12, ease: "none" }, at + i * 0.12);
    }
    tl.to(el, { x: 0, y: 0, duration: 0.12, ease: "none" }, at + n * 0.12);
  }

  return { OUT, MOVE, IN, camIn, camOut, splitWords, title, titleOut, rise, pop, fadeOut, cursorTo, click, fmtAmount, count, swap, jitter };
})();
