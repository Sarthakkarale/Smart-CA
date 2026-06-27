from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user_model import User, Role
from app.schemas.auth_schema import RegisterRequest
from app.core.security import hash_password


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