from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('858eaa2a8c5921a809073c1f907d2f56fc95afdf'.encode('utf-8'))
        return
