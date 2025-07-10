from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.model import InputFeatures
from app.predict import make_prediction
from app.gradio_ui import create_gradio_interface
from gradio.routes import mount_gradio_app

import os
import json
from datetime import datetime
from collections import Counter
from google.cloud import bigquery


# === CONFIG ===

bq_client = bigquery.Client()
dataset_id = "credit_model_logs"
table_id = "predictions"

# === FASTAPI APP ===
app = FastAPI(title="Credit Default Prediction API")


@app.post("/predict")
def predict(features: InputFeatures):
    prediction = make_prediction(features)

    row = {
        "timestamp": datetime.now().isoformat(),
        "input_json": json.dumps(features.dict()),
        "prediction": int(prediction),
    }

    try:
        errors = bq_client.insert_rows_json(f"{dataset_id}.{table_id}", [row])
        if errors:
            print("❌ Error al insertar en BigQuery:", errors)
    except Exception as e:
        print("❌ Error al conectar con BigQuery:", str(e))

    return {"prediction": prediction}


@app.get("/health")
def health():
    return {"status": "ok"}


# === GRADIO ===
interface = create_gradio_interface()
app = mount_gradio_app(app, interface, path="/gradio")
