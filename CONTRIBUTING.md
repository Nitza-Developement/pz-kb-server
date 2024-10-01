## How to Contribute

1. **Clone the Repository**: Clone the repository to your local machine using:

   ```bash
   git clone https://github.com/Nitza-Developement/pz-kb-server.git
   ```

2. **Create a Branch**: Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**: Make your changes in the appropriate files. Ensure your code follows the project's coding standards.

4. **Commit Changes**: Commit your changes with a clear and descriptive commit message:

   ```bash
   git commit -m "Add feature: your-feature-name"
   ```

5. **Push Changes**: Push your changes to the repository:

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**: Go to the repository and create a pull request from your branch. Provide a clear description of your changes and any related issues.

   NOTE: ⚠️ Please keep your branch changes up to date to avoid PR reviewers issues.

## 🌳 File Structure

```bash
├───src/
│   ├───helpers/        # Utility functions and helper methods
│   │   └─── ...
│   ├───router/         # Route definitions and handlers
│   │   └─── ...
│   ├───middleware/     # Middleware functions for request/response processing
│   │   └─── ...
│   ├───actions/        # Actions that trigger specific flows logic, e.g., pay_subscription_braintree, (main use-cases are here)
│   │   └─── ...
│   ├───services/       # Vendor logic and service layer
│   │   └───bigcommerce
│   │   └───killbill
│   │   └───paypal
│   │   └───test
│   │   └─── ...
│   │
│   ├───blueprints.py   # Blueprint definitions for modularizing routes
│   ├───config.py       # Configuration settings for the application (++env)
│   ├───setup.py        # Setup script for initializing the application
│   └───swagger.py      # Swagger documentation setup
│
├───tests/              # Test cases and testing framework folder
│   ├───router/         # Tests for route handlers
│   │   └─── ...
│   └─── ...
│
├───Dockerfile          # Instructions for building the Docker image
├───.env                # Environment variables for the **application**
└───app.py              # Main application entry point
```

- Each endpoint of the application must be placed within the router directory and follow the naming convention `__route_name__.py` or just `__route.py`.
- Additionally, each endpoint should be contained within a parent folder and include the following code snippet:

```python
# `router > parent_folder_name > endpoint_name`
from flask import Blueprint, jsonify
from src.blueprints import __bp_name__
bp = Blueprint(__bp_name__(), __name__, url_prefix="/parent_folder_name")
...
```

Furthermore, each endpoint must be isolated (**only one endpoint per file**) with the following structure

```python
...
@bp.route("/endpoint_name", methods=["METHODS_TYPE"], strict_slashes=False)
def endpoint_name():
    return jsonify({"message": "Example Response"}), 200
```

## ⚠️ Code Style

- use [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) to comply to our code formatting standard. This will make the job easier for the reviewers of pull requests; you can use `# fmt: off` and `# fmt: on` to prevent formatting the code between these two comments (not recommended)

- keep update the **requirements.txt** using `pip freeze > requirements.txt` when installing a new python package

- Write **comments** and **docstrings** to explain your code.

- Add swagger docstring for new features with the following structure:

```python
@bp.route("/hello_word", methods=["GET"], strict_slashes=False)
def hello_word():
    """
    Endpoint returning a simple Hello world JSON message.
    ---
    tags:
      - Example
    responses:
      200:
        description: A successful response
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Hello world"
    """
    return jsonify({"message": "Hello world"}), 200
```

- Ensure compliance swagger with the [OpenAPI v3 Specifications](https://swagger.io/specification/v3/).

- `TAG : 503` for minimum docstring's under constructions endpoints and a little description to explain it

- Add tests for new features in the `tests/` directory.

  - ..

- <!-- TODO -->

## Reporting Issues

If you find a bug or have a suggestion, please open an issue in the issue tracker and inform in the appropiate [zulip's channel](https://pinkzebra.zulipchat.com/). Provide as much detail as possible to help us understand and address the issue.

Thank you for your contributions!
