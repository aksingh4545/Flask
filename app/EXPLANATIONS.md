# Beginner Guide and Explanations

This file explains each example in simple language. Read it side-by-side with the code.

## How To Use This Guide

1) Start with `examples/01_basics` and run the app.
2) Read the notes for that example below.
3) Move to the next example only after you understand the current one.

## 1) Basics (Functions, Decorators, App Setup)

Files:
- `examples/01_basics/app.py`

What you see:
- `app = Flask(__name__)` creates the application object.
- A view function is just a normal Python function.
- `@app.route("/")` connects a URL to a function.
- A tiny decorator wraps a route so you can see how decorators work in Flask.

Why it matters:
- Flask routes are normal Python functions, which makes the framework easy to learn.

## 2) Routes

Files:
- `examples/02_routes/app.py`

What you see:
- `<int:item_id>` turns a URL segment into an integer argument.
- `methods=["GET", "POST"]` tells Flask which HTTP verbs are allowed.
- `request.args` reads query parameters.

Why it matters:
- This is how you build clean URLs and accept input from the browser.

## 3) API

Files:
- `examples/03_api/app.py`

What you see:
- `request.get_json(silent=True)` safely reads JSON.
- `jsonify(...)` returns JSON responses.
- CORS is enabled so a separate frontend can call the API.

Why it matters:
- Most modern apps use JSON APIs. This is the smallest working version.

## 4) CRUD

Files:
- `examples/04_crud/app.py`

What you see:
- A simple SQLAlchemy model.
- Create, read, update, and delete routes.

Why it matters:
- CRUD is the backbone of most real applications.

## 5) Database

Files:
- `examples/05_database/app.py`

What you see:
- A health check query and a tiny `User` table.

Why it matters:
- This is the simplest way to confirm your database works.

## 6) Session Authentication

Files:
- `examples/06_auth_sessions/app.py`

What you see:
- `Flask-Login` stores a user id in a session cookie.
- `@login_required` protects a route.

Why it matters:
- Session auth is common for classic web apps.

## 7) JWT Authentication

Files:
- `examples/07_auth_jwt/app.py`

What you see:
- A token is created on login.
- The token is sent in the `Authorization` header.

Why it matters:
- JWTs are common for mobile apps and separate frontends.

## 8) RBAC

Files:
- `examples/08_rbac/app.py`

What you see:
- Roles map to permissions like `read` or `write`.
- A decorator checks permissions before a route runs.

Why it matters:
- RBAC is how teams control who can do what.

## 9) Other

Files:
- `examples/09_other/app.py`

What you see:
- A custom CLI command and a simple config value.

Why it matters:
- CLI tools and config make real apps easier to maintain.

## Mini Project (Task Tracker)

Files:
- `mini_project/backend/app/__init__.py`
- `mini_project/backend/app/auth/routes.py`
- `mini_project/backend/app/api/routes.py`
- `mini_project/backend/app/rbac/decorators.py`
- `mini_project/backend/app/models.py`

What you see:
- App factory pattern and blueprints.
- Session login and JWT token endpoints.
- RBAC checks on update and delete.

Why it matters:
- This shows how small examples grow into a real project layout.
