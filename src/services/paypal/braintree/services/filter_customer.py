import braintree
from ..config import gateway

def filter_customers(
    first_name: str = None, 
    last_name: str = None, 
    email: str = None, 
    company: str = None, 
    phone: str = None
) -> list:
    """
    Retrieves customers from the Braintree gateway based on various filters.

    Args:
        first_name (str, optional): The first name of the customer.
        last_name (str, optional): The last name of the customer.
        email (str, optional): The email address of the customer.
        company (str, optional): The company name associated with the customer.
        phone (str, optional): The phone number of the customer.

    Returns:
        list: A list containing the filtered customers.
    """
    retorno = []
    search_criteria = gateway.customer.search()

    if first_name:
        search_criteria.first_name.is_(first_name)
    if last_name:
        search_criteria.last_name.is_(last_name)
    if email:
        search_criteria.email.is_(email)
    if company:
        search_criteria.company.is_(company)
    if phone:
        search_criteria.phone.is_(phone)

    retorno = [customer for customer in search_criteria.items]
    
    return retorno