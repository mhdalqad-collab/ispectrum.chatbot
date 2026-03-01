from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health, chat, mapping
from app.core.config import settings

app = FastAPI(
    title="Ollama Fullstack Backend",
    version="1.0.0",
    description="FastAPI backend that proxies requests to a local Ollama server."
)

# CORS for frontend (localhost or Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(chat.router, prefix="/v1", tags=["chat"])
app.include_router(mapping.router, prefix="/v1", tags=["mapping"])
