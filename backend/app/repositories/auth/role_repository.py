from sqlalchemy.orm import Session

from app.models.auth.role import Role


class RoleRepository:

    @staticmethod
    def get_by_name(db: Session, role_name: str):
        return db.query(Role).filter(Role.role_name == role_name).first()