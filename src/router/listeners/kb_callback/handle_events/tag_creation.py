def handle_tag_creation(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling tag creation notification...")
    print("with data : ", data)  # use to debug (comment when done)
