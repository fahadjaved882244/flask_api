from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# Initialize extensions
# Extensions are initialized without an app while they are bound to the app later in the factory function
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
ma = Marshmallow()

def create_app(config_class='config'):
    # Create the Flask application
    app = Flask(__name__)

    # Application configuration
    app.config.from_object(config_class)

    # Initialize Flask extensions with the app instance
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    
    # Import and register Blueprints
    from app.controllers.user_controller import user_blueprint
    from app.controllers.observation_controller import observation_blueprint
    app.register_blueprint(user_blueprint)
    app.register_blueprint(observation_blueprint)
    
    # Create database tables for our data models
    with app.app_context():
        db.create_all()

    return app
