def handle_broadcast_service(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling broadcast service notification...")
    print("with data : ", data)  # use to debug (comment when done)
