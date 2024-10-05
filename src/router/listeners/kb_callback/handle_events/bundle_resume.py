def handle_bundle_resume(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling bundle resume notification...")
    print("with data : ", data)  # use to debug (comment when done)
