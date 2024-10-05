def handle_bundle_pause(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling bundle pause notification...")
    print("with data : ", data)  # use to debug (comment when done)
