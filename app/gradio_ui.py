import gradio as gr
import requests
from app.predict import make_prediction
from app.model import InputFeatures


# Define the Gradio UI function
def gradio_predict(
    RevolvingUtilizationOfUnsecuredLines: float,
    age: int,
    NumberOfTime30_59DaysPastDueNotWorse: int,
    DebtRatio: float,
    MonthlyIncome: float,
    NumberOfOpenCreditLinesAndLoans: int,
    NumberOfTimes90DaysLate: int,
    NumberRealEstateLoansOrLines: int,
    NumberOfTime60_89DaysPastDueNotWorse: int,
    NumberOfDependents: int,
):
    features = InputFeatures(
        RevolvingUtilizationOfUnsecuredLines=RevolvingUtilizationOfUnsecuredLines,
        age=age,
        NumberOfTime30_59DaysPastDueNotWorse=NumberOfTime30_59DaysPastDueNotWorse,
        DebtRatio=DebtRatio,
        MonthlyIncome=MonthlyIncome,
        NumberOfOpenCreditLinesAndLoans=NumberOfOpenCreditLinesAndLoans,
        NumberOfTimes90DaysLate=NumberOfTimes90DaysLate,
        NumberRealEstateLoansOrLines=NumberRealEstateLoansOrLines,
        NumberOfTime60_89DaysPastDueNotWorse=NumberOfTime60_89DaysPastDueNotWorse,
        NumberOfDependents=NumberOfDependents,
    )

    prediction = make_prediction(features)
    return prediction


# Create the Gradio interface using the new API
def create_gradio_interface():
    inputs = [
        gr.Number(label="Revolving Utilization of Unsecured Lines"),
        gr.Number(label="Age"),
        gr.Number(label="Number of Time 30-59 Days Past Due Not Worse"),
        gr.Number(label="Debt Ratio"),
        gr.Number(label="Monthly Income"),
        gr.Number(label="Number of Open Credit Lines and Loans"),
        gr.Number(label="Number of Times 90 Days Late"),
        gr.Number(label="Number of Real Estate Loans or Lines"),
        gr.Number(label="Number of Time 60-89 Days Past Due Not Worse"),
        gr.Number(label="Number of Dependents"),
    ]

    outputs = gr.Textbox()

    return gr.Interface(fn=gradio_predict, inputs=inputs, outputs=outputs)
