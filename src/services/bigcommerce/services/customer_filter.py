from ..config import api_v3 as client


def filter(
    store_hash: str = None,
    id_in: list = None,
    company_in: list = None,
    customer_group_id_in: list = None,
    date_created: str = None,
    date_created_min: str = None,
    date_created_max: str = None,
    date_modified: str = None,
    date_modified_min: str = None,
    date_modified_max: str = None,
    email_in: list = None,
    name_in: list = None,
    name_like: str = None,
    registration_ip_address_in: list = None,
    include: list = None,
    sort: str = None,
    page: int = None,
    limit: int = None,
):
    """
    Filter customers based on specific criteria.

    :param store_hash: Store hash to identify the store.
    :param id_in: List of customer IDs to filter by.
    :param company_in: List of companies to filter by.
    :param customer_group_id_in: List of customer group IDs to filter by.
    :param date_created: Filter by specific creation date.
    :param date_created_min: Filter by minimum creation date.
    :param date_created_max: Filter by maximum creation date.
    :param date_modified: Filter by specific modification date.
    :param date_modified_min: Filter by minimum modification date.
    :param date_modified_max: Filter by maximum modification date.
    :param email_in: List of emails to filter by.
    :param name_in: List of names to filter by (first and last name).
    :param name_like: List of name substrings to filter by (first and last name).
    :param registration_ip_address_in: List of IP addresses to filter by.
    :param include: List of sub-resources to include.

    :param sort: Sorting criteria.
    :param page: Page number to retrieve (default: 1).
    :param limit: Number of items per page (default: 50).
    :return: Response from the custom GET filtered request.
    """
    from .customer_fetch import __get

    params = []
    if id_in and isinstance(id_in, list):
        params.append(f"id:in={','.join(map(str, id_in))}")
    if company_in and isinstance(company_in, list):
        params.append(f"company:in={','.join(company_in)}")
    if customer_group_id_in and isinstance(customer_group_id_in, list):
        params.append(
            f"customer_group_id:in={','.join(map(str, customer_group_id_in))}"
        )
    if date_created:
        params.append(f"date_created={date_created}")
    if date_created_min:
        params.append(f"date_created:min={date_created_min}")
    if date_created_max:
        params.append(f"date_created:max={date_created_max}")
    if date_modified:
        params.append(f"date_modified={date_modified}")
    if date_modified_min:
        params.append(f"date_modified:min={date_modified_min}")
    if date_modified_max:
        params.append(f"date_modified:max={date_modified_max}")
    if email_in and isinstance(email_in, list):
        params.append(f"email:in={','.join(email_in)}")
    if name_in and isinstance(name_in, list):
        params.append(f"name:in={','.join(name_in)}")
    if name_like and isinstance(name_like, list):
        params.append(f"name:like={','.join(name_like)}")
    if registration_ip_address_in and isinstance(registration_ip_address_in, list):
        params.append(
            f"registration_ip_address:in={','.join(map(str, registration_ip_address_in))}"
        )
    if include and isinstance(include, list):
        params.append(f"include={','.join(include)}")
    if sort:
        params.append(f"sort={sort}")

    return __get(page=page, limit=limit, sort=sort, params=params)
