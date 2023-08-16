# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:30:17 2023

@author: Lucie
"""
import socket
import select

IP   = "192.168.1.26"
PORT1 = 52001
PORT2 = 52002

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("trying to bind socket 1 to ", IP,PORT1)
sock1.bind((IP,PORT1))
print("trying to bind socket 2 to ", IP,PORT2)
sock2.bind((IP,PORT2))
print("sockets binded ! ")

#%%
socketList = [sock1,sock2]
while True:
    ls = select.select(socketList,[],[],1)
    for s in ls[0]:
        data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
        print("#message from:",addr)
        print("#message to :",s.getsockname())
        print("#message :", data,"\n") # depending on getsockname you should adapt # your decoding method
        
#We recieve the data quicker on port 52002 than on port 52001.