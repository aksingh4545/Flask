from __future__ import annotations

import os
from flask import Flask, jsonify, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/flask_learning",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()


@app.post("/register")
def register():
    payload = request.get_json(silent=True) or {}
    email = payload.get("email")
    password = payload.get("password")
    if not email or not password:
        return jsonify(error="email and password are required"), 400

    user = User(email=email, password_hash=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return jsonify(id=user.id, email=user.email), 201


@app.post("/login")
def login():
    payload = request.get_json(silent=True) or {}
    email = payload.get("email")
    password = payload.get("password")
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password or ""):
        return jsonify(error="invalid credentials"), 401

    login_user(user)
    return jsonify(message="logged in")


@app.post("/logout")
@login_required
def logout():
    logout_user()
    return jsonify(message="logged out")


@app.get("/me")
@login_required
def me():
    return jsonify(message="You are authenticated via session")


if __name__ == "__main__":
    app.run(debug=True)
