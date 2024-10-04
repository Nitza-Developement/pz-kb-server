import braintree
from ..config import gateway

def get_customer_by_email(email) -> object:
    """
    Retrieves a single customer from the Braintree gateway by their email address.

    Args:
        email (str): The email address to search for the customer.

    Returns:
        object: A customer details object.
    """
    response = gateway.customer.search(
            braintree.CustomerSearch.email == email
        )
    retorno = next(response.items, None)
    
    return retorno


