from ..config import api_v3 as client


def update(customer_data):
    """
    Update an existing customer with the provided data.

    :param data: Data for the customer to be updated.
    :return: Response from the PUT request.
    """
    return client.put("/customers", customer_data)
