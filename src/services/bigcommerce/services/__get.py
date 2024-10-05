from ..config import api_v3, api_v2


def __get_v2(url="", sort=None, page=None, limit=None, params=None):
    return __get(
        client=api_v2,
        url=url,
        sort=sort,
        page=page,
        limit=limit,
        params=params,
    )


def __get_v3(url="", sort=None, page=None, limit=None, params=None):
    return __get(
        client=api_v3,
        url=url,
        sort=sort,
        page=page,
        limit=limit,
        params=params,
    )


def __get(client, url="", sort=None, page=None, limit=None, params=None):
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
        return client.get(f"{url}?{query_string}")
    else:
        return client.get(url, limit=limit, page=page)
