def handle_custom_field_creation(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling custom field creation notification...")
    print("with data : ", data)  # use to debug (comment when done)
