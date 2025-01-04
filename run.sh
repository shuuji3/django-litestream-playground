#!/bin/bash
set -e

if [ -f db.sqlite3 ]; then
  echo "Database already exists"
  exit 1
else
  echo "No database found, restoring from replica if exists"
  uv run litestream restore -config litestream.yaml -if-replica-exists db.sqlite3
fi

uv run manage.py collectstatic --noinput
uv run manage.py migrate

# Run litestream with your app as the subprocess.
uv run litestream replicate -config litestream.yaml -exec "uv run uvicorn --host=0.0.0.0 --port $PORT django_litestream_playground.asgi:application"
