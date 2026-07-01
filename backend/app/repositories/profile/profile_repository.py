from sqlalchemy.orm import Session

from app.models.profile.financial_profile import FinancialProfile


class ProfileRepository:

    @staticmethod
    def create(db: Session, profile: FinancialProfile):
        db.add(profile)
        db.commit()
        db.refresh(profile)
        return profile

    @staticmethod
    def get_by_user_id(db: Session, user_id: int):
        return (
            db.query(FinancialProfile)
            .filter(FinancialProfile.user_id == user_id)
            .first()
        )

    @staticmethod
    def update(db: Session, profile: FinancialProfile):
        db.commit()
        db.refresh(profile)
        return profile

    @staticmethod
    def delete(db: Session, profile: FinancialProfile):
        db.delete(profile)
        db.commit()