def handle_invoice_adjustment(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling invoice adjustment notification...")
    print("with data : ", data)  # use to debug (comment when done)
