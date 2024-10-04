import country_converter as coco

cc = coco.CountryConverter()


def country_arg_type(country, type, return_country=False):
    """
    Identify if the country argument matches the specified type.

    Args:
        country (str): The country argument to check.
        type (str): The type to check against. Can be "short_name", "oficial_name", "code_alpha2", or "code_alpha3".
        return_country (bool, optional): If True, return the country argument instead of a boolean. Defaults to False.

    Returns:
        bool or str: True if the country argument matches the specified type, False otherwise. If return_country is True, returns the country argument instead of a boolean.
    """
    if type == "short_name" and len(country) == 2:
        return country if return_country else True

    if type == "oficial_name" and len(country) > 2 and country.isalpha():
        return country if return_country else True

    if type == "code_alpha2" and len(country) == 2:
        return country if return_country else True

    if type == "code_alpha3" and len(country) == 3:
        return country if return_country else True

    return country if return_country else False


def country_converter(
    short_name: str = None,
    oficial_name: str = None,
    code_alpha2: str = None,
    code_alpha3: str = None,
) -> tuple:
    """
    Converts country information between different formats.

    Args:
        short_name (str, optional): The short name of the country. Defaults to None.
        oficial_name (str, optional): The official name of the country. Defaults to None.
        code_alpha2 (str, optional): The ISO 3166-1 alpha-2 code of the country. Defaults to None.
        code_alpha3 (str, optional): The ISO 3166-1 alpha-3 code of the country. Defaults to None.

    Returns:
        tuple: A tuple containing the :
            - short name
            - official name
            - ISO 3166-1 alpha-2 code
            - ISO 3166-1 alpha-3 code
    """

    # fmt: off
    if short_name:
        oficial_name = oficial_name if oficial_name else cc.convert(names=short_name, to="name_official")
        code_alpha2 = code_alpha2 if code_alpha2 else cc.convert(names=short_name, to="ISO2")
        code_alpha3 = code_alpha3 if code_alpha3 else cc.convert(names=short_name, to="ISO3")
    
    elif oficial_name:
        short_name = short_name if short_name else cc.convert(names=oficial_name, to="short_name")
        code_alpha2 = code_alpha2 if code_alpha2 else cc.convert(names=oficial_name, to="ISO2")
        code_alpha3 = code_alpha3 if code_alpha3 else cc.convert(names=oficial_name, to="ISO3")
    
    elif code_alpha2:
        short_name = short_name if short_name else cc.convert(names=code_alpha2, to="short_name")
        oficial_name = oficial_name if oficial_name else cc.convert(names=code_alpha2, to="name_official")
        code_alpha3 = code_alpha3 if code_alpha3 else cc.convert(names=code_alpha2, to="ISO3")
    
    elif code_alpha3:
        short_name = short_name if short_name else cc.convert(names=code_alpha3, to="short_name")
        oficial_name = oficial_name if oficial_name else cc.convert(names=code_alpha3, to="name_official")
        code_alpha2 = code_alpha2 if code_alpha2 else cc.convert(names=code_alpha3, to="ISO2")
    
    else:
        short_name = ""
        oficial_name = ""
        code_alpha2 = ""
        code_alpha3 = ""

    # fmt: on
    return (short_name, oficial_name, code_alpha2, code_alpha3)
