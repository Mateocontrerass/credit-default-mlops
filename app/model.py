from pydantic import BaseModel, Field


class InputFeatures(BaseModel):
    RevolvingUtilizationOfUnsecuredLines: float
    age: int
    NumberOfTime30_59DaysPastDueNotWorse: int = Field(
        alias="NumberOfTime30-59DaysPastDueNotWorse"
    )
    DebtRatio: float
    MonthlyIncome: float
    NumberOfOpenCreditLinesAndLoans: int
    NumberOfTimes90DaysLate: int
    NumberRealEstateLoansOrLines: int
    NumberOfTime60_89DaysPastDueNotWorse: int = Field(
        alias="NumberOfTime60-89DaysPastDueNotWorse"
    )
    NumberOfDependents: int

    model_config = {"populate_by_name": True}
