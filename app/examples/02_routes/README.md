# 02 - Routes

What you learn:
- HTTP methods
- URL converters
- Query params
- Error handlers

## Install

```
python -m venv .venv
.venv\Scripts\activate
pip install Flask
```

## Run

```
set FLASK_APP=app.py
flask run
```

## Try

- `GET /items/42?include=details`
- `POST /items` with JSON body
- `GET /cause-404`
