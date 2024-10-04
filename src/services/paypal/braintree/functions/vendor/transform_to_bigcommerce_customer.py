import braintree
from ...config import gateway
from src.helpers.country_converter import country_converter


def transform_to_bigcommerce_customer(braintree_customer_id: str):
    """
    Transforms a Braintree customer into a BigCommerce customer structure.

    Args:
        braintree_customer_id (str): The ID of the customer in Braintree.

    Returns:
        dict: A BigCommerce customer structure.
    """
    ppb_customer = gateway.customer.find(braintree_customer_id)
    ppb_customer_addresses = ppb_customer.addresses if ppb_customer.addresses else []
    ppb_customer_payment_methods = (
        ppb_customer.payment_methods if ppb_customer.payment_methods else []
    )
    ppb_customer_credit_cards = (
        ppb_customer.credit_cards if ppb_customer.credit_cards else []
    )

    # Crear el diccionario del cliente de BigCommerce
    bigcommerce_customer = {
        "first_name": ppb_customer.first_name,
        "last_name": ppb_customer.last_name,
        "email": ppb_customer.email,
        "company": ppb_customer.company,
        "phone": ppb_customer.phone,
        "addresses": __get_addresses(ppb_customer_addresses),
        "stored_instruments": __get_stored_instruments(
            ppb_customer_credit_cards, ppb_customer_payment_methods
        ),
    }

    return bigcommerce_customer


def __get_addresses(ppb_customer_addresses):
    """
    Processes PayPal Braintree customer addresses into a format suitable for Bigcommerce.

    Args:
        ppb_customer_addresses (list or dict): A list or dictionary of customer addresses from PayPal Braintree.

    Returns:
        list or dict: A list of formatted addresses or a single formatted address dictionary for Bigcommerce.
    """

    def process_address(add):
        (
            country_short_name,
            country_oficial_name,
            country_code_alpha2,
            country_code_alpha3,
        ) = country_converter(
            oficial_name=add.country_name if add.country_name else None,
            code_alpha2=add.country_code_alpha2 if add.country_code_alpha2 else None,
            code_alpha3=add.country_code_alpha3 if add.country_code_alpha3 else None,
        )

        return {
            "first_name": add.first_name if add.first_name else "Unknown",
            "last_name": add.last_name if add.last_name else "Unknown",
            "company": add.company if add.company else "Unknown",
            "address1": add.street_address if add.street_address else "Unknown",
            "address2": add.extended_address if add.extended_address else "Unknown",
            "postal_code": add.postal_code if add.postal_code else "Unknown",
            "city": add.locality if add.locality else "Unknown",
            "state_or_province": add.region if add.region else "Unknown",
            "country": country_short_name,
            "country_code": country_code_alpha2,
        }

    if isinstance(ppb_customer_addresses, list):
        return [process_address(add) for add in ppb_customer_addresses]
    elif isinstance(ppb_customer_addresses, object):
        add = ppb_customer_addresses
        return process_address(add)


def __get_stored_instruments(ppb_customer_credit_cards, ppb_customer_payment_methods):
    """
    Extracts and processes from stored credit card instruments from Braintree for BigCommerce.

    Args:
        ppb_customer_credit_cards (list): A list of stored credit card instruments from Braintree customer.
        ppb_customer_payment_methods (list): A list of stored payment methods instruments from Braintree customer.

    Returns:
        list: A list of dictionaries representing stored instruments for BigCommerce.
    """
    from src.services.paypal.braintree.const.payment_method_types import (
        INVERTED_CARD_BRANDS as CARD_BRANDS,
    )

    retorno = []
    ppb_customer_stored_instruments = (
        ppb_customer_credit_cards
        if ppb_customer_credit_cards != []
        else ppb_customer_payment_methods
    )

    for si in ppb_customer_stored_instruments:
        _address = si.billing_address if si.billing_address else []
        billing_address = __get_addresses(_address)
        brand = CARD_BRANDS.get(si.card_type) if si.card_type else "Unknown"
        type = ""  # posible values : ['stored_card', 'paypal_account', 'bank_account', 'digital_wallet']
        # currency_code = "USD" if si.billing_address.country_code_alpha2 == "US" else "CAD"

        retorno += [
            {
                "token": si.token if si.token else "Unknown",
                "is_default": si.default if si.default else "Unknown",
                "brand": brand,
                "expiry_month": (
                    si.expiration_month if si.expiration_month else "Unknown"
                ),
                "expiry_year": si.expiration_year if si.expiration_year else "Unknown",
                "issuer_identification_number": si.bin if si.bin else "Unknown",
                "iin": si.bin if si.bin else "Unknown",
                "last_4": si.last_4 if si.last_4 else "Unknown",
                "billing_address": billing_address,
            }
        ]
    return retorno
