from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.security import get_current_user

from app.models.auth.user import User

from app.schemas.profile.profile_schema import (
    FinancialProfileCreate,
    FinancialProfileUpdate,
    FinancialProfileResponse
)

from app.services.profile.profile_service import ProfileService


router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.post(
    "/create",
    response_model=FinancialProfileResponse
)
def create_profile(
    profile: FinancialProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ProfileService.create_profile(
        db=db,
        user_id=current_user.user_id,
        profile_data=profile
    )


@router.get(
    "/me",
    response_model=FinancialProfileResponse
)
def get_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ProfileService.get_profile(
        db=db,
        user_id=current_user.user_id
    )


@router.put(
    "/update",
    response_model=FinancialProfileResponse
)
def update_profile(
    profile: FinancialProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ProfileService.update_profile(
        db=db,
        user_id=current_user.user_id,
        profile_data=profile
    )


@router.delete("/delete")
def delete_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ProfileService.delete_profile(
        db=db,
        user_id=current_user.user_id
    )
