// ElevenLabs TTS, one clip per line, with character timestamps -> word timings.
// usage: node tts.mjs <script.txt> <outDir> <lang> [voiceId] [model]
// Lines are cached: a line is re-synthesised only when its text changed
// (delete <outDir>/lNN.json to force a retake).
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const [, , scriptPath, outDir, lang, voice = "onwK4e9ZLuTAKqWW03F9", model = "eleven_v4"] = process.argv;
if (!lang) throw new Error("usage: tts.mjs <script.txt> <outDir> <lang> [voice] [model]");
const envFile = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../../.env");  // not .pathname: percent-encoded on a non-ASCII path
// the key is read only when a line actually needs synthesis (cached episodes rebuild without it)
let key = null;
function apiKey() {
  if (key) return key;
  const env = fs.existsSync(envFile) ? fs.readFileSync(envFile, "utf8") : "";
  key = (env.match(/ELEVENLABS_API_KEY=(\S+)/) || [])[1];
  if (!key) throw new Error("no ELEVENLABS_API_KEY in tmp/explainer/.env");
  return key;
}
// {cue} markers sit before the word they sync to; they are stripped before synthesis.
const raw = fs.readFileSync(scriptPath, "utf8").split("\n").map((s) => s.trim()).filter((s) => s && !s.startsWith("#"));
const parsed = raw.map((line) => {
  const cues = [];
  let text = "";
  for (const part of line.split(/(\{\w+\})/)) {
    const m = part.match(/^\{(\w+)\}$/);
    if (m) cues.push({ id: m[1], at: text.length }); else text += part;
  }
  return { text, cues };
});
const lines = parsed.map((p) => p.text);
fs.mkdirSync(outDir, { recursive: true });

function words(al) {
  const out = [];
  let cur = null;
  al.characters.forEach((ch, i) => {
    const s = al.character_start_times_seconds[i], e = al.character_end_times_seconds[i];
    if (/\s/.test(ch)) { if (cur) { out.push(cur); cur = null; } return; }
    if (!cur) cur = { text: "", start: s, end: e };
    cur.text += ch; cur.end = e;
  });
  if (cur) out.push(cur);
  return out;
}

async function synth(body) {
  const url = `https://api.elevenlabs.io/v1/text-to-speech/${voice}/with-timestamps?output_format=mp3_44100_128`;
  const r = await fetch(url, { method: "POST", headers: { "xi-api-key": apiKey(), "Content-Type": "application/json" }, body: JSON.stringify(body) });
  return r.json();
}

let spent = 0;
const meta = [];
for (let i = 0; i < lines.length; i++) {
  const id = `l${String(i + 1).padStart(2, "0")}`;
  const mp3 = path.join(outDir, `${id}.mp3`);
  const wav = path.join(outDir, `${id}.wav`);
  const js = path.join(outDir, `${id}.json`);
  const cached = fs.existsSync(js) && JSON.parse(fs.readFileSync(js, "utf8")).text === lines[i];
  if (!cached) {
    const body = { text: lines[i], model_id: model, language_code: lang, voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true } };
    if (i > 0) body.previous_text = lines[i - 1];
    if (i < lines.length - 1) body.next_text = lines[i + 1];
    let j = await synth(body);
    if (!j.audio_base64 && (body.previous_text || body.next_text)) {
      console.error(id, "retry without context:", JSON.stringify(j.detail).slice(0, 200));
      delete body.previous_text; delete body.next_text;
      j = await synth(body);
    }
    if (!j.audio_base64) throw new Error(id + " " + JSON.stringify(j.detail));
    spent += lines[i].length;
    fs.writeFileSync(mp3, Buffer.from(j.audio_base64, "base64"));
    fs.writeFileSync(js, JSON.stringify({ text: lines[i], alignment: j.alignment }));
    execFileSync("ffmpeg", ["-y", "-v", "error", "-i", mp3, "-ar", "48000", "-ac", "2", wav]);
  }
  // wavs are not shipped in the handoff archive: rebuild them from the cached mp3
  if (!fs.existsSync(wav)) execFileSync("ffmpeg", ["-y", "-v", "error", "-i", mp3, "-ar", "48000", "-ac", "2", wav]);
  const { text, alignment } = JSON.parse(fs.readFileSync(js, "utf8"));
  const dur = parseFloat(execFileSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", wav]).toString());
  const w = words(alignment);
  // cue time = start of the first non-space character at/after the marker's offset
  const cues = parsed[i].cues.map(({ id, at }) => {
    let k = at;
    while (k < alignment.characters.length && /\s/.test(alignment.characters[k])) k++;
    return { id, t: +alignment.character_start_times_seconds[Math.min(k, alignment.characters.length - 1)].toFixed(3) };
  });
  meta.push({ id, text, file: `${id}.wav`, duration: +dur.toFixed(3), speechStart: +w[0].start.toFixed(3), speechEnd: +w[w.length - 1].end.toFixed(3), cues,
    words: w.map((x) => ({ ...x, start: +x.start.toFixed(3), end: +x.end.toFixed(3) })) });
  if (alignment.characters.join("") !== text) console.error(id, "WARN alignment text differs from input; cue offsets may drift");
  console.log(id, dur.toFixed(2) + "s", "speech", w[0].start.toFixed(2), "->", w[w.length - 1].end.toFixed(2), "|", text.slice(0, 70));
}
fs.writeFileSync(path.join(outDir, "voice.json"), JSON.stringify(meta, null, 1));
console.log(`chars synthesised this run: ${spent}`);
