from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('e4b530a664a29846f6d7b7caad5ea4fb390ee60d'.encode('utf-8'))
        return
