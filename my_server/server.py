from http.server import BaseHTTPRequestHandler,HTTPServer
import time

hostname = "localhost"
port = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.end_headers()
        self.wfile.write(bytes("Hello World","utf-8"))

def startServer():
    webServer = HTTPServer((hostname,port),MyServer)
    print("Server running  on the port 8080")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    
    webServer.server_close()
    print("Server stopped")