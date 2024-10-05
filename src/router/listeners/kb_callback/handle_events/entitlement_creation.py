def handle_entitlement_creation(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling entitlement creation notification...")
    print("with data : ", data)  # use to debug (comment when done)
