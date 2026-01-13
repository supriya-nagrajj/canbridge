# backend/app/main.py

from fastapi import FastAPI
from app.routes import warrior_stories
from app.routes import predict, history, report
from app.services.db import init_db
from app.routes.auth import router as auth_router
from app.services.model_loader import load_models

app = FastAPI(
    title="CanBridge Backend API",
    description="Backend for Cancer Detection and Support System",
    version="1.0.0"
)

# ---------------- STARTUP ----------------
@app.on_event("startup")
def startup_event():
    init_db()
    load_models()
# ---------------- ROUTES ----------------
app.include_router(predict.router)
app.include_router(history.router)
app.include_router(report.router)
app.include_router(warrior_stories.router)
app.include_router(auth_router)