// Publish rendered episodes to Bunny Stream and write the manifest the landing reads.
//
// usage (from anywhere):  node tmp/explainer/series/tools/publish.mjs [episode ...] [--force]
//   no episode  → every `<NN-slug>.<lang>.mp4` in ../_renders
//   --force     → re-upload even when the file on Bunny matches the local one
//
// Keys come from tmp/explainer/.env (BUNNY_STREAM_LIBRARY_KEY) and are never printed.
// Library id + CDN host come from tmp/explainer/bunny.json. A video is identified by its
// TITLE = `<episode>.<lang>` (e.g. `00-trailer.fr`), so a re-render replaces the same
// title: the old video is deleted, the new one gets a new guid, and the manifest follows.
// "Unchanged" = the sha256 of the local file is the one recorded in the manifest.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));     // not .pathname: it stays percent-encoded on a non-ASCII path
const root = path.resolve(here, "../..");                     // tmp/explainer
const renders = path.resolve(here, "../_renders");
const manifestPath = path.join(renders, "manifest.json");

const env = fs.readFileSync(path.join(root, ".env"), "utf8");
const key = (env.match(/^BUNNY_STREAM_LIBRARY_KEY=(\S+)/m) || [])[1];
if (!key) throw new Error("no BUNNY_STREAM_LIBRARY_KEY in tmp/explainer/.env");
const { libraryId, cdnHost, customHosts = {}, titlePrefix }  = JSON.parse(fs.readFileSync(path.join(root, "bunny.json"), "utf8"));
// A video is identified by its title, and a re-publish DELETES every video with the same title.
// This product has its own library since 2026-10-14, but the prefix stays mandatory: if the library
// is ever shared again, "00-trailer.fr" would delete another product's trailer.
if (!titlePrefix) throw new Error("bunny.json: titlePrefix is required (shared library) — e.g. \"maerp/\"");
const API = `https://video.bunnycdn.com/library/${libraryId}`;

const args = process.argv.slice(2);
const force = args.includes("--force");
const only = args.filter((a) => !a.startsWith("--"));

async function api(method, url, body, headers = {}) {
  const r = await fetch(url, { method, headers: { AccessKey: key, accept: "application/json", ...headers }, body, duplex: body?.pipe ? "half" : undefined });
  const text = await r.text();
  if (!r.ok) throw new Error(`${method} ${url.replace(API, "")} -> ${r.status} ${text.slice(0, 200)}`);
  return text ? JSON.parse(text) : {};
}

const sha = (f) => crypto.createHash("sha256").update(fs.readFileSync(f)).digest("hex");
const duration = (f) => Number(execFileSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).toString().trim());
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const manifest = fs.existsSync(manifestPath) ? JSON.parse(fs.readFileSync(manifestPath, "utf8")) : { cdnHost, libraryId, videos: {} };
manifest.cdnHost = cdnHost; manifest.libraryId = libraryId;

const files = fs.readdirSync(renders).filter((f) => /^[\w-]+\.(ru|fr|en|es)\.mp4$/.test(f)).sort()
  .filter((f) => only.length === 0 || only.some((ep) => f.startsWith(ep + ".")));
if (files.length === 0) { console.log("nothing to publish in", renders); process.exit(0); }

const existing = (await api("GET", `${API}/videos?page=1&itemsPerPage=1000`)).items ?? [];

for (const f of files) {
  const [, ep, lang] = f.match(/^([\w-]+)\.(\w\w)\.mp4$/);
  const title = `${titlePrefix}${ep}.${lang}`;
  const file = path.join(renders, f);
  const hash = sha(file);
  const prev = manifest.videos[ep]?.[lang];
  const remote = existing.filter((v) => v.title === title);
  if (!force && prev && prev.sha256 === hash && remote.some((v) => v.guid === prev.guid)) {
    console.log(`= ${title} unchanged (${prev.guid})`);
    continue;
  }
  for (const v of remote) await api("DELETE", `${API}/videos/${v.guid}`);
  const { guid } = await api("POST", `${API}/videos`, JSON.stringify({ title }), { "content-type": "application/json" });
  await api("PUT", `${API}/videos/${guid}`, fs.readFileSync(file), { "content-type": "application/octet-stream" });
  (manifest.videos[ep] ??= {})[lang] = { guid, sha256: hash, duration: Math.round(duration(file) * 10) / 10, uploadedAt: new Date().toISOString() };
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 1) + "\n");
  console.log(`+ ${title} uploaded (${guid}, ${(fs.statSync(file).size / 1e6).toFixed(1)} MB)`);
}

// Encoding is asynchronous: status 4 = finished, 5 = error. Wait so the caller knows the
// URLs in the manifest actually play.
const guids = files.map((f) => { const [, ep, lang] = f.match(/^([\w-]+)\.(\w\w)\.mp4$/); return [`${ep}.${lang}`, manifest.videos[ep][lang].guid]; });
for (let i = 0; i < 90; i++) {
  const st = await Promise.all(guids.map(async ([t, g]) => [t, (await api("GET", `${API}/videos/${g}`))]));
  const pending = st.filter(([, v]) => v.status < 4);
  const failed = st.filter(([, v]) => v.status > 4);
  if (failed.length) { console.log("ENCODING FAILED:", failed.map(([t, v]) => `${t} (status ${v.status})`).join(", ")); process.exit(1); }
  if (pending.length === 0) {
    for (const [t, v] of st) console.log(`✓ ${t} ${v.width}x${v.height} ${v.length}s resolutions ${v.availableResolutions}`);
    break;
  }
  if (i % 3 === 0) console.log(`… encoding: ${pending.map(([t, v]) => `${t} ${v.encodeProgress}%`).join(", ")}`);
  await sleep(10000);
}
// The landing reads a TRACKED copy with only what a page needs (no hashes, no timestamps —
// they would make every re-publish a diff). Commit it together with the page that uses it.
const webManifest = path.resolve(root, "../../apps/web/components/landing/videos.json");
const web = { cdnHost, customHosts, videos: {} };   // customHosts: only hosts video_hosts.mjs verified live
for (const ep of Object.keys(manifest.videos).sort()) {
  web.videos[ep] = {};
  for (const lang of Object.keys(manifest.videos[ep]).sort()) {
    const { guid, duration: d, uploadedAt } = manifest.videos[ep][lang];
    // `uploaded` (yyyy-mm-dd) feeds the VideoObject JSON-LD of the episode page (uploadDate).
    web.videos[ep][lang] = { guid, duration: Math.round(d), uploaded: uploadedAt.slice(0, 10) };
  }
}
fs.writeFileSync(webManifest, JSON.stringify(web, null, 2) + "\n");
console.log(`landing manifest -> ${path.relative(process.cwd(), webManifest)}`);
console.log(`manifest -> ${path.relative(process.cwd(), manifestPath)}  (https://${cdnHost}/<guid>/playlist.m3u8 · play_720p.mp4 · thumbnail.jpg)`);

// Captions, transcripts and local posters for the video library (apps/web/public/videos/…):
// they depend on the guids just written, so they are regenerated on every publish.
execFileSync("node", [path.join(here, "web_assets.mjs"), ...files.map((f) => f.split(".")[0]).filter((e, i, a) => a.indexOf(e) === i)], { stdio: "inherit" });
