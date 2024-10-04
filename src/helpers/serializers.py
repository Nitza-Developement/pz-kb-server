def object_to_dict(obj, seen=None, attributes_to_omit=None):
    """
    Convert a Python object to a dictionary, omitting specified attributes and handling nested objects.

    Parameters:
        obj (object): The object to be converted to a dictionary.
        seen (set, optional): A set to keep track of already processed objects to prevent infinite recursion.
                              This parameter is used internally during recursive calls.
        attributes_to_omit (set or list, optional): A set or list of attribute names to omit from the dictionary.
                                                     Defaults to {"_setattrs"} if not provided.

    Returns:
        dict: A dictionary representation of the object, excluding specified attributes and null values.
              If the object has circular references, it returns None for that object.

    Example:
        >>> customer = Customer()  # Assuming Customer is a defined class with attributes
        >>> attributes_to_omit = {"config, gateway"}
        >>> customer_dict = object_to_dict(customer, attributes_to_omit=attributes_to_omit)
    """
    default_attributes_to_omit = {"_setattrs"}
    if seen is None:
        seen = set()

    # Avoid cycles
    obj_id = id(obj)
    if obj_id in seen:
        return None  # or you can return an empty dict or a marker indicating it was omitted
    seen.add(obj_id)

    # Ensure attributes_to_omit is a set
    if attributes_to_omit is None:
        attributes_to_omit = set()
    elif isinstance(attributes_to_omit, list):
        attributes_to_omit = set(attributes_to_omit)

    # Add default attributes to omit
    attributes_to_omit.update(default_attributes_to_omit)

    if hasattr(obj, "__dict__"):
        dictionary = {}
        for key, value in obj.__dict__.items():
            if key in attributes_to_omit:
                continue  # Omit unwanted attributes

            if isinstance(value, (list, set, tuple)):
                # Filter out null values when constructing the list
                dictionary[key] = [object_to_dict(i, seen, attributes_to_omit) for i in value if i is not None]
            elif hasattr(value, "__dict__"):
                dictionary[key] = object_to_dict(value, seen, attributes_to_omit)
            else:
                # Only add non-null attributes
                if value is not None:
                    dictionary[key] = value
                    
        return dictionary
    return obj  # If it doesn't have __dict__, return the original object

def object_list_to_dict(object_list, attributes_to_omit=None):
    """
    Convert a list of Python objects to a list of dictionaries, omitting specified attributes from each object.

    Parameters:
        object_list (list): A list of objects to be converted to dictionaries.
        attributes_to_omit (set or list, optional): A set or list of attribute names to omit from the dictionaries.
                                                     If not provided, defaults to None.

    Returns:
        list: A list of dictionaries representing the objects, each excluding the specified attributes and
              any null values.

    Example:
        >>> customer_list = [Customer1(), Customer2()]  # Assuming Customer1 and Customer2 are defined classes
        >>> attributes_to_omit = {"config", "gateway", "sensitive_info"}
        >>> customers_dict = object_list_to_dict(customer_list, attributes_to_omit=attributes_to_omit)
    """
    retorno = [object_to_dict(obj, attributes_to_omit=attributes_to_omit) for obj in object_list]
    return retorno