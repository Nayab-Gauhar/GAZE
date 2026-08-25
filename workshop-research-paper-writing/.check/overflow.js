// Detects slides whose content overflows the 720px slide height.
const puppeteer = require('puppeteer-core');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: process.env.CHROME_PATH || '/usr/local/bin/chrome',
    args: ['--no-sandbox', '--disable-dev-shm-usage'],
    headless: true,
  });
  for (const file of process.argv.slice(2)) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 720 });
    await page.goto('file://' + path.resolve(file), { waitUntil: 'networkidle0' });
    const bad = await page.evaluate(() => {
      const out = [];
      document.querySelectorAll('section').forEach((s, i) => {
        // reset marp scaling so we measure natural layout
        const h = s.scrollHeight;
        const ch = s.clientHeight;
        const w = s.scrollWidth;
        const cw = s.clientWidth;
        const title = (s.querySelector('h1') || {}).textContent || '(no h1)';
        if (h > ch + 2 || w > cw + 2) {
          out.push({ n: i + 1, title: title.trim().slice(0, 60), overflowY: h - ch, overflowX: w - cw });
        }
      });
      return out;
    });
    console.log('\n=== ' + path.basename(file) + ' ===');
    if (!bad.length) console.log('  no overflow detected');
    bad.forEach((b) =>
      console.log(`  slide ${String(b.n).padStart(3)}  +${String(b.overflowY).padStart(4)}px Y  +${String(b.overflowX).padStart(3)}px X  ${b.title}`)
    );
  }
  await browser.close();
})();
