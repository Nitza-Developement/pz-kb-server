def handle_invoice_notification(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling invoice notification notification...")
    print("with data : ", data)  # use to debug (comment when done)
