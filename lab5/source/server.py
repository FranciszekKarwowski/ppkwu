#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import cgi

class web_server(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()

	def do_HEAD(self):
		self._set_headers()

	def do_POST(self):
		ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            
		length = int(self.headers.get('content-length'))
		message = json.loads(self.rfile.read(length))
        
		message['received'] = 'ok'
        
		self._set_headers()
		self.wfile.write(json.dumps(message))

    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
