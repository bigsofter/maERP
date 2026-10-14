// What the landing's video library needs besides the MP4 on Bunny — written INTO the repo
// (apps/web), committed with the page:
//   apps/web/public/videos/<slug>/<lang>.vtt   captions, from the corrected VO + the built timing
//   apps/web/public/videos/<slug>/<lang>.jpg   the Bunny poster, local copy: Bunny answers 403 to a
//                                              request without an allowed Referer, so WhatsApp /
//                                              Google could never fetch the OG image from there
//   apps/web/components/landing/video-transcripts.json   VO paragraphs without {cue}, per language
//
// usage: node tmp/explainer/series/tools/web_assets.mjs [episode ...]   (default: every episode
// in apps/web/components/landing/videos.json). Run after publish.mjs (it needs the guids) and
// after a re-render (the timing must be the one the MP4 was built from — render.sh builds it).
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const series = path.resolve(here, "..");
const web = path.resolve(series, "../../../apps/web");
const manifest = JSON.parse(fs.readFileSync(path.join(web, "components/landing/videos.json"), "utf8"));
const transcriptsPath = path.join(web, "components/landing/video-transcripts.json");
const transcripts = fs.existsSync(transcriptsPath) ? JSON.parse(fs.readFileSync(transcriptsPath, "utf8")) : {};

// Same rule as videos.ts `episodeSlug`: 00-trailer → trailer, 01-e01 → e01.
const slugOf = (ep) => (ep === "00-trailer" ? "trailer" : ep.split("-").slice(1).join("-"));

const MAX_CHARS = 84;   // one caption = at most two lines of ~42
const LINE = 42;

const frTypo = (s) =>
  s.replace(/« /g, "« ").replace(/ »/g, " »").replace(/ ([:;?!])/g, " $1");

function paragraphs(file) {
  return fs.readFileSync(file, "utf8").split("\n").map((l) => l.trim()).filter((l) => l && !l.startsWith("#"));
}

/** A paragraph → [{text, start, end}] using the cue times; the leading text starts with the clip. */
function segments(par, clip, cues) {
  const parts = par.split(/\{(\w+)\}/);   // [text, id, text, id, text…]
  const out = [];
  if (parts[0].trim()) out.push({ text: parts[0], start: clip.start });
  for (let i = 1; i < parts.length; i += 2) {
    const t = cues[parts[i]];
    if (t === undefined) throw new Error(`cue {${parts[i]}} not in timing`);
    if (out.length && !parts[i + 1].trim()) continue;
    out.push({ text: parts[i + 1], start: t });
  }
  // A cue placed mid-sentence leaves a fragment («dont l’arabe, écrit…»): fine for the picture,
  // but captions read better as clauses — merge tiny fragments into the previous segment.
  const merged = [];
  for (const s of out) {
    const prev = merged[merged.length - 1];
    if (prev && (prev.text.trim().length < 12 || s.text.trim().length < 12) && (prev.text + s.text).trim().length <= MAX_CHARS) prev.text += s.text;
    else merged.push({ ...s });
  }
  const end = clip.start + clip.dur;
  return merged.map((s, i) => ({ text: s.text.replace(/\s+/g, " ").trim(), start: s.start, end: i + 1 < merged.length ? merged[i + 1].start : end }));
}

/** Split a long segment at clause boundaries; time is shared in proportion to characters. */
function split(seg) {
  if (seg.text.length <= MAX_CHARS) return [seg];
  const words = seg.text.split(" ");
  const chunks = [];
  let cur = "";
  for (const w of words) {
    const next = cur ? cur + " " + w : w;
    if (next.length > MAX_CHARS && cur) { chunks.push(cur); cur = w; }
    else cur = next;
    // prefer to cut after punctuation once the chunk is half full
    if (/[.!?…:;,—]$/.test(cur) && cur.length >= MAX_CHARS / 2) { chunks.push(cur); cur = ""; }
  }
  if (cur) chunks.push(cur);
  // a dangling 1–2 word tail goes back to the previous chunk when it fits
  for (let i = chunks.length - 1; i > 0; i--) {
    if (chunks[i].length < 14 && (chunks[i - 1] + " " + chunks[i]).length <= MAX_CHARS + 10) { chunks[i - 1] += " " + chunks[i]; chunks.splice(i, 1); }
  }
  const total = chunks.reduce((n, c) => n + c.length, 0);
  let t = seg.start;
  return chunks.map((c) => {
    const d = ((seg.end - seg.start) * c.length) / total;
    const out = { text: c, start: t, end: t + d };
    t += d;
    return out;
  });
}

