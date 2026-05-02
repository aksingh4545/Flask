from __future__ import annotations

from functools import wraps
from flask import Flask, jsonify, request

app = Flask(__name__)

ROLE_PERMISSIONS = {
    "admin": {"read", "write", "delete"},
    "editor": {"read", "write"},
    "viewer": {"read"},
}


def require_permission(permission: str):
    def decorator(handler):
        @wraps(handler)
        def wrapper(*args, **kwargs):
            role = request.headers.get("X-Role", "viewer")
            allowed = permission in ROLE_PERMISSIONS.get(role, set())
            if not allowed:
                return jsonify(error="forbidden"), 403
            return handler(*args, **kwargs)

        return wrapper

    return decorator


@app.get("/report")
@require_permission("read")
def view_report():
    return jsonify(message="report data")


@app.post("/report")
@require_permission("write")
def edit_report():
    return jsonify(message="report updated")


@app.delete("/report")
@require_permission("delete")
def delete_report():
    return jsonify(message="report deleted")


if __name__ == "__main__":
    app.run(debug=True)
