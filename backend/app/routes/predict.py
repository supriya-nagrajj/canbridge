# backend/app/routes/predict.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image
import numpy as np
from datetime import datetime

from app.services.model_loader import get_model
from app.services.db import get_connection

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)

SUPPORTED_CANCERS = ["brain", "breast", "lung"]

BRAIN_LABELS = [
    "Glioma Tumor",
    "Meningioma Tumor",
    "No Tumor",
    "Pituitary Tumor"
]


@router.post("/{cancer_type}")
async def predict_cancer(cancer_type: str, file: UploadFile = File(...)):

    if cancer_type not in SUPPORTED_CANCERS:
        raise HTTPException(status_code=400, detail="Invalid cancer type")

    try:
        # -------- IMAGE PREPROCESSING --------
        image = Image.open(file.file).convert("RGB")
        image = image.resize((150, 150))

        img_array = np.array(image, dtype="float32") / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        conn = get_connection()
        cursor = conn.cursor()

        # -------- BRAIN MODEL --------
        if cancer_type == "brain":
            model = get_model("brain")
            preds = model.predict(img_array)

            class_index = int(np.argmax(preds))
            confidence = float(preds[0][class_index])
            prediction_label = BRAIN_LABELS[class_index]

        # -------- MOCK OTHERS --------
        else:
            prediction_label = "Model under development"
            confidence = 0.0

        # -------- SAVE TO DB --------
        cursor.execute("""
            INSERT INTO predictions (cancer_type, prediction, confidence, created_at)
            VALUES (?, ?, ?, ?)
        """, (
            cancer_type,
            prediction_label,
            confidence,
            datetime.utcnow().isoformat()
        ))

        prediction_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return {
            "prediction_id": prediction_id,
            "cancer_type": cancer_type,
            "prediction": prediction_label,
            "confidence": confidence
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