function wrap(text) {
  if (text.length <= LINE) return text;
  // the space closest to the middle
  const mid = text.length / 2;
  let best = -1;
  for (let i = 0; i < text.length; i++) if (text[i] === " " && (best < 0 || Math.abs(i - mid) < Math.abs(best - mid))) best = i;
  return best < 0 ? text : text.slice(0, best) + "\n" + text.slice(best + 1);
}

const ts = (s) => {
  const ms = Math.round(s * 1000);
  const h = Math.floor(ms / 3600000), m = Math.floor((ms % 3600000) / 60000), sec = Math.floor((ms % 60000) / 1000);
  return `${String(h).padStart(2, "0")}:${String(m).padStart(2, "0")}:${String(sec).padStart(2, "0")}.${String(ms % 1000).padStart(3, "0")}`;
};

const eps = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(manifest.videos);
for (const ep of eps) {
  const slug = slugOf(ep);
  const outDir = path.join(web, "public/videos", slug);
  fs.mkdirSync(outDir, { recursive: true });
  transcripts[ep] = {};
  for (const lang of Object.keys(manifest.videos[ep]).sort()) {
    const { guid, duration } = manifest.videos[ep][lang];
    const timing = JSON.parse(fs.readFileSync(path.join(series, ep, "build", lang, "timing.json"), "utf8"));
    const pars = paragraphs(path.join(series, ep, "vo", `${lang}.txt`));
    if (pars.length !== timing.clips.length) throw new Error(`${ep}.${lang}: ${pars.length} paragraphs vs ${timing.clips.length} clips`);
    if (Math.abs(timing.total - duration) > 1.5) throw new Error(`${ep}.${lang}: timing ${timing.total}s vs published ${duration}s — rebuild/re-render first`);
    const typo = lang === "fr" ? frTypo : (s) => s;

    const cues = pars.flatMap((p, i) => segments(p, timing.clips[i], timing.cues)).flatMap(split);
    let vtt = "WEBVTT\n";
    cues.forEach((c, i) => { vtt += `\n${i + 1}\n${ts(c.start)} --> ${ts(Math.max(c.end - 0.05, c.start + 0.5))}\n${wrap(typo(c.text))}\n`; });
    fs.writeFileSync(path.join(outDir, `${lang}.vtt`), vtt);
    transcripts[ep][lang] = pars.map((p) => typo(p.replace(/\{\w+\}/g, "").replace(/\s+/g, " ").trim()));

    const res = await fetch(`https://${manifest.cdnHost}/${guid}/thumbnail.jpg`, { headers: { Referer: "https://tinycio.ma/" } });
    if (!res.ok) throw new Error(`${ep}.${lang}: poster HTTP ${res.status}`);
    fs.writeFileSync(path.join(outDir, `${lang}.jpg`), Buffer.from(await res.arrayBuffer()));
    console.log(`✓ ${ep}.${lang} → videos/${slug}/${lang}.{vtt,jpg}  ${cues.length} captions`);
  }
}
const sorted = Object.fromEntries(Object.keys(transcripts).sort().map((k) => [k, transcripts[k]]));
fs.writeFileSync(transcriptsPath, JSON.stringify(sorted, null, 2) + "\n");
console.log(`transcripts -> ${path.relative(process.cwd(), transcriptsPath)}`);
