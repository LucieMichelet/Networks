# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:55:49 2023

@author: Lucie
"""



import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024 # read size


data_name = (input("Client's name: \n")+"\r\n").encode('ascii') 


data_string = input("Message : \n")
data_command = input("Command : (len - isdigit - upper) \n")
http_head = ("\r\nPOST /contro_eval.html HTTP/1.1")
r = "\r\nHost:"+str(TCP_IP)+":"+str(TCP_PORT)
r+="\r\nContent-Length:"+str(len(data_string))
r+="\r\nstring="+data_string+"&command="+data_command
http_response = http_head + r

data = data_name + http_response.encode('ascii')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('connecting to '+ TCP_IP + ':' + str(TCP_PORT) +'...')
s.connect((TCP_IP, TCP_PORT))

print('sending data...\n') 
s.send(data)  

    
data = s.recv(BUFFER_SIZE) 
print("Serveur :\n", data.decode('ascii')) 
D = data.decode('ascii')
 

s.close()