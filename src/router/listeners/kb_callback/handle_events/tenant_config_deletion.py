def handle_tenant_config_deletion(event: object):
    """ """
    data = event.get_json()
    print(">>> Handling tenant config deletion notification...")
    print("with data : ", data)  # use to debug (comment when done)
