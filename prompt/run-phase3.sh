#!/usr/bin/env bash
# Run Phase 3: Wiki Compilation via Claude Code (Opus)
# Usage: bash prompt/run-phase3.sh

set -e

cd ~/lgensol-wiki

claude -p "$(cat prompt/phase3-wiki-compilation.md)" \
  --model opus \
  --allowedTools "Read,Write,Bash" \
  --max-turns 80 \
  --output-format text \
  --verbose