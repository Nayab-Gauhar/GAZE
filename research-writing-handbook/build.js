#!/usr/bin/env node
/**
 * Builds the handbook: manual/*.md  ->  build/handbook.html  ->  build/handbook.pdf
 * Generates a table of contents, numbers pages, and reports statistics.
 */
const fs = require('fs');
const path = require('path');
const MarkdownIt = require('markdown-it');
const anchor = require('markdown-it-anchor');

const ROOT = __dirname;
const MANUAL = path.join(ROOT, 'manual');
const BUILD = path.join(ROOT, 'build');

const md = new MarkdownIt({ html: true, linkify: false, typographer: true })
  .use(anchor, { slugify: (s) => s.toLowerCase().replace(/[^\w]+/g, '-').replace(/^-|-$/g, '') });

// ---------------------------------------------------------------- collect
const files = fs.readdirSync(MANUAL).filter((f) => f.endsWith('.md')).sort();
if (!files.length) { console.error('No markdown in manual/'); process.exit(1); }

let source = '';
for (const f of files) source += fs.readFileSync(path.join(MANUAL, f), 'utf8') + '\n\n';

const words = source.replace(/```[\s\S]*?```/g, ' ').split(/\s+/).filter(Boolean).length;

// ---------------------------------------------------------------- headings for TOC
const toc = [];
source.split('\n').forEach((line) => {
  const m = /^(#{1,3})\s+(.+?)\s*$/.exec(line);
  if (!m) return;
  const text = m[2].replace(/<[^>]+>/g, '').trim();
  if (/^(List of|Preface|How to Use)/i.test(text) && m[1].length === 1) return;
  toc.push({ level: m[1].length, text, id: text.toLowerCase().replace(/[^\w]+/g, '-').replace(/^-|-$/g, '') });
});

const tocHtml =
  '<div class="toc"><h1>Table of Contents</h1>' +
  toc.map((h) => `<div class="toc-l${h.level}"><a href="#${h.id}">${h.text}</a></div>`).join('') +
  '</div><div class="pagebreak"></div>';

const body = md.render(source);

// ---------------------------------------------------------------- assemble
const fontsPath = path.join(ROOT, 'assets', 'fonts.css');
if (!fs.existsSync(fontsPath)) {
  console.warn('WARNING: assets/fonts.css missing — run `node make-fonts-css.js` first.');
  console.warn('         Diagram box-drawing and checkbox glyphs may render as empty boxes.');
}
const fontsCss = fs.existsSync(fontsPath) ? fs.readFileSync(fontsPath, 'utf8') : '';
const css = fontsCss + '\n' + fs.readFileSync(path.join(ROOT, 'assets', 'print.css'), 'utf8');
const html = `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Research Paper Writing and Research Tools</title><style>${css}</style></head>
<body>${body.replace('<!--TOC-->', '')}</body></html>`;

// Inject the TOC immediately before the "How to Use This Guide" heading, so the
// order is: title page, preface, table of contents, how to use, lists, chapters.
const anchorRe = /<h1 id="how-to-use-this-guide"[^>]*>/;
if (!anchorRe.test(html)) {
  console.warn('WARNING: TOC anchor heading not found — table of contents NOT injected.');
}
const withToc = html.replace(anchorRe, (m) => `${tocHtml}${m}`);

fs.mkdirSync(BUILD, { recursive: true });
fs.writeFileSync(path.join(BUILD, 'handbook.html'), withToc);
fs.writeFileSync(path.join(BUILD, 'handbook.md'), source);

console.log(`markdown files : ${files.length}`);
console.log(`words          : ${words.toLocaleString()}`);
console.log(`toc entries    : ${toc.length}`);
console.log(`html           : build/handbook.html`);

// ---------------------------------------------------------------- pdf
(async () => {
  if (process.argv.includes('--html-only')) return;
  const puppeteer = require('puppeteer-core');
  const browser = await puppeteer.launch({
    executablePath: process.env.CHROME_PATH || '/usr/local/bin/chrome',
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--font-render-hinting=none'],
    headless: true,
  });
  const page = await browser.newPage();
  await page.setContent(withToc, { waitUntil: 'networkidle0', timeout: 180000 });
  await page.emulateMediaType('print');
  await page.pdf({
    path: path.join(BUILD, 'handbook.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: '20mm', bottom: '20mm', left: '20mm', right: '18mm' },
    displayHeaderFooter: true,
    headerTemplate:
      '<div style="font-size:8pt;color:#888;width:100%;padding:0 18mm;font-family:Georgia,serif;">' +
      '<span style="float:right">Research Paper Writing and Research Tools</span></div>',
    footerTemplate:
      '<div style="font-size:9pt;color:#555;width:100%;text-align:center;font-family:Georgia,serif;">' +
      '<span class="pageNumber"></span></div>',
  });
  await browser.close();
  const bytes = fs.statSync(path.join(BUILD, 'handbook.pdf')).size;
  console.log(`pdf            : build/handbook.pdf (${(bytes / 1048576).toFixed(1)} MB)`);
})();
