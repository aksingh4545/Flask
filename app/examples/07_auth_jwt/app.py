from __future__ import annotations

from datetime import datetime, timedelta, timezone
from functools import wraps
import jwt
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["JWT_SECRET"] = "dev-jwt-secret"

USERS = {"admin@example.com": "password"}


def create_token(email: str) -> str:
    payload = {
        "sub": email,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
        "iat": datetime.now(timezone.utc),
    }
    return jwt.encode(payload, app.config["JWT_SECRET"], algorithm="HS256")


def jwt_required(handler):

    # Decorator = function that wraps another function
# wrapper = the new function that runs instead
# *args, **kwargs = allows wrapper to work with ANY function


# @my_decorator
# def say_hello(): 
# say_hello = my_decorator(say_hello)

    @wraps(handler)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify(error="missing token"), 401

        token = auth_header.replace("Bearer ", "", 1)
        try:
            payload = jwt.decode(token, app.config["JWT_SECRET"], algorithms=["HS256"])
        except jwt.PyJWTError:
            return jsonify(error="invalid or expired token"), 401

        request.jwt_subject = payload.get("sub")
        return handler(*args, **kwargs)

    return wrapper


@app.post("/login")
def login():
    payload = request.get_json(silent=True) or {}
    email = payload.get("email")
    password = payload.get("password")
    if USERS.get(email) != password:
        return jsonify(error="invalid credentials"), 401
    return jsonify(token=create_token(email))


@app.get("/protected")
@jwt_required
def protected():
    return jsonify(message=f"Hello {request.jwt_subject}")


if __name__ == "__main__":
    app.run(debug=True)
