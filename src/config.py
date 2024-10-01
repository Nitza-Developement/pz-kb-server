# fmt: off
import os
from collections import UserDict
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()

class EnvDict(UserDict):
    """
    EnvConfig allowing easy access to configuration variables using dictionary-like syntax.

    It returns the value of a config variable if it exists, and returns None
    if the variable is not defined in the Flask config.

    Usage:
        __env["EXISTING_KEY"]  # Returns the value of the config key
        __env["NON_EXISTING_KEY"]  # Returns None if the key doesn't exist
    """
    def __getitem__(self, key):
        return self.data.get(key, None)

# Instance of EnvConfig for direct use
__env = EnvDict({
    # APP
    "DEBUG" : os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1"),
    "HOST" : os.getenv("FLASK_HOST", "0.0.0.0"),
    "PORT" : os.getenv("FLASK_PORT", "5000"),
    "SERVER" : f"{os.getenv('FLASK_HOST', '0.0.0.0')}:{os.getenv('FLASK_PORT', '5000')}",
    "SECRET_KEY" : os.getenv("SECRET_KEY"),
    "ENV" : os.getenv("FLASK_ENV", "development"),

    "CORS_ORIGINS": "*",
    "CORS_ALLOW_HEADERS": ["Authorization", "Content-Type"],
    "CORS_EXPOSE_HEADERS": ["Authorization"],
    "CORS_SUPPORTS_CREDENTIALS": True,
    "CORS_METHODS": ["GET", "POST", "OPTIONS"],


    # ROUTER
    "ROUTER_DIR" : "router",
    "ROUTES_FILES" : [
        "routes.py",
        "route.py",
        "urls.py",
        "url.py",
    ],
    "ROUTES_FILES_BETWEEN" : [
        ("__", ".py"),
    ],
    "ROUTES_FILES_IGNORE" : [
        "__init__.py",
    ],

    # SWAGGER
    "SWAGGER_UI" : os.getenv("SWAGGER_UI", "True").lower() in ("true", "1"),
    "SWAGGER_HOST" : os.getenv("SWAGGER_HOST", "localhost:5000"),
    "SWAGGER_BASE_PATH" : "/",
    "SWAGGER_SPECS_ROUTE" : "/apidocs/",
    "SWAGGER_ENDPOINT" : "apispec",
    "SWAGGER_ROUTE" : "/apispec.json",
    "SWAGGER_STATIC_URL_PATH" : "/flasgger_static",

    # KILLBILL
    "KB_TENANT" : os.getenv("KB_TENANT"),
    "KB_USERNAME" : os.getenv("KB_USERNAME"),
    "KB_PASSWORD" : os.getenv("KB_PASSWORD"),
    "KB_API_URL" : os.getenv("KB_API_URL", "localhost:8080"),
    "KB_TIMEOUT" : 30,
    "KB_API_KEY" : os.getenv("KB_API_KEY"),
    "KB_API_SECRET" : os.getenv("KB_API_SECRET"),

    # BIGCOMMERCE
    "BC_PAGINATION_DEFAULT_LIMIT" : 50,
    "BC_PAGINATION_DEFAULT_PAGE" : 1,

    "BC_BASE_URL_BASIC" : "https://api.bigcommerce.com",
    "BC_BASE_URL_PAYMENT" : "https://payments.bigcommerce.com",

    "BC_USERNAME" : os.getenv("BC_USERNAME"),
    "BC_STORE_HASH" : os.getenv("BC_STORE_HASH"),
    "BC_ACCESS_TOKEN" : os.getenv("BC_ACCESS_TOKEN"),
    "BC_API_TOKEN" : os.getenv("BC_ACCESS_TOKEN"),

    "BC_AUTH_URL_BASIC": f"{os.getenv('BC_BASE_URL_BASIC')}stores/{os.getenv('BC_STORE_HASH')}",
    "BC_AUTH_URL_PAYMENT": f"{os.getenv('BC_BASE_URL_PAYMENT')}stores/{os.getenv('BC_STORE_HASH')}",

    "BC_APP_CLIENT_ID" : os.getenv("BC_APP_CLIENT_ID"),
    "BC_APP_CLIENT_SECRET" : os.getenv("BC_APP_CLIENT_SECRET"),

    "BC_CONSULTANT_GROUP_ID" : 0,  # TODO definir los ids para cada tipo (único campo encontrado para separar las clases)
    "BC_CUSTOMER_GROUP_ID" : 0,  # TODO definir los ids para cada tipo (único campo encontrado para separar las clases)

    # BRAINTREE
    "PP_BT_ENVIRONMENT" : os.getenv("PP_BT_ENVIRONMENT"),
    "PP_BT_MERCHANT_ID" : os.getenv("PP_BT_MERCHANT_ID"),
    "PP_BT_PUBLIC_KEY" : os.getenv("PP_BT_PUBLIC_KEY"),
    "PP_BT_PRIVATE_KEY" : os.getenv("PP_BT_PRIVATE_KEY"),
})


def configure_cors(app):
    """
    Ensure all responses have the CORS headers. This ensures any failures are also accessible by the client.

    Args:
        app (Flask): The Flask application instance.
    """
    CORS(app, resources={r"/*": {
        "origins": __env["CORS_ORIGINS"],
        "allow_headers": __env["CORS_ALLOW_HEADERS"],
        "expose_headers": __env["CORS_EXPOSE_HEADERS"],
        "supports_credentials": __env["CORS_SUPPORTS_CREDENTIALS"],
        "methods": __env["CORS_METHODS"],
    }})

def configure_app(app):
    """
    Configures the Flask application with environment variables.

    Args:
        app (Flask): The Flask application instance.

    """
    for key, value in __env.items():
        app.config[key] = value
