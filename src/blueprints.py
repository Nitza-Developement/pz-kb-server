import importlib.util
import os, uuid


def register_blueprints(app):
    """
    Register all blueprints found in routes.py files within the router directory.

    Args:
        app (Flask): The Flask application instance.
    """
    for module_path in __find_routes_files(app):
        module_name = module_path.replace(os.sep, ".").replace(".py", "")
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        app.register_blueprint(module.bp)


def __find_routes_files(app):
    """
    Generator function to find all routes.py files within the router directory.

    Args:
        app (Flask): The Flask application instance.

    Yields:
        str: The path to a routes.py file.
    """
    router_dir = app.config["ROUTER_DIR"]
    routes_files = app.config["ROUTES_FILES"]
    routes_files_between = app.config["ROUTES_FILES_BETWEEN"]
    routes_files_ignore = app.config["ROUTES_FILES_IGNORE"]

    for root, _, files in os.walk(os.path.join(os.path.dirname(__file__), router_dir)):
        for file in files:
            if file in routes_files_ignore:
                continue
            if file in routes_files or any(
                file.startswith(prefix) and file.endswith(suffix)
                for prefix, suffix in routes_files_between
            ):
                yield os.path.join(root, file)


def __bp_name__():
    """
    Generates a unique name using a UUID.

    This function generates a unique identifier by creating a UUID and
    returning the first 12 characters of its hexadecimal representation.

    Returns:
        str: A unique 12-character string.
    """
    return uuid.uuid4().hex[:12]
