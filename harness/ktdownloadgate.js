// Download-then-click gate for the public site. Bar: after clicking the EPUB link on a
// page, the page must NOT be left "leaving" (fam.js's navigation flag set, veil up), and
// the next button on the page must still navigate. Declared 2026-09-23 after the owner
// reported that every button died once Download had been pressed: fam.js set
// `navigating` on the click and waited for a page that never came, because a download
// never leaves the page. FAILED on both pages before the fix (watchdog in fam.js +
// `download` on the site's EPUB anchors), PASSES after.
//
// Not in gates.txt: it needs the live site and a Playwright Chromium. Run it by hand
// after any change to fam.js, to the site's button rows, or to what the EPUB URL serves:
//
//   NODE_PATH=/home/ubuntu/character-playground/node_modules \
//     node ktdownloadgate.js https://oona13.com/rohonc/read.html
//   STRIP=1 ...   also removes the `download` attribute first, so the shared script's
//                 watchdog is what is being tested, not the attribute
//
// Exit 0 = PASS, 1 = FAIL. Default page: the read page; the front page has the same row.
const { chromium } = require('playwright');
(async () => {
  const url = process.argv[2] || 'https://oona13.com/rohonc/read.html';
  const b = await chromium.launch(); const ctx = await b.newContext({ acceptDownloads: true });
  const p = await ctx.newPage(); await p.goto(url, { waitUntil: 'networkidle' });
  if (process.env.STRIP) await p.evaluate(() => document.querySelectorAll('a[href$=".epub"]').forEach(a => a.removeAttribute('download')));
  const dl = p.waitForEvent('download', { timeout: 8000 }).catch(() => null);
  await p.click('a[href$=".epub"]');
  const d = await dl; console.log('download event:', d ? 'yes ' + d.suggestedFilename() : 'NO');
  await p.waitForTimeout(3000);   // longer than fam.js's 2.5s watchdog
  const st = await p.evaluate(() => ({ leaving: document.documentElement.classList.contains('oona-leaving'),
    veil: (v => v ? getComputedStyle(v).opacity : 'none')(document.getElementById('oona-veil')), url: location.href }));
  console.log('after download click:', JSON.stringify(st));
  await p.click('a.go'); await p.waitForTimeout(2500);
  console.log('after clicking the next button, url:', p.url());
  const ok = !st.leaving && st.veil !== '1' && p.url() !== url;
  console.log(ok ? '[download] PASS' : '[download] FAIL');
  await b.close(); process.exit(ok ? 0 : 1);
})();
