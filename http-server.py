from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Login</h1><form method="POST" action="/login">'
                             b'<input type="text" name="username" placeholder="Username"><br>'
                             b'<input type="password" name="password" placeholder="Password"><br>'
                             b'<input type="submit" value="Login"></form></body></html>')
        elif self.path == '/token':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Successful authentication')


    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            username = None
            password = None
            for param in post_data.split('&'):
                key, value = param.split('=')
                if key == 'username':
                    username = urllib.parse.unquote(value)
                elif key == 'password':
                    password = urllib.parse.unquote(value)

            # Login verification logic
            if username == 'username' and password == 'password':
                self.send_response(303)
                self.send_header('Location', '/token')
                self.end_headers()
            else:
                self.send_response(401)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>Login failed</h1></body></html>')


def run():
    server_address = ('', 8000)
    httpd = ThreadingHTTPServer(server_address, MyHandler)
    print('Starting server on http://localhost:8000/')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

