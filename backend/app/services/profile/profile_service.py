from sqlalchemy.orm import Session
# Adjust this path to the actual filename where your FinancialProfile class lives
from app.models.profile.financial_profile import FinancialProfile # Ensure this model exists
from app.schemas.profile.profile_schema import FinancialProfileCreate, FinancialProfileUpdate

class ProfileService:

    @staticmethod
    def create_profile(db: Session, user_id: int, profile_data: FinancialProfileCreate):
        """Creates a new financial profile record for the authenticated user."""
        # Convert schema to dict and add the user_id
        profile_dict = profile_data.dict()
        profile_dict["user_id"] = user_id
        
        new_profile = FinancialProfile(**profile_dict)
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)
        return new_profile

    @staticmethod
    def get_profile(db: Session, user_id: int):
        """Fetches the user's financial profile."""
        return db.query(FinancialProfile).filter(FinancialProfile.user_id == user_id).first()

    @staticmethod
    def update_profile(db: Session, user_id: int, profile_data: FinancialProfileUpdate):
        """Updates an existing financial profile."""
        db_profile = db.query(FinancialProfile).filter(FinancialProfile.user_id == user_id).first()
        
        if db_profile:
            # Update only the fields provided in the request
            update_data = profile_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_profile, key, value)
            
            db.commit()
            db.refresh(db_profile)
        return db_profile

    @staticmethod
    def delete_profile(db: Session, user_id: int):
        """Deletes the user's financial profile."""
        db_profile = db.query(FinancialProfile).filter(FinancialProfile.user_id == user_id).first()
        if db_profile:
            db.delete(db_profile)
            db.commit()
            return {"message": "Profile successfully deleted"}
        return {"message": "Profile not found"}