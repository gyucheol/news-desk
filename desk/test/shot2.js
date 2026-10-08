const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const [w, h, tag] of [[1200, 1000, 'd'], [400, 860, 'm']]) {
    const p = await (await b.newContext({ viewport: { width: w, height: h } })).newPage();
    await p.route(/fonts\.(googleapis|gstatic)\.com/, r => r.abort());
    await p.goto('http://127.0.0.1:8765/index.html'); await p.waitForTimeout(1200);
    await p.screenshot({ path: `t-${tag}-1.png` });
    await p.locator('.dbtn').first().click(); await p.waitForTimeout(300);
    for (const [sel, n] of [['.dwrap', 2], ['.vc', 3], ['.hyps', 4], ['.cco', 5], ['.picks', 6]]) {
      await p.locator(sel).first().evaluate(el => { const r = el.getBoundingClientRect(); window.scrollTo(0, window.scrollY + r.top - 90); }); await p.waitForTimeout(150);
      await p.screenshot({ path: `t-${tag}-${n}.png` });
    }
    console.log(tag, 'overflow', await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth), 'chips', await p.locator('#nb-ind').innerText());
  }
  await b.close();
})();
