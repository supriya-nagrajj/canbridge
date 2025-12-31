import tensorflow as tf
import os

# backend/app/services/model_loader.py

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

_models = {}

def get_model(cancer_type: str):
    """
    Loads and returns the model for the given cancer type.
    Uses singleton pattern (loads once).
    """
    if cancer_type == "brain":
        if "brain" not in _models:
            model_path = os.path.join(MODEL_DIR, "braintumor.keras")
            _models["brain"] = tf.keras.models.load_model(model_path)
        return _models["brain"]

    # breast & lung will be added later
    return None
