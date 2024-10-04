import braintree
from ..config import gateway

def get_all_customers() -> list:
    """
    Retrieves all customers from the Braintree gateway.

    Returns:
        list: A list with customer details.
    """
    retorno = []
    
    response = gateway.customer.all()
    retorno = [customer for customer in response.items]
        
    return retorno

def get_customers_by_email(email : str) -> list:
    """
    Retrieves a list of customers from the Braintree gateway by their email address.

    Args:
        email (str): The email address to search for customers.

    Returns:
        list: A list containing the matched customers.
    """
    retorno = []

    response = gateway.customer.search(
        braintree.CustomerSearch.email == email
    )
    retorno = [customer for customer in response.items]

    return retorno