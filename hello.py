def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    params = [bytes(param, encoding='utf-8') for param in environ['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return iter([params])
