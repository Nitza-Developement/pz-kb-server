from ..config import api_v2 as client
from .__get import __get_v2 as __get


def get_all(sort=None, page=None, limit=None):
    """
    Retrieve all records with pagination support.

    :param sort: Sorting criteria.
    :param page: Page number to retrieve (default: 1).
    :param limit: Maximum number of records to retrieve (default: 50).
    :return: Response from the GET request.
    """
    return __get(url="/orders", page=page, limit=limit, sort=sort)


def count_all():
    """
    Get the total number of available records.

    :return: Total number of records if available, -1 otherwise.
    """
    return __get(url="/orders/count")


def count():
    """
    Get the total number of available records.

    :return: Total number of records if available, -1 otherwise.
    """
    res = __get(url="/orders/count")
    return res.get("count", -1)


def count_statuses():
    """
    Get the total number of available records.

    :return: Total number of records separated by statuses if available, {} otherwise.
    """
    res = __get(url="/orders/count")
    return res.get("statuses", {})


def get_by_id(order_id: int):
    """
    Retrieve one order records, empty if 404 or not found.

    :param id: ID of the order.
    :return: Response from the GET request.
    """
    return __get(url=f"/orders/{order_id}")


def get_by_customer_id(customer_id: str, status_id: int = None):
    """
    Retrieve orders for a customer with a specific status.

    :param customer_id: Customer ID in the order.
    :param status_id (optional): Status ID of the order (use const of order_statuses_id.py).
    :return: Response from the GET request.
    """
    from .order_filter import filter

    if status_id:
        return filter(page=1, limit=250, customer_id=customer_id, status_id=status_id)

    return filter(page=1, limit=250, customer_id=customer_id)
