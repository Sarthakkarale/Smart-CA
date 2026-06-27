from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth.auth import RegisterRequest, LoginRequest
from app.db.database import get_db
from app.services.auth.auth_service import register_user, login_user
from app.core.security import get_current_user
from app.models.auth.user import User


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db)
):
    return register_user(user, db)


@router.post("/login")
def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):
    return login_user(user, db)


@router.get("/me")
def get_my_profile(
    current_user: User = Depends(get_current_user)
):
    return {
        "user_id": current_user.user_id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "phone": current_user.phone,
        "role_id": current_user.role_id,
        "is_active": current_user.is_active
    }