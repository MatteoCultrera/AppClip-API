from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('2F1add9&p1=a95bc7b7&p2=0b2752a2f3faaa85835cfdfc5f3'.encode('utf-8'))
        return
