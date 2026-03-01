import requests
from typing import List, Dict, Any, Optional
from app.core.config import settings

class OllamaError(RuntimeError):
    pass

def _post_json(url: str, payload: Dict[str, Any], timeout: int = 120) -> Dict[str, Any]:
    try:
        r = requests.post(url, json=payload, timeout=timeout)
    except requests.RequestException as e:
        raise OllamaError(f"Failed to connect to Ollama at {settings.OLLAMA_BASE_URL}. Error: {e}") from e

    if r.status_code >= 400:
        raise OllamaError(f"Ollama error {r.status_code}: {r.text}")

    return r.json()

def chat(
    messages: List[Dict[str, str]],
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    num_predict: Optional[int] = None,
) -> Dict[str, Any]:
    payload = {
        "model": model or settings.DEFAULT_OLLAMA_MODEL,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature if temperature is not None else settings.DEFAULT_TEMPERATURE,
            "num_predict": num_predict if num_predict is not None else settings.DEFAULT_NUM_PREDICT,
        }
    }
    url = f"{settings.OLLAMA_BASE_URL}/api/chat"
    return _post_json(url, payload)

def generate(
    prompt: str,
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    num_predict: Optional[int] = None,
) -> Dict[str, Any]:
    payload = {
        "model": model or settings.DEFAULT_OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature if temperature is not None else settings.DEFAULT_TEMPERATURE,
            "num_predict": num_predict if num_predict is not None else settings.DEFAULT_NUM_PREDICT,
        }
    }
    url = f"{settings.OLLAMA_BASE_URL}/api/generate"
    return _post_json(url, payload)
