# Ollama Fullstack (READY)

This bundle contains:
- backend/ (FastAPI) -> http://localhost:8000
- frontend/ (Next.js) -> http://localhost:3000

## 0) Requirements
- Ollama installed
- Node.js installed (for frontend)
- Python 3.10+ (for backend)

## 1) Pull a model (chatbot)
Recommended:
```powershell
ollama pull llama3
```

## 2) Run everything (one command)
From the root folder:
```powershell
powershell -ExecutionPolicy Bypass -File .\run_all.ps1
```

## 3) Open
- Frontend: http://localhost:3000
- Backend docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

## If you deploy frontend on Vercel
Set `NEXT_PUBLIC_BACKEND_URL` to your PUBLIC backend URL.
Also set backend `CORS_ORIGINS` to include your Vercel domain.
