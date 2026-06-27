from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError

from app.core.config import settings


class TokenService:

    @staticmethod
    def create_access_token(data: dict):

        payload = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        payload.update(
            {
                "exp": expire,
                "type": "access"
            }
        )

        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )

    @staticmethod
    def create_refresh_token(data: dict):

        payload = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(
            days=settings.REFRESH_TOKEN_EXPIRE_DAYS
        )

        payload.update(
            {
                "exp": expire,
                "type": "refresh"
            }
        )

        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )

    @staticmethod
    def decode_token(token: str):

        try:
            return jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )

        except JWTError:
            return None