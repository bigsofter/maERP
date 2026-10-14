// Bring the video.tinycio.* hostnames live on Bunny, one TLD at a time, and only then
// tell the landing to use them.
//
// usage:  node tmp/explainer/series/tools/video_hosts.mjs [ma com es ru]
//
// Per host: DNS must already CNAME to the library's b-cdn host (the owner sets that at the
// registrar) → free certificate (Let's Encrypt via Bunny) → force HTTPS → a real ranged GET
// of a published MP4 with a landing Referer must answer 206. Only a host that passes ALL of
// that is written to `customHosts` in tmp/explainer/bunny.json and in the tracked
// apps/web/components/landing/videos.json — so the site never points at a hostname that
// does not serve yet. Re-running is safe: a live host is re-checked, not re-provisioned.
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "../..");                     // tmp/explainer
const env = fs.readFileSync(path.join(root, ".env"), "utf8");
const key = (env.match(/^BUNNY_API_KEY=(\S+)/m) || [])[1];
if (!key) throw new Error("no BUNNY_API_KEY in tmp/explainer/.env");
const bunnyPath = path.join(root, "bunny.json");
const bunny = JSON.parse(fs.readFileSync(bunnyPath, "utf8"));
const webPath = path.resolve(root, "../../apps/web/components/landing/videos.json");
const web = JSON.parse(fs.readFileSync(webPath, "utf8"));

const tlds = process.argv.slice(2).length ? process.argv.slice(2) : ["ma", "com", "es", "ru"];
const api = (method, p, body) =>
  fetch(`https://api.bunny.net${p}`, { method, headers: { AccessKey: key, accept: "application/json", "content-type": "application/json" }, body: body && JSON.stringify(body) });

// Any published file will do for the live check; the trailer always exists.
const sample = Object.values(web.videos)[0];
const sampleGuid = (sample.fr ?? Object.values(sample)[0]).guid;

bunny.customHosts ??= {};
for (const tld of tlds) {
  const host = `video.tinycio.${tld}`;
  const say = (m) => console.log(`${host}: ${m}`);
  const cname = execFileSync("dig", ["+short", "@1.1.1.1", "CNAME", host]).toString().trim().replace(/\.$/, "");  // public resolver: the local one caches the old NXDOMAIN for hours
  if (cname !== bunny.cdnHost) { say(`DNS not ready — CNAME is "${cname || "none"}", expected ${bunny.cdnHost}`); continue; }

  const zone = await (await api("GET", `/pullzone/${bunny.pullZoneId}`)).json();
  const h = zone.Hostnames.find((x) => x.Value === host);
  if (!h) { say("not registered on the pull zone (addHostname first)"); continue; }
  if (!h.HasCertificate) {
    const r = await api("GET", `/pullzone/loadFreeCertificate?hostname=${host}`);
    if (!r.ok) { say(`certificate request failed: HTTP ${r.status} ${(await r.text()).slice(0, 160)}`); continue; }
    say("certificate issued");
  }
  if (!h.ForceSSL) {
    const r = await api("POST", `/pullzone/${bunny.pullZoneId}/setForceSSL`, { Hostname: host, ForceSSL: true });
    if (!r.ok) { say(`force-SSL failed: HTTP ${r.status}`); continue; }
  }

  let code = 0;
  for (let i = 0; i < 12 && code !== 206; i++) {
    if (i) await new Promise((r) => setTimeout(r, 10000));   // edge config takes ~1 min to propagate
    // curl pinned to the address the PUBLIC resolver gives: this machine's resolver may still
    // hold the pre-CNAME NXDOMAIN for hours, which says nothing about what visitors get.
    const ip = execFileSync("dig", ["+short", "@1.1.1.1", host]).toString().trim().split("\n").pop();
    try {
      code = Number(execFileSync("curl", ["-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "15", "--resolve", `${host}:443:${ip}`,
        "-r", "0-999", "-H", `Referer: https://tinycio.${tld}/`, `https://${host}/${sampleGuid}/play_720p.mp4`]).toString());
    } catch { code = 0; }
  }
  if (code !== 206) { say(`serves HTTP ${code}, not 206 — left OFF the landing`); continue; }
  bunny.customHosts[tld] = host;
  say("LIVE (206 over HTTPS) — landing will use it");
}

fs.writeFileSync(bunnyPath, JSON.stringify(bunny, null, 1) + "\n");
web.customHosts = Object.fromEntries(Object.entries(bunny.customHosts).sort());
fs.writeFileSync(webPath, JSON.stringify(web, null, 2) + "\n");
console.log(`customHosts = ${JSON.stringify(web.customHosts)} -> ${path.relative(process.cwd(), webPath)}`);
