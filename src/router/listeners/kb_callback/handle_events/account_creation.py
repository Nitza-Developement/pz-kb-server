def handle_account_creation(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling account creation notification...")
    print("with data : ", data)  # use to debug (comment when done)
