from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date,
    DECIMAL,
    DateTime,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


class FinancialProfile(Base):
    __tablename__ = "financial_profile"

    profile_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    # ==========================
    # Personal
    # ==========================
    dob = Column(Date)
    gender = Column(String(20))
    phone = Column(String(20))
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(10))

    # ==========================
    # Tax
    # ==========================
    pan = Column(String(20))
    aadhaar = Column(String(20))
    tax_regime = Column(String(30))
    resident_status = Column(String(30))
    gst_registered = Column(Boolean, default=False)
    gst_number = Column(String(30))
    itr_history = Column(String(30))

    # ==========================
    # Professional
    # ==========================
    employment_type = Column(String(50))
    occupation = Column(String(100))
    company_name = Column(String(150))
    annual_income = Column(DECIMAL(12, 2))
    experience = Column(Integer)
    business_type = Column(String(100))

    # ==========================
    # Financial
    # ==========================
    bank_name = Column(String(100))
    monthly_expense = Column(DECIMAL(12, 2))
    existing_investments = Column(DECIMAL(12, 2))
    loan_amount = Column(DECIMAL(12, 2))
    insurance_cover = Column(DECIMAL(12, 2))
    emergency_fund = Column(DECIMAL(12, 2))

    # ==========================
    # Goals
    # ==========================
    retirement = Column(Boolean, default=False)
    buy_house = Column(Boolean, default=False)
    buy_car = Column(Boolean, default=False)
    child_education = Column(Boolean, default=False)
    wealth_creation = Column(Boolean, default=False)
    travel = Column(Boolean, default=False)

    other_goal = Column(Text)
    target_year = Column(Integer)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    user = relationship(
        "User",
        back_populates="financial_profile",
    )