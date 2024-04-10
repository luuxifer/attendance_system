# Python 3 server example
from base64 import encode
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime
import os

hostName = "192.168.137.33"
serverPort = 8080

class PythonServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(bytes(str(200), "utf-8"))
#        elif self.path == '/log':
#            self.send_response(200)
#            self.send_header("Content-type", "text/plain")
#            self.end_headers()

            #Show log data 
#            self.wfile.write(bytes("LOGDATA", "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(bytes(str(404), "utf-8"))

    def do_POST(self):
        if self.path == "/":
            
            length = int(self.headers['Content-length'])
            str_value = self.rfile.read(length).decode("utf-8")
            value = json.loads(str_value)        
                
            filename = datetime.today().strftime('%Y-%m-%d')
            time = datetime.today().strftime('%H:%M:%S')

            

            os.system("echo %s >> %s" % (time + '\t' + value["data"], filename + '.log'))

            # Response confirm message 
        

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), PythonServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")