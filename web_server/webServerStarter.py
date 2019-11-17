import http.server
import socketserver
import json
import cgi

import webServer

def run(port):
    server_class=http.server.HTTPServer
    handler_class=webServer.Server

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print('Starting httpd on port %d...' % (port)) 
    httpd.serve_forever()