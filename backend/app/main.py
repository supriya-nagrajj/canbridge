# backend/app/main.py

from fastapi import FastAPI

from app.routes import predict, history, report
from app.services.db import init_db

app = FastAPI(
    title="CanBridge Backend API",
    description="Backend for Cancer Detection and Support System",
    version="1.0.0"
)

# ---------------- STARTUP ----------------
@app.on_event("startup")
def startup_event():
    init_db()

# ---------------- ROUTES ----------------
app.include_router(predict.router)
app.include_router(history.router)
app.include_router(report.router)