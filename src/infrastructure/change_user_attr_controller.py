from flask import Request, jsonify, session, url_for
from src.infrastructure.db_user_repository import DbUserRepository


class ChangeUserAttrController:

    def __init__(self, user_repository: DbUserRepository):
        self.__user_repository = user_repository

    def post(self, request: Request) -> dict:
        data = request.get_json()
        email = data.get("email")
        self.__user_repository.update(email)
        session["email"] = email
        return jsonify({"redirect_url": url_for("dashboard"), "email": email}), 200
