import os
from dotenv import load_dotenv

load_dotenv()

def _split_csv(v: str) -> list[str]:
    return [x.strip() for x in v.split(",") if x.strip()]

class Settings:
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
    DEFAULT_OLLAMA_MODEL: str = os.getenv("DEFAULT_OLLAMA_MODEL", "llama3")
    DEFAULT_NUM_PREDICT: int = int(os.getenv("DEFAULT_NUM_PREDICT", "512"))
    DEFAULT_TEMPERATURE: float = float(os.getenv("DEFAULT_TEMPERATURE", "0.2"))
    CORS_ORIGINS: list[str] = _split_csv(os.getenv("CORS_ORIGINS", "http://localhost:3000"))

settings = Settings()
