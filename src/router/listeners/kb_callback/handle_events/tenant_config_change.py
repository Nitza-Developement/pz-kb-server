def handle_tenant_config_change(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling tenant config change notification...")
    print("with data : ", data)  # use to debug (comment when done)
