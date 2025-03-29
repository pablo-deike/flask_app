from flask import Flask, render_template, request
from init_db import migrate
from container import db, verification_controller

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db.init_app(app=app)
migrate.init_app(app=app, db=db)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/verify", methods=["POST"])
def verification():
    return verification_controller.post(
        request.args.get("username"), request.args.get("password")
    )


if __name__ == "__main__":
    app.run(port=8000, debug=True)
