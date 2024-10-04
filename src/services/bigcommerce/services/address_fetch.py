from ..config import api_v3 as client
from .__get import __get

def get_all(sort=None, page=None, limit=None):
    """
    Retrieve all records with pagination support.

    :param sort: Sorting criteria.
    :param page: Page number to retrieve (default: 1).
    :param limit: Maximum number of records to retrieve (default: 50).
    :return: Response from the GET request.
    """
    return __get(url="/customers/addresses", page=page, limit=limit, sort=sort)


def count():
    """
    Get the total number of available records.

    :return: Total number of records if available, -1 otherwise.
    """
    res = __get(url="/customers/addresses", page=0, limit=0)
    return res.get("meta", {}).get("pagination", {}).get("total", -1)


def get_by_id(address_id: int):
    """
    Retrieve one address records, empty if 404 or not found.

    :param id: ID of the address.
    :return: Response from the GET request.
    """
    from .address_filter import filter

    res = filter(page=1, limit=99999, id_in=[address_id])
    return res["data"] if res["data"] else []


def get_by_customer_id(customer_id: str):
    """
    Retrieve one address records, empty if 404 or not found.

    :param customer_id: Customer ID in the address.
    :return: Response from the GET request.
    """
    from .address_filter import filter

    res = filter(page=1, limit=99999, customer_id_in=[customer_id])
    return res["data"] if res["data"] else []