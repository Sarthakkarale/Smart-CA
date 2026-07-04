from decimal import Decimal
from typing import List

from pydantic import BaseModel


class DashboardSummaryResponse(BaseModel):
    monthly_income: Decimal
    monthly_expenses: Decimal
    monthly_savings: Decimal
    financial_health_score: int

    class Config:
        from_attributes = True


class AISuggestion(BaseModel):
    title: str
    message: str

    class Config:
        from_attributes = True


class DashboardChartsResponse(BaseModel):
    income: List[Decimal]
    expenses: List[Decimal]
    savings: List[Decimal]

    class Config:
        from_attributes = True


class ProfileSummaryResponse(BaseModel):
    name: str
    occupation: str | None = None
    risk_appetite: str | None = None
    financial_goals: str | None = None

    class Config:
        from_attributes = True