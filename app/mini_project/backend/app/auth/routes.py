from __future__ import annotations

from flask import jsonify, request
from flask_login import login_user, logout_user

from . import auth_bp
from ..extensions import db, login_manager
from ..models import User
from .services import hash_password, verify_password, create_jwt


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))


@auth_bp.post("/register")
def register():
    payload = request.get_json(silent=True) or {}
    email = payload.get("email")
    password = payload.get("password")
    role = payload.get("role", "viewer")
    if not email or not password:
        return jsonify(error="email and password are required"), 400

    existing = User.query.filter_by(email=email).first()
    if existing:
        return jsonify(error="email already registered"), 409

    user = User(email=email, password_hash=hash_password(password), role=role)
    db.session.add(user)
    db.session.commit()
    return jsonify(id=user.id, email=user.email, role=user.role), 201


@auth_bp.post("/login")
def login():
    payload = request.get_json(silent=True) or {}
    email = payload.get("email")
    password = payload.get("password")
    user = User.query.filter_by(email=email).first()
    if not user or not verify_password(user.password_hash, password or ""):
        return jsonify(error="invalid credentials"), 401

    login_user(user)
    return jsonify(message="logged in via session")


@auth_bp.post("/logout")
def logout():
    logout_user()
    return jsonify(message="logged out")


@auth_bp.post("/token")
def token():
    payload = request.get_json(silent=True) or {}
    email = payload.get("email")
    password = payload.get("password")
    user = User.query.filter_by(email=email).first()
    if not user or not verify_password(user.password_hash, password or ""):
        return jsonify(error="invalid credentials"), 401

    return jsonify(token=create_jwt(user.email))
