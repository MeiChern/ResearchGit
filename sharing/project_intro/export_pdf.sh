#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
INPUT_HTML="$ROOT_DIR/index.html"
OUTPUT_PDF="$ROOT_DIR/researchgit_project_intro.pdf"
CHROME_BIN="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

if [[ ! -x "$CHROME_BIN" ]]; then
  echo "Chrome not found at: $CHROME_BIN" >&2
  exit 1
fi

if [[ ! -f "$INPUT_HTML" ]]; then
  echo "Presentation not found at: $INPUT_HTML" >&2
  exit 1
fi

"$CHROME_BIN" \
  --headless=new \
  --disable-gpu \
  --run-all-compositor-stages-before-draw \
  --virtual-time-budget=4000 \
  --print-to-pdf="$OUTPUT_PDF" \
  "file://$INPUT_HTML?print-pdf"

echo "Exported PDF to $OUTPUT_PDF"
