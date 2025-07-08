from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.model import InputFeatures
from app.predict import make_prediction
from app.gradio_ui import create_gradio_interface
from threading import Thread

import csv
import os
import json
from datetime import datetime
from collections import Counter

# === CONFIG FOR CSV LOGGING ===
CSV_FILE = "prediction_logs.csv"
FIELDNAMES = ["timestamp", "input_json", "prediction"]

# Create the CSV log file if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()

# === FASTAPI SETUP ===
app = FastAPI(title="Credit Default Prediction API")


@app.post("/predict")
def predict(features: InputFeatures):
    """
    Predict the probability of credit default based on input features.
    """
    prediction = make_prediction(features)

    # Save prediction to CSV
    with open(CSV_FILE, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(
            {
                "timestamp": datetime.now().isoformat(),
                "input_json": json.dumps(features.dict()),
                "prediction": int(prediction),
            }
        )

    return {"prediction": prediction}


@app.get("/monitor")
def monitor():
    """
    Returns total predictions and class distribution from CSV logs.
    """
    try:
        with open(CSV_FILE, mode="r") as f:
            reader = csv.DictReader(f)
            preds = [int(row["prediction"]) for row in reader]

        total = len(preds)
        distribution = dict(Counter(preds))

        return JSONResponse(
            {"total_predictions": total, "class_distribution": distribution}
        )

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# === RUN GRADIO ON STARTUP ===
@app.on_event("startup")
def startup():
    def run_gradio():
        interface = create_gradio_interface()
        interface.launch(
            server_name="0.0.0.0",  # <- necesario para exponer fuera del contenedor
            server_port=7860,  # <- para que coincida con tu `-p 7860:7860`
            share=False,
            inline=False,
        )

    thread = Thread(target=run_gradio)
    thread.start()
