#!/bin/sh
# Load .env files into environment (order matters — later overrides earlier)
for ENV_FILE in /app/hermes.env /app/.env; do
    if [ -f "$ENV_FILE" ]; then
        echo "entrypoint: Loading $ENV_FILE"
        while IFS='=' read -r key val || [ -n "$key" ]; do
            case "$key" in
                ''|'#'*) continue ;;
                *)
                    val=$(echo "$val" | sed "s/^['\"]//;s/['\"]$//")
                    export "$key=$val"
                    ;;
            esac
        done < "$ENV_FILE"
    fi
done

echo "entrypoint: ACCESS_TOKEN=$(test -n \"$ACCESS_TOKEN\" && echo 'set' || echo 'NOT SET')"
echo "entrypoint: OLLAMA_API_KEY=$(test -n \"$OLLAMA_API_KEY\" && echo 'set' || echo 'NOT SET')"

exec /app/wiki-server