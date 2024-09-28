from flask import Blueprint, jsonify
from src.blueprints import __bp_name__

from src.services.bigcommerce.services.customer_filter import filter as filter_customer

# from src.services.bigcommerce.functions.get_customer import (
#     __get_id_from_customer_response,
# )


bp = Blueprint(__bp_name__(), __name__, url_prefix="/test")


@bp.route("/bc", methods=["GET"], strict_slashes=False)
def test_plugging():
    """
    Endpoint making a simple request to the Bigcommerce's store.
    ---
    tags:
      - Test
    responses:
      200:
        description: A successful response
    """
    a = filter_customer(
        id_in=[215104],
        # company_in=["MiraCommerce"],
        # email_in=["alejandro.stivanello@miracommerce.com", "customer2@example.com"],
    )
    # b = __get_id_from_customer_response(a)
    return jsonify(a), 200
