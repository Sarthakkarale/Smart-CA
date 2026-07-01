from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.profile.financial_profile import FinancialProfile
from app.repositories.profile.profile_repository import ProfileRepository
from app.schemas.profile.profile_schema import (
    FinancialProfileCreate,
    FinancialProfileUpdate,
)


class ProfileService:

    @staticmethod
    def create_profile(
        db: Session,
        user_id: int,
        profile_data: FinancialProfileCreate,
    ):
        existing_profile = ProfileRepository.get_by_user_id(db, user_id)

        if existing_profile:
            raise HTTPException(
                status_code=400,
                detail="Profile already exists."
            )

        profile = FinancialProfile(
            user_id=user_id,
            **profile_data.model_dump()
        )

        return ProfileRepository.create(db, profile)

    @staticmethod
    def get_profile(
        db: Session,
        user_id: int,
    ):
        profile = ProfileRepository.get_by_user_id(db, user_id)

        if not profile:
            raise HTTPException(
                status_code=404,
                detail="Profile not found."
            )

        return profile

    @staticmethod
    def update_profile(
        db: Session,
        user_id: int,
        profile_data: FinancialProfileUpdate,
    ):
        profile = ProfileRepository.get_by_user_id(db, user_id)

        if not profile:
            raise HTTPException(
                status_code=404,
                detail="Profile not found."
            )

        update_data = profile_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(profile, key, value)

        return ProfileRepository.update(db, profile)

    @staticmethod
    def delete_profile(
        db: Session,
        user_id: int,
    ):
        profile = ProfileRepository.get_by_user_id(db, user_id)

        if not profile:
            raise HTTPException(
                status_code=404,
                detail="Profile not found."
            )

        ProfileRepository.delete(db, profile)

        return {
            "message": "Profile deleted successfully."
        }