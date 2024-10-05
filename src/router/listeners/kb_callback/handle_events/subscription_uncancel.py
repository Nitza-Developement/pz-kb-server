def handle_subscription_uncancel(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling subscription uncancel notification...")
    print("with data : ", data)  # use to debug (comment when done)
