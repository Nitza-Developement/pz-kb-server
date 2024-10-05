def handle_subscription_phase(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling subscription phase notification...")
    print("with data : ", data)  # use to debug (comment when done)
