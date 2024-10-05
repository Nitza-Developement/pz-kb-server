def handle_blocking_state(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling blocking state notification...")
    print("with data : ", data)  # use to debug (comment when done)
