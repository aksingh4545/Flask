from __future__ import annotations

from flask import Flask, jsonify, request, abort

app = Flask(__name__)


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id: int):
    include = request.args.get("include", "summary")
    return jsonify(item_id=item_id, include=include)


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not name:
        return jsonify(error="'name' is required"), 400
    return jsonify(id=1, name=name), 201


@app.route("/cause-404")
def cause_404():
    abort(404)


@app.errorhandler(404)
def not_found(_err):
    return jsonify(error="Not Found"), 404


if __name__ == "__main__":
    app.run(debug=True)
