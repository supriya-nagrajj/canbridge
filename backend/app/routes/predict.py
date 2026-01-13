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

SUPPORTED_CANCERS = ["brain", "breast", "skin"]

# -----------------------------
# Common image preprocessing
# -----------------------------
def preprocess_image(file, target_size=(224, 224)):
    image = Image.open(file).convert("RGB")
    image = image.resize(target_size)
    img_array = np.array(image, dtype="float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


@router.post("/{cancer_type}")
async def predict_cancer(cancer_type: str, file: UploadFile = File(...)):

    if cancer_type not in SUPPORTED_CANCERS:
        raise HTTPException(status_code=400, detail="Invalid cancer type")

    try:
        # -------- PREPROCESS IMAGE --------
        img_array = preprocess_image(file.file)

        conn = get_connection()
        cursor = conn.cursor()

        # =====================================================
        # BRAIN — Binary Tumor Screening (Glioma vs Non-Glioma)
        # =====================================================
        if cancer_type == "brain":
            model = get_model("brain")
            prob = float(model.predict(img_array)[0][0])

            if prob >= 0.2:
                prediction_label = "Most likely Malignant tumor (Glioma-like)"
                confidence = prob
            else:
                prediction_label = "Most likely Benign tumor (Non-Glioma-like)"
                confidence = 1 - prob

        # =====================================================
        # BREAST — Binary Cancer Detection
        # =====================================================
        elif cancer_type == "breast":
            model = get_model("breast")
            prob = float(model.predict(img_array)[0][0])

            if prob >= 0.5:
                prediction_label = "Malignant (high risk)"
                confidence = prob
            else:
                prediction_label = "Benign (low risk)"
                confidence = 1 - prob

        # =====================================================
        # SKIN — Binary Cancer Detection
        # =====================================================
        elif cancer_type == "skin":
            model = get_model("skin")
            prob = float(model.predict(img_array)[0][0])

            if prob >= 0.5:
                prediction_label = "Malignant lesion suspected"
                confidence = prob
            else:
                prediction_label = "Benign lesion"
                confidence = 1 - prob

        # -------- SAVE TO DB --------
        cursor.execute("""
            INSERT INTO predictions (cancer_type, prediction, confidence, created_at)
            VALUES (?, ?, ?, ?)
        """, (
            cancer_type,
            prediction_label,
            round(confidence, 4),
            datetime.utcnow().isoformat()
        ))

        prediction_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return {
            "prediction_id": prediction_id,
            "cancer_type": cancer_type,
            "prediction": prediction_label,
            "confidence": round(confidence, 4)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
