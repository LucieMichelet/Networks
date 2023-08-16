#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Minimal UDP sender - IPSA """

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 43210
MESSAGE = "Hello, World!"   # using utf8 char 

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode('utf8'), (UDP_IP, UDP_PORT))
