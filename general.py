

def add_cors(resp):
    origin = request.headers.get('Origin', '*')
    headers = request.headers.get(
        'Access-Control-Request-Headers', 'Authorization'
    # )
    # resp.headers['Access-Control-Allow-Origin'] = origin
    # resp.headers['Access-Control-Allow-Credentials'] = 'true'
    # resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT'
    # resp.headers['Access-Control-Allow-Headers'] = headers
    # # set low for debugging
    # if app.debug:
    #     resp.headers['Access-Control-Max-Age'] = '1'
    # return resp
