# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:57:05 2023

@author: Lucie
"""

import socket
#TCP_IP = '10.9.127.207'
TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024 

sconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("binding to "+ TCP_IP +":"+str(TCP_PORT)," ...")
sconn.bind((TCP_IP, TCP_PORT))

print("Waiting client ...")
sconn.listen(1)
s, addr = sconn.accept()
print('Client connected with address:', addr)

D = '';
while D != 'fin':
    data = s.recv(BUFFER_SIZE) 
    name = socket.gethostname()
    print("\nClient ",name,":\n", data.decode('ascii'))
    if data.decode('ascii') == 'fin':
        break
    data = input("Serveur :\n").encode('ascii')
    s.send(data)  
    print('sending data...\n') 
    D = data.decode('ascii')

s.close()
sconn.close()