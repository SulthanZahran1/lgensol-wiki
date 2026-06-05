#!/usr/bin/env bash
set -e
cd /home/dev/lgensol-wiki/server

# Source API keys
source /home/dev/.hermes/.env

export OLLAMA_MODEL="deepseek-v4-flash:cloud"
export WIKI_DIR="/home/dev/lgensol-wiki/wiki"
export GRAPH_PATH="/home/dev/lgensol-wiki/server/data/graph.json"

exec ./wiki-server