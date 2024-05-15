from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import index

hostName = "0.0.0.0"
serverPort = 10021

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open('/templates/table_template.html', 'r') as file:
            content = file.read()
            content.replace("{$test}", "<p>Das ist ein Test!</p>")
            print(content)
            self.wfile.write(bytes(content, "utf-8"))

if __name__ == "__main__":       
    print("WTF") 
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")