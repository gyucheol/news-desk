// 주제 추천의 근거 영상 조회수 확인용 (HANDOFF_SCRIPT.md 3장).
// 유튜브를 직접 긁지 않고, 유튜브 공식 데이터(YouTube Data API)를 보여 주는 공개 도구
// mattw.io/youtube-metadata 화면에서 제목, 채널, 올린 날, 조회수를 읽습니다.
// 쓰는 법: node video/tools/youtube_views.js <영상 ID> [<영상 ID> ...]
// 결과: 영상마다 한 줄 JSON {id, title, channel, publishedAt, viewCount, checkedAt}
const { chromium } = require('playwright');

function pick(text, key) {
  const m = text.match(new RegExp('"' + key + '":\\s*"([^"]*)"'));
  return m ? m[1] : null;
}

(async () => {
  const ids = process.argv.slice(2);
  if (!ids.length) {
    console.error('usage: node youtube_views.js <video id> [...]');
    process.exit(2);
  }
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const id of ids) {
    const url = 'https://mattw.io/youtube-metadata/?url=' +
      encodeURIComponent('https://www.youtube.com/watch?v=' + id) + '&submit=true';
    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
      await page.waitForTimeout(3000);
      const text = await page.innerText('body');
      console.log(JSON.stringify({
        id,
        title: pick(text, 'title'),
        channel: pick(text, 'channelTitle'),
        publishedAt: pick(text, 'publishedAt'),
        viewCount: pick(text, 'viewCount'),
        checkedAt: new Date().toISOString(),
      }));
    } catch (e) {
      console.log(JSON.stringify({ id, error: String(e.message || e) }));
    }
  }
  await browser.close();
})();
