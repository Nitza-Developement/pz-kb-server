def handle_invoice_creation(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling invoice creation notification...")
    print("with data : ", data)  # use to debug (comment when done)
