def handle_subscription_change(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling subscription change notification...")
    print("with data : ", data)  # use to debug (comment when done)
