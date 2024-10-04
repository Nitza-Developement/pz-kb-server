import braintree
from ..config import gateway
from .get_customer import get_customer_by_email
from src.helpers.country_converter import country_converter, country_arg_type


def create_billing_address_by_email(
    customer_email,
    street_address,
    extended_address,
    locality,
    region,
    postal_code,
    country,
):
    """
    Creates a new billing address for a customer using their email address.

    Args:
        customer_email (str): The email address of the customer.
        street_address (str): The street address.
        extended_address (str): The street address.
        locality (str): The city or locality.
        region (str): The state or region.
        postal_code (str): The postal code.
        country (str): The country can be [short_name, oficial_name, code_alpha2, code_alpha3].

    Returns:
        braintree.Address: The newly created billing address object.
    """
    customer = get_customer_by_email(customer_email)
    customer_id = customer.id

    return create_billing_address_by_id(
        customer_id, street_address, locality, region, postal_code, country
    )


def create_billing_address_by_id(
    customer_id,
    street_address,
    extended_address,
    locality,
    region,
    postal_code,
    country,
):
    """
    Creates a new billing address for a customer using their customer ID.

    Args:
        customer_id (str): The ID of the customer.
        street_address (str): The street address.
        extended_address (str): The street address.
        locality (str): The city or locality.
        region (str): The state or region.
        postal_code (str): The postal code.
        country (str): The country can be [short_name, oficial_name, code_alpha2, code_alpha3].

    Returns:
        braintree.Address: The newly created billing address object.
    """

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

    result = gateway.address.create(
        {
            "customer_id": customer_id,
            "street_address": street_address,
            "extended_address": extended_address,
            "locality": locality,
            "region": region,
            "postal_code": postal_code,
            "country_code_alpha2": country_code_alpha2,
            # "country_code_alpha3": country_code_alpha3,
            "country_name": country_oficial_name,
        }
    )
    return result.address if result.address else result
