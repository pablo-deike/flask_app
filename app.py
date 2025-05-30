import os
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from flask_login import login_required, logout_user
from init_db import db, migrate, bcrypt, login_manager
from container import (
    auth_controller,
    register_controller,
    user_repository,
    change_user_attr_controller,
)

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
db.init_app(app=app)
migrate.init_app(app=app, db=db)
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"


def create_app(config=None):
    load_dotenv()
    app = Flask(__name__)

    if config is not None:
        app.config.update(config)
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DEV_DATABASE_URL")
        app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    register_routes(app)
    return app


def register_routes(app):
    @app.route("/", methods=["GET"])
    def home():
        return render_template("home.html")

    @app.route("/login", methods=["GET"])
    def login():
        return render_template("login.html")

    @app.route("/register", methods=["GET"])
    def register_get():
        return render_template("register.html")

    @app.route("/register/save", methods=["POST"])
    def register_post():
        return register_controller.post(request)

    @app.route("/auth", methods=["POST"])
    def verification():
        return auth_controller.post(request)

    @app.route("/dashboard", methods=["GET"])
    @login_required
    def dashboard():
        return render_template("dashboard.html")

    @login_manager.user_loader
    def load_user(userid):
        return user_repository.get_by_id(int(userid))

    @app.route("/change_user_attr", methods=["POST"])
    @login_required
    def change_user_attr():
        return change_user_attr_controller.post(request)

    @app.route("/logout", methods=["GET"])
    @login_required
    def logout():
        logout_user()
        session.pop("email", None)
        return redirect(url_for("home"))


if __name__ == "__main__":
    app = create_app()
    app.run(port=8000, debug=True)
