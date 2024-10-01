from flask import request
from app import app

@app.after_request
def add_cors(response):
    """ Ensure all responses have the CORS headers. This ensures any failures are also accessible
        by the client. """
    return response

    method = request.method
    path = request.path
    response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', '*')
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    response.headers['Access-Control-Allow-Headers'] = request.headers.get('Access-Control-Request-Headers', 'Authorization')

    if not request.method == 'OPTIONS':
        print(f"Incoming request METHOD: {method}, PATH: {path}")
    return response
