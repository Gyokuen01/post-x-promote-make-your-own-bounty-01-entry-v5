/**
 * post-x-promote-make-your-own-bounty-01 — make.fun entry.
 *
 * The entry itself is a post on X: a quote of make.fun's own post about
 * making your own bounty, with a photo attached. The house reads the post
 * from X itself (its counts, the make.fun link, the @makefunai tag and the
 * play code), so this program has exactly one job: hand the post's address
 * to the house by copying POST.json from this repository to /output.
 *
 * The house runs this program from a working directory of its own choosing,
 * so every path here is resolved from this script file's own location,
 * never from the process working directory.
 */
import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const postFile = join(repoRoot, "POST.json");
const outDir = process.env.OUTPUT_DIR ?? "/output";

function fail(message: string): never {
  console.error(`post-x-promote: ${message}`);
  process.exit(1);
}

let raw: string;
try {
  raw = readFileSync(postFile, "utf8");
} catch {
  fail(`cannot read POST.json at ${postFile}`);
}

let parsed: unknown;
try {
  parsed = JSON.parse(raw);
} catch {
  fail("POST.json is not valid JSON");
}

if (typeof parsed !== "object" || parsed === null || Array.isArray(parsed)) {
  fail("POST.json must be an object with a string url");
}

const url = (parsed as Record<string, unknown>).url;
if (typeof url !== "string" || url.length === 0) {
  fail("POST.json must carry a non-empty string url");
}

if (!/^https:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\//.test(url)) {
  fail(`POST.json url is not an X post address: ${url}`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(postFile, join(outDir, "POST.json"));
console.log(`post-x-promote: handed in ${url}`);
