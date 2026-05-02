from __future__ import annotations

from datetime import datetime, timedelta, timezone
from functools import wraps
import jwt
from flask import current_app, jsonify, request, g
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password: str) -> str:
    return generate_password_hash(password)


def verify_password(password_hash: str, password: str) -> bool:
    return check_password_hash(password_hash, password)


def create_jwt(email: str) -> str:
    payload = {
        "sub": email,
        "exp": datetime.now(timezone.utc) + timedelta(hours=2),
        "iat": datetime.now(timezone.utc),
    }
    return jwt.encode(payload, current_app.config["JWT_SECRET"], algorithm="HS256")


def jwt_required(handler):
    @wraps(handler)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify(error="missing token"), 401

        token = auth_header.replace("Bearer ", "", 1)
        try:
            payload = jwt.decode(
                token, current_app.config["JWT_SECRET"], algorithms=["HS256"]
            )
        except jwt.PyJWTError:
            return jsonify(error="invalid or expired token"), 401

        email = payload.get("sub")
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify(error="user not found"), 404

        g.jwt_email = email
        g.current_user = user
        return handler(*args, **kwargs)

    return wrapper
