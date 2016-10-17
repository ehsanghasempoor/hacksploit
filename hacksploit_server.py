#!/usr/bin/env python

import os
import sys
import socket
import getpass

platform = sys.platform
LHOST = 'localhost'
LPORT = 34567
SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
running = 1
connected = 0
user = getpass.getuser()
line = ""
cmd = []

while running:
	print "Awaiting connection..."
	while not connected:
		#try:
		s.connect((LHOST, LPORT))
		connected == 1
		print "Connection established!"
		s.send(user)
		'''except socket.error, msg:
			connected == 0'''
	while connected:
		line = s.recv(size)
		if line:
			# Handle command
			if line == "/help":
				s.send("""Commands:
	/help		You obviously know how this one works.
	/disconnect	Disconnects you from the server.
	/stop		Stops the server.
	""")
			elif line == "/stop":
				s.send("Are you sure you want to stop the server (Y/n)?")
				choice = s.recv(size)
				if choice.lower() == 'y':
					s.send("_CMD(disconnect)")
					connected = 0
					running = 0
					break
			elif line == "/disconnect":
				s.send("_CMD(disconnect)")
				connected = 0
			else:
				s.send(line)
	s.close()
