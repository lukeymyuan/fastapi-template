# FastAPI Webhook Template

A minimal template for receiving inbound webhooks with FastAPI.

## Features

- FastAPI app with lifespan hook
- CORS middleware
- `GET /healthcheck` endpoint
- `POST /webhooks` endpoint guarded by an IP allowlist
- Pydantic-settings config with `.env` and environment profiles (`LOCAL` / `TESTING` / `STAGING` / `PRODUCTION`)
- API versioning via `root_path` in deployed environments
- Logging configured via `logging.ini`, wired through the `run.py` dev entrypoint
- Global HTTP exception hierarchy
- Timezone-aware Pydantic base model
- Ruff lint/format
- pytest with FastAPI `TestClient`
- `uv` for dependency management
- GitHub Actions CI for lint and tests

## Requirements

- Python 3.12+
- [`uv`](https://docs.astral.sh/uv/)

## Setup

Copy the example env file and install dependencies:

```bash
cp .env.example .env
uv sync
```

## Run

```bash
uv run run.py
```

The app will be available at <http://localhost:8000>.

## Lint and format

```bash
uv run ruff check .
uv run ruff format .
```

## Test

```bash
uv run pytest
```
