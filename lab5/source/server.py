#!/usr/bin/env python3
import http.server
import socketserver
import os
import datetime
from urllib.parse import urlparse, parse_qs

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
	def do_GET(self):

		print(self.path)
        
		if self.path == '/':
			self.protocol_version = 'HTTP/1.1'
			self.send_response(200)
			self.send_header("Content-type", "text/html; charset=UTF-8")
			self.end_headers()            
			self.wfile.write(b"Enter values in parameters\n")
		elif 'num1' in self.path and 'num2' in self.path:
			self.protocol_version = 'HTTP/1.1'
			self.send_response(200)
			self.send_header("Content-type", "text/plain; charset=UTF-8")
			self.end_headers()
			query_components = parse_qs(urlparse(self.path).query)
			a = 123
			self.wfile.write(str(a).encode('UTF-8'));
		else:
			super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
