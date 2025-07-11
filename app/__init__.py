from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .models import User, Feedback
    with app.app_context():
        db.create_all()

    from .routes.auth import auth_bp
    from .routes.feedback import feedback_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(feedback_bp)

    return app
