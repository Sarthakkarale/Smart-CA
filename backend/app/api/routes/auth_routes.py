from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth_schema import RegisterRequest
from app.db.database import get_db
from app.services.auth_service import register_user

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