def handle_subscription_creation(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling subscription creation notification...")
    print("with data : ", data)  # use to debug (comment when done)
