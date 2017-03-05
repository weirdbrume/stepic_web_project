def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    params = [param for param in environ['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return [params]
