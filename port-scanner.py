#!/usr/bin/python
#Author: Priyadarshee Kumar
#Port scanner : opensourced with GPL

import sys
import socket

##Pre_scanner : suppose port is opne in firewall, but service is stopped
## Useful for doing a pre-validation of datacenter before build
##

def pre_scanner(port):
	sock = socket.socket()
	sock.bind(('0.0.0.0', port))
	sock.listen(5)

	while True:
   		conn, addr = sock.accept()
   		print 'Got connection from', addr
   		conn.send('Thank you for connecting')
   		conn.close()


def post_scanner(target,port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	status = sock.connect_ex((target, port))
		sock.close()
	except socket.error as err:
		pass
	return status



host = raw_input("Enter the hostname:")
portNumber = int(raw_input("Enter the port:"))

## pre_scanner should be triggered on the server side only
##pre_scanner(portNumber) 

if post_scanner(host,portNumber) == 0:
	print "Target Host: {} TCP Port: {} status : open.".format(host,portNumber)
else:
	print "Target Host: {} TCP Port: {} status : closed.".format(host,portNumber)
