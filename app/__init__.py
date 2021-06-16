from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from app.config import Config


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    app.db = db
    return app
