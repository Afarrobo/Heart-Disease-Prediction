from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI

from app.schemas import HeartInput, PredictionOutput

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "heart_model.joblib"
FEATURES = list(HeartInput.model_fields.keys())

app = FastAPI(title="Heart Disease Prediction API", version="1.0.0")
model = joblib.load(MODEL_PATH)


@app.get("/")
def root():
    return {"message": "Heart Disease API. See /docs"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/info")
def info():
    return {
        "model_type": type(model).__name__,
        "n_features": len(FEATURES),
        "features": FEATURES,
        "target": "heart_disease (true = presence, false = absence)",
    }


@app.post("/predict", response_model=PredictionOutput)
def predict(data: HeartInput):
    X = pd.DataFrame([data.model_dump()])[FEATURES]
    pred = int(model.predict(X)[0])
    proba = float(model.predict_proba(X)[0][1])
    return PredictionOutput(heart_disease=bool(pred), probability=round(proba, 4))
