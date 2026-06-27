from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.auth.user import User
from app.schemas.auth.auth import RegisterRequest, LoginRequest
from app.core.security import hash_password, verify_password
from app.services.auth.token_service import TokenService
from app.repositories.auth.user_repository import UserRepository
from app.repositories.auth.role_repository import RoleRepository
from app.services.auth.session_service import SessionService


def register_user(user: RegisterRequest, db: Session):

    existing_user = UserRepository.get_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    user_role = RoleRepository.get_by_name(db, "USER")

    if not user_role:
        raise HTTPException(
            status_code=500,
            detail="USER role not found."
        )

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password_hash=hash_password(user.password),
        role_id=user_role.role_id
    )

    UserRepository.create(db, new_user)

    return {
        "success": True,
        "message": "Registration successful."
    }


def login_user(user: LoginRequest, db: Session):

    existing_user = UserRepository.get_by_email(db, user.email)

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    if not verify_password(user.password, existing_user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid password."
        )

    if not existing_user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Account is inactive."
        )

    access_token = TokenService.create_access_token(
    data={
        "sub": existing_user.email,
        "user_id": existing_user.user_id,
        "role_id": existing_user.role_id
    }
)

    refresh_token = TokenService.create_refresh_token(
    data={
        "sub": existing_user.email,
        "user_id": existing_user.user_id,
        "role_id": existing_user.role_id
    }
)

    SessionService.create_session(
    db=db,
    user_id=existing_user.user_id,
    refresh_token=refresh_token
    )

    return {
    "success": True,
    "message": "Login successful.",
    "access_token": access_token,
    "refresh_token": refresh_token,
    "token_type": "bearer",
    "user": {
        "user_id": existing_user.user_id,
        "full_name": existing_user.full_name,
        "email": existing_user.email,
        "role_id": existing_user.role_id
    }
}