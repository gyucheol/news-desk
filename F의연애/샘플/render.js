// Deterministic renderer: loads an HTML page that exposes window.renderFrame(t) and window.DURATION,
// screenshots every frame and pipes PNGs into ffmpeg (H.264, yuv420p, no audio).
const { chromium } = require('playwright');
const { spawn } = require('child_process');
(async () => {
  const [html, out, fpsArg, onlyFrames] = process.argv.slice(2);
  const fps = parseInt(fpsArg || '30');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await page.goto('file://' + html);
  await page.evaluate(() => document.fonts.ready);
  const dur = await page.evaluate(() => window.DURATION);
  if (onlyFrames) { // preview stills: comma-separated seconds
    for (const s of onlyFrames.split(',')) {
      await page.evaluate(t => window.renderFrame(t), parseFloat(s));
      await page.screenshot({ path: `${out}_${s}.png` });
    }
    await browser.close(); return;
  }
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const n = Math.round(dur * fps);
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => window.renderFrame(t), i / fps);
    const buf = await page.screenshot({ type: 'png' });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 150 === 0) console.log('frame', i, '/', n);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log('done', out);
})();
