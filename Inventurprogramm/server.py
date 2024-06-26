from http.server import BaseHTTPRequestHandler, HTTPServer
from classes.table_content import TableContent
from classes.csv_handler import CSVHandler

hostName = '0.0.0.0'
serverPort = 10021

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html' or self.path == '/?':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('templates/table_template.html', 'r') as file:
                content = file.read()
                content = content.replace('{$tabledata}', TableContent.get_tablecontent())
                self.wfile.write(bytes(content, 'utf-8'))
            

        elif self.path == '/new_record?': 
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('templates/new_record_template.html', 'r') as file:
                content = file.read()
                self.wfile.write(bytes(content, 'utf-8'))


        elif '/delete_record/' in self.path:
            key = str(self.path.split('/')[-1])
            CSVHandler.delete_record(key)
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>404 Not Found</h1><p>Die Seite, die Sie aufrufen wollten, existiert nicht.</p></body></html>')   


    def do_POST(self):
        if self.path == '/save_new_record':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            record_data = dict(item.split('=') for item in post_data.split('&'))
            CSVHandler.add_record([record_data['bezeichnung'], record_data['typ'], record_data['hersteller'], record_data['anschaffungsdatum'], record_data['anschaffungspreis'], record_data['abteilung'], record_data['standort']])
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>404 Not Found</h1><p>Die Seite, die Sie aufrufen wollten, existiert nicht.</p></body></html>')   


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Unsere GUI ist eine Website!")
    print('Server gestartet | http://%s:%s' % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server gestoppt.')