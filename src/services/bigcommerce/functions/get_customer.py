def __get_ids_from_customer_response(response: dict, force_first=False):
    """
    Get the id of a customer based on the response.

    This function attempts to retrieve the customer id from the given response dictionary.
    - It first checks if the 'id' key is present at the top level of the response.
    - If not found, it looks for the 'data' key. If 'data' is a list, it returns the ids of the elements in the list.
    - If 'force_first' is True, it returns the id of the first element in the list.
    - If 'data' is not a list, it attempts to retrieve the id from the 'data' dictionary.

    :param response: A dictionary containing the response data.
    :param force_first: A boolean flag to force returning the first id in the list if 'data' is a list.
    :return: Customer id if available, None otherwise.
    """
    customer_id = response.get("id", None)
    if customer_id:
        return customer_id

    data = response.get("data", {})
    if isinstance(data, list):
        if force_first and len(data) > 0:
            return data[0].get("id", None)
        return [item.get("id", None) for item in data]

    else:
        return data.get("id", None)
