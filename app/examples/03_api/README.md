# 03 - API Basics

What you learn:
- JSON requests and responses
- Status codes
- Minimal validation
- In-memory storage for learning

## Install

```
pip install Flask Flask-Cors
```

## Run

```
set FLASK_APP=app.py
flask run
```

## Try

- `GET /api/notes`
- `POST /api/notes` with JSON: `{ "title": "First" }`
