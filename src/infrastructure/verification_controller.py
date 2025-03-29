from flask import jsonify
from src.infrastructure.db_user_repository import DbUserRepository


class VerificationController:

    def __init__(self, user_repository: DbUserRepository):
        self.user_repository = user_repository

    def post(self, username: str, password: str):
        user = self.user_repository.get_by_username(username)
        if user is None:
            return jsonify({"error": "Invalid username or password"}), 401
        if user.verify_password(password) is True:
            return (
                jsonify({"message": "Login successful", "token": "fake-jwt-token"}),
                200,
            )
        return jsonify({"error": "Invalid username or password"}), 401
