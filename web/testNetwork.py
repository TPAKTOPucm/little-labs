import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        filename = self.headers['filename']
        with open("С:\\test\\"+filename, 'wb') as f:
            f.write(self.rfile.read(content_length))
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    server_address = ('', 20)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()