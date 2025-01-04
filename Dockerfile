FROM python:3.13-slim-bookworm
LABEL authors="shuuji3"

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY . .

RUN uv sync --frozen

CMD ["./run.sh"]
