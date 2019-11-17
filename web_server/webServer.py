import http.server
import socketserver
import json
import cgi
import os

from datetime import datetime

class Server(http.server.BaseHTTPRequestHandler):
    def write_to_file(self, message):
        INCOMING_REQUESTS_FOLDER = 'INCOMING_REQUESTS'
        if not os.path.exists(INCOMING_REQUESTS_FOLDER):
            try:
                os.mkdir(INCOMING_REQUESTS_FOLDER)
            except OSError:
                print("Creation of the directory %s failed" % INCOMING_REQUESTS_FOLDER)
            else:
                print("Successfully created the directory %s " % INCOMING_REQUESTS_FOLDER)
        
        fileName = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3] + '.txt'
        f = open(INCOMING_REQUESTS_FOLDER + '/' + fileName, 'a+')
        f.write(json.dumps(message))
        f.close()

    def read_from_file(self):
        data = {}
        INCOMING_REQUESTS_FOLDER = 'INCOMING_REQUESTS'
        if os.path.exists(INCOMING_REQUESTS_FOLDER):
            try:
                f = []
                for (dirpath, dirnames, filenames) in os.walk(INCOMING_REQUESTS_FOLDER):
                    f.extend(filenames)
                    break
                if len(f) > 0:
                    f.sort()
                    print(f[len(f) - 1])
                    file = f[len(f) - 1]

                    if '.txt' in file:
                        with open(os.path.join(dirpath, file), 'r') as f:
                            data = json.loads(f.read())

                            print(data)
                else:
                    print("INCOMING_REQUESTS_FOLDER is empty")


            except OSError:
                print("Error reading data - OSError")
            else:
                print("Read file successfully")
        else:
            print("Folder %s is not exist " % INCOMING_REQUESTS_FOLDER)

        return data

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
        print("get request")
        self._set_headers()
        
        message = self.read_from_file()
        
        # message = {'hello': 'world', 'received': 'ok'}
        self.wfile.write(json.dumps(message).encode('utf-8'))
        
    # POST echoes the message adding a JSON field
    def do_POST(self):
        try:
            # ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
            
            # refuse to receive non-json content
            # if ctype != 'application/json':
            #     self.send_response(400)
            #     self.end_headers()
            #     return
                
            # read the message and convert it into a python dictionary
            length = int(self.headers.get('content-length'))
            data = self.rfile.read(length)
            print(data)
            print(data.decode('utf-8'))
            payload_string = data.decode('utf-8')
            message = json.loads(payload_string) if payload_string else None
            print(message)

            # Write JSON to file
            print('recived json: ' + json.dumps(message))
            self.write_to_file(message)
            
            # add a property to the object, just to mess with data
            message['received'] = 'ok'
            
            # send the message back
            self._set_headers()
            self.wfile.write(json.dumps(message).encode('utf-8'))

        except Exception as e:
            print("Error: " + str(e))