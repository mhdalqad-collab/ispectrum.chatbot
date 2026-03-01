# Run backend + frontend (two separate windows is easier, but this works too)
# 1) Ensure Ollama is installed and model is pulled:
#    ollama pull llama3
#
# 2) Run this script from the root folder.
#
Write-Host "Starting backend on http://localhost:8000 ..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy", "Bypass", "-Command", "cd backend; if (!(Test-Path .venv)) { python -m venv .venv }; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; if (!(Test-Path .env)) { Copy-Item .env.example .env }; uvicorn app.main:app --reload --port 8000"

Write-Host "Starting frontend on http://localhost:3000 ..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy", "Bypass", "-Command", "cd frontend; if (!(Test-Path .env.local)) { Copy-Item .env.local.example .env.local }; npm install; npm run dev"
