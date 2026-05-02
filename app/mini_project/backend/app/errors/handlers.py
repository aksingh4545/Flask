from __future__ import annotations

from flask import Flask, jsonify


def register_error_handlers(app: Flask) -> None:
    @app.errorhandler(404)
    def not_found(_err):
        return jsonify(error="not found"), 404

    @app.errorhandler(500)
    def server_error(_err):
        return jsonify(error="server error"), 500
