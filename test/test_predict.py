import sys
import os

# Agrega el directorio padre al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.model import InputFeatures
from app.predict import make_prediction


def test_make_prediction_valid_input():
    features = InputFeatures(
        RevolvingUtilizationOfUnsecuredLines=0.5,
        age=45,
        NumberOfTime30_59DaysPastDueNotWorse=0,
        DebtRatio=0.3,
        MonthlyIncome=5000,
        NumberOfOpenCreditLinesAndLoans=5,
        NumberOfTimes90DaysLate=0,
        NumberRealEstateLoansOrLines=1,
        NumberOfTime60_89DaysPastDueNotWorse=0,
        NumberOfDependents=2,
    )
    prediction = make_prediction(features)
    assert 0 <= prediction <= 1
