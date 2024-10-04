import braintree
from ..config import gateway
from .create_billing_address import create_billing_address_by_id
from .create_credit_cart import create_credit_cart_by_id
from src.helpers.country_converter import country_converter, country_arg_type


def create_customer(
    first_name,
    last_name,
    email,
    phone=None,
    company=None,
    website=None,
    fax=None,
    street_address=None,
    extended_address=None,
    locality=None,
    region=None,
    postal_code=None,
    country=None,
    cardholder_name=None,
    number=None,
    expiration_date=None,
    cvv=None,
):
    """
    Creates a new customer in Braintree with an optional billing address and credit card.

    Args:
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        email (str): The email address of the customer.
        phone (str, optional): The phone number of the customer. Defaults to None.
        company (str, optional): The company name of the customer. Defaults to None.
        website (str, optional): The website of the customer. Defaults to None.
        fax (str, optional): The fax number of the customer. Defaults to None.

        street_address (str, optional): The street address. Defaults to None.
        extended_address (str, optional): The extended address. Defaults to None.
        locality (str, optional): The city or locality. Defaults to None.
        region (str, optional): The state or region. Defaults to None.
        postal_code (str, optional): The postal code. Defaults to None.
        country (str, optional): The country can be [short_name, oficial_name, code_alpha2, code_alpha3]. Defaults to None.

        cardholder_name (str, optional): The name of the cardholder. Defaults to None.
        number (str, optional): The credit card number. Defaults to None.
        expiration_date (str, optional): The expiration date of the credit card. Defaults to None.
        cvv (str, optional): The CVV of the credit card. Defaults to None.

    Returns:
        braintree.Customer: The newly created customer object.
    """
    customer_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "company": company,
        "website": website,
        "fax": fax,
    }

    if cardholder_name and number and expiration_date and cvv:
        customer_data["credit_card"] = {
            "cardholder_name": cardholder_name,
            "number": number,
            "expiration_date": expiration_date,
            "cvv": cvv,
        }

        if street_address and locality and region and postal_code and country:
            (
                country_short_name,
                country_oficial_name,
                country_code_alpha2,
                country_code_alpha3,
            ) = country_converter(
                short_name=country_arg_type(country, "short_name", True),
                oficial_name=country_arg_type(country, "oficial_name", True),
                code_alpha2=country_arg_type(country, "code_alpha2", True),
                code_alpha3=country_arg_type(country, "code_alpha3", True),
            )

            customer_data["credit_card"]["billing_address"] = {
                "street_address": street_address,
                "extended_address": extended_address,
                "locality": locality,
                "region": region,
                "postal_code": postal_code,
                "country_code_alpha2": country_code_alpha2,
                # "country_code_alpha3": country_code_alpha3,
                "country_name": country_oficial_name,
            }

    result = gateway.customer.create(customer_data)
    return result.customer if result.customer else result
