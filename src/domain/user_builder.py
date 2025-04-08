from src.domain.user import User
from init_db import bcrypt


class UserBuilder:

    def create_user(self, user_name: str, email: str, password: str) -> User:
        pswhash = bcrypt.generate_password_hash(password)
        return User(user_name=user_name, email=email, password=pswhash)
