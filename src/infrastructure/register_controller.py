from flask import Request, Response, jsonify, redirect, url_for
from src.domain.user_builder import UserBuilder
from src.domain.user_repository import UserRepository


class RegisterController:

    def __init__(self, user_repository: UserRepository, user_builder: UserBuilder):
        self.__user_repository = user_repository
        self.__user_builder = user_builder

    def post(self, request: Request):
        data = request.json
        user = self.__user_builder.create_user(
            user_name=data.get("username"),
            password=data.get("password"),
            email=data.get("email"),
        )
        try:
            self.__user_repository.save(user)
            return (
                jsonify(
                    {"message": "User registered", "redirect_url": url_for("login")}
                ),
                201,
            )
        except Exception as e:
            print(str(e))
            return (
                jsonify({"error": "Invalid username or email", "message": str(e)}),
                403,
            )
