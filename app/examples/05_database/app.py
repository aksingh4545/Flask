from __future__ import annotations

import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/flask_learning",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)


with app.app_context():
    db.create_all()


@app.get("/db/health")
def db_health():
    # A lightweight query to confirm database connectivity.
    result = db.session.execute("SELECT 1").scalar()
    return jsonify(ok=bool(result))


@app.post("/db/users")
def create_user():
    payload = request.get_json(silent=True) or {}
    email = payload.get("email")
    if not email:
        return jsonify(error="email is required"), 400

    user = User(email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify(id=user.id, email=user.email), 201


if __name__ == "__main__":
    app.run(debug=True)
