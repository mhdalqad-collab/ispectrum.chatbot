from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/health", tags=["health"])
def health():
    return {
        "status": "ok",
        "ollama_base_url": settings.OLLAMA_BASE_URL,
        "default_model": settings.DEFAULT_OLLAMA_MODEL,
        "cors_origins": settings.CORS_ORIGINS,
    }
