from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('3d8c5da2e384bc96835593f5067fa9ab2a1e16f1'.encode('utf-8'))
        return
