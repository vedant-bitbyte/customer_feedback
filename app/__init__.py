from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Create a single shared SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Bind the app to the db
    db.init_app(app)

    # Import models inside app context to avoid unregistered app issues
    from .models import User, Feedback
    with app.app_context():
        db.create_all()

    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.feedback import feedback_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(feedback_bp)

    return app
