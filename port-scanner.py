#!/usr/bin/python
#Author: Priyadarshee Kumar
#Date: 22/10/2015
#Port scanner : opensourced with GPL

import sys
import socket

def socket_server(port):
	sock = socket.socket()
	sock.bind(('0.0.0.0', port))
	sock.listen(5)

	while True:
   		conn, addr = sock.accept()
   		print 'Got connection from', addr
   		conn.send('Thank you for connecting')
   		conn.close()


def socket_client(target,port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	status = sock.connect_ex((target, port))
		sock.close()
	except socket.error as err:
		pass
	return status



host = raw_input("Enter the hostname:")
portNumber = int(raw_input("Enter the port:"))

## socket_server should be triggered on the server side only
##socket_server(portNumber) 
## To check all portsby default, extend it with below rather than taking user input portNumber
## for porNumber in range(65535):

if socket_client(host,portNumber) == 0:
	print "Target Host: {} TCP Port: {} status : open.".format(host,portNumber)
else:
	print "Target Host: {} TCP Port: {} status : closed.".format(host,portNumber)
