from sqlalchemy.orm import Session

from app.models.auth.session import UserSession


class SessionRepository:

    @staticmethod
    def create(db: Session, session: UserSession):
        db.add(session)
        db.commit()
        db.refresh(session)
        return session

    @staticmethod
    def get_by_refresh_token(db: Session, refresh_token: str):
        return (
            db.query(UserSession)
            .filter(
                UserSession.refresh_token == refresh_token,
                UserSession.is_revoked == False
            )
            .first()
        )

    @staticmethod
    def revoke(db: Session, session: UserSession):
        session.is_revoked = True
        db.commit()

    @staticmethod
    def revoke_by_refresh_token(db: Session, refresh_token: str):

        session = (
            db.query(UserSession)
            .filter(UserSession.refresh_token == refresh_token)
            .first()
        )

        if session:
            session.is_revoked = True
            db.commit()

        return session