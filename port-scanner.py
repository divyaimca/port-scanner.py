#!/usr/bin/python
#Author: Priyadarshee Kumar
#Port scanner

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

help="""
Give the inputs as list here
python port-scanner.py
Enter list of target IPs: ["127.0.0.1","localhost"]
Enter list of ports: [11,22,33,]
"""

target_hosts = input("Enter list of target IPs: ")
target_ports = input("Enter list of ports: ")

def scanner(target,port):
    try:
        sock.connect((target, port))
        return True
    except:
        return False


for _host in target_hosts:
        for portNumber in target_ports:
                if scanner(host,portNumber):
                        print "Target Host: {} TCP Port: {} status : open.".format(_host,portNumber)
                else:
                        print "Target Host: {} TCP Port: {} status : closed.".format(_host,portNumber)
