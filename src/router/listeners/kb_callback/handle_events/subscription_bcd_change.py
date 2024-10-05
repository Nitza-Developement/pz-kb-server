def handle_subscription_bcd_change(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling subscription bcd change notification...")
    print("with data : ", data)  # use to debug (comment when done)
