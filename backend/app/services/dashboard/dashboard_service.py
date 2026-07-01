from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.dashboard.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def get_dashboard_summary(db: Session, user_id: int):
        """
        Returns dashboard summary for authenticated user.
        """

        profile = DashboardRepository.get_financial_profile(db, user_id)

        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Financial profile not found."
            )

        monthly_income = profile.monthly_income or Decimal("0")
        monthly_expenses = profile.monthly_expenses or Decimal("0")

        monthly_savings = monthly_income - monthly_expenses

        health_score = DashboardService.calculate_health_score(profile)

        return {
            "monthly_income": monthly_income,
            "monthly_expenses": monthly_expenses,
            "monthly_savings": monthly_savings,
            "financial_health_score": health_score
        }

    @staticmethod
    def calculate_health_score(profile) -> int:
        """
        Financial Health Score Algorithm

        Initial Score = 100

        -20 if monthly expenses exceed 80% of income
        -20 if debt exceeds annual income
        -15 if savings are less than 6 months of income
        -15 if investments are zero

        Final score remains between 0 and 100.
        """

        score = 100

        income = profile.monthly_income or Decimal("0")
        expenses = profile.monthly_expenses or Decimal("0")

        annual_income = profile.annual_income or (income * 12)

        savings = profile.existing_savings or Decimal("0")
        investments = profile.existing_investments or Decimal("0")
        debt = profile.debt_amount or Decimal("0")

        # High monthly expenses
        if income > 0 and expenses > income * Decimal("0.80"):
            score -= 20

        # High debt
        if debt > annual_income:
            score -= 20

        # Low savings
        if savings < income * 6:
            score -= 15

        # No investments
        if investments == 0:
            score -= 15

        # Clamp score
        score = max(0, min(score, 100))

        return score
    
    @staticmethod
    def get_ai_suggestions(db: Session, user_id: int):
        """
        Generate AI-based financial suggestions.
        """

        profile = DashboardRepository.get_financial_profile(db, user_id)

        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Financial profile not found."
            )

        suggestions = []

        income = profile.monthly_income or Decimal("0")
        expenses = profile.monthly_expenses or Decimal("0")
        annual_income = profile.annual_income or (income * 12)

        savings = profile.existing_savings or Decimal("0")
        investments = profile.existing_investments or Decimal("0")
        insurance = profile.existing_insurance or Decimal("0")
        debt = profile.debt_amount or Decimal("0")

        # High Expenses
        if income > 0 and expenses > income * Decimal("0.80"):
            suggestions.append({
                "title": "Reduce Expenses",
                "message": "Your monthly expenses are more than 80% of your monthly income."
            })

        # High Debt
        if debt > annual_income:
            suggestions.append({
                "title": "Reduce Debt",
                "message": "Your total debt is greater than your annual income."
            })

        # Low Savings
        if savings < income * 6:
            suggestions.append({
                "title": "Emergency Fund",
                "message": "Build an emergency fund equal to at least six months of income."
            })

        # No Investments
        if investments == 0:
            suggestions.append({
                "title": "Start Investing",
                "message": "Begin investing regularly to build long-term wealth."
            })

        # No Insurance
        if insurance == 0:
            suggestions.append({
                "title": "Insurance",
                "message": "Consider purchasing health and life insurance."
            })

        # Good Financial Profile
        if not suggestions:
            suggestions.append({
                "title": "Excellent",
                "message": "Your financial profile looks healthy. Keep monitoring your finances regularly."
            })

        return suggestions

    @staticmethod
    def get_chart_data(db: Session, user_id: int):
        """
        Returns chart data.

        TODO:
        Replace mock values with actual monthly financial history
        after transaction/history module is implemented.
        """

        profile = DashboardRepository.get_financial_profile(db, user_id)

        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Financial profile not found."
            )

        income = profile.monthly_income or Decimal("0")
        expenses = profile.monthly_expenses or Decimal("0")
        savings = income - expenses

        return {
            "income": [
                income - Decimal("10000"),
                income - Decimal("5000"),
                income
            ],
            "expenses": [
                expenses - Decimal("3000"),
                expenses - Decimal("1000"),
                expenses
            ],
            "savings": [
                savings - Decimal("7000"),
                savings - Decimal("4000"),
                savings
            ]
        }

    @staticmethod
    def get_profile_summary(db: Session, user_id: int):
        """
        Returns profile summary for dashboard.
        """

        user = DashboardRepository.get_user(db, user_id)
        profile = DashboardRepository.get_financial_profile(db, user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found."
            )

        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Financial profile not found."
            )

        return {
            "name": user.full_name,
            "occupation": profile.occupation,
            "risk_appetite": profile.risk_appetite,
            "financial_goals": profile.financial_goals
        }