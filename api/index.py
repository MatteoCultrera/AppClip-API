from http.server import BaseHTTPRequestHandler

token='settings'

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(token.encode('utf-8'))
        return
