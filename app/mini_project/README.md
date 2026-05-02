# Mini Project - Task Tracker (After Examples)

This mini project uses:
- Flask app factory + blueprints
- PostgreSQL (SQLAlchemy)
- Session auth (Flask-Login)
- JWT auth (PyJWT)
- RBAC decorators
- Separate frontend

If you are brand new, start with `examples/01_basics` first.

## Backend Setup

```
cd mini_project\backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Set environment variables (PowerShell):

```
$env:FLASK_ENV = "development"
$env:DATABASE_URL = "postgresql+psycopg2://USER:PASSWORD@localhost:5432/flask_learning"
$env:SECRET_KEY = "dev-secret"
$env:JWT_SECRET = "dev-jwt-secret"
```

Run:

```
set FLASK_APP=wsgi.py
flask run
```

## Frontend

Open `mini_project/frontend/index.html` in your browser and use it to login and manage tasks.

## API Endpoints (Summary)

- `POST /auth/register` (session)
- `POST /auth/login` (session)
- `POST /auth/logout` (session)
- `POST /auth/token` (JWT)
- `GET /api/tasks` (JWT)
- `POST /api/tasks` (JWT)
- `PATCH /api/tasks/<id>` (JWT + RBAC)
- `DELETE /api/tasks/<id>` (JWT + RBAC)
