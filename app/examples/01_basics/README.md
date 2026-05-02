# 01 - Basics (Functions, Decorators, App Setup)

What you learn:
- What a Flask app is
- How a route calls a Python function
- How decorators wrap a route
- How to read query parameters

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

- `GET /`
- `GET /greet?name=Ravi`
- `GET /sum/3/5`
- `GET /headers`

## What to notice

- The function name becomes the route handler.
- The decorator runs before the route function.
- `request.args` reads `?name=...` from the URL.
