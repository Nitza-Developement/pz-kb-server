def handle_entitlement_cancel(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling entitlement_cancel notification...")
    print("with data : ", data)  # use to debug (comment when done)
