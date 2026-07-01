from sqlalchemy.orm import Session

from app.models.auth.user import User
from app.models.profile.financial_profile import FinancialProfile


class DashboardRepository:

    @staticmethod
    def get_user(db: Session, user_id: int):
        """
        Fetch authenticated user.
        """
        return (
            db.query(User)
            .filter(User.user_id == user_id)
            .first()
        )

    @staticmethod
    def get_financial_profile(db: Session, user_id: int):
        """
        Fetch financial profile.
        """
        return (
            db.query(FinancialProfile)
            .filter(FinancialProfile.user_id == user_id)
            .first()
        )