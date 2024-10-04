from ..config import api_v3 as client


def filter(
    id_in: list = None,
    customer_id_in: list = None,
    company_in: list = None,
    name_in: list = None,
    include: list = None,
    
    sort: str = None,
    page: int = None,
    limit: int = None,
):
    """
    Filter customers based on specific criteria.

    :param id_in: List of address IDs to filter by.
    :param customer_id_in: List of customer IDs to filter by.
    :param company_in: List of companies to filter by.
    :param name_in: List of names to filter by (first and last name).
    :param include: List of sub-resources to include.

    :param sort: Sorting criteria.
    :param page: Page number to retrieve (default: 1).
    :param limit: Number of items per page (default: 50).
    :return: Response from the custom GET filtered request.
    """
    from .__get import __get

    params = []
    if id_in and isinstance(id_in, list):
        params.append(f"id:in={','.join(map(str, id_in))}")
    if customer_id_in and isinstance(customer_id_in, list):
        params.append(f"customer_id:in={','.join(map(str, customer_id_in))}")
    if company_in and isinstance(company_in, list):
        params.append(f"company:in={','.join(company_in)}")
    if name_in and isinstance(name_in, list):
        params.append(f"name:in={','.join(name_in)}")
    if include and isinstance(include, list):
        params.append(f"include={','.join(include)}")
    if sort:
        params.append(f"sort={sort}")

    return __get(url="/customers/addresses", page=page, limit=limit, sort=sort, params=params)
