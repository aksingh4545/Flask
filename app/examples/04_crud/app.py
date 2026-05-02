from __future__ import annotations

import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/flask_learning",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)




with app.app_context():
    db.create_all()
    # app context = make Flask aware of the current app while running code outside a request.


@app.post("/items")
def create_item():
    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    if not name:
        return jsonify(error="name is required"), 400

    item = Item(name=name)
    db.session.add(item)
    db.session.commit()
    return jsonify(id=item.id, name=item.name), 201


@app.get("/items")
def list_items():
    items = Item.query.order_by(Item.id.asc()).all()
    return jsonify([{"id": item.id, "name": item.name} for item in items])


@app.patch("/items/<int:item_id>")
def update_item(item_id: int):
    item = Item.query.get(item_id)
    if not item:
        return jsonify(error="item not found"), 404

    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    if name:
        item.name = name
    db.session.commit()
    return jsonify(id=item.id, name=item.name)


@app.delete("/items/<int:item_id>")
def delete_item(item_id: int):
    item = Item.query.get(item_id)
    if not item:
        return jsonify(error="item not found"), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify(message="deleted")


if __name__ == "__main__":
    app.run(debug=True)
