import http.server
import socketserver

PORT = 8080


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("  Cmd: " + self.command)
        print("  Path: " + self.path)

        request = self.path
        if request == "/" or request.startswith("/index"):
            f = open("index.html")
        elif request.startswith("/pink"):
            f = open("pink.html")
        elif request.startswith("/blue"):
            f = open("blue.html")
        else:
            f = open("error.html")

        content = f.read()
        f.close()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))
        return

Handler = TestHandler

# Handler = http.server.SimpleHTTPRequestHandler

# Handler function whenever there is a request
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()
