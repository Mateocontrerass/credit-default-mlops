# Credit Default Prediction API 🧠💳

This project is an end-to-end machine learning system to predict whether a customer will default on a credit payment. It includes a FastAPI-based prediction service, a Gradio web UI, automatic logging to BigQuery, and CI/CD with GitHub Actions. The entire system is containerized and deployable on Google Cloud Run.

---

## 🚀 Features

- **Prediction API** built with FastAPI
- **Gradio Web UI** for interactive input
- **Prediction logging** directly to BigQuery
- **CI pipeline** with formatting, linting, and tests
- **Dockerized** for reproducibility
- **Cloud Run** deployment on GCP

---

## 🧪 How it works

### 🔗 API Endpoint

- **POST** `/predict`
- **Input (JSON)**

```json
{
  "RevolvingUtilizationOfUnsecuredLines": 0.766,
  "age": 45,
  "NumberOfTime30_59DaysPastDueNotWorse": 2,
  "DebtRatio": 0.802,
  "MonthlyIncome": 5000,
  "NumberOfOpenCreditLinesAndLoans": 13,
  "NumberOfTimes90DaysLate": 0,
  "NumberRealEstateLoansOrLines": 6,
  "NumberOfTime60_89DaysPastDueNotWorse": 0,
  "NumberOfDependents": 2
}
```

- **Output**

```json
{
  "prediction": 0
}
```

- **GET** `/gradio`  
  Launches the Gradio UI for form-based prediction.

---

## 🛠️ Setup & Development

### 📦 Install

```bash
git clone https://github.com/your-username/credit-default-api.git
cd credit-default-api
make install  # Or use `pip install -r requirements.txt`
```

### 🚀 Run Locally

```bash
make run
# Or manually:
# uvicorn app.main:app --reload --port 8000
```

Access:
- API: http://localhost:8000/predict
- Gradio UI: http://localhost:8000/gradio

---

## ✅ Tests & Linting

```bash
make lint       # Run black formatting check
make test       # Run pytest
```

---

## ☁️ Cloud Deployment (GCP)

- Fully deployed using Google Cloud Run
- Logs predictions to BigQuery (`credit_model_logs.prediction_logs`)
- Docker image built via GitHub Actions CI pipeline

---

## 📁 Project Structure

```
├── app/
│   ├── main.py              # FastAPI app
│   ├── model.py             # Pydantic schema
│   ├── predict.py           # Prediction logic
│   └── gradio_ui.py         # Gradio UI
├── models/                  # Trained ML model (pickle)
├── .github/workflows/ci.yml# CI Pipeline
├── Dockerfile               # Docker for Cloud Run
├── Makefile                 # Automation commands
├── requirements.txt         # Python dependencies
└── README.md
```

---

## Author

Mateo Contreras – [LinkedIn](https://www.linkedin.com/in/mateo-contreras-data)

---

## License

MIT – feel free to use, modify, and deploy.
