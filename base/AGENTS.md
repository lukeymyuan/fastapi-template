# FastAPI Template

FastAPI, Python 3.12, uv, Ruff, pytest

## Commands

- `uv sync`: Install dependencies
- `uv run run.py`: Dev server (port 8000, reload + logging.ini)
- `uv run pytest`: Full test suite
- `uv run pytest tests/test_main.py::test_healthcheck`: Single test
- `uv run ruff check .`: Lint
- `uv run ruff format .`: Format

## Architecture

- `src/`    Application code. `main.py` is the FastAPI entry point; config, constants, schemas, and exceptions live in flat modules alongside it.
- `tests/`  pytest suite, uses FastAPI `TestClient`.

## Code Style

- Type hints on all function signatures
- Manage deps with uv only
- Pydantic v2 models for all request/response shapes
- Prefer the simplest solution; avoid needless abstraction. Comments explain *why*, not *what*.

## FastAPI conventions

For deeper conventions (DB, auth, background tasks) when the project grows, follow
https://github.com/zhanymkanov/fastapi-best-practices
