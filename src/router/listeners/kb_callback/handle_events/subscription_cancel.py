def handle_subscription_cancel(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling subscription cancel notification...")
    print("with data : ", data)  # use to debug (comment when done)
