from typing import Optional
from flask_sqlalchemy import SQLAlchemy

from src.domain.user import User
from src.domain.user_repository import UserRepository


class DbUserRepository(UserRepository):

    def __init__(self, db_instance: SQLAlchemy):
        self.db = db_instance

    def get_by_username(self, username: str) -> Optional[User]:
        return self.db.session.execute(
            self.db.select(User).filter_by(username=username)
        ).scalar_one()
