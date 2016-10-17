#!/usr/bin/env python

import os
import sys
import socket
import getpass

platform = sys.platform
host = 'localhost'
port = 34567
backlog = 5
size = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to port
s.bind((host,port))
s.listen(backlog)

running = 1
connected = 0
user = 'null'
line = ""
cmd = []
response = ""
logo = """
  __      ___                                       ____                             __
  HHh     HHHh                                      lllll                            TT
   HHh     HHHh                                       lll                       _____tt_____
  jHHj    HHHH                                        lll                       tttttttttttt
  HHH     HHHH                                       _lll                   __       tt
  HHH_____HHHP                                       lll                    II      tt
 jHHHHHHHHHHH      __    _  __    __        ____     lll        ____      ____      tt
 HHHHHHHHHHHH     AAAA__aA  XXx  _XXx   P pPPPPPp    lll      _oOOOOo_    IIII      tt
 HHj     HHHj    aa   AAA     Xx_XX     PPP     Pp  _lll     _O      O     _II     tt
jHH     jHHH    aA     aa    _XXx      PP       PP  lll_     O      _O     II      tt
HHH     HHHH    aA____aA    _X XX__    PP       Pp   lll___  O ____ O     II__     tt_____
HHJ     HHHJ     YAAAA Aa   Xx   XXx  PPp_____pP       llll   *OOOO*    IIIIII      Yttttt
                                      PP PPPPP
                                      PP
                                     PP
                                     PP

"""
print logo
print "Haxploit Terminal v1.0"
print ""
print "User:		%s" % getpass.getuser()
print "Platform: 	%s" % platform

############################################
#          I N I T I A L I Z I N G         #
############################################

def cls():
	if platform == "linux2" or platform == "linux" or platform == "posix":
		os.system("clear")
		os.system("clear")
	elif platform == "win32" or platform == "Win32" or platform == "dos" or platform == "msdos" or platform == "freedos":
		os.system("cls")
	else:
		print ("%s not supported." % platform)

############################################
#            M A I N   L O O P             #
############################################
print ""
while running:
	# Offline commands
	if connected == 0:
		line = raw_input('haxploit# ')
		if line == "":
			line = 'nop'
		cmd = line.split()
		# Handle offline-only commands
		if cmd[0] == 'nop':
			sys.stdout.write("")
		elif cmd[0] == "exit":
			s.close()
			running = 0
			break
		elif cmd[0] == "connect":
			print "Awaiting connection..."
			while not connected:
				# Accept connection
				client, address = s.accept()
				verif_ip = client.recv(32)
				auth_ip = cmd[0]
				# Verify this is the rhost we want
				if verif_ip == auth_ip:
					print "Connection established!"
					print "ID: %s" % user
					# Send user ID
					client.send("_CMD_(CON_ACPT)")
					connected = 1
				else:
					print "Connection to %s denied." % user
					client.send("_CMD_(sleep)")
					client.send("10")
		elif cmd[0] == "cls":
			cls()

