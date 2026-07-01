from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DECIMAL,
    DateTime,
    ForeignKey,
    Enum,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.database import Base


class FinancialProfile(Base):
    __tablename__ = "financial_profile"

    profile_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    age = Column(Integer, nullable=False)

    occupation = Column(String(100))

    monthly_income = Column(
        DECIMAL(12, 2),
        nullable=False
    )

    monthly_expenses = Column(
        DECIMAL(12, 2)
    )

    annual_income = Column(
        DECIMAL(12, 2)
    )

    family_size = Column(Integer)

    dependents = Column(Integer)

    marital_status = Column(
        Enum("SINGLE", "MARRIED", "OTHER"),
        nullable=True
    )

    risk_appetite = Column(
        Enum("LOW", "MODERATE", "HIGH"),
        nullable=True
    )

    financial_goals = Column(Text)

    existing_savings = Column(
        DECIMAL(12, 2)
    )

    existing_investments = Column(
        DECIMAL(12, 2)
    )

    existing_insurance = Column(
        DECIMAL(12, 2)
    )

    debt_amount = Column(
        DECIMAL(12, 2)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    user = relationship(
        "User",
        back_populates="financial_profile"
    )
    