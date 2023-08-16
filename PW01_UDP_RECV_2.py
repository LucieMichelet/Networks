#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Minimal UDP reciever - IPSA """

import socket
import struct
import datetime

#%%

IP   = "192.168.1.26"
PORT = 52002

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

print("trying to bind to ", IP,PORT)
sock.bind((IP,PORT))# association de la socket avec IP/PORT
print("waiting for data....")


#%%
while True:
    data,addr=sock.recvfrom(1024) # attente d'un message de lecture
    recieved_bytes = data
    format = 'diiiiffff' # byte array format : d for double , i for int, f for float
    decoded = struct.unpack(format,recieved_bytes[0:40])
    print("from:",addr)
    print("date :",datetime.datetime.fromtimestamp(decoded[0]))
    print(decoded,"\n")


