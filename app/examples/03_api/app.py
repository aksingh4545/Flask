from __future__ import annotations

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

NOTES = [
    {"id": 1, "title": "Learn Flask"},
    {"id": 2, "title": "Build an API"},
]


@app.get("/api/notes")
def list_notes():
    return jsonify(NOTES)


@app.post("/api/notes")
def create_note():
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    if not title:
        return jsonify(error="title is required"), 400

    new_note = {"id": len(NOTES) + 1, "title": title}
    NOTES.append(new_note)
    return jsonify(new_note), 201


if __name__ == "__main__":
    app.run(debug=True)
