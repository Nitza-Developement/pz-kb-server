from ..config import api_v3 as client


def __get(sort=None, page=None, limit=None, params=None):
    """
    Perform a GET request to the base URL with pagination parameters.

    :param sort: Sorting criteria.
    :param limit: Maximum number of records to retrieve (default: 50).
    :param page: Page number to retrieve (default: 1).
    :param params: Query params criteria.

    :return: Response from the GET request.
    """
    from src.config import __env

    PAGINATION_DEFAULT_LIMIT = __env.get("BC_PAGINATION_DEFAULT_LIMIT", 50)
    PAGINATION_DEFAULT_PAGE = __env.get("BC_PAGINATION_DEFAULT_PAGE", 1)

    limit = int(limit if limit is not None else PAGINATION_DEFAULT_LIMIT)
    page = int(page if page is not None else PAGINATION_DEFAULT_PAGE)

    query_string = "&".join(params) if params else ""
    # query_string += f"&sort={sort}" if sort else ""

    if query_string:
        query_string += f"&page={page}&limit={limit}"
        return client.get(f"/customers?{query_string}")
    else:
        return client.get("/customers", limit=limit, page=page)


def get_all(sort=None, page=None, limit=None):
    """
    Retrieve all records with pagination support.

    :param sort: Sorting criteria.
    :param page: Page number to retrieve (default: 1).
    :param limit: Maximum number of records to retrieve (default: 50).
    :return: Response from the GET request.
    """
    return __get(page=page, limit=limit, sort=sort)


def count():
    """
    Get the total number of available records.

    :return: Total number of records if available, -1 otherwise.
    """
    res = __get(page=0, limit=0)
    return res.get("meta", {}).get("pagination", {}).get("total", -1)


def get_by_id(customer_id: int):
    """
    Retrieve all records with pagination support.

    :param id: ID of the customer.
    :return: Response from the GET request.
    """
    from .customer_filter import filter

    return filter(page=1, limit=1, id_in=[customer_id])


def get_by_email(email: str):
    """
    Retrieve all records with pagination support.

    :param email: Email of the customer.
    :return: Response from the GET request.
    """
    from .customer_filter import filter

    return filter(page=1, limit=1, email_in=[email])
