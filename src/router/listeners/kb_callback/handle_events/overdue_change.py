def handle_overdue_change(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling overdue change notification...")
    print("with data : ", data)  # use to debug (comment when done)
