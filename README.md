# FastAPI Template

A minimal template for kickstarting new FastAPI projects.

## Features

- FastAPI app with lifespan hook
- CORS middleware
- `GET /healthcheck` endpoint
- Pydantic-settings config with `.env` and environment profiles (`LOCAL` / `TESTING` / `STAGING` / `PRODUCTION`)
- API versioning via `root_path` in deployed environments
- Logging configured at import time via `logging.ini` (no CLI flag required)
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
uv run uvicorn src.main:app --reload
```

The app will be available at <http://localhost:8000>.

## Lint and format

```bash
uv run ruff check src tests
uv run ruff format src tests
```

## Test

```bash
uv run pytest
```

## Project layout

```
.
├── .env.example
├── .github/workflows/ci.yml
├── README.md
├── logging.ini
├── pyproject.toml
├── ruff.toml
├── uv.lock
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── constants.py
│   ├── exceptions.py
│   ├── main.py
│   ├── schemas.py
│   └── utils.py
└── tests/
    ├── __init__.py
    └── test_main.py
```
