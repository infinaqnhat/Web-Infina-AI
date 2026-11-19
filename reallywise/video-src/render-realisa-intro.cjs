// Renders realisa-intro.html to an MP4 with its soundtrack, frame by frame (deterministic).
// Usage: node render-realisa-intro.cjs <out.mp4> [workdir] [fps]
// Voiceover: put vo/<cue id>.wav (44.1 kHz mono) next to this file and run retime-cues.py first.
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs'), path = require('path');
(async () => {
  const [out, work = '/tmp', fpsArg] = process.argv.slice(2);
  const fps = +(fpsArg || 30);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file://' + path.join(__dirname, 'realisa-intro.html'));
  await page.waitForLoadState('networkidle');
  await page.evaluate(() => document.fonts.ready);
  const tl = await page.evaluate(() => window.TIMELINE());
  const tlFile = path.join(work, 'timeline.json'), wav = path.join(work, 'soundtrack.wav');
  fs.writeFileSync(tlFile, JSON.stringify(tl, null, 1));
  execFileSync('python3', [path.join(__dirname, 'build-audio.py'), tlFile, wav, path.join(__dirname, 'vo')], { stdio: 'inherit' });
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-i', wav, '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
    '-shortest', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const total = Math.round(tl.duration * fps);
  for (let i = 0; i < total; i++) {
    await page.evaluate(t => window.render(t), i / fps);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 300 === 0) console.log(`frame ${i}/${total}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  // Frame 0 is the cover scene: save it as the thumbnail and embed it as the MP4 cover art,
  // so Slack and other players never show a blank preview.
  const thumb = out.replace(/\.mp4$/, '-thumbnail.jpg'), tmp = out + '.tmp.mp4';
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', out, '-frames:v', '1', '-q:v', '2', thumb]);
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', out, '-i', thumb, '-map', '0', '-map', '1', '-c', 'copy',
    '-disposition:v:1', 'attached_pic', '-movflags', '+faststart', tmp]);
  fs.renameSync(tmp, out);
  console.log('thumbnail', thumb);
  console.log('done', out);
})();
