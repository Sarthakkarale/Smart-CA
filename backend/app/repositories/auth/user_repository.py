from sqlalchemy.orm import Session

from app.models.auth.user import User


class UserRepository:

    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.user_id == user_id).first()

    @staticmethod
    def create(db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user