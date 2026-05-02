from __future__ import annotations

from flask import jsonify, request, g

from . import api_bp
from ..extensions import db
from ..models import Task
from ..auth.services import jwt_required
from ..rbac.decorators import require_permission


@api_bp.get("/tasks")
@jwt_required
def list_tasks():
    user = g.current_user
    tasks = Task.query.filter_by(owner_id=user.id).order_by(Task.id.asc()).all()
    return jsonify([task.to_dict() for task in tasks])


@api_bp.post("/tasks")
@jwt_required
def create_task():
    user = g.current_user
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    if not title:
        return jsonify(error="title is required"), 400

    task = Task(title=title, owner_id=user.id)
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


@api_bp.patch("/tasks/<int:task_id>")
@jwt_required
@require_permission("write")
def update_task(task_id: int):
    user = g.current_user
    task = Task.query.filter_by(id=task_id, owner_id=user.id).first()
    if not task:
        return jsonify(error="task not found"), 404

    payload = request.get_json(silent=True) or {}
    if "title" in payload:
        task.title = payload["title"]
    if "completed" in payload:
        task.completed = bool(payload["completed"])

    db.session.commit()
    return jsonify(task.to_dict())


@api_bp.delete("/tasks/<int:task_id>")
@jwt_required
@require_permission("delete")
def delete_task(task_id: int):
    user = g.current_user
    task = Task.query.filter_by(id=task_id, owner_id=user.id).first()
    if not task:
        return jsonify(error="task not found"), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify(message="deleted")
