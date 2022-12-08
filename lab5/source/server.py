#!/usr/bin/env python3
import http.server
import socketserver
import os
import datetime
import requests
from urllib.parse import urlparse, parse_qs

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
	def do_GET(self):

		print(self.path)
        
		headers = {'Accept': 'application/json'}
		r = requests.get(self.path, headers=headers)
		print(f"Response: {r.json()}")
	def do_POST(self):
		r = requests.post(self.path, json={"key":"value"})
		print(f"Request: {r.json()}")

    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
