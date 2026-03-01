from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ollama_client import chat as ollama_chat, OllamaError
from app.core.config import settings

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    try:
        model = req.model or settings.DEFAULT_OLLAMA_MODEL
        system = req.system or "You are a helpful assistant."

        messages = [{"role": "system", "content": system}]
        if req.history:
            messages.extend([m.model_dump() for m in req.history])
        messages.append({"role": "user", "content": req.message})

        out = ollama_chat(
            messages=messages,
            model=model,
            temperature=req.temperature,
            num_predict=req.num_predict,
        )

        response_text = (out.get("message") or {}).get("content", "")
        usage = {
            "prompt_eval_count": out.get("prompt_eval_count"),
            "eval_count": out.get("eval_count"),
            "total_duration_ns": out.get("total_duration"),
            "load_duration_ns": out.get("load_duration"),
        }
        return ChatResponse(model=model, response=response_text, usage=usage)

    except OllamaError as e:
        raise HTTPException(status_code=502, detail=str(e))
