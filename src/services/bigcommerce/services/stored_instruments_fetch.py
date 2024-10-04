from ..config import api_v3 as client
from .__get import __get


def get_stored_instruments(customerId : int) -> list:
    """
    Fetch all customer stored instruments.

    :param id: ID of the customer.
    :return: Response from the GET request.
    """
    return __get(url=f"customers/{customerId}/stored-instruments")

def get_default_stored_instruments(customerId : int) -> dict:
    """
    Fetch default customer stored instrument.

    :param id: ID of the customer.
    :return: Response modified data from the GET request.
    """
    response = get_stored_instruments(customerId)
    if not response or not response[0]:
        return {}

    retorno = response[0]
    for res in response:
        if res.get("is_default"):
            retorno = res
            break
            
    return retorno

def get_addresses(customerId : int) -> list:
    """
    Fetch all customer addresses.

    :param id: ID of the customer.
    :return: Response modified data from the GET request.
    """
    response = get_stored_instruments(customerId)
    if not response:
        return {}

    retorno = []
    for res in response:
        if res.get("billing_address"):
            retorno += [res.get("billing_address")]
            
    return retorno

def get_default_address(customerId : int) -> dict:
    """
    Fetch default customer address.

    :param id: ID of the customer.
    :return: Response modified data from the GET request.
    """
    response = get_default_stored_instruments(customerId)
    if not response or not isinstance(response, dict) or not response.get("billing_address"):
        return {}

    retorno = response.get("billing_address")
    return retorno