const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => chromium.launch());
  const errs = [];
  for (const [w, h, tag] of [[1200, 900, 'd'], [400, 800, 'm']]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h } });
    const p = await ctx.newPage();
    p.on('console', m => { if (m.type() === 'error' && !/fonts\.g|ERR_|Failed to load resource/.test(m.text())) errs.push(tag + ' console: ' + m.text()); });
    p.on('pageerror', e => errs.push(tag + ' pageerror: ' + e.message));
    await p.route(/fonts\.(googleapis|gstatic)\.com/, r => r.abort());
    await p.goto('http://127.0.0.1:8765/index.html'); await p.waitForTimeout(1200);
    const ov = async name => { const o = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth); if (o > 0) errs.push(tag + ' overflow ' + name + ' ' + o); };
    await p.screenshot({ path: `s-${tag}-news.png` }); await ov('news');
    console.log(tag, 'items', await p.locator('.item').count(), 'days', await p.locator('.dayh').count(), 'sub:', await p.locator('#sub').textContent(), 'badge:', await p.locator('#tab-news .badge').textContent());
    // open Toshiba detail
    await p.locator('.dbtn').first().click(); await p.waitForTimeout(300);
    const row = p.locator('.item:has(.dwrap)'); await row.scrollIntoViewIfNeeded();
    await row.screenshot({ path: `s-${tag}-detail.png` }); await ov('detail');
    console.log(tag, 'detail chars', (await row.locator('.dwrap').innerText()).length, 'cco', await row.locator('.cco').count(), 'hyp', await row.locator('.hyp').count());
    // check detail on first item, read on second, filter chips
    await p.locator('.item .ck input').first().check(); await p.waitForTimeout(200);
    await p.locator('.item .read').nth(1).click(); await p.waitForTimeout(200);
    console.log(tag, 'bar hidden?', await p.locator('#reqbar').isHidden(), 'n-detail', await p.locator('#n-detail').textContent(), 'writes', JSON.stringify(await p.evaluate(() => (window.__writes || []).map(w => [w[0], Object.keys(w[1].ids || {}).length]))));
    await p.locator('#reqcopy').click(); await p.waitForTimeout(200);
    console.log(tag, 'reqmsg:', await p.locator('#reqmsg').textContent(), 'reqtext:', (await p.locator('#reqtext').count()) ? (await p.locator('#reqtext').inputValue()).slice(0, 120) : '(clipboard)');
    await p.evaluate(() => window.scrollTo(0, 0)); await p.screenshot({ path: `s-${tag}-news2.png` });
    await p.locator('.chip', { hasText: '가스·LNG' }).click(); await p.waitForTimeout(200);
    console.log(tag, 'gas items', await p.locator('.item').count());
    await p.locator('.sgb', { hasText: '로이터' }).click(); await p.waitForTimeout(200);
    console.log(tag, 'gas+rtr items', await p.locator('.item').count());
    await p.locator('.basis summary').first().click(); await p.waitForTimeout(100); await ov('basis');
    await p.locator('.item').first().screenshot({ path: `s-${tag}-basis.png` });
    await p.locator('#tab-ind').click(); await p.waitForTimeout(400); await p.screenshot({ path: `s-${tag}-ind.png` }); await ov('ind');
    console.log(tag, 'ind nodes', await p.locator('.node').count());
    // from a flow chip to an old card
    const chip = p.locator('button.src[data-act="gonews"]').first();
    if (await chip.count()) { await chip.click(); await p.waitForTimeout(400); console.log(tag, 'gonews → tab', await p.locator('.navlink[aria-current]').textContent(), 'cardbox', await p.locator('.cardbox').count()); }
    await p.locator('#tab-arch').click(); await p.waitForTimeout(300); await p.evaluate(() => window.scrollTo(0, 0)); await p.screenshot({ path: `s-${tag}-arch.png` }); await ov('arch');
    console.log(tag, 'arch rows', await p.locator('.orow').count(), 'hint:', await p.locator('#arch-hint').textContent());
    await p.locator('#am-all').click(); await p.waitForTimeout(400); console.log(tag, 'old archive details', await p.locator('.arch details').count()); await ov('arch-all');
    await ctx.close();
  }
  console.log('ERRORS', errs.length, errs.join('\n'));
  await b.close();
})();
