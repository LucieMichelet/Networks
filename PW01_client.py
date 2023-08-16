# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:55:16 2023

@author: Lucie
"""

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024 # read size

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('connecting to '+ TCP_IP + ':' + str(TCP_PORT) +'...')
s.connect((TCP_IP, TCP_PORT))


D = '';

while D != 'fin':   
    data = input("Client : \n").encode('ascii') 
    print('sending data...\n') 
    s.send(data)  
    if data.decode('ascii') == 'fin':
        break
    data = s.recv(BUFFER_SIZE) 
    print("Serveur :\n", data.decode('ascii')) 
    D = data.decode('ascii')
 

s.close()