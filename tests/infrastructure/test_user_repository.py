from flask_sqlalchemy import SQLAlchemy


class TestUserRepository:

    def __init__(self, db: SQLAlchemy):
        self.db = db
