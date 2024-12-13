PORT="${PORT:-8080}"
HOST="${HOST:-0.0.0.0}"

uvicorn main:app --host "$HOST" --port "$PORT" --forwarded-allow-ips '*'