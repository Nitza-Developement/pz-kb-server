from flask import Blueprint, request, jsonify
from src.blueprints import __bp_name__
# import modules, actions, services here ...

bp = Blueprint(__bp_name__(), __name__, url_prefix="/test")


@bp.route("/self", methods=["GET"], strict_slashes=False)
def test_self():
    """
    Endpoint returning a simple JSON response from this Flask's server.
    ---
    tags:
      - Test
    responses:
      200:
        description: A successful response
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Hello from this server"
    """
    # test your function here ...
    return jsonify({"message": "Hello from this server"}), 200