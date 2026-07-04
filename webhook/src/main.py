import logging
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from src.config import app_configs, settings
from src.exceptions import PermissionDenied

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_application: FastAPI) -> AsyncGenerator:
    # Startup
    yield
    # Shutdown


app = FastAPI(**app_configs, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_origin_regex=settings.CORS_ORIGINS_REGEX,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/webhooks")
async def receive_webhook(request: Request) -> dict[str, Any]:
    client_ip = request.client.host if request.client else None
    if settings.WEBHOOK_ALLOWED_IPS and client_ip not in settings.WEBHOOK_ALLOWED_IPS:
        raise PermissionDenied()

    payload = await request.json()
    logger.info("Received webhook from %s: %s", client_ip, payload)

    return {"status": "received"}
