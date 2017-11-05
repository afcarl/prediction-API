from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    from services.model_server.views import users_blueprint
    app.register_blueprint(users_blueprint)

    return app