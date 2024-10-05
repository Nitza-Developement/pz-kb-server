def handle_tag_deletion(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling tag deletion notification...")
    print("with data : ", data)  # use to debug (comment when done)
