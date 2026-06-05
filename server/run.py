#!/usr/bin/env python3
"""Load .env and start the wiki server with env vars properly set."""
import os
import subprocess
import sys

# Load .env
env_path = os.path.expanduser("~/.hermes/.env")
with open(env_path) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            os.environ[key] = val

os.environ["OLLAMA_MODEL"] = "deepseek-v4-flash:cloud"
os.environ["WIKI_DIR"] = "/home/dev/lgensol-wiki/wiki"
os.environ["GRAPH_PATH"] = "/home/dev/lgensol-wiki/server/data/graph.json"

print(f"OLLAMA_API_KEY loaded: {os.environ.get('OLLAMA_API_KEY','NOT FOUND')[:8]}...")
sys.stdout.flush()

server_dir = "/home/dev/lgensol-wiki/server"
os.chdir(server_dir)
os.execve("./wiki-server", ["./wiki-server"], os.environ)