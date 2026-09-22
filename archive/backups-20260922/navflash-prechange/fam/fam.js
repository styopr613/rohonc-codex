/* OONA family bar — injected identically on every OONA property.
   Include on any page:  <link rel="stylesheet" href="https://oona13.com/fam/fam.css">
                         <script src="https://oona13.com/fam/fam.js" defer></script>
   Edit the LIST here (and only here).
   <script src=".../fam.js" data-oona="veil"> = transitions only, no bar (Cover Maker / Book Maker
   keep their own product menu). The veil needs no fam.css: it carries its own rules. */
(function () {
  if (document.getElementById('oona-root')) return;
  var cs = document.currentScript, BAR = !(cs && cs.getAttribute('data-oona') === 'veil');
  var DARK = '#0B0D10';
  // Light properties and their page colour. Also listed in the inline referrer snippet that light
  // pages carry in <head> (see OONA13.md "Page transitions"): keep the two lists identical.
  var LIGHT = [['oona13.com/library', '#faf7f0'], ['oona13.com/guides', '#f4f1ea'], ['oona13.com/cover-tools', '#f4f1ea'],
               ['oona13.com/book-tools', '#f6f2ea'], ['covermaker.oona13.com', '#f7f4ee'], ['bookmaker.oona13.com', '#f6f3ec']];
  function lightOf(u) { var k = u.host + u.pathname; for (var i = 0; i < LIGHT.length; i++) { var p = LIGHT[i][0]; if (k === p || k === p + '/' || k.indexOf(p + '/') === 0) return LIGHT[i][1]; } return null; }
  var TOP = [                                   // the brand itself is the link to the novel's home
    ['Archive', 'https://oona13.com/archive'],
    ['Free Library', 'https://oona13.com/library/'],
    ['Guides', 'https://oona13.com/guides/'],
    ['Rohonc', 'https://oona13.com/rohonc/']
  ];
  // The general site footer, drawn under the experiments block by fam/foot.js. One source of
  // truth for that row. NOTE: src/app/(book)/BookPage.tsx keeps its own copy for the novel's own
  // footer — it is React and cannot read this file — so if this list changes, change that too.
  var SITE = [
    ['Read Online', 'https://oona13.com/books/oona-13'],
    ['Kindle', 'https://www.amazon.com/dp/B0FC5QHX68'],
    ['Paperback', 'https://www.amazon.com/dp/B0FD8Y4QBX'],
    ['Free Library', 'https://oona13.com/library/'],
    ['Cover Maker', 'https://covermaker.oona13.com/'],
    ['Book Maker', 'https://bookmaker.oona13.com/']
  ];
  var GROUPS = [
    { label: 'Make your book', items: [
      ['Cover Maker', 'https://covermaker.oona13.com/'],
      ['Book Maker', 'https://bookmaker.oona13.com/'],
      ['Cover tools', 'https://oona13.com/cover-tools/'],
      ['Book tools', 'https://oona13.com/book-tools']
    ]},
    // In the order of the argument (2026-09-13): the triangle in the circle → one point going round
    // and the wave is its shadow → ten thousand of those waves make a creature → the wave leaves the
    // page as radio → you tune one in. The clock is its own thing and sits last.
    // SOH CAH TOA is the third section OF the Sine wave page (2026-09-13); its old address redirects there.
    { label: 'Extras', heading: 'Science experiments', items: [
      ['Shortwave', 'https://oona13.com/shortwave/'],        // the radio first: owner, "they are the coolest"
      ['How radio works', 'https://oona13.com/shortwave/learn/'],
      ['Sine wave', 'https://oona13.com/math/trigdemo.html'],
      ['Math art', 'https://oona13.com/math/mathart.html'],
      ['Infinity Clock', 'https://oona13.com/timeclock']
    ]}
  ];

  // The experiment pages build their footer from this same list (see fam/foot.js) — one source of truth.
  var EX = GROUPS.filter(function (g) { return g.label === 'Extras'; })[0];
  window.OONA_EXTRAS = EX ? EX.items : [];
  window.OONA_SITE = SITE;

  var here = location.host + location.pathname.replace(/\/+$/, '');
  function isHere(href) {
    var u = href.replace(/^https?:\/\//, '').replace(/\/+$/, '');
    if (u === 'oona13.com') return here === 'oona13.com';             // the novel's home only
    return here === u || here.indexOf(u + '/') === 0;
  }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function link(it, cls) { return '<a href="' + it[1] + '" class="' + (cls || '') + (isHere(it[1]) ? ' here' : '') + '">' + esc(it[0]) + '</a>'; }

  var html = '<a class="brand' + (isHere('https://oona13.com/') ? ' here' : '') + '" href="https://oona13.com/">OONA 13</a>';
  TOP.forEach(function (it) { html += link(it, 'top'); });
  GROUPS.forEach(function (g) {
    var open = g.items.some(function (it) { return isHere(it[1]); });
    html += '<span class="grp' + (open ? ' here' : '') + '"><button type="button" aria-haspopup="true" aria-expanded="false">' + esc(g.label) + '<small>&#9662;</small></button><span class="pop" role="menu">'
      + (g.heading ? '<b>' + esc(g.heading) + '</b>' : '') + g.items.map(function (it) { return link(it); }).join('') + '</span></span>';
  });
  html += '<span class="sp"></span><button type="button" class="burger" aria-haspopup="true" aria-expanded="false" aria-label="Menu"><span class="bx"><b></b><b></b><b></b></span><span class="bw">Menu</span></button>';
  // Phone drawer (2026-09-09, after NN/g + Smashing reading): a side sheet with a scrim, 48px rows, the page's own
  // sections first, the five family destinations as plain rows, and the two groups as accordions — the group holding
  // the current page starts open, the other stays folded, so the sheet is ~9 rows instead of a 20-link wall.
  var drawer = '<span class="local"></span>' + link(['OONA 13 · Home', 'https://oona13.com/'], 'row') + TOP.map(function (it) { return link(it, 'row'); }).join('');
  GROUPS.forEach(function (g) {
    var open = g.items.some(function (it) { return isHere(it[1]); });
    drawer += '<details class="acc"' + (open ? ' open' : '') + '><summary>' + esc(g.heading || g.label) + '<small>&#9662;</small></summary>' + g.items.map(function (it) { return link(it, 'row sub'); }).join('') + '</details>';
  });
  html += '<div class="scrim"></div><div class="drawer" role="dialog" aria-label="Menu">' + drawer + '</div>';

  // ONE foreign node at the top of <body> holds both the bar and the veil. It is a custom tag on
  // purpose: React (Next.js pages hydrate the whole document) only claims a DOM node whose tag
  // matches what it rendered; a <div> here got claimed, mismatched and wiped. <oona-root> never.
  var root = document.createElement('oona-root'); root.id = 'oona-root';
  var bar = null;
  if (BAR) {
    bar = document.createElement('nav');
    bar.id = 'oona-fam'; bar.setAttribute('aria-label', 'OONA family'); bar.innerHTML = html;
    var grps = bar.querySelectorAll('.grp'); if (grps.length) grps[grps.length - 1].classList.add('last');
    root.appendChild(bar);
    document.documentElement.classList.add('oona-fam-on'); document.body.classList.add('oona-fam-on');
  }
  document.body.insertBefore(root, document.body.firstChild);

  // ONE hamburger on phones (owner 2026-09-09: "two competing menus … need a hamburger with everything").
  // A page hands its own sections to the drawer: window.OONA_FAM.local('This page', [['Story', '#story'], …]).
  // They sit above the family list; the page hides its own phone menu. Desktop is untouched — the bar
  // stays the family, the page keeps its own nav.
  window.OONA_FAM = { local: function (heading, items) {
    if (!bar) return;
    var box = bar.querySelector('.drawer .local');
    document.documentElement.classList.add('oona-fam-local');   // only THIS script version sets it: a page hides its own phone menu on this class, never on the bar alone (stale cached fam.js must not strand the page's sections)
    box.innerHTML = '<b>' + esc(heading || 'This page') + '</b>' + items.map(function (it) { return link(it, 'row lcl'); }).join('');
  } };
  function closeAll() {
    if (!bar) return;
    bar.querySelectorAll('.grp').forEach(function (g) { g.classList.remove('open'); delete g.dataset.pinned; g.querySelector('button').setAttribute('aria-expanded', 'false'); });
    bar.classList.remove('open'); bar.querySelector('.burger').setAttribute('aria-expanded', 'false');
    document.documentElement.classList.remove('oona-menu-open');
  }
  var timer = null;
  function open(g) { clearTimeout(timer); closeAll(); g.classList.add('open'); g.querySelector('button').setAttribute('aria-expanded', 'true'); }
  if (BAR) bar.querySelectorAll('.grp').forEach(function (g) {
    var b = g.querySelector('button');
    // click pins the panel open until an outside click / Esc; hover opens and closes with a grace period
    b.addEventListener('click', function (e) { e.stopPropagation(); var was = g.classList.contains('open') && g.dataset.pinned; closeAll(); if (!was) { open(g); g.dataset.pinned = '1'; } });
    g.addEventListener('mouseenter', function () { if (!g.classList.contains('open')) open(g); else clearTimeout(timer); });
    g.addEventListener('mouseleave', function () { if (g.dataset.pinned) return; clearTimeout(timer); timer = setTimeout(function () { g.classList.remove('open'); b.setAttribute('aria-expanded', 'false'); }, 260); });
  });
  if (BAR) bar.querySelector('.burger').addEventListener('click', function (e) { e.stopPropagation(); var was = bar.classList.contains('open'); closeAll(); if (!was) { bar.classList.add('open'); this.setAttribute('aria-expanded', 'true'); document.documentElement.classList.add('oona-menu-open'); } });
  if (BAR) bar.querySelector('.scrim').addEventListener('click', function (e) { e.stopPropagation(); closeAll(); });
  document.addEventListener('click', function (e) { if (bar && !bar.contains(e.target)) closeAll(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(); });

  // ---- transitions. A veil covers the page at first paint and fades away (.6s, Fluency's ease-out);
  // on any click to an OONA host it fades back (.17s) before navigating. Content is never made
  // transparent. The veil's colour is the colour the page ARRIVED painted in (the inline
  // html{background} in <head>, which light pages decide from document.referrer: coming from a
  // dark OONA site → arrive dark and light up; from a light one or from outside → arrive in their
  // own colour). Leaving: light → light fades to the destination's cream, anything else fades to
  // dark. So light↔light never passes through black, and dark↔light always does. ----
  function clear(c) { return !c || c === 'transparent' || c === 'rgba(0, 0, 0, 0)'; }
  function paintedBg() {                     // what the canvas is painted right now
    var c = getComputedStyle(document.documentElement).backgroundColor;
    if (clear(c)) c = getComputedStyle(document.body).backgroundColor;
    return clear(c) ? DARK : c;
  }
  function lum(c) {                          // 0..1 from rgb()/#hex
    var m = /rgba?\((\d+),\s*(\d+),\s*(\d+)/.exec(c); if (!m) { m = /^#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i.exec(c); if (!m) return 0; m = [0, parseInt(m[1], 16), parseInt(m[2], 16), parseInt(m[3], 16)]; }
    return (0.2126 * m[1] + 0.7152 * m[2] + 0.0722 * m[3]) / 255;
  }
  var arrived = paintedBg();
  function tone(c) { return lum(c) > 0.5 ? 'light' : 'dark'; }
  function ownColour() {                     // the page's real colour (a light page may be painted dark on arrival)
    var p = document.getElementById('oona-paint'); return (p && p.getAttribute('data-bg')) || paintedBg();
  }
  function urlTone(href) { try { return tone(lightOf(new URL(href, location.href)) || DARK); } catch (x) { return 'dark'; } }
  // Same-origin navigations: the browser's cross-document View Transition does the work (fam.css /
  // prodhead.css opt in; the bar/header is a named group so it stays painted). We step aside:
  // no veil on the way out, and on the way in the veil is dropped in `pagereveal` — which fires
  // before the new page is captured — so the cross-fade goes straight to the real page.
  var VT = 'CSSViewTransitionRule' in window;
  var css = document.createElement('style'); css.id = 'oona-veil-css';
  css.textContent = '#oona-veil{position:fixed;inset:0;z-index:2147482998;pointer-events:none;opacity:1;background:' + DARK + '}'
    + '#oona-veil.in{animation:oona-veil-in .6s cubic-bezier(.23,1,.32,1) forwards}@keyframes oona-veil-in{from{opacity:1}to{opacity:0}}'
    + '#oona-veil.in.lift{animation-duration:.9s;animation-timing-function:cubic-bezier(.5,0,.4,1)}'   /* dark -> light: ease in AND out, no snap */
    + '#oona-veil.out{animation:none;opacity:0;transition:opacity .17s ease-in}html.oona-leaving #oona-veil.out{opacity:1}'
    + '@media (prefers-reduced-motion:reduce){#oona-veil{display:none !important}}';
  document.head.appendChild(css);
  function unpaint() {                       // hand the canvas back to the page's real colour
    var p = document.getElementById('oona-paint'); if (!p) return;
    var bg = p.getAttribute('data-bg');
    if (bg) p.textContent = 'html{background:' + bg + '}'; else p.parentNode.removeChild(p);
  }
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var veil = document.createElement('div'); veil.id = 'oona-veil'; veil.style.background = arrived;
  root.appendChild(veil);
  var vtArrived = false;
  // The browser's own cross-document transition is used ONLY between two pages of the same tone
  // (dark->dark, light->light) — Fluency's case. A dark<->light hop skips it on both ends and
  // uses the veil instead (2026-09-07: the owner's Chrome 151 showed a white flash on those hops).
  window.addEventListener('pageswap', function (e) {
    if (!e.viewTransition || !e.activation || !e.activation.entry) return;
    if (urlTone(e.activation.entry.url) !== tone(ownColour())) e.viewTransition.skipTransition();
  });
  window.addEventListener('pagereveal', function (e) {          // fires before first render, before the rAF below
    if (!e.viewTransition) return;
    var fromTone = 'dark'; try { if (document.referrer) fromTone = urlTone(document.referrer); } catch (x) {}
    if (fromTone !== tone(ownColour())) { e.viewTransition.skipTransition(); return; }   // veil path lights it up
    vtArrived = true; veil.classList.add('out'); unpaint();
  });
  if (reduce) { veil.remove(); unpaint(); }
  else {
    requestAnimationFrame(function () {
      if (vtArrived) return;
      var p = document.getElementById('oona-paint'), lift = !!(p && p.getAttribute('data-bg') && /#0B0D10/i.test(p.textContent));
      unpaint(); veil.classList.add('in'); if (lift) veil.classList.add('lift');   // both under the opaque veil
    });
    veil.addEventListener('animationend', function () { veil.classList.remove('in'); veil.classList.add('out'); });
  }
  var bypass = false, navigating = false;
  document.addEventListener('click', function (e) {
    if (bypass) return;
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    if ((a.target && a.target !== '_self') || a.hasAttribute('download')) return;
    var u; try { u = new URL(a.href, location.href); } catch (x) { return; }
    if (u.protocol !== 'http:' && u.protocol !== 'https:') return;
    var inBar = bar && bar.contains(a);
    if (inBar && u.href.split('#')[0] === location.href.split('#')[0]) {   // the bar's link to the page you are on: no reload, no transition, just the top (or the section, for a page's own #anchor)
      e.preventDefault(); closeAll();
      var sec = u.hash && u.hash.length > 1 ? document.getElementById(decodeURIComponent(u.hash.slice(1))) : null;
      try { sec ? sec.scrollIntoView({ behavior: 'smooth', block: 'start' }) : window.scrollTo({ top: 0, behavior: 'smooth' }); } catch (x) { sec ? sec.scrollIntoView() : window.scrollTo(0, 0); }
      return;
    }
    if (inBar) closeAll();
    if (u.href.split('#')[0] === location.href.split('#')[0]) return;
    if (navigating) { e.preventDefault(); return; }                        // one navigation at a time: a double press must not start a second one
    if (reduce) return;
    if (!/(^|\.)oona13\.com$/.test(u.hostname)) return;
    a.referrerPolicy = 'no-referrer-when-downgrade';   // within the family, send the full URL: the next page reads it to pick its arrival colour
    if (!inBar && window.next && u.host === location.host) return;   // the site's own links: Next routes them client-side
    if (VT && u.origin === location.origin && urlTone(u.href) === tone(ownColour())) { navigating = true; return; }   // same origin + same tone: native view transition (Fluency's case)
    navigating = true;
    e.preventDefault();
    var pageNow = getComputedStyle(document.body).backgroundColor; if (clear(pageNow)) pageNow = paintedBg();
    var dest = lightOf(u);
    veil.style.background = (dest && lum(pageNow) > 0.5) ? dest : DARK;
    if (!veil.parentNode) root.appendChild(veil);
    veil.classList.remove('in'); veil.classList.add('out');
    void veil.offsetWidth;
    document.documentElement.classList.add('oona-leaving');
    // navigate through the anchor itself (not location.href) so its referrerPolicy applies and the
    // next page sees the full URL we came from; `bypass` lets that synthetic click through this handler
    setTimeout(function () { bypass = true; try { a.click(); } finally { bypass = false; } }, 180);
  }, true);
  // (Speculation-rules prefetch was here 2026-09-06/07 and removed: on the owner's Chrome 151 every
  //  hover-prefetched navigation showed a white flash that no local Chromium reproduced.)
  window.addEventListener('pageshow', function (ev) {
    navigating = false;
    document.documentElement.classList.remove('oona-leaving');
    if (ev.persisted) { veil.classList.remove('in'); veil.classList.add('out'); }
  });
})();
