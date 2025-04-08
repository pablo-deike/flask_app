from flask import Flask, render_template, request
from init_db import db, migrate, bcrypt
from container import auth_controller, register_controller

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db.init_app(app=app)
migrate.init_app(app=app, db=db)
bcrypt.init_app(app)


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
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
