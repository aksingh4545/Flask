from __future__ import annotations

from functools import wraps
from flask import jsonify, g

ROLE_PERMISSIONS = {
    "admin": {"read", "write", "delete"},
    "editor": {"read", "write"},
    "viewer": {"read"},
}


def require_permission(permission: str):
    def decorator(handler):
        @wraps(handler)
        def wrapper(*args, **kwargs):
            user = getattr(g, "current_user", None)
            if not user:
                return jsonify(error="missing user"), 401

            allowed = permission in ROLE_PERMISSIONS.get(user.role, set())
            if not allowed:
                return jsonify(error="forbidden"), 403

            return handler(*args, **kwargs)

        return wrapper

    return decorator
