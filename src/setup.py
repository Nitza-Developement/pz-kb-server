from flask import Flask
from src.config import configure_app, configure_cors
from src.blueprints import register_blueprints
from src.swagger import configure_swagger


def create_app():
    """
    Creates and configures a new instance of the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)

    # Configure the app
    configure_app(app)
    
    # Configure the CORS
    configure_cors(app)

    # Register Blueprints
    register_blueprints(app)

    # Configure the swagger
    configure_swagger(app)

    return app
