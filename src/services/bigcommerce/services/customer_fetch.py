from ..config import api_v3 as client
from .__get import  __get_v3 as __get

def get_all(sort=None, page=None, limit=None):
    """
    Retrieve all records with pagination support.

    :param sort: Sorting criteria.
    :param page: Page number to retrieve (default: 1).
    :param limit: Maximum number of records to retrieve (default: 50).
    :return: Response from the GET request.
    """
    return __get(url="/customers", page=page, limit=limit, sort=sort)


def count():
    """
    Get the total number of available records.

    :return: Total number of records if available, -1 otherwise.
    """
    res = __get(url="/customers", page=0, limit=0)
    return res.get("meta", {}).get("pagination", {}).get("total", -1)


def get_by_id(customer_id: int):
    """
    Retrieve one customer records, empty if 404 or not found.

    :param id: ID of the customer.
    :return: Response from the GET request.
    """
    from .customer_filter import filter

    res = filter(page=1, limit=1, id_in=[customer_id])
    return res["data"][0] if res["data"] else {}


def get_by_email(email: str):
    """
    Retrieve one customer records, empty if 404 or not found.

    :param email: Email of the customer.
    :return: Response from the GET request.
    """
    from .customer_filter import filter

    res = filter(page=1, limit=1, email_in=[email])
    return res["data"][0] if res["data"] else {}