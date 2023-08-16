# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:48:58 2023

@author: Lucie
"""

import socket

UDP_IP = '10.9.148.125'
UDP_PORT = 56001
BUFFER_SIZE = 1024 

MESSAGE = "Lucie Michelet"   # using utf8 char 

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode('utf8'), (UDP_IP, UDP_PORT))



data,addr=sock.recvfrom(1024) # attente d'un message de lecture

print("from:",addr)
print("received message:", data.decode('utf8'))

sock.sendto(data, (UDP_IP, UDP_PORT))
print("Sent message :", data.decode('ascii'))
print("data sent.")

sock.close()
    
    
    