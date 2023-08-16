# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:15:20 2023

@author: Lucie
"""

""" Minimal UDP reciever - IPSA """

import socket
import struct

#%%

IP   = "192.168.1.26"
PORT = 52001

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

print("trying to bind to ", IP,PORT)
sock.bind((IP,PORT))# association de la socket avec IP/PORT
print("waiting for data....")


#%%
while True:
    data,addr=sock.recvfrom(1024) # attente d'un message de lecture

    print("from:",addr)
    print("received message:", data.decode('utf8'))
    
