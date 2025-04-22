from flask import Request, Response, jsonify, session, url_for
from flask_login import login_user
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
            login_user(user)
            session["email"] = user.email
            session["userid"] = user.id
            return (
                jsonify({"redirect_url": url_for("dashboard")}),
                200,
            )
        return jsonify({"error": "Invalid password"}), 401
