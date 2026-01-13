# backend/app/services/model_loader.py

import os
import tensorflow as tf

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

_models = {}


def load_models():
    global _models

    try:
        _models["brain"] = tf.keras.models.load_model(
            os.path.join(MODEL_DIR, "glioma_screening_model.keras")
        )
        print("✅ Brain model loaded")
    except Exception as e:
        print("❌ Failed to load brain model:", e)
        _models["brain"] = None

    try:
        _models["breast"] = tf.keras.models.load_model(
            os.path.join(MODEL_DIR, "breast_busi_resnet50.keras")
        )
        print("✅ Breast model loaded")
    except Exception as e:
        print("❌ Failed to load breast model:", e)
        _models["breast"] = None

    try:
        _models["skin"] = tf.keras.models.load_model(
            os.path.join(MODEL_DIR, "skin_resnet50.keras")
        )
        print("✅ Skin model loaded")
    except Exception as e:
        print("❌ Failed to load skin model:", e)
        _models["skin"] = None


def get_model(model_name: str):
    model = _models.get(model_name)

    if model is None:
        raise RuntimeError(f"Model '{model_name}' is not loaded")

    return model
