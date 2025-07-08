# data_utils.py

import os
import mlflow
import polars as pl
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
from prefect import task


@task
def load_data(path):
    return pl.read_csv(path)


@task
def preprocess(df):
    df = df.with_columns(
        [
            pl.when(
                pl.col("MonthlyIncome").is_null() | (pl.col("MonthlyIncome") == "NA")
            )
            .then(0)
            .otherwise(pl.col("MonthlyIncome"))
            .cast(pl.Int32)
            .alias("MonthlyIncome"),
            pl.when(
                pl.col("NumberOfDependents").is_null()
                | (pl.col("NumberOfDependents") == "NA")
            )
            .then(0)
            .otherwise(pl.col("NumberOfDependents"))
            .cast(pl.Int32)
            .alias("NumberOfDependents"),
            pl.col("SeriousDlqin2yrs")
            .fill_null(0)
            .cast(pl.Int32)
            .alias("SeriousDlqin2yrs"),
        ]
    )

    df = df.fill_null(0)
    df = df.select(df.columns[1:])
    x = df.drop("SeriousDlqin2yrs").to_numpy()
    y = df["SeriousDlqin2yrs"].to_numpy()
    return x, y


@task
def train_model(x, y):
    model = LogisticRegression(max_iter=1000, random_state=123)
    model.fit(x, y)
    return model


@task
def evaluate_model(model, x, y):
    y_pred = model.predict(x)
    accuracy = accuracy_score(y, y_pred)

    return accuracy


@task
def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(model, f)


from prefect import task
import mlflow
import mlflow.sklearn


@task
def run_training(train_path, test_path, model_path):
    # Configura la URI de seguimiento (puede ser localhost o tu contenedor)
    mlflow.set_experiment("credit_default_lr")

    with mlflow.start_run():
        # Carga datos
        df_train = load_data.submit(train_path)
        df_test = load_data.submit(test_path)

        # Preprocesamiento
        x_train, y_train = preprocess.submit(df_train).result()
        x_test, y_test = preprocess.submit(df_test).result()

        # Entrenamiento
        model = train_model.submit(x_train, y_train).result()
        accuracy = evaluate_model.submit(model, x_test, y_test).result()

        # Log de parámetros y métricas
        mlflow.log_param("model_type", "logistic_regression")
        mlflow.log_metric("accuracy", accuracy)

        # Guarda modelo como artefacto (en MLflow UI → artefacts)
        mlflow.sklearn.log_model(model, artifact_path="model")

        # Guarda localmente si necesitas usarlo con FastAPI/Gradio
        save_model.submit(model, model_path)

        print(f"✅ Modelo entrenado con accuracy: {accuracy:.4f}")
