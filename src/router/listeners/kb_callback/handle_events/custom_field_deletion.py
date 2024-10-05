def handle_custom_field_deletion(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling custom field deletion notification...")
    print("with data : ", data)  # use to debug (comment when done)
