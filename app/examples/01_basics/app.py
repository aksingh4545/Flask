from __future__ import annotations

from functools import wraps
from time import perf_counter
from flask import Flask, jsonify, request, Response

app = Flask(__name__)
app.config["APP_NAME"] = "Flask Basics"


def timing_decorator(func):
    """Measure how long a request handler takes and return time in a header."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        response = func(*args, **kwargs)
        elapsed_ms = (perf_counter() - start) * 1000

        # Ensure we always have a Response object to attach headers.
        if isinstance(response, Response):
            response.headers["X-Elapsed-ms"] = f"{elapsed_ms:.2f}"
            return response

        flask_response = app.make_response(response)
        flask_response.headers["X-Elapsed-ms"] = f"{elapsed_ms:.2f}"
        return flask_response

    return wrapper


@app.route("/")
@timing_decorator
def index():
    """A basic handler function that returns a string."""
    return f"Welcome to {app.config['APP_NAME']}"


@app.route("/greet")
@timing_decorator
def greet():
    """Read query parameters using request.args."""
    name = request.args.get("name", "World")
    return jsonify(message=f"Hello, {name}!")


@app.route("/sum/<int:a>/<int:b>")
@timing_decorator
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
