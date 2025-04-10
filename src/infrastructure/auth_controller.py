from flask import Request, Response, jsonify, url_for
from src.infrastructure.db_user_repository import DbUserRepository


class AuthController:

    def __init__(self, user_repository: DbUserRepository):
        self.__user_repository = user_repository

    def post(self, request: Request) -> Response:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        user = self.__user_repository.get_by_username(username)
        if user is None:
            return jsonify({"error": "Invalid username"}), 401
        if user.verify_password(password) is True:
            return (
                jsonify({"redirect_url": url_for("dashboard")}),
                200,
            )
        return jsonify({"error": "Invalid password"}), 401
