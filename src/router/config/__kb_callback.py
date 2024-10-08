from flask import Blueprint, request, jsonify
from src.blueprints import __bp_name__
from src.config import __env
from src.services.killbill.config import killbill_api, header

bp = Blueprint(__bp_name__(), __name__, url_prefix="/config")


@bp.route("/kb_callback", methods=["PUT"], strict_slashes=False)
def kb_callback():
    """
    Endpoint to config Killbill callback notifications.
    ---
    description: This endpoint refresh notifications subscription to Killbill.
    parameters:
      - name: cb
        in: body
        type: string
        required: false
        description: The callback URL for Killbill notifications. If not provided, the default URL will be used.
    tags:
      - Config
    responses:
      200:
        description: Successful operation
    """
    default_CALLBACK = f"{__env['SERVER']}/listeners/kb_callback"
    CALLBACK_URL = request.json.get("cb", default_CALLBACK)

    # Delete existing notifications subscription
    killbill_api.tenant.delete_push_notification(header=header)

    # Add new notifications subscription
    killbill_api.tenant.create_push_notification(header=header, callback_url=CALLBACK_URL)

    # Check notifications subscription
    response = killbill_api.tenant.retrieve_push_notifications(header=header)
    return jsonify(), 200
