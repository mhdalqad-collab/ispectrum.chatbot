from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, chat, mapping
from app.core.config import settings

app = FastAPI(
    title="iSpectrum Backend",
    version="1.0.0",
    description="FastAPI backend for iSpectrum chatbot (proxies to local Ollama).",
)

# ---- CORS (Fix for Vercel + Local Dev) ----
# NOTE: Keep this as the ONLY CORS middleware.
# If you add a second CORS middleware, browsers can fail preflight (CORS error).
ALLOWED_ORIGINS = [
    "https://ispectrum-chatbot.vercel.app",
    "http://localhost:3000",
    "http://localhost:3001",
]

# If you set additional origins in .env (CORS_ORIGINS=...), include them too
# settings.CORS_ORIGINS should be a list if your config parses it, otherwise it might be None.
if getattr(settings, "CORS_ORIGINS", None):
    # Add configured origins, avoiding duplicates
    for o in settings.CORS_ORIGINS:
        if o and o not in ALLOWED_ORIGINS:
            ALLOWED_ORIGINS.append(o)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,  # IMPORTANT for browser preflight reliability
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Routes ----
app.include_router(health.router)
app.include_router(chat.router, prefix="/v1", tags=["chat"])
app.include_router(mapping.router, prefix="/v1", tags=["mapping"])