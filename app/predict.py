import numpy as np
from app.load_model import load_model
from app.model import InputFeatures

model = load_model()


def make_prediction(features: InputFeatures) -> float:
    """
    Make a prediction using the loaded model and input features.

    Args:
        features (InputFeatures): Input features for the prediction.

    Returns:
        float: Predicted probability of credit default.
    """
    # Convert input features to a numpy array
    input_data = np.array(
        [
            [
                features.RevolvingUtilizationOfUnsecuredLines,
                features.age,
                features.NumberOfTime30_59DaysPastDueNotWorse,
                features.DebtRatio,
                features.MonthlyIncome,
                features.NumberOfOpenCreditLinesAndLoans,
                features.NumberOfTimes90DaysLate,
                features.NumberRealEstateLoansOrLines,
                features.NumberOfTime60_89DaysPastDueNotWorse,
                features.NumberOfDependents,
            ]
        ]
    )

    # Make prediction
    prediction = model.predict_proba(input_data)[:, 1]

    return float(prediction[0])  # Return the probability of default as a float
