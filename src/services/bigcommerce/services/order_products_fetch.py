from ..config import api_v2 as client
from .__get import __get_v2 as __get


def get_all(order_id: int, sort=None, page=None, limit=None):
    """
    Retrieve all records with pagination support.

    :param id: ID of the order.
    :param sort: Sorting criteria.
    :param page: Page number to retrieve (default: 1).
    :param limit: Maximum number of records to retrieve (default: 50).
    :return: Response from the GET request.
    """
    return __get(url=f"/orders/{order_id}/products", page=page, limit=limit, sort=sort)


def get_by_id(order_id: int, product_id: int):
    """
    Retrieve one order-product records, empty if 404 or not found.

    :param order_id: ID of the product.
    :param product_id: ID of the order.
    :return: Response from the GET request.
    """
    return __get(url=f"/orders/{order_id}/products/{product_id}")
