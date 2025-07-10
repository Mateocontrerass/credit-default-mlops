# Credit Default Prediction API - An end to end MLOps Project
### Project set up on the 9th of July 2025, API up until 30th of July 2025.
Credit default occurs when a borrower fails to repay a loan according to the agreed terms. For banks and financial institutions, accurately identifying customers who are at high risk of default is critical to minimizing financial losses and maintaining portfolio health.

This project addresses the problem by developing a machine learning system that predicts the likelihood of a customer defaulting on their credit obligations. The goal is to automate risk assessment and support decision-making for loan approvals and credit limit assignments.

We use the "Give Me Some Credit" dataset from Kaggle, which contains anonymized credit-related features for over 150,000 individuals. These include variables like income, age, debt ratio, and history of late payments.

---

## 🚀 Features

- **MLFlow** for experiment tracking
- **Prefect** orchestration for retraining and automation
- **FastAPI** backend for serving predictions
- **Gradio** web interface for interactive input
- **Prediction logging** directly to Google BigQuery
- **CI pipeline** with `pytest`, `black`, and GitHub Actions
- **Dockerized** environment for full reproducibility
- **Cloud Run** deployment on Google Cloud Platform (GCP)

---

## ⚙️ How It Works

###  API Endpoints

- **POST** `/predict`  
  Returns the default prediction (0 or 1)

  **Example input**  
  `POST https://credit-predictor-564519181363.us-central1.run.app/predict`
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

  **Response**
  ```json
  {
    "prediction": 0
  }
  ```

- **GET** `/gradio`  
  Interactive UI for predictions  
  👉 [Try it Live](https://credit-predictor-564519181363.us-central1.run.app/gradio/)

---

## 🛠️ Setup & Development

### 📦 Install

```bash
git clone https://github.com/your-username/credit-default-mlops.git
cd credit-default-mlops
make install  # Or use `pip install -r requirements.txt`
```
> This installs both production and dev dependencies (via `requirements.txt` and `requirements-dev.txt`) and activates `pre-commit` hooks.

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

Tests include:
- `/predict` endpoint testing
- End-to-end test via Dockerized container
---

## ☁️ Cloud Deployment (GCP)

- Deployed on **Google Cloud Run**
- Predictions logged directly to **BigQuery** (`credit_model_logs.prediction_logs`)
- CI pipeline via **GitHub Actions**
- Docker image built using the included `Dockerfile`

---

## 📁 Project Structure

```
├── app/
│   ├── main.py              # FastAPI app entrypoint
│   ├── model.py             # Input schema with Pydantic
│   ├── predict.py           # ML model loading & prediction
│   └── gradio_ui.py         # Gradio interface
├── src/
│   ├── configs.py           
│   └── train_model.py       # Training logic + Prefect flow
├── models/
│   └── model_lr.pkl         # Trained Logistic Regression model
├── test/
│   ├── test_predict.py      # Unit test for /predict
│   └── test_docker_predict.py # Integration test in container
├── notebooks/
│   └── model.ipynb          # EDA and training experiments
├── .github/workflows/
│   └── ci.yml               # GitHub Actions pipeline
├── Dockerfile               # Cloud Run-compatible build
├── Makefile                 # CLI commands
├── requirements.txt         # Production deps
├── requirements-dev.txt     # Linting / test / CI tools
└── README.md
```

---

## 👤 Author

**Mateo Contreras**  
💼 Credit Risk Data Scientist | Banco de Bogotá  
🔗 [LinkedIn](https://www.linkedin.com/in/mateocontreras/)

---

## License

MIT — free to use, share, and modify.
