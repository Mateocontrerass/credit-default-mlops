import requests


def test_predict_endpoint_running():
    url = "http://localhost:8000/predict"
    payload = {
        "RevolvingUtilizationOfUnsecuredLines": 0.5,
        "age": 45,
        "NumberOfTime30-59DaysPastDueNotWorse": 0,
        "DebtRatio": 0.3,
        "MonthlyIncome": 5000,
        "NumberOfOpenCreditLinesAndLoans": 5,
        "NumberOfTimes90DaysLate": 0,
        "NumberRealEstateLoansOrLines": 1,
        "NumberOfTime60-89DaysPastDueNotWorse": 0,
        "NumberOfDependents": 2,
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200
    json_data = response.json()
    assert "prediction" in json_data
    assert 0 <= json_data["prediction"] <= 1


# curl -X POST http://127.0.0.1:8001/predict   -H "Content-Type: application/json"   -d '{
#     "RevolvingUtilizationOfUnsecuredLines": 0.5,
#     "age": 45,
#     "NumberOfTime30-59DaysPastDueNotWorse": 1,
#     "DebtRatio": 0.2,
#     "MonthlyIncome": 5000,
#     "NumberOfOpenCreditLinesAndLoans": 6,
#     "NumberOfTimes90DaysLate": 0,
#     "NumberRealEstateLoansOrLines": 1,
#     "NumberOfTime60-89DaysPastDueNotWorse": 0,
#     "NumberOfDependents": 2
#   }'
