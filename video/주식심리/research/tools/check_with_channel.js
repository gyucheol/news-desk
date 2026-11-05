// 주제 조사용 조회수 확인 도구 (2026-11-05, 주식 심리 편). Read-only checker for topic research (same source as video/tools/youtube_views.js:
// the public mattw.io YouTube Metadata page = official YouTube Data API values; youtube.com is not opened).
// Adds duration and the channel totals shown on the same page.
// usage: node check_with_channel.js OUT.jsonl ID [ID...]   (skips IDs that already have a view count in any check*.jsonl next to OUT)
const { chromium } = require('playwright');
const fs = require('fs');
function pickStr(text, key, from = 0) {
  const re = new RegExp('"' + key + '":\\s*"((?:[^"\\\\]|\\\\.)*)"', 'g'); re.lastIndex = from;
  const m = re.exec(text); if (!m) return null;
  try { return JSON.parse('"' + m[1] + '"'); } catch (e) { return m[1]; }
}
async function one(page, id) {
  const url = 'https://mattw.io/youtube-metadata/?url=' + encodeURIComponent('https://www.youtube.com/watch?v=' + id) + '&submit=true';
  await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForTimeout(2500);
  const text = await page.innerText('body');
  const view = text.match(/"viewCount":\s*"(\d+)"/);
  const si = text.indexOf('"subscriberCount"');
  let ch = {};
  if (si > 0) {
    const seg = text.slice(Math.max(0, si - 300), si + 300);
    const cv = seg.match(/"viewCount":\s*"(\d+)"/), cs = seg.match(/"subscriberCount":\s*"(\d+)"/), cn = seg.match(/"videoCount":\s*"(\d+)"/);
    ch = { chViews: cv ? +cv[1] : null, chSubs: cs ? +cs[1] : null, chVideos: cn ? +cn[1] : null };
  }
  return { id, title: pickStr(text, 'title'), channel: pickStr(text, 'channelTitle'), channelId: pickStr(text, 'channelId'),
    publishedAt: pickStr(text, 'publishedAt'), viewCount: view ? +view[1] : null, duration: pickStr(text, 'duration'),
    ...ch, checkedAt: new Date().toISOString() };
}
(async () => {
  const [out, ...ids0] = process.argv.slice(2);
  const done = new Set();
  const dir = require('path').dirname(out);
  for (const f of fs.readdirSync(dir).filter(f => /^check.*\.jsonl$/.test(f)))
    for (const l of fs.readFileSync(dir + '/' + f, 'utf8').split('\n')) { try { const j = JSON.parse(l); if (j.viewCount != null) done.add(j.id); } catch (e) {} }
  const ids = [...new Set(ids0)].filter(i => !done.has(i));
  const browser = await chromium.launch();
  const N = 3; let k = 0;
  await Promise.all([...Array(N)].map(async () => {
    const page = await browser.newPage();
    while (k < ids.length) {
      const id = ids[k++];
      let r = null;
      for (let t = 0; t < 2 && !(r && r.viewCount != null); t++) {
        try { r = await one(page, id); } catch (e) { r = { id, error: String(e.message || e).slice(0, 120) }; }
      }
      fs.appendFileSync(out, JSON.stringify(r) + '\n');
    }
  }));
  await browser.close();
})();
