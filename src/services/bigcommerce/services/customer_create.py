from ..config import api_v3 as client


def create(customer_data):
    """
    Create a new customer with the provided data.

    :param data: Data for the customer to be created.
    :return: Response from the POST request.
    """
    return client.post("/customers", customer_data)
