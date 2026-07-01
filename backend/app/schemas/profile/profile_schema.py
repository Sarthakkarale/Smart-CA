from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


class FinancialProfileBase(BaseModel):
    age: int
    occupation: Optional[str] = None

    monthly_income: Decimal
    monthly_expenses: Optional[Decimal] = None
    annual_income: Optional[Decimal] = None

    family_size: Optional[int] = None
    dependents: Optional[int] = None

    marital_status: Optional[str] = None
    risk_appetite: Optional[str] = None

    financial_goals: Optional[str] = None

    existing_savings: Optional[Decimal] = None
    existing_investments: Optional[Decimal] = None
    existing_insurance: Optional[Decimal] = None

    debt_amount: Optional[Decimal] = None


class FinancialProfileCreate(FinancialProfileBase):
    pass


class FinancialProfileUpdate(BaseModel):
    age: Optional[int] = None
    occupation: Optional[str] = None

    monthly_income: Optional[Decimal] = None
    monthly_expenses: Optional[Decimal] = None
    annual_income: Optional[Decimal] = None

    family_size: Optional[int] = None
    dependents: Optional[int] = None

    marital_status: Optional[str] = None
    risk_appetite: Optional[str] = None

    financial_goals: Optional[str] = None

    existing_savings: Optional[Decimal] = None
    existing_investments: Optional[Decimal] = None
    existing_insurance: Optional[Decimal] = None

    debt_amount: Optional[Decimal] = None


class FinancialProfileResponse(FinancialProfileBase):
    profile_id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)

