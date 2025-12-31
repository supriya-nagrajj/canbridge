# backend/app/routes/report.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.services.db import get_connection
from app.services.pdf_generator import generate_report
import os
import uuid

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.get("/{prediction_id}")
def download_report(prediction_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, cancer_type, prediction, confidence, created_at
        FROM predictions
        WHERE id = ?
    """, (prediction_id,))

    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Prediction not found")

    prediction_record = dict(row)

    reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    filename = f"canbridge_report_{uuid.uuid4().hex}.pdf"
    output_path = os.path.join(reports_dir, filename)

    generate_report(prediction_record, output_path)

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename="CanBridge_Report.pdf"
    )
