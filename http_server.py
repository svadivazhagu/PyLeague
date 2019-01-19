import http.server
import socketserver
import os

web_dir = os.path.join(os.path.dirname(__file__), 'public')
os.chdir(web_dir)


def do_GET(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    path = self.translate_path(self.path)
    print(path)

    try:
        f = open(path, 'rb')
    except OSError:
        self.send_error(http.server.HTTPStatus.NOT_FOUND, "File not found")
        return None

    if f:
        try:
            self.copyfile(f, self.wfile)
        finally:
            f.close()
   

handler = http.server.SimpleHTTPRequestHandler
handler.do_GET = do_GET

server_address = ('', 8080)
httpd = socketserver.TCPServer(server_address, handler)
httpd.serve_forever()

