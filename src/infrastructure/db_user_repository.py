from typing import Optional
from flask_sqlalchemy import SQLAlchemy

from src.domain.user import User
from src.domain.user_repository import UserRepository
from init_db import bcrypt


class DbUserRepository(UserRepository):

    def __init__(self, db_instance: SQLAlchemy):
        self.db = db_instance

    def get_by_id(self, user_id: int) -> User:
        return self.db.session.execute(
            self.db.select(User).filter_by(id=user_id)
        ).scalar_one()

    def get_by_username(self, user_name: str) -> Optional[User]:
        return self.db.session.execute(
            self.db.select(User).filter_by(user_name=user_name)
        ).scalar_one_or_none()

    def save(self, user: User) -> None:
        self.db.session.add(user)
        self.db.session.commit()
