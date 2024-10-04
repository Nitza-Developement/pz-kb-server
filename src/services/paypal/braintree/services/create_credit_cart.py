import braintree
from ..config import gateway
from .get_customer import get_customer_by_email


def create_credit_cart_by_email(
    cardholder_name,
    number,
    expiration_date,
    cvv,
    customer_email,
    customer_address_id=None,
):
    """
    Creates a new credit card for a customer using their email address.

    Args:
        cardholder_name (str): The name of the cardholder.
        number (str): The credit card number.
        expiration_date (str): The expiration date of the credit card.
        cvv (str): The CVV of the credit card.
        customer_email (str): The email address of the customer.
        customer_address_id (str, optional): The billing address ID of the customer. Defaults to None.

    Returns:
        braintree.CreditCard: The newly created credit card object.
    """
    customer = get_customer_by_email(customer_email)
    customer_id = get_customer_by_email(customer_email)
    if not customer_address_id:
        customer_address_id = customer.addresses[0].id

    return create_credit_cart_by_id(
        customer_id, customer_address_id, cardholder_name, number, expiration_date, cvv
    )


def create_credit_cart_by_id(
    cardholder_name,
    number,
    expiration_date,
    cvv,
    customer_id,
    customer_address_id=None,
):
    """
    Creates a new credit card for a customer using their customer ID.

    Args:
        cardholder_name (str): The name of the cardholder.
        number (str): The credit card number.
        expiration_date (str): The expiration date of the credit card.
        cvv (str): The CVV of the credit card.
        customer_id (str): The ID of the customer.
        customer_address_id (str, optional): The billing address ID of the customer. Defaults to None.

    Returns:
        braintree.CreditCard: The newly created credit card object.
    """
    if not customer_address_id:
        customer = gateway.customer.find(customer_id)
        customer_address_id = customer.addresses[0].id

    result = gateway.credit_card.create(
        {
            "customer_id": customer_id,
            "billing_address_id": customer_address_id,
            "cardholder_name": cardholder_name,
            "expiration_date": expiration_date,
            "cvv": cvv,
            "number": number,
        }
    )

    return result.credit_card if result.credit_card else result
