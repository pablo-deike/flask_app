from flask_login import UserMixin
from init_db import db, bcrypt


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def verify_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password, password)
