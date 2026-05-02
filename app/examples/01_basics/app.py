from __future__ import annotations

from functools import wraps
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["APP_NAME"] = "Flask Basics"


def log_call(func):
    """A tiny decorator to show how wrapping a route works."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@app.route("/")
@log_call
def index():
    """A basic handler function that returns a string."""
    return f"Welcome to {app.config['APP_NAME']}"


@app.route("/greet")
@log_call
def greet():
    """Read query parameters using request.args."""
    name = request.args.get("name", "World")
    return jsonify(message=f"Hello, {name}!")


@app.route("/sum/<int:a>/<int:b>")
@log_call
def add(a: int, b: int):
    """Route variables are parsed and passed to the function."""
    return jsonify(result=a + b)


@app.route("/headers")
def headers():
    """Inspect request headers."""
    user_agent = request.headers.get("User-Agent", "unknown")
    return jsonify(user_agent=user_agent)


if __name__ == "__main__":
    app.run(debug=True)
