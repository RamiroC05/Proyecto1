from http.server import HTTPServer, CGIHTTPRequestHandler
class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/"]
httpd = HTTPServer(("", 8002), Handler)
httpd.serve_forever()