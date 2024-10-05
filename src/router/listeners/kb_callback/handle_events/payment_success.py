def handle_payment_success(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling payment success notification...")
    print("with data : ", data)  # use to debug (comment when done)
