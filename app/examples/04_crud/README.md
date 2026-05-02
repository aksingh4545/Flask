# 04 - CRUD with PostgreSQL

What you learn:
- SQLAlchemy models
- Create, read, update, delete
- Basic error handling

## Install

```
pip install Flask Flask-SQLAlchemy psycopg2-binary
```

## Configure

Set `DATABASE_URL`:

```
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@localhost:5432/flask_learning
```

## Run

```
set FLASK_APP=app.py
flask run
```

## Try

- `POST /items` with JSON `{ "name": "Pen" }`
- `GET /items`
- `PATCH /items/1` with JSON `{ "name": "Pencil" }`
- `DELETE /items/1`
