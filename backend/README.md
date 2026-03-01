# Backend (FastAPI) — Run

## 1) Create venv
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2) Copy env
```powershell
copy .env.example .env
```

## 3) Run
```powershell
uvicorn app.main:app --reload --port 8000
```

Open: http://localhost:8000/docs
