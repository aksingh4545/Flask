from __future__ import annotations

from flask import jsonify

from . import main_bp


@main_bp.get("/")
def index():
    return jsonify(message="Task Tracker API")


@main_bp.get("/health")
def health():
    return jsonify(ok=True)
