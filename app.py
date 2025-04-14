import os
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_login import login_required, logout_user
from init_db import db, migrate, bcrypt, login_manager
from container import auth_controller, register_controller, user_repository

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
db.init_app(app=app)
migrate.init_app(app=app, db=db)
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"


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


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=8000, debug=True)
