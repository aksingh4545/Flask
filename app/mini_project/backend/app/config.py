from __future__ import annotations

import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    JWT_SECRET = os.getenv("JWT_SECRET", "dev-jwt-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:postgres@localhost:5432/flask_learning",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
