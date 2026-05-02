# Detailed Explanations

This guide explains the code in each example and the mini project. Use it alongside the source files.

## 1) Basics (Functions, Decorators, App Setup)

Files:
- `examples/01_basics/app.py`

Key ideas:
- `app = Flask(__name__)` creates the WSGI app instance.
- A **view function** is just a Python function attached to a route.
- `@app.route("/path")` maps URL -> function.
- The custom `timing_decorator` uses `functools.wraps` so Flask keeps the original function name. This matters for debugging and for internal routing.
- Responses can be a `str`, a `dict` wrapped by `jsonify`, or a `Response` object. The decorator normalizes responses so it can attach headers consistently.

## 2) Routes

Files:
- `examples/02_routes/app.py`

Key ideas:
- Route parameters like `<int:item_id>` are automatically converted to Python types.
- `methods=["GET", "POST"]` limits which HTTP methods a handler accepts.
- `request.args` reads query parameters like `?include=details`.
- `@app.errorhandler(404)` overrides Flask's default 404 response and returns JSON instead of HTML.

## 3) API

Files:
- `examples/03_api/app.py`

Key ideas:
- `request.get_json(silent=True)` reads JSON safely and avoids exceptions.
- The endpoint returns JSON and a status code `(data, 201)` for created resources.
- `Flask-Cors` enables browser-based frontends to call the API from another origin.

## 4) CRUD

Files:
- `examples/04_crud/app.py`

Key ideas:
- `Flask-SQLAlchemy` provides `db.Model` as a base class for ORM models.
- `db.session.add(...)` queues an insert; `db.session.commit()` persists it.
- `GET /items` lists rows and formats them as JSON.
- `PATCH /items/<id>` updates only the fields provided.
- `DELETE /items/<id>` removes the row.

## 5) Database

Files:
- `examples/05_database/app.py`

Key ideas:
- `db.session.execute("SELECT 1")` is a lightweight health check.
- A tiny `User` model shows how you define columns, types, and constraints.

## 6) Session Authentication

Files:
- `examples/06_auth_sessions/app.py`

Key ideas:
- `Flask-Login` stores a user id in the session cookie.
- `login_user(user)` marks the user as authenticated for future requests.
- `@login_required` guards endpoints that should only be accessed when logged in.
- Passwords are stored as secure hashes (never plain text).

## 7) JWT Authentication

Files:
- `examples/07_auth_jwt/app.py`

Key ideas:
- JWTs are signed tokens that contain a subject (`sub`) and expiration (`exp`).
- A `Bearer <token>` header is required for protected routes.
- The decorator verifies the token and rejects expired or invalid tokens.

## 8) RBAC

Files:
- `examples/08_rbac/app.py`

Key ideas:
- RBAC is enforced using a decorator that checks the caller role.
- A role maps to a set of permissions like `read`, `write`, `delete`.
- If a permission is missing, a `403` response is returned.

## 9) Other

Files:
- `examples/09_other/app.py`

Key ideas:
- `@app.cli.command` adds custom CLI commands to your Flask app.
- Configuration via environment variables keeps secrets out of the code.

## Mini Project (Task Tracker)

Files:
- `mini_project/backend/app/__init__.py`
- `mini_project/backend/app/auth/routes.py`
- `mini_project/backend/app/api/routes.py`
- `mini_project/backend/app/rbac/decorators.py`
- `mini_project/backend/app/models.py`

Key ideas:
- **App factory pattern**: `create_app()` builds the app with config, extensions, and blueprints.
- **Blueprints**: `auth`, `api`, and `main` split routes into modules.
- **Session auth**: `POST /auth/login` stores the session cookie.
- **JWT auth**: `POST /auth/token` returns a signed token.
- **RBAC**: `require_permission` uses the user role to allow or block updates and deletes.
- **Tasks API**: authenticated users can create and view their own tasks.

Frontend:
- `mini_project/frontend/index.html` + `app.js` show a simple login + task manager UI.
- The frontend stores the JWT in memory and uses it for API calls.
