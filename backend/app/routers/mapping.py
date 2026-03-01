from fastapi import APIRouter, HTTPException
from app.schemas.mapping import MappingSuggestRequest, MappingSuggestResponse
from app.services.ollama_client import generate as ollama_generate, OllamaError
from app.core.config import settings
import json

router = APIRouter()

def _build_prompt(columns, target_fields, notes):
    return f"""You are a data integration assistant.
Task: Propose a mapping from input dataset columns to target fields.

Return ONLY valid JSON (no markdown, no comments) in this exact shape:
{{
  "mapping": {{ "<target_field>": "<best_matching_input_column_or_empty>" }},
  "confidence": {{ "<target_field>": <number_0_to_1> }},
  "explanation": "<short explanation>"
}}

Rules:
- Use empty string "" if no good match.
- Confidence is a float between 0 and 1.
- Prefer exact/near matches, then semantic matches.
- Do not invent columns.

Input columns:
{columns}

Target fields:
{target_fields}

Context/notes:
{notes or ""}

JSON:
"""

@router.post("/mapping/suggest", response_model=MappingSuggestResponse)
def suggest_mapping(req: MappingSuggestRequest):
    try:
        model = req.model or settings.DEFAULT_OLLAMA_MODEL
        prompt = _build_prompt(req.columns, req.target_fields, req.notes)

        out = ollama_generate(
            prompt=prompt,
            model=model,
            temperature=req.temperature,
            num_predict=req.num_predict,
        )

        text = (out.get("response") or "").strip()

        try:
            data = json.loads(text)
        except Exception:
            start = text.find("{")
            end = text.rfind("}")
            if start != -1 and end != -1 and end > start:
                data = json.loads(text[start:end+1])
            else:
                raise

        mapping = data.get("mapping", {}) if isinstance(data, dict) else {}
        confidence = data.get("confidence", {}) if isinstance(data, dict) else {}
        explanation = data.get("explanation", "") if isinstance(data, dict) else ""

        return MappingSuggestResponse(
            model=model,
            mapping=mapping,
            confidence=confidence,
            explanation=explanation,
        )

    except OllamaError as e:
        raise HTTPException(status_code=502, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail=f"Failed to parse JSON from model output: {text[:500]}")
