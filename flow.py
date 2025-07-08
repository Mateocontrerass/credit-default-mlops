from prefect import flow, task
from src.train_model import run_training



@flow(name="credit-default-training-pipeline", description="A flow to train a credit default prediction model.")

def training_pipeline():
    run_training(
        train_path="data/cs-training.csv",
        test_path="data/cs-test.csv",
        model_path="models/model_lr.pkl"
    )


if __name__ == "__main__":
    training_pipeline()
