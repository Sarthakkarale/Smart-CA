from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


# ==========================================================
# Base Schema
# ==========================================================

class FinancialProfileBase(BaseModel):

    # ==========================
    # Personal
    # ==========================

    dob: Optional[date] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None

    # ==========================
    # Tax
    # ==========================

    pan: Optional[str] = None
    aadhaar: Optional[str] = None
    tax_regime: Optional[str] = None
    resident_status: Optional[str] = None

    gst_registered: bool = False
    gst_number: Optional[str] = None
    itr_history: Optional[str] = None

    # ==========================
    # Professional
    # ==========================

    employment_type: Optional[str] = None
    occupation: Optional[str] = None
    company_name: Optional[str] = None

    annual_income: Optional[Decimal] = None

    experience: Optional[int] = None

    business_type: Optional[str] = None

    # ==========================
    # Financial
    # ==========================

    bank_name: Optional[str] = None

    monthly_expense: Optional[Decimal] = None

    existing_investments: Optional[Decimal] = None

    loan_amount: Optional[Decimal] = None

    insurance_cover: Optional[Decimal] = None

    emergency_fund: Optional[Decimal] = None

    # ==========================
    # Goals
    # ==========================

    retirement: bool = False

    buy_house: bool = False

    buy_car: bool = False

    child_education: bool = False

    wealth_creation: bool = False

    travel: bool = False

    other_goal: Optional[str] = None

    target_year: Optional[int] = None


# ==========================================================
# Create
# ==========================================================

class FinancialProfileCreate(FinancialProfileBase):
    pass


# ==========================================================
# Update
# ==========================================================

class FinancialProfileUpdate(FinancialProfileBase):
    pass


# ==========================================================
# Response
# ==========================================================

class FinancialProfileResponse(FinancialProfileBase):

    profile_id: int

    user_id: int

    class Config:
        from_attributes = True