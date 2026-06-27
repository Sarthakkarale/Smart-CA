from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.auth.user import User, Role
from app.schemas.auth.auth import RegisterRequest
from app.core.security import hash_password
from app.core.security import hash_password, verify_password, create_access_token


def register_user(user: RegisterRequest, db: Session):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    user_role = db.query(Role).filter(Role.role_name == "USER").first()

    if not user_role:
        raise HTTPException(
            status_code=500,
            detail="USER role not found in roles table."
        )

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password_hash=hash_password(user.password),
        role_id=user_role.role_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "success": True,
        "message": "Registration successful."
    }
from app.core.security import verify_password
from app.schemas.auth.auth import LoginRequest


def login_user(user: LoginRequest, db: Session):

    existing_user = db.query(User).filter(User.email == user.email).first()

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

    access_token = create_access_token(
    data={
        "sub": existing_user.email,
        "user_id": existing_user.user_id,
        "role_id": existing_user.role_id
    }
)

    return {
    "success": True,
    "message": "Login successful.",
    "access_token": access_token,
    "token_type": "bearer",
    "user": {
        "user_id": existing_user.user_id,
        "full_name": existing_user.full_name,
        "email": existing_user.email,
        "role_id": existing_user.role_id
    }
    }