from flask import Blueprint, jsonify
from src.blueprints import __bp_name__

bp = Blueprint(__bp_name__(), __name__, url_prefix="/test")


@bp.route("/kb_plugging", methods=["GET"], strict_slashes=False)
def test_plugging():
    """
    Endpoint returning a simple JSON response from the Killbill's java plugin.
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
              example: "Hello from killbill plugging"
    """
    return jsonify({"message": "Hello from killbill plugging"}), 200
