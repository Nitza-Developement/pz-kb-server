from ..config import api_v2 as client


def filter(
    min_id: int = None,
    max_id: int = None,
    min_total: float = None,
    max_total: float = None,
    customer_id: int = None,
    email: str = None,
    status_id: int = None,
    cart_id: str = None,
    payment_method: str = None,
    min_date_created: str = None,
    max_date_created: str = None,
    min_date_modified: str = None,
    max_date_modified: str = None,
    channel_id: int = None,
    include: list = None,
    external_order_id: str = None,
    sort: str = None,
    page: int = None,
    limit: int = None,
):
    """
    Filter orders based on specific criteria.

    :param min_id: Minimum order ID.
    :param max_id: Maximum order ID.
    :param min_total: Minimum order total.
    :param max_total: Maximum order total.
    :param customer_id: Customer ID.
    :param email: Email of the customer.
    :param status_id: Status ID of the order.
    :param cart_id: Cart ID of the order.
    :param payment_method: Payment method used on the order.
    :param min_date_created: Minimum date the order was created.
    :param max_date_created: Maximum date the order was created.
    :param min_date_modified: Minimum date the order was modified.
    :param max_date_modified: Maximum date the order was modified.
    :param channel_id: Channel ID of the sales channel.
    :param include: List of sub-resources to include.
    :param external_order_id: External order ID.
    :return: Response from the custom GET filtered request.

    :param sort: Sorting criteria.
    :param page: Page number to retrieve (default: 1).
    :param limit: Number of items per page (default: 50).
    :return: Response from the custom GET filtered request.
    """
    from .__get import __get_v2 as __get

    params = []
    if min_id is not None:
        params.append(f"min_id={min_id}")
    if max_id is not None:
        params.append(f"max_id={max_id}")
    if min_total is not None:
        params.append(f"min_total={min_total}")
    if max_total is not None:
        params.append(f"max_total={max_total}")
    if customer_id is not None:
        params.append(f"customer_id={customer_id}")
    if email:
        params.append(f"email={email}")
    if status_id is not None:
        params.append(f"status_id={status_id}")
    if cart_id:
        params.append(f"cart_id={cart_id}")
    if payment_method:
        params.append(f"payment_method={payment_method}")
    if min_date_created:
        params.append(f"min_date_created={min_date_created}")
    if max_date_created:
        params.append(f"max_date_created={max_date_created}")
    if min_date_modified:
        params.append(f"min_date_modified={min_date_modified}")
    if max_date_modified:
        params.append(f"max_date_modified={max_date_modified}")
    if channel_id is not None:
        params.append(f"channel_id={channel_id}")
    if include and isinstance(include, list):
        params.append(f"include={','.join(include)}")
    if external_order_id:
        params.append(f"external_order_id={external_order_id}")
    if sort:
        params.append(f"sort={sort}")

    return __get(url="/orders", page=page, limit=limit, sort=sort, params=params)
