from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# Initialize extensions
# Extensions are initialized without an app while they are bound to the app later in the factory function
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app(config_class='config'):
    # Create the Flask application
    app = Flask(__name__)

    # Application configuration
    app.config.from_object(config_class)

    # Initialize Flask extensions with the app instance
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Import and register Blueprints
    from app.controllers.user_controller import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix = "/user")
    # from app.controllers.observation_controller import obs_blueprint
    # app.register_blueprint(obs_blueprint)
    
    # Create database tables for our data models
    with app.app_context():
        db.create_all()

    return app
