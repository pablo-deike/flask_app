from unittest import TestCase
from flask_sqlalchemy import SQLAlchemy
from init_db import db


class TestUserRepository(TestCase):

    def setUp(self):
        self.db = db

    def save_returns_ok(self):
        pass
