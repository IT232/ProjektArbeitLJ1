from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from table_content import TableContent
from csv_handler import CSVHandler

hostName = "0.0.0.0"
serverPort = 10021

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open('/templates/table_template.html', 'r') as file:
                content = file.read()
                content.replace("{$tabledata}", TableContent.get_tablecontent())
                print(content)
                self.wfile.write(bytes(content, "utf-8"))

        elif self.path == '/new_record':  
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open('/templates/new_record_template.html', 'r') as file:
                content = file.read()
                self.wfile.write(bytes(content, "utf-8"))

        elif self.path == '/delete_record/':
            key = int(self.path.split("/")[-1])
            CSVHandler.delete_record(key)
            self.send_header("Location", "/")

        else:
            self.send_response(404)  # Page not found
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body><h1>404 Not Found</h1><p>Die Seite wurde nicht gefunden.</p></body></html>")      
       


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