from flask import Blueprint, jsonify
from src.blueprints import __bp_name__

bp = Blueprint(__bp_name__(), __name__, url_prefix="/payments")


@bp.route("/pay", methods=["GET"], strict_slashes=False)
def pay():
    """
    Under construction
    ---
    tags:
      - 503
    """
    return jsonify({"message": "This functions pay"}), 200
