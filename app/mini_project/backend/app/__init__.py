from __future__ import annotations

from flask import Flask
from flask_cors import CORS

from .config import Config
from .extensions import db, login_manager
from .errors.handlers import register_error_handlers
from .auth.routes import auth_bp
from .api.routes import api_bp
from .main.routes import main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config())

    CORS(app, supports_credentials=True)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(api_bp, url_prefix="/api")

    register_error_handlers(app)

    return app
