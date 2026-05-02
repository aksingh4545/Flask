from __future__ import annotations

import os
from flask import Flask, jsonify

app = Flask(__name__)
app.config["APP_MODE"] = os.getenv("APP_MODE", "development")


@app.cli.command("say-hello")
def say_hello():
    print("Hello from Flask CLI")


@app.get("/status")
def status():
    return jsonify(mode=app.config["APP_MODE"], ok=True)


@app.errorhandler(500)
def handle_server_error(_err):
    return jsonify(error="server error"), 500


if __name__ == "__main__":
    app.run(debug=True)
