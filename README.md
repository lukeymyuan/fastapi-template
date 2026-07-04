# FastAPI Templates

A small collection of minimal FastAPI starter templates.

## Templates

- [`base/`](base/) - A minimal, general-purpose FastAPI starter (config, CORS, healthcheck, exception hierarchy, tests, CI). Use this for a standard request/response API.
- [`webhook/`](webhook/) - The base template plus a `POST /webhooks` endpoint guarded by a source-IP allowlist. Use this to receive inbound webhooks from a provider.
