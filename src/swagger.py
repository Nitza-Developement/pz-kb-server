from flasgger import Swagger


def configure_swagger(app):
    """
    Configures Swagger for the given Flask app.

    Args:
        app (Flask): The Flask application instance.
    """
    swagger_ui = app.config["SWAGGER_UI"]
    host = app.config["SWAGGER_HOST"]
    base_path = app.config["SWAGGER_BASE_PATH"]
    swagger_specs_route = app.config["SWAGGER_SPECS_ROUTE"]
    swagger_endpoint = app.config["SWAGGER_ENDPOINT"]
    swagger_route = app.config["SWAGGER_ROUTE"]
    swagger_static_url_path = app.config["SWAGGER_STATIC_URL_PATH"]

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": swagger_endpoint,
                "route": swagger_route,
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": swagger_static_url_path,
        "swagger_ui": swagger_ui,
        "specs_route": swagger_specs_route,
    }

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Pink Zebra's Flasks Server Backend for (KillBill, Bigcommerce, Braintree)",
            "description": "Flask's Server Backend between (KillBill, Bigcommerce, Braintree) for the v2 of the Pink Zebra project documentation with Swagger",
            "version": "1.0.0",
        },
        "host": host,
        "basePath": base_path,
        # "schemes": [
        #     "http",
        #     "https"
        # ],
        # "securityDefinitions": {
        #     "Bearer": {
        #         "type": "apiKey",
        #         "name": "Authorization",
        #         "in": "header",
        #         "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        #     }
        # }
    }

    swagger = Swagger(app, config=swagger_config, template=swagger_template)
    return swagger
