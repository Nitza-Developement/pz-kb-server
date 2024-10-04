from src.helpers.dates import expired_date
from src.services.bigcommerce.services.customer_fetch import get_by_id as bc_get_by_id
from src.services.bigcommerce.services.stored_instruments_fetch import get_stored_instruments as bc_get_stored_instruments
from src.services.bigcommerce.services.address_fetch import get_by_customer_id as bc_get_addresses_by_id
import braintree


def transform_to_braintree_customer(bigcommerce_customer_id):
    """
    Transforms a BigCommerce customer into a Braintree customer structure.

    Args:
        bigcommerce_customer_id (str): The ID of the customer in BigCommerce.

    Returns:
        braintree.CustomerRequest: A Braintree customer request object.
    """
    bc_customer = bc_get_by_id(bigcommerce_customer_id)
    bc_customer_addresses = bc_get_addresses_by_id(bigcommerce_customer_id)
    bc_customer_stored_instruments = bc_get_stored_instruments(bigcommerce_customer_id)
    
    # Crear el objeto de solicitud de cliente para Braintree
    braintree_customer_request = {
        "first_name" : bc_customer.get("first_name", ""),
        "last_name" : bc_customer.get("last_name", ""),
        "email" : bc_customer.get("email"),
        "fax" : bc_customer.get("", ),
        "phone" : bc_customer.get("phone", ""),
        "company" : bc_customer.get("company", ""),
        "payment_methods": __get_payment_methods_methods(bc_customer_stored_instruments),
        "credit_cards" : __get_credit_cards_methods(bc_customer_stored_instruments),
        "addresses": __get_addresses(bc_customer_addresses),
    }
    return braintree_customer_request
    return braintree.Customer(**braintree_customer_request)

def __get_addresses(bc_customer_addresses):
    """
    Processes BigCommerce customer addresses into a format suitable for Braintree.

    Args:
        bc_customer_addresses (list or dict): A list or dictionary of customer addresses from BigCommerce.

    Returns:
        list or dict: A list of formatted addresses or a single formatted address dictionary for Braintree.
    """
    import country_converter as coco
    cc = coco.CountryConverter()

    def process_address(add):

        country_short_name = add.get("country", "")
        country_code_alpha2 = add.get("country_code", "")
        country_oficial_name = ""
        country_code_alpha3 = ""
        if country_code_alpha2 != "":
            country_short_name = "" if country_short_name == "" else cc.convert(names=country_code_alpha2, to='name_short') 
            country_oficial_name = cc.convert(names=country_code_alpha2, to='name_official')
            country_code_alpha3 = cc.convert(names=country_code_alpha2, to='ISO3')
        elif country_short_name != "":
            country_oficial_name = cc.convert(names=country_short_name, to='name_official')
            country_code_alpha2 = cc.convert(names=country_short_name, to='ISO2')
            country_code_alpha3 = cc.convert(names=country_short_name, to='ISO3')
        
        return {
                "first_name": add.get("first_name", ""),
                "last_name": add.get("last_name", ""),
                "company": add.get("company", ""),
                "country_code_alpha2": country_code_alpha2,
                "country_code_alpha3": country_code_alpha3,
                "country_name": country_oficial_name,
                "postal_code": add.get("postal_code", ""),
                "locality": add.get("city", ""),
                "region": add.get("state_or_province", ""),
                "street_address": add.get("address1", ""),
                "extended_address": add.get("address2", ""),
            }

    if isinstance(bc_customer_addresses, list):
        return [process_address(add) for add in bc_customer_addresses]   
    elif isinstance(bc_customer_addresses, dict):
        add = bc_customer_addresses
        return process_address(add)




def __get_payment_methods_methods(bc_customer_stored_instruments):
    """
    Extracts and processes stored payments methods instruments from BigCommerce for Braintree.

    Args:
        bc_customer_stored_instruments (list): A list of stored payments methods instruments for a BigCommerce customer.

    Returns:
        list: A list of dictionaries representing each payments methods for Braintree.
    """
    return __get_credit_cards_methods(bc_customer_stored_instruments)

def __get_credit_cards_methods(bc_customer_stored_instruments):
    """
    Extracts and processes stored credit card instruments from BigCommerce for Braintree.

    Args:
        bc_customer_stored_instruments (list): A list of stored credit card instruments for a BigCommerce customer.

    Returns:
        list: A list of dictionaries representing each credit card for Braintree.
    """
    
    retorno = []

    for si in bc_customer_stored_instruments:
        _address = si.get("billing_address", {})
        billing_address = __get_addresses(_address)

        retorno += [
            {
                "cardholder_name": f"{si.get('brand', '')} {si.get('stored_card', '')}",
                "bin": si.get("issuer_identification_number", ""),
                "card_type": si.get("brand", ""),
                "token": si.get("token", ""),
                "customer_location": _address.get("country_code", ""),
                "last_4":  si.get("last_4"),
                "default":si.get("is_default", False),
                "expiration_month": si.get("expiry_month"),
                "expiration_year": si.get("expiry_year"),
                # "expired": expired_date(month = si.get("expiry_month"), year = si.get("expiry_year")),
                # "is_expired": expired_date(month = si.get("expiry_month"), year = si.get("expiry_year")),
                "billing_address": billing_address,
            }
        ]
    return retorno