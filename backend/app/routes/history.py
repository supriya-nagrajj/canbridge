# backend/app/routes/history.py

from fastapi import APIRouter
from app.services.db import get_connection

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def get_prediction_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, cancer_type, prediction, confidence, created_at
        FROM predictions
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row["id"],
            "cancer_type": row["cancer_type"],
            "prediction": row["prediction"],
            "confidence": row["confidence"],
            "created_at": row["created_at"]
        }
        for row in rows
    ]
