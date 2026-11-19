// news-image-20261119: "The World in One Day" — one 1024x1024 poster summing up
// Thursday 19 November 2026 (GTA VI launch, Jeffries as first Black Speaker,
// Gaza floods, Anthropic's record $81.3B IPO). The image is entry.png beside
// this file, drawn from scratch with PIL; this program only copies it to
// /output/entry.png, so both grader runs write byte-identical output.
// No network, no randomness, no timestamps.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
