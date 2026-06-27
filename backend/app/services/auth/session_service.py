from datetime import datetime, timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.auth.session import UserSession
from app.repositories.auth.session_repository import SessionRepository
from app.services.auth.token_service import TokenService
from app.repositories.auth.user_repository import UserRepository


class SessionService:

    @staticmethod
    def create_session(
        db: Session,
        user_id: int,
        refresh_token: str,
        ip_address: str = None,
        user_agent: str = None
    ):
        session = UserSession(
            user_id=user_id,
            refresh_token=refresh_token,
            ip_address=ip_address,
            user_agent=user_agent,
            expires_at=datetime.utcnow() + timedelta(days=7)
        )

        return SessionRepository.create(db, session)

    @staticmethod
    def refresh_access_token(db: Session, refresh_token: str):

        payload = TokenService.decode_token(refresh_token)

        if payload is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired refresh token"
            )

        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=401,
                detail="Invalid token type"
            )

        session = SessionRepository.get_by_refresh_token(db, refresh_token)

        if not session:
            raise HTTPException(
                status_code=401,
                detail="Session not found or revoked"
            )

        if session.expires_at < datetime.utcnow():
            raise HTTPException(
                status_code=401,
                detail="Refresh token expired"
            )

        user = UserRepository.get_by_id(db, session.user_id)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        access_token = TokenService.create_access_token(
            data={
                "sub": user.email,
                "user_id": user.user_id,
                "role_id": user.role_id
            }
        )

        return {
            "success": True,
            "access_token": access_token,
            "token_type": "bearer"
        }
    
    @staticmethod
    def logout(db: Session, refresh_token: str):

        session = SessionRepository.revoke_by_refresh_token(
            db,
            refresh_token
        )

        if not session:
            raise HTTPException(
                status_code=404,
                detail="Session not found"
            )

        return {
            "success": True,
            "message": "Logged out successfully."
        }